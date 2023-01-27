# encoding: utf-8
# module System.ComponentModel.Composition calls itself Composition
# from System.ComponentModel.Composition, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Attribute, Enum, IDisposable, Type

from System.Collections import IDictionary

from System.Collections.ObjectModel import ReadOnlyCollection

from System.ComponentModel.Composition.Hosting import (CompositionBatch, 
    CompositionContainer)

from System.ComponentModel.Composition.Primitives import (ComposablePart, 
    ComposablePartDefinition, ICompositionElement)

from System.Reflection import ReflectionContext

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    IAttributedImport, T, TMetadataView, field#)
"""

# no functions
# classes

class AttributedModelServices: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AddExportedValue(batch:CompositionBatch, *__args) -> ComposablePart: # Not found arg types: {'*__args': 'T'}
        """
        AddExportedValue[T](batch: CompositionBatch, exportedValue: T) -> ComposablePart
        AddExportedValue[T](batch: CompositionBatch, contractName: str, exportedValue: T) -> ComposablePart
        """
        ...

    @staticmethod
    def AddPart(batch:CompositionBatch, attributedPart:object) -> ComposablePart:
        """ AddPart(batch: CompositionBatch, attributedPart: object) -> ComposablePart """
        ...

    @staticmethod
    def ComposeExportedValue(container:CompositionContainer, *__args): # ->  # Not found arg types: {'*__args': 'T'}
        """ ComposeExportedValue[T](container: CompositionContainer, exportedValue: T)ComposeExportedValue[T](container: CompositionContainer, contractName: str, exportedValue: T) """
        ...

    @staticmethod
    def ComposeParts(container:CompositionContainer, attributedParts:Array): # -> 
        """ ComposeParts(container: CompositionContainer, *attributedParts: Array[object]) """
        ...

    @staticmethod
    def CreatePart(*__args:object) -> ComposablePart:
        """
        CreatePart(attributedPart: object) -> ComposablePart
        CreatePart(attributedPart: object, reflectionContext: ReflectionContext) -> ComposablePart
        CreatePart(partDefinition: ComposablePartDefinition, attributedPart: object) -> ComposablePart
        """
        ...

    @staticmethod
    def CreatePartDefinition(type:Type, origin:ICompositionElement, ensureIsDiscoverable:bool = ...) -> ComposablePartDefinition:
        """
        CreatePartDefinition(type: Type, origin: ICompositionElement) -> ComposablePartDefinition
        CreatePartDefinition(type: Type, origin: ICompositionElement, ensureIsDiscoverable: bool) -> ComposablePartDefinition
        """
        ...

    @staticmethod
    def Exports(part:ComposablePartDefinition, contractType:Type = ...) -> bool:
        """
        Exports(part: ComposablePartDefinition, contractType: Type) -> bool
        Exports[T](part: ComposablePartDefinition) -> bool
        """
        ...

    @staticmethod
    def GetContractName(type:Type) -> str:
        """ GetContractName(type: Type) -> str """
        ...

    @staticmethod
    def GetMetadataView(metadata:IDictionary): # -> TMetadataView
        """ GetMetadataView[TMetadataView](metadata: IDictionary[str, object]) -> TMetadataView """
        ...

    @staticmethod
    def GetTypeIdentity(*__args:Type) -> str:
        """
        GetTypeIdentity(type: Type) -> str
        GetTypeIdentity(method: MethodInfo) -> str
        """
        ...

    @staticmethod
    def Imports(part:ComposablePartDefinition, *__args:Type) -> bool:
        """
        Imports(part: ComposablePartDefinition, contractType: Type) -> bool
        Imports(part: ComposablePartDefinition, contractType: Type, importCardinality: ImportCardinality) -> bool
        Imports[T](part: ComposablePartDefinition) -> bool
        Imports[T](part: ComposablePartDefinition, importCardinality: ImportCardinality) -> bool
        """
        ...

    @staticmethod
    def SatisfyImportsOnce(compositionService:ICompositionService, attributedPart:object, reflectionContext:ReflectionContext = ...) -> ComposablePart:
        """
        SatisfyImportsOnce(compositionService: ICompositionService, attributedPart: object) -> ComposablePart
        SatisfyImportsOnce(compositionService: ICompositionService, attributedPart: object, reflectionContext: ReflectionContext) -> ComposablePart
        """
        ...

    __all__: list = ...


class CatalogReflectionContextAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CatalogReflectionContextAttribute(reflectionContextType: Type) """
    def CreateReflectionContext(self) -> ReflectionContext:
        """ CreateReflectionContext(self: CatalogReflectionContextAttribute) -> ReflectionContext """
        ...

    def __new__(cls, reflectionContextType:Type) -> Self:
        """ __new__(cls: type, reflectionContextType: Type) """
        ...


class CompositionException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CompositionException()
    CompositionException(message: str)
    CompositionException(message: str, innerException: Exception)
    CompositionException(errors: IEnumerable[CompositionError])
    """
    @property
    def Errors(self) -> ReadOnlyCollection:
        """ Get: Errors(self: CompositionException) -> ReadOnlyCollection[CompositionError] """
        ...

    @property
    def RootCauses(self) -> ReadOnlyCollection:
        """ Get: RootCauses(self: CompositionException) -> ReadOnlyCollection[Exception] """
        ...


    SerializeObjectState = ...


class ChangeRejectedException(CompositionException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ChangeRejectedException()
    ChangeRejectedException(message: str)
    ChangeRejectedException(message: str, innerException: Exception)
    ChangeRejectedException(errors: IEnumerable[CompositionError])
    """
    SerializeObjectState = ...


class CompositionContractMismatchException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CompositionContractMismatchException()
    CompositionContractMismatchException(message: str)
    CompositionContractMismatchException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class CompositionError: # skipped bases: <type 'object'>, <type 'object'>
    """
    CompositionError(message: str)
    CompositionError(message: str, element: ICompositionElement)
    CompositionError(message: str, exception: Exception)
    CompositionError(message: str, element: ICompositionElement, exception: Exception)
    """
    @property
    def Description(self) -> str:
        """ Get: Description(self: CompositionError) -> str """
        ...

    @property
    def Element(self) -> ICompositionElement:
        """ Get: Element(self: CompositionError) -> ICompositionElement """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: CompositionError) -> Exception """
        ...


    def ToString(self) -> str:
        """ ToString(self: CompositionError) -> str """
        ...


class CreationPolicy(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CreationPolicy, values: Any (0), NonShared (2), Shared (1) """
    Any: CreationPolicy = ...
    NonShared: CreationPolicy = ...
    Shared: CreationPolicy = ...
    value__ = ...


class ExportAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ExportAttribute()
    ExportAttribute(contractType: Type)
    ExportAttribute(contractName: str)
    ExportAttribute(contractName: str, contractType: Type)
    """
    @property
    def ContractName(self) -> str:
        """ Get: ContractName(self: ExportAttribute) -> str """
        ...

    @property
    def ContractType(self) -> Type:
        """ Get: ContractType(self: ExportAttribute) -> Type """
        ...


    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, contractType: Type)
        __new__(cls: type, contractName: str)
        __new__(cls: type, contractName: str, contractType: Type)
        """
        ...


class ExportLifetimeContext(IDisposable): # skipped bases: <type 'object'>
    """ ExportLifetimeContext[T](value: T, disposeAction: Action) """
    @property
    def Value(self): # -> T
        """ Get: Value(self: ExportLifetimeContext[T]) -> T """
        ...



class ExportMetadataAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ExportMetadataAttribute(name: str, value: object) """
    @property
    def IsMultiple(self) -> bool:
        """
        Get: IsMultiple(self: ExportMetadataAttribute) -> bool
        Set: IsMultiple(self: ExportMetadataAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ExportMetadataAttribute) -> str """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: ExportMetadataAttribute) -> object """
        ...


    def __new__(cls, name:str, value:object) -> Self:
        """ __new__(cls: type, name: str, value: object) """
        ...


class ICompositionService: # skipped bases: <type 'object'>
    """ no doc """
    def SatisfyImportsOnce(self, part:ComposablePart): # -> 
        """ SatisfyImportsOnce(self: ICompositionService, part: ComposablePart) """
        ...


class ImportAttribute(IAttributedImport, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ImportAttribute()
    ImportAttribute(contractType: Type)
    ImportAttribute(contractName: str)
    ImportAttribute(contractName: str, contractType: Type)
    """
    @property
    def AllowDefault(self) -> bool:
        """
        Get: AllowDefault(self: ImportAttribute) -> bool
        Set: AllowDefault(self: ImportAttribute) = value
        """
        ...

    @property
    def AllowRecomposition(self) -> bool:
        """
        Get: AllowRecomposition(self: ImportAttribute) -> bool
        Set: AllowRecomposition(self: ImportAttribute) = value
        """
        ...

    @property
    def ContractName(self) -> str:
        """ Get: ContractName(self: ImportAttribute) -> str """
        ...

    @property
    def ContractType(self) -> Type:
        """ Get: ContractType(self: ImportAttribute) -> Type """
        ...

    @property
    def RequiredCreationPolicy(self) -> CreationPolicy:
        """
        Get: RequiredCreationPolicy(self: ImportAttribute) -> CreationPolicy
        Set: RequiredCreationPolicy(self: ImportAttribute) = value
        """
        ...

    @property
    def Source(self) -> ImportSource:
        """
        Get: Source(self: ImportAttribute) -> ImportSource
        Set: Source(self: ImportAttribute) = value
        """
        ...


    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, contractType: Type)
        __new__(cls: type, contractName: str)
        __new__(cls: type, contractName: str, contractType: Type)
        """
        ...


class ImportCardinalityMismatchException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ImportCardinalityMismatchException()
    ImportCardinalityMismatchException(message: str)
    ImportCardinalityMismatchException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ImportingConstructorAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ImportingConstructorAttribute() """
    pass

class ImportManyAttribute(IAttributedImport, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ImportManyAttribute()
    ImportManyAttribute(contractType: Type)
    ImportManyAttribute(contractName: str)
    ImportManyAttribute(contractName: str, contractType: Type)
    """
    @property
    def AllowRecomposition(self) -> bool:
        """
        Get: AllowRecomposition(self: ImportManyAttribute) -> bool
        Set: AllowRecomposition(self: ImportManyAttribute) = value
        """
        ...

    @property
    def ContractName(self) -> str:
        """ Get: ContractName(self: ImportManyAttribute) -> str """
        ...

    @property
    def ContractType(self) -> Type:
        """ Get: ContractType(self: ImportManyAttribute) -> Type """
        ...

    @property
    def RequiredCreationPolicy(self) -> CreationPolicy:
        """
        Get: RequiredCreationPolicy(self: ImportManyAttribute) -> CreationPolicy
        Set: RequiredCreationPolicy(self: ImportManyAttribute) = value
        """
        ...

    @property
    def Source(self) -> ImportSource:
        """
        Get: Source(self: ImportManyAttribute) -> ImportSource
        Set: Source(self: ImportManyAttribute) = value
        """
        ...


    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, contractType: Type)
        __new__(cls: type, contractName: str)
        __new__(cls: type, contractName: str, contractType: Type)
        """
        ...


class ImportSource(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ImportSource, values: Any (0), Local (1), NonLocal (2) """
    Any: ImportSource = ...
    Local: ImportSource = ...
    NonLocal: ImportSource = ...
    value__ = ...


class InheritedExportAttribute(ExportAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    InheritedExportAttribute()
    InheritedExportAttribute(contractType: Type)
    InheritedExportAttribute(contractName: str)
    InheritedExportAttribute(contractName: str, contractType: Type)
    """
    pass

class IPartImportsSatisfiedNotification: # skipped bases: <type 'object'>
    """ no doc """
    def OnImportsSatisfied(self): # -> 
        """ OnImportsSatisfied(self: IPartImportsSatisfiedNotification) """
        ...


class MetadataAttributeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MetadataAttributeAttribute() """
    pass

class MetadataViewImplementationAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MetadataViewImplementationAttribute(implementationType: Type) """
    @property
    def ImplementationType(self) -> Type:
        """ Get: ImplementationType(self: MetadataViewImplementationAttribute) -> Type """
        ...


    def __new__(cls, implementationType:Type) -> Self:
        """ __new__(cls: type, implementationType: Type) """
        ...


class PartCreationPolicyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PartCreationPolicyAttribute(creationPolicy: CreationPolicy) """
    @property
    def CreationPolicy(self) -> CreationPolicy:
        """ Get: CreationPolicy(self: PartCreationPolicyAttribute) -> CreationPolicy """
        ...


    def __new__(cls, creationPolicy:CreationPolicy) -> Self:
        """ __new__(cls: type, creationPolicy: CreationPolicy) """
        ...


class PartMetadataAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PartMetadataAttribute(name: str, value: object) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: PartMetadataAttribute) -> str """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: PartMetadataAttribute) -> object """
        ...


    def __new__(cls, name:str, value:object) -> Self:
        """ __new__(cls: type, name: str, value: object) """
        ...


class PartNotDiscoverableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PartNotDiscoverableAttribute() """
    pass

# variables with complex values

