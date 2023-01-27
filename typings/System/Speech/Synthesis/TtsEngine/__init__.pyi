# encoding: utf-8
# module System.Speech.Synthesis.TtsEngine calls itself TtsEngine
# from System.Speech, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, IEquatable, Int16, IntPtr, Single, Uri

from System.IO import Stream

"""The following names are not found in the module: field#
"""

# no functions
# classes

class ContourPoint(IEquatable): # skipped bases: <type 'object'>
    """ ContourPoint(start: Single, change: Single, changeType: ContourPointChangeType) """
    @property
    def Change(self) -> Single:
        """ Get: Change(self: ContourPoint) -> Single """
        ...

    @property
    def ChangeType(self) -> ContourPointChangeType:
        """ Get: ChangeType(self: ContourPoint) -> ContourPointChangeType """
        ...

    @property
    def Start(self) -> Single:
        """ Get: Start(self: ContourPoint) -> Single """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: ContourPoint) -> int """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ContourPointChangeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ContourPointChangeType, values: Hz (0), Percentage (1) """
    Hz: ContourPointChangeType = ...
    Percentage: ContourPointChangeType = ...
    value__ = ...


class EmphasisBreak(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EmphasisBreak, values: Default (-7), ExtraStrong (-6), ExtraWeak (-2), Medium (-4), None (-1), Strong (-5), Weak (-3) """
    Default: EmphasisBreak = ...
    ExtraStrong: EmphasisBreak = ...
    ExtraWeak: EmphasisBreak = ...
    Medium: EmphasisBreak = ...
    Strong: EmphasisBreak = ...
    value__ = ...
    Weak: EmphasisBreak = ...


class EmphasisWord(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EmphasisWord, values: Default (0), Moderate (2), None (3), Reduced (4), Strong (1) """
    Default: EmphasisWord = ...
    Moderate: EmphasisWord = ...
    Reduced: EmphasisWord = ...
    Strong: EmphasisWord = ...
    value__ = ...


class EventParameterType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EventParameterType, values: Object (2), Pointer (3), String (4), Token (1), Undefined (0) """
    Object: EventParameterType = ...
    Pointer: EventParameterType = ...
    String: EventParameterType = ...
    Token: EventParameterType = ...
    Undefined: EventParameterType = ...
    value__ = ...


class FragmentState(IEquatable): # skipped bases: <type 'object'>
    """ FragmentState(action: TtsEngineAction, langId: int, emphasis: int, duration: int, sayAs: SayAs, prosody: Prosody, phonemes: Array[Char]) """
    @property
    def Action(self) -> TtsEngineAction:
        """ Get: Action(self: FragmentState) -> TtsEngineAction """
        ...

    @property
    def Duration(self) -> int:
        """ Get: Duration(self: FragmentState) -> int """
        ...

    @property
    def Emphasis(self) -> int:
        """ Get: Emphasis(self: FragmentState) -> int """
        ...

    @property
    def LangId(self) -> int:
        """ Get: LangId(self: FragmentState) -> int """
        ...

    @property
    def Phoneme(self) -> Array:
        """ Get: Phoneme(self: FragmentState) -> Array[Char] """
        ...

    @property
    def Prosody(self) -> Prosody:
        """ Get: Prosody(self: FragmentState) -> Prosody """
        ...

    @property
    def SayAs(self) -> SayAs:
        """ Get: SayAs(self: FragmentState) -> SayAs """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: FragmentState) -> int """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ITtsEngineSite: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Actions(self) -> int:
        """ Get: Actions(self: ITtsEngineSite) -> int """
        ...

    @property
    def EventInterest(self) -> int:
        """ Get: EventInterest(self: ITtsEngineSite) -> int """
        ...

    @property
    def Rate(self) -> int:
        """ Get: Rate(self: ITtsEngineSite) -> int """
        ...

    @property
    def Volume(self) -> int:
        """ Get: Volume(self: ITtsEngineSite) -> int """
        ...


    def AddEvents(self, events:Array, count:int): # -> 
        """ AddEvents(self: ITtsEngineSite, events: Array[SpeechEventInfo], count: int) """
        ...

    def CompleteSkip(self, skipped:int): # -> 
        """ CompleteSkip(self: ITtsEngineSite, skipped: int) """
        ...

    def GetSkipInfo(self) -> SkipInfo:
        """ GetSkipInfo(self: ITtsEngineSite) -> SkipInfo """
        ...

    def LoadResource(self, uri:Uri, mediaType:str) -> Stream:
        """ LoadResource(self: ITtsEngineSite, uri: Uri, mediaType: str) -> Stream """
        ...

    def Write(self, data:IntPtr, count:int) -> int:
        """ Write(self: ITtsEngineSite, data: IntPtr, count: int) -> int """
        ...


class Prosody: # skipped bases: <type 'object'>, <type 'object'>
    """ Prosody() """
    @property
    def Duration(self) -> int:
        """
        Get: Duration(self: Prosody) -> int
        Set: Duration(self: Prosody) = value
        """
        ...

    @property
    def Pitch(self) -> ProsodyNumber:
        """
        Get: Pitch(self: Prosody) -> ProsodyNumber
        Set: Pitch(self: Prosody) = value
        """
        ...

    @property
    def Range(self) -> ProsodyNumber:
        """
        Get: Range(self: Prosody) -> ProsodyNumber
        Set: Range(self: Prosody) = value
        """
        ...

    @property
    def Rate(self) -> ProsodyNumber:
        """
        Get: Rate(self: Prosody) -> ProsodyNumber
        Set: Rate(self: Prosody) = value
        """
        ...

    @property
    def Volume(self) -> ProsodyNumber:
        """
        Get: Volume(self: Prosody) -> ProsodyNumber
        Set: Volume(self: Prosody) = value
        """
        ...


    def GetContourPoints(self) -> Array:
        """ GetContourPoints(self: Prosody) -> Array[ContourPoint] """
        ...

    def SetContourPoints(self, points:Array): # -> 
        """ SetContourPoints(self: Prosody, points: Array[ContourPoint]) """
        ...


class ProsodyNumber(IEquatable): # skipped bases: <type 'object'>
    """
    ProsodyNumber(ssmlAttributeId: int)
    ProsodyNumber(number: Single)
    """
    @property
    def IsNumberPercent(self) -> bool:
        """ Get: IsNumberPercent(self: ProsodyNumber) -> bool """
        ...

    @property
    def Number(self) -> Single:
        """ Get: Number(self: ProsodyNumber) -> Single """
        ...

    @property
    def SsmlAttributeId(self) -> int:
        """ Get: SsmlAttributeId(self: ProsodyNumber) -> int """
        ...

    @property
    def Unit(self) -> ProsodyUnit:
        """ Get: Unit(self: ProsodyNumber) -> ProsodyUnit """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: ProsodyNumber) -> int """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    AbsoluteNumber: int = ...


class ProsodyPitch(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProsodyPitch, values: Default (0), ExtraHigh (5), ExtraLow (1), High (4), Low (2), Medium (3) """
    Default: ProsodyPitch = ...
    ExtraHigh: ProsodyPitch = ...
    ExtraLow: ProsodyPitch = ...
    High: ProsodyPitch = ...
    Low: ProsodyPitch = ...
    Medium: ProsodyPitch = ...
    value__ = ...


class ProsodyRange(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProsodyRange, values: Default (0), ExtraHigh (5), ExtraLow (1), High (4), Low (2), Medium (3) """
    Default: ProsodyRange = ...
    ExtraHigh: ProsodyRange = ...
    ExtraLow: ProsodyRange = ...
    High: ProsodyRange = ...
    Low: ProsodyRange = ...
    Medium: ProsodyRange = ...
    value__ = ...


class ProsodyRate(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProsodyRate, values: Default (0), ExtraFast (5), ExtraSlow (1), Fast (4), Medium (3), Slow (2) """
    Default: ProsodyRate = ...
    ExtraFast: ProsodyRate = ...
    ExtraSlow: ProsodyRate = ...
    Fast: ProsodyRate = ...
    Medium: ProsodyRate = ...
    Slow: ProsodyRate = ...
    value__ = ...


class ProsodyUnit(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProsodyUnit, values: Default (0), Hz (1), Semitone (2) """
    Default: ProsodyUnit = ...
    Hz: ProsodyUnit = ...
    Semitone: ProsodyUnit = ...
    value__ = ...


class ProsodyVolume(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProsodyVolume, values: Default (-1), ExtraLoud (-7), ExtraSoft (-3), Loud (-6), Medium (-5), Silent (-2), Soft (-4) """
    Default: ProsodyVolume = ...
    ExtraLoud: ProsodyVolume = ...
    ExtraSoft: ProsodyVolume = ...
    Loud: ProsodyVolume = ...
    Medium: ProsodyVolume = ...
    Silent: ProsodyVolume = ...
    Soft: ProsodyVolume = ...
    value__ = ...


class SayAs: # skipped bases: <type 'object'>, <type 'object'>
    """ SayAs() """
    @property
    def Detail(self) -> str:
        """
        Get: Detail(self: SayAs) -> str
        Set: Detail(self: SayAs) = value
        """
        ...

    @property
    def Format(self) -> str:
        """
        Get: Format(self: SayAs) -> str
        Set: Format(self: SayAs) = value
        """
        ...

    @property
    def InterpretAs(self) -> str:
        """
        Get: InterpretAs(self: SayAs) -> str
        Set: InterpretAs(self: SayAs) = value
        """
        ...



class SkipInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ SkipInfo() """
    @property
    def Count(self) -> int:
        """
        Get: Count(self: SkipInfo) -> int
        Set: Count(self: SkipInfo) = value
        """
        ...

    @property
    def Type(self) -> int:
        """
        Get: Type(self: SkipInfo) -> int
        Set: Type(self: SkipInfo) = value
        """
        ...



class SpeakOutputFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SpeakOutputFormat, values: Text (1), WaveFormat (0) """
    Text: SpeakOutputFormat = ...
    value__ = ...
    WaveFormat: SpeakOutputFormat = ...


class SpeechEventInfo(IEquatable): # skipped bases: <type 'object'>
    """ SpeechEventInfo(eventId: Int16, parameterType: Int16, param1: int, param2: IntPtr) """
    @property
    def EventId(self) -> Int16:
        """ Get: EventId(self: SpeechEventInfo) -> Int16 """
        ...

    @property
    def Param1(self) -> int:
        """ Get: Param1(self: SpeechEventInfo) -> int """
        ...

    @property
    def Param2(self) -> IntPtr:
        """ Get: Param2(self: SpeechEventInfo) -> IntPtr """
        ...

    @property
    def ParameterType(self) -> Int16:
        """ Get: ParameterType(self: SpeechEventInfo) -> Int16 """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: SpeechEventInfo) -> int """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TextFragment: # skipped bases: <type 'object'>, <type 'object'>
    """ TextFragment() """
    @property
    def State(self) -> FragmentState:
        """
        Get: State(self: TextFragment) -> FragmentState
        Set: State(self: TextFragment) = value
        """
        ...

    @property
    def TextLength(self) -> int:
        """
        Get: TextLength(self: TextFragment) -> int
        Set: TextLength(self: TextFragment) = value
        """
        ...

    @property
    def TextOffset(self) -> int:
        """
        Get: TextOffset(self: TextFragment) -> int
        Set: TextOffset(self: TextFragment) = value
        """
        ...

    @property
    def TextToSpeak(self) -> str:
        """
        Get: TextToSpeak(self: TextFragment) -> str
        Set: TextToSpeak(self: TextFragment) = value
        """
        ...



class TtsEngineAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TtsEngineAction, values: Bookmark (3), ParseUnknownTag (7), Pronounce (2), Silence (1), Speak (0), SpellOut (4), StartParagraph (6), StartSentence (5) """
    Bookmark: TtsEngineAction = ...
    ParseUnknownTag: TtsEngineAction = ...
    Pronounce: TtsEngineAction = ...
    Silence: TtsEngineAction = ...
    Speak: TtsEngineAction = ...
    SpellOut: TtsEngineAction = ...
    StartParagraph: TtsEngineAction = ...
    StartSentence: TtsEngineAction = ...
    value__ = ...


class TtsEngineSsml: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def AddLexicon(self, uri:Uri, mediaType:str, site:ITtsEngineSite): # -> 
        """ AddLexicon(self: TtsEngineSsml, uri: Uri, mediaType: str, site: ITtsEngineSite) """
        ...

    def GetOutputFormat(self, speakOutputFormat:SpeakOutputFormat, targetWaveFormat:IntPtr) -> IntPtr:
        """ GetOutputFormat(self: TtsEngineSsml, speakOutputFormat: SpeakOutputFormat, targetWaveFormat: IntPtr) -> IntPtr """
        ...

    def RemoveLexicon(self, uri:Uri, site:ITtsEngineSite): # -> 
        """ RemoveLexicon(self: TtsEngineSsml, uri: Uri, site: ITtsEngineSite) """
        ...

    def Speak(self, fragment:Array, waveHeader:IntPtr, site:ITtsEngineSite): # -> 
        """ Speak(self: TtsEngineSsml, fragment: Array[TextFragment], waveHeader: IntPtr, site: ITtsEngineSite) """
        ...


class TtsEventId(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TtsEventId, values: AudioLevel (9), Bookmark (4), EndInputStream (2), Phoneme (6), SentenceBoundary (7), StartInputStream (1), Viseme (8), VoiceChange (3), WordBoundary (5) """
    AudioLevel: TtsEventId = ...
    Bookmark: TtsEventId = ...
    EndInputStream: TtsEventId = ...
    Phoneme: TtsEventId = ...
    SentenceBoundary: TtsEventId = ...
    StartInputStream: TtsEventId = ...
    value__ = ...
    Viseme: TtsEventId = ...
    VoiceChange: TtsEventId = ...
    WordBoundary: TtsEventId = ...


