# encoding: utf-8
# module System.Speech.Recognition.SrgsGrammar calls itself SrgsGrammar
# from System.Speech, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import Array, Enum, MarshalByRefObject, Single, Uri

from System.Collections.ObjectModel import KeyedCollection

from System.Globalization import CultureInfo

from System.IO import Stream

from System.Speech.Recognition import SubsetMatchingMode

from System.Xml import XmlWriter

from typing import Self

"""The following names are not found in the module: (IElement, IElementText, 
    IItem, IOneOf, IPropertyTag, IRule, IRuleRef, ISemanticTag, ISubset, 
    IToken, field#)
"""

# no functions
# classes

class SrgsDocument: # skipped bases: <type 'object'>, <type 'object'>
    """
    SrgsDocument()
    SrgsDocument(path: str)
    SrgsDocument(srgsGrammar: XmlReader)
    SrgsDocument(builder: GrammarBuilder)
    SrgsDocument(grammarRootRule: SrgsRule)
    """
    @property
    def AssemblyReferences(self) -> Collection:
        """ Get: AssemblyReferences(self: SrgsDocument) -> Collection[str] """
        ...

    @property
    def CodeBehind(self) -> Collection:
        """ Get: CodeBehind(self: SrgsDocument) -> Collection[str] """
        ...

    @property
    def Culture(self) -> CultureInfo:
        """
        Get: Culture(self: SrgsDocument) -> CultureInfo
        Set: Culture(self: SrgsDocument) = value
        """
        ...

    @property
    def Debug(self) -> bool:
        """
        Get: Debug(self: SrgsDocument) -> bool
        Set: Debug(self: SrgsDocument) = value
        """
        ...

    @property
    def ImportNamespaces(self) -> Collection:
        """ Get: ImportNamespaces(self: SrgsDocument) -> Collection[str] """
        ...

    @property
    def Language(self) -> str:
        """
        Get: Language(self: SrgsDocument) -> str
        Set: Language(self: SrgsDocument) = value
        """
        ...

    @property
    def Mode(self) -> SrgsGrammarMode:
        """
        Get: Mode(self: SrgsDocument) -> SrgsGrammarMode
        Set: Mode(self: SrgsDocument) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: SrgsDocument) -> str
        Set: Namespace(self: SrgsDocument) = value
        """
        ...

    @property
    def PhoneticAlphabet(self) -> SrgsPhoneticAlphabet:
        """
        Get: PhoneticAlphabet(self: SrgsDocument) -> SrgsPhoneticAlphabet
        Set: PhoneticAlphabet(self: SrgsDocument) = value
        """
        ...

    @property
    def Root(self) -> SrgsRule:
        """
        Get: Root(self: SrgsDocument) -> SrgsRule
        Set: Root(self: SrgsDocument) = value
        """
        ...

    @property
    def Rules(self) -> SrgsRulesCollection:
        """ Get: Rules(self: SrgsDocument) -> SrgsRulesCollection """
        ...

    @property
    def Script(self) -> str:
        """
        Get: Script(self: SrgsDocument) -> str
        Set: Script(self: SrgsDocument) = value
        """
        ...

    @property
    def XmlBase(self) -> Uri:
        """
        Get: XmlBase(self: SrgsDocument) -> Uri
        Set: XmlBase(self: SrgsDocument) = value
        """
        ...


    def WriteSrgs(self, srgsGrammar:XmlWriter): # -> 
        """ WriteSrgs(self: SrgsDocument, srgsGrammar: XmlWriter) """
        ...


class SrgsElement(MarshalByRefObject, IElement): # skipped bases: <type 'object'>
    """ no doc """
    pass

class SrgsGrammarCompiler: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Compile(*__args): # -> 
        """ Compile(inputPath: str, outputStream: Stream)Compile(srgsGrammar: SrgsDocument, outputStream: Stream)Compile(reader: XmlReader, outputStream: Stream) """
        ...

    @staticmethod
    def CompileClassLibrary(*__args): # -> 
        """ CompileClassLibrary(inputPaths: Array[str], outputPath: str, referencedAssemblies: Array[str], keyFile: str)CompileClassLibrary(srgsGrammar: SrgsDocument, outputPath: str, referencedAssemblies: Array[str], keyFile: str)CompileClassLibrary(reader: XmlReader, outputPath: str, referencedAssemblies: Array[str], keyFile: str) """
        ...

    __all__: list = ...


class SrgsGrammarMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SrgsGrammarMode, values: Dtmf (1), Voice (0) """
    Dtmf: SrgsGrammarMode = ...
    value__ = ...
    Voice: SrgsGrammarMode = ...


class SrgsItem(IItem, SrgsElement): # skipped bases: <type 'IElement'>, <type 'object'>
    """
    SrgsItem()
    SrgsItem(text: str)
    SrgsItem(*elements: Array[SrgsElement])
    SrgsItem(repeatCount: int)
    SrgsItem(min: int, max: int)
    SrgsItem(min: int, max: int, text: str)
    SrgsItem(min: int, max: int, *elements: Array[SrgsElement])
    """
    @property
    def Elements(self) -> Collection:
        """ Get: Elements(self: SrgsItem) -> Collection[SrgsElement] """
        ...

    @property
    def MaxRepeat(self) -> int:
        """ Get: MaxRepeat(self: SrgsItem) -> int """
        ...

    @property
    def MinRepeat(self) -> int:
        """ Get: MinRepeat(self: SrgsItem) -> int """
        ...

    @property
    def RepeatProbability(self) -> Single:
        """
        Get: RepeatProbability(self: SrgsItem) -> Single
        Set: RepeatProbability(self: SrgsItem) = value
        """
        ...

    @property
    def Weight(self) -> Single:
        """
        Get: Weight(self: SrgsItem) -> Single
        Set: Weight(self: SrgsItem) = value
        """
        ...


    def Add(self, element:SrgsElement): # -> 
        """ Add(self: SrgsItem, element: SrgsElement) """
        ...

    def SetRepeat(self, *__args:int): # -> 
        """ SetRepeat(self: SrgsItem, count: int)SetRepeat(self: SrgsItem, minRepeat: int, maxRepeat: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, text: str)
        __new__(cls: type, *elements: Array[SrgsElement])
        __new__(cls: type, repeatCount: int)
        __new__(cls: type, min: int, max: int)
        __new__(cls: type, min: int, max: int, text: str)
        __new__(cls: type, min: int, max: int, *elements: Array[SrgsElement])
        """
        ...


class SrgsNameValueTag(IPropertyTag, SrgsElement): # skipped bases: <type 'IElement'>, <type 'object'>
    """
    SrgsNameValueTag()
    SrgsNameValueTag(value: object)
    SrgsNameValueTag(name: str, value: object)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: SrgsNameValueTag) -> str
        Set: Name(self: SrgsNameValueTag) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: SrgsNameValueTag) -> object
        Set: Value(self: SrgsNameValueTag) = value
        """
        ...


    def __new__(cls, *__args:object) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, value: object)
        __new__(cls: type, name: str, value: object)
        """
        ...


class SrgsOneOf(IOneOf, SrgsElement): # skipped bases: <type 'IElement'>, <type 'object'>
    """
    SrgsOneOf()
    SrgsOneOf(*items: Array[str])
    SrgsOneOf(*items: Array[SrgsItem])
    """
    @property
    def Items(self) -> Collection:
        """ Get: Items(self: SrgsOneOf) -> Collection[SrgsItem] """
        ...


    def Add(self, item:SrgsItem): # -> 
        """ Add(self: SrgsOneOf, item: SrgsItem) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __new__(cls, items:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, *items: Array[str])
        __new__(cls: type, *items: Array[SrgsItem])
        """
        ...


class SrgsPhoneticAlphabet(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SrgsPhoneticAlphabet, values: Ipa (1), Sapi (0), Ups (2) """
    Ipa: SrgsPhoneticAlphabet = ...
    Sapi: SrgsPhoneticAlphabet = ...
    Ups: SrgsPhoneticAlphabet = ...
    value__ = ...


class SrgsRule(IRule): # skipped bases: <type 'IElement'>, <type 'object'>
    """
    SrgsRule(id: str)
    SrgsRule(id: str, *elements: Array[SrgsElement])
    """
    @property
    def BaseClass(self) -> str:
        """
        Get: BaseClass(self: SrgsRule) -> str
        Set: BaseClass(self: SrgsRule) = value
        """
        ...

    @property
    def Elements(self) -> Collection:
        """ Get: Elements(self: SrgsRule) -> Collection[SrgsElement] """
        ...

    @property
    def Id(self) -> str:
        """
        Get: Id(self: SrgsRule) -> str
        Set: Id(self: SrgsRule) = value
        """
        ...

    @property
    def OnError(self) -> str:
        """
        Get: OnError(self: SrgsRule) -> str
        Set: OnError(self: SrgsRule) = value
        """
        ...

    @property
    def OnInit(self) -> str:
        """
        Get: OnInit(self: SrgsRule) -> str
        Set: OnInit(self: SrgsRule) = value
        """
        ...

    @property
    def OnParse(self) -> str:
        """
        Get: OnParse(self: SrgsRule) -> str
        Set: OnParse(self: SrgsRule) = value
        """
        ...

    @property
    def OnRecognition(self) -> str:
        """
        Get: OnRecognition(self: SrgsRule) -> str
        Set: OnRecognition(self: SrgsRule) = value
        """
        ...

    @property
    def Scope(self) -> SrgsRuleScope:
        """
        Get: Scope(self: SrgsRule) -> SrgsRuleScope
        Set: Scope(self: SrgsRule) = value
        """
        ...

    @property
    def Script(self) -> str:
        """
        Get: Script(self: SrgsRule) -> str
        Set: Script(self: SrgsRule) = value
        """
        ...


    def Add(self, element:SrgsElement): # -> 
        """ Add(self: SrgsRule, element: SrgsElement) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class SrgsRuleRef(IRuleRef, SrgsElement): # skipped bases: <type 'IElement'>, <type 'object'>
    """
    SrgsRuleRef(uri: Uri)
    SrgsRuleRef(uri: Uri, rule: str)
    SrgsRuleRef(uri: Uri, rule: str, semanticKey: str)
    SrgsRuleRef(uri: Uri, rule: str, semanticKey: str, parameters: str)
    SrgsRuleRef(rule: SrgsRule)
    SrgsRuleRef(rule: SrgsRule, semanticKey: str)
    SrgsRuleRef(rule: SrgsRule, semanticKey: str, parameters: str)
    """
    @property
    def Params(self) -> str:
        """ Get: Params(self: SrgsRuleRef) -> str """
        ...

    @property
    def SemanticKey(self) -> str:
        """ Get: SemanticKey(self: SrgsRuleRef) -> str """
        ...

    @property
    def Uri(self) -> Uri:
        """ Get: Uri(self: SrgsRuleRef) -> Uri """
        ...


    def __new__(cls, *__args:Uri) -> Self:
        """
        __new__(cls: type, uri: Uri)
        __new__(cls: type, uri: Uri, rule: str)
        __new__(cls: type, uri: Uri, rule: str, semanticKey: str)
        __new__(cls: type, uri: Uri, rule: str, semanticKey: str, parameters: str)
        __new__(cls: type, rule: SrgsRule)
        __new__(cls: type, rule: SrgsRule, semanticKey: str)
        __new__(cls: type, rule: SrgsRule, semanticKey: str, parameters: str)
        """
        ...

    Dictation: SrgsRuleRef = ...
    Garbage: SrgsRuleRef = ...
    MnemonicSpelling: SrgsRuleRef = ...
    Null: SrgsRuleRef = ...
    Void: SrgsRuleRef = ...


class SrgsRulesCollection(KeyedCollection): # skipped bases: <type 'IList[SrgsRule]'>, <type 'ICollection[SrgsRule]'>, <type 'IEnumerable[SrgsRule]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IReadOnlyCollection[SrgsRule]'>, <type 'ICollection'>, <type 'IReadOnlyList[SrgsRule]'>, <type 'object'>
    """ SrgsRulesCollection() """
    pass

class SrgsRuleScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SrgsRuleScope, values: Private (1), Public (0) """
    Private: SrgsRuleScope = ...
    Public: SrgsRuleScope = ...
    value__ = ...


class SrgsSemanticInterpretationTag(ISemanticTag, SrgsElement): # skipped bases: <type 'IElement'>, <type 'object'>
    """
    SrgsSemanticInterpretationTag()
    SrgsSemanticInterpretationTag(script: str)
    """
    @property
    def Script(self) -> str:
        """
        Get: Script(self: SrgsSemanticInterpretationTag) -> str
        Set: Script(self: SrgsSemanticInterpretationTag) = value
        """
        ...


    def __new__(cls, script:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, script: str)
        """
        ...


class SrgsSubset(ISubset, SrgsElement): # skipped bases: <type 'IElement'>, <type 'object'>
    """
    SrgsSubset(text: str)
    SrgsSubset(text: str, matchingMode: SubsetMatchingMode)
    """
    @property
    def MatchingMode(self) -> SubsetMatchingMode:
        """
        Get: MatchingMode(self: SrgsSubset) -> SubsetMatchingMode
        Set: MatchingMode(self: SrgsSubset) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: SrgsSubset) -> str
        Set: Text(self: SrgsSubset) = value
        """
        ...


    def __new__(cls, text:str, matchingMode:SubsetMatchingMode = ...) -> Self:
        """
        __new__(cls: type, text: str)
        __new__(cls: type, text: str, matchingMode: SubsetMatchingMode)
        """
        ...


class SrgsText(IElementText, SrgsElement): # skipped bases: <type 'IElement'>, <type 'object'>
    """
    SrgsText()
    SrgsText(text: str)
    """
    @property
    def Text(self) -> str:
        """
        Get: Text(self: SrgsText) -> str
        Set: Text(self: SrgsText) = value
        """
        ...


    def __new__(cls, text:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, text: str)
        """
        ...


class SrgsToken(IToken, SrgsElement): # skipped bases: <type 'IElement'>, <type 'object'>
    """ SrgsToken(text: str) """
    @property
    def Display(self) -> str:
        """
        Get: Display(self: SrgsToken) -> str
        Set: Display(self: SrgsToken) = value
        """
        ...

    @property
    def Pronunciation(self) -> str:
        """
        Get: Pronunciation(self: SrgsToken) -> str
        Set: Pronunciation(self: SrgsToken) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: SrgsToken) -> str
        Set: Text(self: SrgsToken) = value
        """
        ...


    def __new__(cls, text:str) -> Self:
        """ __new__(cls: type, text: str) """
        ...


