# encoding: utf-8
# module System.Resources.Tools calls itself Tools
# from System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Type

from System.CodeDom import CodeCompileUnit

from System.CodeDom.Compiler import CodeDomProvider

from System.Collections import IDictionary

from typing import Tuple as Tuple_


# no functions
# classes

class ITargetAwareCodeDomProvider: # skipped bases: <type 'object'>
    """ no doc """
    def SupportsProperty(self, type:Type, propertyName:str, isWritable:bool) -> bool:
        """ SupportsProperty(self: ITargetAwareCodeDomProvider, type: Type, propertyName: str, isWritable: bool) -> bool """
        ...


class StronglyTypedResourceBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Create(*__args) -> Tuple_[CodeCompileUnit, Array]:
        """
        Create(resourceList: IDictionary, baseName: str, generatedCodeNamespace: str, codeProvider: CodeDomProvider, internalClass: bool) -> (CodeCompileUnit, Array[str])
        Create(resxFile: str, baseName: str, generatedCodeNamespace: str, codeProvider: CodeDomProvider, internalClass: bool) -> (CodeCompileUnit, Array[str])
        Create(resourceList: IDictionary, baseName: str, generatedCodeNamespace: str, resourcesNamespace: str, codeProvider: CodeDomProvider, internalClass: bool) -> (CodeCompileUnit, Array[str])
        Create(resxFile: str, baseName: str, generatedCodeNamespace: str, resourcesNamespace: str, codeProvider: CodeDomProvider, internalClass: bool) -> (CodeCompileUnit, Array[str])
        """
        ...

    @staticmethod
    def VerifyResourceName(key:str, provider:CodeDomProvider) -> str:
        """ VerifyResourceName(key: str, provider: CodeDomProvider) -> str """
        ...

    __all__: list = ...


