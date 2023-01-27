# encoding: utf-8
# module System.Text calls itself Text
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import ArgumentException, Array, Byte, Char, Enum, ICloneable

from System.Runtime.Serialization import ISerializable

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class Encoding(ICloneable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ASCII(self) -> Encoding:
        """ Get: ASCII() -> Encoding """
        ...

    @property
    def BigEndianUnicode(self) -> Encoding:
        """ Get: BigEndianUnicode() -> Encoding """
        ...

    @property
    def BodyName(self) -> str:
        """ Get: BodyName(self: Encoding) -> str """
        ...

    @property
    def CodePage(self) -> int:
        """ Get: CodePage(self: Encoding) -> int """
        ...

    @property
    def DecoderFallback(self) -> DecoderFallback:
        """
        Get: DecoderFallback(self: Encoding) -> DecoderFallback
        Set: DecoderFallback(self: Encoding) = value
        """
        ...

    @property
    def Default(self) -> Encoding:
        """ Get: Default() -> Encoding """
        ...

    @property
    def EncoderFallback(self) -> EncoderFallback:
        """
        Get: EncoderFallback(self: Encoding) -> EncoderFallback
        Set: EncoderFallback(self: Encoding) = value
        """
        ...

    @property
    def EncodingName(self) -> str:
        """ Get: EncodingName(self: Encoding) -> str """
        ...

    @property
    def HeaderName(self) -> str:
        """ Get: HeaderName(self: Encoding) -> str """
        ...

    @property
    def IsBrowserDisplay(self) -> bool:
        """ Get: IsBrowserDisplay(self: Encoding) -> bool """
        ...

    @property
    def IsBrowserSave(self) -> bool:
        """ Get: IsBrowserSave(self: Encoding) -> bool """
        ...

    @property
    def IsMailNewsDisplay(self) -> bool:
        """ Get: IsMailNewsDisplay(self: Encoding) -> bool """
        ...

    @property
    def IsMailNewsSave(self) -> bool:
        """ Get: IsMailNewsSave(self: Encoding) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: Encoding) -> bool """
        ...

    @property
    def IsSingleByte(self) -> bool:
        """ Get: IsSingleByte(self: Encoding) -> bool """
        ...

    @property
    def Unicode(self) -> Encoding:
        """ Get: Unicode() -> Encoding """
        ...

    @property
    def UTF32(self) -> Encoding:
        """ Get: UTF32() -> Encoding """
        ...

    @property
    def UTF7(self) -> Encoding:
        """ Get: UTF7() -> Encoding """
        ...

    @property
    def UTF8(self) -> Encoding:
        """ Get: UTF8() -> Encoding """
        ...

    @property
    def WebName(self) -> str:
        """ Get: WebName(self: Encoding) -> str """
        ...

    @property
    def WindowsCodePage(self) -> int:
        """ Get: WindowsCodePage(self: Encoding) -> int """
        ...


    @staticmethod
    def Convert(srcEncoding:Encoding, dstEncoding:Encoding, bytes:Array, index:int = ..., count:int = ...) -> Array:
        """
        Convert(srcEncoding: Encoding, dstEncoding: Encoding, bytes: Array[Byte]) -> Array[Byte]
        Convert(srcEncoding: Encoding, dstEncoding: Encoding, bytes: Array[Byte], index: int, count: int) -> Array[Byte]
        """
        ...

    def Equals(self, value:object) -> bool:
        """ Equals(self: Encoding, value: object) -> bool """
        ...

    def GetByteCount(self, *__args:Array) -> int:
        """
        GetByteCount(self: Encoding, chars: Array[Char]) -> int
        GetByteCount(self: Encoding, s: str) -> int
        GetByteCount(self: Encoding, chars: Char*, count: int) -> int
        GetByteCount(self: Encoding, chars: Array[Char], index: int, count: int) -> int
        """
        ...

    def GetBytes(self, *__args:Array) -> Array:
        """
        GetBytes(self: Encoding, chars: Array[Char]) -> Array[Byte]
        GetBytes(self: Encoding, chars: Array[Char], index: int, count: int) -> Array[Byte]
        GetBytes(self: Encoding, s: str) -> Array[Byte]
        GetBytes(self: Encoding, s: str, charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int) -> int
        GetBytes(self: Encoding, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int) -> int
        GetBytes(self: Encoding, chars: Char*, charCount: int, bytes: Byte*, byteCount: int) -> int
        """
        ...

    def GetCharCount(self, bytes:Byte, *__args:int) -> int:
        """
        GetCharCount(self: Encoding, bytes: Array[Byte]) -> int
        GetCharCount(self: Encoding, bytes: Byte*, count: int) -> int
        GetCharCount(self: Encoding, bytes: Array[Byte], index: int, count: int) -> int
        """
        ...

    def GetChars(self, bytes, *__args) -> Array:
        """
        GetChars(self: Encoding, bytes: Array[Byte]) -> Array[Char]
        GetChars(self: Encoding, bytes: Array[Byte], index: int, count: int) -> Array[Char]
        GetChars(self: Encoding, bytes: Array[Byte], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int) -> int
        GetChars(self: Encoding, bytes: Byte*, byteCount: int, chars: Char*, charCount: int) -> int
        """
        ...

    def GetDecoder(self) -> Decoder:
        """ GetDecoder(self: Encoding) -> Decoder """
        ...

    def GetEncoder(self) -> Encoder:
        """ GetEncoder(self: Encoding) -> Encoder """
        ...

    @staticmethod
    def GetEncoding(*__args:int) -> Encoding:
        """
        GetEncoding(codepage: int) -> Encoding
        GetEncoding(codepage: int, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding
        GetEncoding(name: str) -> Encoding
        GetEncoding(name: str, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding
        """
        ...

    @staticmethod
    def GetEncodings() -> Array:
        """ GetEncodings() -> Array[EncodingInfo] """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Encoding) -> int """
        ...

    def GetMaxByteCount(self, charCount:int) -> int:
        """ GetMaxByteCount(self: Encoding, charCount: int) -> int """
        ...

    def GetMaxCharCount(self, byteCount:int) -> int:
        """ GetMaxCharCount(self: Encoding, byteCount: int) -> int """
        ...

    def GetPreamble(self) -> Array:
        """ GetPreamble(self: Encoding) -> Array[Byte] """
        ...

    def GetString(self, bytes:Byte, *__args:int) -> str:
        """
        GetString(self: Encoding, bytes: Byte*, byteCount: int) -> str
        GetString(self: Encoding, bytes: Array[Byte]) -> str
        GetString(self: Encoding, bytes: Array[Byte], index: int, count: int) -> str
        """
        ...

    def IsAlwaysNormalized(self, form:NormalizationForm = ...) -> bool:
        """
        IsAlwaysNormalized(self: Encoding) -> bool
        IsAlwaysNormalized(self: Encoding, form: NormalizationForm) -> bool
        """
        ...

    @staticmethod
    def RegisterProvider(provider:EncodingProvider): # -> 
        """ RegisterProvider(provider: EncodingProvider) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class ASCIIEncoding(Encoding): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """ ASCIIEncoding() """
    pass

class Decoder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Fallback(self) -> DecoderFallback:
        """
        Get: Fallback(self: Decoder) -> DecoderFallback
        Set: Fallback(self: Decoder) = value
        """
        ...

    @property
    def FallbackBuffer(self) -> DecoderFallbackBuffer:
        """ Get: FallbackBuffer(self: Decoder) -> DecoderFallbackBuffer """
        ...


    def Convert(self, bytes, *__args) -> Tuple_[int, int, bool]:
        """
        Convert(self: Decoder, bytes: Array[Byte], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int, charCount: int, flush: bool) -> (int, int, bool)
        Convert(self: Decoder, bytes: Byte*, byteCount: int, chars: Char*, charCount: int, flush: bool) -> (int, int, bool)
        """
        ...

    def GetCharCount(self, bytes, *__args) -> int:
        """
        GetCharCount(self: Decoder, bytes: Array[Byte], index: int, count: int, flush: bool) -> int
        GetCharCount(self: Decoder, bytes: Byte*, count: int, flush: bool) -> int
        GetCharCount(self: Decoder, bytes: Array[Byte], index: int, count: int) -> int
        """
        ...

    def GetChars(self, bytes, *__args) -> int:
        """
        GetChars(self: Decoder, bytes: Array[Byte], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int, flush: bool) -> int
        GetChars(self: Decoder, bytes: Array[Byte], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int) -> int
        GetChars(self: Decoder, bytes: Byte*, byteCount: int, chars: Char*, charCount: int, flush: bool) -> int
        """
        ...

    def Reset(self): # -> 
        """ Reset(self: Decoder) """
        ...


class DecoderFallback: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ExceptionFallback(self) -> DecoderFallback:
        """ Get: ExceptionFallback() -> DecoderFallback """
        ...

    @property
    def MaxCharCount(self) -> int:
        """ Get: MaxCharCount(self: DecoderFallback) -> int """
        ...

    @property
    def ReplacementFallback(self) -> DecoderFallback:
        """ Get: ReplacementFallback() -> DecoderFallback """
        ...


    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer:
        """ CreateFallbackBuffer(self: DecoderFallback) -> DecoderFallbackBuffer """
        ...



class DecoderExceptionFallback(DecoderFallback): # skipped bases: <type 'object'>
    """ DecoderExceptionFallback() """
    def Equals(self, value:object) -> bool:
        """ Equals(self: DecoderExceptionFallback, value: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: DecoderExceptionFallback) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DecoderFallbackBuffer: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Remaining(self) -> int:
        """ Get: Remaining(self: DecoderFallbackBuffer) -> int """
        ...


    def Fallback(self, bytesUnknown:Array, index:int) -> bool:
        """ Fallback(self: DecoderFallbackBuffer, bytesUnknown: Array[Byte], index: int) -> bool """
        ...

    def GetNextChar(self) -> Char:
        """ GetNextChar(self: DecoderFallbackBuffer) -> Char """
        ...

    def MovePrevious(self) -> bool:
        """ MovePrevious(self: DecoderFallbackBuffer) -> bool """
        ...

    def Reset(self): # -> 
        """ Reset(self: DecoderFallbackBuffer) """
        ...


class DecoderExceptionFallbackBuffer(DecoderFallbackBuffer): # skipped bases: <type 'object'>
    """ DecoderExceptionFallbackBuffer() """
    pass

class DecoderFallbackException(ArgumentException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DecoderFallbackException()
    DecoderFallbackException(message: str)
    DecoderFallbackException(message: str, innerException: Exception)
    DecoderFallbackException(message: str, bytesUnknown: Array[Byte], index: int)
    """
    @property
    def BytesUnknown(self) -> Array:
        """ Get: BytesUnknown(self: DecoderFallbackException) -> Array[Byte] """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: DecoderFallbackException) -> int """
        ...


    SerializeObjectState = ...


class DecoderReplacementFallback(DecoderFallback): # skipped bases: <type 'object'>
    """
    DecoderReplacementFallback()
    DecoderReplacementFallback(replacement: str)
    """
    @property
    def DefaultString(self) -> str:
        """ Get: DefaultString(self: DecoderReplacementFallback) -> str """
        ...


    def Equals(self, value:object) -> bool:
        """ Equals(self: DecoderReplacementFallback, value: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: DecoderReplacementFallback) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, replacement:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, replacement: str)
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DecoderReplacementFallbackBuffer(DecoderFallbackBuffer): # skipped bases: <type 'object'>
    """ DecoderReplacementFallbackBuffer(fallback: DecoderReplacementFallback) """
    def __new__(cls, fallback:DecoderReplacementFallback) -> Self:
        """ __new__(cls: type, fallback: DecoderReplacementFallback) """
        ...


class Encoder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Fallback(self) -> EncoderFallback:
        """
        Get: Fallback(self: Encoder) -> EncoderFallback
        Set: Fallback(self: Encoder) = value
        """
        ...

    @property
    def FallbackBuffer(self) -> EncoderFallbackBuffer:
        """ Get: FallbackBuffer(self: Encoder) -> EncoderFallbackBuffer """
        ...


    def Convert(self, chars, *__args) -> Tuple_[int, int, bool]:
        """
        Convert(self: Encoder, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int, byteCount: int, flush: bool) -> (int, int, bool)
        Convert(self: Encoder, chars: Char*, charCount: int, bytes: Byte*, byteCount: int, flush: bool) -> (int, int, bool)
        """
        ...

    def GetByteCount(self, chars, *__args) -> int:
        """
        GetByteCount(self: Encoder, chars: Char*, count: int, flush: bool) -> int
        GetByteCount(self: Encoder, chars: Array[Char], index: int, count: int, flush: bool) -> int
        """
        ...

    def GetBytes(self, chars, *__args) -> int:
        """
        GetBytes(self: Encoder, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int, flush: bool) -> int
        GetBytes(self: Encoder, chars: Char*, charCount: int, bytes: Byte*, byteCount: int, flush: bool) -> int
        """
        ...

    def Reset(self): # -> 
        """ Reset(self: Encoder) """
        ...


class EncoderFallback: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ExceptionFallback(self) -> EncoderFallback:
        """ Get: ExceptionFallback() -> EncoderFallback """
        ...

    @property
    def MaxCharCount(self) -> int:
        """ Get: MaxCharCount(self: EncoderFallback) -> int """
        ...

    @property
    def ReplacementFallback(self) -> EncoderFallback:
        """ Get: ReplacementFallback() -> EncoderFallback """
        ...


    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer:
        """ CreateFallbackBuffer(self: EncoderFallback) -> EncoderFallbackBuffer """
        ...



class EncoderExceptionFallback(EncoderFallback): # skipped bases: <type 'object'>
    """ EncoderExceptionFallback() """
    def Equals(self, value:object) -> bool:
        """ Equals(self: EncoderExceptionFallback, value: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: EncoderExceptionFallback) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class EncoderFallbackBuffer: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Remaining(self) -> int:
        """ Get: Remaining(self: EncoderFallbackBuffer) -> int """
        ...


    def Fallback(self, *__args) -> bool:
        """
        Fallback(self: EncoderFallbackBuffer, charUnknown: Char, index: int) -> bool
        Fallback(self: EncoderFallbackBuffer, charUnknownHigh: Char, charUnknownLow: Char, index: int) -> bool
        """
        ...

    def GetNextChar(self) -> Char:
        """ GetNextChar(self: EncoderFallbackBuffer) -> Char """
        ...

    def MovePrevious(self) -> bool:
        """ MovePrevious(self: EncoderFallbackBuffer) -> bool """
        ...

    def Reset(self): # -> 
        """ Reset(self: EncoderFallbackBuffer) """
        ...


class EncoderExceptionFallbackBuffer(EncoderFallbackBuffer): # skipped bases: <type 'object'>
    """ EncoderExceptionFallbackBuffer() """
    pass

class EncoderFallbackException(ArgumentException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    EncoderFallbackException()
    EncoderFallbackException(message: str)
    EncoderFallbackException(message: str, innerException: Exception)
    """
    @property
    def CharUnknown(self) -> Char:
        """ Get: CharUnknown(self: EncoderFallbackException) -> Char """
        ...

    @property
    def CharUnknownHigh(self) -> Char:
        """ Get: CharUnknownHigh(self: EncoderFallbackException) -> Char """
        ...

    @property
    def CharUnknownLow(self) -> Char:
        """ Get: CharUnknownLow(self: EncoderFallbackException) -> Char """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: EncoderFallbackException) -> int """
        ...


    def IsUnknownSurrogate(self) -> bool:
        """ IsUnknownSurrogate(self: EncoderFallbackException) -> bool """
        ...

    SerializeObjectState = ...


class EncoderReplacementFallback(EncoderFallback): # skipped bases: <type 'object'>
    """
    EncoderReplacementFallback()
    EncoderReplacementFallback(replacement: str)
    """
    @property
    def DefaultString(self) -> str:
        """ Get: DefaultString(self: EncoderReplacementFallback) -> str """
        ...


    def Equals(self, value:object) -> bool:
        """ Equals(self: EncoderReplacementFallback, value: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: EncoderReplacementFallback) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, replacement:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, replacement: str)
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class EncoderReplacementFallbackBuffer(EncoderFallbackBuffer): # skipped bases: <type 'object'>
    """ EncoderReplacementFallbackBuffer(fallback: EncoderReplacementFallback) """
    def __new__(cls, fallback:EncoderReplacementFallback) -> Self:
        """ __new__(cls: type, fallback: EncoderReplacementFallback) """
        ...


class EncodingInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CodePage(self) -> int:
        """ Get: CodePage(self: EncodingInfo) -> int """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: EncodingInfo) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: EncodingInfo) -> str """
        ...


    def Equals(self, value:object) -> bool:
        """ Equals(self: EncodingInfo, value: object) -> bool """
        ...

    def GetEncoding(self) -> Encoding:
        """ GetEncoding(self: EncodingInfo) -> Encoding """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: EncodingInfo) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class EncodingProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ EncodingProvider() """
    def GetEncoding(self, *__args:str) -> Encoding:
        """
        GetEncoding(self: EncodingProvider, name: str, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding
        GetEncoding(self: EncodingProvider, codepage: int, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding
        GetEncoding(self: EncodingProvider, name: str) -> Encoding
        GetEncoding(self: EncodingProvider, codepage: int) -> Encoding
        """
        ...


class NormalizationForm(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NormalizationForm, values: FormC (1), FormD (2), FormKC (5), FormKD (6) """
    FormC: NormalizationForm = ...
    FormD: NormalizationForm = ...
    FormKC: NormalizationForm = ...
    FormKD: NormalizationForm = ...
    value__ = ...


class StringBuilder(ISerializable): # skipped bases: <type 'object'>
    """
    StringBuilder()
    StringBuilder(capacity: int)
    StringBuilder(value: str)
    StringBuilder(value: str, capacity: int)
    StringBuilder(value: str, startIndex: int, length: int, capacity: int)
    StringBuilder(capacity: int, maxCapacity: int)
    """
    @property
    def Capacity(self) -> int:
        """
        Get: Capacity(self: StringBuilder) -> int
        Set: Capacity(self: StringBuilder) = value
        """
        ...

    @property
    def Length(self) -> int:
        """
        Get: Length(self: StringBuilder) -> int
        Set: Length(self: StringBuilder) = value
        """
        ...

    @property
    def MaxCapacity(self) -> int:
        """ Get: MaxCapacity(self: StringBuilder) -> int """
        ...


    def Append(self, value:Char, *__args:int) -> StringBuilder:
        """
        Append(self: StringBuilder, value: Char, repeatCount: int) -> StringBuilder
        Append(self: StringBuilder, value: Array[Char]) -> StringBuilder
        Append(self: StringBuilder, value: object) -> StringBuilder
        Append(self: StringBuilder, value: UInt64) -> StringBuilder
        Append(self: StringBuilder, value: UInt32) -> StringBuilder
        Append(self: StringBuilder, value: UInt16) -> StringBuilder
        Append(self: StringBuilder, value: Decimal) -> StringBuilder
        Append(self: StringBuilder, value: float) -> StringBuilder
        Append(self: StringBuilder, value: Single) -> StringBuilder
        Append(self: StringBuilder, value: Int64) -> StringBuilder
        Append(self: StringBuilder, value: int) -> StringBuilder
        Append(self: StringBuilder, value: Int16) -> StringBuilder
        Append(self: StringBuilder, value: Char) -> StringBuilder
        Append(self: StringBuilder, value: Byte) -> StringBuilder
        Append(self: StringBuilder, value: SByte) -> StringBuilder
        Append(self: StringBuilder, value: str, startIndex: int, count: int) -> StringBuilder
        Append(self: StringBuilder, value: str) -> StringBuilder
        Append(self: StringBuilder, value: Array[Char], startIndex: int, charCount: int) -> StringBuilder
        Append(self: StringBuilder, value: Char*, valueCount: int) -> StringBuilder
        Append(self: StringBuilder, value: bool) -> StringBuilder
        """
        ...

    def AppendFormat(self, *__args) -> StringBuilder:
        """
        AppendFormat(self: StringBuilder, format: str, arg0: object) -> StringBuilder
        AppendFormat(self: StringBuilder, format: str, arg0: object, arg1: object) -> StringBuilder
        AppendFormat(self: StringBuilder, format: str, arg0: object, arg1: object, arg2: object) -> StringBuilder
        AppendFormat(self: StringBuilder, provider: IFormatProvider, format: str, arg0: object) -> StringBuilder
        AppendFormat(self: StringBuilder, provider: IFormatProvider, format: str, arg0: object, arg1: object) -> StringBuilder
        AppendFormat(self: StringBuilder, provider: IFormatProvider, format: str, arg0: object, arg1: object, arg2: object) -> StringBuilder
        AppendFormat(self: StringBuilder, format: str, *args: Array[object]) -> StringBuilder
        AppendFormat(self: StringBuilder, provider: IFormatProvider, format: str, *args: Array[object]) -> StringBuilder
        """
        ...

    def AppendLine(self, value:str = ...) -> StringBuilder:
        """
        AppendLine(self: StringBuilder) -> StringBuilder
        AppendLine(self: StringBuilder, value: str) -> StringBuilder
        """
        ...

    def Clear(self) -> StringBuilder:
        """ Clear(self: StringBuilder) -> StringBuilder """
        ...

    def CopyTo(self, sourceIndex:int, destination:Array, destinationIndex:int, count:int): # -> 
        """ CopyTo(self: StringBuilder, sourceIndex: int, destination: Array[Char], destinationIndex: int, count: int) """
        ...

    def EnsureCapacity(self, capacity:int) -> int:
        """ EnsureCapacity(self: StringBuilder, capacity: int) -> int """
        ...

    def Equals(self, *__args:StringBuilder) -> bool:
        """ Equals(self: StringBuilder, sb: StringBuilder) -> bool """
        ...

    def Insert(self, index:int, value:str, *__args:int) -> StringBuilder:
        """
        Insert(self: StringBuilder, index: int, value: str, count: int) -> StringBuilder
        Insert(self: StringBuilder, index: int, value: UInt64) -> StringBuilder
        Insert(self: StringBuilder, index: int, value: UInt32) -> StringBuilder
        Insert(self: StringBuilder, index: int, value: UInt16) -> StringBuilder
        Insert(self: StringBuilder, index: int, value: Decimal) -> StringBuilder
        Insert(self: StringBuilder, index: int, value: float) -> StringBuilder
        Insert(self: StringBuilder, index: int, value: Single) -> StringBuilder
        Insert(self: StringBuilder, index: int, value: Int64) -> StringBuilder
        Insert(self: StringBuilder, index: int, value: int) -> StringBuilder
        Insert(self: StringBuilder, index: int, value: Array[Char], startIndex: int, charCount: int) -> StringBuilder
        Insert(self: StringBuilder, index: int, value: Array[Char]) -> StringBuilder
        Insert(self: StringBuilder, index: int, value: Char) -> StringBuilder
        Insert(self: StringBuilder, index: int, value: Int16) -> StringBuilder
        Insert(self: StringBuilder, index: int, value: Byte) -> StringBuilder
        Insert(self: StringBuilder, index: int, value: SByte) -> StringBuilder
        Insert(self: StringBuilder, index: int, value: str) -> StringBuilder
        Insert(self: StringBuilder, index: int, value: object) -> StringBuilder
        Insert(self: StringBuilder, index: int, value: bool) -> StringBuilder
        """
        ...

    def Remove(self, startIndex:int, length:int) -> StringBuilder:
        """ Remove(self: StringBuilder, startIndex: int, length: int) -> StringBuilder """
        ...

    def Replace(self, *__args) -> StringBuilder:
        """
        Replace(self: StringBuilder, oldValue: str, newValue: str) -> StringBuilder
        Replace(self: StringBuilder, oldValue: str, newValue: str, startIndex: int, count: int) -> StringBuilder
        Replace(self: StringBuilder, oldChar: Char, newChar: Char) -> StringBuilder
        Replace(self: StringBuilder, oldChar: Char, newChar: Char, startIndex: int, count: int) -> StringBuilder
        """
        ...

    def ToString(self, startIndex:int = ..., length:int = ...) -> str:
        """
        ToString(self: StringBuilder) -> str
        ToString(self: StringBuilder, startIndex: int, length: int) -> str
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class UnicodeEncoding(Encoding): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    UnicodeEncoding()
    UnicodeEncoding(bigEndian: bool, byteOrderMark: bool)
    UnicodeEncoding(bigEndian: bool, byteOrderMark: bool, throwOnInvalidBytes: bool)
    """
    CharSize: int = ...


class UTF32Encoding(Encoding): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    UTF32Encoding()
    UTF32Encoding(bigEndian: bool, byteOrderMark: bool)
    UTF32Encoding(bigEndian: bool, byteOrderMark: bool, throwOnInvalidCharacters: bool)
    """
    pass

class UTF7Encoding(Encoding): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    UTF7Encoding()
    UTF7Encoding(allowOptionals: bool)
    """
    pass

class UTF8Encoding(Encoding): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    UTF8Encoding()
    UTF8Encoding(encoderShouldEmitUTF8Identifier: bool)
    UTF8Encoding(encoderShouldEmitUTF8Identifier: bool, throwOnInvalidBytes: bool)
    """
    pass

# variables with complex values

