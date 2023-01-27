# encoding: utf-8
# module Microsoft.VisualBasic.Activities calls itself Activities
# from System.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import IEquatable, Type

from System.Activities import (ActivityWithResult, CodeActivity, 
    LocationReferenceEnvironment)

from System.Activities.ExpressionParser import SourceExpressionException

from System.Activities.Expressions import ITextExpression

from System.Activities.XamlIntegration import IValueSerializableExpression

from System.Collections import IEnumerable

from System.Collections.Generic import ISet

from System.Data import Constraint

from System.EnterpriseServices import Activity

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: IExpressionContainer
"""

# no functions
# classes

class VisualBasic: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetSettings(target:object) -> VisualBasicSettings:
        """ GetSettings(target: object) -> VisualBasicSettings """
        ...

    @staticmethod
    def SetSettings(target:object, value:VisualBasicSettings): # -> 
        """ SetSettings(target: object, value: VisualBasicSettings) """
        ...

    @staticmethod
    def SetSettingsForImplementation(target:object, value:VisualBasicSettings): # -> 
        """ SetSettingsForImplementation(target: object, value: VisualBasicSettings) """
        ...

    @staticmethod
    def ShouldSerializeSettings(target:object) -> bool:
        """ ShouldSerializeSettings(target: object) -> bool """
        ...

    __all__: list = ...


class VisualBasicDesignerHelper: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def NameShadowingConstraint(self) -> Constraint:
        """ Get: NameShadowingConstraint() -> Constraint """
        ...


    @staticmethod
    def CreatePrecompiledVisualBasicReference(targetType, expressionText, namespaces, referencedAssemblies, environment, returnType, compileError, vbSettings) -> Tuple_[Activity, Type, SourceExpressionException, VisualBasicSettings]:
        """ CreatePrecompiledVisualBasicReference(targetType: Type, expressionText: str, namespaces: IEnumerable[str], referencedAssemblies: IEnumerable[str], environment: LocationReferenceEnvironment) -> (Activity, Type, SourceExpressionException, VisualBasicSettings) """
        ...

    @staticmethod
    def CreatePrecompiledVisualBasicValue(targetType, expressionText, namespaces, referencedAssemblies, environment, returnType, compileError, vbSettings) -> Tuple_[Activity, Type, SourceExpressionException, VisualBasicSettings]:
        """ CreatePrecompiledVisualBasicValue(targetType: Type, expressionText: str, namespaces: IEnumerable[str], referencedAssemblies: IEnumerable[str], environment: LocationReferenceEnvironment) -> (Activity, Type, SourceExpressionException, VisualBasicSettings) """
        ...

    @staticmethod
    def RecompileVisualBasicReference(visualBasicReference, returnType, compileError, vbSettings) -> Tuple_[Activity, Type, SourceExpressionException, VisualBasicSettings]:
        """ RecompileVisualBasicReference(visualBasicReference: ActivityWithResult) -> (Activity, Type, SourceExpressionException, VisualBasicSettings) """
        ...

    @staticmethod
    def RecompileVisualBasicValue(visualBasicValue, returnType, compileError, vbSettings) -> Tuple_[Activity, Type, SourceExpressionException, VisualBasicSettings]:
        """ RecompileVisualBasicValue(visualBasicValue: ActivityWithResult) -> (Activity, Type, SourceExpressionException, VisualBasicSettings) """
        ...

    __all__: list = ...


class VisualBasicImportReference(IEquatable): # skipped bases: <type 'object'>
    """ VisualBasicImportReference() """
    @property
    def Assembly(self) -> str:
        """
        Get: Assembly(self: VisualBasicImportReference) -> str
        Set: Assembly(self: VisualBasicImportReference) = value
        """
        ...

    @property
    def Import(self) -> str:
        """
        Get: Import(self: VisualBasicImportReference) -> str
        Set: Import(self: VisualBasicImportReference) = value
        """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: VisualBasicImportReference) -> int """
        ...


class VisualBasicReference(IExpressionContainer, ITextExpression, IValueSerializableExpression, CodeActivity): # skipped bases: <type 'object'>
    """
    VisualBasicReference[TResult]()
    VisualBasicReference[TResult](expressionText: str)
    """
    def __new__(cls, expressionText:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, expressionText: str)
        """
        ...


class VisualBasicSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ VisualBasicSettings() """
    @property
    def Default(self) -> VisualBasicSettings:
        """ Get: Default() -> VisualBasicSettings """
        ...

    @property
    def ImportReferences(self) -> ISet:
        """ Get: ImportReferences(self: VisualBasicSettings) -> ISet[VisualBasicImportReference] """
        ...




class VisualBasicValue(IExpressionContainer, ITextExpression, IValueSerializableExpression, CodeActivity): # skipped bases: <type 'object'>
    """
    VisualBasicValue[TResult]()
    VisualBasicValue[TResult](expressionText: str)
    """
    def __new__(cls, expressionText:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, expressionText: str)
        """
        ...


# variables with complex values

