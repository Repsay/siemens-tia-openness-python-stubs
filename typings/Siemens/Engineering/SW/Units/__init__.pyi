# encoding: utf-8
# module Siemens.Engineering.SW.Units calls itself Units
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringComposition, IEngineeringObject,
    IEngineeringService, IEngineeringServiceProvider, MultilingualText)

from Siemens.Engineering.Library.MasterCopies import (IMasterCopySource,
    IMasterCopyTarget, MasterCopy)

from Siemens.Engineering.SW.Blocks import PlcBlockSystemGroup

from Siemens.Engineering.SW.ExternalSources import (
    PlcExternalSourceSystemGroup)

from Siemens.Engineering.SW.Tags import PlcTagTableSystemGroup

from Siemens.Engineering.SW.Types import PlcTypeSystemGroup

from System import Enum, IEquatable

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess, field#)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class PlcUnit(IInternalObjectAccess, IEngineeringServiceProvider, IMasterCopyTarget, IEngineeringObject, IMasterCopySource, IEquatable): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents a Plc unit """
    @property
    def Author(self) -> str:
        """
        The author of the Plc unit

        Get: Author(self: PlcUnit) -> str

        Set: Author(self: PlcUnit) = value
        """
        ...

    @property
    def BlockGroup(self) -> PlcBlockSystemGroup:
        """
        Gets the Plc block system group

        Get: BlockGroup(self: PlcUnit) -> PlcBlockSystemGroup
        """
        ...

    @property
    def Comment(self) -> MultilingualText:
        """
        The comment of the Plc unit

        Get: Comment(self: PlcUnit) -> MultilingualText
        """
        ...

    @property
    def ExternalSourceGroup(self) -> PlcExternalSourceSystemGroup:
        """
        Gets unit external source group

        Get: ExternalSourceGroup(self: PlcUnit) -> PlcExternalSourceSystemGroup
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the Plc unit

        Get: Name(self: PlcUnit) -> str

        Set: Name(self: PlcUnit) = value
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: PlcUnit) -> IEngineeringObject
        """
        ...

    @property
    def Relations(self) -> PlcUnitRelationComposition:
        """
        Gets the unit relations

        Get: Relations(self: PlcUnit) -> PlcUnitRelationComposition
        """
        ...

    @property
    def TagTableGroup(self) -> PlcTagTableSystemGroup:
        """
        Gets the Plc tag table system group

        Get: TagTableGroup(self: PlcUnit) -> PlcTagTableSystemGroup
        """
        ...

    @property
    def TypeGroup(self) -> PlcTypeSystemGroup:
        """
        Gets the Plc type system group

        Get: TypeGroup(self: PlcUnit) -> PlcTypeSystemGroup
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: PlcUnit)

            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcUnit) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcUnit) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcUnitComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of Plc units """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: PlcUnitComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, sourceMasterCopy:MasterCopy) -> PlcUnit:
        """
        CreateFrom(self: PlcUnitComposition, sourceMasterCopy: MasterCopy) -> PlcUnit

            Create a Plc unit from a master copy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.SW.Units.PlcUnit
        """
        ...

    def Find(self, name:str) -> PlcUnit:
        """
        Find(self: PlcUnitComposition, name: str) -> PlcUnit

            Find a Plc unit by name

            name: Name of Plc unit

            Returns: Siemens.Engineering.SW.Units.PlcUnit
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcUnitComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcUnitComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcUnit](enumerable: IEnumerable[PlcUnit], value: PlcUnit) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcUnitProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Provides Plc units """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: PlcUnitProvider) -> IEngineeringObject
        """
        ...

    @property
    def UnitGroup(self) -> PlcUnitSystemGroup:
        """
        Gets the Plc unit system group

        Get: UnitGroup(self: PlcUnitProvider) -> PlcUnitSystemGroup
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcUnitProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcUnitProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcUnitRelation(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents a unit relation """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: PlcUnitRelation) -> IEngineeringObject
        """
        ...

    @property
    def RelatedObject(self) -> str:
        """
        Related object of the relation

        Get: RelatedObject(self: PlcUnitRelation) -> str

        Set: RelatedObject(self: PlcUnitRelation) = value
        """
        ...

    @property
    def RelationType(self) -> UnitRelationType:
        """
        Unit relation type which allowed to access

        Get: RelationType(self: PlcUnitRelation) -> UnitRelationType
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: PlcUnitRelation)

            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcUnitRelation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcUnitRelation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcUnitRelationComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of Plc unit relations """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: PlcUnitRelationComposition) -> IEngineeringObject
        """
        ...


    def Find(self, relatedObject:str) -> PlcUnitRelation:
        """
        Find(self: PlcUnitRelationComposition, relatedObject: str) -> PlcUnitRelation

            Find a Plc unit relation by the name of the related object

            relatedObject: Name of the related object

            Returns: Siemens.Engineering.SW.Units.PlcUnitRelation
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcUnitRelationComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcUnitRelationComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcUnitRelation](enumerable: IEnumerable[PlcUnitRelation], value: PlcUnitRelation) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcUnitSystemGroup(IEquatable, IEngineeringObject, IEngineeringServiceProvider, IMasterCopyTarget, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ System group containing Plc units """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: PlcUnitSystemGroup) -> IEngineeringObject
        """
        ...

    @property
    def Units(self) -> PlcUnitComposition:
        """
        Composition of Plc units

        Get: Units(self: PlcUnitSystemGroup) -> PlcUnitComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcUnitSystemGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcUnitSystemGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UnitAccessType(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Unit accessibility type

    enum UnitAccessType, values: Published (0), Unpublished (1)
    """
    Published: UnitAccessType = ...
    Unpublished: UnitAccessType = ...
    value__ = ...


class UnitRelationType(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Relation types in Unit relation editor

    enum UnitRelationType, values: NonUnitDB (1), SoftwareUnit (0), TODB (2)
    """
    NonUnitDB: UnitRelationType = ...
    SoftwareUnit: UnitRelationType = ...
    TODB: UnitRelationType = ...
    value__ = ...
