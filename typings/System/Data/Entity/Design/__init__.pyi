# encoding: utf-8
# module System.Data.Entity.Design calls itself Design
# from System.Data.Entity.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (AsyncCallback, Enum, EventArgs, IAsyncResult, 
    MulticastDelegate, Version)

from System.CodeDom import CodeTypeReference

from System.Collections import ICollection, IEnumerable, IList

from System.Collections.Generic import List

from System.Collections.ObjectModel import ReadOnlyCollection

from System.Data.Entity.Design.PluralizationServices import (
    PluralizationService)

from System.Data.EntityClient import EntityConnection

from System.Data.Mapping import StorageMappingItemCollection

from System.Data.Metadata.Edm import (DataSpace, EdmItemCollection, 
    EntityContainer, GlobalItem, MetadataItem, StoreItemCollection)

from System.IO import Stream, TextWriter

from System.Xml import XmlReader

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class EdmToObjectNamespaceMap: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: EdmToObjectNamespaceMap) -> int """
        ...

    @property
    def EdmNamespaces(self) -> ICollection:
        """ Get: EdmNamespaces(self: EdmToObjectNamespaceMap) -> ICollection[str] """
        ...


    def Add(self, edmNamespace:str, objectNamespace:str): # -> 
        """ Add(self: EdmToObjectNamespaceMap, edmNamespace: str, objectNamespace: str) """
        ...

    def Clear(self): # -> 
        """ Clear(self: EdmToObjectNamespaceMap) """
        ...

    def Contains(self, edmNamespace:str) -> bool:
        """ Contains(self: EdmToObjectNamespaceMap, edmNamespace: str) -> bool """
        ...

    def Remove(self, edmNamespace:str) -> bool:
        """ Remove(self: EdmToObjectNamespaceMap, edmNamespace: str) -> bool """
        ...

    def TryGetObjectNamespace(self, edmNamespace, objectNamespace) -> Tuple_[bool, str]:
        """ TryGetObjectNamespace(self: EdmToObjectNamespaceMap, edmNamespace: str) -> (bool, str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class EntityClassGenerator: # skipped bases: <type 'object'>, <type 'object'>
    """
    EntityClassGenerator()
    EntityClassGenerator(languageOption: LanguageOption)
    """
    @property
    def EdmToObjectNamespaceMap(self) -> EdmToObjectNamespaceMap:
        """ Get: EdmToObjectNamespaceMap(self: EntityClassGenerator) -> EdmToObjectNamespaceMap """
        ...

    @property
    def LanguageOption(self) -> LanguageOption:
        """
        Get: LanguageOption(self: EntityClassGenerator) -> LanguageOption
        Set: LanguageOption(self: EntityClassGenerator) = value
        """
        ...


    def GenerateCode(self, *__args) -> IList:
        """
        GenerateCode(self: EntityClassGenerator, sourceEdmSchema: XmlReader, target: TextWriter) -> IList[EdmSchemaError]
        GenerateCode(self: EntityClassGenerator, sourceEdmSchema: XmlReader, target: TextWriter, additionalEdmSchemas: IEnumerable[XmlReader]) -> IList[EdmSchemaError]
        GenerateCode(self: EntityClassGenerator, sourceEdmSchemaFilePath: str, targetFilePath: str) -> IList[EdmSchemaError]
        GenerateCode(self: EntityClassGenerator, sourceEdmSchemaFilePath: str, targetPath: str, additionalEdmSchemaFilePaths: IEnumerable[str]) -> IList[EdmSchemaError]
        """
        ...

    OnPropertyGenerated = ...
    OnTypeGenerated = ...


class EntityCodeGenerator: # skipped bases: <type 'object'>, <type 'object'>
    """ EntityCodeGenerator(languageOption: LanguageOption) """
    @property
    def EdmToObjectNamespaceMap(self) -> EdmToObjectNamespaceMap:
        """ Get: EdmToObjectNamespaceMap(self: EntityCodeGenerator) -> EdmToObjectNamespaceMap """
        ...

    @property
    def LanguageOption(self) -> LanguageOption:
        """
        Get: LanguageOption(self: EntityCodeGenerator) -> LanguageOption
        Set: LanguageOption(self: EntityCodeGenerator) = value
        """
        ...


    def GenerateCode(self, *__args) -> IList:
        """
        GenerateCode(self: EntityCodeGenerator, sourceEdmSchemaFilePath: str, targetPath: str, additionalEdmSchemaFilePaths: IEnumerable[str], targetEntityFrameworkVersion: Version) -> IList[EdmSchemaError]
        GenerateCode(self: EntityCodeGenerator, sourceEdmSchemaFilePath: str, targetPath: str, additionalEdmSchemaFilePaths: IEnumerable[str]) -> IList[EdmSchemaError]
        GenerateCode(self: EntityCodeGenerator, sourceEdmSchemaFilePath: str, targetPath: str, targetEntityFrameworkVersion: Version) -> IList[EdmSchemaError]
        GenerateCode(self: EntityCodeGenerator, sourceEdmSchemaFilePath: str, targetPath: str) -> IList[EdmSchemaError]
        GenerateCode(self: EntityCodeGenerator, sourceEdmSchema: XmlReader, target: TextWriter, targetEntityFrameworkVersion: Version) -> IList[EdmSchemaError]
        GenerateCode(self: EntityCodeGenerator, sourceEdmSchema: XmlReader, target: TextWriter) -> IList[EdmSchemaError]
        GenerateCode(self: EntityCodeGenerator, sourceEdmSchema: XmlReader, target: TextWriter, additionalEdmSchemas: IEnumerable[XmlReader], targetEntityFrameworkVersion: Version) -> IList[EdmSchemaError]
        GenerateCode(self: EntityCodeGenerator, sourceEdmSchema: XmlReader, target: TextWriter, additionalEdmSchemas: IEnumerable[XmlReader]) -> IList[EdmSchemaError]
        """
        ...


class EntityFrameworkVersions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetSchemaXsd(entityFrameworkVersion:Version, dataSpace:DataSpace) -> Stream:
        """ GetSchemaXsd(entityFrameworkVersion: Version, dataSpace: DataSpace) -> Stream """
        ...

    Version1: Version = ...
    Version2: Version = ...
    Version3: Version = ...
    __all__: list = ...


class EntityModelSchemaGenerator: # skipped bases: <type 'object'>, <type 'object'>
    """
    EntityModelSchemaGenerator(storeEntityContainer: EntityContainer)
    EntityModelSchemaGenerator(storeEntityContainer: EntityContainer, namespaceName: str, modelEntityContainerName: str)
    EntityModelSchemaGenerator(storeItemCollection: StoreItemCollection, namespaceName: str, modelEntityContainerName: str)
    """
    @property
    def EdmItemCollection(self) -> EdmItemCollection:
        """ Get: EdmItemCollection(self: EntityModelSchemaGenerator) -> EdmItemCollection """
        ...

    @property
    def EntityContainer(self) -> EntityContainer:
        """ Get: EntityContainer(self: EntityModelSchemaGenerator) -> EntityContainer """
        ...

    @property
    def GenerateForeignKeyProperties(self) -> bool:
        """
        Get: GenerateForeignKeyProperties(self: EntityModelSchemaGenerator) -> bool
        Set: GenerateForeignKeyProperties(self: EntityModelSchemaGenerator) = value
        """
        ...

    @property
    def PluralizationService(self) -> PluralizationService:
        """
        Get: PluralizationService(self: EntityModelSchemaGenerator) -> PluralizationService
        Set: PluralizationService(self: EntityModelSchemaGenerator) = value
        """
        ...


    def GenerateMetadata(self, targetEntityFrameworkVersion:Version = ...) -> IList:
        """
        GenerateMetadata(self: EntityModelSchemaGenerator) -> IList[EdmSchemaError]
        GenerateMetadata(self: EntityModelSchemaGenerator, targetEntityFrameworkVersion: Version) -> IList[EdmSchemaError]
        """
        ...

    def WriteModelSchema(self, *__args:str): # -> 
        """ WriteModelSchema(self: EntityModelSchemaGenerator, outputFileName: str)WriteModelSchema(self: EntityModelSchemaGenerator, writer: XmlWriter) """
        ...

    def WriteStorageMapping(self, *__args:str): # -> 
        """ WriteStorageMapping(self: EntityModelSchemaGenerator, outputFileName: str)WriteStorageMapping(self: EntityModelSchemaGenerator, writer: XmlWriter) """
        ...


class EntityStoreSchemaFilterEffect(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EntityStoreSchemaFilterEffect, values: Allow (0), Exclude (1) """
    Allow: EntityStoreSchemaFilterEffect = ...
    Exclude: EntityStoreSchemaFilterEffect = ...
    value__ = ...


class EntityStoreSchemaFilterEntry: # skipped bases: <type 'object'>, <type 'object'>
    """
    EntityStoreSchemaFilterEntry(catalog: str, schema: str, name: str, types: EntityStoreSchemaFilterObjectTypes, effect: EntityStoreSchemaFilterEffect)
    EntityStoreSchemaFilterEntry(catalog: str, schema: str, name: str)
    """
    @property
    def Catalog(self) -> str:
        """ Get: Catalog(self: EntityStoreSchemaFilterEntry) -> str """
        ...

    @property
    def Effect(self) -> EntityStoreSchemaFilterEffect:
        """ Get: Effect(self: EntityStoreSchemaFilterEntry) -> EntityStoreSchemaFilterEffect """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: EntityStoreSchemaFilterEntry) -> str """
        ...

    @property
    def Schema(self) -> str:
        """ Get: Schema(self: EntityStoreSchemaFilterEntry) -> str """
        ...

    @property
    def Types(self) -> EntityStoreSchemaFilterObjectTypes:
        """ Get: Types(self: EntityStoreSchemaFilterEntry) -> EntityStoreSchemaFilterObjectTypes """
        ...



class EntityStoreSchemaFilterObjectTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) EntityStoreSchemaFilterObjectTypes, values: All (7), Function (4), None (0), Table (1), View (2) """
    All: EntityStoreSchemaFilterObjectTypes = ...
    Function: EntityStoreSchemaFilterObjectTypes = ...
    Table: EntityStoreSchemaFilterObjectTypes = ...
    value__ = ...
    View: EntityStoreSchemaFilterObjectTypes = ...


class EntityStoreSchemaGenerator: # skipped bases: <type 'object'>, <type 'object'>
    """ EntityStoreSchemaGenerator(providerInvariantName: str, connectionString: str, namespaceName: str) """
    @property
    def EntityContainer(self) -> EntityContainer:
        """ Get: EntityContainer(self: EntityStoreSchemaGenerator) -> EntityContainer """
        ...

    @property
    def GenerateForeignKeyProperties(self) -> bool:
        """
        Get: GenerateForeignKeyProperties(self: EntityStoreSchemaGenerator) -> bool
        Set: GenerateForeignKeyProperties(self: EntityStoreSchemaGenerator) = value
        """
        ...

    @property
    def StoreItemCollection(self) -> StoreItemCollection:
        """ Get: StoreItemCollection(self: EntityStoreSchemaGenerator) -> StoreItemCollection """
        ...


    @staticmethod
    def CreateStoreSchemaConnection(providerInvariantName:str, connectionString:str, targetEntityFrameworkVersion:Version = ...) -> EntityConnection:
        """
        CreateStoreSchemaConnection(providerInvariantName: str, connectionString: str) -> EntityConnection
        CreateStoreSchemaConnection(providerInvariantName: str, connectionString: str, targetEntityFrameworkVersion: Version) -> EntityConnection
        """
        ...

    def GenerateStoreMetadata(self, filters:IEnumerable = ..., targetEntityFrameworkVersion:Version = ...) -> IList:
        """
        GenerateStoreMetadata(self: EntityStoreSchemaGenerator) -> IList[EdmSchemaError]
        GenerateStoreMetadata(self: EntityStoreSchemaGenerator, filters: IEnumerable[EntityStoreSchemaFilterEntry]) -> IList[EdmSchemaError]
        GenerateStoreMetadata(self: EntityStoreSchemaGenerator, filters: IEnumerable[EntityStoreSchemaFilterEntry], targetEntityFrameworkVersion: Version) -> IList[EdmSchemaError]
        """
        ...

    def WriteStoreSchema(self, *__args:str): # -> 
        """ WriteStoreSchema(self: EntityStoreSchemaGenerator, outputFileName: str)WriteStoreSchema(self: EntityStoreSchemaGenerator, writer: XmlWriter) """
        ...


class EntityViewGenerator: # skipped bases: <type 'object'>, <type 'object'>
    """
    EntityViewGenerator(languageOption: LanguageOption)
    EntityViewGenerator()
    """
    @property
    def LanguageOption(self) -> LanguageOption:
        """
        Get: LanguageOption(self: EntityViewGenerator) -> LanguageOption
        Set: LanguageOption(self: EntityViewGenerator) = value
        """
        ...


    def GenerateViews(self, mappingCollection:StorageMappingItemCollection, *__args:str) -> IList:
        """
        GenerateViews(self: EntityViewGenerator, mappingCollection: StorageMappingItemCollection, outputPath: str) -> IList[EdmSchemaError]
        GenerateViews(self: EntityViewGenerator, mappingCollection: StorageMappingItemCollection, outputWriter: TextWriter) -> IList[EdmSchemaError]
        GenerateViews(self: EntityViewGenerator, mappingCollection: StorageMappingItemCollection, outputWriter: TextWriter, targetEntityFrameworkVersion: Version) -> IList[EdmSchemaError]
        """
        ...

    @staticmethod
    def Validate(mappingCollection:StorageMappingItemCollection, targetEntityFrameworkVersion:Version = ...) -> IList:
        """
        Validate(mappingCollection: StorageMappingItemCollection) -> IList[EdmSchemaError]
        Validate(mappingCollection: StorageMappingItemCollection, targetEntityFrameworkVersion: Version) -> IList[EdmSchemaError]
        """
        ...


class LanguageOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LanguageOption, values: GenerateCSharpCode (0), GenerateVBCode (1) """
    GenerateCSharpCode: LanguageOption = ...
    GenerateVBCode: LanguageOption = ...
    value__ = ...


class MetadataExtensionMethods: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetPrimitiveTypes(itemCollection:EdmItemCollection, edmVersion:Version) -> ReadOnlyCollection:
        """ GetPrimitiveTypes(itemCollection: EdmItemCollection, edmVersion: Version) -> ReadOnlyCollection[PrimitiveType] """
        ...

    __all__: list = ...


class MetadataItemCollectionFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateEdmItemCollection(readers:IEnumerable, *__args:Version) -> Tuple_[EdmItemCollection, IList]:
        """
        CreateEdmItemCollection(readers: IEnumerable[XmlReader]) -> (EdmItemCollection, IList[EdmSchemaError])
        CreateEdmItemCollection(readers: IEnumerable[XmlReader], targetEntityFrameworkVersion: Version) -> (EdmItemCollection, IList[EdmSchemaError])
        """
        ...

    @staticmethod
    def CreateStorageMappingItemCollection(edmCollection:EdmItemCollection, storeCollection:StoreItemCollection, readers:IEnumerable, *__args:Version) -> Tuple_[StorageMappingItemCollection, IList]:
        """
        CreateStorageMappingItemCollection(edmCollection: EdmItemCollection, storeCollection: StoreItemCollection, readers: IEnumerable[XmlReader]) -> (StorageMappingItemCollection, IList[EdmSchemaError])
        CreateStorageMappingItemCollection(edmCollection: EdmItemCollection, storeCollection: StoreItemCollection, readers: IEnumerable[XmlReader], targetEntityFrameworkVersion: Version) -> (StorageMappingItemCollection, IList[EdmSchemaError])
        """
        ...

    @staticmethod
    def CreateStoreItemCollection(readers:IEnumerable, *__args:Version) -> Tuple_[StoreItemCollection, IList]:
        """
        CreateStoreItemCollection(readers: IEnumerable[XmlReader]) -> (StoreItemCollection, IList[EdmSchemaError])
        CreateStoreItemCollection(readers: IEnumerable[XmlReader], targetEntityFrameworkVersion: Version) -> (StoreItemCollection, IList[EdmSchemaError])
        """
        ...

    __all__: list = ...


class PropertyGeneratedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    PropertyGeneratedEventArgs()
    PropertyGeneratedEventArgs(propertySource: MetadataItem, backingFieldName: str, returnType: CodeTypeReference)
    """
    @property
    def AdditionalAttributes(self) -> List:
        """ Get: AdditionalAttributes(self: PropertyGeneratedEventArgs) -> List[CodeAttributeDeclaration] """
        ...

    @property
    def AdditionalGetStatements(self) -> List:
        """ Get: AdditionalGetStatements(self: PropertyGeneratedEventArgs) -> List[CodeStatement] """
        ...

    @property
    def AdditionalSetStatements(self) -> List:
        """ Get: AdditionalSetStatements(self: PropertyGeneratedEventArgs) -> List[CodeStatement] """
        ...

    @property
    def BackingFieldName(self) -> str:
        """ Get: BackingFieldName(self: PropertyGeneratedEventArgs) -> str """
        ...

    @property
    def PropertySource(self) -> MetadataItem:
        """ Get: PropertySource(self: PropertyGeneratedEventArgs) -> MetadataItem """
        ...

    @property
    def ReturnType(self) -> CodeTypeReference:
        """
        Get: ReturnType(self: PropertyGeneratedEventArgs) -> CodeTypeReference
        Set: ReturnType(self: PropertyGeneratedEventArgs) = value
        """
        ...


    def __new__(cls, propertySource:MetadataItem = ..., backingFieldName:str = ..., returnType:CodeTypeReference = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, propertySource: MetadataItem, backingFieldName: str, returnType: CodeTypeReference)
        """
        ...


class PropertyGeneratedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ PropertyGeneratedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:PropertyGeneratedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: PropertyGeneratedEventHandler, sender: object, e: PropertyGeneratedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: PropertyGeneratedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:PropertyGeneratedEventArgs): # -> 
        """ Invoke(self: PropertyGeneratedEventHandler, sender: object, e: PropertyGeneratedEventArgs) """
        ...


class TypeGeneratedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    TypeGeneratedEventArgs()
    TypeGeneratedEventArgs(typeSource: GlobalItem, baseType: CodeTypeReference)
    """
    @property
    def AdditionalAttributes(self) -> List:
        """ Get: AdditionalAttributes(self: TypeGeneratedEventArgs) -> List[CodeAttributeDeclaration] """
        ...

    @property
    def AdditionalInterfaces(self) -> List:
        """ Get: AdditionalInterfaces(self: TypeGeneratedEventArgs) -> List[Type] """
        ...

    @property
    def AdditionalMembers(self) -> List:
        """ Get: AdditionalMembers(self: TypeGeneratedEventArgs) -> List[CodeTypeMember] """
        ...

    @property
    def BaseType(self) -> CodeTypeReference:
        """
        Get: BaseType(self: TypeGeneratedEventArgs) -> CodeTypeReference
        Set: BaseType(self: TypeGeneratedEventArgs) = value
        """
        ...

    @property
    def TypeSource(self) -> GlobalItem:
        """ Get: TypeSource(self: TypeGeneratedEventArgs) -> GlobalItem """
        ...


    def __new__(cls, typeSource:GlobalItem = ..., baseType:CodeTypeReference = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, typeSource: GlobalItem, baseType: CodeTypeReference)
        """
        ...


class TypeGeneratedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TypeGeneratedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:TypeGeneratedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: TypeGeneratedEventHandler, sender: object, e: TypeGeneratedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: TypeGeneratedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:TypeGeneratedEventArgs): # -> 
        """ Invoke(self: TypeGeneratedEventHandler, sender: object, e: TypeGeneratedEventArgs) """
        ...


# variables with complex values

