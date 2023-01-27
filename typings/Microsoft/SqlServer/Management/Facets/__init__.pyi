# encoding: utf-8
# module Microsoft.SqlServer.Management.Facets calls itself Facets
# from Microsoft.SqlServer.Dmf, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.Dmf.Common, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Dmf import AutomatedPolicyEvaluationMode

from System import Array, Attribute, Type

from System.Collections import IEnumerable

from System.Collections.Generic import List

from typing import Self


# no functions
# classes

class EvaluationModeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EvaluationModeAttribute(evaluationModes: AutomatedPolicyEvaluationMode) """
    @property
    def AutomatedPolicyEvaluationMode(self) -> AutomatedPolicyEvaluationMode:
        """
        Get: AutomatedPolicyEvaluationMode(self: EvaluationModeAttribute) -> AutomatedPolicyEvaluationMode
        Set: AutomatedPolicyEvaluationMode(self: EvaluationModeAttribute) = value
        """
        ...

    @property
    def EvaluationModes(self) -> AutomatedPolicyEvaluationMode:
        """ Get: EvaluationModes(self: EvaluationModeAttribute) -> AutomatedPolicyEvaluationMode """
        ...


    def __new__(cls, evaluationModes:AutomatedPolicyEvaluationMode) -> Self:
        """ __new__(cls: type, evaluationModes: AutomatedPolicyEvaluationMode) """
        ...


class FacetEvaluationContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Interface(self) -> Type:
        """ Get: Interface(self: FacetEvaluationContext) -> Type """
        ...

    @property
    def Target(self) -> object:
        """ Get: Target(self: FacetEvaluationContext) -> object """
        ...


    def Alter(self): # -> 
        """ Alter(self: FacetEvaluationContext) """
        ...

    @staticmethod
    def GetFacetEvaluationContext(*__args) -> FacetEvaluationContext:
        """
        GetFacetEvaluationContext(facetName: str, target: object) -> FacetEvaluationContext
        GetFacetEvaluationContext(facetType: Type, target: object) -> FacetEvaluationContext
        """
        ...

    def GetPropertyValue(self, name:str) -> object:
        """ GetPropertyValue(self: FacetEvaluationContext, name: str) -> object """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: FacetEvaluationContext) """
        ...

    def SetPropertyValue(self, name:str, value:object): # -> 
        """ SetPropertyValue(self: FacetEvaluationContext, name: str, value: object) """
        ...


class FacetRepository: # skipped bases: <type 'object'>, <type 'object'>
    """ FacetRepository() """
    @property
    def RegisteredFacets(self) -> IEnumerable:
        """ Get: RegisteredFacets() -> IEnumerable """
        ...


    @staticmethod
    def GetFacetEvaluationMode(facet:Type) -> AutomatedPolicyEvaluationMode:
        """ GetFacetEvaluationMode(facet: Type) -> AutomatedPolicyEvaluationMode """
        ...

    @staticmethod
    def GetFacetProperties(managementFacet:Type) -> Array:
        """ GetFacetProperties(managementFacet: Type) -> Array[PropertyInfo] """
        ...

    @staticmethod
    def GetFacetsForType(target:Type) -> List:
        """ GetFacetsForType(target: Type) -> List[Type] """
        ...

    @staticmethod
    def GetFacetSupportedRootType(facet:Type) -> Type:
        """ GetFacetSupportedRootType(facet: Type) -> Type """
        ...

    @staticmethod
    def GetFacetSupportedTypes(managementFacet:Type) -> List:
        """ GetFacetSupportedTypes(managementFacet: Type) -> List[Type] """
        ...

    @staticmethod
    def GetFacetType(facetShortName:str) -> Type:
        """ GetFacetType(facetShortName: str) -> Type """
        ...

    @staticmethod
    def GetRootFacets(rootType:Type) -> List:
        """ GetRootFacets(rootType: Type) -> List[Type] """
        ...

    @staticmethod
    def IsPropertyConfigurable(managementFacet:Type, propertyName:str) -> bool:
        """ IsPropertyConfigurable(managementFacet: Type, propertyName: str) -> bool """
        ...

    @staticmethod
    def IsRegisteredFacet(facet:Type) -> bool:
        """ IsRegisteredFacet(facet: Type) -> bool """
        ...

    @staticmethod
    def IsRootFacet(rootType:Type, facet:Type) -> bool:
        """ IsRootFacet(rootType: Type, facet: Type) -> bool """
        ...



class IDmfAdapter: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDmfObjectInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ObjectPath(self) -> str:
        """ Get: ObjectPath(self: IDmfObjectInfo) -> str """
        ...

    @property
    def RootPath(self) -> str:
        """ Get: RootPath(self: IDmfObjectInfo) -> str """
        ...



class PropertySourceSubObjectTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PropertySourceSubObjectTypeAttribute(sourceType: Type) """
    @property
    def SourceType(self) -> Type:
        """ Get: SourceType(self: PropertySourceSubObjectTypeAttribute) -> Type """
        ...


    def __new__(cls, sourceType:Type) -> Self:
        """ __new__(cls: type, sourceType: Type) """
        ...


class StateChangeEventAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    StateChangeEventAttribute(eventName: str, targetType: str)
    StateChangeEventAttribute(eventName: str, targetType: str, targetTypeAlias: str)
    """
    @property
    def EventName(self) -> str:
        """ Get: EventName(self: StateChangeEventAttribute) -> str """
        ...

    @property
    def TargetType(self) -> str:
        """ Get: TargetType(self: StateChangeEventAttribute) -> str """
        ...

    @property
    def TargetTypeAlias(self) -> str:
        """ Get: TargetTypeAlias(self: StateChangeEventAttribute) -> str """
        ...


    def __new__(cls, eventName:str, targetType:str, targetTypeAlias:str = ...) -> Self:
        """
        __new__(cls: type, eventName: str, targetType: str)
        __new__(cls: type, eventName: str, targetType: str, targetTypeAlias: str)
        """
        ...


