# encoding: utf-8
# module System.Data.Services.Design calls itself Design
# from System.Data.Services.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum, EventArgs

from System.CodeDom import CodeTypeReference

from System.Collections import ICollection, IList

from System.Collections.Generic import List

from System.Data.Metadata.Edm import GlobalItem, MetadataItem

from System.Xml import XmlReader

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class DataServiceCodeVersion(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DataServiceCodeVersion, values: V1 (0), V2 (1) """
    V1: DataServiceCodeVersion = ...
    V2: DataServiceCodeVersion = ...
    value__ = ...


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

    @property
    def UseDataServiceCollection(self) -> bool:
        """
        Get: UseDataServiceCollection(self: EntityClassGenerator) -> bool
        Set: UseDataServiceCollection(self: EntityClassGenerator) = value
        """
        ...

    @property
    def Version(self) -> DataServiceCodeVersion:
        """
        Get: Version(self: EntityClassGenerator) -> DataServiceCodeVersion
        Set: Version(self: EntityClassGenerator) = value
        """
        ...


    def GenerateCode(self, sourceReader:XmlReader, *__args:str) -> IList:
        """
        GenerateCode(self: EntityClassGenerator, sourceReader: XmlReader, targetFilePath: str) -> IList[EdmSchemaError]
        GenerateCode(self: EntityClassGenerator, sourceReader: XmlReader, targetWriter: TextWriter, namespacePrefix: str) -> IList[EdmSchemaError]
        """
        ...

    OnPropertyGenerated = ...
    OnTypeGenerated = ...


class LanguageOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LanguageOption, values: GenerateCSharpCode (0), GenerateVBCode (1) """
    GenerateCSharpCode: LanguageOption = ...
    GenerateVBCode: LanguageOption = ...
    value__ = ...


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


