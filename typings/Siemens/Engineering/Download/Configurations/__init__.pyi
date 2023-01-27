# encoding: utf-8
# module Siemens.Engineering.Download.Configurations calls itself Configurations
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

class DownloadConfiguration(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Donwload configuration base class. """
    @property
    def Message(self) -> str:
        """
        Descriptions of this onfiguration

        Get: Message(self: DownloadConfiguration) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: DownloadConfiguration) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: DownloadConfiguration) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: DownloadConfiguration) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DownloadSelectionConfiguration(DownloadConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Download configuration that provides choices. """
    pass

class ActiveTestCanBeAborted(DownloadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Active test and commissioning functions could be canceled by loading to the device. """
    @property
    def CurrentSelection(self) -> ActiveTestCanBeAbortedSelections:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: ActiveTestCanBeAborted) -> ActiveTestCanBeAbortedSelections

        Set: CurrentSelection(self: ActiveTestCanBeAborted) = value
        """
        ...



class ActiveTestCanBeAbortedSelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for ActiveTestCanBeAborted configuration

    enum ActiveTestCanBeAbortedSelections, values: AcceptAll (1), NoAction (0)
    """
    AcceptAll: ActiveTestCanBeAbortedSelections = ...
    NoAction: ActiveTestCanBeAbortedSelections = ...
    value__ = ...


class ActiveTestCanPreventDownload(DownloadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Active test and commissioning functions could prevent loading to the device. """
    @property
    def CurrentSelection(self) -> ActiveTestCanPreventDownloadSelections:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: ActiveTestCanPreventDownload) -> ActiveTestCanPreventDownloadSelections

        Set: CurrentSelection(self: ActiveTestCanPreventDownload) = value
        """
        ...



class ActiveTestCanPreventDownloadSelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for ActiveTestCanPreventDownload configuration

    enum ActiveTestCanPreventDownloadSelections, values: AcceptAll (1), NoAction (0)
    """
    AcceptAll: ActiveTestCanPreventDownloadSelections = ...
    NoAction: ActiveTestCanPreventDownloadSelections = ...
    value__ = ...


class AlarmTextLibrariesDownload(DownloadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Download all alarm texts and text list texts """
    @property
    def CurrentSelection(self) -> AlarmTextLibrariesDownloadSelections:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: AlarmTextLibrariesDownload) -> AlarmTextLibrariesDownloadSelections

        Set: CurrentSelection(self: AlarmTextLibrariesDownload) = value
        """
        ...



class AlarmTextLibrariesDownloadSelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for AlarmTextLibrariesDownload configuration

    enum AlarmTextLibrariesDownloadSelections, values: ConsistentDownload (0), NoAction (1)
    """
    ConsistentDownload: AlarmTextLibrariesDownloadSelections = ...
    NoAction: AlarmTextLibrariesDownloadSelections = ...
    value__ = ...


class AllBlocksDownload(DownloadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Download software to device """
    @property
    def CurrentSelection(self) -> AllBlocksDownloadSelections:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: AllBlocksDownload) -> AllBlocksDownloadSelections

        Set: CurrentSelection(self: AllBlocksDownload) = value
        """
        ...



class AllBlocksDownloadSelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for AllBlocksDownload configuration

    enum AllBlocksDownloadSelections, values: DownloadAllBlocks (0)
    """
    DownloadAllBlocks: AllBlocksDownloadSelections = ...
    value__ = ...


class DownloadPasswordConfiguration(DownloadConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Download password configuration. """
    def SetPassword(self, password:SecureString): # ->
        """
        SetPassword(self: DownloadPasswordConfiguration, password: SecureString)

            Sets password

            password: Required password.
        """
        ...


class BlockBindingPassword(DownloadPasswordConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Block binding password configuration """
    pass

class DownloadCheckConfiguration(DownloadConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Download configuration that can be checked/unchecked. """
    @property
    def Checked(self) -> bool:
        """
        Specifies if this configuration checked.

        Get: Checked(self: DownloadCheckConfiguration) -> bool

        Set: Checked(self: DownloadCheckConfiguration) = value
        """
        ...



class CheckBeforeDownload(DownloadCheckConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Checks before downloading to the device. """
    pass

class ConsistentBlocksDownload(DownloadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Download software to device """
    @property
    def CurrentSelection(self) -> ConsistentBlocksDownloadSelections:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: ConsistentBlocksDownload) -> ConsistentBlocksDownloadSelections

        Set: CurrentSelection(self: ConsistentBlocksDownload) = value
        """
        ...



class ConsistentBlocksDownloadSelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for ConsistentBlocksDownload configuration

    enum ConsistentBlocksDownloadSelections, values: ConsistentDownload (0)
    """
    ConsistentDownload: ConsistentBlocksDownloadSelections = ...
    value__ = ...


class DifferentTargetConfiguration(DownloadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Differences between configured and target modules (online) """
    @property
    def CurrentSelection(self) -> DifferentTargetConfigurationSelections:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: DifferentTargetConfiguration) -> DifferentTargetConfigurationSelections

        Set: CurrentSelection(self: DifferentTargetConfiguration) = value
        """
        ...



class DifferentTargetConfigurationSelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for DifferentTargetConfiguration configuration

    enum DifferentTargetConfigurationSelections, values: AcceptAll (1), NoAction (0)
    """
    AcceptAll: DifferentTargetConfigurationSelections = ...
    NoAction: DifferentTargetConfigurationSelections = ...
    value__ = ...


class DowngradeTargetDevice(DownloadCheckConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Different data formats in online and offline project. """
    pass

class ExpandDownload(DownloadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ The download must be expanded beyond your selection. """
    @property
    def CurrentSelection(self) -> ExpandDownloadSelections:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: ExpandDownload) -> ExpandDownloadSelections

        Set: CurrentSelection(self: ExpandDownload) = value
        """
        ...



class ExpandDownloadSelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for ExpandDownload configuration

    enum ExpandDownloadSelections, values: Download (1), NoAction (0)
    """
    Download: ExpandDownloadSelections = ...
    NoAction: ExpandDownloadSelections = ...
    value__ = ...


class FitHmiComponents(DownloadCheckConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Components with a different version are installed on the target device. """
    pass

class InitializeMemory(DownloadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ The modules will initialize memory. """
    @property
    def CurrentSelection(self) -> InitializeMemorySelections:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: InitializeMemory) -> InitializeMemorySelections

        Set: CurrentSelection(self: InitializeMemory) = value
        """
        ...



class InitializeMemorySelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for InitializeMemory configuration

    enum InitializeMemorySelections, values: AcceptAll (1), NoAction (0)
    """
    AcceptAll: InitializeMemorySelections = ...
    NoAction: InitializeMemorySelections = ...
    value__ = ...


class LoadIdentificationData(DownloadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Load identification data to the PROFINET IO devices and their modules. """
    @property
    def CurrentSelection(self) -> LoadIdentificationDataSelections:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: LoadIdentificationData) -> LoadIdentificationDataSelections

        Set: CurrentSelection(self: LoadIdentificationData) = value
        """
        ...



class LoadIdentificationDataSelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for LoadIdentificationData configuration

    enum LoadIdentificationDataSelections, values: LoadData (1), LoadNothing (0)
    """
    LoadData: LoadIdentificationDataSelections = ...
    LoadNothing: LoadIdentificationDataSelections = ...
    value__ = ...


class ModuleReadAccessPassword(DownloadPasswordConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Enter a password to gain read access to the module. """
    pass

class ModuleWriteAccessPassword(DownloadPasswordConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Enter a password to gain write access to the module """
    pass

class OverwriteHmiData(DownloadCheckConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Overwrite if object exists online? """
    pass

class OverwriteSystemData(DownloadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Delete and replace system data in target """
    @property
    def CurrentSelection(self) -> OverwriteSystemDataSelections:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: OverwriteSystemData) -> OverwriteSystemDataSelections

        Set: CurrentSelection(self: OverwriteSystemData) = value
        """
        ...



class OverwriteSystemDataSelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for OverwriteSystemData configuration

    enum OverwriteSystemDataSelections, values: NoAction (0), Overwrite (1)
    """
    NoAction: OverwriteSystemDataSelections = ...
    Overwrite: OverwriteSystemDataSelections = ...
    value__ = ...


class OverwriteTargetLanguages(DownloadCheckConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ There are differences between the settings for the project and the settings for PLC programming. """
    pass

class ProtectionLevelChanged(DownloadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ CPU protection will be changed to a lower level. """
    @property
    def CurrentSelection(self) -> ProtectionLevelChangedSelections:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: ProtectionLevelChanged) -> ProtectionLevelChangedSelections

        Set: CurrentSelection(self: ProtectionLevelChanged) = value
        """
        ...



class ProtectionLevelChangedSelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for ProtectionLevelChanged configuration

    enum ProtectionLevelChangedSelections, values: ContinueDownloading (1), NoChange (0)
    """
    ContinueDownloading: ProtectionLevelChangedSelections = ...
    NoChange: ProtectionLevelChangedSelections = ...
    value__ = ...


class ResetModule(DownloadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Reset module """
    @property
    def CurrentSelection(self) -> ResetModuleSelections:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: ResetModule) -> ResetModuleSelections

        Set: CurrentSelection(self: ResetModule) = value
        """
        ...



class ResetModuleSelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for ResetModule configuration

    enum ResetModuleSelections, values: DeleteAll (1), NoAction (0)
    """
    DeleteAll: ResetModuleSelections = ...
    NoAction: ResetModuleSelections = ...
    value__ = ...


class StartBackupModules(DownloadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Start modules after downloading to device. """
    @property
    def CurrentSelection(self) -> StartBackupModulesSelections:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: StartBackupModules) -> StartBackupModulesSelections

        Set: CurrentSelection(self: StartBackupModules) = value
        """
        ...



class StartBackupModulesSelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for StartBackupModules configuration

    enum StartBackupModulesSelections, values: NoAction (0), StartModule (2), SwitchToPrimaryCpu (1)
    """
    NoAction: StartBackupModulesSelections = ...
    StartModule: StartBackupModulesSelections = ...
    SwitchToPrimaryCpu: StartBackupModulesSelections = ...
    value__ = ...


class StartModules(DownloadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Start modules after downloading to device. """
    @property
    def CurrentSelection(self) -> StartModulesSelections:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: StartModules) -> StartModulesSelections

        Set: CurrentSelection(self: StartModules) = value
        """
        ...



class StartModulesSelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for StartModules configuration

    enum StartModulesSelections, values: NoAction (0), StartModule (1)
    """
    NoAction: StartModulesSelections = ...
    StartModule: StartModulesSelections = ...
    value__ = ...


class StopHSystem(DownloadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ The modules are stopped for downloading to device. """
    @property
    def CurrentSelection(self) -> StopHSystemSelections:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: StopHSystem) -> StopHSystemSelections

        Set: CurrentSelection(self: StopHSystem) = value
        """
        ...



class StopHSystemOrModule(DownloadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ The modules are stopped for downloading to device. """
    @property
    def CurrentSelection(self) -> StopHSystemOrModuleSelections:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: StopHSystemOrModule) -> StopHSystemOrModuleSelections

        Set: CurrentSelection(self: StopHSystemOrModule) = value
        """
        ...



class StopHSystemOrModuleSelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for StopHSystemOrModule configuration

    enum StopHSystemOrModuleSelections, values: NoAction (0), StopHSystem (1), StopModule (2)
    """
    NoAction: StopHSystemOrModuleSelections = ...
    StopHSystem: StopHSystemOrModuleSelections = ...
    StopModule: StopHSystemOrModuleSelections = ...
    value__ = ...


class StopHSystemSelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for StopHSystem configuration

    enum StopHSystemSelections, values: NoAction (0), StopHSystem (1)
    """
    NoAction: StopHSystemSelections = ...
    StopHSystem: StopHSystemSelections = ...
    value__ = ...


class StopModules(DownloadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ The modules are stopped for downloading to device. """
    @property
    def CurrentSelection(self) -> StopModulesSelections:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: StopModules) -> StopModulesSelections

        Set: CurrentSelection(self: StopModules) = value
        """
        ...



class StopModulesSelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for StopModules configuration

    enum StopModulesSelections, values: NoAction (0), StopAll (1)
    """
    NoAction: StopModulesSelections = ...
    StopAll: StopModulesSelections = ...
    value__ = ...


class SwitchBackupToPrimary(DownloadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Start modules after downloading to device. """
    @property
    def CurrentSelection(self) -> SwitchBackupToPrimarySelections:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: SwitchBackupToPrimary) -> SwitchBackupToPrimarySelections

        Set: CurrentSelection(self: SwitchBackupToPrimary) = value
        """
        ...



class SwitchBackupToPrimarySelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for SwitchBackupToPrimary configuration

    enum SwitchBackupToPrimarySelections, values: NoAction (0), SwitchToPrimaryCpu (1)
    """
    NoAction: SwitchBackupToPrimarySelections = ...
    SwitchToPrimaryCpu: SwitchBackupToPrimarySelections = ...
    value__ = ...


class TurnOffSequence(DownloadCheckConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Turn off the sequence before loading. """
    pass

class UpgradeTargetDevice(DownloadCheckConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Different project versions in the configured device and target device (online). """
    pass

class WaitOnReboot(DownloadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Wait on reboot of a pc system. """
    @property
    def CurrentSelection(self) -> WaitOnRebootSelections:
        """
        Current selection for this configuation.

        Get: CurrentSelection(self: WaitOnReboot) -> WaitOnRebootSelections

        Set: CurrentSelection(self: WaitOnReboot) = value
        """
        ...



class WaitOnRebootSelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for WaitOnReboot configuration.

    enum WaitOnRebootSelections, values: NoAction (0), Wait (1)
    """
    NoAction: WaitOnRebootSelections = ...
    value__ = ...
    Wait: WaitOnRebootSelections = ...
