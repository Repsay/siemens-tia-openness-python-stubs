# encoding: utf-8
# module System.ComponentModel.Composition.Hosting calls itself Hosting
# from System.ComponentModel.Composition, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Action, Array, Enum, EventArgs, IDisposable

from System.Collections import ICollection, IEnumerable

from System.Collections.ObjectModel import ReadOnlyCollection

from System.ComponentModel.Composition import ICompositionService

from System.ComponentModel.Composition.Primitives import (ComposablePart, 
    ComposablePartCatalog, ComposablePartDefinition, Export, 
    ICompositionElement, ImportCardinality, ImportDefinition)

from System.Reflection import Assembly, ReflectionContext

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, Func, Lazy, 
    T, field#)
"""

# no functions
# classes

class INotifyComposablePartCatalogChanged: # skipped bases: <type 'object'>
    """ no doc """
    Changed = ...
    Changing = ...


class AggregateCatalog(ComposablePartCatalog, INotifyComposablePartCatalogChanged): # skipped bases: <type 'IDisposable'>, <type 'IEnumerable[ComposablePartDefinition]'>, <type 'IEnumerable'>, <type 'object'>
    """
    AggregateCatalog()
    AggregateCatalog(*catalogs: Array[ComposablePartCatalog])
    AggregateCatalog(catalogs: IEnumerable[ComposablePartCatalog])
    """
    @property
    def Catalogs(self) -> ICollection:
        """ Get: Catalogs(self: AggregateCatalog) -> ICollection[ComposablePartCatalog] """
        ...


    def OnChanged(self, *args): #cannot find CLR method
        """ OnChanged(self: AggregateCatalog, e: ComposablePartCatalogChangeEventArgs) """
        ...

    def OnChanging(self, *args): #cannot find CLR method
        """ OnChanging(self: AggregateCatalog, e: ComposablePartCatalogChangeEventArgs) """
        ...

    def __new__(cls, catalogs:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, *catalogs: Array[ComposablePartCatalog])
        __new__(cls: type, catalogs: IEnumerable[ComposablePartCatalog])
        """
        ...

    Changed = ...
    Changing = ...


class ExportProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetExport(self, contractName:str = ...): # -> Lazy
        """
        GetExport[T](self: ExportProvider) -> Lazy[T]
        GetExport[T](self: ExportProvider, contractName: str) -> Lazy[T]
        GetExport[(T, TMetadataView)](self: ExportProvider) -> Lazy[T, TMetadataView]
        GetExport[(T, TMetadataView)](self: ExportProvider, contractName: str) -> Lazy[T, TMetadataView]
        """
        ...

    def GetExportedValue(self, contractName:str = ...): # -> T
        """
        GetExportedValue[T](self: ExportProvider) -> T
        GetExportedValue[T](self: ExportProvider, contractName: str) -> T
        """
        ...

    def GetExportedValueOrDefault(self, contractName:str = ...): # -> T
        """
        GetExportedValueOrDefault[T](self: ExportProvider) -> T
        GetExportedValueOrDefault[T](self: ExportProvider, contractName: str) -> T
        """
        ...

    def GetExportedValues(self, contractName:str = ...) -> IEnumerable:
        """
        GetExportedValues[T](self: ExportProvider) -> IEnumerable[T]
        GetExportedValues[T](self: ExportProvider, contractName: str) -> IEnumerable[T]
        """
        ...

    def GetExports(self, *__args:ImportDefinition) -> IEnumerable:
        """
        GetExports(self: ExportProvider, definition: ImportDefinition) -> IEnumerable[Export]
        GetExports(self: ExportProvider, type: Type, metadataViewType: Type, contractName: str) -> IEnumerable[Lazy[object, object]]
        GetExports[T](self: ExportProvider) -> IEnumerable[Lazy[T]]
        GetExports[T](self: ExportProvider, contractName: str) -> IEnumerable[Lazy[T]]
        GetExports[(T, TMetadataView)](self: ExportProvider) -> IEnumerable[Lazy[T, TMetadataView]]
        GetExports[(T, TMetadataView)](self: ExportProvider, contractName: str) -> IEnumerable[Lazy[T, TMetadataView]]
        GetExports(self: ExportProvider, definition: ImportDefinition, atomicComposition: AtomicComposition) -> IEnumerable[Export]
        """
        ...

    def GetExportsCore(self, *args): #cannot find CLR method
        """ GetExportsCore(self: ExportProvider, definition: ImportDefinition, atomicComposition: AtomicComposition) -> IEnumerable[Export] """
        ...

    def OnExportsChanged(self, *args): #cannot find CLR method
        """ OnExportsChanged(self: ExportProvider, e: ExportsChangeEventArgs) """
        ...

    def OnExportsChanging(self, *args): #cannot find CLR method
        """ OnExportsChanging(self: ExportProvider, e: ExportsChangeEventArgs) """
        ...

    def TryGetExports(self, definition, atomicComposition, exports) -> Tuple_[bool, IEnumerable]:
        """ TryGetExports(self: ExportProvider, definition: ImportDefinition, atomicComposition: AtomicComposition) -> (bool, IEnumerable[Export]) """
        ...

    ExportsChanged = ...
    ExportsChanging = ...


class AggregateExportProvider(IDisposable, ExportProvider): # skipped bases: <type 'object'>
    """
    AggregateExportProvider(*providers: Array[ExportProvider])
    AggregateExportProvider(providers: IEnumerable[ExportProvider])
    """
    @property
    def Providers(self) -> ReadOnlyCollection:
        """ Get: Providers(self: AggregateExportProvider) -> ReadOnlyCollection[ExportProvider] """
        ...


    def __new__(cls, providers:Array) -> Self:
        """
        __new__(cls: type, *providers: Array[ExportProvider])
        __new__(cls: type, providers: IEnumerable[ExportProvider])
        """
        ...


class ApplicationCatalog(ComposablePartCatalog, ICompositionElement): # skipped bases: <type 'IDisposable'>, <type 'IEnumerable[ComposablePartDefinition]'>, <type 'IEnumerable'>, <type 'object'>
    """
    ApplicationCatalog()
    ApplicationCatalog(definitionOrigin: ICompositionElement)
    ApplicationCatalog(reflectionContext: ReflectionContext)
    ApplicationCatalog(reflectionContext: ReflectionContext, definitionOrigin: ICompositionElement)
    """
    def ToString(self) -> str:
        """ ToString(self: ApplicationCatalog) -> str """
        ...

    def __new__(cls, *__args:ICompositionElement) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, definitionOrigin: ICompositionElement)
        __new__(cls: type, reflectionContext: ReflectionContext)
        __new__(cls: type, reflectionContext: ReflectionContext, definitionOrigin: ICompositionElement)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class AssemblyCatalog(ComposablePartCatalog, ICompositionElement): # skipped bases: <type 'IDisposable'>, <type 'IEnumerable[ComposablePartDefinition]'>, <type 'IEnumerable'>, <type 'object'>
    """
    AssemblyCatalog(codeBase: str)
    AssemblyCatalog(codeBase: str, reflectionContext: ReflectionContext)
    AssemblyCatalog(codeBase: str, definitionOrigin: ICompositionElement)
    AssemblyCatalog(codeBase: str, reflectionContext: ReflectionContext, definitionOrigin: ICompositionElement)
    AssemblyCatalog(assembly: Assembly, reflectionContext: ReflectionContext)
    AssemblyCatalog(assembly: Assembly, reflectionContext: ReflectionContext, definitionOrigin: ICompositionElement)
    AssemblyCatalog(assembly: Assembly)
    AssemblyCatalog(assembly: Assembly, definitionOrigin: ICompositionElement)
    """
    @property
    def Assembly(self) -> Assembly:
        """ Get: Assembly(self: AssemblyCatalog) -> Assembly """
        ...


    def ToString(self) -> str:
        """ ToString(self: AssemblyCatalog) -> str """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, codeBase: str)
        __new__(cls: type, codeBase: str, reflectionContext: ReflectionContext)
        __new__(cls: type, codeBase: str, definitionOrigin: ICompositionElement)
        __new__(cls: type, codeBase: str, reflectionContext: ReflectionContext, definitionOrigin: ICompositionElement)
        __new__(cls: type, assembly: Assembly, reflectionContext: ReflectionContext)
        __new__(cls: type, assembly: Assembly, reflectionContext: ReflectionContext, definitionOrigin: ICompositionElement)
        __new__(cls: type, assembly: Assembly)
        __new__(cls: type, assembly: Assembly, definitionOrigin: ICompositionElement)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class AtomicComposition(IDisposable): # skipped bases: <type 'object'>
    """
    AtomicComposition()
    AtomicComposition(outerAtomicComposition: AtomicComposition)
    """
    def AddCompleteAction(self, completeAction:Action): # -> 
        """ AddCompleteAction(self: AtomicComposition, completeAction: Action) """
        ...

    def AddRevertAction(self, revertAction:Action): # -> 
        """ AddRevertAction(self: AtomicComposition, revertAction: Action) """
        ...

    def Complete(self): # -> 
        """ Complete(self: AtomicComposition) """
        ...

    def SetValue(self, key:object, value:object): # -> 
        """ SetValue(self: AtomicComposition, key: object, value: object) """
        ...

    def TryGetValue(self, key:object, *__args:bool): # -> Tuple_[bool, T]
        """
        TryGetValue[T](self: AtomicComposition, key: object) -> (bool, T)
        TryGetValue[T](self: AtomicComposition, key: object, localAtomicCompositionOnly: bool) -> (bool, T)
        """
        ...


class CatalogExportProvider(IDisposable, ExportProvider): # skipped bases: <type 'object'>
    """
    CatalogExportProvider(catalog: ComposablePartCatalog)
    CatalogExportProvider(catalog: ComposablePartCatalog, isThreadSafe: bool)
    CatalogExportProvider(catalog: ComposablePartCatalog, compositionOptions: CompositionOptions)
    """
    @property
    def Catalog(self) -> ComposablePartCatalog:
        """ Get: Catalog(self: CatalogExportProvider) -> ComposablePartCatalog """
        ...

    @property
    def SourceProvider(self) -> ExportProvider:
        """
        Get: SourceProvider(self: CatalogExportProvider) -> ExportProvider
        Set: SourceProvider(self: CatalogExportProvider) = value
        """
        ...


    def __new__(cls, catalog:ComposablePartCatalog, *__args:bool) -> Self:
        """
        __new__(cls: type, catalog: ComposablePartCatalog)
        __new__(cls: type, catalog: ComposablePartCatalog, isThreadSafe: bool)
        __new__(cls: type, catalog: ComposablePartCatalog, compositionOptions: CompositionOptions)
        """
        ...


class CatalogExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateCompositionService(composablePartCatalog:ComposablePartCatalog) -> CompositionService:
        """ CreateCompositionService(composablePartCatalog: ComposablePartCatalog) -> CompositionService """
        ...

    __all__: list = ...


class ComposablePartCatalogChangeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ComposablePartCatalogChangeEventArgs(addedDefinitions: IEnumerable[ComposablePartDefinition], removedDefinitions: IEnumerable[ComposablePartDefinition], atomicComposition: AtomicComposition) """
    @property
    def AddedDefinitions(self) -> IEnumerable:
        """ Get: AddedDefinitions(self: ComposablePartCatalogChangeEventArgs) -> IEnumerable[ComposablePartDefinition] """
        ...

    @property
    def AtomicComposition(self) -> AtomicComposition:
        """ Get: AtomicComposition(self: ComposablePartCatalogChangeEventArgs) -> AtomicComposition """
        ...

    @property
    def RemovedDefinitions(self) -> IEnumerable:
        """ Get: RemovedDefinitions(self: ComposablePartCatalogChangeEventArgs) -> IEnumerable[ComposablePartDefinition] """
        ...


    def __new__(cls, addedDefinitions:IEnumerable, removedDefinitions:IEnumerable, atomicComposition:AtomicComposition) -> Self:
        """ __new__(cls: type, addedDefinitions: IEnumerable[ComposablePartDefinition], removedDefinitions: IEnumerable[ComposablePartDefinition], atomicComposition: AtomicComposition) """
        ...


class ComposablePartExportProvider(IDisposable, ExportProvider): # skipped bases: <type 'object'>
    """
    ComposablePartExportProvider()
    ComposablePartExportProvider(isThreadSafe: bool)
    ComposablePartExportProvider(compositionOptions: CompositionOptions)
    """
    @property
    def SourceProvider(self) -> ExportProvider:
        """
        Get: SourceProvider(self: ComposablePartExportProvider) -> ExportProvider
        Set: SourceProvider(self: ComposablePartExportProvider) = value
        """
        ...


    def Compose(self, batch:CompositionBatch): # -> 
        """ Compose(self: ComposablePartExportProvider, batch: CompositionBatch) """
        ...

    def __new__(cls, *__args:bool) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, isThreadSafe: bool)
        __new__(cls: type, compositionOptions: CompositionOptions)
        """
        ...


class CompositionBatch: # skipped bases: <type 'object'>, <type 'object'>
    """
    CompositionBatch()
    CompositionBatch(partsToAdd: IEnumerable[ComposablePart], partsToRemove: IEnumerable[ComposablePart])
    """
    @property
    def PartsToAdd(self) -> ReadOnlyCollection:
        """ Get: PartsToAdd(self: CompositionBatch) -> ReadOnlyCollection[ComposablePart] """
        ...

    @property
    def PartsToRemove(self) -> ReadOnlyCollection:
        """ Get: PartsToRemove(self: CompositionBatch) -> ReadOnlyCollection[ComposablePart] """
        ...


    def AddExport(self, export:Export) -> ComposablePart:
        """ AddExport(self: CompositionBatch, export: Export) -> ComposablePart """
        ...

    def AddPart(self, part:ComposablePart): # -> 
        """ AddPart(self: CompositionBatch, part: ComposablePart) """
        ...

    def RemovePart(self, part:ComposablePart): # -> 
        """ RemovePart(self: CompositionBatch, part: ComposablePart) """
        ...


class CompositionConstants: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    ExportTypeIdentityMetadataName: str = ...
    GenericContractMetadataName: str = ...
    GenericParametersMetadataName: str = ...
    ImportSourceMetadataName: str = ...
    IsGenericPartMetadataName: str = ...
    PartCreationPolicyMetadataName: str = ...
    __all__: list = ...


class CompositionContainer(ICompositionService, IDisposable, ExportProvider): # skipped bases: <type 'object'>
    """
    CompositionContainer()
    CompositionContainer(*providers: Array[ExportProvider])
    CompositionContainer(compositionOptions: CompositionOptions, *providers: Array[ExportProvider])
    CompositionContainer(catalog: ComposablePartCatalog, *providers: Array[ExportProvider])
    CompositionContainer(catalog: ComposablePartCatalog, isThreadSafe: bool, *providers: Array[ExportProvider])
    CompositionContainer(catalog: ComposablePartCatalog, compositionOptions: CompositionOptions, *providers: Array[ExportProvider])
    """
    @property
    def Catalog(self) -> ComposablePartCatalog:
        """ Get: Catalog(self: CompositionContainer) -> ComposablePartCatalog """
        ...

    @property
    def Providers(self) -> ReadOnlyCollection:
        """ Get: Providers(self: CompositionContainer) -> ReadOnlyCollection[ExportProvider] """
        ...


    def Compose(self, batch:CompositionBatch): # -> 
        """ Compose(self: CompositionContainer, batch: CompositionBatch) """
        ...

    def ReleaseExport(self, export:Export): # -> 
        """ ReleaseExport(self: CompositionContainer, export: Export)ReleaseExport[T](self: CompositionContainer, export: Lazy[T]) """
        ...

    def ReleaseExports(self, exports:IEnumerable): # -> 
        """ ReleaseExports(self: CompositionContainer, exports: IEnumerable[Export])ReleaseExports[T](self: CompositionContainer, exports: IEnumerable[Lazy[T]])ReleaseExports[(T, TMetadataView)](self: CompositionContainer, exports: IEnumerable[Lazy[T, TMetadataView]]) """
        ...

    def __new__(cls, *__args:Array) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, *providers: Array[ExportProvider])
        __new__(cls: type, compositionOptions: CompositionOptions, *providers: Array[ExportProvider])
        __new__(cls: type, catalog: ComposablePartCatalog, *providers: Array[ExportProvider])
        __new__(cls: type, catalog: ComposablePartCatalog, isThreadSafe: bool, *providers: Array[ExportProvider])
        __new__(cls: type, catalog: ComposablePartCatalog, compositionOptions: CompositionOptions, *providers: Array[ExportProvider])
        """
        ...


class CompositionOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CompositionOptions, values: Default (0), DisableSilentRejection (1), ExportCompositionService (4), IsThreadSafe (2) """
    Default: CompositionOptions = ...
    DisableSilentRejection: CompositionOptions = ...
    ExportCompositionService: CompositionOptions = ...
    IsThreadSafe: CompositionOptions = ...
    value__ = ...


class CompositionScopeDefinition(ComposablePartCatalog, INotifyComposablePartCatalogChanged): # skipped bases: <type 'IDisposable'>, <type 'IEnumerable[ComposablePartDefinition]'>, <type 'IEnumerable'>, <type 'object'>
    """
    CompositionScopeDefinition(catalog: ComposablePartCatalog, children: IEnumerable[CompositionScopeDefinition])
    CompositionScopeDefinition(catalog: ComposablePartCatalog, children: IEnumerable[CompositionScopeDefinition], publicSurface: IEnumerable[ExportDefinition])
    """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: CompositionScopeDefinition) -> IEnumerable[CompositionScopeDefinition] """
        ...

    @property
    def PublicSurface(self) -> IEnumerable:
        """ Get: PublicSurface(self: CompositionScopeDefinition) -> IEnumerable[ExportDefinition] """
        ...


    def OnChanged(self, *args): #cannot find CLR method
        """ OnChanged(self: CompositionScopeDefinition, e: ComposablePartCatalogChangeEventArgs) """
        ...

    def OnChanging(self, *args): #cannot find CLR method
        """ OnChanging(self: CompositionScopeDefinition, e: ComposablePartCatalogChangeEventArgs) """
        ...

    def __new__(cls, catalog:ComposablePartCatalog, children:IEnumerable, publicSurface:IEnumerable = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, catalog: ComposablePartCatalog, children: IEnumerable[CompositionScopeDefinition])
        __new__(cls: type, catalog: ComposablePartCatalog, children: IEnumerable[CompositionScopeDefinition], publicSurface: IEnumerable[ExportDefinition])
        """
        ...

    Changed = ...
    Changing = ...


class CompositionService(ICompositionService, IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    pass

class DirectoryCatalog(ComposablePartCatalog, INotifyComposablePartCatalogChanged, ICompositionElement): # skipped bases: <type 'IDisposable'>, <type 'IEnumerable[ComposablePartDefinition]'>, <type 'IEnumerable'>, <type 'object'>
    """
    DirectoryCatalog(path: str)
    DirectoryCatalog(path: str, reflectionContext: ReflectionContext)
    DirectoryCatalog(path: str, definitionOrigin: ICompositionElement)
    DirectoryCatalog(path: str, reflectionContext: ReflectionContext, definitionOrigin: ICompositionElement)
    DirectoryCatalog(path: str, searchPattern: str)
    DirectoryCatalog(path: str, searchPattern: str, definitionOrigin: ICompositionElement)
    DirectoryCatalog(path: str, searchPattern: str, reflectionContext: ReflectionContext)
    DirectoryCatalog(path: str, searchPattern: str, reflectionContext: ReflectionContext, definitionOrigin: ICompositionElement)
    """
    @property
    def FullPath(self) -> str:
        """ Get: FullPath(self: DirectoryCatalog) -> str """
        ...

    @property
    def LoadedFiles(self) -> ReadOnlyCollection:
        """ Get: LoadedFiles(self: DirectoryCatalog) -> ReadOnlyCollection[str] """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: DirectoryCatalog) -> str """
        ...

    @property
    def SearchPattern(self) -> str:
        """ Get: SearchPattern(self: DirectoryCatalog) -> str """
        ...


    def OnChanged(self, *args): #cannot find CLR method
        """ OnChanged(self: DirectoryCatalog, e: ComposablePartCatalogChangeEventArgs) """
        ...

    def OnChanging(self, *args): #cannot find CLR method
        """ OnChanging(self: DirectoryCatalog, e: ComposablePartCatalogChangeEventArgs) """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: DirectoryCatalog) """
        ...

    def ToString(self) -> str:
        """ ToString(self: DirectoryCatalog) -> str """
        ...

    def __new__(cls, path:str, *__args:ReflectionContext) -> Self:
        """
        __new__(cls: type, path: str)
        __new__(cls: type, path: str, reflectionContext: ReflectionContext)
        __new__(cls: type, path: str, definitionOrigin: ICompositionElement)
        __new__(cls: type, path: str, reflectionContext: ReflectionContext, definitionOrigin: ICompositionElement)
        __new__(cls: type, path: str, searchPattern: str)
        __new__(cls: type, path: str, searchPattern: str, definitionOrigin: ICompositionElement)
        __new__(cls: type, path: str, searchPattern: str, reflectionContext: ReflectionContext)
        __new__(cls: type, path: str, searchPattern: str, reflectionContext: ReflectionContext, definitionOrigin: ICompositionElement)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...

    Changed = ...
    Changing = ...


class ExportsChangeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ExportsChangeEventArgs(addedExports: IEnumerable[ExportDefinition], removedExports: IEnumerable[ExportDefinition], atomicComposition: AtomicComposition) """
    @property
    def AddedExports(self) -> IEnumerable:
        """ Get: AddedExports(self: ExportsChangeEventArgs) -> IEnumerable[ExportDefinition] """
        ...

    @property
    def AtomicComposition(self) -> AtomicComposition:
        """ Get: AtomicComposition(self: ExportsChangeEventArgs) -> AtomicComposition """
        ...

    @property
    def ChangedContractNames(self) -> IEnumerable:
        """ Get: ChangedContractNames(self: ExportsChangeEventArgs) -> IEnumerable[str] """
        ...

    @property
    def RemovedExports(self) -> IEnumerable:
        """ Get: RemovedExports(self: ExportsChangeEventArgs) -> IEnumerable[ExportDefinition] """
        ...


    def __new__(cls, addedExports:IEnumerable, removedExports:IEnumerable, atomicComposition:AtomicComposition) -> Self:
        """ __new__(cls: type, addedExports: IEnumerable[ExportDefinition], removedExports: IEnumerable[ExportDefinition], atomicComposition: AtomicComposition) """
        ...


class FilteredCatalog(ComposablePartCatalog, INotifyComposablePartCatalogChanged): # skipped bases: <type 'IDisposable'>, <type 'IEnumerable[ComposablePartDefinition]'>, <type 'IEnumerable'>, <type 'object'>
    """ FilteredCatalog(catalog: ComposablePartCatalog, filter: Func[ComposablePartDefinition, bool]) """
    @property
    def Complement(self) -> FilteredCatalog:
        """ Get: Complement(self: FilteredCatalog) -> FilteredCatalog """
        ...


    def IncludeDependencies(self, importFilter = ...) -> FilteredCatalog: # Not found arg types: {'importFilter': 'Func'}
        """
        IncludeDependencies(self: FilteredCatalog) -> FilteredCatalog
        IncludeDependencies(self: FilteredCatalog, importFilter: Func[ImportDefinition, bool]) -> FilteredCatalog
        """
        ...

    def IncludeDependents(self, importFilter = ...) -> FilteredCatalog: # Not found arg types: {'importFilter': 'Func'}
        """
        IncludeDependents(self: FilteredCatalog) -> FilteredCatalog
        IncludeDependents(self: FilteredCatalog, importFilter: Func[ImportDefinition, bool]) -> FilteredCatalog
        """
        ...

    def OnChanged(self, *args): #cannot find CLR method
        """ OnChanged(self: FilteredCatalog, e: ComposablePartCatalogChangeEventArgs) """
        ...

    def OnChanging(self, *args): #cannot find CLR method
        """ OnChanging(self: FilteredCatalog, e: ComposablePartCatalogChangeEventArgs) """
        ...

    def __new__(cls, catalog:ComposablePartCatalog, filter) -> Self: # Not found arg types: {'filter': 'Func'}
        """ __new__(cls: type, catalog: ComposablePartCatalog, filter: Func[ComposablePartDefinition, bool]) """
        ...

    Changed = ...
    Changing = ...


class ImportEngine(ICompositionService, IDisposable): # skipped bases: <type 'object'>
    """
    ImportEngine(sourceProvider: ExportProvider)
    ImportEngine(sourceProvider: ExportProvider, isThreadSafe: bool)
    ImportEngine(sourceProvider: ExportProvider, compositionOptions: CompositionOptions)
    """
    def PreviewImports(self, part:ComposablePart, atomicComposition:AtomicComposition): # -> 
        """ PreviewImports(self: ImportEngine, part: ComposablePart, atomicComposition: AtomicComposition) """
        ...

    def ReleaseImports(self, part:ComposablePart, atomicComposition:AtomicComposition): # -> 
        """ ReleaseImports(self: ImportEngine, part: ComposablePart, atomicComposition: AtomicComposition) """
        ...

    def SatisfyImports(self, part:ComposablePart): # -> 
        """ SatisfyImports(self: ImportEngine, part: ComposablePart) """
        ...


class ScopingExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ContainsPartMetadata(part:ComposablePartDefinition, key:str, value) -> bool: # Not found arg types: {'value': 'T'}
        """ ContainsPartMetadata[T](part: ComposablePartDefinition, key: str, value: T) -> bool """
        ...

    @staticmethod
    def ContainsPartMetadataWithKey(part:ComposablePartDefinition, key:str) -> bool:
        """ ContainsPartMetadataWithKey(part: ComposablePartDefinition, key: str) -> bool """
        ...

    @staticmethod
    def Exports(part:ComposablePartDefinition, contractName:str) -> bool:
        """ Exports(part: ComposablePartDefinition, contractName: str) -> bool """
        ...

    @staticmethod
    def Filter(catalog:ComposablePartCatalog, filter) -> FilteredCatalog: # Not found arg types: {'filter': 'Func'}
        """ Filter(catalog: ComposablePartCatalog, filter: Func[ComposablePartDefinition, bool]) -> FilteredCatalog """
        ...

    @staticmethod
    def Imports(part:ComposablePartDefinition, contractName:str, importCardinality:ImportCardinality = ...) -> bool:
        """
        Imports(part: ComposablePartDefinition, contractName: str) -> bool
        Imports(part: ComposablePartDefinition, contractName: str, importCardinality: ImportCardinality) -> bool
        """
        ...

    __all__: list = ...


class TypeCatalog(ComposablePartCatalog, ICompositionElement): # skipped bases: <type 'IDisposable'>, <type 'IEnumerable[ComposablePartDefinition]'>, <type 'IEnumerable'>, <type 'object'>
    """
    TypeCatalog(*types: Array[Type])
    TypeCatalog(types: IEnumerable[Type])
    TypeCatalog(types: IEnumerable[Type], definitionOrigin: ICompositionElement)
    TypeCatalog(types: IEnumerable[Type], reflectionContext: ReflectionContext)
    TypeCatalog(types: IEnumerable[Type], reflectionContext: ReflectionContext, definitionOrigin: ICompositionElement)
    """
    def ToString(self) -> str:
        """ ToString(self: TypeCatalog) -> str """
        ...

    def __new__(cls, types:IEnumerable, *__args:ICompositionElement) -> Self:
        """
        __new__(cls: type, *types: Array[Type])
        __new__(cls: type, types: IEnumerable[Type])
        __new__(cls: type, types: IEnumerable[Type], definitionOrigin: ICompositionElement)
        __new__(cls: type, types: IEnumerable[Type], reflectionContext: ReflectionContext)
        __new__(cls: type, types: IEnumerable[Type], reflectionContext: ReflectionContext, definitionOrigin: ICompositionElement)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


