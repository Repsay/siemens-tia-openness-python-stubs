# encoding: utf-8
# module System.Data.Objects.DataClasses calls itself DataClasses
# from System.Data.Entity, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute, Enum, Type

from System.Collections import ICollection, IEnumerable, IEnumerator

from System.ComponentModel import (IListSource, INotifyPropertyChanged, 
    INotifyPropertyChanging)

from System.Data import EntityKey, EntityState

from System.Data.Metadata.Edm import (RelationshipMultiplicity, 
    RelationshipSet)

from System.Data.Objects import MergeOption

from System.Management import ObjectQuery

from System.Runtime.Serialization import StreamingContext

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class StructuralObject(INotifyPropertyChanging, INotifyPropertyChanged): # skipped bases: <type 'object'>
    """ no doc """
    def BinaryEquals(self, *args): #cannot find CLR method
        """ BinaryEquals(first: Array[Byte], second: Array[Byte]) -> bool """
        ...

    def DefaultDateTimeValue(self, *args): #cannot find CLR method
        """ DefaultDateTimeValue() -> DateTime """
        ...

    def GetValidValue(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """ OnPropertyChanged(self: StructuralObject, property: str) """
        ...

    def OnPropertyChanging(self, *args): #cannot find CLR method
        """ OnPropertyChanging(self: StructuralObject, property: str) """
        ...

    def ReportPropertyChanged(self, *args): #cannot find CLR method
        """ ReportPropertyChanged(self: StructuralObject, property: str) """
        ...

    def ReportPropertyChanging(self, *args): #cannot find CLR method
        """ ReportPropertyChanging(self: StructuralObject, property: str) """
        ...

    def SetValidValue(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def VerifyComplexObjectIsNotNull(self, *args): #cannot find CLR method
        """ no doc """
        ...

    EntityKeyPropertyName: str = ...
    PropertyChanged = ...
    PropertyChanging = ...


class ComplexObject(StructuralObject): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'INotifyPropertyChanging'>, <type 'object'>
    """ no doc """
    pass

class EdmPropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    pass

class EdmComplexPropertyAttribute(EdmPropertyAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EdmComplexPropertyAttribute() """
    pass

class EdmTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: EdmTypeAttribute) -> str
        Set: Name(self: EdmTypeAttribute) = value
        """
        ...

    @property
    def NamespaceName(self) -> str:
        """
        Get: NamespaceName(self: EdmTypeAttribute) -> str
        Set: NamespaceName(self: EdmTypeAttribute) = value
        """
        ...



class EdmComplexTypeAttribute(EdmTypeAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EdmComplexTypeAttribute() """
    pass

class EdmEntityTypeAttribute(EdmTypeAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EdmEntityTypeAttribute() """
    pass

class EdmEnumTypeAttribute(EdmTypeAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EdmEnumTypeAttribute() """
    pass

class EdmFunctionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EdmFunctionAttribute(namespaceName: str, functionName: str) """
    @property
    def FunctionName(self) -> str:
        """ Get: FunctionName(self: EdmFunctionAttribute) -> str """
        ...

    @property
    def NamespaceName(self) -> str:
        """ Get: NamespaceName(self: EdmFunctionAttribute) -> str """
        ...


    def __new__(cls, namespaceName:str, functionName:str) -> Self:
        """ __new__(cls: type, namespaceName: str, functionName: str) """
        ...


class EdmRelationshipAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    EdmRelationshipAttribute(relationshipNamespaceName: str, relationshipName: str, role1Name: str, role1Multiplicity: RelationshipMultiplicity, role1Type: Type, role2Name: str, role2Multiplicity: RelationshipMultiplicity, role2Type: Type)
    EdmRelationshipAttribute(relationshipNamespaceName: str, relationshipName: str, role1Name: str, role1Multiplicity: RelationshipMultiplicity, role1Type: Type, role2Name: str, role2Multiplicity: RelationshipMultiplicity, role2Type: Type, isForeignKey: bool)
    """
    @property
    def IsForeignKey(self) -> bool:
        """ Get: IsForeignKey(self: EdmRelationshipAttribute) -> bool """
        ...

    @property
    def RelationshipName(self) -> str:
        """ Get: RelationshipName(self: EdmRelationshipAttribute) -> str """
        ...

    @property
    def RelationshipNamespaceName(self) -> str:
        """ Get: RelationshipNamespaceName(self: EdmRelationshipAttribute) -> str """
        ...

    @property
    def Role1Multiplicity(self) -> RelationshipMultiplicity:
        """ Get: Role1Multiplicity(self: EdmRelationshipAttribute) -> RelationshipMultiplicity """
        ...

    @property
    def Role1Name(self) -> str:
        """ Get: Role1Name(self: EdmRelationshipAttribute) -> str """
        ...

    @property
    def Role1Type(self) -> Type:
        """ Get: Role1Type(self: EdmRelationshipAttribute) -> Type """
        ...

    @property
    def Role2Multiplicity(self) -> RelationshipMultiplicity:
        """ Get: Role2Multiplicity(self: EdmRelationshipAttribute) -> RelationshipMultiplicity """
        ...

    @property
    def Role2Name(self) -> str:
        """ Get: Role2Name(self: EdmRelationshipAttribute) -> str """
        ...

    @property
    def Role2Type(self) -> Type:
        """ Get: Role2Type(self: EdmRelationshipAttribute) -> Type """
        ...


    def __new__(cls, relationshipNamespaceName:str, relationshipName:str, role1Name:str, role1Multiplicity:RelationshipMultiplicity, role1Type:Type, role2Name:str, role2Multiplicity:RelationshipMultiplicity, role2Type:Type, isForeignKey:bool = ...) -> Self:
        """
        __new__(cls: type, relationshipNamespaceName: str, relationshipName: str, role1Name: str, role1Multiplicity: RelationshipMultiplicity, role1Type: Type, role2Name: str, role2Multiplicity: RelationshipMultiplicity, role2Type: Type)
        __new__(cls: type, relationshipNamespaceName: str, relationshipName: str, role1Name: str, role1Multiplicity: RelationshipMultiplicity, role1Type: Type, role2Name: str, role2Multiplicity: RelationshipMultiplicity, role2Type: Type, isForeignKey: bool)
        """
        ...


class EdmRelationshipNavigationPropertyAttribute(EdmPropertyAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EdmRelationshipNavigationPropertyAttribute(relationshipNamespaceName: str, relationshipName: str, targetRoleName: str) """
    @property
    def RelationshipName(self) -> str:
        """ Get: RelationshipName(self: EdmRelationshipNavigationPropertyAttribute) -> str """
        ...

    @property
    def RelationshipNamespaceName(self) -> str:
        """ Get: RelationshipNamespaceName(self: EdmRelationshipNavigationPropertyAttribute) -> str """
        ...

    @property
    def TargetRoleName(self) -> str:
        """ Get: TargetRoleName(self: EdmRelationshipNavigationPropertyAttribute) -> str """
        ...


    def __new__(cls, relationshipNamespaceName:str, relationshipName:str, targetRoleName:str) -> Self:
        """ __new__(cls: type, relationshipNamespaceName: str, relationshipName: str, targetRoleName: str) """
        ...


class EdmScalarPropertyAttribute(EdmPropertyAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EdmScalarPropertyAttribute() """
    @property
    def EntityKeyProperty(self) -> bool:
        """
        Get: EntityKeyProperty(self: EdmScalarPropertyAttribute) -> bool
        Set: EntityKeyProperty(self: EdmScalarPropertyAttribute) = value
        """
        ...

    @property
    def IsNullable(self) -> bool:
        """
        Get: IsNullable(self: EdmScalarPropertyAttribute) -> bool
        Set: IsNullable(self: EdmScalarPropertyAttribute) = value
        """
        ...



class EdmSchemaAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    EdmSchemaAttribute()
    EdmSchemaAttribute(assemblyGuid: str)
    """
    def __new__(cls, assemblyGuid:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, assemblyGuid: str)
        """
        ...


class RelatedEnd(IRelatedEnd): # skipped bases: <type 'object'>
    """ no doc """
    def OnDeserialized(self, context:StreamingContext): # -> 
        """ OnDeserialized(self: RelatedEnd, context: StreamingContext) """
        ...

    AssociationChanged = ...


class EntityCollection(IListSource, RelatedEnd, ICollection): # skipped bases: <type 'IRelatedEnd'>, <type 'IEnumerable[TEntity]'>, <type 'IEnumerable'>, <type 'object'>
    """ EntityCollection[TEntity]() """
    def Attach(self, *__args:IEnumerable): # -> 
        """ Attach(self: EntityCollection[TEntity], entities: IEnumerable[TEntity])Attach(self: EntityCollection[TEntity], entity: TEntity) """
        ...

    def CreateSourceQuery(self) -> ObjectQuery:
        """ CreateSourceQuery(self: EntityCollection[TEntity]) -> ObjectQuery[TEntity] """
        ...

    def OnCollectionDeserialized(self, context:StreamingContext): # -> 
        """ OnCollectionDeserialized(self: EntityCollection[TEntity], context: StreamingContext) """
        ...

    def OnSerializing(self, context:StreamingContext): # -> 
        """ OnSerializing(self: EntityCollection[TEntity], context: StreamingContext) """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class IEntityWithChangeTracker: # skipped bases: <type 'object'>
    """ no doc """
    def SetChangeTracker(self, changeTracker:IEntityChangeTracker): # -> 
        """ SetChangeTracker(self: IEntityWithChangeTracker, changeTracker: IEntityChangeTracker) """
        ...


class IEntityWithKey: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def EntityKey(self) -> EntityKey:
        """
        Get: EntityKey(self: IEntityWithKey) -> EntityKey
        Set: EntityKey(self: IEntityWithKey) = value
        """
        ...



class IEntityWithRelationships: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RelationshipManager(self) -> RelationshipManager:
        """ Get: RelationshipManager(self: IEntityWithRelationships) -> RelationshipManager """
        ...



class EntityObject(IEntityWithKey, IEntityWithRelationships, StructuralObject, IEntityWithChangeTracker): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'INotifyPropertyChanging'>, <type 'object'>
    """ no doc """
    @property
    def EntityState(self) -> EntityState:
        """ Get: EntityState(self: EntityObject) -> EntityState """
        ...



class EntityReference: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def EntityKey(self) -> EntityKey:
        """
        Get: EntityKey(self: EntityReference) -> EntityKey
        Set: EntityKey(self: EntityReference) = value
        """
        ...


    def __reduce_ex__(self, *args): #cannot find CLR method
        ...


class IEntityChangeTracker: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def EntityState(self) -> EntityState:
        """ Get: EntityState(self: IEntityChangeTracker) -> EntityState """
        ...


    def EntityComplexMemberChanged(self, entityMemberName:str, complexObject:object, complexObjectMemberName:str): # -> 
        """ EntityComplexMemberChanged(self: IEntityChangeTracker, entityMemberName: str, complexObject: object, complexObjectMemberName: str) """
        ...

    def EntityComplexMemberChanging(self, entityMemberName:str, complexObject:object, complexObjectMemberName:str): # -> 
        """ EntityComplexMemberChanging(self: IEntityChangeTracker, entityMemberName: str, complexObject: object, complexObjectMemberName: str) """
        ...

    def EntityMemberChanged(self, entityMemberName:str): # -> 
        """ EntityMemberChanged(self: IEntityChangeTracker, entityMemberName: str) """
        ...

    def EntityMemberChanging(self, entityMemberName:str): # -> 
        """ EntityMemberChanging(self: IEntityChangeTracker, entityMemberName: str) """
        ...


class IRelatedEnd: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsLoaded(self) -> bool:
        """ Get: IsLoaded(self: IRelatedEnd) -> bool """
        ...

    @property
    def RelationshipName(self) -> str:
        """ Get: RelationshipName(self: IRelatedEnd) -> str """
        ...

    @property
    def RelationshipSet(self) -> RelationshipSet:
        """ Get: RelationshipSet(self: IRelatedEnd) -> RelationshipSet """
        ...

    @property
    def SourceRoleName(self) -> str:
        """ Get: SourceRoleName(self: IRelatedEnd) -> str """
        ...

    @property
    def TargetRoleName(self) -> str:
        """ Get: TargetRoleName(self: IRelatedEnd) -> str """
        ...


    def Add(self, entity:IEntityWithRelationships): # -> 
        """ Add(self: IRelatedEnd, entity: IEntityWithRelationships)Add(self: IRelatedEnd, entity: object) """
        ...

    def Attach(self, entity:IEntityWithRelationships): # -> 
        """ Attach(self: IRelatedEnd, entity: IEntityWithRelationships)Attach(self: IRelatedEnd, entity: object) """
        ...

    def CreateSourceQuery(self) -> IEnumerable:
        """ CreateSourceQuery(self: IRelatedEnd) -> IEnumerable """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: IRelatedEnd) -> IEnumerator """
        ...

    def Load(self, mergeOption:MergeOption = ...): # -> 
        """ Load(self: IRelatedEnd)Load(self: IRelatedEnd, mergeOption: MergeOption) """
        ...

    def Remove(self, entity:IEntityWithRelationships) -> bool:
        """
        Remove(self: IRelatedEnd, entity: IEntityWithRelationships) -> bool
        Remove(self: IRelatedEnd, entity: object) -> bool
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...


class RelationshipKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RelationshipKind, values: Association (0) """
    Association: RelationshipKind = ...
    value__ = ...


class RelationshipManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Create(owner:IEntityWithRelationships) -> RelationshipManager:
        """ Create(owner: IEntityWithRelationships) -> RelationshipManager """
        ...

    def GetAllRelatedEnds(self) -> IEnumerable:
        """ GetAllRelatedEnds(self: RelationshipManager) -> IEnumerable[IRelatedEnd] """
        ...

    def GetRelatedCollection(self, relationshipName:str, targetRoleName:str) -> EntityCollection:
        """ GetRelatedCollection[TTargetEntity](self: RelationshipManager, relationshipName: str, targetRoleName: str) -> EntityCollection[TTargetEntity] """
        ...

    def GetRelatedEnd(self, relationshipName:str, targetRoleName:str) -> IRelatedEnd:
        """ GetRelatedEnd(self: RelationshipManager, relationshipName: str, targetRoleName: str) -> IRelatedEnd """
        ...

    def GetRelatedReference(self, relationshipName:str, targetRoleName:str) -> EntityReference:
        """ GetRelatedReference[TTargetEntity](self: RelationshipManager, relationshipName: str, targetRoleName: str) -> EntityReference[TTargetEntity] """
        ...

    def InitializeRelatedCollection(self, relationshipName:str, targetRoleName:str, entityCollection:EntityCollection): # -> 
        """ InitializeRelatedCollection[TTargetEntity](self: RelationshipManager, relationshipName: str, targetRoleName: str, entityCollection: EntityCollection[TTargetEntity]) """
        ...

    def InitializeRelatedReference(self, relationshipName:str, targetRoleName:str, entityReference:EntityReference): # -> 
        """ InitializeRelatedReference[TTargetEntity](self: RelationshipManager, relationshipName: str, targetRoleName: str, entityReference: EntityReference[TTargetEntity]) """
        ...

    def OnDeserialized(self, context:StreamingContext): # -> 
        """ OnDeserialized(self: RelationshipManager, context: StreamingContext) """
        ...

    def OnSerializing(self, context:StreamingContext): # -> 
        """ OnSerializing(self: RelationshipManager, context: StreamingContext) """
        ...


