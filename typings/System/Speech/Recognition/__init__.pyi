# encoding: utf-8
# module System.Speech.Recognition calls itself Recognition
# from System.Speech, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import (Array, DateTime, Enum, EventArgs, IDisposable, Single, 
    TimeSpan, Type)

from System.Collections import IDictionary

from System.Collections.Generic import KeyValuePair

from System.Collections.ObjectModel import ReadOnlyCollection

from System.ComponentModel import AsyncCompletedEventArgs

from System.Globalization import CultureInfo

from System.IO import Stream

from System.Runtime.Serialization import ISerializable

from System.Speech.AudioFormat import SpeechAudioFormatInfo

from System.Xml.XPath import IXPathNavigable

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class AudioLevelUpdatedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AudioLevel(self) -> int:
        """ Get: AudioLevel(self: AudioLevelUpdatedEventArgs) -> int """
        ...



class AudioSignalProblem(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AudioSignalProblem, values: None (0), NoSignal (2), TooFast (5), TooLoud (3), TooNoisy (1), TooSlow (6), TooSoft (4) """
    NoSignal: AudioSignalProblem = ...
    TooFast: AudioSignalProblem = ...
    TooLoud: AudioSignalProblem = ...
    TooNoisy: AudioSignalProblem = ...
    TooSlow: AudioSignalProblem = ...
    TooSoft: AudioSignalProblem = ...
    value__ = ...


class AudioSignalProblemOccurredEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AudioLevel(self) -> int:
        """ Get: AudioLevel(self: AudioSignalProblemOccurredEventArgs) -> int """
        ...

    @property
    def AudioPosition(self) -> TimeSpan:
        """ Get: AudioPosition(self: AudioSignalProblemOccurredEventArgs) -> TimeSpan """
        ...

    @property
    def AudioSignalProblem(self) -> AudioSignalProblem:
        """ Get: AudioSignalProblem(self: AudioSignalProblemOccurredEventArgs) -> AudioSignalProblem """
        ...

    @property
    def RecognizerAudioPosition(self) -> TimeSpan:
        """ Get: RecognizerAudioPosition(self: AudioSignalProblemOccurredEventArgs) -> TimeSpan """
        ...



class AudioState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AudioState, values: Silence (1), Speech (2), Stopped (0) """
    Silence: AudioState = ...
    Speech: AudioState = ...
    Stopped: AudioState = ...
    value__ = ...


class AudioStateChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AudioState(self) -> AudioState:
        """ Get: AudioState(self: AudioStateChangedEventArgs) -> AudioState """
        ...



class Choices: # skipped bases: <type 'object'>, <type 'object'>
    """
    Choices()
    Choices(*phrases: Array[str])
    Choices(*alternateChoices: Array[GrammarBuilder])
    """
    def Add(self, *__args:Array): # -> 
        """ Add(self: Choices, *phrases: Array[str])Add(self: Choices, *alternateChoices: Array[GrammarBuilder]) """
        ...

    def ToGrammarBuilder(self) -> GrammarBuilder:
        """ ToGrammarBuilder(self: Choices) -> GrammarBuilder """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...


class Grammar: # skipped bases: <type 'object'>, <type 'object'>
    """
    Grammar(path: str)
    Grammar(path: str, ruleName: str)
    Grammar(path: str, ruleName: str, parameters: Array[object])
    Grammar(srgsDocument: SrgsDocument)
    Grammar(srgsDocument: SrgsDocument, ruleName: str)
    Grammar(srgsDocument: SrgsDocument, ruleName: str, parameters: Array[object])
    Grammar(srgsDocument: SrgsDocument, ruleName: str, baseUri: Uri)
    Grammar(srgsDocument: SrgsDocument, ruleName: str, baseUri: Uri, parameters: Array[object])
    Grammar(stream: Stream)
    Grammar(stream: Stream, ruleName: str)
    Grammar(stream: Stream, ruleName: str, parameters: Array[object])
    Grammar(stream: Stream, ruleName: str, baseUri: Uri)
    Grammar(stream: Stream, ruleName: str, baseUri: Uri, parameters: Array[object])
    Grammar(builder: GrammarBuilder)
    """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: Grammar) -> bool
        Set: Enabled(self: Grammar) = value
        """
        ...

    @property
    def IsStg(self):
        ...

    @property
    def Loaded(self) -> bool:
        """ Get: Loaded(self: Grammar) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Grammar) -> str
        Set: Name(self: Grammar) = value
        """
        ...

    @property
    def Priority(self) -> int:
        """
        Get: Priority(self: Grammar) -> int
        Set: Priority(self: Grammar) = value
        """
        ...

    @property
    def ResourceName(self):
        ...

    @property
    def RuleName(self) -> str:
        """ Get: RuleName(self: Grammar) -> str """
        ...

    @property
    def Weight(self) -> Single:
        """
        Get: Weight(self: Grammar) -> Single
        Set: Weight(self: Grammar) = value
        """
        ...


    @staticmethod
    def LoadLocalizedGrammarFromType(type:Type, onInitParameters:Array) -> Grammar:
        """ LoadLocalizedGrammarFromType(type: Type, *onInitParameters: Array[object]) -> Grammar """
        ...

    def StgInit(self, *args): #cannot find CLR method
        """ StgInit(self: Grammar, parameters: Array[object]) """
        ...

    SpeechRecognized = ...


class DictationGrammar(Grammar): # skipped bases: <type 'object'>
    """
    DictationGrammar()
    DictationGrammar(topic: str)
    """
    def SetDictationContext(self, precedingText:str, subsequentText:str): # -> 
        """ SetDictationContext(self: DictationGrammar, precedingText: str, subsequentText: str) """
        ...


class DisplayAttributes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DisplayAttributes, values: ConsumeLeadingSpaces (16), None (0), OneTrailingSpace (4), TwoTrailingSpaces (8), ZeroTrailingSpaces (2) """
    ConsumeLeadingSpaces: DisplayAttributes = ...
    OneTrailingSpace: DisplayAttributes = ...
    TwoTrailingSpaces: DisplayAttributes = ...
    value__ = ...
    ZeroTrailingSpaces: DisplayAttributes = ...


class EmulateRecognizeCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Result(self) -> RecognitionResult:
        """ Get: Result(self: EmulateRecognizeCompletedEventArgs) -> RecognitionResult """
        ...



class GrammarBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """
    GrammarBuilder()
    GrammarBuilder(phrase: str)
    GrammarBuilder(phrase: str, subsetMatchingCriteria: SubsetMatchingMode)
    GrammarBuilder(phrase: str, minRepeat: int, maxRepeat: int)
    GrammarBuilder(builder: GrammarBuilder, minRepeat: int, maxRepeat: int)
    GrammarBuilder(alternateChoices: Choices)
    GrammarBuilder(key: SemanticResultKey)
    GrammarBuilder(value: SemanticResultValue)
    """
    @property
    def Culture(self) -> CultureInfo:
        """
        Get: Culture(self: GrammarBuilder) -> CultureInfo
        Set: Culture(self: GrammarBuilder) = value
        """
        ...

    @property
    def DebugShowPhrases(self) -> str:
        """ Get: DebugShowPhrases(self: GrammarBuilder) -> str """
        ...


    @staticmethod
    def Add(*__args) -> GrammarBuilder:
        """
        Add(phrase: str, builder: GrammarBuilder) -> GrammarBuilder
        Add(builder: GrammarBuilder, phrase: str) -> GrammarBuilder
        Add(choices: Choices, builder: GrammarBuilder) -> GrammarBuilder
        Add(builder: GrammarBuilder, choices: Choices) -> GrammarBuilder
        Add(builder1: GrammarBuilder, builder2: GrammarBuilder) -> GrammarBuilder
        """
        ...

    def Append(self, *__args:str): # -> 
        """ Append(self: GrammarBuilder, phrase: str)Append(self: GrammarBuilder, phrase: str, subsetMatchingCriteria: SubsetMatchingMode)Append(self: GrammarBuilder, phrase: str, minRepeat: int, maxRepeat: int)Append(self: GrammarBuilder, builder: GrammarBuilder)Append(self: GrammarBuilder, alternateChoices: Choices)Append(self: GrammarBuilder, key: SemanticResultKey)Append(self: GrammarBuilder, value: SemanticResultValue)Append(self: GrammarBuilder, builder: GrammarBuilder, minRepeat: int, maxRepeat: int) """
        ...

    def AppendDictation(self, category:str = ...): # -> 
        """ AppendDictation(self: GrammarBuilder)AppendDictation(self: GrammarBuilder, category: str) """
        ...

    def AppendRuleReference(self, path:str, rule:str = ...): # -> 
        """ AppendRuleReference(self: GrammarBuilder, path: str)AppendRuleReference(self: GrammarBuilder, path: str, rule: str) """
        ...

    def AppendWildcard(self): # -> 
        """ AppendWildcard(self: GrammarBuilder) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(phrase: str, builder: GrammarBuilder) -> GrammarBuilder
        __radd__(choices: Choices, builder: GrammarBuilder) -> GrammarBuilder
        __radd__(builder1: GrammarBuilder, builder2: GrammarBuilder) -> GrammarBuilder
        """
        ...


class LoadGrammarCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Grammar(self) -> Grammar:
        """ Get: Grammar(self: LoadGrammarCompletedEventArgs) -> Grammar """
        ...



class RecognitionEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Result(self) -> RecognitionResult:
        """ Get: Result(self: RecognitionEventArgs) -> RecognitionResult """
        ...



class RecognizedPhrase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Confidence(self) -> Single:
        """ Get: Confidence(self: RecognizedPhrase) -> Single """
        ...

    @property
    def Grammar(self) -> Grammar:
        """ Get: Grammar(self: RecognizedPhrase) -> Grammar """
        ...

    @property
    def HomophoneGroupId(self) -> int:
        """ Get: HomophoneGroupId(self: RecognizedPhrase) -> int """
        ...

    @property
    def Homophones(self) -> ReadOnlyCollection:
        """ Get: Homophones(self: RecognizedPhrase) -> ReadOnlyCollection[RecognizedPhrase] """
        ...

    @property
    def ReplacementWordUnits(self) -> Collection:
        """ Get: ReplacementWordUnits(self: RecognizedPhrase) -> Collection[ReplacementText] """
        ...

    @property
    def Semantics(self) -> SemanticValue:
        """ Get: Semantics(self: RecognizedPhrase) -> SemanticValue """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: RecognizedPhrase) -> str """
        ...

    @property
    def Words(self) -> ReadOnlyCollection:
        """ Get: Words(self: RecognizedPhrase) -> ReadOnlyCollection[RecognizedWordUnit] """
        ...


    def ConstructSmlFromSemantics(self) -> IXPathNavigable:
        """ ConstructSmlFromSemantics(self: RecognizedPhrase) -> IXPathNavigable """
        ...


class RecognitionResult(RecognizedPhrase, ISerializable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Alternates(self) -> ReadOnlyCollection:
        """ Get: Alternates(self: RecognitionResult) -> ReadOnlyCollection[RecognizedPhrase] """
        ...

    @property
    def Audio(self) -> RecognizedAudio:
        """ Get: Audio(self: RecognitionResult) -> RecognizedAudio """
        ...


    def GetAudioForWordRange(self, firstWord:RecognizedWordUnit, lastWord:RecognizedWordUnit) -> RecognizedAudio:
        """ GetAudioForWordRange(self: RecognitionResult, firstWord: RecognizedWordUnit, lastWord: RecognizedWordUnit) -> RecognizedAudio """
        ...


class RecognizeCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AudioPosition(self) -> TimeSpan:
        """ Get: AudioPosition(self: RecognizeCompletedEventArgs) -> TimeSpan """
        ...

    @property
    def BabbleTimeout(self) -> bool:
        """ Get: BabbleTimeout(self: RecognizeCompletedEventArgs) -> bool """
        ...

    @property
    def InitialSilenceTimeout(self) -> bool:
        """ Get: InitialSilenceTimeout(self: RecognizeCompletedEventArgs) -> bool """
        ...

    @property
    def InputStreamEnded(self) -> bool:
        """ Get: InputStreamEnded(self: RecognizeCompletedEventArgs) -> bool """
        ...

    @property
    def Result(self) -> RecognitionResult:
        """ Get: Result(self: RecognizeCompletedEventArgs) -> RecognitionResult """
        ...



class RecognizedAudio: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AudioPosition(self) -> TimeSpan:
        """ Get: AudioPosition(self: RecognizedAudio) -> TimeSpan """
        ...

    @property
    def Duration(self) -> TimeSpan:
        """ Get: Duration(self: RecognizedAudio) -> TimeSpan """
        ...

    @property
    def Format(self) -> SpeechAudioFormatInfo:
        """ Get: Format(self: RecognizedAudio) -> SpeechAudioFormatInfo """
        ...

    @property
    def StartTime(self) -> DateTime:
        """ Get: StartTime(self: RecognizedAudio) -> DateTime """
        ...


    def GetRange(self, audioPosition:TimeSpan, duration:TimeSpan) -> RecognizedAudio:
        """ GetRange(self: RecognizedAudio, audioPosition: TimeSpan, duration: TimeSpan) -> RecognizedAudio """
        ...

    def WriteToAudioStream(self, outputStream:Stream): # -> 
        """ WriteToAudioStream(self: RecognizedAudio, outputStream: Stream) """
        ...

    def WriteToWaveStream(self, outputStream:Stream): # -> 
        """ WriteToWaveStream(self: RecognizedAudio, outputStream: Stream) """
        ...


class RecognizedWordUnit: # skipped bases: <type 'object'>, <type 'object'>
    """ RecognizedWordUnit(text: str, confidence: Single, pronunciation: str, lexicalForm: str, displayAttributes: DisplayAttributes, audioPosition: TimeSpan, audioDuration: TimeSpan) """
    @property
    def Confidence(self) -> Single:
        """ Get: Confidence(self: RecognizedWordUnit) -> Single """
        ...

    @property
    def DisplayAttributes(self) -> DisplayAttributes:
        """ Get: DisplayAttributes(self: RecognizedWordUnit) -> DisplayAttributes """
        ...

    @property
    def LexicalForm(self) -> str:
        """ Get: LexicalForm(self: RecognizedWordUnit) -> str """
        ...

    @property
    def Pronunciation(self) -> str:
        """ Get: Pronunciation(self: RecognizedWordUnit) -> str """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: RecognizedWordUnit) -> str """
        ...



class RecognizeMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RecognizeMode, values: Multiple (1), Single (0) """
    Multiple: RecognizeMode = ...
    Single: RecognizeMode = ...
    value__ = ...


class RecognizerInfo(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AdditionalInfo(self) -> IDictionary:
        """ Get: AdditionalInfo(self: RecognizerInfo) -> IDictionary[str, str] """
        ...

    @property
    def Culture(self) -> CultureInfo:
        """ Get: Culture(self: RecognizerInfo) -> CultureInfo """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: RecognizerInfo) -> str """
        ...

    @property
    def Id(self) -> str:
        """ Get: Id(self: RecognizerInfo) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: RecognizerInfo) -> str """
        ...

    @property
    def SupportedAudioFormats(self) -> ReadOnlyCollection:
        """ Get: SupportedAudioFormats(self: RecognizerInfo) -> ReadOnlyCollection[SpeechAudioFormatInfo] """
        ...



class RecognizerState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RecognizerState, values: Listening (1), Stopped (0) """
    Listening: RecognizerState = ...
    Stopped: RecognizerState = ...
    value__ = ...


class RecognizerUpdateReachedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AudioPosition(self) -> TimeSpan:
        """ Get: AudioPosition(self: RecognizerUpdateReachedEventArgs) -> TimeSpan """
        ...

    @property
    def UserToken(self) -> object:
        """ Get: UserToken(self: RecognizerUpdateReachedEventArgs) -> object """
        ...



class ReplacementText: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CountOfWords(self) -> int:
        """ Get: CountOfWords(self: ReplacementText) -> int """
        ...

    @property
    def DisplayAttributes(self) -> DisplayAttributes:
        """ Get: DisplayAttributes(self: ReplacementText) -> DisplayAttributes """
        ...

    @property
    def FirstWordIndex(self) -> int:
        """ Get: FirstWordIndex(self: ReplacementText) -> int """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: ReplacementText) -> str """
        ...



class SemanticResultKey: # skipped bases: <type 'object'>, <type 'object'>
    """
    SemanticResultKey(semanticResultKey: str, *phrases: Array[str])
    SemanticResultKey(semanticResultKey: str, *builders: Array[GrammarBuilder])
    """
    def ToGrammarBuilder(self) -> GrammarBuilder:
        """ ToGrammarBuilder(self: SemanticResultKey) -> GrammarBuilder """
        ...


class SemanticResultValue: # skipped bases: <type 'object'>, <type 'object'>
    """
    SemanticResultValue(value: object)
    SemanticResultValue(phrase: str, value: object)
    SemanticResultValue(builder: GrammarBuilder, value: object)
    """
    def ToGrammarBuilder(self) -> GrammarBuilder:
        """ ToGrammarBuilder(self: SemanticResultValue) -> GrammarBuilder """
        ...


class SemanticValue(IDictionary): # skipped bases: <type 'ICollection[KeyValuePair[str, SemanticValue]]'>, <type 'IEnumerable'>, <type 'IEnumerable[KeyValuePair[str, SemanticValue]]'>, <type 'object'>
    """
    SemanticValue(keyName: str, value: object, confidence: Single)
    SemanticValue(value: object)
    """
    @property
    def Confidence(self) -> Single:
        """ Get: Confidence(self: SemanticValue) -> Single """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: SemanticValue) -> int """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: SemanticValue) -> object """
        ...


    def Contains(self, item:KeyValuePair) -> bool:
        """ Contains(self: SemanticValue, item: KeyValuePair[str, SemanticValue]) -> bool """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: SemanticValue, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SemanticValue) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SpeechDetectedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AudioPosition(self) -> TimeSpan:
        """ Get: AudioPosition(self: SpeechDetectedEventArgs) -> TimeSpan """
        ...



class SpeechHypothesizedEventArgs(RecognitionEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    pass

class SpeechRecognitionEngine(IDisposable): # skipped bases: <type 'object'>
    """
    SpeechRecognitionEngine()
    SpeechRecognitionEngine(culture: CultureInfo)
    SpeechRecognitionEngine(recognizerId: str)
    SpeechRecognitionEngine(recognizerInfo: RecognizerInfo)
    """
    @property
    def AudioFormat(self) -> SpeechAudioFormatInfo:
        """ Get: AudioFormat(self: SpeechRecognitionEngine) -> SpeechAudioFormatInfo """
        ...

    @property
    def AudioLevel(self) -> int:
        """ Get: AudioLevel(self: SpeechRecognitionEngine) -> int """
        ...

    @property
    def AudioPosition(self) -> TimeSpan:
        """ Get: AudioPosition(self: SpeechRecognitionEngine) -> TimeSpan """
        ...

    @property
    def AudioState(self) -> AudioState:
        """ Get: AudioState(self: SpeechRecognitionEngine) -> AudioState """
        ...

    @property
    def BabbleTimeout(self) -> TimeSpan:
        """
        Get: BabbleTimeout(self: SpeechRecognitionEngine) -> TimeSpan
        Set: BabbleTimeout(self: SpeechRecognitionEngine) = value
        """
        ...

    @property
    def EndSilenceTimeout(self) -> TimeSpan:
        """
        Get: EndSilenceTimeout(self: SpeechRecognitionEngine) -> TimeSpan
        Set: EndSilenceTimeout(self: SpeechRecognitionEngine) = value
        """
        ...

    @property
    def EndSilenceTimeoutAmbiguous(self) -> TimeSpan:
        """
        Get: EndSilenceTimeoutAmbiguous(self: SpeechRecognitionEngine) -> TimeSpan
        Set: EndSilenceTimeoutAmbiguous(self: SpeechRecognitionEngine) = value
        """
        ...

    @property
    def Grammars(self) -> ReadOnlyCollection:
        """ Get: Grammars(self: SpeechRecognitionEngine) -> ReadOnlyCollection[Grammar] """
        ...

    @property
    def InitialSilenceTimeout(self) -> TimeSpan:
        """
        Get: InitialSilenceTimeout(self: SpeechRecognitionEngine) -> TimeSpan
        Set: InitialSilenceTimeout(self: SpeechRecognitionEngine) = value
        """
        ...

    @property
    def MaxAlternates(self) -> int:
        """
        Get: MaxAlternates(self: SpeechRecognitionEngine) -> int
        Set: MaxAlternates(self: SpeechRecognitionEngine) = value
        """
        ...

    @property
    def RecognizerAudioPosition(self) -> TimeSpan:
        """ Get: RecognizerAudioPosition(self: SpeechRecognitionEngine) -> TimeSpan """
        ...

    @property
    def RecognizerInfo(self) -> RecognizerInfo:
        """ Get: RecognizerInfo(self: SpeechRecognitionEngine) -> RecognizerInfo """
        ...


    def EmulateRecognize(self, *__args:str) -> RecognitionResult:
        """
        EmulateRecognize(self: SpeechRecognitionEngine, inputText: str) -> RecognitionResult
        EmulateRecognize(self: SpeechRecognitionEngine, inputText: str, compareOptions: CompareOptions) -> RecognitionResult
        EmulateRecognize(self: SpeechRecognitionEngine, wordUnits: Array[RecognizedWordUnit], compareOptions: CompareOptions) -> RecognitionResult
        """
        ...

    def EmulateRecognizeAsync(self, *__args:str): # -> 
        """ EmulateRecognizeAsync(self: SpeechRecognitionEngine, inputText: str)EmulateRecognizeAsync(self: SpeechRecognitionEngine, inputText: str, compareOptions: CompareOptions)EmulateRecognizeAsync(self: SpeechRecognitionEngine, wordUnits: Array[RecognizedWordUnit], compareOptions: CompareOptions) """
        ...

    @staticmethod
    def InstalledRecognizers() -> ReadOnlyCollection:
        """ InstalledRecognizers() -> ReadOnlyCollection[RecognizerInfo] """
        ...

    def LoadGrammar(self, grammar:Grammar): # -> 
        """ LoadGrammar(self: SpeechRecognitionEngine, grammar: Grammar) """
        ...

    def LoadGrammarAsync(self, grammar:Grammar): # -> 
        """ LoadGrammarAsync(self: SpeechRecognitionEngine, grammar: Grammar) """
        ...

    def QueryRecognizerSetting(self, settingName:str) -> object:
        """ QueryRecognizerSetting(self: SpeechRecognitionEngine, settingName: str) -> object """
        ...

    def Recognize(self, initialSilenceTimeout:TimeSpan = ...) -> RecognitionResult:
        """
        Recognize(self: SpeechRecognitionEngine) -> RecognitionResult
        Recognize(self: SpeechRecognitionEngine, initialSilenceTimeout: TimeSpan) -> RecognitionResult
        """
        ...

    def RecognizeAsync(self, mode:RecognizeMode = ...): # -> 
        """ RecognizeAsync(self: SpeechRecognitionEngine)RecognizeAsync(self: SpeechRecognitionEngine, mode: RecognizeMode) """
        ...

    def RecognizeAsyncCancel(self): # -> 
        """ RecognizeAsyncCancel(self: SpeechRecognitionEngine) """
        ...

    def RecognizeAsyncStop(self): # -> 
        """ RecognizeAsyncStop(self: SpeechRecognitionEngine) """
        ...

    def RequestRecognizerUpdate(self, userToken:object = ..., audioPositionAheadToRaiseUpdate:TimeSpan = ...): # -> 
        """ RequestRecognizerUpdate(self: SpeechRecognitionEngine)RequestRecognizerUpdate(self: SpeechRecognitionEngine, userToken: object)RequestRecognizerUpdate(self: SpeechRecognitionEngine, userToken: object, audioPositionAheadToRaiseUpdate: TimeSpan) """
        ...

    def SetInputToAudioStream(self, audioSource:Stream, audioFormat:SpeechAudioFormatInfo): # -> 
        """ SetInputToAudioStream(self: SpeechRecognitionEngine, audioSource: Stream, audioFormat: SpeechAudioFormatInfo) """
        ...

    def SetInputToDefaultAudioDevice(self): # -> 
        """ SetInputToDefaultAudioDevice(self: SpeechRecognitionEngine) """
        ...

    def SetInputToNull(self): # -> 
        """ SetInputToNull(self: SpeechRecognitionEngine) """
        ...

    def SetInputToWaveFile(self, path:str): # -> 
        """ SetInputToWaveFile(self: SpeechRecognitionEngine, path: str) """
        ...

    def SetInputToWaveStream(self, audioSource:Stream): # -> 
        """ SetInputToWaveStream(self: SpeechRecognitionEngine, audioSource: Stream) """
        ...

    def UnloadAllGrammars(self): # -> 
        """ UnloadAllGrammars(self: SpeechRecognitionEngine) """
        ...

    def UnloadGrammar(self, grammar:Grammar): # -> 
        """ UnloadGrammar(self: SpeechRecognitionEngine, grammar: Grammar) """
        ...

    def UpdateRecognizerSetting(self, settingName:str, updatedValue:str): # -> 
        """ UpdateRecognizerSetting(self: SpeechRecognitionEngine, settingName: str, updatedValue: str)UpdateRecognizerSetting(self: SpeechRecognitionEngine, settingName: str, updatedValue: int) """
        ...

    AudioLevelUpdated = ...
    AudioSignalProblemOccurred = ...
    AudioStateChanged = ...
    EmulateRecognizeCompleted = ...
    LoadGrammarCompleted = ...
    RecognizeCompleted = ...
    RecognizerUpdateReached = ...
    SpeechDetected = ...
    SpeechHypothesized = ...
    SpeechRecognitionRejected = ...
    SpeechRecognized = ...


class SpeechRecognitionRejectedEventArgs(RecognitionEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    pass

class SpeechRecognizedEventArgs(RecognitionEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    pass

class SpeechRecognizer(IDisposable): # skipped bases: <type 'object'>
    """ SpeechRecognizer() """
    @property
    def AudioFormat(self) -> SpeechAudioFormatInfo:
        """ Get: AudioFormat(self: SpeechRecognizer) -> SpeechAudioFormatInfo """
        ...

    @property
    def AudioLevel(self) -> int:
        """ Get: AudioLevel(self: SpeechRecognizer) -> int """
        ...

    @property
    def AudioPosition(self) -> TimeSpan:
        """ Get: AudioPosition(self: SpeechRecognizer) -> TimeSpan """
        ...

    @property
    def AudioState(self) -> AudioState:
        """ Get: AudioState(self: SpeechRecognizer) -> AudioState """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: SpeechRecognizer) -> bool
        Set: Enabled(self: SpeechRecognizer) = value
        """
        ...

    @property
    def Grammars(self) -> ReadOnlyCollection:
        """ Get: Grammars(self: SpeechRecognizer) -> ReadOnlyCollection[Grammar] """
        ...

    @property
    def MaxAlternates(self) -> int:
        """
        Get: MaxAlternates(self: SpeechRecognizer) -> int
        Set: MaxAlternates(self: SpeechRecognizer) = value
        """
        ...

    @property
    def PauseRecognizerOnRecognition(self) -> bool:
        """
        Get: PauseRecognizerOnRecognition(self: SpeechRecognizer) -> bool
        Set: PauseRecognizerOnRecognition(self: SpeechRecognizer) = value
        """
        ...

    @property
    def RecognizerAudioPosition(self) -> TimeSpan:
        """ Get: RecognizerAudioPosition(self: SpeechRecognizer) -> TimeSpan """
        ...

    @property
    def RecognizerInfo(self) -> RecognizerInfo:
        """ Get: RecognizerInfo(self: SpeechRecognizer) -> RecognizerInfo """
        ...

    @property
    def State(self) -> RecognizerState:
        """ Get: State(self: SpeechRecognizer) -> RecognizerState """
        ...


    def EmulateRecognize(self, *__args:str) -> RecognitionResult:
        """
        EmulateRecognize(self: SpeechRecognizer, inputText: str) -> RecognitionResult
        EmulateRecognize(self: SpeechRecognizer, inputText: str, compareOptions: CompareOptions) -> RecognitionResult
        EmulateRecognize(self: SpeechRecognizer, wordUnits: Array[RecognizedWordUnit], compareOptions: CompareOptions) -> RecognitionResult
        """
        ...

    def EmulateRecognizeAsync(self, *__args:str): # -> 
        """ EmulateRecognizeAsync(self: SpeechRecognizer, inputText: str)EmulateRecognizeAsync(self: SpeechRecognizer, inputText: str, compareOptions: CompareOptions)EmulateRecognizeAsync(self: SpeechRecognizer, wordUnits: Array[RecognizedWordUnit], compareOptions: CompareOptions) """
        ...

    def LoadGrammar(self, grammar:Grammar): # -> 
        """ LoadGrammar(self: SpeechRecognizer, grammar: Grammar) """
        ...

    def LoadGrammarAsync(self, grammar:Grammar): # -> 
        """ LoadGrammarAsync(self: SpeechRecognizer, grammar: Grammar) """
        ...

    def RequestRecognizerUpdate(self, userToken:object = ..., audioPositionAheadToRaiseUpdate:TimeSpan = ...): # -> 
        """ RequestRecognizerUpdate(self: SpeechRecognizer)RequestRecognizerUpdate(self: SpeechRecognizer, userToken: object)RequestRecognizerUpdate(self: SpeechRecognizer, userToken: object, audioPositionAheadToRaiseUpdate: TimeSpan) """
        ...

    def UnloadAllGrammars(self): # -> 
        """ UnloadAllGrammars(self: SpeechRecognizer) """
        ...

    def UnloadGrammar(self, grammar:Grammar): # -> 
        """ UnloadGrammar(self: SpeechRecognizer, grammar: Grammar) """
        ...

    AudioLevelUpdated = ...
    AudioSignalProblemOccurred = ...
    AudioStateChanged = ...
    EmulateRecognizeCompleted = ...
    LoadGrammarCompleted = ...
    RecognizerUpdateReached = ...
    SpeechDetected = ...
    SpeechHypothesized = ...
    SpeechRecognitionRejected = ...
    SpeechRecognized = ...
    StateChanged = ...


class SpeechUI: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def SendTextFeedback(result:RecognitionResult, feedback:str, isSuccessfulAction:bool) -> bool:
        """ SendTextFeedback(result: RecognitionResult, feedback: str, isSuccessfulAction: bool) -> bool """
        ...


class StateChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RecognizerState(self) -> RecognizerState:
        """ Get: RecognizerState(self: StateChangedEventArgs) -> RecognizerState """
        ...



class SubsetMatchingMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SubsetMatchingMode, values: OrderedSubset (1), OrderedSubsetContentRequired (3), Subsequence (0), SubsequenceContentRequired (2) """
    OrderedSubset: SubsetMatchingMode = ...
    OrderedSubsetContentRequired: SubsetMatchingMode = ...
    Subsequence: SubsetMatchingMode = ...
    SubsequenceContentRequired: SubsetMatchingMode = ...
    value__ = ...


# variables with complex values

