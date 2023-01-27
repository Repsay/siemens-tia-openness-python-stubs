# encoding: utf-8
# module Babel
# from Microsoft.SqlServer.Management.SqlParser, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum, Nullable

from System.Activities import Location

from System.Collections import IList

from System.Collections.Generic import List

from typing import Tuple as Tuple_

"""The following names are not found in the module: field#
"""

# no functions
# classes

class CodeObjectQuickInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    EndLocation = ...
    StartLocation = ...
    Text = ...


class LineScanner: # skipped bases: <type 'object'>, <type 'object'>
    """ LineScanner() """
    @property
    def BatchSeparator(self) -> str:
        """
        Get: BatchSeparator(self: LineScanner) -> str
        Set: BatchSeparator(self: LineScanner) = value
        """
        ...

    @property
    def IsSqlCmdModeEnabled(self) -> bool:
        """
        Get: IsSqlCmdModeEnabled(self: LineScanner) -> bool
        Set: IsSqlCmdModeEnabled(self: LineScanner) = value
        """
        ...


    @staticmethod
    def DefineToken(token:int, type:TokenType, trigger:TokenTriggers): # -> 
        """ DefineToken(token: int, type: TokenType, trigger: TokenTriggers) """
        ...

    def PopulateDefiniton(self, tokenInfo:TokenInfo): # -> 
        """ PopulateDefiniton(self: LineScanner, tokenInfo: TokenInfo) """
        ...

    def ScanTokenAndProvideInfoAboutIt(self, tokenInfo:TokenInfo, state:int) -> Tuple_[bool, int]:
        """ ScanTokenAndProvideInfoAboutIt(self: LineScanner, tokenInfo: TokenInfo, state: int) -> (bool, int) """
        ...

    def SetSource(self, source:str, offset:int): # -> 
        """ SetSource(self: LineScanner, source: str, offset: int) """
        ...


class MethodHelpText: # skipped bases: <type 'object'>, <type 'object'>
    """ MethodHelpText(name: str, description: str, type: str, shouldShowParentheses: bool, isVarArg: bool) """
    @property
    def Description(self) -> str:
        """ Get: Description(self: MethodHelpText) -> str """
        ...

    @property
    def IsVarArg(self) -> bool:
        """ Get: IsVarArg(self: MethodHelpText) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MethodHelpText) -> str """
        ...

    @property
    def Parameters(self) -> IList:
        """ Get: Parameters(self: MethodHelpText) -> IList[Parameter] """
        ...

    @property
    def ShouldShowParentheses(self) -> bool:
        """ Get: ShouldShowParentheses(self: MethodHelpText) -> bool """
        ...

    @property
    def Type(self) -> str:
        """ Get: Type(self: MethodHelpText) -> str """
        ...


    def ToXml(self) -> str:
        """ ToXml(self: MethodHelpText) -> str """
        ...


class MethodNameAndParamLocations: # skipped bases: <type 'object'>, <type 'object'>
    """ MethodNameAndParamLocations(name: str) """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: MethodNameAndParamLocations) -> str
        Set: Name(self: MethodNameAndParamLocations) = value
        """
        ...

    @property
    def NameEndLocation(self) -> Location:
        """
        Get: NameEndLocation(self: MethodNameAndParamLocations) -> Location
        Set: NameEndLocation(self: MethodNameAndParamLocations) = value
        """
        ...

    @property
    def NameStartLocation(self) -> Location:
        """
        Get: NameStartLocation(self: MethodNameAndParamLocations) -> Location
        Set: NameStartLocation(self: MethodNameAndParamLocations) = value
        """
        ...

    @property
    def ParamEndLocation(self) -> Nullable:
        """
        Get: ParamEndLocation(self: MethodNameAndParamLocations) -> Nullable[Location]
        Set: ParamEndLocation(self: MethodNameAndParamLocations) = value
        """
        ...

    @property
    def ParamSeperatorLocations(self) -> List:
        """
        Get: ParamSeperatorLocations(self: MethodNameAndParamLocations) -> List[Location]
        Set: ParamSeperatorLocations(self: MethodNameAndParamLocations) = value
        """
        ...

    @property
    def ParamStartLocation(self) -> Nullable:
        """
        Get: ParamStartLocation(self: MethodNameAndParamLocations) -> Nullable[Location]
        Set: ParamStartLocation(self: MethodNameAndParamLocations) = value
        """
        ...


    def ToXml(self) -> str:
        """ ToXml(self: MethodNameAndParamLocations) -> str """
        ...


class Parameter: # skipped bases: <type 'object'>, <type 'object'>
    """ Parameter(name: str, description: str, display: str) """
    @property
    def Description(self) -> str:
        """ Get: Description(self: Parameter) -> str """
        ...

    @property
    def Display(self) -> str:
        """ Get: Display(self: Parameter) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Parameter) -> str """
        ...



class Region: # skipped bases: <type 'object'>, <type 'object'>
    """ Region(startLocation: Location, endLocation: Location) """
    @property
    def EndLocation(self) -> Location:
        """ Get: EndLocation(self: Region) -> Location """
        ...

    @property
    def StartLocation(self) -> Location:
        """ Get: StartLocation(self: Region) -> Location """
        ...



class TokenInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ TokenInfo() """
    def ToString(self) -> str:
        """ ToString(self: TokenInfo) -> str """
        ...

    EndIndex = ...
    StartIndex = ...
    Token = ...
    Trigger = ...
    Type = ...


class TokenTriggers(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TokenTriggers, values: MatchBraces (2), MemberSelect (1), MethodTip (240), None (0), Parameter (128), ParameterEnd (64), ParameterNext (32), ParameterStart (16) """
    MatchBraces: TokenTriggers = ...
    MemberSelect: TokenTriggers = ...
    MethodTip: TokenTriggers = ...
    Parameter: TokenTriggers = ...
    ParameterEnd: TokenTriggers = ...
    ParameterNext: TokenTriggers = ...
    ParameterStart: TokenTriggers = ...
    value__ = ...


class TokenType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TokenType, values: Comment (2), Delimiter (14), Error (13), Identifier (3), Keyword (1), Number (5), SqlCmdCommand (12), SqlOperator (10), SqlStoredProcedure (7), SqlString (11), SqlSystemFunction (9), SqlSystemTable (8), Text (0) """
    Comment: TokenType = ...
    Delimiter: TokenType = ...
    Error: TokenType = ...
    Identifier: TokenType = ...
    Keyword: TokenType = ...
    Number: TokenType = ...
    SqlCmdCommand: TokenType = ...
    SqlOperator: TokenType = ...
    SqlStoredProcedure: TokenType = ...
    SqlString: TokenType = ...
    SqlSystemFunction: TokenType = ...
    SqlSystemTable: TokenType = ...
    Text: TokenType = ...
    value__ = ...


# variables with complex values

