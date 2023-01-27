# encoding: utf-8
# module System.Speech.Synthesis calls itself Synthesis
# from System.Speech, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum, EventArgs, IDisposable, TimeSpan, Uri

from System.Collections import IDictionary

from System.Collections.ObjectModel import ReadOnlyCollection

from System.ComponentModel import AsyncCompletedEventArgs

from System.Globalization import CultureInfo

from System.IO import Stream

from System.Speech.AudioFormat import SpeechAudioFormatInfo

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class PromptEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Prompt(self) -> Prompt:
        """ Get: Prompt(self: PromptEventArgs) -> Prompt """
        ...



class BookmarkReachedEventArgs(PromptEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AudioPosition(self) -> TimeSpan:
        """ Get: AudioPosition(self: BookmarkReachedEventArgs) -> TimeSpan """
        ...

    @property
    def Bookmark(self) -> str:
        """ Get: Bookmark(self: BookmarkReachedEventArgs) -> str """
        ...



class Prompt: # skipped bases: <type 'object'>, <type 'object'>
    """
    Prompt(textToSpeak: str)
    Prompt(promptBuilder: PromptBuilder)
    Prompt(textToSpeak: str, media: SynthesisTextFormat)
    """
    @property
    def IsCompleted(self) -> bool:
        """ Get: IsCompleted(self: Prompt) -> bool """
        ...



class FilePrompt(Prompt): # skipped bases: <type 'object'>
    """
    FilePrompt(path: str, media: SynthesisMediaType)
    FilePrompt(promptFile: Uri, media: SynthesisMediaType)
    """
    pass

class InstalledVoice: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: InstalledVoice) -> bool
        Set: Enabled(self: InstalledVoice) = value
        """
        ...

    @property
    def VoiceInfo(self) -> VoiceInfo:
        """ Get: VoiceInfo(self: InstalledVoice) -> VoiceInfo """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: InstalledVoice, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: InstalledVoice) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PhonemeReachedEventArgs(PromptEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AudioPosition(self) -> TimeSpan:
        """ Get: AudioPosition(self: PhonemeReachedEventArgs) -> TimeSpan """
        ...

    @property
    def Duration(self) -> TimeSpan:
        """ Get: Duration(self: PhonemeReachedEventArgs) -> TimeSpan """
        ...

    @property
    def Emphasis(self) -> SynthesizerEmphasis:
        """ Get: Emphasis(self: PhonemeReachedEventArgs) -> SynthesizerEmphasis """
        ...

    @property
    def NextPhoneme(self) -> str:
        """ Get: NextPhoneme(self: PhonemeReachedEventArgs) -> str """
        ...

    @property
    def Phoneme(self) -> str:
        """ Get: Phoneme(self: PhonemeReachedEventArgs) -> str """
        ...



class PromptBreak(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PromptBreak, values: ExtraLarge (5), ExtraSmall (1), Large (4), Medium (3), None (0), Small (2) """
    ExtraLarge: PromptBreak = ...
    ExtraSmall: PromptBreak = ...
    Large: PromptBreak = ...
    Medium: PromptBreak = ...
    Small: PromptBreak = ...
    value__ = ...


class PromptBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """
    PromptBuilder()
    PromptBuilder(culture: CultureInfo)
    """
    @property
    def Culture(self) -> CultureInfo:
        """
        Get: Culture(self: PromptBuilder) -> CultureInfo
        Set: Culture(self: PromptBuilder) = value
        """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: PromptBuilder) -> bool """
        ...


    def AppendAudio(self, *__args:str): # -> 
        """ AppendAudio(self: PromptBuilder, path: str)AppendAudio(self: PromptBuilder, audioFile: Uri)AppendAudio(self: PromptBuilder, audioFile: Uri, alternateText: str) """
        ...

    def AppendBookmark(self, bookmarkName:str): # -> 
        """ AppendBookmark(self: PromptBuilder, bookmarkName: str) """
        ...

    def AppendBreak(self, *__args:PromptBreak): # -> 
        """ AppendBreak(self: PromptBuilder)AppendBreak(self: PromptBuilder, strength: PromptBreak)AppendBreak(self: PromptBuilder, duration: TimeSpan) """
        ...

    def AppendPromptBuilder(self, promptBuilder:PromptBuilder): # -> 
        """ AppendPromptBuilder(self: PromptBuilder, promptBuilder: PromptBuilder) """
        ...

    def AppendSsml(self, *__args:str): # -> 
        """ AppendSsml(self: PromptBuilder, path: str)AppendSsml(self: PromptBuilder, ssmlFile: Uri)AppendSsml(self: PromptBuilder, ssmlFile: XmlReader) """
        ...

    def AppendSsmlMarkup(self, ssmlMarkup:str): # -> 
        """ AppendSsmlMarkup(self: PromptBuilder, ssmlMarkup: str) """
        ...

    def AppendText(self, textToSpeak:str, *__args:PromptRate): # -> 
        """ AppendText(self: PromptBuilder, textToSpeak: str)AppendText(self: PromptBuilder, textToSpeak: str, rate: PromptRate)AppendText(self: PromptBuilder, textToSpeak: str, volume: PromptVolume)AppendText(self: PromptBuilder, textToSpeak: str, emphasis: PromptEmphasis) """
        ...

    def AppendTextWithAlias(self, textToSpeak:str, substitute:str): # -> 
        """ AppendTextWithAlias(self: PromptBuilder, textToSpeak: str, substitute: str) """
        ...

    def AppendTextWithHint(self, textToSpeak:str, sayAs:SayAs): # -> 
        """ AppendTextWithHint(self: PromptBuilder, textToSpeak: str, sayAs: SayAs)AppendTextWithHint(self: PromptBuilder, textToSpeak: str, sayAs: str) """
        ...

    def AppendTextWithPronunciation(self, textToSpeak:str, pronunciation:str): # -> 
        """ AppendTextWithPronunciation(self: PromptBuilder, textToSpeak: str, pronunciation: str) """
        ...

    def ClearContent(self): # -> 
        """ ClearContent(self: PromptBuilder) """
        ...

    def EndParagraph(self): # -> 
        """ EndParagraph(self: PromptBuilder) """
        ...

    def EndSentence(self): # -> 
        """ EndSentence(self: PromptBuilder) """
        ...

    def EndStyle(self): # -> 
        """ EndStyle(self: PromptBuilder) """
        ...

    def EndVoice(self): # -> 
        """ EndVoice(self: PromptBuilder) """
        ...

    def StartParagraph(self, culture:CultureInfo = ...): # -> 
        """ StartParagraph(self: PromptBuilder)StartParagraph(self: PromptBuilder, culture: CultureInfo) """
        ...

    def StartSentence(self, culture:CultureInfo = ...): # -> 
        """ StartSentence(self: PromptBuilder)StartSentence(self: PromptBuilder, culture: CultureInfo) """
        ...

    def StartStyle(self, style:PromptStyle): # -> 
        """ StartStyle(self: PromptBuilder, style: PromptStyle) """
        ...

    def StartVoice(self, *__args:VoiceInfo): # -> 
        """ StartVoice(self: PromptBuilder, voice: VoiceInfo)StartVoice(self: PromptBuilder, name: str)StartVoice(self: PromptBuilder, gender: VoiceGender)StartVoice(self: PromptBuilder, gender: VoiceGender, age: VoiceAge)StartVoice(self: PromptBuilder, gender: VoiceGender, age: VoiceAge, voiceAlternate: int)StartVoice(self: PromptBuilder, culture: CultureInfo) """
        ...

    def ToXml(self) -> str:
        """ ToXml(self: PromptBuilder) -> str """
        ...


class PromptEmphasis(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PromptEmphasis, values: Moderate (2), None (3), NotSet (0), Reduced (4), Strong (1) """
    Moderate: PromptEmphasis = ...
    NotSet: PromptEmphasis = ...
    Reduced: PromptEmphasis = ...
    Strong: PromptEmphasis = ...
    value__ = ...


class PromptRate(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PromptRate, values: ExtraFast (1), ExtraSlow (5), Fast (2), Medium (3), NotSet (0), Slow (4) """
    ExtraFast: PromptRate = ...
    ExtraSlow: PromptRate = ...
    Fast: PromptRate = ...
    Medium: PromptRate = ...
    NotSet: PromptRate = ...
    Slow: PromptRate = ...
    value__ = ...


class PromptStyle: # skipped bases: <type 'object'>, <type 'object'>
    """
    PromptStyle()
    PromptStyle(rate: PromptRate)
    PromptStyle(volume: PromptVolume)
    PromptStyle(emphasis: PromptEmphasis)
    """
    @property
    def Emphasis(self) -> PromptEmphasis:
        """
        Get: Emphasis(self: PromptStyle) -> PromptEmphasis
        Set: Emphasis(self: PromptStyle) = value
        """
        ...

    @property
    def Rate(self) -> PromptRate:
        """
        Get: Rate(self: PromptStyle) -> PromptRate
        Set: Rate(self: PromptStyle) = value
        """
        ...

    @property
    def Volume(self) -> PromptVolume:
        """
        Get: Volume(self: PromptStyle) -> PromptVolume
        Set: Volume(self: PromptStyle) = value
        """
        ...



class PromptVolume(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PromptVolume, values: Default (7), ExtraLoud (6), ExtraSoft (2), Loud (5), Medium (4), NotSet (0), Silent (1), Soft (3) """
    Default: PromptVolume = ...
    ExtraLoud: PromptVolume = ...
    ExtraSoft: PromptVolume = ...
    Loud: PromptVolume = ...
    Medium: PromptVolume = ...
    NotSet: PromptVolume = ...
    Silent: PromptVolume = ...
    Soft: PromptVolume = ...
    value__ = ...


class SayAs(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SayAs, values: Date (3), Day (13), DayMonth (10), DayMonthYear (4), Month (12), MonthDay (9), MonthDayYear (5), MonthYear (8), NumberCardinal (2), NumberOrdinal (1), SpellOut (0), Telephone (17), Text (18), Time (14), Time12 (16), Time24 (15), Year (11), YearMonth (7), YearMonthDay (6) """
    Date: SayAs = ...
    Day: SayAs = ...
    DayMonth: SayAs = ...
    DayMonthYear: SayAs = ...
    Month: SayAs = ...
    MonthDay: SayAs = ...
    MonthDayYear: SayAs = ...
    MonthYear: SayAs = ...
    NumberCardinal: SayAs = ...
    NumberOrdinal: SayAs = ...
    SpellOut: SayAs = ...
    Telephone: SayAs = ...
    Text: SayAs = ...
    Time: SayAs = ...
    Time12: SayAs = ...
    Time24: SayAs = ...
    value__ = ...
    Year: SayAs = ...
    YearMonth: SayAs = ...
    YearMonthDay: SayAs = ...


class SpeakCompletedEventArgs(PromptEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    pass

class SpeakProgressEventArgs(PromptEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AudioPosition(self) -> TimeSpan:
        """ Get: AudioPosition(self: SpeakProgressEventArgs) -> TimeSpan """
        ...

    @property
    def CharacterCount(self) -> int:
        """ Get: CharacterCount(self: SpeakProgressEventArgs) -> int """
        ...

    @property
    def CharacterPosition(self) -> int:
        """ Get: CharacterPosition(self: SpeakProgressEventArgs) -> int """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: SpeakProgressEventArgs) -> str """
        ...



class SpeakStartedEventArgs(PromptEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    pass

class SpeechSynthesizer(IDisposable): # skipped bases: <type 'object'>
    """ SpeechSynthesizer() """
    @property
    def Rate(self) -> int:
        """
        Get: Rate(self: SpeechSynthesizer) -> int
        Set: Rate(self: SpeechSynthesizer) = value
        """
        ...

    @property
    def State(self) -> SynthesizerState:
        """ Get: State(self: SpeechSynthesizer) -> SynthesizerState """
        ...

    @property
    def Voice(self) -> VoiceInfo:
        """ Get: Voice(self: SpeechSynthesizer) -> VoiceInfo """
        ...

    @property
    def Volume(self) -> int:
        """
        Get: Volume(self: SpeechSynthesizer) -> int
        Set: Volume(self: SpeechSynthesizer) = value
        """
        ...


    def AddLexicon(self, uri:Uri, mediaType:str): # -> 
        """ AddLexicon(self: SpeechSynthesizer, uri: Uri, mediaType: str) """
        ...

    def GetCurrentlySpokenPrompt(self) -> Prompt:
        """ GetCurrentlySpokenPrompt(self: SpeechSynthesizer) -> Prompt """
        ...

    def GetInstalledVoices(self, culture:CultureInfo = ...) -> ReadOnlyCollection:
        """
        GetInstalledVoices(self: SpeechSynthesizer) -> ReadOnlyCollection[InstalledVoice]
        GetInstalledVoices(self: SpeechSynthesizer, culture: CultureInfo) -> ReadOnlyCollection[InstalledVoice]
        """
        ...

    def Pause(self): # -> 
        """ Pause(self: SpeechSynthesizer) """
        ...

    def RemoveLexicon(self, uri:Uri): # -> 
        """ RemoveLexicon(self: SpeechSynthesizer, uri: Uri) """
        ...

    def Resume(self): # -> 
        """ Resume(self: SpeechSynthesizer) """
        ...

    def SelectVoice(self, name:str): # -> 
        """ SelectVoice(self: SpeechSynthesizer, name: str) """
        ...

    def SelectVoiceByHints(self, gender:VoiceGender, age:VoiceAge = ..., voiceAlternate:int = ..., culture:CultureInfo = ...): # -> 
        """ SelectVoiceByHints(self: SpeechSynthesizer, gender: VoiceGender)SelectVoiceByHints(self: SpeechSynthesizer, gender: VoiceGender, age: VoiceAge)SelectVoiceByHints(self: SpeechSynthesizer, gender: VoiceGender, age: VoiceAge, voiceAlternate: int)SelectVoiceByHints(self: SpeechSynthesizer, gender: VoiceGender, age: VoiceAge, voiceAlternate: int, culture: CultureInfo) """
        ...

    def SetOutputToAudioStream(self, audioDestination:Stream, formatInfo:SpeechAudioFormatInfo): # -> 
        """ SetOutputToAudioStream(self: SpeechSynthesizer, audioDestination: Stream, formatInfo: SpeechAudioFormatInfo) """
        ...

    def SetOutputToDefaultAudioDevice(self): # -> 
        """ SetOutputToDefaultAudioDevice(self: SpeechSynthesizer) """
        ...

    def SetOutputToNull(self): # -> 
        """ SetOutputToNull(self: SpeechSynthesizer) """
        ...

    def SetOutputToWaveFile(self, path:str, formatInfo:SpeechAudioFormatInfo = ...): # -> 
        """ SetOutputToWaveFile(self: SpeechSynthesizer, path: str)SetOutputToWaveFile(self: SpeechSynthesizer, path: str, formatInfo: SpeechAudioFormatInfo) """
        ...

    def SetOutputToWaveStream(self, audioDestination:Stream): # -> 
        """ SetOutputToWaveStream(self: SpeechSynthesizer, audioDestination: Stream) """
        ...

    def Speak(self, *__args:str): # -> 
        """ Speak(self: SpeechSynthesizer, textToSpeak: str)Speak(self: SpeechSynthesizer, prompt: Prompt)Speak(self: SpeechSynthesizer, promptBuilder: PromptBuilder) """
        ...

    def SpeakAsync(self, *__args:str) -> Prompt:
        """
        SpeakAsync(self: SpeechSynthesizer, textToSpeak: str) -> Prompt
        SpeakAsync(self: SpeechSynthesizer, prompt: Prompt)SpeakAsync(self: SpeechSynthesizer, promptBuilder: PromptBuilder) -> Prompt
        """
        ...

    def SpeakAsyncCancel(self, prompt:Prompt): # -> 
        """ SpeakAsyncCancel(self: SpeechSynthesizer, prompt: Prompt) """
        ...

    def SpeakAsyncCancelAll(self): # -> 
        """ SpeakAsyncCancelAll(self: SpeechSynthesizer) """
        ...

    def SpeakSsml(self, textToSpeak:str): # -> 
        """ SpeakSsml(self: SpeechSynthesizer, textToSpeak: str) """
        ...

    def SpeakSsmlAsync(self, textToSpeak:str) -> Prompt:
        """ SpeakSsmlAsync(self: SpeechSynthesizer, textToSpeak: str) -> Prompt """
        ...

    BookmarkReached = ...
    PhonemeReached = ...
    SpeakCompleted = ...
    SpeakProgress = ...
    SpeakStarted = ...
    StateChanged = ...
    VisemeReached = ...
    VoiceChange = ...


class StateChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def PreviousState(self) -> SynthesizerState:
        """ Get: PreviousState(self: StateChangedEventArgs) -> SynthesizerState """
        ...

    @property
    def State(self) -> SynthesizerState:
        """ Get: State(self: StateChangedEventArgs) -> SynthesizerState """
        ...



class SynthesisMediaType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SynthesisMediaType, values: Ssml (1), Text (0), WaveAudio (2) """
    Ssml: SynthesisMediaType = ...
    Text: SynthesisMediaType = ...
    value__ = ...
    WaveAudio: SynthesisMediaType = ...


class SynthesisTextFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SynthesisTextFormat, values: Ssml (1), Text (0) """
    Ssml: SynthesisTextFormat = ...
    Text: SynthesisTextFormat = ...
    value__ = ...


class SynthesizerEmphasis(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SynthesizerEmphasis, values: Emphasized (2), Stressed (1) """
    Emphasized: SynthesizerEmphasis = ...
    Stressed: SynthesizerEmphasis = ...
    value__ = ...


class SynthesizerState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SynthesizerState, values: Paused (2), Ready (0), Speaking (1) """
    Paused: SynthesizerState = ...
    Ready: SynthesizerState = ...
    Speaking: SynthesizerState = ...
    value__ = ...


class VisemeReachedEventArgs(PromptEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AudioPosition(self) -> TimeSpan:
        """ Get: AudioPosition(self: VisemeReachedEventArgs) -> TimeSpan """
        ...

    @property
    def Duration(self) -> TimeSpan:
        """ Get: Duration(self: VisemeReachedEventArgs) -> TimeSpan """
        ...

    @property
    def Emphasis(self) -> SynthesizerEmphasis:
        """ Get: Emphasis(self: VisemeReachedEventArgs) -> SynthesizerEmphasis """
        ...

    @property
    def NextViseme(self) -> int:
        """ Get: NextViseme(self: VisemeReachedEventArgs) -> int """
        ...

    @property
    def Viseme(self) -> int:
        """ Get: Viseme(self: VisemeReachedEventArgs) -> int """
        ...



class VoiceAge(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum VoiceAge, values: Adult (30), Child (10), NotSet (0), Senior (65), Teen (15) """
    Adult: VoiceAge = ...
    Child: VoiceAge = ...
    NotSet: VoiceAge = ...
    Senior: VoiceAge = ...
    Teen: VoiceAge = ...
    value__ = ...


class VoiceChangeEventArgs(PromptEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Voice(self) -> VoiceInfo:
        """ Get: Voice(self: VoiceChangeEventArgs) -> VoiceInfo """
        ...



class VoiceGender(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum VoiceGender, values: Female (2), Male (1), Neutral (3), NotSet (0) """
    Female: VoiceGender = ...
    Male: VoiceGender = ...
    Neutral: VoiceGender = ...
    NotSet: VoiceGender = ...
    value__ = ...


class VoiceInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AdditionalInfo(self) -> IDictionary:
        """ Get: AdditionalInfo(self: VoiceInfo) -> IDictionary[str, str] """
        ...

    @property
    def Age(self) -> VoiceAge:
        """ Get: Age(self: VoiceInfo) -> VoiceAge """
        ...

    @property
    def Culture(self) -> CultureInfo:
        """ Get: Culture(self: VoiceInfo) -> CultureInfo """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: VoiceInfo) -> str """
        ...

    @property
    def Gender(self) -> VoiceGender:
        """ Get: Gender(self: VoiceInfo) -> VoiceGender """
        ...

    @property
    def Id(self) -> str:
        """ Get: Id(self: VoiceInfo) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: VoiceInfo) -> str """
        ...

    @property
    def SupportedAudioFormats(self) -> ReadOnlyCollection:
        """ Get: SupportedAudioFormats(self: VoiceInfo) -> ReadOnlyCollection[SpeechAudioFormatInfo] """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: VoiceInfo, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: VoiceInfo) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


# variables with complex values

