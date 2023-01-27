# encoding: utf-8
# module System.Speech.AudioFormat calls itself AudioFormat
# from System.Speech, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum

"""The following names are not found in the module: field#
"""

# no functions
# classes

class AudioBitsPerSample(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AudioBitsPerSample, values: Eight (8), Sixteen (16) """
    Eight: AudioBitsPerSample = ...
    Sixteen: AudioBitsPerSample = ...
    value__ = ...


class AudioChannel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AudioChannel, values: Mono (1), Stereo (2) """
    Mono: AudioChannel = ...
    Stereo: AudioChannel = ...
    value__ = ...


class EncodingFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EncodingFormat, values: ALaw (6), Pcm (1), ULaw (7) """
    ALaw: EncodingFormat = ...
    Pcm: EncodingFormat = ...
    ULaw: EncodingFormat = ...
    value__ = ...


class SpeechAudioFormatInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    SpeechAudioFormatInfo(encodingFormat: EncodingFormat, samplesPerSecond: int, bitsPerSample: int, channelCount: int, averageBytesPerSecond: int, blockAlign: int, formatSpecificData: Array[Byte])
    SpeechAudioFormatInfo(samplesPerSecond: int, bitsPerSample: AudioBitsPerSample, channel: AudioChannel)
    """
    @property
    def AverageBytesPerSecond(self) -> int:
        """ Get: AverageBytesPerSecond(self: SpeechAudioFormatInfo) -> int """
        ...

    @property
    def BitsPerSample(self) -> int:
        """ Get: BitsPerSample(self: SpeechAudioFormatInfo) -> int """
        ...

    @property
    def BlockAlign(self) -> int:
        """ Get: BlockAlign(self: SpeechAudioFormatInfo) -> int """
        ...

    @property
    def ChannelCount(self) -> int:
        """ Get: ChannelCount(self: SpeechAudioFormatInfo) -> int """
        ...

    @property
    def EncodingFormat(self) -> EncodingFormat:
        """ Get: EncodingFormat(self: SpeechAudioFormatInfo) -> EncodingFormat """
        ...

    @property
    def SamplesPerSecond(self) -> int:
        """ Get: SamplesPerSecond(self: SpeechAudioFormatInfo) -> int """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: SpeechAudioFormatInfo, obj: object) -> bool """
        ...

    def FormatSpecificData(self) -> Array:
        """ FormatSpecificData(self: SpeechAudioFormatInfo) -> Array[Byte] """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SpeechAudioFormatInfo) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


