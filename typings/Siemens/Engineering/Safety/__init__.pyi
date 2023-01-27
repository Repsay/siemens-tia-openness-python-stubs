# encoding: utf-8
# module Siemens.Engineering.Safety calls itself Safety
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringComposition, IEngineeringObject,
    IEngineeringService)

from System import Enum, IEquatable, UInt16, UInt64

from System.Collections import IList

from System.IO import FileInfo

from System.Security import SecureString

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess, field#)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class AssignmentOfBlockNumbers(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Enables access to attributes for configuring block number ranges of system-generated safety blocks. """
    @property
    def FromDB(self) -> UInt16:
        """
        Gets or sets the "from DB" fixed range block number.

        Get: FromDB(self: AssignmentOfBlockNumbers) -> UInt16

        Set: FromDB(self: AssignmentOfBlockNumbers) = value
        """
        ...

    @property
    def FromFB(self) -> UInt16:
        """
        Gets or sets the "from FB" fixed range block number.

        Get: FromFB(self: AssignmentOfBlockNumbers) -> UInt16

        Set: FromFB(self: AssignmentOfBlockNumbers) = value
        """
        ...

    @property
    def FromFC(self) -> UInt16:
        """
        Gets or sets the "from FC" fixed range block number.

        Get: FromFC(self: AssignmentOfBlockNumbers) -> UInt16

        Set: FromFC(self: AssignmentOfBlockNumbers) = value
        """
        ...

    @property
    def ManagementMode(self) -> BlockNumbersManagementMode:
        """
        Gets or sets indicating whether block numbers are system generated or manually assigned.

        Get: ManagementMode(self: AssignmentOfBlockNumbers) -> BlockNumbersManagementMode

        Set: ManagementMode(self: AssignmentOfBlockNumbers) = value
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: AssignmentOfBlockNumbers) -> IEngineeringObject
        """
        ...

    @property
    def ToDB(self) -> UInt16:
        """
        Gets or sets the "to DB" fixed range block number.

        Get: ToDB(self: AssignmentOfBlockNumbers) -> UInt16

        Set: ToDB(self: AssignmentOfBlockNumbers) = value
        """
        ...

    @property
    def ToFB(self) -> UInt16:
        """
        Gets or sets the "from FB" fixed range block number.

        Get: ToFB(self: AssignmentOfBlockNumbers) -> UInt16

        Set: ToFB(self: AssignmentOfBlockNumbers) = value
        """
        ...

    @property
    def ToFC(self) -> UInt16:
        """
        Gets or sets the "to FC" fixed range block number.

        Get: ToFC(self: AssignmentOfBlockNumbers) -> UInt16

        Set: ToFC(self: AssignmentOfBlockNumbers) = value
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: AssignmentOfBlockNumbers) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: AssignmentOfBlockNumbers) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class BlockNumbersManagementMode(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Defines modes for managing the number blocks of F-system blocks

    enum BlockNumbersManagementMode, values: FixedRange (1), FSystemManaged (0)
    """
    FixedRange: BlockNumbersManagementMode = ...
    FSystemManaged: BlockNumbersManagementMode = ...
    value__ = ...


class GlobalSettings(IEquatable, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'object'>
    """ GlobalSettings """
    def GetHashCode(self) -> int:
        """
        GetHashCode(self: GlobalSettings) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def SafetyModificationsPossible(self, safetyModificationsPossible:bool = ...): # ->
        """
        SafetyModificationsPossible(self: GlobalSettings) -> bool

            Query whether SafetyModifications are possible.

            Returns: System.Boolean

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

    def UsernameForFChangeHistory(self, usernameForFChangeHistory:str = ...): # ->
        """
        UsernameForFChangeHistory(self: GlobalSettings) -> str

            Retrieves the username to be used for F-change history entries

            Returns: System.String

        UsernameForFChangeHistory(self: GlobalSettings, usernameForFChangeHistory: str)

            Sets the username to be used for F-change history entries

            usernameForFChangeHistory: Username to be used for F-change history entries
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class RuntimeGroup(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Enables access to information and methods regarding the Runtime Groups of the Safety program. """
    @property
    def FOBEventClass(self) -> str:
        """
        The Event class of the Fail-safe organization block

        Get: FOBEventClass(self: RuntimeGroup) -> str
        """
        ...

    @property
    def FOBName(self) -> str:
        """
        The name of the Fail-safe organization block

        Get: FOBName(self: RuntimeGroup) -> str
        """
        ...

    @property
    def InfoDbName(self) -> str:
        """
        The name of the Runtime Groups Information DB Block

        Get: InfoDbName(self: RuntimeGroup) -> str
        """
        ...

    @property
    def MainSafetyBlockIDbName(self) -> str:
        """
        The name of the main safety's IDb block

        Get: MainSafetyBlockIDbName(self: RuntimeGroup) -> str
        """
        ...

    @property
    def MainSafetyBlockName(self) -> str:
        """
        The name of the main safety block

        Get: MainSafetyBlockName(self: RuntimeGroup) -> str
        """
        ...

    @property
    def MaximumCycleTime(self) -> int:
        """
        The Maximum Cycle Time of the Runtime Group

        Get: MaximumCycleTime(self: RuntimeGroup) -> int

        Set: MaximumCycleTime(self: RuntimeGroup) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the Runtime Group

        Get: Name(self: RuntimeGroup) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: RuntimeGroup) -> IEngineeringObject
        """
        ...

    @property
    def PostProcessingName(self) -> str:
        """
        The Post processing Block of the Runtime Group

        Get: PostProcessingName(self: RuntimeGroup) -> str
        """
        ...

    @property
    def PreProcessingName(self) -> str:
        """
        The Pre processing Block of the Runtime Group

        Get: PreProcessingName(self: RuntimeGroup) -> str
        """
        ...

    @property
    def WarnCycleTime(self) -> int:
        """
        The Warn Cycle Time of the Runtime Group

        Get: WarnCycleTime(self: RuntimeGroup) -> int

        Set: WarnCycleTime(self: RuntimeGroup) = value
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: RuntimeGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: RuntimeGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class RuntimeGroupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a Safety Runtime Group with its associated information and actions for working with them. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: RuntimeGroupComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> RuntimeGroup:
        """
        Find(self: RuntimeGroupComposition, name: str) -> RuntimeGroup

            Searches for a Runtime Group via the name.

            name: The name of the Runtime Group

            Returns: Siemens.Engineering.Safety.RuntimeGroup
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: RuntimeGroupComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: RuntimeGroupComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[RuntimeGroup](enumerable: IEnumerable[RuntimeGroup], value: RuntimeGroup) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SafetyAdministration(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Provides access to Safety-related information and configuration. """
    @property
    def IsLoggedOnToSafetyOfflineProgram(self) -> bool:
        """
        Query�whether�the�user�is�logged�on

        Get: IsLoggedOnToSafetyOfflineProgram(self: SafetyAdministration) -> bool
        """
        ...

    @property
    def IsSafetyOfflineProgramPasswordSet(self) -> bool:
        """
        Query�whether�a�safety�program�password�is�set

        Get: IsSafetyOfflineProgramPasswordSet(self: SafetyAdministration) -> bool
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: SafetyAdministration) -> IEngineeringObject
        """
        ...

    @property
    def RuntimeGroups(self) -> RuntimeGroupComposition:
        """
        Provides access to the RuntimeGroups of the Safety program.

        Get: RuntimeGroups(self: SafetyAdministration) -> RuntimeGroupComposition
        """
        ...

    @property
    def Settings(self) -> SafetySettings:
        """
        Provides access to the Settings of the Safety program.

        Get: Settings(self: SafetyAdministration) -> SafetySettings
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SafetyAdministration) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def LoginToSafetyOfflineProgram(self, currentPassword:SecureString): # ->
        """
        LoginToSafetyOfflineProgram(self: SafetyAdministration, currentPassword: SecureString)

            Logs into the safety program if correct password is given

            currentPassword: Current password to LoginToSafetyOfflineProgram
        """
        ...

    def LogoffFromSafetyOfflineProgram(self): # ->
        """
        LogoffFromSafetyOfflineProgram(self: SafetyAdministration)

            Log off from the safety program
        """
        ...

    def RevokeSafetyOfflineProgramPassword(self, currentPassword:SecureString): # ->
        """
        RevokeSafetyOfflineProgramPassword(self: SafetyAdministration, currentPassword: SecureString)

            Removes the safety password if it matches the current password

            currentPassword: Current password to verify
        """
        ...

    def SetSafetyOfflineProgramPassword(self, newPassword:SecureString): # ->
        """
        SetSafetyOfflineProgramPassword(self: SafetyAdministration, newPassword: SecureString)

            Sets the safety password if it isn't set

            newPassword: New Password to set
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SafetyAdministration) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SafetyPrintout(IEquatable, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'object'>
    """ Service providing Safety Printout functionality for Plus PLCs. """
    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SafetyPrintout) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Print(self, filePrinter:SafetyPrintoutFilePrinter, fullOutputPath:FileInfo, documentLayout:str, documentationOption:SafetyPrintoutOption) -> bool:
        """
        Print(self: SafetyPrintout, filePrinter: SafetyPrintoutFilePrinter, fullOutputPath: FileInfo, documentLayout: str, documentationOption: SafetyPrintoutOption) -> bool

            Creates a Safety Printout for the current device item and prints it to a file. If the file already exists, it is overridden. - Returns true on success.

            filePrinter: Installed printer driver which supports printing to a file.

            fullOutputPath: Valid output path to a file.

            documentLayout: Document layout used for printing (eg. "DocuInfo_ISO_A4_Portrait")

            documentationOption: Printing option for document format ("All", "Compact")

            Returns: System.Boolean
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SafetyPrintout) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SafetyPrintoutFilePrinter(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Defines the available built-in Windows printer drivers which support printing to file.

    enum SafetyPrintoutFilePrinter, values: MicrosoftPrintToPdf (0), MicrosoftXpsDocumentWriter (1)
    """
    MicrosoftPrintToPdf: SafetyPrintoutFilePrinter = ...
    MicrosoftXpsDocumentWriter: SafetyPrintoutFilePrinter = ...
    value__ = ...


class SafetyPrintoutOption(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Defines the options for Safety Printout.

    enum SafetyPrintoutOption, values: All (0), Compact (1)
    """
    All: SafetyPrintoutOption = ...
    Compact: SafetyPrintoutOption = ...
    value__ = ...


class SafetySettings(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Enables access to information and methods regarding the Settings of the Safety program. """
    @property
    def ActivationOfFChangeHistory(self): # ->
        """
        Indicates whether logging of changes to the Safety program is activated (enabled).

        Get: ActivationOfFChangeHistory(self: SafetySettings) -> bool

        Set: ActivationOfFChangeHistory(self: SafetySettings) = value
        """
        ...

    @property
    def AssignmentOfBlockNumbers(self) -> AssignmentOfBlockNumbers:
        """
        Provides access to attributes for configuring block number ranges of system-generated safety blocks.

        Get: AssignmentOfBlockNumbers(self: SafetySettings) -> AssignmentOfBlockNumbers
        """
        ...

    @property
    def CreateDriverInstanceDataBlocksWithoutPrefix(self) -> bool:
        """
        Gets or sets whether the names of the F-I/O DBs are created without prefix.

        Get: CreateDriverInstanceDataBlocksWithoutPrefix(self: SafetySettings) -> bool

        Set: CreateDriverInstanceDataBlocksWithoutPrefix(self: SafetySettings) = value
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: SafetySettings) -> IEngineeringObject
        """
        ...

    @property
    def SafetyModeCanBeDisabled(self) -> bool:
        """
        Gets or sets indicating whether one can prevent the Safety mode for a Safety program from being disabled.

        Get: SafetyModeCanBeDisabled(self: SafetySettings) -> bool

        Set: SafetyModeCanBeDisabled(self: SafetySettings) = value
        """
        ...

    @property
    def SafetySystemVersion(self): # ->
        """
        Gets or sets the Safety system version (including version of the F-system blocks and automatically generated F-blocks).

        Get: SafetySystemVersion(self: SafetySettings) -> SafetySystemVersion

        Set: SafetySystemVersion(self: SafetySettings) = value
        """
        ...


    def CleanSystemGeneratedObjects(self): # ->
        """
        CleanSystemGeneratedObjects(self: SafetySettings)

            Cleans up the result of the fail-safe compilation.
        """
        ...

    def GetApplicableSafetySystemVersions(self) -> IList:
        """
        GetApplicableSafetySystemVersions(self: SafetySettings) -> IList[SafetySystemVersion]

            A List enumeration with the applicable Safety-System-Versions.

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Safety.SafetySystemVersion>
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SafetySettings) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SafetySettings) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SafetySignature(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Provides the Safety Signature. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: SafetySignature) -> IEngineeringObject
        """
        ...

    @property
    def Type(self) -> SafetySignatureType:
        """
        Defines the type of the SafetySignature

        Get: Type(self: SafetySignature) -> SafetySignatureType
        """
        ...

    @property
    def Value(self) -> UInt64:
        """
        Provides the safety signature value.

        Get: Value(self: SafetySignature) -> UInt64
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SafetySignature) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SafetySignature) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SafetySignatureComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of SafetySignatures """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: SafetySignatureComposition) -> IEngineeringObject
        """
        ...


    def Find(self, type:SafetySignatureType) -> SafetySignature:
        """
        Find(self: SafetySignatureComposition, type: SafetySignatureType) -> SafetySignature

            Searches for a SafetySignature by a given signature type

            type: The type of a SafetySignature

            Returns: Siemens.Engineering.Safety.SafetySignature
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SafetySignatureComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SafetySignatureComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SafetySignature](enumerable: IEnumerable[SafetySignature], value: SafetySignature) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SafetySignatureProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents the Safety Signature of an object. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: SafetySignatureProvider) -> IEngineeringObject
        """
        ...

    @property
    def Signatures(self) -> SafetySignatureComposition:
        """
        Provides the SafetySignatures that belongs to the Parent object.

        Get: Signatures(self: SafetySignatureProvider) -> SafetySignatureComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SafetySignatureProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SafetySignatureProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SafetySignatureType(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Represents the SafetySignature Types

    enum SafetySignatureType, values: BlockOfflineSignature (0)
    """
    BlockOfflineSignature: SafetySignatureType = ...
    value__ = ...


class SafetySystemVersion(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents a Safety system version value. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: SafetySystemVersion) -> IEngineeringObject
        """
        ...

    @property
    def Value(self) -> str:
        """
        The string value of Safety system version.

        Get: Value(self: SafetySystemVersion) -> str
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SafetySystemVersion) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SafetySystemVersion) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...
