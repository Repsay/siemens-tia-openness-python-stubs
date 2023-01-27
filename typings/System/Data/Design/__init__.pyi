# encoding: utf-8
# module System.Data.Design calls itself Design
# from System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum, Type

from System.CodeDom import (CodeCompileUnit, CodeMemberMethod, CodeNamespace, 
    CodeTypeDeclaration)

from System.CodeDom.Compiler import CodeDomProvider

from System.Collections import ICollection, IList

from System.Data import DataException

from System.Data.Common import DbProviderFactory

from System.Runtime.Serialization import SerializationInfo, StreamingContext

from System.Xml.Serialization.Advanced import SchemaImporterExtension

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class MethodSignatureGenerator: # skipped bases: <type 'object'>, <type 'object'>
    """ MethodSignatureGenerator() """
    @property
    def CodeProvider(self) -> CodeDomProvider:
        """
        Get: CodeProvider(self: MethodSignatureGenerator) -> CodeDomProvider
        Set: CodeProvider(self: MethodSignatureGenerator) = value
        """
        ...

    @property
    def ContainerParameterType(self) -> Type:
        """
        Get: ContainerParameterType(self: MethodSignatureGenerator) -> Type
        Set: ContainerParameterType(self: MethodSignatureGenerator) = value
        """
        ...

    @property
    def DataSetClassName(self) -> str:
        """
        Get: DataSetClassName(self: MethodSignatureGenerator) -> str
        Set: DataSetClassName(self: MethodSignatureGenerator) = value
        """
        ...

    @property
    def IsGetMethod(self) -> bool:
        """
        Get: IsGetMethod(self: MethodSignatureGenerator) -> bool
        Set: IsGetMethod(self: MethodSignatureGenerator) = value
        """
        ...

    @property
    def PagingMethod(self) -> bool:
        """
        Get: PagingMethod(self: MethodSignatureGenerator) -> bool
        Set: PagingMethod(self: MethodSignatureGenerator) = value
        """
        ...

    @property
    def ParameterOption(self) -> ParameterGenerationOption:
        """
        Get: ParameterOption(self: MethodSignatureGenerator) -> ParameterGenerationOption
        Set: ParameterOption(self: MethodSignatureGenerator) = value
        """
        ...

    @property
    def TableClassName(self) -> str:
        """
        Get: TableClassName(self: MethodSignatureGenerator) -> str
        Set: TableClassName(self: MethodSignatureGenerator) = value
        """
        ...


    def GenerateMethod(self) -> CodeMemberMethod:
        """ GenerateMethod(self: MethodSignatureGenerator) -> CodeMemberMethod """
        ...

    def GenerateMethodSignature(self) -> str:
        """ GenerateMethodSignature(self: MethodSignatureGenerator) -> str """
        ...

    def GenerateUpdatingMethods(self) -> CodeTypeDeclaration:
        """ GenerateUpdatingMethods(self: MethodSignatureGenerator) -> CodeTypeDeclaration """
        ...

    def SetDesignTableContent(self, designTableContent:str): # -> 
        """ SetDesignTableContent(self: MethodSignatureGenerator, designTableContent: str) """
        ...

    def SetMethodSourceContent(self, methodSourceContent:str): # -> 
        """ SetMethodSourceContent(self: MethodSignatureGenerator, methodSourceContent: str) """
        ...


class ParameterGenerationOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ParameterGenerationOption, values: ClrTypes (0), Objects (2), SqlTypes (1) """
    ClrTypes: ParameterGenerationOption = ...
    Objects: ParameterGenerationOption = ...
    SqlTypes: ParameterGenerationOption = ...
    value__ = ...


class TypedDataSetGenerator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ReferencedAssemblies(self) -> ICollection:
        """ Get: ReferencedAssemblies() -> ICollection[Assembly] """
        ...


    @staticmethod
    def Generate(*__args): # -> 
        """
        Generate(inputFileContent: str, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, codeProvider: CodeDomProvider, specifiedFactory: DbProviderFactory)Generate(inputFileContent: str, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, codeProvider: CodeDomProvider, customDBProviders: Hashtable)Generate(inputFileContent: str, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, codeProvider: CodeDomProvider, customDBProviders: Hashtable, option: GenerateOption)Generate(inputFileContent: str, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, codeProvider: CodeDomProvider, customDBProviders: Hashtable, option: GenerateOption, dataSetNamespace: str)Generate(inputFileContent: str, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, codeProvider: CodeDomProvider, customDBProviders: Hashtable, option: GenerateOption, dataSetNamespace: str, basePath: str)Generate(inputFileContent: str, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, codeProvider: CodeDomProvider) -> str
        Generate(inputFileContent: str, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, codeProvider: CodeDomProvider, option: GenerateOption) -> str
        Generate(inputFileContent: str, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, codeProvider: CodeDomProvider, option: GenerateOption, dataSetNamespace: str) -> str
        Generate(dataSet: DataSet, codeNamespace: CodeNamespace, codeProvider: CodeDomProvider) -> str
        Generate(inputFileContent: str, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, codeProvider: CodeDomProvider, option: GenerateOption, dataSetNamespace: str, basePath: str) -> str
        """
        ...

    def GenerateOption(self, *args): #cannot find CLR method
        """ enum (flags) GenerateOption, values: HierarchicalUpdate (1), LinqOverTypedDatasets (2), None (0) """
        ...

    @staticmethod
    def GetProviderName(inputFileContent:str, tableName:str = ...) -> str:
        """
        GetProviderName(inputFileContent: str) -> str
        GetProviderName(inputFileContent: str, tableName: str) -> str
        """
        ...



class TypedDataSetGeneratorException(DataException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TypedDataSetGeneratorException()
    TypedDataSetGeneratorException(message: str)
    TypedDataSetGeneratorException(message: str, innerException: Exception)
    TypedDataSetGeneratorException(list: IList)
    """
    @property
    def ErrorList(self) -> IList:
        """ Get: ErrorList(self: TypedDataSetGeneratorException) -> IList """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: TypedDataSetGeneratorException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class TypedDataSetSchemaImporterExtension(SchemaImporterExtension): # skipped bases: <type 'object'>
    """ TypedDataSetSchemaImporterExtension() """
    def __new__(cls) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, dataSetGenerateOptions: GenerateOption)
        """
        ...


class TypedDataSetSchemaImporterExtensionFx35(TypedDataSetSchemaImporterExtension): # skipped bases: <type 'object'>
    """ TypedDataSetSchemaImporterExtensionFx35() """
    pass

