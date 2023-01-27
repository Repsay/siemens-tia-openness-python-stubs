# encoding: utf-8
# module Siemens.Engineering calls itself Engineering
# from Siemens.Engineering, Version=16.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.Hmi, Version=16.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=16.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f, Siemens.Engineering.AddIn.Permissions, Version=16.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f, Siemens.Engineering.AddIn.Utilities, Version=16.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations

from Siemens.Engineering.Hmi.Globalization import \
    MultiLingualGraphicComposition
from Siemens.Engineering.HW import (DeviceComposition, DeviceSystemGroup,
                                    DeviceUserGroupComposition,
                                    SubnetComposition, View)
from Siemens.Engineering.HW.Utilities import HardwareUtilityComposition
from Siemens.Engineering.Library import (GlobalLibraryComposition,
                                         ProjectLibrary)
from Siemens.Engineering.Library.MasterCopies import IMasterCopyTarget
from Siemens.Engineering.Settings import TiaPortalSettingsFolderComposition
from System import (AsyncCallback, DateTime, Enum, EventArgs, IAsyncResult,
                    IDisposable, IEquatable, Int64, IServiceProvider,
                    MulticastDelegate, TimeSpan, Type)
from System.Collections import IEnumerable, IList
from System.Globalization import CultureInfo
from System.IO import DirectoryInfo, FileInfo
from System.Security import SecureString

"""The following names are not found in the module: (BoundEvent,
    IApplicationEntryPoint, IInternalApplicationAccess,
    IInternalAssociationAccess, IInternalCompositionAccess,
    IInternalObjectAccess, field#)
"""

from Siemens import IApplicationEntryPoint, IInternalApplicationAccess, IInternalAssociationAccess, IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class AttachingEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ Attaching event arguments """
    @property
    def AccessLevel(self) -> TiaPortalAccessLevel:
        """
        Gets access level argument of the attaching event.

        Get: AccessLevel(self: AttachingEventArgs) -> TiaPortalAccessLevel
        """
        ...

    @property
    def ProcessId(self) -> int:
        """
        Gets attaching process identifier.

        Get: ProcessId(self: AttachingEventArgs) -> int
        """
        ...

    @property
    def ProcessPath(self) -> str:
        """
        Gets attaching event process path.

        Get: ProcessPath(self: AttachingEventArgs) -> str
        """
        ...

    @property
    def TrustAuthority(self) -> TiaPortalTrustAuthority:
        """
        Gets TIA-Portal trust authority of the attaching event.

        Get: TrustAuthority(self: AttachingEventArgs) -> TiaPortalTrustAuthority
        """
        ...

    @property
    def Version(self) -> str:
        """
        Gets version argument of the attaching event.

        Get: Version(self: AttachingEventArgs) -> str
        """
        ...


    def GrantAccess(self): # ->
        """
        GrantAccess(self: AttachingEventArgs)

            Grants permission to the attaching Openness application to attach.
        """
        ...


class ConfirmationChoices(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    The list of possible confirmation choices

    enum (flags) ConfirmationChoices, values: Abort (8), Cancel (256), Ignore (32), No (64), None (0), NoToAll (128), Ok (1), Retry (16), Yes (2), YesToAll (4)
    """
    Abort: ConfirmationChoices = ...
    Cancel: ConfirmationChoices = ...
    Ignore: ConfirmationChoices = ...
    No: ConfirmationChoices = ...
    NoToAll: ConfirmationChoices = ...
    Ok: ConfirmationChoices = ...
    Retry: ConfirmationChoices = ...
    value__ = ...
    Yes: ConfirmationChoices = ...
    YesToAll: ConfirmationChoices = ...


class IEngineeringInstance: # skipped bases: <type 'object'>
    """ IEngineeringInstance """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent of the instance.

        Get: Parent(self: IEngineeringInstance) -> IEngineeringObject
        """
        ...



class IEngineeringCompositionOrObject(IEngineeringInstance): # skipped bases: <type 'object'>
    """ IEngineeringCompositionOrObject """
    pass

class IEngineeringObject(IEngineeringCompositionOrObject): # skipped bases: <type 'IEngineeringInstance'>, <type 'object'>
    """ IEngineeringObject """
    def Create(self, compositionName:str, type:Type, parameters:IEnumerable) -> IEngineeringObject:
        """ Create(self: IEngineeringObject, compositionName: str, type: Type, parameters: IEnumerable[KeyValuePair[str, object]]) -> IEngineeringObject """
        ...

    def GetAttribute(self, name:str) -> object:
        """
        GetAttribute(self: IEngineeringObject, name: str) -> object

            Gets an attribute with the given name.

            name: The name of the attribute to get.

            Returns: The attribute with the given name or a null if not found.
        """
        ...

    def GetAttributeInfos(self) -> IList:
        """
        GetAttributeInfos(self: IEngineeringObject) -> IList[EngineeringAttributeInfo]

            Returns a collection of EngineeringAttributeInfo objects describing the different attributes on this object.

            Returns: A collection of EngineeringAttributeInfo objects describing the different attributes on this object.
        """
        ...

    def GetAttributes(self, names:IEnumerable) -> IList:
        """ GetAttributes(self: IEngineeringObject, names: IEnumerable[str]) -> IList[object] """
        ...

    def GetComposition(self, name:str) -> IEngineeringCompositionOrObject:
        """
        GetComposition(self: IEngineeringObject, name: str) -> IEngineeringCompositionOrObject

            Gets an IEngineeringCompositionOrObject with the given name.

            name: The name of the IEngineeringCompositionOrObject to get.

            Returns: The IEngineeringCompositionOrObject with the given name; otherwise a null.
        """
        ...

    def GetCompositionInfos(self) -> IList:
        """
        GetCompositionInfos(self: IEngineeringObject) -> IList[EngineeringCompositionInfo]

            Gets the list of composition infos available for the object.

            Returns: The list of composition infos available for the object.
        """
        ...

    def GetCreationInfos(self, compositionName:str) -> IList:
        """ GetCreationInfos(self: IEngineeringObject, compositionName: str) -> IList[EngineeringCreationInfo] """
        ...

    def GetInvocationInfos(self) -> IList:
        """
        GetInvocationInfos(self: IEngineeringObject) -> IList[EngineeringInvocationInfo]

            Returns a collection of EngineeringInvocationInfo objects describing the different actions on this object.

            Returns: A collection of EngineeringInvocationInfo objects describing the different actions on this object.
        """
        ...

    def Invoke(self, name:str, parameters:IEnumerable) -> object:
        """ Invoke(self: IEngineeringObject, name: str, parameters: IEnumerable[KeyValuePair[Type, object]]) -> object """
        ...

    def SetAttribute(self, name:str, value:object): # ->
        """
        SetAttribute(self: IEngineeringObject, name: str, value: object)

            Sets an attribute with the given name to the given value value.

            name: The name of the attribute to set with the given value.

            value: The value to set for the attribute with the given name.
        """
        ...

    def SetAttributes(self, attributes:IEnumerable): # ->
        """ SetAttributes(self: IEngineeringObject, attributes: IEnumerable[KeyValuePair[str, object]]) """
        ...


class ConfirmationEventArgs(IInternalObjectAccess, IEngineeringObject, IEquatable, EventArgs): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ The confirmation result. """
    @property
    def Caption(self) -> str:
        """
        Gets the caption of the confirmation.

        Get: Caption(self: ConfirmationEventArgs) -> str
        """
        ...

    @property
    def Choices(self) -> ConfirmationChoices:
        """
        Gets the choices of the confirmation.

        Get: Choices(self: ConfirmationEventArgs) -> ConfirmationChoices
        """
        ...

    @property
    def DetailText(self) -> str:
        """
        Gets the detail text of the confirmation.

        Get: DetailText(self: ConfirmationEventArgs) -> str
        """
        ...

    @property
    def Icon(self) -> ConfirmationIcon:
        """
        Gets the icon.

        Get: Icon(self: ConfirmationEventArgs) -> ConfirmationIcon
        """
        ...

    @property
    def IsHandled(self) -> bool:
        """
        Gets or sets if the confirmation is handled.

        Get: IsHandled(self: ConfirmationEventArgs) -> bool

        Set: IsHandled(self: ConfirmationEventArgs) = value
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ConfirmationEventArgs) -> IEngineeringObject
        """
        ...

    @property
    def Result(self) -> ConfirmationResult:
        """
        Gets or sets the result of the confirmation.

        Get: Result(self: ConfirmationEventArgs) -> ConfirmationResult

        Set: Result(self: ConfirmationEventArgs) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Gets the text of the confirmation.

        Get: Text(self: ConfirmationEventArgs) -> str
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ConfirmationEventArgs) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ConfirmationEventArgs) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class ConfirmationIcon(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    The list of possible confirmation icons

    enum ConfirmationIcon, values: Critical (1), Error (2), General (0)
    """
    Critical: ConfirmationIcon = ...
    Error: ConfirmationIcon = ...
    General: ConfirmationIcon = ...
    value__ = ...


class ConfirmationResult(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    The list of possible confirmation results

    enum ConfirmationResult, values: Abort (3), Cancel (8), Ignore (5), No (6), NoToAll (7), Ok (0), Retry (4), Yes (1), YesToAll (2)
    """
    Abort: ConfirmationResult = ...
    Cancel: ConfirmationResult = ...
    Ignore: ConfirmationResult = ...
    No: ConfirmationResult = ...
    NoToAll: ConfirmationResult = ...
    Ok: ConfirmationResult = ...
    Retry: ConfirmationResult = ...
    value__ = ...
    Yes: ConfirmationResult = ...
    YesToAll: ConfirmationResult = ...


class EngineeringAttributeAccessMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    Flags enum that describes different access levels

    enum (flags) EngineeringAttributeAccessMode, values: None (0), Read (1), ReadWrite (3), Write (2)
    """
    Read: EngineeringAttributeAccessMode = ...
    ReadWrite: EngineeringAttributeAccessMode = ...
    value__ = ...
    Write: EngineeringAttributeAccessMode = ...


class EngineeringAttributeInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ Represents composition information. """
    @property
    def AccessMode(self) -> EngineeringAttributeAccessMode:
        """
        Gets the level of access supported by the attribute.

        Get: AccessMode(self: EngineeringAttributeInfo) -> EngineeringAttributeAccessMode
        """
        ...

    @property
    def CreateRelevance(self) -> EngineeringCreateRelevance:
        """ Get: CreateRelevance(self: EngineeringAttributeInfo) -> EngineeringCreateRelevance """
        ...

    @property
    def Name(self) -> str:
        """
        Gets the name of the attribute.

        Get: Name(self: EngineeringAttributeInfo) -> str
        """
        ...


    def ToString(self) -> str:
        """
        ToString(self: EngineeringAttributeInfo) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...


class EngineeringCompositionInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ Represents composition information. """
    @property
    def Name(self) -> str:
        """
        Gets composition name.

        Get: Name(self: EngineeringCompositionInfo) -> str
        """
        ...


    def ToString(self) -> str:
        """
        ToString(self: EngineeringCompositionInfo) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...


class EngineeringCreateRelevance(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EngineeringCreateRelevance, values: Mandatory (2), None (0), Relevant (1) """
    Mandatory: EngineeringCreateRelevance = ...
    Relevant: EngineeringCreateRelevance = ...
    value__ = ...


class EngineeringCreationInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ Represents the necessary information required to create an object. """
    @property
    def ParameterInfos(self) -> IList:
        """
        The parameters needed to create the object.

        Get: ParameterInfos(self: EngineeringCreationInfo) -> IList[EngineeringCreationParameterInfo]
        """
        ...

    @property
    def Type(self) -> Type:
        """
        The type of the objec that will be created.

        Get: Type(self: EngineeringCreationInfo) -> Type
        """
        ...


    def ToString(self) -> str:
        """
        ToString(self: EngineeringCreationInfo) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...


class EngineeringCreationParameterInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ The parameter info """
    @property
    def IsMandatory(self) -> bool:
        """
        Gets if the parameter is mandatory.

        Get: IsMandatory(self: EngineeringCreationParameterInfo) -> bool
        """
        ...

    @property
    def Name(self) -> str:
        """
        Gets the name of the parameter.

        Get: Name(self: EngineeringCreationParameterInfo) -> str
        """
        ...


    def ToString(self) -> str:
        """
        ToString(self: EngineeringCreationParameterInfo) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...


class EngineeringException(Exception): # skipped bases: <type 'ISerializable'>, <type '_Exception'>, <type 'object'>
    """
    Engineering exception.

    EngineeringException()

    EngineeringException(text: str)

    EngineeringException(text: str, exception: Exception)

    EngineeringException(text: str, *detailTexts: Array[str])
    """
    @property
    def DetailMessageData(self) -> IList:
        """
        Gets the detail message data that describes the current exception.

        Get: DetailMessageData(self: EngineeringException) -> IList[ExceptionMessageData]
        """
        ...

    @property
    def MessageData(self) -> ExceptionMessageData:
        """
        Gets the message data that describes the current exception.

        Get: MessageData(self: EngineeringException) -> ExceptionMessageData
        """
        ...


    SerializeObjectState = ...


class EngineeringTargetInvocationException(EngineeringException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>, <type 'object'>
    """
    Engineering Target Invocation Exception

    EngineeringTargetInvocationException()

    EngineeringTargetInvocationException(text: str)

    EngineeringTargetInvocationException(text: str, exception: Exception)

    EngineeringTargetInvocationException(text: str, *detailTexts: Array[str])
    """
    SerializeObjectState = ...


class EngineeringDelegateInvocationException(EngineeringTargetInvocationException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>, <type 'object'>
    """
    Engineering Delegate Invocation Exception

    EngineeringDelegateInvocationException()

    EngineeringDelegateInvocationException(text: str)

    EngineeringDelegateInvocationException(text: str, exception: Exception)

    EngineeringDelegateInvocationException(text: str, *detailTexts: Array[str])
    """
    SerializeObjectState = ...


class EngineeringInvocationInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ Represents an action info. """
    @property
    def Name(self) -> str:
        """
        Gets the name of the action.

        Get: Name(self: EngineeringInvocationInfo) -> str
        """
        ...

    @property
    def ParameterInfos(self) -> IList:
        """
        Gets the parameter info list.

        Get: ParameterInfos(self: EngineeringInvocationInfo) -> IList[EngineeringInvocationParameterInfo]
        """
        ...


    def ToString(self) -> str:
        """
        ToString(self: EngineeringInvocationInfo) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...


class EngineeringInvocationParameterInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ The parameter info """
    @property
    def Name(self) -> str:
        """
        Gets the name of the parameter.

        Get: Name(self: EngineeringInvocationParameterInfo) -> str
        """
        ...

    @property
    def Type(self) -> Type:
        """
        Gets the type of the parameter.

        Get: Type(self: EngineeringInvocationParameterInfo) -> Type
        """
        ...


    def ToString(self) -> str:
        """
        ToString(self: EngineeringInvocationParameterInfo) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...


class EngineeringNotSupportedException(EngineeringException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>, <type 'object'>
    """
    Engineering Not Supported Exception

    EngineeringNotSupportedException()

    EngineeringNotSupportedException(text: str)

    EngineeringNotSupportedException(text: str, exception: Exception)

    EngineeringNotSupportedException(text: str, *detailTexts: Array[str])
    """
    SerializeObjectState = ...


class EngineeringObjectDisposedException(EngineeringException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>, <type 'object'>
    """
    Engineering Object Disposed Exception

    EngineeringObjectDisposedException()

    EngineeringObjectDisposedException(text: str)

    EngineeringObjectDisposedException(text: str, exception: Exception)

    EngineeringObjectDisposedException(text: str, *detailTexts: Array[str])
    """
    SerializeObjectState = ...


class EngineeringOutOfMemoryException(EngineeringException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>, <type 'object'>
    """
    Engineering Out Of Memory Exception

    EngineeringOutOfMemoryException()

    EngineeringOutOfMemoryException(text: str)

    EngineeringOutOfMemoryException(text: str, exception: Exception)

    EngineeringOutOfMemoryException(text: str, *detailTexts: Array[str])
    """
    SerializeObjectState = ...


class EngineeringRuntimeException(EngineeringException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>, <type 'object'>
    """
    Engineering Runtime Exception

    EngineeringRuntimeException()

    EngineeringRuntimeException(text: str)

    EngineeringRuntimeException(text: str, exception: Exception)

    EngineeringRuntimeException(text: str, *detailTexts: Array[str])
    """
    SerializeObjectState = ...


class EngineeringSecurityException(EngineeringException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>, <type 'object'>
    """
    Engineering Security Exception

    EngineeringSecurityException()

    EngineeringSecurityException(text: str)

    EngineeringSecurityException(text: str, exception: Exception)

    EngineeringSecurityException(text: str, *detailTexts: Array[str])
    """
    SerializeObjectState = ...


class EngineeringServiceInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ Represents an action info. """
    @property
    def Type(self) -> Type:
        """
        Gets the name of the action.

        Get: Type(self: EngineeringServiceInfo) -> Type
        """
        ...


    def ToString(self) -> str:
        """
        ToString(self: EngineeringServiceInfo) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...


class EngineeringUserAbortException(EngineeringTargetInvocationException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>, <type 'object'>
    """
    Engineering User Abort Exception

    EngineeringUserAbortException()

    EngineeringUserAbortException(text: str)

    EngineeringUserAbortException(text: str, exception: Exception)

    EngineeringUserAbortException(text: str, *detailTexts: Array[str])
    """
    SerializeObjectState = ...


class ExceptionMessageData: # skipped bases: <type 'object'>, <type 'object'>
    """ Exception Message Data structure. """
    @property
    def DetailText(self) -> str:
        """
        Gets the detail text.

        Get: DetailText(self: ExceptionMessageData) -> str
        """
        ...

    @property
    def Text(self) -> str:
        """
        Gets the text.

        Get: Text(self: ExceptionMessageData) -> str
        """
        ...


    def ToString(self) -> str:
        """
        ToString(self: ExceptionMessageData) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...


class ExclusiveAccess(IEquatable, IEngineeringObject, IDisposable, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ The class representing an exclusive access session to the TIA Portal """
    @property
    def IsCancellationRequested(self) -> bool:
        """
        Indication if the user has requested a cancellation of the exclusive access session

        Get: IsCancellationRequested(self: ExclusiveAccess) -> bool
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ExclusiveAccess) -> IEngineeringObject
        """
        ...

    @property
    def Text(self) -> str:
        """
        The information to display while an exclusive access session is active

        Get: Text(self: ExclusiveAccess) -> str

        Set: Text(self: ExclusiveAccess) = value
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ExclusiveAccess) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ExclusiveAccess) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def Transaction(self, peristence:ITransactionSupport, undoDescription:str) -> Transaction:
        """
        Transaction(self: ExclusiveAccess, peristence: ITransactionSupport, undoDescription: str) -> Transaction

            Acquires a transaction instance from the active exclusive access session

            peristence: The persistence where the transaction is to be created

            undoDescription: The description of the undo unit that is created for the open transaction

            Returns: Siemens.Engineering.Transaction
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ExportOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    The list of possible scenarios supported by export action parameterization

    enum (flags) ExportOptions, values: None (0), WithDefaults (1), WithReadOnly (2)
    """
    value__ = ...
    WithDefaults: ExportOptions = ...
    WithReadOnly: ExportOptions = ...


class FunctionRightNotFoundException(EngineeringTargetInvocationException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>, <type 'object'>
    """
    Throws when a user who does not have required function right(s) to invoke an Openness API on a protected project

    FunctionRightNotFoundException()

    FunctionRightNotFoundException(text: str)

    FunctionRightNotFoundException(text: str, exception: Exception)

    FunctionRightNotFoundException(text: str, *detailTexts: Array[str])
    """
    SerializeObjectState = ...


class HistoryEntry(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Represents a TIAP project history event """
    @property
    def DateTime(self) -> DateTime:
        """
        The time when the event occurred

        Get: DateTime(self: HistoryEntry) -> DateTime
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: HistoryEntry) -> IEngineeringObject
        """
        ...

    @property
    def Text(self) -> str:
        """
        The event description

        Get: Text(self: HistoryEntry) -> str
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: HistoryEntry) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: HistoryEntry) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class IEngineeringComposition(IEngineeringCompositionOrObject, IEnumerable): # skipped bases: <type 'IEngineeringInstance'>, <type 'object'>
    """ IEngineeringComposition """
    @property
    def Count(self) -> int:
        """
        Gets the number of elements contained within this Composition.

        Get: Count(self: IEngineeringComposition) -> int
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """
        Gets a value indicating whether this Composition was instantiated as ReadOnly.

        Get: IsReadOnly(self: IEngineeringComposition) -> bool
        """
        ...


    def Contains(self, item:IEngineeringObject) -> bool:
        """
        Contains(self: IEngineeringComposition, item: IEngineeringObject) -> bool

            Determines if item is contained within.

            item: The item being sought.

            Returns: true if item is contained within; otherwise false.
        """
        ...

    def Create(self, type:Type, parameters:IEnumerable) -> IEngineeringObject:
        """ Create(self: IEngineeringComposition, type: Type, parameters: IEnumerable[KeyValuePair[str, object]]) -> IEngineeringObject """
        ...

    def GetCreationInfos(self) -> IList:
        """
        GetCreationInfos(self: IEngineeringComposition) -> IList[EngineeringCreationInfo]

            Gets the collection of EngineeringCreateInfo objects describing the different CreateInfos on this object.

            Returns: The collection of EngineeringCreationInfo objects
        """
        ...

    def GetInvocationInfos(self) -> IList:
        """
        GetInvocationInfos(self: IEngineeringComposition) -> IList[EngineeringInvocationInfo]

            Returns a collection of EngineeringInvocationInfo objects describing the different actions on this object.

            Returns: A collection of EngineeringInvocationInfo objects describing the different actions on this object.
        """
        ...

    def IndexOf(self, item:IEngineeringObject) -> int:
        """
        IndexOf(self: IEngineeringComposition, item: IEngineeringObject) -> int

            Searches for item and returns the zero-based index of the first occurrence within.

            item: The item for which an index is sought.

            Returns: The element at the specified item.
        """
        ...

    def Invoke(self, name:str, parameters:IEnumerable) -> object:
        """ Invoke(self: IEngineeringComposition, name: str, parameters: IEnumerable[KeyValuePair[Type, object]]) -> object """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class HistoryEntryComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of HistoryEntries """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: HistoryEntryComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: HistoryEntryComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: HistoryEntryComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[HistoryEntry](enumerable: IEnumerable[HistoryEntry], value: HistoryEntry) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class IEngineeringAssociation(IEngineeringInstance, IEnumerable): # skipped bases: <type 'object'>
    """ IEngineeringAssociation """
    @property
    def Count(self) -> int:
        """
        Gets the number of elements contained within this association.

        Get: Count(self: IEngineeringAssociation) -> int
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """
        Gets a value indicating whether this association was instantiated as ReadOnly.

        Get: IsReadOnly(self: IEngineeringAssociation) -> bool
        """
        ...


    def Contains(self, item:IEngineeringObject) -> bool:
        """
        Contains(self: IEngineeringAssociation, item: IEngineeringObject) -> bool

            Determines if item is contained within.

            item: The item being sought.

            Returns: true if item is contained within; otherwise false.
        """
        ...

    def GetInvocationInfos(self) -> IList:
        """
        GetInvocationInfos(self: IEngineeringAssociation) -> IList[EngineeringInvocationInfo]

            Returns a collection of EngineeringInvocationInfo objects describing the different actions on this object.

            Returns: A collection of EngineeringInvocationInfo objects describing the different actions on this object.
        """
        ...

    def IndexOf(self, item:IEngineeringObject) -> int:
        """
        IndexOf(self: IEngineeringAssociation, item: IEngineeringObject) -> int

            Searches for item and returns the zero-based index of the first occurrence within.

            item: The item for which an index is sought.

            Returns: The element at the specified item.
        """
        ...

    def Invoke(self, name:str, parameters:IEnumerable) -> object:
        """ Invoke(self: IEngineeringAssociation, name: str, parameters: IEnumerable[KeyValuePair[Type, object]]) -> object """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IEngineeringObjectAssociation(IEquatable, IEngineeringAssociation, IInternalAssociationAccess): # skipped bases: <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Associated engineering objects """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent..

        Get: Parent(self: IEngineeringObjectAssociation) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: IEngineeringObjectAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: IEngineeringObjectAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[IEngineeringObject](enumerable: IEnumerable[IEngineeringObject], value: IEngineeringObject) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class IEngineeringRoot(IEngineeringObject): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ IEngineeringRoot """
    pass

class IEngineeringService: # skipped bases: <type 'object'>
    """ The interface representing an engineering service """
    pass

class IEngineeringServiceProvider(IServiceProvider): # skipped bases: <type 'object'>
    """ IEngineeringServiceProvider """
    def GetServiceInfos(self) -> IList:
        """
        GetServiceInfos(self: IEngineeringServiceProvider) -> IList[EngineeringServiceInfo]

            Returns a collection of EngineeringServiceInfo objects describing the different services on this object.

            Returns: A collection of EngineeringServiceInfo objects describing the different services on this object.
        """
        ...


class ImportOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    The list of possible options for Import

    enum (flags) ImportOptions, values: None (0), Override (1)
    """
    Override: ImportOptions = ...
    value__ = ...


class IShowable: # skipped bases: <type 'object'>
    """ Access to Showable attributes """
    def ShowInEditor(self): # ->
        """
        ShowInEditor(self: IShowable)

            Flag to indicate to show in the editor
        """
        ...


class ISystemObject: # skipped bases: <type 'object'>
    """ Access to SystemObject attributes """
    @property
    def IsSystemObject(self) -> bool:
        """
        Indicates if this instance is a system object

        Get: IsSystemObject(self: ISystemObject) -> bool
        """
        ...



class ITransactionSupport: # skipped bases: <type 'object'>
    """ An interface indication that the item supports transactions """
    pass

class Language(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Represents a language that can be enabled in this Project """
    @property
    def Culture(self) -> CultureInfo:
        """
        The culture info object

        Get: Culture(self: Language) -> CultureInfo
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: Language) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: Language) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: Language) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LanguageAssociation(IEquatable, IEngineeringAssociation, IInternalAssociationAccess): # skipped bases: <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Collection of Languages. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent..

        Get: Parent(self: LanguageAssociation) -> IEngineeringObject
        """
        ...


    def Add(self, item:Language): # ->
        """
        Add(self: LanguageAssociation, item: Language)

            Adds an item.

            item: The item to be added.
        """
        ...

    def Find(self, culture:CultureInfo) -> Language:
        """
        Find(self: LanguageAssociation, culture: CultureInfo) -> Language

            Searches for a language by a given culture.

            culture: Language culture

            Returns: Siemens.Engineering.Language
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: LanguageAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Remove(self, item:Language) -> bool:
        """
        Remove(self: LanguageAssociation, item: Language) -> bool

            Removes an item.

            item: The item to be removed.

            Returns: true if the item was removed; otherwise false.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: LanguageAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Language](enumerable: IEnumerable[Language], value: Language) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LanguageComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of Languages """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: LanguageComposition) -> IEngineeringObject
        """
        ...


    def Find(self, culture:CultureInfo) -> Language:
        """
        Find(self: LanguageComposition, culture: CultureInfo) -> Language

            Searches for a language by a given culture.

            culture: Language culture.

            Returns: Siemens.Engineering.Language
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: LanguageComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: LanguageComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Language](enumerable: IEnumerable[Language], value: Language) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LanguageSettings(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Represents a language settings object. """
    @property
    def ActiveLanguages(self) -> LanguageAssociation:
        """
        The collection of active languages.

        Get: ActiveLanguages(self: LanguageSettings) -> LanguageAssociation
        """
        ...

    @property
    def EditingLanguage(self) -> Language:
        """
        Represents an editing language.

        Get: EditingLanguage(self: LanguageSettings) -> Language

        Set: EditingLanguage(self: LanguageSettings) = value
        """
        ...

    @property
    def Languages(self) -> LanguageComposition:
        """
        The collection of all supported languages.

        Get: Languages(self: LanguageSettings) -> LanguageComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: LanguageSettings) -> IEngineeringObject
        """
        ...

    @property
    def ReferenceLanguage(self) -> Language:
        """
        Represents a reference language.

        Get: ReferenceLanguage(self: LanguageSettings) -> Language

        Set: ReferenceLanguage(self: LanguageSettings) = value
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: LanguageSettings) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: LanguageSettings) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MultilingualText(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Represents a String in multiple language translations """
    @property
    def Items(self) -> MultilingualTextItemComposition:
        """
        Contains a collection of multilingual text items.

        Get: Items(self: MultilingualText) -> MultilingualTextItemComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: MultilingualText) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: MultilingualText) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: MultilingualText) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MultilingualTextItem(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Multilingual text item. """
    @property
    def Language(self) -> Language:
        """
        Represents language of this item.

        Get: Language(self: MultilingualTextItem) -> Language
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: MultilingualTextItem) -> IEngineeringObject
        """
        ...

    @property
    def Text(self) -> str:
        """
        Represents text content.

        Get: Text(self: MultilingualTextItem) -> str

        Set: Text(self: MultilingualTextItem) = value
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: MultilingualTextItem) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: MultilingualTextItem) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MultilingualTextItemComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Collection of multilingual text items. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: MultilingualTextItemComposition) -> IEngineeringObject
        """
        ...


    def Find(self, language:Language) -> MultilingualTextItem:
        """
        Find(self: MultilingualTextItemComposition, language: Language) -> MultilingualTextItem

            Searches multilingual text item by language.

            language: Language to find.

            Returns: Siemens.Engineering.MultilingualTextItem
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: MultilingualTextItemComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: MultilingualTextItemComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MultilingualTextItem](enumerable: IEnumerable[MultilingualTextItem], value: MultilingualTextItem) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class NonRecoverableException(Exception): # skipped bases: <type 'ISerializable'>, <type '_Exception'>, <type 'object'>
    """
    Non Recoverable Exception.

    NonRecoverableException()

    NonRecoverableException(text: str)

    NonRecoverableException(text: str, exception: Exception)

    NonRecoverableException(text: str, *detailTexts: Array[str])
    """
    @property
    def DetailMessageData(self) -> IList:
        """
        Gets the detail message data that describes the current exception.

        Get: DetailMessageData(self: NonRecoverableException) -> IList[ExceptionMessageData]
        """
        ...

    @property
    def MessageData(self) -> ExceptionMessageData:
        """
        Gets the message data that describes the current exception.

        Get: MessageData(self: NonRecoverableException) -> ExceptionMessageData
        """
        ...


    SerializeObjectState = ...


class NotificationEventArgs(IInternalObjectAccess, IEngineeringObject, IEquatable, EventArgs): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ The confirmation result. """
    @property
    def Caption(self) -> str:
        """
        Gets the caption of the confirmation.

        Get: Caption(self: NotificationEventArgs) -> str
        """
        ...

    @property
    def DetailText(self) -> str:
        """
        Gets the detail text of the confirmation.

        Get: DetailText(self: NotificationEventArgs) -> str
        """
        ...

    @property
    def Icon(self) -> NotificationIcon:
        """
        Gets the icon.

        Get: Icon(self: NotificationEventArgs) -> NotificationIcon
        """
        ...

    @property
    def IsHandled(self) -> bool:
        """
        Gets or sets if the notification is handled.

        Get: IsHandled(self: NotificationEventArgs) -> bool

        Set: IsHandled(self: NotificationEventArgs) = value
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: NotificationEventArgs) -> IEngineeringObject
        """
        ...

    @property
    def Text(self) -> str:
        """
        Gets the text of the notification.

        Get: Text(self: NotificationEventArgs) -> str
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: NotificationEventArgs) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: NotificationEventArgs) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class NotificationIcon(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    The list of possible notification icons

    enum NotificationIcon, values: Error (3), Information (1), Success (0), Warning (2)
    """
    Error: NotificationIcon = ...
    Information: NotificationIcon = ...
    Success: NotificationIcon = ...
    value__ = ...
    Warning: NotificationIcon = ...


class OpenMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    The modification state of an item being opened.

    enum OpenMode, values: ReadOnly (0), ReadWrite (1)
    """
    ReadOnly: OpenMode = ...
    ReadWrite: OpenMode = ...
    value__ = ...


class Project(IInternalObjectAccess, ITransactionSupport, IEngineeringServiceProvider, IMasterCopyTarget, IEngineeringObject, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IServiceProvider'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Represents a project """
    @property
    def Author(self) -> str:
        """
        Author of the project

        Get: Author(self: Project) -> str
        """
        ...

    @property
    def Comment(self) -> MultilingualText:
        """
        The project's comment

        Get: Comment(self: Project) -> MultilingualText
        """
        ...

    @property
    def Copyright(self) -> str:
        """
        Project copyright information

        Get: Copyright(self: Project) -> str
        """
        ...

    @property
    def CreationTime(self) -> DateTime:
        """
        The creation time of the project

        Get: CreationTime(self: Project) -> DateTime
        """
        ...

    @property
    def DeviceGroups(self) -> DeviceUserGroupComposition:
        """
        Composition of device user groups

        Get: DeviceGroups(self: Project) -> DeviceUserGroupComposition
        """
        ...

    @property
    def Devices(self) -> DeviceComposition:
        """
        Composition of devices

        Get: Devices(self: Project) -> DeviceComposition
        """
        ...

    @property
    def Family(self) -> str:
        """
        The project family

        Get: Family(self: Project) -> str
        """
        ...

    @property
    def Graphics(self) -> MultiLingualGraphicComposition:
        """
        Composition of graphics

        Get: Graphics(self: Project) -> MultiLingualGraphicComposition
        """
        ...

    @property
    def HistoryEntries(self) -> HistoryEntryComposition:
        """
        Contains log of project history events

        Get: HistoryEntries(self: Project) -> HistoryEntryComposition
        """
        ...

    @property
    def HwUtilities(self) -> HardwareUtilityComposition:
        """
        Composition of HW extensions

        Get: HwUtilities(self: Project) -> HardwareUtilityComposition
        """
        ...

    @property
    def IsModified(self) -> bool:
        """
        True if there are unsaved changes to the project

        Get: IsModified(self: Project) -> bool
        """
        ...

    @property
    def IsPrimary(self) -> bool:
        """
        Indicates whether the project is the primary project

        Get: IsPrimary(self: Project) -> bool
        """
        ...

    @property
    def IsSimulationDuringBlockCompilationEnabled(self) -> bool:
        """
        To indicate whether Support for Simulation during block compilation is enabled for the project

        Get: IsSimulationDuringBlockCompilationEnabled(self: Project) -> bool

        Set: IsSimulationDuringBlockCompilationEnabled(self: Project) = value
        """
        ...

    @property
    def LanguageSettings(self) -> LanguageSettings:
        """
        Project's language settings.

        Get: LanguageSettings(self: Project) -> LanguageSettings
        """
        ...

    @property
    def LastModified(self) -> DateTime:
        """
        The time of the last modification of the project

        Get: LastModified(self: Project) -> DateTime
        """
        ...

    @property
    def LastModifiedBy(self) -> str:
        """
        The project was last modified by this user.

        Get: LastModifiedBy(self: Project) -> str
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the project

        Get: Name(self: Project) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: Project) -> IEngineeringObject
        """
        ...

    @property
    def Path(self) -> FileInfo:
        """
        The path to this project

        Get: Path(self: Project) -> FileInfo
        """
        ...

    @property
    def ProjectLibrary(self) -> ProjectLibrary:
        """
        Gets the project library

        Get: ProjectLibrary(self: Project) -> ProjectLibrary
        """
        ...

    @property
    def Size(self) -> Int64:
        """
        The size of the project in KB

        Get: Size(self: Project) -> Int64
        """
        ...

    @property
    def Subnets(self) -> SubnetComposition:
        """
        Composition of Subnets

        Get: Subnets(self: Project) -> SubnetComposition
        """
        ...

    @property
    def UngroupedDevicesGroup(self) -> DeviceSystemGroup:
        """
        Gets the devices system group

        Get: UngroupedDevicesGroup(self: Project) -> DeviceSystemGroup
        """
        ...

    @property
    def UsedProducts(self) -> UsedProductComposition:
        """
        Composition of used products in the project

        Get: UsedProducts(self: Project) -> UsedProductComposition
        """
        ...

    @property
    def Version(self) -> str:
        """
        The version of this project

        Get: Version(self: Project) -> str
        """
        ...


    def Archive(self, targetDirectory:DirectoryInfo, targetName:str, archivationMode:ProjectArchivationMode): # ->
        """
        Archive(self: Project, targetDirectory: DirectoryInfo, targetName: str, archivationMode: ProjectArchivationMode)

            Archives the current project

            targetDirectory: Directory where the project to be archived

            targetName: File name for the archived file

            archivationMode: Archivation mode
        """
        ...

    def Close(self): # ->
        """
        Close(self: Project)

            Closes the project
        """
        ...

    def ExportProjectTexts(self, path:FileInfo, sourceLanguage:CultureInfo, targetLanguage:CultureInfo): # ->
        """
        ExportProjectTexts(self: Project, path: FileInfo, sourceLanguage: CultureInfo, targetLanguage: CultureInfo)

            Export project text to an xlsx file

            path: Path to the xlsx file

            sourceLanguage: The source language to use for the export of project texts

            targetLanguage: The target language to use for the export of project texts
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: Project) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ImportProjectTexts(self, path:FileInfo, updateSourceLanguage:bool) -> ProjectTextResult:
        """
        ImportProjectTexts(self: Project, path: FileInfo, updateSourceLanguage: bool) -> ProjectTextResult

            Import project text from an import file

            path: Path to the xlsx file

            updateSourceLanguage: True if the source language is to be updated

            Returns: Siemens.Engineering.ProjectTextResult
        """
        ...

    def Save(self): # ->
        """
        Save(self: Project)

            Saves all changes of the project
        """
        ...

    def SaveAs(self, targetFolderPath:DirectoryInfo): # ->
        """
        SaveAs(self: Project, targetFolderPath: DirectoryInfo)

            Saves all changes of the project to a new location.

            targetFolderPath: Target location for newly SavedAs project
        """
        ...

    def ShowHwEditor(self, view:View): # ->
        """
        ShowHwEditor(self: Project, view: View)

            Show the indicated item in the HW editor of the attached TIA Portal

            view: Which view of the HW editor to show
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: Project) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ProjectArchivationMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    Archivation mode

    enum ProjectArchivationMode, values: Compressed (1), DiscardRestorableData (2), DiscardRestorableDataAndCompressed (3), None (0)
    """
    Compressed: ProjectArchivationMode = ...
    DiscardRestorableData: ProjectArchivationMode = ...
    DiscardRestorableDataAndCompressed: ProjectArchivationMode = ...
    value__ = ...


class ProjectComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of Projects """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: ProjectComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ProjectComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Open(self, path:FileInfo, umacDelegate:UmacDelegate = ..., projectOpenMode:ProjectOpenMode = ...) -> Project:
        """
        Open(self: ProjectComposition, path: FileInfo) -> Project

            Open Action

            path: Path to the Tia Portal project file

            Returns: Siemens.Engineering.Project

        Open(self: ProjectComposition, path: FileInfo, umacDelegate: UmacDelegate) -> Project

            Open project and authenticate with UMAC if necessary.

            path: Path to the Tia Portal project file.

            umacDelegate: Delegate that will be called if user authentication with UMAC is required.

            Returns: Siemens.Engineering.Project

        Open(self: ProjectComposition, path: FileInfo, umacDelegate: UmacDelegate, projectOpenMode: ProjectOpenMode) -> Project

            Open project and authenticate with UMAC if necessary.

            path: Path to the Tia Portal project file.

            umacDelegate: Delegate that will be called if user authentication with UMAC is required.

            projectOpenMode: Open mode.

            Returns: Siemens.Engineering.Project
        """
        ...

    def OpenWithUpgrade(self, path:FileInfo, umacDelegate:UmacDelegate = ..., projectOpenMode:ProjectOpenMode = ...) -> Project:
        """
        OpenWithUpgrade(self: ProjectComposition, path: FileInfo) -> Project

            Open Action with project update is necessary

            path: Path to the Tia Portal project file

            Returns: Siemens.Engineering.Project

        OpenWithUpgrade(self: ProjectComposition, path: FileInfo, umacDelegate: UmacDelegate) -> Project

            Open Action with project update and authenticate with UMAC if necessary.

            path: Path to the Tia Portal project file.

            umacDelegate: Delegate that will be called if user authentication with UMAC is required.

            Returns: Siemens.Engineering.Project

        OpenWithUpgrade(self: ProjectComposition, path: FileInfo, umacDelegate: UmacDelegate, projectOpenMode: ProjectOpenMode) -> Project

            Open Action with project update and authenticate with UMAC if necessary.

            path: Path to the Tia Portal project file.

            umacDelegate: Delegate that will be called if user authentication with UMAC is required.

            projectOpenMode: Open mode.

            Returns: Siemens.Engineering.Project
        """
        ...

    def Retrieve(self, sourcePath:FileInfo, targetDirectory:DirectoryInfo, umacDelegate:UmacDelegate = ..., projectOpenMode:ProjectOpenMode = ...) -> Project:
        """
        Retrieve(self: ProjectComposition, sourcePath: FileInfo, targetDirectory: DirectoryInfo) -> Project

            Retrieves an archived project

            sourcePath: The path of the archived project file

            targetDirectory: The path to the folder where project would be retrieved.

            Returns: Siemens.Engineering.Project

        Retrieve(self: ProjectComposition, sourcePath: FileInfo, targetDirectory: DirectoryInfo, umacDelegate: UmacDelegate) -> Project

            Retrieves an archived project with UMAC

            sourcePath: The path of the archived project file

            targetDirectory: The path to the folder where project would be retrieved.

            umacDelegate: Delegate will be called if the project is protected and user authentication is required. If the project is not protected, then null can be passed as parameter

            Returns: Siemens.Engineering.Project

        Retrieve(self: ProjectComposition, sourcePath: FileInfo, targetDirectory: DirectoryInfo, umacDelegate: UmacDelegate, projectOpenMode: ProjectOpenMode) -> Project

            Retrieves an archived project with UMAC and opens the project as Primary or Secorndary

            sourcePath: The path of the archived project file

            targetDirectory: The path to the folder where project would be retrieved.

            umacDelegate: Delegate will be called if the project is protected and user authentication is required.If the project is not protected, then null can be passed as parameter

            projectOpenMode: Project Open Mode

            Returns: Siemens.Engineering.Project
        """
        ...

    def RetrieveWithUpgrade(self, sourcePath:FileInfo, targetDirectory:DirectoryInfo, umacDelegate:UmacDelegate = ..., projectOpenMode:ProjectOpenMode = ...) -> Project:
        """
        RetrieveWithUpgrade(self: ProjectComposition, sourcePath: FileInfo, targetDirectory: DirectoryInfo) -> Project

            Retrieves a project from an archive and upgrades it to the current version

            sourcePath: The path of the archived project file

            targetDirectory: The path to the folder where project would be retrieved.

            Returns: Siemens.Engineering.Project

        RetrieveWithUpgrade(self: ProjectComposition, sourcePath: FileInfo, targetDirectory: DirectoryInfo, umacDelegate: UmacDelegate) -> Project

            Retrieves a project from an archive and upgrades it to the current version with umac

            sourcePath: The path of the archived project file

            targetDirectory: The path to the folder where project would be retrieved.

            umacDelegate: Delegate will be called if the project is protected and user authentication is required.If the project is not protected, then null can be passed as parameter

            Returns: Siemens.Engineering.Project

        RetrieveWithUpgrade(self: ProjectComposition, sourcePath: FileInfo, targetDirectory: DirectoryInfo, umacDelegate: UmacDelegate, projectOpenMode: ProjectOpenMode) -> Project

            Retrieves a project from an archive and upgrades it to the current version

            sourcePath: The path of the archived project file

            targetDirectory: The path to the folder where project would be retrieved.

            umacDelegate: Delegate will be called if the project is protected and user authentication is required.If the project is not protected, then null can be passed as parameter

            projectOpenMode: Project Open Mode

            Returns: Siemens.Engineering.Project
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ProjectComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Project](enumerable: IEnumerable[Project], value: Project) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ProjectOpenMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    Project open mode

    enum ProjectOpenMode, values: Primary (0), Secondary (1)
    """
    Primary: ProjectOpenMode = ...
    Secondary: ProjectOpenMode = ...
    value__ = ...


class ProjectTextResult(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Represents a project text result """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ProjectTextResult) -> IEngineeringObject
        """
        ...

    @property
    def Path(self) -> FileInfo:
        """
        Path to a text result

        Get: Path(self: ProjectTextResult) -> FileInfo
        """
        ...

    @property
    def State(self) -> ProjectTextResultState:
        """
        Final state of the project text result

        Get: State(self: ProjectTextResult) -> ProjectTextResultState
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ProjectTextResult) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ProjectTextResult) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ProjectTextResultState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    The state of project text result

    enum ProjectTextResultState, values: Error (2), Info (0), Warning (1)
    """
    Error: ProjectTextResultState = ...
    Info: ProjectTextResultState = ...
    value__ = ...
    Warning: ProjectTextResultState = ...


class TiaPortal(IInternalApplicationAccess, IDisposable, IEngineeringServiceProvider, IApplicationEntryPoint, IEngineeringRoot, IEquatable): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IServiceProvider'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ TIAPortal. """
    @property
    def GlobalLibraries(self) -> GlobalLibraryComposition:
        """
        Composition of global libraries

        Get: GlobalLibraries(self: TiaPortal) -> GlobalLibraryComposition
        """
        ...

    @property
    def Projects(self) -> ProjectComposition:
        """
        Composition of open projects

        Get: Projects(self: TiaPortal) -> ProjectComposition
        """
        ...

    @property
    def SettingsFolders(self) -> TiaPortalSettingsFolderComposition:
        """
        The settings of the TIA portal

        Get: SettingsFolders(self: TiaPortal) -> TiaPortalSettingsFolderComposition
        """
        ...


    def ExclusiveAccess(self, text:str = ...) -> ExclusiveAccess:
        """
        ExclusiveAccess(self: TiaPortal) -> ExclusiveAccess

            Acquire an exclusive access session to the TIA Portal

            Returns: Siemens.Engineering.ExclusiveAccess

        ExclusiveAccess(self: TiaPortal, text: str) -> ExclusiveAccess

            Acquire an exclusive access session to the TIA Portal

            text: The text to present to the interactive user while an exclusive access session is active

            Returns: Siemens.Engineering.ExclusiveAccess
        """
        ...

    def GetCurrentProcess(self) -> TiaPortalProcess:
        """
        GetCurrentProcess(self: TiaPortal) -> TiaPortalProcess

            Gets the information of connected TIA-Portal.

            Returns: The connected TIA-Portal.
        """
        ...

    Confirmation = ...
    Disposed = ...
    Notification = ...


class TiaPortalAccessLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    The access level of the associated TIA Portal

    enum (flags) TiaPortalAccessLevel, values: Elevated (256), Modify (4), NoLicense (1), None (0), Pilot (32), Published (8), Trusted (2)
    """
    Elevated: TiaPortalAccessLevel = ...
    Modify: TiaPortalAccessLevel = ...
    NoLicense: TiaPortalAccessLevel = ...
    Pilot: TiaPortalAccessLevel = ...
    Published: TiaPortalAccessLevel = ...
    Trusted: TiaPortalAccessLevel = ...
    value__ = ...


class TiaPortalMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    Mode how to start the TIA-Portal.

    enum TiaPortalMode, values: WithoutUserInterface (0), WithUserInterface (1)
    """
    value__ = ...
    WithoutUserInterface: TiaPortalMode = ...
    WithUserInterface: TiaPortalMode = ...


class TiaPortalProcess(IDisposable): # skipped bases: <type 'object'>
    """ TiaPortalProcess """
    @property
    def AcquisitionTime(self) -> DateTime:
        """
        Gets the time when the TiaPortalProcess object was acquired.

        Get: AcquisitionTime(self: TiaPortalProcess) -> DateTime
        """
        ...

    @property
    def AttachedSessions(self) -> IList:
        """
        Gets a list of other process attached to this same TIA-Portal process.

        Get: AttachedSessions(self: TiaPortalProcess) -> IList[TiaPortalSession]
        """
        ...

    @property
    def Id(self) -> int:
        """
        Gets the Process ID of the TIA Portal.

        Get: Id(self: TiaPortalProcess) -> int
        """
        ...

    @property
    def InstalledSoftware(self) -> IList:
        """
        Gets a list of installed software of the TIA-Portal process.

        Get: InstalledSoftware(self: TiaPortalProcess) -> IList[TiaPortalProduct]
        """
        ...

    @property
    def Mode(self) -> TiaPortalMode:
        """
        Gets the mode of the attached TIA-Portal.

        Get: Mode(self: TiaPortalProcess) -> TiaPortalMode
        """
        ...

    @property
    def Path(self) -> FileInfo:
        """
        The path to the executable of the TIA Portal.

        Get: Path(self: TiaPortalProcess) -> FileInfo
        """
        ...

    @property
    def ProjectPath(self) -> FileInfo:
        """
        Gets the path of any project currently open in the attached TIA_Portal.

        Get: ProjectPath(self: TiaPortalProcess) -> FileInfo
        """
        ...



class TiaPortalProduct: # skipped bases: <type 'object'>, <type 'object'>
    """ TiaPortalProduct """
    @property
    def Name(self) -> str:
        """
        Gets the product name.

        Get: Name(self: TiaPortalProduct) -> str
        """
        ...

    @property
    def Options(self) -> IList:
        """
        Gets a list of installed options of the TIA-Portal process.

        Get: Options(self: TiaPortalProduct) -> IList[TiaPortalProduct]
        """
        ...

    @property
    def Version(self) -> str:
        """
        Gets the product version.

        Get: Version(self: TiaPortalProduct) -> str
        """
        ...



class TiaPortalSession(IDisposable): # skipped bases: <type 'object'>
    """ TiaPortalSession """
    @property
    def AccessLevel(self) -> TiaPortalAccessLevel:
        """
        Gets the access level of the process.

        Get: AccessLevel(self: TiaPortalSession) -> TiaPortalAccessLevel
        """
        ...

    @property
    def AttachTime(self) -> DateTime:
        """
        Gets the attached session date and time.

        Get: AttachTime(self: TiaPortalSession) -> DateTime
        """
        ...

    @property
    def Id(self) -> int:
        """
        Gets the attached session identifier.

        Get: Id(self: TiaPortalSession) -> int
        """
        ...

    @property
    def IsActive(self) -> bool:
        """
        Gets a boolean value describing whether the TIA Portal is in  the middle of processing a call from this session.

        Get: IsActive(self: TiaPortalSession) -> bool
        """
        ...

    @property
    def ProcessId(self) -> int:
        """
        Gets the attached session process identifier.

        Get: ProcessId(self: TiaPortalSession) -> int
        """
        ...

    @property
    def ProcessPath(self) -> FileInfo:
        """
        Gets the path to where the executable of the attached process lives.

        Get: ProcessPath(self: TiaPortalSession) -> FileInfo
        """
        ...

    @property
    def TrustAuthority(self) -> TiaPortalTrustAuthority:
        """
        Indicates if the current session was started by a process that was signed, and if so, if it is an Openness certificate or not.

        Get: TrustAuthority(self: TiaPortalSession) -> TiaPortalTrustAuthority
        """
        ...

    @property
    def UtilizationTime(self) -> TimeSpan:
        """
        Gets time the process has spent actively using the TIA Portal.

        Get: UtilizationTime(self: TiaPortalSession) -> TimeSpan
        """
        ...

    @property
    def Version(self) -> str:
        """
        Gets the attached session version.

        Get: Version(self: TiaPortalSession) -> str
        """
        ...



class TiaPortalTrustAuthority(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    The trust authority of the associated TIA Portal

    enum (flags) TiaPortalTrustAuthority, values: Certified (2), CertifiedWithExpiration (256), FeatureTokens (512), None (0), Signed (1)
    """
    Certified: TiaPortalTrustAuthority = ...
    CertifiedWithExpiration: TiaPortalTrustAuthority = ...
    FeatureTokens: TiaPortalTrustAuthority = ...
    Signed: TiaPortalTrustAuthority = ...
    value__ = ...


class Transaction(IEquatable, IEngineeringObject, IDisposable, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Represents an open transaction in a persistence (i.e. single unit of work) """
    @property
    def CanCommit(self) -> bool:
        """
        Indicates if the transaction can be committed.

        Get: CanCommit(self: Transaction) -> bool
        """
        ...

    @property
    def CommitRequested(self) -> bool:
        """
        Indicates if a commit has been requested.

        Get: CommitRequested(self: Transaction) -> bool
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: Transaction) -> IEngineeringObject
        """
        ...


    def CommitOnDispose(self): # ->
        """
        CommitOnDispose(self: Transaction)

            Commit transaction when disposed
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: Transaction) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: Transaction) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UmacCredentials(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Object that is used to authenticate user. """
    @property
    def Name(self) -> str:
        """
        User name.

        Get: Name(self: UmacCredentials) -> str

        Set: Name(self: UmacCredentials) = value
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: UmacCredentials) -> IEngineeringObject
        """
        ...

    @property
    def Type(self) -> UmacUserType:
        """
        User Type

        Get: Type(self: UmacCredentials) -> UmacUserType

        Set: Type(self: UmacCredentials) = value
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UmacCredentials) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def SetPassword(self, password:SecureString): # ->
        """
        SetPassword(self: UmacCredentials, password: SecureString)

            Set password.

            password: Password
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UmacCredentials) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UmacDelegate(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """
    The delegate that will called back for user credetials if project is protected.

    UmacDelegate(object: object, method: IntPtr)
    """
    def BeginInvoke(self, umacCredentials:UmacCredentials, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: UmacDelegate, umacCredentials: UmacCredentials, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # ->
        """ EndInvoke(self: UmacDelegate, result: IAsyncResult) """
        ...

    def Invoke(self, umacCredentials:UmacCredentials): # ->
        """ Invoke(self: UmacDelegate, umacCredentials: UmacCredentials) """
        ...


class UmacUserType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    User type.

    enum UmacUserType, values: Global (1), Project (0)
    """
    Global: UmacUserType = ...
    Project: UmacUserType = ...
    value__ = ...


class UsedProduct(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Represents a product used by a project """
    @property
    def Name(self) -> str:
        """
        The name of the used product

        Get: Name(self: UsedProduct) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: UsedProduct) -> IEngineeringObject
        """
        ...

    @property
    def Version(self) -> str:
        """
        The product version

        Get: Version(self: UsedProduct) -> str
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UsedProduct) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UsedProduct) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UsedProductComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of UsedProducts """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: UsedProductComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UsedProductComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UsedProductComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[UsedProduct](enumerable: IEnumerable[UsedProduct], value: UsedProduct) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


# variables with complex values
