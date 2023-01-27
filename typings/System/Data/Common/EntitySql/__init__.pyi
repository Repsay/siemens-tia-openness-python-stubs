# encoding: utf-8
# module System.Data.Common.EntitySql calls itself EntitySql
# from System.Data.Entity, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array

from System.Collections.ObjectModel import ReadOnlyCollection

from System.Data.Common.CommandTrees import DbCommandTree, DbLambda


# no functions
# classes

class EntitySqlParser: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Parse(self, query:str, parameters:Array) -> ParseResult:
        """ Parse(self: EntitySqlParser, query: str, *parameters: Array[DbParameterReferenceExpression]) -> ParseResult """
        ...

    def ParseLambda(self, query:str, variables:Array) -> DbLambda:
        """ ParseLambda(self: EntitySqlParser, query: str, *variables: Array[DbVariableReferenceExpression]) -> DbLambda """
        ...


class FunctionDefinition: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def EndPosition(self) -> int:
        """ Get: EndPosition(self: FunctionDefinition) -> int """
        ...

    @property
    def Lambda(self) -> DbLambda:
        """ Get: Lambda(self: FunctionDefinition) -> DbLambda """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: FunctionDefinition) -> str """
        ...

    @property
    def StartPosition(self) -> int:
        """ Get: StartPosition(self: FunctionDefinition) -> int """
        ...



class ParseResult: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CommandTree(self) -> DbCommandTree:
        """ Get: CommandTree(self: ParseResult) -> DbCommandTree """
        ...

    @property
    def FunctionDefinitions(self) -> ReadOnlyCollection:
        """ Get: FunctionDefinitions(self: ParseResult) -> ReadOnlyCollection[FunctionDefinition] """
        ...



