# encoding: utf-8
# module Siemens.Engineering.SW calls itself SW
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringObject, IEngineeringService, 
    IEngineeringServiceProvider)

from Siemens.Engineering.Compare import CompareResult

from Siemens.Engineering.HW import Software

from Siemens.Engineering.Library.Types import (IInstanceSearchScope, 
    IUpdateProjectScope)

from Siemens.Engineering.SW.Blocks import PlcBlockSystemGroup

from Siemens.Engineering.SW.ExternalSources import (
    PlcExternalSourceSystemGroup)

from Siemens.Engineering.SW.Tags import PlcTagTableSystemGroup

from Siemens.Engineering.SW.TechnologicalObjects import (
    TechnologicalInstanceDBGroup)

from Siemens.Engineering.SW.Types import PlcTypeSystemGroup

from Siemens.Engineering.SW.WatchAndForceTables import (
    PlcWatchAndForceTableSystemGroup)

from System import Enum, IEquatable

from System.Collections import IList

"""The following names are not found in the module: (IInternalObjectAccess, 
    field#)
"""

# no functions
# classes

class Fingerprint(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ fingerprint """
    @property
    def Id(self) -> FingerprintId:
        """
        ID of the fingerprint
        Get: Id(self: Fingerprint) -> FingerprintId
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: Fingerprint) -> IEngineeringObject
        """
        ...

    @property
    def Value(self) -> str:
        """
        fingerprint data
        Get: Value(self: Fingerprint) -> str
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: Fingerprint) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: Fingerprint) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class FingerprintId(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    fingerprint id
    enum FingerprintId, values: Alarms (5), Code (0), Comments (1), Events (8), Interface (2), LibraryType (3), Properties (10), Supervisions (6), TechnologyObject (7), Texts (4), TextualInterface (9)
    """
    Alarms: FingerprintId = ...
    Code: FingerprintId = ...
    Comments: FingerprintId = ...
    Events: FingerprintId = ...
    Interface: FingerprintId = ...
    LibraryType: FingerprintId = ...
    Properties: FingerprintId = ...
    Supervisions: FingerprintId = ...
    TechnologyObject: FingerprintId = ...
    Texts: FingerprintId = ...
    TextualInterface: FingerprintId = ...
    value__ = ...


class FingerprintProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Provides fingerprints. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: FingerprintProvider) -> IEngineeringObject
        """
        ...


    def GetFingerprints(self) -> IList:
        """
        GetFingerprints(self: FingerprintProvider) -> IList[Fingerprint]
            Read Fingerprint
            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Fingerprint>
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: FingerprintProvider) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: FingerprintProvider) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ISoftwareCompareTarget: # skipped bases: <type 'object'>
    """ Access to the controller in a compare scenario """
    pass

class PlcChecksumProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Provides checksums. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: PlcChecksumProvider) -> IEngineeringObject
        """
        ...

    @property
    def Software(self) -> str:
        """
        Software checksum
        Get: Software(self: PlcChecksumProvider) -> str
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcChecksumProvider) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcChecksumProvider) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcSoftware(IInstanceSearchScope, IUpdateProjectScope, IEngineeringServiceProvider, ISoftwareCompareTarget, Software): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents the software components of a Plc """
    @property
    def BlockGroup(self) -> PlcBlockSystemGroup:
        """
        Gets the Plc block system group
        Get: BlockGroup(self: PlcSoftware) -> PlcBlockSystemGroup
        """
        ...

    @property
    def ExternalSourceGroup(self) -> PlcExternalSourceSystemGroup:
        """
        Gets the Plc external source system group
        Get: ExternalSourceGroup(self: PlcSoftware) -> PlcExternalSourceSystemGroup
        """
        ...

    @property
    def TagTableGroup(self) -> PlcTagTableSystemGroup:
        """
        Get the Plc tag table system group
        Get: TagTableGroup(self: PlcSoftware) -> PlcTagTableSystemGroup
        """
        ...

    @property
    def TechnologicalObjectGroup(self) -> TechnologicalInstanceDBGroup:
        """
        This system folder can contain technological objects
        Get: TechnologicalObjectGroup(self: PlcSoftware) -> TechnologicalInstanceDBGroup
        """
        ...

    @property
    def TypeGroup(self) -> PlcTypeSystemGroup:
        """
        Gets Plc type system group
        Get: TypeGroup(self: PlcSoftware) -> PlcTypeSystemGroup
        """
        ...

    @property
    def WatchAndForceTableGroup(self) -> PlcWatchAndForceTableSystemGroup:
        """
        Get the Plc watch table system group
        Get: WatchAndForceTableGroup(self: PlcSoftware) -> PlcWatchAndForceTableSystemGroup
        """
        ...


    def CompareTo(self, compareTarget:ISoftwareCompareTarget) -> CompareResult:
        """
        CompareTo(self: PlcSoftware, compareTarget: ISoftwareCompareTarget) -> CompareResult
            Compare the PLC software to the given target
            compareTarget: The target to compare to the PLC software
            Returns: Siemens.Engineering.Compare.CompareResult
        """
        ...

    def CompareToOnline(self) -> CompareResult:
        """
        CompareToOnline(self: PlcSoftware) -> CompareResult
            Compare the PLC software to the online target
            Returns: Siemens.Engineering.Compare.CompareResult
        """
        ...


class SWImportOptions(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    The list of possible sw importoptions for Import
    enum (flags) SWImportOptions, values: IgnoreMissingReferencedObjects (2), IgnoreStructuralChanges (1), None (0)
    """
    IgnoreMissingReferencedObjects: SWImportOptions = ...
    IgnoreStructuralChanges: SWImportOptions = ...
    value__ = ...


# variables with complex values

