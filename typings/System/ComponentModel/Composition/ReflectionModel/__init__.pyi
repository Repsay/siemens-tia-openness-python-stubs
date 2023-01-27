# encoding: utf-8
# module System.ComponentModel.Composition.ReflectionModel calls itself ReflectionModel
# from System.ComponentModel.Composition, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array

from System.Collections import IDictionary, IEnumerable

from System.ComponentModel.Composition import CreationPolicy

from System.ComponentModel.Composition.Primitives import (
    ComposablePartDefinition, ContractBasedImportDefinition, ExportDefinition, 
    ICompositionElement, ImportCardinality, ImportDefinition)

from System.Reflection import MemberTypes

from typing import Tuple as Tuple_

"""The following names are not found in the module: Lazy
"""

# no functions
# classes

class LazyMemberInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    LazyMemberInfo(member: MemberInfo)
    LazyMemberInfo(memberType: MemberTypes, *accessors: Array[MemberInfo])
    LazyMemberInfo(memberType: MemberTypes, accessorsCreator: Func[Array[MemberInfo]])
    """
    @property
    def MemberType(self) -> MemberTypes:
        """ Get: MemberType(self: LazyMemberInfo) -> MemberTypes """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: LazyMemberInfo, obj: object) -> bool """
        ...

    def GetAccessors(self) -> Array:
        """ GetAccessors(self: LazyMemberInfo) -> Array[MemberInfo] """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: LazyMemberInfo) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ReflectionModelServices: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateExportDefinition(exportingMember:LazyMemberInfo, contractName:str, metadata, origin:ICompositionElement) -> ExportDefinition: # Not found arg types: {'metadata': 'Lazy'}
        """ CreateExportDefinition(exportingMember: LazyMemberInfo, contractName: str, metadata: Lazy[IDictionary[str, object]], origin: ICompositionElement) -> ExportDefinition """
        ...

    @staticmethod
    def CreateImportDefinition(*__args) -> ContractBasedImportDefinition:
        """
        CreateImportDefinition(importingMember: LazyMemberInfo, contractName: str, requiredTypeIdentity: str, requiredMetadata: IEnumerable[KeyValuePair[str, Type]], cardinality: ImportCardinality, isRecomposable: bool, requiredCreationPolicy: CreationPolicy, metadata: IDictionary[str, object], isExportFactory: bool, origin: ICompositionElement) -> ContractBasedImportDefinition
        CreateImportDefinition(importingMember: LazyMemberInfo, contractName: str, requiredTypeIdentity: str, requiredMetadata: IEnumerable[KeyValuePair[str, Type]], cardinality: ImportCardinality, isRecomposable: bool, requiredCreationPolicy: CreationPolicy, origin: ICompositionElement) -> ContractBasedImportDefinition
        CreateImportDefinition(importingMember: LazyMemberInfo, contractName: str, requiredTypeIdentity: str, requiredMetadata: IEnumerable[KeyValuePair[str, Type]], cardinality: ImportCardinality, isRecomposable: bool, isPreRequisite: bool, requiredCreationPolicy: CreationPolicy, metadata: IDictionary[str, object], isExportFactory: bool, origin: ICompositionElement) -> ContractBasedImportDefinition
        CreateImportDefinition(parameter: Lazy[ParameterInfo], contractName: str, requiredTypeIdentity: str, requiredMetadata: IEnumerable[KeyValuePair[str, Type]], cardinality: ImportCardinality, requiredCreationPolicy: CreationPolicy, origin: ICompositionElement) -> ContractBasedImportDefinition
        CreateImportDefinition(parameter: Lazy[ParameterInfo], contractName: str, requiredTypeIdentity: str, requiredMetadata: IEnumerable[KeyValuePair[str, Type]], cardinality: ImportCardinality, requiredCreationPolicy: CreationPolicy, metadata: IDictionary[str, object], isExportFactory: bool, origin: ICompositionElement) -> ContractBasedImportDefinition
        """
        ...

    @staticmethod
    def CreatePartDefinition(partType, isDisposalRequired:bool, imports, exports, metadata, origin:ICompositionElement) -> ComposablePartDefinition: # Not found arg types: {'imports': 'Lazy', 'exports': 'Lazy', 'metadata': 'Lazy', 'partType': 'Lazy'}
        """ CreatePartDefinition(partType: Lazy[Type], isDisposalRequired: bool, imports: Lazy[IEnumerable[ImportDefinition]], exports: Lazy[IEnumerable[ExportDefinition]], metadata: Lazy[IDictionary[str, object]], origin: ICompositionElement) -> ComposablePartDefinition """
        ...

    @staticmethod
    def GetExportFactoryProductImportDefinition(importDefinition:ImportDefinition) -> ContractBasedImportDefinition:
        """ GetExportFactoryProductImportDefinition(importDefinition: ImportDefinition) -> ContractBasedImportDefinition """
        ...

    @staticmethod
    def GetExportingMember(exportDefinition:ExportDefinition) -> LazyMemberInfo:
        """ GetExportingMember(exportDefinition: ExportDefinition) -> LazyMemberInfo """
        ...

    @staticmethod
    def GetImportingMember(importDefinition:ImportDefinition) -> LazyMemberInfo:
        """ GetImportingMember(importDefinition: ImportDefinition) -> LazyMemberInfo """
        ...

    @staticmethod
    def GetImportingParameter(importDefinition:ImportDefinition): # -> Lazy
        """ GetImportingParameter(importDefinition: ImportDefinition) -> Lazy[ParameterInfo] """
        ...

    @staticmethod
    def GetPartType(partDefinition:ComposablePartDefinition): # -> Lazy
        """ GetPartType(partDefinition: ComposablePartDefinition) -> Lazy[Type] """
        ...

    @staticmethod
    def IsDisposalRequired(partDefinition:ComposablePartDefinition) -> bool:
        """ IsDisposalRequired(partDefinition: ComposablePartDefinition) -> bool """
        ...

    @staticmethod
    def IsExportFactoryImportDefinition(importDefinition:ImportDefinition) -> bool:
        """ IsExportFactoryImportDefinition(importDefinition: ImportDefinition) -> bool """
        ...

    @staticmethod
    def IsImportingParameter(importDefinition:ImportDefinition) -> bool:
        """ IsImportingParameter(importDefinition: ImportDefinition) -> bool """
        ...

    @staticmethod
    def TryMakeGenericPartDefinition(partDefinition, genericParameters, specialization) -> Tuple_[bool, ComposablePartDefinition]:
        """ TryMakeGenericPartDefinition(partDefinition: ComposablePartDefinition, genericParameters: IEnumerable[Type]) -> (bool, ComposablePartDefinition) """
        ...

    __all__: list = ...


