# encoding: utf-8
# module Microsoft.PowerShell.Commands.StringManipulation.FlashExtractText.Semantics.Internal calls itself Internal
# from Microsoft.PowerShell.Commands.Utility, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, IComparable, IEquatable, Tuple, UInt32

from System.Collections.Generic import Dictionary, List

from System.Text.RegularExpressions import Regex

from System.Xml.Linq import XElement

from typing import Tuple as Tuple_

"""The following names are not found in the module: (IRenderableLiteral, 
    field#)
"""

# no functions
# classes

class CachedList(List): # skipped bases: <type 'IReadOnlyList[PositionMatch]'>, <type 'IList[PositionMatch]'>, <type 'ICollection[PositionMatch]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IReadOnlyCollection[PositionMatch]'>, <type 'IEnumerable[PositionMatch]'>, <type 'ICollection'>, <type 'object'>
    """
    CachedList()
    CachedList(l: IEnumerable[PositionMatch])
    """
    def BinarySearchForFirstGreaterOrEqual(self, key:UInt32) -> int:
        """ BinarySearchForFirstGreaterOrEqual(self: CachedList, key: UInt32) -> int """
        ...

    def BinarySearchForFirstLessThanOrEqual(self, key:UInt32) -> int:
        """ BinarySearchForFirstLessThanOrEqual(self: CachedList, key: UInt32) -> int """
        ...

    def GetValues(self, start:UInt32, end:UInt32) -> Tuple:
        """ GetValues(self: CachedList, start: UInt32, end: UInt32) -> Tuple[int, int] """
        ...


class PositionMatch: # skipped bases: <type 'object'>, <type 'object'>
    """ PositionMatch(p: UInt32, l: UInt32) """
    def Equals(self, *__args:PositionMatch) -> bool:
        """
        Equals(self: PositionMatch, other: PositionMatch) -> bool
        Equals(self: PositionMatch, obj: object) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: PositionMatch) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Length = ...
    Position = ...
    Right = ...


class RegularExpression(IRenderableLiteral): # skipped bases: <type 'object'>
    """ RegularExpression(regExp1: Token, regExp2: Token, regExp3: Token, exampleCount: int) """
    @property
    def Display(self) -> str:
        """ Get: Display(self: RegularExpression) -> str """
        ...

    @property
    def Regex(self) -> Regex:
        """ Get: Regex(self: RegularExpression) -> Regex """
        ...

    @property
    def Score(self) -> int:
        """ Get: Score(self: RegularExpression) -> int """
        ...


    @staticmethod
    def Create(*__args:int) -> RegularExpression:
        """
        Create(exampleCount: int) -> RegularExpression
        Create(token: Token, exampleCount: int) -> RegularExpression
        Create(re: Token, regularExpressionList: RegularExpression) -> RegularExpression
        Create(regex: RegularExpression, re: Token) -> RegularExpression
        Create(token1: Token, token2: Token, exampleCount: int) -> RegularExpression
        Create(token1: Token, token2: Token, token3: Token, exampleCount: int) -> RegularExpression
        """
        ...

    def Equals(self, other:object) -> bool:
        """ Equals(self: RegularExpression, other: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: RegularExpression) -> int """
        ...

    def LeftMatchesAt(self, context:SynthesisContext, position:UInt32, start:UInt32, end:UInt32) -> bool:
        """ LeftMatchesAt(self: RegularExpression, context: SynthesisContext, position: UInt32, start: UInt32, end: UInt32) -> bool """
        ...

    def MatchesAt(self, context:SynthesisContext, position:UInt32, start:UInt32 = ..., end:UInt32 = ...) -> bool:
        """
        MatchesAt(self: RegularExpression, context: SynthesisContext, position: UInt32) -> bool
        MatchesAt(self: RegularExpression, context: SynthesisContext, position: UInt32, start: UInt32, end: UInt32) -> bool
        """
        ...

    def Render(self) -> str:
        """ Render(self: RegularExpression) -> str """
        ...

    def RenderXml(self) -> XElement:
        """ RenderXml(self: RegularExpression) -> XElement """
        ...

    def Run(self, *__args:SynthesisContext) -> List:
        """
        Run(self: RegularExpression, context: SynthesisContext) -> List[PositionMatch]
        Run(self: RegularExpression, range: Tuple[SynthesisContext, Tuple[UInt32, UInt32]]) -> List[PositionMatch]
        Run(self: RegularExpression, context: SynthesisContext, start: UInt32, end: UInt32) -> List[PositionMatch]
        """
        ...

    def ToRegexJsonArray(self) -> Array:
        """ ToRegexJsonArray(self: RegularExpression) -> Array[str] """
        ...

    def ToRegexString(self) -> str:
        """ ToRegexString(self: RegularExpression) -> str """
        ...

    def ToString(self) -> str:
        """ ToString(self: RegularExpression) -> str """
        ...

    @staticmethod
    def TryParse(literal:str) -> RegularExpression:
        """ TryParse(literal: str) -> RegularExpression """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Count = ...
    ExampleCount = ...


class SynthesisContext: # skipped bases: <type 'object'>, <type 'object'>
    """ SynthesisContext(s: str) """
    @property
    def Content(self) -> str:
        """ Get: Content(self: SynthesisContext) -> str """
        ...

    @property
    def EndPosition(self) -> UInt32:
        """ Get: EndPosition(self: SynthesisContext) -> UInt32 """
        ...

    @property
    def FieldRegex(self) -> RegularExpression:
        """ Get: FieldRegex(self: SynthesisContext) -> RegularExpression """
        ...

    @property
    def InputEndIsPrecise(self) -> bool:
        """ Get: InputEndIsPrecise(self: SynthesisContext) -> bool """
        ...

    @property
    def InputStartIsPrecise(self) -> bool:
        """ Get: InputStartIsPrecise(self: SynthesisContext) -> bool """
        ...

    @property
    def PrefixFieldRegex(self) -> RegularExpression:
        """ Get: PrefixFieldRegex(self: SynthesisContext) -> RegularExpression """
        ...

    @property
    def StartPosition(self) -> UInt32:
        """ Get: StartPosition(self: SynthesisContext) -> UInt32 """
        ...

    @property
    def SuffixFieldRegex(self) -> RegularExpression:
        """ Get: SuffixFieldRegex(self: SynthesisContext) -> RegularExpression """
        ...


    @staticmethod
    def AddStaticToken(token:Token): # -> 
        """ AddStaticToken(token: Token) """
        ...

    @staticmethod
    def GetStaticTokenByName(name:str) -> Token:
        """ GetStaticTokenByName(name: str) -> Token """
        ...

    def InitializeLearningContext(self, examples:List, inputStartIsPrecise:bool, inputEndIsPrecise:bool, prefixRegex:Regex, contentRegex:Regex, suffixRegex:Regex): # -> 
        """ InitializeLearningContext(self: SynthesisContext, examples: List[Tuple[UInt32, UInt32]], inputStartIsPrecise: bool, inputEndIsPrecise: bool, prefixRegex: Regex, contentRegex: Regex, suffixRegex: Regex) """
        ...

    def TryGetAllMatchesEndingAt(self, pos, matches) -> Tuple_[bool, Dictionary]:
        """ TryGetAllMatchesEndingAt(self: SynthesisContext, pos: UInt32) -> (bool, Dictionary[Token, TokenMatch]) """
        ...

    def TryGetAllMatchesStartingAt(self, pos, matches) -> Tuple_[bool, Dictionary]:
        """ TryGetAllMatchesStartingAt(self: SynthesisContext, pos: UInt32) -> (bool, Dictionary[Token, TokenMatch]) """
        ...

    def TryGetMatchPositionsFor(self, token, matchPositions) -> Tuple_[bool, CachedList]:
        """ TryGetMatchPositionsFor(self: SynthesisContext, token: Token) -> (bool, CachedList) """
        ...

    def TryGetTokenMatchEndingAt(self, pos, token, match) -> Tuple_[bool, TokenMatch]:
        """ TryGetTokenMatchEndingAt(self: SynthesisContext, pos: UInt32, token: Token) -> (bool, TokenMatch) """
        ...

    def TryGetTokenMatchStartingAt(self, pos, token, match) -> Tuple_[bool, TokenMatch]:
        """ TryGetTokenMatchStartingAt(self: SynthesisContext, pos: UInt32, token: Token) -> (bool, TokenMatch) """
        ...


class Token(IComparable, IEquatable): # skipped bases: <type 'object'>
    """ Token(regex: Regex, name: str, score: int, isSymbol: bool) """
    @property
    def Display(self) -> str:
        """ Get: Display(self: Token) -> str """
        ...

    @property
    def IsDynamicToken(self) -> bool:
        """ Get: IsDynamicToken(self: Token) -> bool """
        ...

    @property
    def IsSymbol(self) -> bool:
        """ Get: IsSymbol(self: Token) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Token) -> str """
        ...

    @property
    def Regex(self) -> Regex:
        """ Get: Regex(self: Token) -> Regex """
        ...

    @property
    def Score(self) -> int:
        """ Get: Score(self: Token) -> int """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: Token) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Token) -> str """
        ...

    def ToXml(self) -> XElement:
        """ ToXml(self: Token) -> XElement """
        ...

    @staticmethod
    def TryParse(xml:XElement) -> Token:
        """ TryParse(xml: XElement) -> Token """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    LineSeparatorName: str = ...
    MinScore: int = ...


class TokenMatch(IEquatable): # skipped bases: <type 'object'>
    """ TokenMatch(t: Token, l: UInt32) """
    def GetHashCode(self) -> int:
        """ GetHashCode(self: TokenMatch) -> int """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Length = ...
    Token = ...


