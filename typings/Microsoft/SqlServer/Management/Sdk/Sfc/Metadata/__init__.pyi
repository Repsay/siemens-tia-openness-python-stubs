# encoding: utf-8
# module Microsoft.SqlServer.Management.Sdk.Sfc.Metadata calls itself Metadata
# from Microsoft.SqlServer.Management.Sdk.Sfc, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Sdk.Sfc import SfcException, Urn

from System import (Array, AsyncCallback, Attribute, Delegate, Enum, 
    IAsyncResult, MulticastDelegate, Type, Version)

from System.Collections import IEnumerable

from System.Collections.Generic import List

from System.ComponentModel import AttributeCollection

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class ISfcMetadata: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Metadata(self) -> SfcMetadataDiscovery:
        """ Get: Metadata(self: ISfcMetadata) -> SfcMetadataDiscovery """
        ...



class ISfcMetadataProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetMetadataProvider(self) -> SfcMetadataDiscovery:
        """ GetMetadataProvider(self: ISfcMetadataProvider) -> SfcMetadataDiscovery """
        ...


class ISfcReferenceCollectionResolver: # skipped bases: <type 'object'>
    """ no doc """
    def ResolveCollection(self, instance:object, args:Array) -> IEnumerable:
        """ ResolveCollection(self: ISfcReferenceCollectionResolver, instance: object, args: Array[object]) -> IEnumerable """
        ...


class ISfcReferenceResolver: # skipped bases: <type 'object'>
    """ no doc """
    def Resolve(self, instance:object, args:Array) -> object:
        """ Resolve(self: ISfcReferenceResolver, instance: object, args: Array[object]) -> object """
        ...


class ReferenceResolverDelegate(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ReferenceResolverDelegate(object: object, method: IntPtr) """
    def BeginInvoke(self, instance:object, parameters:Array, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ReferenceResolverDelegate, instance: object, parameters: Array[object], callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> object:
        """ EndInvoke(self: ReferenceResolverDelegate, result: IAsyncResult) -> object """
        ...

    def Invoke(self, instance:object, parameters:Array) -> object:
        """ Invoke(self: ReferenceResolverDelegate, instance: object, *parameters: Array[object]) -> object """
        ...


class SfcBrowsableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SfcBrowsableAttribute(isBrowsable: bool) """
    @property
    def IsBrowsable(self) -> bool:
        """
        Get: IsBrowsable(self: SfcBrowsableAttribute) -> bool
        Set: IsBrowsable(self: SfcBrowsableAttribute) = value
        """
        ...


    def __new__(cls, isBrowsable:bool) -> Self:
        """ __new__(cls: type, isBrowsable: bool) """
        ...


class SfcCardinality(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SfcCardinality, values: None (0), One (1), OneToAny (4), ZeroToAny (3), ZeroToOne (2) """
    One: SfcCardinality = ...
    OneToAny: SfcCardinality = ...
    value__ = ...
    ZeroToAny: SfcCardinality = ...
    ZeroToOne: SfcCardinality = ...


class SfcContainerCardinality(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SfcContainerCardinality, values: OneToAny (1), ZeroToAny (0) """
    OneToAny: SfcContainerCardinality = ...
    value__ = ...
    ZeroToAny: SfcContainerCardinality = ...


class SfcContainerRelationship(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SfcContainerRelationship, values: ChildContainer (1), ObjectContainer (0) """
    ChildContainer: SfcContainerRelationship = ...
    ObjectContainer: SfcContainerRelationship = ...
    value__ = ...


class SfcElementTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SfcElementTypeAttribute(elementTypeName: str) """
    @property
    def ElementTypeName(self) -> str:
        """
        Get: ElementTypeName(self: SfcElementTypeAttribute) -> str
        Set: ElementTypeName(self: SfcElementTypeAttribute) = value
        """
        ...


    def __new__(cls, elementTypeName:str) -> Self:
        """ __new__(cls: type, elementTypeName: str) """
        ...


class SfcRelationshipAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    @property
    def Cardinality(self) -> SfcCardinality:
        """ Get: Cardinality(self: SfcRelationshipAttribute) -> SfcCardinality """
        ...

    @property
    def ContainsType(self) -> Type:
        """ Get: ContainsType(self: SfcRelationshipAttribute) -> Type """
        ...

    @property
    def Relationship(self) -> SfcRelationship:
        """ Get: Relationship(self: SfcRelationshipAttribute) -> SfcRelationship """
        ...


    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, relationship: SfcRelationship)
        __new__(cls: type, relationship: SfcRelationship, cardinality: SfcCardinality)
        __new__(cls: type, relationship: SfcRelationship, cardinality: SfcCardinality, containsType: Type)
        """
        ...


class SfcIgnoreAttribute(SfcRelationshipAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SfcIgnoreAttribute() """
    pass

class SfcInvalidForTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SfcInvalidForTypeAttribute(excludedType: Type) """
    @property
    def ExcludedType(self) -> Type:
        """ Get: ExcludedType(self: SfcInvalidForTypeAttribute) -> Type """
        ...


    def __new__(cls, excludedType:Type) -> Self:
        """ __new__(cls: type, excludedType: Type) """
        ...


class SfcKeyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    SfcKeyAttribute()
    SfcKeyAttribute(position: int)
    """
    @property
    def Position(self) -> int:
        """ Get: Position(self: SfcKeyAttribute) -> int """
        ...


    def __new__(cls, position:int = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, position: int)
        """
        ...


class SfcMetadataDiscovery: # skipped bases: <type 'object'>, <type 'object'>
    """ SfcMetadataDiscovery(type: Type) """
    @property
    def ElementTypeName(self) -> str:
        """ Get: ElementTypeName(self: SfcMetadataDiscovery) -> str """
        ...

    @property
    def IsBrowsable(self) -> bool:
        """ Get: IsBrowsable(self: SfcMetadataDiscovery) -> bool """
        ...

    @property
    def Keys(self) -> List:
        """ Get: Keys(self: SfcMetadataDiscovery) -> List[SfcMetadataRelation] """
        ...

    @property
    def Objects(self) -> List:
        """ Get: Objects(self: SfcMetadataDiscovery) -> List[SfcMetadataRelation] """
        ...

    @property
    def Properties(self) -> List:
        """ Get: Properties(self: SfcMetadataDiscovery) -> List[SfcMetadataRelation] """
        ...

    @property
    def ReferredBy(self) -> List:
        """ Get: ReferredBy(self: SfcMetadataDiscovery) -> List[Type] """
        ...

    @property
    def Relations(self) -> List:
        """ Get: Relations(self: SfcMetadataDiscovery) -> List[SfcMetadataRelation] """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: SfcMetadataDiscovery) -> Type """
        ...

    @property
    def TypeAttributes(self) -> AttributeCollection:
        """ Get: TypeAttributes(self: SfcMetadataDiscovery) -> AttributeCollection """
        ...


    def FindProperty(self, propertyName:str) -> SfcMetadataRelation:
        """ FindProperty(self: SfcMetadataDiscovery, propertyName: str) -> SfcMetadataRelation """
        ...

    @staticmethod
    def GetParentsFromType(childType:Type) -> List:
        """ GetParentsFromType(childType: Type) -> List[Type] """
        ...

    @staticmethod
    def GetRootFromType(inputType:Type) -> Type:
        """ GetRootFromType(inputType: Type) -> Type """
        ...

    @staticmethod
    def GetUrnSkeletonsFromType(inputType:Type) -> List:
        """ GetUrnSkeletonsFromType(inputType: Type) -> List[str] """
        ...


class SfcMetadataRelation(SfcMetadataDiscovery): # skipped bases: <type 'object'>
    """
    SfcMetadataRelation(propertyName: str, type: Type, cardinality: SfcCardinality, relationship: SfcRelationship, containerType: Type, flags: SfcPropertyFlags, defaultValue: object, attributes: AttributeCollection)
    SfcMetadataRelation(propertyName: str, type: Type, cardinality: SfcCardinality, relationship: SfcRelationship, containerType: Type, flags: SfcPropertyFlags, attributes: AttributeCollection)
    SfcMetadataRelation(propertyName: str, type: Type, cardinality: SfcCardinality, relationship: SfcRelationship, containerType: Type, attributes: AttributeCollection)
    SfcMetadataRelation(propertyName: str, type: Type, cardinality: SfcCardinality, relationship: SfcRelationship, containerType: Type)
    SfcMetadataRelation(propertyName: str, type: Type, cardinality: SfcCardinality, relationship: SfcRelationship, attributes: AttributeCollection)
    SfcMetadataRelation(propertyName: str, type: Type, cardinality: SfcCardinality, attributes: AttributeCollection)
    SfcMetadataRelation(propertyName: str, type: Type, flags: SfcPropertyFlags, attributes: AttributeCollection)
    SfcMetadataRelation(propertyName: str, type: Type, flags: SfcPropertyFlags)
    SfcMetadataRelation(propertyName: str, type: Type)
    """
    @property
    def Cardinality(self) -> SfcCardinality:
        """ Get: Cardinality(self: SfcMetadataRelation) -> SfcCardinality """
        ...

    @property
    def ContainerType(self) -> Type:
        """ Get: ContainerType(self: SfcMetadataRelation) -> Type """
        ...

    @property
    def PropertyDefaultValue(self) -> object:
        """ Get: PropertyDefaultValue(self: SfcMetadataRelation) -> object """
        ...

    @property
    def PropertyFlags(self) -> SfcPropertyFlags:
        """ Get: PropertyFlags(self: SfcMetadataRelation) -> SfcPropertyFlags """
        ...

    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: SfcMetadataRelation) -> str """
        ...

    @property
    def Relationship(self) -> SfcRelationship:
        """ Get: Relationship(self: SfcMetadataRelation) -> SfcRelationship """
        ...

    @property
    def RelationshipAttributes(self) -> AttributeCollection:
        """ Get: RelationshipAttributes(self: SfcMetadataRelation) -> AttributeCollection """
        ...

    @property
    def SupportsDesignMode(self) -> bool:
        """ Get: SupportsDesignMode(self: SfcMetadataRelation) -> bool """
        ...


    def Resolve(self, instance:object) -> object:
        """
        Resolve(self: SfcMetadataRelation, instance: object) -> object
        Resolve[(T, S)](self: SfcMetadataRelation, instance: S) -> T
        """
        ...

    def ResolveCollection(self, instance:object) -> IEnumerable:
        """
        ResolveCollection(self: SfcMetadataRelation, instance: object) -> IEnumerable
        ResolveCollection[(T, S)](self: SfcMetadataRelation, instance: S) -> IEnumerable[T]
        """
        ...


class SfcNonSerializableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SfcNonSerializableAttribute() """
    pass

class SfcObjectAttribute(SfcRelationshipAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    SfcObjectAttribute(flags: SfcObjectFlags)
    SfcObjectAttribute()
    SfcObjectAttribute(cardinality: SfcObjectCardinality, flags: SfcObjectFlags)
    SfcObjectAttribute(cardinality: SfcObjectCardinality)
    SfcObjectAttribute(relationship: SfcObjectRelationship, flags: SfcObjectFlags)
    SfcObjectAttribute(relationship: SfcObjectRelationship)
    SfcObjectAttribute(relationship: SfcObjectRelationship, cardinality: SfcObjectCardinality, flags: SfcObjectFlags)
    SfcObjectAttribute(relationship: SfcObjectRelationship, cardinality: SfcObjectCardinality)
    SfcObjectAttribute(containsType: Type, flags: SfcObjectFlags)
    SfcObjectAttribute(containsType: Type)
    SfcObjectAttribute(cardinality: SfcContainerCardinality, containsType: Type, flags: SfcObjectFlags)
    SfcObjectAttribute(cardinality: SfcContainerCardinality, containsType: Type)
    SfcObjectAttribute(relationship: SfcContainerRelationship, cardinality: SfcContainerCardinality, containsType: Type, flags: SfcObjectFlags)
    SfcObjectAttribute(relationship: SfcContainerRelationship, cardinality: SfcContainerCardinality, containsType: Type)
    """
    @property
    def Deploy(self) -> bool:
        """
        Get: Deploy(self: SfcObjectAttribute) -> bool
        Set: Deploy(self: SfcObjectAttribute) = value
        """
        ...

    @property
    def Design(self) -> bool:
        """
        Get: Design(self: SfcObjectAttribute) -> bool
        Set: Design(self: SfcObjectAttribute) = value
        """
        ...

    @property
    def Flags(self) -> SfcObjectFlags:
        """
        Get: Flags(self: SfcObjectAttribute) -> SfcObjectFlags
        Set: Flags(self: SfcObjectAttribute) = value
        """
        ...

    @property
    def NaturalOrder(self) -> bool:
        """
        Get: NaturalOrder(self: SfcObjectAttribute) -> bool
        Set: NaturalOrder(self: SfcObjectAttribute) = value
        """
        ...



class SfcObjectCardinality(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SfcObjectCardinality, values: One (0), ZeroToOne (1) """
    One: SfcObjectCardinality = ...
    value__ = ...
    ZeroToOne: SfcObjectCardinality = ...


class SfcObjectFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SfcObjectFlags, values: Deploy (64), Design (32), NaturalOrder (16), None (0) """
    Deploy: SfcObjectFlags = ...
    Design: SfcObjectFlags = ...
    NaturalOrder: SfcObjectFlags = ...
    value__ = ...


class SfcObjectNotFoundException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcObjectNotFoundException()
    SfcObjectNotFoundException(message: str)
    SfcObjectNotFoundException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SfcObjectRelationship(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SfcObjectRelationship, values: ChildObject (2), Object (0), ParentObject (1) """
    ChildObject: SfcObjectRelationship = ...
    Object: SfcObjectRelationship = ...
    ParentObject: SfcObjectRelationship = ...
    value__ = ...


class SfcParentAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    SfcParentAttribute()
    SfcParentAttribute(parentName: str)
    """
    @property
    def Parent(self) -> str:
        """ Get: Parent(self: SfcParentAttribute) -> str """
        ...


    def __new__(cls, parentName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parentName: str)
        """
        ...


class SfcPropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    SfcPropertyAttribute()
    SfcPropertyAttribute(flags: SfcPropertyFlags)
    SfcPropertyAttribute(flags: SfcPropertyFlags, defaultValue: str)
    """
    @property
    def Computed(self) -> bool:
        """
        Get: Computed(self: SfcPropertyAttribute) -> bool
        Set: Computed(self: SfcPropertyAttribute) = value
        """
        ...

    @property
    def Data(self) -> bool:
        """
        Get: Data(self: SfcPropertyAttribute) -> bool
        Set: Data(self: SfcPropertyAttribute) = value
        """
        ...

    @property
    def DefaultValue(self) -> str:
        """ Get: DefaultValue(self: SfcPropertyAttribute) -> str """
        ...

    @property
    def Deploy(self) -> bool:
        """
        Get: Deploy(self: SfcPropertyAttribute) -> bool
        Set: Deploy(self: SfcPropertyAttribute) = value
        """
        ...

    @property
    def Design(self) -> bool:
        """
        Get: Design(self: SfcPropertyAttribute) -> bool
        Set: Design(self: SfcPropertyAttribute) = value
        """
        ...

    @property
    def Encrypted(self) -> bool:
        """
        Get: Encrypted(self: SfcPropertyAttribute) -> bool
        Set: Encrypted(self: SfcPropertyAttribute) = value
        """
        ...

    @property
    def Expensive(self) -> bool:
        """
        Get: Expensive(self: SfcPropertyAttribute) -> bool
        Set: Expensive(self: SfcPropertyAttribute) = value
        """
        ...

    @property
    def Flags(self) -> SfcPropertyFlags:
        """
        Get: Flags(self: SfcPropertyAttribute) -> SfcPropertyFlags
        Set: Flags(self: SfcPropertyAttribute) = value
        """
        ...

    @property
    def ReadOnlyAfterCreation(self) -> bool:
        """
        Get: ReadOnlyAfterCreation(self: SfcPropertyAttribute) -> bool
        Set: ReadOnlyAfterCreation(self: SfcPropertyAttribute) = value
        """
        ...

    @property
    def Required(self) -> bool:
        """
        Get: Required(self: SfcPropertyAttribute) -> bool
        Set: Required(self: SfcPropertyAttribute) = value
        """
        ...

    @property
    def SqlAzureDatabase(self) -> bool:
        """
        Get: SqlAzureDatabase(self: SfcPropertyAttribute) -> bool
        Set: SqlAzureDatabase(self: SfcPropertyAttribute) = value
        """
        ...

    @property
    def Standalone(self) -> bool:
        """
        Get: Standalone(self: SfcPropertyAttribute) -> bool
        Set: Standalone(self: SfcPropertyAttribute) = value
        """
        ...


    def __new__(cls, flags:SfcPropertyFlags = ..., defaultValue:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, flags: SfcPropertyFlags)
        __new__(cls: type, flags: SfcPropertyFlags, defaultValue: str)
        """
        ...


class SfcPropertyFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SfcPropertyFlags, values: Computed (64), Data (512), Deploy (8192), Design (4096), Encrypted (128), Expensive (32), None (0), ReadOnlyAfterCreation (256), Required (16), SqlAzureDatabase (2048), Standalone (1024) """
    Computed: SfcPropertyFlags = ...
    Data: SfcPropertyFlags = ...
    Deploy: SfcPropertyFlags = ...
    Design: SfcPropertyFlags = ...
    Encrypted: SfcPropertyFlags = ...
    Expensive: SfcPropertyFlags = ...
    ReadOnlyAfterCreation: SfcPropertyFlags = ...
    Required: SfcPropertyFlags = ...
    SqlAzureDatabase: SfcPropertyFlags = ...
    Standalone: SfcPropertyFlags = ...
    value__ = ...


class SfcReferenceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    SfcReferenceAttribute(resolverType: Type)
    SfcReferenceAttribute(resolverType: Type, parameters: Array[str])
    SfcReferenceAttribute(referenceType: Type, urnTemplate: str, *parameters: Array[str])
    SfcReferenceAttribute(referenceType: Type, resolverType: Type, methodName: str, *parameters: Array[str])
    SfcReferenceAttribute(referenceType: Type, keys: Array[str], urnTemplate: str, *parameters: Array[str])
    SfcReferenceAttribute(referenceType: Type, keys: Array[str], resolverType: Type, methodName: str, *parameters: Array[str])
    """
    @property
    def Arguments(self) -> Array:
        """ Get: Arguments(self: SfcReferenceAttribute) -> Array[str] """
        ...

    @property
    def InstanceResolver(self) -> ISfcReferenceResolver:
        """ Get: InstanceResolver(self: SfcReferenceAttribute) -> ISfcReferenceResolver """
        ...

    @property
    def Keys(self) -> Array:
        """
        Get: Keys(self: SfcReferenceAttribute) -> Array[str]
        Set: Keys(self: SfcReferenceAttribute) = value
        """
        ...

    @property
    def Resolver(self) -> Delegate:
        """ Get: Resolver(self: SfcReferenceAttribute) -> Delegate """
        ...

    @property
    def Type(self) -> Type:
        """
        Get: Type(self: SfcReferenceAttribute) -> Type
        Set: Type(self: SfcReferenceAttribute) = value
        """
        ...

    @property
    def UrnTemplate(self) -> str:
        """ Get: UrnTemplate(self: SfcReferenceAttribute) -> str """
        ...


    def GetUrn(self, instance:object) -> Urn:
        """ GetUrn(self: SfcReferenceAttribute, instance: object) -> Urn """
        ...

    def Resolve(self, instance:object) -> object:
        """
        Resolve(self: SfcReferenceAttribute, instance: object) -> object
        Resolve[(T, S)](self: SfcReferenceAttribute, instance: S) -> T
        """
        ...

    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type, resolverType: Type)
        __new__(cls: type, resolverType: Type, parameters: Array[str])
        __new__(cls: type, referenceType: Type, urnTemplate: str, *parameters: Array[str])
        __new__(cls: type, referenceType: Type, resolverType: Type, methodName: str, *parameters: Array[str])
        __new__(cls: type, referenceType: Type, keys: Array[str], urnTemplate: str, *parameters: Array[str])
        __new__(cls: type, referenceType: Type, keys: Array[str], resolverType: Type, methodName: str, *parameters: Array[str])
        """
        ...


class SfcReferenceCollectionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    SfcReferenceCollectionAttribute(resolverType: Type)
    SfcReferenceCollectionAttribute(resolverType: Type, *parameters: Array[str])
    """
    @property
    def Arguments(self) -> Array:
        """ Get: Arguments(self: SfcReferenceCollectionAttribute) -> Array[str] """
        ...

    @property
    def CollectionResolver(self) -> ISfcReferenceCollectionResolver:
        """ Get: CollectionResolver(self: SfcReferenceCollectionAttribute) -> ISfcReferenceCollectionResolver """
        ...


    def ResolveCollection(self, instance:object) -> IEnumerable:
        """
        ResolveCollection(self: SfcReferenceCollectionAttribute, instance: object) -> IEnumerable
        ResolveCollection[(T, S)](self: SfcReferenceCollectionAttribute, instance: S) -> IEnumerable[T]
        """
        ...

    def __new__(cls, resolverType:Type, parameters:Array = ...) -> Self:
        """
        __new__(cls: type, resolverType: Type)
        __new__(cls: type, resolverType: Type, *parameters: Array[str])
        """
        ...


class SfcReferenceCollectionResolverFactoryDelegate(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SfcReferenceCollectionResolverFactoryDelegate(object: object, method: IntPtr) """
    def BeginInvoke(self, parameters:Array, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SfcReferenceCollectionResolverFactoryDelegate, parameters: Array[str], callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> ISfcReferenceCollectionResolver:
        """ EndInvoke(self: SfcReferenceCollectionResolverFactoryDelegate, result: IAsyncResult) -> ISfcReferenceCollectionResolver """
        ...

    def Invoke(self, parameters:Array) -> ISfcReferenceCollectionResolver:
        """ Invoke(self: SfcReferenceCollectionResolverFactoryDelegate, parameters: Array[str]) -> ISfcReferenceCollectionResolver """
        ...


class SfcReferenceResolverFactoryDelegate(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SfcReferenceResolverFactoryDelegate(object: object, method: IntPtr) """
    def BeginInvoke(self, parameters:Array, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SfcReferenceResolverFactoryDelegate, parameters: Array[str], callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> ISfcReferenceResolver:
        """ EndInvoke(self: SfcReferenceResolverFactoryDelegate, result: IAsyncResult) -> ISfcReferenceResolver """
        ...

    def Invoke(self, parameters:Array) -> ISfcReferenceResolver:
        """ Invoke(self: SfcReferenceResolverFactoryDelegate, parameters: Array[str]) -> ISfcReferenceResolver """
        ...


class SfcReferenceSelectorAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SfcReferenceSelectorAttribute(pathExpression: str, field: str, *parameters: Array[str]) """
    @property
    def Arguments(self) -> Array:
        """ Get: Arguments(self: SfcReferenceSelectorAttribute) -> Array[object] """
        ...

    @property
    def Field(self) -> str:
        """ Get: Field(self: SfcReferenceSelectorAttribute) -> str """
        ...

    @property
    def PathExpression(self) -> str:
        """ Get: PathExpression(self: SfcReferenceSelectorAttribute) -> str """
        ...


    def __new__(cls, pathExpression:str, field:str, parameters:Array) -> Self:
        """ __new__(cls: type, pathExpression: str, field: str, *parameters: Array[str]) """
        ...


class SfcRelationship(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SfcRelationship, values: ChildContainer (4), ChildObject (3), Ignore (6), None (0), Object (1), ObjectContainer (2), ParentObject (5) """
    ChildContainer: SfcRelationship = ...
    ChildObject: SfcRelationship = ...
    Ignore: SfcRelationship = ...
    Object: SfcRelationship = ...
    ObjectContainer: SfcRelationship = ...
    ParentObject: SfcRelationship = ...
    value__ = ...


class SfcSerializationAdapterAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SfcSerializationAdapterAttribute(adapterType: Type) """
    @property
    def SfcSerializationAdapterType(self) -> Type:
        """ Get: SfcSerializationAdapterType(self: SfcSerializationAdapterAttribute) -> Type """
        ...


    def __new__(cls, adapterType:Type) -> Self:
        """ __new__(cls: type, adapterType: Type) """
        ...


class SfcSkuAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    SfcSkuAttribute(skuName: str, exclusive: bool)
    SfcSkuAttribute(skuNames: Array[str], exclusive: bool)
    """
    @property
    def Exclusive(self) -> bool:
        """ Get: Exclusive(self: SfcSkuAttribute) -> bool """
        ...

    @property
    def SkuNames(self) -> Array:
        """ Get: SkuNames(self: SfcSkuAttribute) -> Array[str] """
        ...


    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, skuName: str, exclusive: bool)
        __new__(cls: type, skuNames: Array[str], exclusive: bool)
        """
        ...


class SfcVersionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    SfcVersionAttribute(beginMajor: int, beginMinor: int, beginBuild: int, beginRevision: int, endMajor: int, endMinor: int, endBuild: int, endRevision: int)
    SfcVersionAttribute(beginMajor: int, beginMinor: int, beginBuild: int, beginRevision: int)
    SfcVersionAttribute(beginMajor: int, endMajor: int)
    SfcVersionAttribute(beginMajor: int)
    """
    @property
    def BeginVersion(self) -> Version:
        """ Get: BeginVersion(self: SfcVersionAttribute) -> Version """
        ...

    @property
    def EndVersion(self) -> Version:
        """ Get: EndVersion(self: SfcVersionAttribute) -> Version """
        ...


    def __new__(cls, beginMajor:int, *__args:int) -> Self:
        """
        __new__(cls: type, beginMajor: int, beginMinor: int, beginBuild: int, beginRevision: int, endMajor: int, endMinor: int, endBuild: int, endRevision: int)
        __new__(cls: type, beginMajor: int, beginMinor: int, beginBuild: int, beginRevision: int)
        __new__(cls: type, beginMajor: int, endMajor: int)
        __new__(cls: type, beginMajor: int)
        """
        ...


