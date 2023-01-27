# encoding: utf-8
# module System.ComponentModel.Composition.Primitives calls itself Primitives
# from System.ComponentModel.Composition, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Delegate, Enum, IDisposable, Type

from System.Collections import IDictionary, IEnumerable

from System.ComponentModel.Composition import CreationPolicy

from System.Linq import IQueryable

from System.Linq.Expressions import Expression

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class ComposablePart: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ExportDefinitions(self) -> IEnumerable:
        """ Get: ExportDefinitions(self: ComposablePart) -> IEnumerable[ExportDefinition] """
        ...

    @property
    def ImportDefinitions(self) -> IEnumerable:
        """ Get: ImportDefinitions(self: ComposablePart) -> IEnumerable[ImportDefinition] """
        ...

    @property
    def Metadata(self) -> IDictionary:
        """ Get: Metadata(self: ComposablePart) -> IDictionary[str, object] """
        ...


    def Activate(self): # -> 
        """ Activate(self: ComposablePart) """
        ...

    def GetExportedValue(self, definition:ExportDefinition) -> object:
        """ GetExportedValue(self: ComposablePart, definition: ExportDefinition) -> object """
        ...

    def SetImport(self, definition:ImportDefinition, exports:IEnumerable): # -> 
        """ SetImport(self: ComposablePart, definition: ImportDefinition, exports: IEnumerable[Export]) """
        ...


class ComposablePartCatalog(IDisposable, IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Parts(self) -> IQueryable:
        """ Get: Parts(self: ComposablePartCatalog) -> IQueryable[ComposablePartDefinition] """
        ...


    def GetExports(self, definition:ImportDefinition) -> IEnumerable:
        """ GetExports(self: ComposablePartCatalog, definition: ImportDefinition) -> IEnumerable[Tuple[ComposablePartDefinition, ExportDefinition]] """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ComposablePartDefinition](enumerable: IEnumerable[ComposablePartDefinition], value: ComposablePartDefinition) -> bool """
        ...


class ComposablePartDefinition: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ExportDefinitions(self) -> IEnumerable:
        """ Get: ExportDefinitions(self: ComposablePartDefinition) -> IEnumerable[ExportDefinition] """
        ...

    @property
    def ImportDefinitions(self) -> IEnumerable:
        """ Get: ImportDefinitions(self: ComposablePartDefinition) -> IEnumerable[ImportDefinition] """
        ...

    @property
    def Metadata(self) -> IDictionary:
        """ Get: Metadata(self: ComposablePartDefinition) -> IDictionary[str, object] """
        ...


    def CreatePart(self) -> ComposablePart:
        """ CreatePart(self: ComposablePartDefinition) -> ComposablePart """
        ...


class ComposablePartException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ComposablePartException()
    ComposablePartException(message: str)
    ComposablePartException(message: str, element: ICompositionElement)
    ComposablePartException(message: str, innerException: Exception)
    ComposablePartException(message: str, element: ICompositionElement, innerException: Exception)
    """
    @property
    def Element(self) -> ICompositionElement:
        """ Get: Element(self: ComposablePartException) -> ICompositionElement """
        ...


    SerializeObjectState = ...


class ImportDefinition: # skipped bases: <type 'object'>, <type 'object'>
    """
    ImportDefinition(constraint: Expression[Func[ExportDefinition, bool]], contractName: str, cardinality: ImportCardinality, isRecomposable: bool, isPrerequisite: bool)
    ImportDefinition(constraint: Expression[Func[ExportDefinition, bool]], contractName: str, cardinality: ImportCardinality, isRecomposable: bool, isPrerequisite: bool, metadata: IDictionary[str, object])
    """
    @property
    def Cardinality(self) -> ImportCardinality:
        """ Get: Cardinality(self: ImportDefinition) -> ImportCardinality """
        ...

    @property
    def Constraint(self) -> Expression:
        """ Get: Constraint(self: ImportDefinition) -> Expression[Func[ExportDefinition, bool]] """
        ...

    @property
    def ContractName(self) -> str:
        """ Get: ContractName(self: ImportDefinition) -> str """
        ...

    @property
    def IsPrerequisite(self) -> bool:
        """ Get: IsPrerequisite(self: ImportDefinition) -> bool """
        ...

    @property
    def IsRecomposable(self) -> bool:
        """ Get: IsRecomposable(self: ImportDefinition) -> bool """
        ...

    @property
    def Metadata(self) -> IDictionary:
        """ Get: Metadata(self: ImportDefinition) -> IDictionary[str, object] """
        ...


    def IsConstraintSatisfiedBy(self, exportDefinition:ExportDefinition) -> bool:
        """ IsConstraintSatisfiedBy(self: ImportDefinition, exportDefinition: ExportDefinition) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: ImportDefinition) -> str """
        ...


class ContractBasedImportDefinition(ImportDefinition): # skipped bases: <type 'object'>
    """
    ContractBasedImportDefinition(contractName: str, requiredTypeIdentity: str, requiredMetadata: IEnumerable[KeyValuePair[str, Type]], cardinality: ImportCardinality, isRecomposable: bool, isPrerequisite: bool, requiredCreationPolicy: CreationPolicy)
    ContractBasedImportDefinition(contractName: str, requiredTypeIdentity: str, requiredMetadata: IEnumerable[KeyValuePair[str, Type]], cardinality: ImportCardinality, isRecomposable: bool, isPrerequisite: bool, requiredCreationPolicy: CreationPolicy, metadata: IDictionary[str, object])
    """
    @property
    def RequiredCreationPolicy(self) -> CreationPolicy:
        """ Get: RequiredCreationPolicy(self: ContractBasedImportDefinition) -> CreationPolicy """
        ...

    @property
    def RequiredMetadata(self) -> IEnumerable:
        """ Get: RequiredMetadata(self: ContractBasedImportDefinition) -> IEnumerable[KeyValuePair[str, Type]] """
        ...

    @property
    def RequiredTypeIdentity(self) -> str:
        """ Get: RequiredTypeIdentity(self: ContractBasedImportDefinition) -> str """
        ...



class Export: # skipped bases: <type 'object'>, <type 'object'>
    """
    Export(contractName: str, exportedValueGetter: Func[object])
    Export(contractName: str, metadata: IDictionary[str, object], exportedValueGetter: Func[object])
    Export(definition: ExportDefinition, exportedValueGetter: Func[object])
    """
    @property
    def Definition(self) -> ExportDefinition:
        """ Get: Definition(self: Export) -> ExportDefinition """
        ...

    @property
    def Metadata(self) -> IDictionary:
        """ Get: Metadata(self: Export) -> IDictionary[str, object] """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: Export) -> object """
        ...


    def GetExportedValueCore(self, *args): #cannot find CLR method
        """ GetExportedValueCore(self: Export) -> object """
        ...


class ExportDefinition: # skipped bases: <type 'object'>, <type 'object'>
    """ ExportDefinition(contractName: str, metadata: IDictionary[str, object]) """
    @property
    def ContractName(self) -> str:
        """ Get: ContractName(self: ExportDefinition) -> str """
        ...

    @property
    def Metadata(self) -> IDictionary:
        """ Get: Metadata(self: ExportDefinition) -> IDictionary[str, object] """
        ...


    def ToString(self) -> str:
        """ ToString(self: ExportDefinition) -> str """
        ...


class ExportedDelegate: # skipped bases: <type 'object'>, <type 'object'>
    """ ExportedDelegate(instance: object, method: MethodInfo) """
    def CreateDelegate(self, delegateType:Type) -> Delegate:
        """ CreateDelegate(self: ExportedDelegate, delegateType: Type) -> Delegate """
        ...


class ICompositionElement: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: ICompositionElement) -> str """
        ...

    @property
    def Origin(self) -> ICompositionElement:
        """ Get: Origin(self: ICompositionElement) -> ICompositionElement """
        ...



class ImportCardinality(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ImportCardinality, values: ExactlyOne (1), ZeroOrMore (2), ZeroOrOne (0) """
    ExactlyOne: ImportCardinality = ...
    value__ = ...
    ZeroOrMore: ImportCardinality = ...
    ZeroOrOne: ImportCardinality = ...


