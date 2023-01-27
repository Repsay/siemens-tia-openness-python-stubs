# encoding: utf-8
# module Microsoft.SqlServer.Management.SqlParser.MetadataDifferencer calls itself MetadataDifferencer
# from Microsoft.SqlServer.Management.SqlParser, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.SqlParser.Metadata import (
    IMetadataObject)

from System.Collections import IDictionary, IEnumerable

"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class ChangeResult: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CreatedObjects(self) -> IEnumerable:
        """ Get: CreatedObjects(self: ChangeResult) -> IEnumerable[IMetadataObject] """
        ...

    @property
    def DeletedObjects(self) -> IEnumerable:
        """ Get: DeletedObjects(self: ChangeResult) -> IEnumerable[IMetadataObject] """
        ...

    @property
    def SourceModifiedObjects(self) -> IDictionary:
        """ Get: SourceModifiedObjects(self: ChangeResult) -> IDictionary[IMetadataObject, ObjectDifference] """
        ...

    @property
    def TargetModifiedObjects(self) -> IDictionary:
        """ Get: TargetModifiedObjects(self: ChangeResult) -> IDictionary[IMetadataObject, ObjectDifference] """
        ...


    def IsEmpty(self) -> bool:
        """ IsEmpty(self: ChangeResult) -> bool """
        ...


class DifferencerException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    SerializeObjectState = ...


class ObjectDifference: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ChangedObjectSource(self) -> IMetadataObject:
        """ Get: ChangedObjectSource(self: ObjectDifference) -> IMetadataObject """
        ...

    @property
    def ChangedObjectTarget(self) -> IMetadataObject:
        """ Get: ChangedObjectTarget(self: ObjectDifference) -> IMetadataObject """
        ...

    @property
    def PropertyDifferences(self) -> IDictionary:
        """ Get: PropertyDifferences(self: ObjectDifference) -> IDictionary[str, PropertyDifference] """
        ...



class PropertyDifference: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: PropertyDifference) -> str """
        ...



class OrderedCollectionDifference(PropertyDifference): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def OrderDifferences(self) -> IEnumerable:
        """ Get: OrderDifferences(self: OrderedCollectionDifference) -> IEnumerable[OrderedScalarDifference] """
        ...



class ScalarDifference(PropertyDifference): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SourceValue(self) -> object:
        """ Get: SourceValue(self: ScalarDifference) -> object """
        ...

    @property
    def TargetValue(self) -> object:
        """ Get: TargetValue(self: ScalarDifference) -> object """
        ...



class OrderedScalarDifference(ScalarDifference): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SourceIndex(self) -> int:
        """ Get: SourceIndex(self: OrderedScalarDifference) -> int """
        ...

    @property
    def TargetIndex(self) -> int:
        """ Get: TargetIndex(self: OrderedScalarDifference) -> int """
        ...



