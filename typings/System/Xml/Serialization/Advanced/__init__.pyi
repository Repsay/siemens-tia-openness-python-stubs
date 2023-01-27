# encoding: utf-8
# module System.Xml.Serialization.Advanced calls itself Advanced
# from System.Xml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array

from System.CodeDom import CodeCompileUnit, CodeExpression, CodeNamespace

from System.CodeDom.Compiler import CodeDomProvider

from System.Collections import CollectionBase

from System.Xml.Schema import XmlSchemaAny, XmlSchemaObject

from System.Xml.Serialization import (CodeGenerationOptions, 
    XmlSchemaImporter, XmlSchemas)


# no functions
# classes

class SchemaImporterExtension: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def ImportAnyElement(self, any:XmlSchemaAny, mixed:bool, schemas:XmlSchemas, importer:XmlSchemaImporter, compileUnit:CodeCompileUnit, mainNamespace:CodeNamespace, options:CodeGenerationOptions, codeProvider:CodeDomProvider) -> str:
        """ ImportAnyElement(self: SchemaImporterExtension, any: XmlSchemaAny, mixed: bool, schemas: XmlSchemas, importer: XmlSchemaImporter, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, options: CodeGenerationOptions, codeProvider: CodeDomProvider) -> str """
        ...

    def ImportDefaultValue(self, value:str, type:str) -> CodeExpression:
        """ ImportDefaultValue(self: SchemaImporterExtension, value: str, type: str) -> CodeExpression """
        ...

    def ImportSchemaType(self, *__args) -> str:
        """
        ImportSchemaType(self: SchemaImporterExtension, name: str, ns: str, context: XmlSchemaObject, schemas: XmlSchemas, importer: XmlSchemaImporter, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, options: CodeGenerationOptions, codeProvider: CodeDomProvider) -> str
        ImportSchemaType(self: SchemaImporterExtension, type: XmlSchemaType, context: XmlSchemaObject, schemas: XmlSchemas, importer: XmlSchemaImporter, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, options: CodeGenerationOptions, codeProvider: CodeDomProvider) -> str
        """
        ...


class SchemaImporterExtensionCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ SchemaImporterExtensionCollection() """
    def Add(self, *__args:SchemaImporterExtension) -> int:
        """
        Add(self: SchemaImporterExtensionCollection, extension: SchemaImporterExtension) -> int
        Add(self: SchemaImporterExtensionCollection, name: str, type: Type) -> int
        """
        ...

    def Contains(self, extension:SchemaImporterExtension) -> bool:
        """ Contains(self: SchemaImporterExtensionCollection, extension: SchemaImporterExtension) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: SchemaImporterExtensionCollection, array: Array[SchemaImporterExtension], index: int) """
        ...

    def IndexOf(self, extension:SchemaImporterExtension) -> int:
        """ IndexOf(self: SchemaImporterExtensionCollection, extension: SchemaImporterExtension) -> int """
        ...

    def Insert(self, index:int, extension:SchemaImporterExtension): # -> 
        """ Insert(self: SchemaImporterExtensionCollection, index: int, extension: SchemaImporterExtension) """
        ...

    def Remove(self, *__args:str): # -> 
        """ Remove(self: SchemaImporterExtensionCollection, name: str)Remove(self: SchemaImporterExtensionCollection, extension: SchemaImporterExtension) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


