# encoding: utf-8
# module System.Data.Metadata.Edm calls itself Edm
# from System.Data.Entity, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Action, Byte, Enum, Nullable, Type

from System.Collections import IEnumerable

from System.Collections.ObjectModel import ReadOnlyCollection

from System.Data.Common.CommandTrees import DbExpression, DbQueryCommandTree

from System.Data.Common.EntitySql import EntitySqlParser

from System.Reflection import Assembly

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: T, field#
"""

# no functions
# classes

class MetadataItem: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BuiltInTypeKind(self) -> BuiltInTypeKind:
        """ Get: BuiltInTypeKind(self: MetadataItem) -> BuiltInTypeKind """
        ...

    @property
    def Documentation(self) -> Documentation:
        """
        Get: Documentation(self: MetadataItem) -> Documentation
        Set: Documentation(self: MetadataItem) = value
        """
        ...

    @property
    def MetadataProperties(self) -> ReadOnlyMetadataCollection:
        """ Get: MetadataProperties(self: MetadataItem) -> ReadOnlyMetadataCollection[MetadataProperty] """
        ...


    @staticmethod
    def GetBuiltInType(builtInTypeKind:BuiltInTypeKind) -> EdmType:
        """ GetBuiltInType(builtInTypeKind: BuiltInTypeKind) -> EdmType """
        ...

    @staticmethod
    def GetGeneralFacetDescriptions() -> ReadOnlyCollection:
        """ GetGeneralFacetDescriptions() -> ReadOnlyCollection[FacetDescription] """
        ...


class EdmMember(MetadataItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DeclaringType(self) -> StructuralType:
        """ Get: DeclaringType(self: EdmMember) -> StructuralType """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: EdmMember) -> str """
        ...

    @property
    def TypeUsage(self) -> TypeUsage:
        """ Get: TypeUsage(self: EdmMember) -> TypeUsage """
        ...


    def ToString(self) -> str:
        """ ToString(self: EdmMember) -> str """
        ...


class RelationshipEndMember(EdmMember): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DeleteBehavior(self) -> OperationAction:
        """ Get: DeleteBehavior(self: RelationshipEndMember) -> OperationAction """
        ...

    @property
    def RelationshipMultiplicity(self) -> RelationshipMultiplicity:
        """ Get: RelationshipMultiplicity(self: RelationshipEndMember) -> RelationshipMultiplicity """
        ...


    def GetEntityType(self) -> EntityType:
        """ GetEntityType(self: RelationshipEndMember) -> EntityType """
        ...


class AssociationEndMember(RelationshipEndMember): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BuiltInTypeKind(self) -> BuiltInTypeKind:
        """ Get: BuiltInTypeKind(self: AssociationEndMember) -> BuiltInTypeKind """
        ...



class EntitySetBase(MetadataItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ElementType(self) -> EntityTypeBase:
        """ Get: ElementType(self: EntitySetBase) -> EntityTypeBase """
        ...

    @property
    def EntityContainer(self) -> EntityContainer:
        """ Get: EntityContainer(self: EntitySetBase) -> EntityContainer """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: EntitySetBase) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: EntitySetBase) -> str """
        ...


class RelationshipSet(EntitySetBase): # skipped bases: <type 'object'>
    """ no doc """
    pass

class AssociationSet(RelationshipSet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AssociationSetEnds(self) -> ReadOnlyMetadataCollection:
        """ Get: AssociationSetEnds(self: AssociationSet) -> ReadOnlyMetadataCollection[AssociationSetEnd] """
        ...



class AssociationSetEnd(MetadataItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CorrespondingAssociationEndMember(self) -> AssociationEndMember:
        """ Get: CorrespondingAssociationEndMember(self: AssociationSetEnd) -> AssociationEndMember """
        ...

    @property
    def EntitySet(self) -> EntitySet:
        """ Get: EntitySet(self: AssociationSetEnd) -> EntitySet """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: AssociationSetEnd) -> str """
        ...

    @property
    def ParentAssociationSet(self) -> AssociationSet:
        """ Get: ParentAssociationSet(self: AssociationSetEnd) -> AssociationSet """
        ...

    @property
    def Role(self) -> str:
        """ Get: Role(self: AssociationSetEnd) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: AssociationSetEnd) -> str """
        ...


class GlobalItem(MetadataItem): # skipped bases: <type 'object'>
    """ no doc """
    pass

class EdmType(GlobalItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Abstract(self) -> bool:
        """ Get: Abstract(self: EdmType) -> bool """
        ...

    @property
    def BaseType(self) -> EdmType:
        """ Get: BaseType(self: EdmType) -> EdmType """
        ...

    @property
    def FullName(self) -> str:
        """ Get: FullName(self: EdmType) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: EdmType) -> str """
        ...

    @property
    def NamespaceName(self) -> str:
        """ Get: NamespaceName(self: EdmType) -> str """
        ...


    def GetCollectionType(self) -> CollectionType:
        """ GetCollectionType(self: EdmType) -> CollectionType """
        ...

    def ToString(self) -> str:
        """ ToString(self: EdmType) -> str """
        ...


class StructuralType(EdmType): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Members(self) -> ReadOnlyMetadataCollection:
        """ Get: Members(self: StructuralType) -> ReadOnlyMetadataCollection[EdmMember] """
        ...



class EntityTypeBase(StructuralType): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def KeyMembers(self) -> ReadOnlyMetadataCollection:
        """ Get: KeyMembers(self: EntityTypeBase) -> ReadOnlyMetadataCollection[EdmMember] """
        ...



class RelationshipType(EntityTypeBase): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RelationshipEndMembers(self) -> ReadOnlyMetadataCollection:
        """ Get: RelationshipEndMembers(self: RelationshipType) -> ReadOnlyMetadataCollection[RelationshipEndMember] """
        ...



class AssociationType(RelationshipType): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AssociationEndMembers(self) -> ReadOnlyMetadataCollection:
        """ Get: AssociationEndMembers(self: AssociationType) -> ReadOnlyMetadataCollection[AssociationEndMember] """
        ...

    @property
    def BuiltInTypeKind(self) -> BuiltInTypeKind:
        """ Get: BuiltInTypeKind(self: AssociationType) -> BuiltInTypeKind """
        ...

    @property
    def IsForeignKey(self) -> bool:
        """ Get: IsForeignKey(self: AssociationType) -> bool """
        ...

    @property
    def ReferentialConstraints(self) -> ReadOnlyMetadataCollection:
        """ Get: ReferentialConstraints(self: AssociationType) -> ReadOnlyMetadataCollection[ReferentialConstraint] """
        ...



class BuiltInTypeKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BuiltInTypeKind, values: AssociationEndMember (0), AssociationSet (2), AssociationSetEnd (1), AssociationType (3), CollectionKind (7), CollectionType (6), ComplexType (8), Documentation (9), EdmFunction (18), EdmMember (24), EdmProperty (28), EdmType (11), EntityContainer (12), EntitySet (13), EntitySetBase (4), EntityType (14), EntityTypeBase (5), EnumMember (16), EnumType (15), Facet (17), FunctionParameter (19), GlobalItem (20), MetadataItem (23), MetadataProperty (21), NavigationProperty (22), OperationAction (10), ParameterMode (25), PrimitiveType (26), PrimitiveTypeKind (27), ProviderManifest (29), ReferentialConstraint (30), RefType (31), RelationshipEndMember (32), RelationshipMultiplicity (33), RelationshipSet (34), RelationshipType (35), RowType (36), SimpleType (37), StructuralType (38), TypeUsage (39) """
    AssociationEndMember: BuiltInTypeKind = ...
    AssociationSet: BuiltInTypeKind = ...
    AssociationSetEnd: BuiltInTypeKind = ...
    AssociationType: BuiltInTypeKind = ...
    CollectionKind: BuiltInTypeKind = ...
    CollectionType: BuiltInTypeKind = ...
    ComplexType: BuiltInTypeKind = ...
    Documentation: BuiltInTypeKind = ...
    EdmFunction: BuiltInTypeKind = ...
    EdmMember: BuiltInTypeKind = ...
    EdmProperty: BuiltInTypeKind = ...
    EdmType: BuiltInTypeKind = ...
    EntityContainer: BuiltInTypeKind = ...
    EntitySet: BuiltInTypeKind = ...
    EntitySetBase: BuiltInTypeKind = ...
    EntityType: BuiltInTypeKind = ...
    EntityTypeBase: BuiltInTypeKind = ...
    EnumMember: BuiltInTypeKind = ...
    EnumType: BuiltInTypeKind = ...
    Facet: BuiltInTypeKind = ...
    FunctionParameter: BuiltInTypeKind = ...
    GlobalItem: BuiltInTypeKind = ...
    MetadataItem: BuiltInTypeKind = ...
    MetadataProperty: BuiltInTypeKind = ...
    NavigationProperty: BuiltInTypeKind = ...
    OperationAction: BuiltInTypeKind = ...
    ParameterMode: BuiltInTypeKind = ...
    PrimitiveType: BuiltInTypeKind = ...
    PrimitiveTypeKind: BuiltInTypeKind = ...
    ProviderManifest: BuiltInTypeKind = ...
    ReferentialConstraint: BuiltInTypeKind = ...
    RefType: BuiltInTypeKind = ...
    RelationshipEndMember: BuiltInTypeKind = ...
    RelationshipMultiplicity: BuiltInTypeKind = ...
    RelationshipSet: BuiltInTypeKind = ...
    RelationshipType: BuiltInTypeKind = ...
    RowType: BuiltInTypeKind = ...
    SimpleType: BuiltInTypeKind = ...
    StructuralType: BuiltInTypeKind = ...
    TypeUsage: BuiltInTypeKind = ...
    value__ = ...


class CollectionKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CollectionKind, values: Bag (1), List (2), None (0) """
    Bag: CollectionKind = ...
    List: CollectionKind = ...
    value__ = ...


class CollectionType(EdmType): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BuiltInTypeKind(self) -> BuiltInTypeKind:
        """ Get: BuiltInTypeKind(self: CollectionType) -> BuiltInTypeKind """
        ...

    @property
    def TypeUsage(self) -> TypeUsage:
        """ Get: TypeUsage(self: CollectionType) -> TypeUsage """
        ...



class ComplexType(StructuralType): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BuiltInTypeKind(self) -> BuiltInTypeKind:
        """ Get: BuiltInTypeKind(self: ComplexType) -> BuiltInTypeKind """
        ...

    @property
    def Properties(self) -> ReadOnlyMetadataCollection:
        """ Get: Properties(self: ComplexType) -> ReadOnlyMetadataCollection[EdmProperty] """
        ...



class ConcurrencyMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConcurrencyMode, values: Fixed (1), None (0) """
    Fixed: ConcurrencyMode = ...
    value__ = ...


class DataSpace(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DataSpace, values: CSpace (1), CSSpace (4), OCSpace (3), OSpace (0), SSpace (2) """
    CSpace: DataSpace = ...
    CSSpace: DataSpace = ...
    OCSpace: DataSpace = ...
    OSpace: DataSpace = ...
    SSpace: DataSpace = ...
    value__ = ...


class Documentation(MetadataItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: Documentation) -> bool """
        ...

    @property
    def LongDescription(self) -> str:
        """ Get: LongDescription(self: Documentation) -> str """
        ...

    @property
    def Summary(self) -> str:
        """ Get: Summary(self: Documentation) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: Documentation) -> str """
        ...


class EdmError: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Message(self) -> str:
        """ Get: Message(self: EdmError) -> str """
        ...



class EdmFunction(EdmType): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BuiltInTypeKind(self) -> BuiltInTypeKind:
        """ Get: BuiltInTypeKind(self: EdmFunction) -> BuiltInTypeKind """
        ...

    @property
    def CommandTextAttribute(self) -> str:
        """ Get: CommandTextAttribute(self: EdmFunction) -> str """
        ...

    @property
    def IsComposableAttribute(self) -> bool:
        """ Get: IsComposableAttribute(self: EdmFunction) -> bool """
        ...

    @property
    def Parameters(self) -> ReadOnlyMetadataCollection:
        """ Get: Parameters(self: EdmFunction) -> ReadOnlyMetadataCollection[FunctionParameter] """
        ...

    @property
    def ReturnParameter(self) -> FunctionParameter:
        """ Get: ReturnParameter(self: EdmFunction) -> FunctionParameter """
        ...

    @property
    def ReturnParameters(self) -> ReadOnlyMetadataCollection:
        """ Get: ReturnParameters(self: EdmFunction) -> ReadOnlyMetadataCollection[FunctionParameter] """
        ...



class ItemCollection(ReadOnlyMetadataCollection): # skipped bases: <type 'IList[GlobalItem]'>, <type 'IReadOnlyCollection[GlobalItem]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[GlobalItem]'>, <type 'IReadOnlyList[GlobalItem]'>, <type 'IEnumerable[GlobalItem]'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def DataSpace(self) -> DataSpace:
        """ Get: DataSpace(self: ItemCollection) -> DataSpace """
        ...


    def GetEntityContainer(self, name:str, ignoreCase:bool = ...) -> EntityContainer:
        """
        GetEntityContainer(self: ItemCollection, name: str) -> EntityContainer
        GetEntityContainer(self: ItemCollection, name: str, ignoreCase: bool) -> EntityContainer
        """
        ...

    def GetFunctions(self, functionName:str, ignoreCase:bool = ...) -> ReadOnlyCollection:
        """
        GetFunctions(self: ItemCollection, functionName: str) -> ReadOnlyCollection[EdmFunction]
        GetFunctions(self: ItemCollection, functionName: str, ignoreCase: bool) -> ReadOnlyCollection[EdmFunction]
        """
        ...

    def GetItem(self, identity:str, ignoreCase:bool = ...): # -> T
        """
        GetItem[T](self: ItemCollection, identity: str) -> T
        GetItem[T](self: ItemCollection, identity: str, ignoreCase: bool) -> T
        """
        ...

    def GetItems(self) -> ReadOnlyCollection:
        """ GetItems[T](self: ItemCollection) -> ReadOnlyCollection[T] """
        ...

    def GetType(self, name:str = ..., namespaceName:str = ..., ignoreCase:bool = ...) -> EdmType:
        """
        GetType(self: ItemCollection, name: str, namespaceName: str) -> EdmType
        GetType(self: ItemCollection, name: str, namespaceName: str, ignoreCase: bool) -> EdmType
        """
        ...

    def TryGetEntityContainer(self, name:str, *__args:bool) -> Tuple_[bool, EntityContainer]:
        """
        TryGetEntityContainer(self: ItemCollection, name: str) -> (bool, EntityContainer)
        TryGetEntityContainer(self: ItemCollection, name: str, ignoreCase: bool) -> (bool, EntityContainer)
        """
        ...

    def TryGetItem(self, identity:str, *__args:bool): # -> Tuple_[bool, T]
        """
        TryGetItem[T](self: ItemCollection, identity: str) -> (bool, T)
        TryGetItem[T](self: ItemCollection, identity: str, ignoreCase: bool) -> (bool, T)
        """
        ...

    def TryGetType(self, name:str, namespaceName:str, *__args:bool) -> Tuple_[bool, EdmType]:
        """
        TryGetType(self: ItemCollection, name: str, namespaceName: str) -> (bool, EdmType)
        TryGetType(self: ItemCollection, name: str, namespaceName: str, ignoreCase: bool) -> (bool, EdmType)
        """
        ...


class EdmItemCollection(ItemCollection): # skipped bases: <type 'IList[GlobalItem]'>, <type 'IReadOnlyCollection[GlobalItem]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[GlobalItem]'>, <type 'IReadOnlyList[GlobalItem]'>, <type 'IEnumerable[GlobalItem]'>, <type 'ICollection'>, <type 'object'>
    """
    EdmItemCollection(xmlReaders: IEnumerable[XmlReader])
    EdmItemCollection(*filePaths: Array[str])
    """
    @property
    def EdmVersion(self) -> float:
        """ Get: EdmVersion(self: EdmItemCollection) -> float """
        ...


    def GetPrimitiveTypes(self, edmVersion:float = ...) -> ReadOnlyCollection:
        """
        GetPrimitiveTypes(self: EdmItemCollection) -> ReadOnlyCollection[PrimitiveType]
        GetPrimitiveTypes(self: EdmItemCollection, edmVersion: float) -> ReadOnlyCollection[PrimitiveType]
        """
        ...

    def __new__(cls, *__args:IEnumerable) -> Self:
        """
        __new__(cls: type, xmlReaders: IEnumerable[XmlReader])
        __new__(cls: type, *filePaths: Array[str])
        """
        ...


class EdmProperty(EdmMember): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BuiltInTypeKind(self) -> BuiltInTypeKind:
        """ Get: BuiltInTypeKind(self: EdmProperty) -> BuiltInTypeKind """
        ...

    @property
    def DefaultValue(self) -> object:
        """ Get: DefaultValue(self: EdmProperty) -> object """
        ...

    @property
    def Nullable(self) -> bool:
        """ Get: Nullable(self: EdmProperty) -> bool """
        ...



class EdmSchemaError(EdmError): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Column(self) -> int:
        """ Get: Column(self: EdmSchemaError) -> int """
        ...

    @property
    def ErrorCode(self) -> int:
        """ Get: ErrorCode(self: EdmSchemaError) -> int """
        ...

    @property
    def Line(self) -> int:
        """ Get: Line(self: EdmSchemaError) -> int """
        ...

    @property
    def SchemaLocation(self) -> str:
        """ Get: SchemaLocation(self: EdmSchemaError) -> str """
        ...

    @property
    def SchemaName(self) -> str:
        """ Get: SchemaName(self: EdmSchemaError) -> str """
        ...

    @property
    def Severity(self) -> EdmSchemaErrorSeverity:
        """
        Get: Severity(self: EdmSchemaError) -> EdmSchemaErrorSeverity
        Set: Severity(self: EdmSchemaError) = value
        """
        ...

    @property
    def StackTrace(self) -> str:
        """ Get: StackTrace(self: EdmSchemaError) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: EdmSchemaError) -> str """
        ...


class EdmSchemaErrorSeverity(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EdmSchemaErrorSeverity, values: Error (1), Warning (0) """
    Error: EdmSchemaErrorSeverity = ...
    value__ = ...
    Warning: EdmSchemaErrorSeverity = ...


class EntityContainer(GlobalItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BaseEntitySets(self) -> ReadOnlyMetadataCollection:
        """ Get: BaseEntitySets(self: EntityContainer) -> ReadOnlyMetadataCollection[EntitySetBase] """
        ...

    @property
    def BuiltInTypeKind(self) -> BuiltInTypeKind:
        """ Get: BuiltInTypeKind(self: EntityContainer) -> BuiltInTypeKind """
        ...

    @property
    def FunctionImports(self) -> ReadOnlyMetadataCollection:
        """ Get: FunctionImports(self: EntityContainer) -> ReadOnlyMetadataCollection[EdmFunction] """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: EntityContainer) -> str """
        ...


    def GetEntitySetByName(self, name:str, ignoreCase:bool) -> EntitySet:
        """ GetEntitySetByName(self: EntityContainer, name: str, ignoreCase: bool) -> EntitySet """
        ...

    def GetRelationshipSetByName(self, name:str, ignoreCase:bool) -> RelationshipSet:
        """ GetRelationshipSetByName(self: EntityContainer, name: str, ignoreCase: bool) -> RelationshipSet """
        ...

    def ToString(self) -> str:
        """ ToString(self: EntityContainer) -> str """
        ...

    def TryGetEntitySetByName(self, name, ignoreCase, entitySet) -> Tuple_[bool, EntitySet]:
        """ TryGetEntitySetByName(self: EntityContainer, name: str, ignoreCase: bool) -> (bool, EntitySet) """
        ...

    def TryGetRelationshipSetByName(self, name, ignoreCase, relationshipSet) -> Tuple_[bool, RelationshipSet]:
        """ TryGetRelationshipSetByName(self: EntityContainer, name: str, ignoreCase: bool) -> (bool, RelationshipSet) """
        ...


class EntitySet(EntitySetBase): # skipped bases: <type 'object'>
    """ no doc """
    pass

class EntityType(EntityTypeBase): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BuiltInTypeKind(self) -> BuiltInTypeKind:
        """ Get: BuiltInTypeKind(self: EntityType) -> BuiltInTypeKind """
        ...

    @property
    def NavigationProperties(self) -> ReadOnlyMetadataCollection:
        """ Get: NavigationProperties(self: EntityType) -> ReadOnlyMetadataCollection[NavigationProperty] """
        ...

    @property
    def Properties(self) -> ReadOnlyMetadataCollection:
        """ Get: Properties(self: EntityType) -> ReadOnlyMetadataCollection[EdmProperty] """
        ...


    def GetReferenceType(self) -> RefType:
        """ GetReferenceType(self: EntityType) -> RefType """
        ...


class EnumMember(MetadataItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: EnumMember) -> str """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: EnumMember) -> object """
        ...


    def ToString(self) -> str:
        """ ToString(self: EnumMember) -> str """
        ...


class SimpleType(EdmType): # skipped bases: <type 'object'>
    """ no doc """
    pass

class EnumType(SimpleType): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BuiltInTypeKind(self) -> BuiltInTypeKind:
        """ Get: BuiltInTypeKind(self: EnumType) -> BuiltInTypeKind """
        ...

    @property
    def IsFlags(self) -> bool:
        """ Get: IsFlags(self: EnumType) -> bool """
        ...

    @property
    def Members(self) -> ReadOnlyMetadataCollection:
        """ Get: Members(self: EnumType) -> ReadOnlyMetadataCollection[EnumMember] """
        ...

    @property
    def UnderlyingType(self) -> PrimitiveType:
        """ Get: UnderlyingType(self: EnumType) -> PrimitiveType """
        ...



class Facet(MetadataItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Description(self) -> FacetDescription:
        """ Get: Description(self: Facet) -> FacetDescription """
        ...

    @property
    def FacetType(self) -> EdmType:
        """ Get: FacetType(self: Facet) -> EdmType """
        ...

    @property
    def IsUnbounded(self) -> bool:
        """ Get: IsUnbounded(self: Facet) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Facet) -> str """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: Facet) -> object """
        ...


    def ToString(self) -> str:
        """ ToString(self: Facet) -> str """
        ...


class FacetDescription: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DefaultValue(self) -> object:
        """ Get: DefaultValue(self: FacetDescription) -> object """
        ...

    @property
    def FacetName(self) -> str:
        """ Get: FacetName(self: FacetDescription) -> str """
        ...

    @property
    def FacetType(self) -> EdmType:
        """ Get: FacetType(self: FacetDescription) -> EdmType """
        ...

    @property
    def IsConstant(self) -> bool:
        """ Get: IsConstant(self: FacetDescription) -> bool """
        ...

    @property
    def IsRequired(self) -> bool:
        """ Get: IsRequired(self: FacetDescription) -> bool """
        ...

    @property
    def MaxValue(self) -> Nullable:
        """ Get: MaxValue(self: FacetDescription) -> Nullable[int] """
        ...

    @property
    def MinValue(self) -> Nullable:
        """ Get: MinValue(self: FacetDescription) -> Nullable[int] """
        ...


    def ToString(self) -> str:
        """ ToString(self: FacetDescription) -> str """
        ...


class FunctionParameter(MetadataItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DeclaringFunction(self) -> EdmFunction:
        """ Get: DeclaringFunction(self: FunctionParameter) -> EdmFunction """
        ...

    @property
    def Mode(self) -> ParameterMode:
        """ Get: Mode(self: FunctionParameter) -> ParameterMode """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: FunctionParameter) -> str """
        ...

    @property
    def TypeUsage(self) -> TypeUsage:
        """ Get: TypeUsage(self: FunctionParameter) -> TypeUsage """
        ...


    def ToString(self) -> str:
        """ ToString(self: FunctionParameter) -> str """
        ...


class MetadataProperty(MetadataItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: MetadataProperty) -> str """
        ...

    @property
    def PropertyKind(self) -> PropertyKind:
        """ Get: PropertyKind(self: MetadataProperty) -> PropertyKind """
        ...

    @property
    def TypeUsage(self) -> TypeUsage:
        """ Get: TypeUsage(self: MetadataProperty) -> TypeUsage """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: MetadataProperty) -> object """
        ...



class MetadataWorkspace: # skipped bases: <type 'object'>, <type 'object'>
    """
    MetadataWorkspace()
    MetadataWorkspace(paths: IEnumerable[str], assembliesToConsider: IEnumerable[Assembly])
    """
    @staticmethod
    def ClearCache(): # -> 
        """ ClearCache() """
        ...

    def CreateEntitySqlParser(self) -> EntitySqlParser:
        """ CreateEntitySqlParser(self: MetadataWorkspace) -> EntitySqlParser """
        ...

    def CreateQueryCommandTree(self, query:DbExpression) -> DbQueryCommandTree:
        """ CreateQueryCommandTree(self: MetadataWorkspace, query: DbExpression) -> DbQueryCommandTree """
        ...

    def GetEdmSpaceType(self, objectSpaceType:StructuralType) -> StructuralType:
        """
        GetEdmSpaceType(self: MetadataWorkspace, objectSpaceType: StructuralType) -> StructuralType
        GetEdmSpaceType(self: MetadataWorkspace, objectSpaceType: EnumType) -> EnumType
        """
        ...

    def GetEntityContainer(self, name:str, *__args:DataSpace) -> EntityContainer:
        """
        GetEntityContainer(self: MetadataWorkspace, name: str, dataSpace: DataSpace) -> EntityContainer
        GetEntityContainer(self: MetadataWorkspace, name: str, ignoreCase: bool, dataSpace: DataSpace) -> EntityContainer
        """
        ...

    def GetFunctions(self, name:str, namespaceName:str, dataSpace:DataSpace, ignoreCase:bool = ...) -> ReadOnlyCollection:
        """
        GetFunctions(self: MetadataWorkspace, name: str, namespaceName: str, dataSpace: DataSpace) -> ReadOnlyCollection[EdmFunction]
        GetFunctions(self: MetadataWorkspace, name: str, namespaceName: str, dataSpace: DataSpace, ignoreCase: bool) -> ReadOnlyCollection[EdmFunction]
        """
        ...

    def GetItem(self, identity:str, *__args:DataSpace): # -> T
        """
        GetItem[T](self: MetadataWorkspace, identity: str, dataSpace: DataSpace) -> T
        GetItem[T](self: MetadataWorkspace, identity: str, ignoreCase: bool, dataSpace: DataSpace) -> T
        """
        ...

    def GetItemCollection(self, dataSpace:DataSpace) -> ItemCollection:
        """ GetItemCollection(self: MetadataWorkspace, dataSpace: DataSpace) -> ItemCollection """
        ...

    def GetItems(self, dataSpace:DataSpace) -> ReadOnlyCollection:
        """
        GetItems(self: MetadataWorkspace, dataSpace: DataSpace) -> ReadOnlyCollection[GlobalItem]
        GetItems[T](self: MetadataWorkspace, dataSpace: DataSpace) -> ReadOnlyCollection[T]
        """
        ...

    def GetObjectSpaceType(self, edmSpaceType:StructuralType) -> StructuralType:
        """
        GetObjectSpaceType(self: MetadataWorkspace, edmSpaceType: StructuralType) -> StructuralType
        GetObjectSpaceType(self: MetadataWorkspace, edmSpaceType: EnumType) -> EnumType
        """
        ...

    def GetPrimitiveTypes(self, dataSpace:DataSpace) -> ReadOnlyCollection:
        """ GetPrimitiveTypes(self: MetadataWorkspace, dataSpace: DataSpace) -> ReadOnlyCollection[PrimitiveType] """
        ...

    def GetRelevantMembersForUpdate(self, entitySet:EntitySetBase, entityType:EntityTypeBase, partialUpdateSupported:bool) -> ReadOnlyCollection:
        """ GetRelevantMembersForUpdate(self: MetadataWorkspace, entitySet: EntitySetBase, entityType: EntityTypeBase, partialUpdateSupported: bool) -> ReadOnlyCollection[EdmMember] """
        ...

    def GetRequiredOriginalValueMembers(self, entitySet:EntitySetBase, entityType:EntityTypeBase) -> IEnumerable:
        """ GetRequiredOriginalValueMembers(self: MetadataWorkspace, entitySet: EntitySetBase, entityType: EntityTypeBase) -> IEnumerable[EdmMember] """
        ...

    def GetType(self, name:str = ..., namespaceName:str = ..., *__args:DataSpace) -> EdmType:
        """
        GetType(self: MetadataWorkspace, name: str, namespaceName: str, dataSpace: DataSpace) -> EdmType
        GetType(self: MetadataWorkspace, name: str, namespaceName: str, ignoreCase: bool, dataSpace: DataSpace) -> EdmType
        """
        ...

    def LoadFromAssembly(self, assembly:Assembly, logLoadMessage:Action = ...): # -> 
        """ LoadFromAssembly(self: MetadataWorkspace, assembly: Assembly)LoadFromAssembly(self: MetadataWorkspace, assembly: Assembly, logLoadMessage: Action[str]) """
        ...

    def RegisterItemCollection(self, collection:ItemCollection): # -> 
        """ RegisterItemCollection(self: MetadataWorkspace, collection: ItemCollection) """
        ...

    def TryGetEdmSpaceType(self, objectSpaceType, edmSpaceType) -> Tuple_[bool, StructuralType]:
        """
        TryGetEdmSpaceType(self: MetadataWorkspace, objectSpaceType: StructuralType) -> (bool, StructuralType)
        TryGetEdmSpaceType(self: MetadataWorkspace, objectSpaceType: EnumType) -> (bool, EnumType)
        """
        ...

    def TryGetEntityContainer(self, name:str, *__args:DataSpace) -> Tuple_[bool, EntityContainer]:
        """
        TryGetEntityContainer(self: MetadataWorkspace, name: str, dataSpace: DataSpace) -> (bool, EntityContainer)
        TryGetEntityContainer(self: MetadataWorkspace, name: str, ignoreCase: bool, dataSpace: DataSpace) -> (bool, EntityContainer)
        """
        ...

    def TryGetItem(self, identity:str, *__args:DataSpace): # -> Tuple_[bool, T]
        """
        TryGetItem[T](self: MetadataWorkspace, identity: str, space: DataSpace) -> (bool, T)
        TryGetItem[T](self: MetadataWorkspace, identity: str, ignoreCase: bool, dataSpace: DataSpace) -> (bool, T)
        """
        ...

    def TryGetItemCollection(self, dataSpace, collection) -> Tuple_[bool, ItemCollection]:
        """ TryGetItemCollection(self: MetadataWorkspace, dataSpace: DataSpace) -> (bool, ItemCollection) """
        ...

    def TryGetObjectSpaceType(self, edmSpaceType, objectSpaceType) -> Tuple_[bool, StructuralType]:
        """
        TryGetObjectSpaceType(self: MetadataWorkspace, edmSpaceType: StructuralType) -> (bool, StructuralType)
        TryGetObjectSpaceType(self: MetadataWorkspace, edmSpaceType: EnumType) -> (bool, EnumType)
        """
        ...

    def TryGetType(self, name:str, namespaceName:str, *__args:DataSpace) -> Tuple_[bool, EdmType]:
        """
        TryGetType(self: MetadataWorkspace, name: str, namespaceName: str, dataSpace: DataSpace) -> (bool, EdmType)
        TryGetType(self: MetadataWorkspace, name: str, namespaceName: str, ignoreCase: bool, dataSpace: DataSpace) -> (bool, EdmType)
        """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    MaximumEdmVersionSupported: float = ...


class NavigationProperty(EdmMember): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BuiltInTypeKind(self) -> BuiltInTypeKind:
        """ Get: BuiltInTypeKind(self: NavigationProperty) -> BuiltInTypeKind """
        ...

    @property
    def FromEndMember(self) -> RelationshipEndMember:
        """ Get: FromEndMember(self: NavigationProperty) -> RelationshipEndMember """
        ...

    @property
    def RelationshipType(self) -> RelationshipType:
        """ Get: RelationshipType(self: NavigationProperty) -> RelationshipType """
        ...

    @property
    def ToEndMember(self) -> RelationshipEndMember:
        """ Get: ToEndMember(self: NavigationProperty) -> RelationshipEndMember """
        ...


    def GetDependentProperties(self) -> IEnumerable:
        """ GetDependentProperties(self: NavigationProperty) -> IEnumerable[EdmProperty] """
        ...


class ObjectItemCollection(ItemCollection): # skipped bases: <type 'IList[GlobalItem]'>, <type 'IReadOnlyCollection[GlobalItem]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[GlobalItem]'>, <type 'IReadOnlyList[GlobalItem]'>, <type 'IEnumerable[GlobalItem]'>, <type 'ICollection'>, <type 'object'>
    """ ObjectItemCollection() """
    def GetClrType(self, objectSpaceType:StructuralType) -> Type:
        """
        GetClrType(self: ObjectItemCollection, objectSpaceType: StructuralType) -> Type
        GetClrType(self: ObjectItemCollection, objectSpaceType: EnumType) -> Type
        """
        ...

    def GetPrimitiveTypes(self) -> IEnumerable:
        """ GetPrimitiveTypes(self: ObjectItemCollection) -> IEnumerable[PrimitiveType] """
        ...

    def LoadFromAssembly(self, assembly:Assembly, edmItemCollection:EdmItemCollection = ..., logLoadMessage:Action = ...): # -> 
        """ LoadFromAssembly(self: ObjectItemCollection, assembly: Assembly)LoadFromAssembly(self: ObjectItemCollection, assembly: Assembly, edmItemCollection: EdmItemCollection, logLoadMessage: Action[str])LoadFromAssembly(self: ObjectItemCollection, assembly: Assembly, edmItemCollection: EdmItemCollection) """
        ...

    def TryGetClrType(self, objectSpaceType, clrType) -> Tuple_[bool, Type]:
        """
        TryGetClrType(self: ObjectItemCollection, objectSpaceType: StructuralType) -> (bool, Type)
        TryGetClrType(self: ObjectItemCollection, objectSpaceType: EnumType) -> (bool, Type)
        """
        ...


class OperationAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OperationAction, values: Cascade (1), None (0), Restrict (2) """
    Cascade: OperationAction = ...
    Restrict: OperationAction = ...
    value__ = ...


class ParameterMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ParameterMode, values: In (0), InOut (2), Out (1), ReturnValue (3) """
    In: ParameterMode = ...
    InOut: ParameterMode = ...
    Out: ParameterMode = ...
    ReturnValue: ParameterMode = ...
    value__ = ...


class ParameterTypeSemantics(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ParameterTypeSemantics, values: AllowImplicitConversion (0), AllowImplicitPromotion (1), ExactMatchOnly (2) """
    AllowImplicitConversion: ParameterTypeSemantics = ...
    AllowImplicitPromotion: ParameterTypeSemantics = ...
    ExactMatchOnly: ParameterTypeSemantics = ...
    value__ = ...


class PrimitiveType(SimpleType): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BuiltInTypeKind(self) -> BuiltInTypeKind:
        """ Get: BuiltInTypeKind(self: PrimitiveType) -> BuiltInTypeKind """
        ...

    @property
    def ClrEquivalentType(self) -> Type:
        """ Get: ClrEquivalentType(self: PrimitiveType) -> Type """
        ...

    @property
    def FacetDescriptions(self) -> ReadOnlyCollection:
        """ Get: FacetDescriptions(self: PrimitiveType) -> ReadOnlyCollection[FacetDescription] """
        ...

    @property
    def PrimitiveTypeKind(self) -> PrimitiveTypeKind:
        """ Get: PrimitiveTypeKind(self: PrimitiveType) -> PrimitiveTypeKind """
        ...


    def GetEdmPrimitiveType(self, primitiveTypeKind=None) -> EdmType:
        """
        GetEdmPrimitiveType(self: PrimitiveType) -> EdmType
        GetEdmPrimitiveType(primitiveTypeKind: PrimitiveTypeKind) -> PrimitiveType
        """
        ...

    @staticmethod
    def GetEdmPrimitiveTypes() -> ReadOnlyCollection:
        """ GetEdmPrimitiveTypes() -> ReadOnlyCollection[PrimitiveType] """
        ...


class PrimitiveTypeKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PrimitiveTypeKind, values: Binary (0), Boolean (1), Byte (2), DateTime (3), DateTimeOffset (14), Decimal (4), Double (5), Geography (16), GeographyCollection (30), GeographyLineString (25), GeographyMultiLineString (28), GeographyMultiPoint (27), GeographyMultiPolygon (29), GeographyPoint (24), GeographyPolygon (26), Geometry (15), GeometryCollection (23), GeometryLineString (18), GeometryMultiLineString (21), GeometryMultiPoint (20), GeometryMultiPolygon (22), GeometryPoint (17), GeometryPolygon (19), Guid (6), Int16 (9), Int32 (10), Int64 (11), SByte (8), Single (7), String (12), Time (13) """
    Binary: PrimitiveTypeKind = ...
    Boolean: PrimitiveTypeKind = ...
    Byte: PrimitiveTypeKind = ...
    DateTime: PrimitiveTypeKind = ...
    DateTimeOffset: PrimitiveTypeKind = ...
    Decimal: PrimitiveTypeKind = ...
    Double: PrimitiveTypeKind = ...
    Geography: PrimitiveTypeKind = ...
    GeographyCollection: PrimitiveTypeKind = ...
    GeographyLineString: PrimitiveTypeKind = ...
    GeographyMultiLineString: PrimitiveTypeKind = ...
    GeographyMultiPoint: PrimitiveTypeKind = ...
    GeographyMultiPolygon: PrimitiveTypeKind = ...
    GeographyPoint: PrimitiveTypeKind = ...
    GeographyPolygon: PrimitiveTypeKind = ...
    Geometry: PrimitiveTypeKind = ...
    GeometryCollection: PrimitiveTypeKind = ...
    GeometryLineString: PrimitiveTypeKind = ...
    GeometryMultiLineString: PrimitiveTypeKind = ...
    GeometryMultiPoint: PrimitiveTypeKind = ...
    GeometryMultiPolygon: PrimitiveTypeKind = ...
    GeometryPoint: PrimitiveTypeKind = ...
    GeometryPolygon: PrimitiveTypeKind = ...
    Guid: PrimitiveTypeKind = ...
    Int16: PrimitiveTypeKind = ...
    Int32: PrimitiveTypeKind = ...
    Int64: PrimitiveTypeKind = ...
    SByte: PrimitiveTypeKind = ...
    Single: PrimitiveTypeKind = ...
    String: PrimitiveTypeKind = ...
    Time: PrimitiveTypeKind = ...
    value__ = ...


class PropertyKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PropertyKind, values: Extended (1), System (0) """
    Extended: PropertyKind = ...
    System: PropertyKind = ...
    value__ = ...


class ReadOnlyMetadataCollection(ReadOnlyCollection): # skipped bases: <type 'IList[T]'>, <type 'ICollection[T]'>, <type 'IReadOnlyCollection[T]'>, <type 'IEnumerable'>, <type 'IEnumerable[T]'>, <type 'IList'>, <type 'ICollection'>, <type 'IReadOnlyList[T]'>, <type 'object'>
    """ no doc """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ReadOnlyMetadataCollection[T]) -> bool """
        ...


    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def GetValue(self, identity:str, ignoreCase:bool): # -> T
        """ GetValue(self: ReadOnlyMetadataCollection[T], identity: str, ignoreCase: bool) -> T """
        ...

    def TryGetValue(self, identity, ignoreCase, item): # -> Tuple_[bool, T]
        """ TryGetValue(self: ReadOnlyMetadataCollection[T], identity: str, ignoreCase: bool) -> (bool, T) """
        ...



class ReferentialConstraint(MetadataItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def FromProperties(self) -> ReadOnlyMetadataCollection:
        """ Get: FromProperties(self: ReferentialConstraint) -> ReadOnlyMetadataCollection[EdmProperty] """
        ...

    @property
    def FromRole(self) -> RelationshipEndMember:
        """ Get: FromRole(self: ReferentialConstraint) -> RelationshipEndMember """
        ...

    @property
    def ToProperties(self) -> ReadOnlyMetadataCollection:
        """ Get: ToProperties(self: ReferentialConstraint) -> ReadOnlyMetadataCollection[EdmProperty] """
        ...

    @property
    def ToRole(self) -> RelationshipEndMember:
        """ Get: ToRole(self: ReferentialConstraint) -> RelationshipEndMember """
        ...


    def ToString(self) -> str:
        """ ToString(self: ReferentialConstraint) -> str """
        ...


class RefType(EdmType): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BuiltInTypeKind(self) -> BuiltInTypeKind:
        """ Get: BuiltInTypeKind(self: RefType) -> BuiltInTypeKind """
        ...

    @property
    def ElementType(self) -> EntityTypeBase:
        """ Get: ElementType(self: RefType) -> EntityTypeBase """
        ...



class RelationshipMultiplicity(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RelationshipMultiplicity, values: Many (2), One (1), ZeroOrOne (0) """
    Many: RelationshipMultiplicity = ...
    One: RelationshipMultiplicity = ...
    value__ = ...
    ZeroOrOne: RelationshipMultiplicity = ...


class RowType(StructuralType): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BuiltInTypeKind(self) -> BuiltInTypeKind:
        """ Get: BuiltInTypeKind(self: RowType) -> BuiltInTypeKind """
        ...

    @property
    def Properties(self) -> ReadOnlyMetadataCollection:
        """ Get: Properties(self: RowType) -> ReadOnlyMetadataCollection[EdmProperty] """
        ...



class StoreGeneratedPattern(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum StoreGeneratedPattern, values: Computed (2), Identity (1), None (0) """
    Computed: StoreGeneratedPattern = ...
    Identity: StoreGeneratedPattern = ...
    value__ = ...


class StoreItemCollection(ItemCollection): # skipped bases: <type 'IList[GlobalItem]'>, <type 'IReadOnlyCollection[GlobalItem]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[GlobalItem]'>, <type 'IReadOnlyList[GlobalItem]'>, <type 'IEnumerable[GlobalItem]'>, <type 'ICollection'>, <type 'object'>
    """
    StoreItemCollection(xmlReaders: IEnumerable[XmlReader])
    StoreItemCollection(*filePaths: Array[str])
    """
    @property
    def StoreSchemaVersion(self) -> float:
        """ Get: StoreSchemaVersion(self: StoreItemCollection) -> float """
        ...


    def GetPrimitiveTypes(self) -> ReadOnlyCollection:
        """ GetPrimitiveTypes(self: StoreItemCollection) -> ReadOnlyCollection[PrimitiveType] """
        ...

    def __new__(cls, *__args:IEnumerable) -> Self:
        """
        __new__(cls: type, xmlReaders: IEnumerable[XmlReader])
        __new__(cls: type, *filePaths: Array[str])
        """
        ...


class TypeUsage(MetadataItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def EdmType(self) -> EdmType:
        """ Get: EdmType(self: TypeUsage) -> EdmType """
        ...

    @property
    def Facets(self) -> ReadOnlyMetadataCollection:
        """ Get: Facets(self: TypeUsage) -> ReadOnlyMetadataCollection[Facet] """
        ...


    @staticmethod
    def CreateBinaryTypeUsage(primitiveType:PrimitiveType, isFixedLength:bool, maxLength:int = ...) -> TypeUsage:
        """
        CreateBinaryTypeUsage(primitiveType: PrimitiveType, isFixedLength: bool, maxLength: int) -> TypeUsage
        CreateBinaryTypeUsage(primitiveType: PrimitiveType, isFixedLength: bool) -> TypeUsage
        """
        ...

    @staticmethod
    def CreateDateTimeOffsetTypeUsage(primitiveType:PrimitiveType, precision:Nullable) -> TypeUsage:
        """ CreateDateTimeOffsetTypeUsage(primitiveType: PrimitiveType, precision: Nullable[Byte]) -> TypeUsage """
        ...

    @staticmethod
    def CreateDateTimeTypeUsage(primitiveType:PrimitiveType, precision:Nullable) -> TypeUsage:
        """ CreateDateTimeTypeUsage(primitiveType: PrimitiveType, precision: Nullable[Byte]) -> TypeUsage """
        ...

    @staticmethod
    def CreateDecimalTypeUsage(primitiveType:PrimitiveType, precision:Byte = ..., scale:Byte = ...) -> TypeUsage:
        """
        CreateDecimalTypeUsage(primitiveType: PrimitiveType, precision: Byte, scale: Byte) -> TypeUsage
        CreateDecimalTypeUsage(primitiveType: PrimitiveType) -> TypeUsage
        """
        ...

    @staticmethod
    def CreateDefaultTypeUsage(edmType:EdmType) -> TypeUsage:
        """ CreateDefaultTypeUsage(edmType: EdmType) -> TypeUsage """
        ...

    @staticmethod
    def CreateStringTypeUsage(primitiveType:PrimitiveType, isUnicode:bool, isFixedLength:bool, maxLength:int = ...) -> TypeUsage:
        """
        CreateStringTypeUsage(primitiveType: PrimitiveType, isUnicode: bool, isFixedLength: bool, maxLength: int) -> TypeUsage
        CreateStringTypeUsage(primitiveType: PrimitiveType, isUnicode: bool, isFixedLength: bool) -> TypeUsage
        """
        ...

    @staticmethod
    def CreateTimeTypeUsage(primitiveType:PrimitiveType, precision:Nullable) -> TypeUsage:
        """ CreateTimeTypeUsage(primitiveType: PrimitiveType, precision: Nullable[Byte]) -> TypeUsage """
        ...

    def IsSubtypeOf(self, typeUsage:TypeUsage) -> bool:
        """ IsSubtypeOf(self: TypeUsage, typeUsage: TypeUsage) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: TypeUsage) -> str """
        ...


