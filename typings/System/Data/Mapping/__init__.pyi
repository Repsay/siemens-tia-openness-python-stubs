# encoding: utf-8
# module System.Data.Mapping calls itself Mapping
# from System.Data.Entity, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Attribute, Type

from System.Data.Metadata.Edm import (EdmItemCollection, ItemCollection, 
    StoreItemCollection)

from typing import Self


# no functions
# classes

class EntityViewContainer: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def EdmEntityContainerName(self) -> str:
        """
        Get: EdmEntityContainerName(self: EntityViewContainer) -> str
        Set: EdmEntityContainerName(self: EntityViewContainer) = value
        """
        ...

    @property
    def HashOverAllExtentViews(self) -> str:
        """
        Get: HashOverAllExtentViews(self: EntityViewContainer) -> str
        Set: HashOverAllExtentViews(self: EntityViewContainer) = value
        """
        ...

    @property
    def HashOverMappingClosure(self) -> str:
        """
        Get: HashOverMappingClosure(self: EntityViewContainer) -> str
        Set: HashOverMappingClosure(self: EntityViewContainer) = value
        """
        ...

    @property
    def StoreEntityContainerName(self) -> str:
        """
        Get: StoreEntityContainerName(self: EntityViewContainer) -> str
        Set: StoreEntityContainerName(self: EntityViewContainer) = value
        """
        ...

    @property
    def ViewCount(self) -> int:
        """ Get: ViewCount(self: EntityViewContainer) -> int """
        ...


    def GetViewAt(self, *args): #cannot find CLR method
        """ GetViewAt(self: EntityViewContainer, index: int) -> KeyValuePair[str, str] """
        ...


class EntityViewGenerationAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EntityViewGenerationAttribute(viewGenerationType: Type) """
    @property
    def ViewGenerationType(self) -> Type:
        """ Get: ViewGenerationType(self: EntityViewGenerationAttribute) -> Type """
        ...


    def __new__(cls, viewGenerationType:Type) -> Self:
        """ __new__(cls: type, viewGenerationType: Type) """
        ...


class MappingItemCollection(ItemCollection): # skipped bases: <type 'IList[GlobalItem]'>, <type 'IReadOnlyCollection[GlobalItem]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[GlobalItem]'>, <type 'IReadOnlyList[GlobalItem]'>, <type 'IEnumerable[GlobalItem]'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class StorageMappingItemCollection(MappingItemCollection): # skipped bases: <type 'IList[GlobalItem]'>, <type 'IReadOnlyCollection[GlobalItem]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[GlobalItem]'>, <type 'IReadOnlyList[GlobalItem]'>, <type 'IEnumerable[GlobalItem]'>, <type 'ICollection'>, <type 'object'>
    """
    StorageMappingItemCollection(edmCollection: EdmItemCollection, storeCollection: StoreItemCollection, *filePaths: Array[str])
    StorageMappingItemCollection(edmCollection: EdmItemCollection, storeCollection: StoreItemCollection, xmlReaders: IEnumerable[XmlReader])
    """
    @property
    def MappingVersion(self) -> float:
        """ Get: MappingVersion(self: StorageMappingItemCollection) -> float """
        ...


    def __new__(cls, edmCollection:EdmItemCollection, storeCollection:StoreItemCollection, *__args:Array) -> Self:
        """
        __new__(cls: type, edmCollection: EdmItemCollection, storeCollection: StoreItemCollection, *filePaths: Array[str])
        __new__(cls: type, edmCollection: EdmItemCollection, storeCollection: StoreItemCollection, xmlReaders: IEnumerable[XmlReader])
        """
        ...


