# encoding: utf-8
# module System.Net.Http.Headers calls itself Headers
# from System.Net.Http, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, ICloneable, Nullable, Uri

from System.Collections import ICollection, IEnumerable, IEnumerator

from typing import Tuple as Tuple_


# no functions
# classes

class AuthenticationHeaderValue(ICloneable): # skipped bases: <type 'object'>
    """
    AuthenticationHeaderValue(scheme: str)
    AuthenticationHeaderValue(scheme: str, parameter: str)
    """
    @property
    def Parameter(self) -> str:
        """ Get: Parameter(self: AuthenticationHeaderValue) -> str """
        ...

    @property
    def Scheme(self) -> str:
        """ Get: Scheme(self: AuthenticationHeaderValue) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: AuthenticationHeaderValue, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: AuthenticationHeaderValue) -> int """
        ...

    @staticmethod
    def Parse(input:str) -> AuthenticationHeaderValue:
        """ Parse(input: str) -> AuthenticationHeaderValue """
        ...

    def ToString(self) -> str:
        """ ToString(self: AuthenticationHeaderValue) -> str """
        ...

    @staticmethod
    def TryParse(input, parsedValue) -> Tuple_[bool, AuthenticationHeaderValue]:
        """ TryParse(input: str) -> (bool, AuthenticationHeaderValue) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CacheControlHeaderValue(ICloneable): # skipped bases: <type 'object'>
    """ CacheControlHeaderValue() """
    @property
    def Extensions(self) -> ICollection:
        """ Get: Extensions(self: CacheControlHeaderValue) -> ICollection[NameValueHeaderValue] """
        ...

    @property
    def MaxAge(self) -> Nullable:
        """
        Get: MaxAge(self: CacheControlHeaderValue) -> Nullable[TimeSpan]
        Set: MaxAge(self: CacheControlHeaderValue) = value
        """
        ...

    @property
    def MaxStale(self) -> bool:
        """
        Get: MaxStale(self: CacheControlHeaderValue) -> bool
        Set: MaxStale(self: CacheControlHeaderValue) = value
        """
        ...

    @property
    def MaxStaleLimit(self) -> Nullable:
        """
        Get: MaxStaleLimit(self: CacheControlHeaderValue) -> Nullable[TimeSpan]
        Set: MaxStaleLimit(self: CacheControlHeaderValue) = value
        """
        ...

    @property
    def MinFresh(self) -> Nullable:
        """
        Get: MinFresh(self: CacheControlHeaderValue) -> Nullable[TimeSpan]
        Set: MinFresh(self: CacheControlHeaderValue) = value
        """
        ...

    @property
    def MustRevalidate(self) -> bool:
        """
        Get: MustRevalidate(self: CacheControlHeaderValue) -> bool
        Set: MustRevalidate(self: CacheControlHeaderValue) = value
        """
        ...

    @property
    def NoCache(self) -> bool:
        """
        Get: NoCache(self: CacheControlHeaderValue) -> bool
        Set: NoCache(self: CacheControlHeaderValue) = value
        """
        ...

    @property
    def NoCacheHeaders(self) -> ICollection:
        """ Get: NoCacheHeaders(self: CacheControlHeaderValue) -> ICollection[str] """
        ...

    @property
    def NoStore(self) -> bool:
        """
        Get: NoStore(self: CacheControlHeaderValue) -> bool
        Set: NoStore(self: CacheControlHeaderValue) = value
        """
        ...

    @property
    def NoTransform(self) -> bool:
        """
        Get: NoTransform(self: CacheControlHeaderValue) -> bool
        Set: NoTransform(self: CacheControlHeaderValue) = value
        """
        ...

    @property
    def OnlyIfCached(self) -> bool:
        """
        Get: OnlyIfCached(self: CacheControlHeaderValue) -> bool
        Set: OnlyIfCached(self: CacheControlHeaderValue) = value
        """
        ...

    @property
    def Private(self) -> bool:
        """
        Get: Private(self: CacheControlHeaderValue) -> bool
        Set: Private(self: CacheControlHeaderValue) = value
        """
        ...

    @property
    def PrivateHeaders(self) -> ICollection:
        """ Get: PrivateHeaders(self: CacheControlHeaderValue) -> ICollection[str] """
        ...

    @property
    def ProxyRevalidate(self) -> bool:
        """
        Get: ProxyRevalidate(self: CacheControlHeaderValue) -> bool
        Set: ProxyRevalidate(self: CacheControlHeaderValue) = value
        """
        ...

    @property
    def Public(self) -> bool:
        """
        Get: Public(self: CacheControlHeaderValue) -> bool
        Set: Public(self: CacheControlHeaderValue) = value
        """
        ...

    @property
    def SharedMaxAge(self) -> Nullable:
        """
        Get: SharedMaxAge(self: CacheControlHeaderValue) -> Nullable[TimeSpan]
        Set: SharedMaxAge(self: CacheControlHeaderValue) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: CacheControlHeaderValue, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CacheControlHeaderValue) -> int """
        ...

    @staticmethod
    def Parse(input:str) -> CacheControlHeaderValue:
        """ Parse(input: str) -> CacheControlHeaderValue """
        ...

    def ToString(self) -> str:
        """ ToString(self: CacheControlHeaderValue) -> str """
        ...

    @staticmethod
    def TryParse(input, parsedValue) -> Tuple_[bool, CacheControlHeaderValue]:
        """ TryParse(input: str) -> (bool, CacheControlHeaderValue) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ContentDispositionHeaderValue(ICloneable): # skipped bases: <type 'object'>
    """ ContentDispositionHeaderValue(dispositionType: str) """
    @property
    def CreationDate(self) -> Nullable:
        """
        Get: CreationDate(self: ContentDispositionHeaderValue) -> Nullable[DateTimeOffset]
        Set: CreationDate(self: ContentDispositionHeaderValue) = value
        """
        ...

    @property
    def DispositionType(self) -> str:
        """
        Get: DispositionType(self: ContentDispositionHeaderValue) -> str
        Set: DispositionType(self: ContentDispositionHeaderValue) = value
        """
        ...

    @property
    def FileName(self) -> str:
        """
        Get: FileName(self: ContentDispositionHeaderValue) -> str
        Set: FileName(self: ContentDispositionHeaderValue) = value
        """
        ...

    @property
    def FileNameStar(self) -> str:
        """
        Get: FileNameStar(self: ContentDispositionHeaderValue) -> str
        Set: FileNameStar(self: ContentDispositionHeaderValue) = value
        """
        ...

    @property
    def ModificationDate(self) -> Nullable:
        """
        Get: ModificationDate(self: ContentDispositionHeaderValue) -> Nullable[DateTimeOffset]
        Set: ModificationDate(self: ContentDispositionHeaderValue) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ContentDispositionHeaderValue) -> str
        Set: Name(self: ContentDispositionHeaderValue) = value
        """
        ...

    @property
    def Parameters(self) -> ICollection:
        """ Get: Parameters(self: ContentDispositionHeaderValue) -> ICollection[NameValueHeaderValue] """
        ...

    @property
    def ReadDate(self) -> Nullable:
        """
        Get: ReadDate(self: ContentDispositionHeaderValue) -> Nullable[DateTimeOffset]
        Set: ReadDate(self: ContentDispositionHeaderValue) = value
        """
        ...

    @property
    def Size(self) -> Nullable:
        """
        Get: Size(self: ContentDispositionHeaderValue) -> Nullable[Int64]
        Set: Size(self: ContentDispositionHeaderValue) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: ContentDispositionHeaderValue, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ContentDispositionHeaderValue) -> int """
        ...

    @staticmethod
    def Parse(input:str) -> ContentDispositionHeaderValue:
        """ Parse(input: str) -> ContentDispositionHeaderValue """
        ...

    def ToString(self) -> str:
        """ ToString(self: ContentDispositionHeaderValue) -> str """
        ...

    @staticmethod
    def TryParse(input, parsedValue) -> Tuple_[bool, ContentDispositionHeaderValue]:
        """ TryParse(input: str) -> (bool, ContentDispositionHeaderValue) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ContentRangeHeaderValue(ICloneable): # skipped bases: <type 'object'>
    """
    ContentRangeHeaderValue(from: Int64, to: Int64, length: Int64)
    ContentRangeHeaderValue(length: Int64)
    ContentRangeHeaderValue(from: Int64, to: Int64)
    """
    @property
    def From(self) -> Nullable:
        """ Get: From(self: ContentRangeHeaderValue) -> Nullable[Int64] """
        ...

    @property
    def HasLength(self) -> bool:
        """ Get: HasLength(self: ContentRangeHeaderValue) -> bool """
        ...

    @property
    def HasRange(self) -> bool:
        """ Get: HasRange(self: ContentRangeHeaderValue) -> bool """
        ...

    @property
    def Length(self) -> Nullable:
        """ Get: Length(self: ContentRangeHeaderValue) -> Nullable[Int64] """
        ...

    @property
    def To(self) -> Nullable:
        """ Get: To(self: ContentRangeHeaderValue) -> Nullable[Int64] """
        ...

    @property
    def Unit(self) -> str:
        """
        Get: Unit(self: ContentRangeHeaderValue) -> str
        Set: Unit(self: ContentRangeHeaderValue) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: ContentRangeHeaderValue, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ContentRangeHeaderValue) -> int """
        ...

    @staticmethod
    def Parse(input:str) -> ContentRangeHeaderValue:
        """ Parse(input: str) -> ContentRangeHeaderValue """
        ...

    def ToString(self) -> str:
        """ ToString(self: ContentRangeHeaderValue) -> str """
        ...

    @staticmethod
    def TryParse(input, parsedValue) -> Tuple_[bool, ContentRangeHeaderValue]:
        """ TryParse(input: str) -> (bool, ContentRangeHeaderValue) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class EntityTagHeaderValue(ICloneable): # skipped bases: <type 'object'>
    """
    EntityTagHeaderValue(tag: str)
    EntityTagHeaderValue(tag: str, isWeak: bool)
    """
    @property
    def Any(self) -> EntityTagHeaderValue:
        """ Get: Any() -> EntityTagHeaderValue """
        ...

    @property
    def IsWeak(self) -> bool:
        """ Get: IsWeak(self: EntityTagHeaderValue) -> bool """
        ...

    @property
    def Tag(self) -> str:
        """ Get: Tag(self: EntityTagHeaderValue) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: EntityTagHeaderValue, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: EntityTagHeaderValue) -> int """
        ...

    @staticmethod
    def Parse(input:str) -> EntityTagHeaderValue:
        """ Parse(input: str) -> EntityTagHeaderValue """
        ...

    def ToString(self) -> str:
        """ ToString(self: EntityTagHeaderValue) -> str """
        ...

    @staticmethod
    def TryParse(input, parsedValue) -> Tuple_[bool, EntityTagHeaderValue]:
        """ TryParse(input: str) -> (bool, EntityTagHeaderValue) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class HttpHeaders(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Add(self, name:str, *__args:str): # -> 
        """ Add(self: HttpHeaders, name: str, value: str)Add(self: HttpHeaders, name: str, values: IEnumerable[str]) """
        ...

    def Clear(self): # -> 
        """ Clear(self: HttpHeaders) """
        ...

    def Contains(self, name:str) -> bool:
        """ Contains(self: HttpHeaders, name: str) -> bool """
        ...

    def GetValues(self, name:str) -> IEnumerable:
        """ GetValues(self: HttpHeaders, name: str) -> IEnumerable[str] """
        ...

    def Remove(self, name:str) -> bool:
        """ Remove(self: HttpHeaders, name: str) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: HttpHeaders) -> str """
        ...

    def TryAddWithoutValidation(self, name:str, *__args:IEnumerable) -> bool:
        """
        TryAddWithoutValidation(self: HttpHeaders, name: str, values: IEnumerable[str]) -> bool
        TryAddWithoutValidation(self: HttpHeaders, name: str, value: str) -> bool
        """
        ...

    def TryGetValues(self, name, values) -> Tuple_[bool, IEnumerable]:
        """ TryGetValues(self: HttpHeaders, name: str) -> (bool, IEnumerable[str]) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[KeyValuePair[str, IEnumerable[str]]](enumerable: IEnumerable[KeyValuePair[str, IEnumerable[str]]], value: KeyValuePair[str, IEnumerable[str]]) -> bool """
        ...


class HttpContentHeaders(HttpHeaders): # skipped bases: <type 'IEnumerable[KeyValuePair[str, IEnumerable[str]]]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Allow(self) -> ICollection:
        """ Get: Allow(self: HttpContentHeaders) -> ICollection[str] """
        ...

    @property
    def ContentDisposition(self) -> ContentDispositionHeaderValue:
        """
        Get: ContentDisposition(self: HttpContentHeaders) -> ContentDispositionHeaderValue
        Set: ContentDisposition(self: HttpContentHeaders) = value
        """
        ...

    @property
    def ContentEncoding(self) -> ICollection:
        """ Get: ContentEncoding(self: HttpContentHeaders) -> ICollection[str] """
        ...

    @property
    def ContentLanguage(self) -> ICollection:
        """ Get: ContentLanguage(self: HttpContentHeaders) -> ICollection[str] """
        ...

    @property
    def ContentLength(self) -> Nullable:
        """
        Get: ContentLength(self: HttpContentHeaders) -> Nullable[Int64]
        Set: ContentLength(self: HttpContentHeaders) = value
        """
        ...

    @property
    def ContentLocation(self) -> Uri:
        """
        Get: ContentLocation(self: HttpContentHeaders) -> Uri
        Set: ContentLocation(self: HttpContentHeaders) = value
        """
        ...

    @property
    def ContentMD5(self) -> Array:
        """
        Get: ContentMD5(self: HttpContentHeaders) -> Array[Byte]
        Set: ContentMD5(self: HttpContentHeaders) = value
        """
        ...

    @property
    def ContentRange(self) -> ContentRangeHeaderValue:
        """
        Get: ContentRange(self: HttpContentHeaders) -> ContentRangeHeaderValue
        Set: ContentRange(self: HttpContentHeaders) = value
        """
        ...

    @property
    def ContentType(self) -> MediaTypeHeaderValue:
        """
        Get: ContentType(self: HttpContentHeaders) -> MediaTypeHeaderValue
        Set: ContentType(self: HttpContentHeaders) = value
        """
        ...

    @property
    def Expires(self) -> Nullable:
        """
        Get: Expires(self: HttpContentHeaders) -> Nullable[DateTimeOffset]
        Set: Expires(self: HttpContentHeaders) = value
        """
        ...

    @property
    def LastModified(self) -> Nullable:
        """
        Get: LastModified(self: HttpContentHeaders) -> Nullable[DateTimeOffset]
        Set: LastModified(self: HttpContentHeaders) = value
        """
        ...



class HttpHeaderValueCollection(ICollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: HttpHeaderValueCollection[T]) -> IEnumerator[T] """
        ...

    def ParseAdd(self, input:str): # -> 
        """ ParseAdd(self: HttpHeaderValueCollection[T], input: str) """
        ...

    def ToString(self) -> str:
        """ ToString(self: HttpHeaderValueCollection[T]) -> str """
        ...

    def TryParseAdd(self, input:str) -> bool:
        """ TryParseAdd(self: HttpHeaderValueCollection[T], input: str) -> bool """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class HttpRequestHeaders(HttpHeaders): # skipped bases: <type 'IEnumerable[KeyValuePair[str, IEnumerable[str]]]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Accept(self) -> HttpHeaderValueCollection:
        """ Get: Accept(self: HttpRequestHeaders) -> HttpHeaderValueCollection[MediaTypeWithQualityHeaderValue] """
        ...

    @property
    def AcceptCharset(self) -> HttpHeaderValueCollection:
        """ Get: AcceptCharset(self: HttpRequestHeaders) -> HttpHeaderValueCollection[StringWithQualityHeaderValue] """
        ...

    @property
    def AcceptEncoding(self) -> HttpHeaderValueCollection:
        """ Get: AcceptEncoding(self: HttpRequestHeaders) -> HttpHeaderValueCollection[StringWithQualityHeaderValue] """
        ...

    @property
    def AcceptLanguage(self) -> HttpHeaderValueCollection:
        """ Get: AcceptLanguage(self: HttpRequestHeaders) -> HttpHeaderValueCollection[StringWithQualityHeaderValue] """
        ...

    @property
    def Authorization(self) -> AuthenticationHeaderValue:
        """
        Get: Authorization(self: HttpRequestHeaders) -> AuthenticationHeaderValue
        Set: Authorization(self: HttpRequestHeaders) = value
        """
        ...

    @property
    def CacheControl(self) -> CacheControlHeaderValue:
        """
        Get: CacheControl(self: HttpRequestHeaders) -> CacheControlHeaderValue
        Set: CacheControl(self: HttpRequestHeaders) = value
        """
        ...

    @property
    def Connection(self) -> HttpHeaderValueCollection:
        """ Get: Connection(self: HttpRequestHeaders) -> HttpHeaderValueCollection[str] """
        ...

    @property
    def ConnectionClose(self) -> Nullable:
        """
        Get: ConnectionClose(self: HttpRequestHeaders) -> Nullable[bool]
        Set: ConnectionClose(self: HttpRequestHeaders) = value
        """
        ...

    @property
    def Date(self) -> Nullable:
        """
        Get: Date(self: HttpRequestHeaders) -> Nullable[DateTimeOffset]
        Set: Date(self: HttpRequestHeaders) = value
        """
        ...

    @property
    def Expect(self) -> HttpHeaderValueCollection:
        """ Get: Expect(self: HttpRequestHeaders) -> HttpHeaderValueCollection[NameValueWithParametersHeaderValue] """
        ...

    @property
    def ExpectContinue(self) -> Nullable:
        """
        Get: ExpectContinue(self: HttpRequestHeaders) -> Nullable[bool]
        Set: ExpectContinue(self: HttpRequestHeaders) = value
        """
        ...

    @property
    def From(self) -> str:
        """
        Get: From(self: HttpRequestHeaders) -> str
        Set: From(self: HttpRequestHeaders) = value
        """
        ...

    @property
    def Host(self) -> str:
        """
        Get: Host(self: HttpRequestHeaders) -> str
        Set: Host(self: HttpRequestHeaders) = value
        """
        ...

    @property
    def IfMatch(self) -> HttpHeaderValueCollection:
        """ Get: IfMatch(self: HttpRequestHeaders) -> HttpHeaderValueCollection[EntityTagHeaderValue] """
        ...

    @property
    def IfModifiedSince(self) -> Nullable:
        """
        Get: IfModifiedSince(self: HttpRequestHeaders) -> Nullable[DateTimeOffset]
        Set: IfModifiedSince(self: HttpRequestHeaders) = value
        """
        ...

    @property
    def IfNoneMatch(self) -> HttpHeaderValueCollection:
        """ Get: IfNoneMatch(self: HttpRequestHeaders) -> HttpHeaderValueCollection[EntityTagHeaderValue] """
        ...

    @property
    def IfRange(self) -> RangeConditionHeaderValue:
        """
        Get: IfRange(self: HttpRequestHeaders) -> RangeConditionHeaderValue
        Set: IfRange(self: HttpRequestHeaders) = value
        """
        ...

    @property
    def IfUnmodifiedSince(self) -> Nullable:
        """
        Get: IfUnmodifiedSince(self: HttpRequestHeaders) -> Nullable[DateTimeOffset]
        Set: IfUnmodifiedSince(self: HttpRequestHeaders) = value
        """
        ...

    @property
    def MaxForwards(self) -> Nullable:
        """
        Get: MaxForwards(self: HttpRequestHeaders) -> Nullable[int]
        Set: MaxForwards(self: HttpRequestHeaders) = value
        """
        ...

    @property
    def Pragma(self) -> HttpHeaderValueCollection:
        """ Get: Pragma(self: HttpRequestHeaders) -> HttpHeaderValueCollection[NameValueHeaderValue] """
        ...

    @property
    def ProxyAuthorization(self) -> AuthenticationHeaderValue:
        """
        Get: ProxyAuthorization(self: HttpRequestHeaders) -> AuthenticationHeaderValue
        Set: ProxyAuthorization(self: HttpRequestHeaders) = value
        """
        ...

    @property
    def Range(self) -> RangeHeaderValue:
        """
        Get: Range(self: HttpRequestHeaders) -> RangeHeaderValue
        Set: Range(self: HttpRequestHeaders) = value
        """
        ...

    @property
    def Referrer(self) -> Uri:
        """
        Get: Referrer(self: HttpRequestHeaders) -> Uri
        Set: Referrer(self: HttpRequestHeaders) = value
        """
        ...

    @property
    def TE(self) -> HttpHeaderValueCollection:
        """ Get: TE(self: HttpRequestHeaders) -> HttpHeaderValueCollection[TransferCodingWithQualityHeaderValue] """
        ...

    @property
    def Trailer(self) -> HttpHeaderValueCollection:
        """ Get: Trailer(self: HttpRequestHeaders) -> HttpHeaderValueCollection[str] """
        ...

    @property
    def TransferEncoding(self) -> HttpHeaderValueCollection:
        """ Get: TransferEncoding(self: HttpRequestHeaders) -> HttpHeaderValueCollection[TransferCodingHeaderValue] """
        ...

    @property
    def TransferEncodingChunked(self) -> Nullable:
        """
        Get: TransferEncodingChunked(self: HttpRequestHeaders) -> Nullable[bool]
        Set: TransferEncodingChunked(self: HttpRequestHeaders) = value
        """
        ...

    @property
    def Upgrade(self) -> HttpHeaderValueCollection:
        """ Get: Upgrade(self: HttpRequestHeaders) -> HttpHeaderValueCollection[ProductHeaderValue] """
        ...

    @property
    def UserAgent(self) -> HttpHeaderValueCollection:
        """ Get: UserAgent(self: HttpRequestHeaders) -> HttpHeaderValueCollection[ProductInfoHeaderValue] """
        ...

    @property
    def Via(self) -> HttpHeaderValueCollection:
        """ Get: Via(self: HttpRequestHeaders) -> HttpHeaderValueCollection[ViaHeaderValue] """
        ...

    @property
    def Warning(self) -> HttpHeaderValueCollection:
        """ Get: Warning(self: HttpRequestHeaders) -> HttpHeaderValueCollection[WarningHeaderValue] """
        ...



class HttpResponseHeaders(HttpHeaders): # skipped bases: <type 'IEnumerable[KeyValuePair[str, IEnumerable[str]]]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def AcceptRanges(self) -> HttpHeaderValueCollection:
        """ Get: AcceptRanges(self: HttpResponseHeaders) -> HttpHeaderValueCollection[str] """
        ...

    @property
    def Age(self) -> Nullable:
        """
        Get: Age(self: HttpResponseHeaders) -> Nullable[TimeSpan]
        Set: Age(self: HttpResponseHeaders) = value
        """
        ...

    @property
    def CacheControl(self) -> CacheControlHeaderValue:
        """
        Get: CacheControl(self: HttpResponseHeaders) -> CacheControlHeaderValue
        Set: CacheControl(self: HttpResponseHeaders) = value
        """
        ...

    @property
    def Connection(self) -> HttpHeaderValueCollection:
        """ Get: Connection(self: HttpResponseHeaders) -> HttpHeaderValueCollection[str] """
        ...

    @property
    def ConnectionClose(self) -> Nullable:
        """
        Get: ConnectionClose(self: HttpResponseHeaders) -> Nullable[bool]
        Set: ConnectionClose(self: HttpResponseHeaders) = value
        """
        ...

    @property
    def Date(self) -> Nullable:
        """
        Get: Date(self: HttpResponseHeaders) -> Nullable[DateTimeOffset]
        Set: Date(self: HttpResponseHeaders) = value
        """
        ...

    @property
    def ETag(self) -> EntityTagHeaderValue:
        """
        Get: ETag(self: HttpResponseHeaders) -> EntityTagHeaderValue
        Set: ETag(self: HttpResponseHeaders) = value
        """
        ...

    @property
    def Location(self) -> Uri:
        """
        Get: Location(self: HttpResponseHeaders) -> Uri
        Set: Location(self: HttpResponseHeaders) = value
        """
        ...

    @property
    def Pragma(self) -> HttpHeaderValueCollection:
        """ Get: Pragma(self: HttpResponseHeaders) -> HttpHeaderValueCollection[NameValueHeaderValue] """
        ...

    @property
    def ProxyAuthenticate(self) -> HttpHeaderValueCollection:
        """ Get: ProxyAuthenticate(self: HttpResponseHeaders) -> HttpHeaderValueCollection[AuthenticationHeaderValue] """
        ...

    @property
    def RetryAfter(self) -> RetryConditionHeaderValue:
        """
        Get: RetryAfter(self: HttpResponseHeaders) -> RetryConditionHeaderValue
        Set: RetryAfter(self: HttpResponseHeaders) = value
        """
        ...

    @property
    def Server(self) -> HttpHeaderValueCollection:
        """ Get: Server(self: HttpResponseHeaders) -> HttpHeaderValueCollection[ProductInfoHeaderValue] """
        ...

    @property
    def Trailer(self) -> HttpHeaderValueCollection:
        """ Get: Trailer(self: HttpResponseHeaders) -> HttpHeaderValueCollection[str] """
        ...

    @property
    def TransferEncoding(self) -> HttpHeaderValueCollection:
        """ Get: TransferEncoding(self: HttpResponseHeaders) -> HttpHeaderValueCollection[TransferCodingHeaderValue] """
        ...

    @property
    def TransferEncodingChunked(self) -> Nullable:
        """
        Get: TransferEncodingChunked(self: HttpResponseHeaders) -> Nullable[bool]
        Set: TransferEncodingChunked(self: HttpResponseHeaders) = value
        """
        ...

    @property
    def Upgrade(self) -> HttpHeaderValueCollection:
        """ Get: Upgrade(self: HttpResponseHeaders) -> HttpHeaderValueCollection[ProductHeaderValue] """
        ...

    @property
    def Vary(self) -> HttpHeaderValueCollection:
        """ Get: Vary(self: HttpResponseHeaders) -> HttpHeaderValueCollection[str] """
        ...

    @property
    def Via(self) -> HttpHeaderValueCollection:
        """ Get: Via(self: HttpResponseHeaders) -> HttpHeaderValueCollection[ViaHeaderValue] """
        ...

    @property
    def Warning(self) -> HttpHeaderValueCollection:
        """ Get: Warning(self: HttpResponseHeaders) -> HttpHeaderValueCollection[WarningHeaderValue] """
        ...

    @property
    def WwwAuthenticate(self) -> HttpHeaderValueCollection:
        """ Get: WwwAuthenticate(self: HttpResponseHeaders) -> HttpHeaderValueCollection[AuthenticationHeaderValue] """
        ...



class MediaTypeHeaderValue(ICloneable): # skipped bases: <type 'object'>
    """ MediaTypeHeaderValue(mediaType: str) """
    @property
    def CharSet(self) -> str:
        """
        Get: CharSet(self: MediaTypeHeaderValue) -> str
        Set: CharSet(self: MediaTypeHeaderValue) = value
        """
        ...

    @property
    def MediaType(self) -> str:
        """
        Get: MediaType(self: MediaTypeHeaderValue) -> str
        Set: MediaType(self: MediaTypeHeaderValue) = value
        """
        ...

    @property
    def Parameters(self) -> ICollection:
        """ Get: Parameters(self: MediaTypeHeaderValue) -> ICollection[NameValueHeaderValue] """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: MediaTypeHeaderValue, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: MediaTypeHeaderValue) -> int """
        ...

    @staticmethod
    def Parse(input:str) -> MediaTypeHeaderValue:
        """ Parse(input: str) -> MediaTypeHeaderValue """
        ...

    def ToString(self) -> str:
        """ ToString(self: MediaTypeHeaderValue) -> str """
        ...

    @staticmethod
    def TryParse(input, parsedValue) -> Tuple_[bool, MediaTypeHeaderValue]:
        """ TryParse(input: str) -> (bool, MediaTypeHeaderValue) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MediaTypeWithQualityHeaderValue(MediaTypeHeaderValue): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    MediaTypeWithQualityHeaderValue(mediaType: str)
    MediaTypeWithQualityHeaderValue(mediaType: str, quality: float)
    """
    @property
    def Quality(self) -> Nullable:
        """
        Get: Quality(self: MediaTypeWithQualityHeaderValue) -> Nullable[float]
        Set: Quality(self: MediaTypeWithQualityHeaderValue) = value
        """
        ...



class NameValueHeaderValue(ICloneable): # skipped bases: <type 'object'>
    """
    NameValueHeaderValue(name: str)
    NameValueHeaderValue(name: str, value: str)
    """
    @property
    def Name(self) -> str:
        """ Get: Name(self: NameValueHeaderValue) -> str """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: NameValueHeaderValue) -> str
        Set: Value(self: NameValueHeaderValue) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: NameValueHeaderValue, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: NameValueHeaderValue) -> int """
        ...

    @staticmethod
    def Parse(input:str) -> NameValueHeaderValue:
        """ Parse(input: str) -> NameValueHeaderValue """
        ...

    def ToString(self) -> str:
        """ ToString(self: NameValueHeaderValue) -> str """
        ...

    @staticmethod
    def TryParse(input, parsedValue) -> Tuple_[bool, NameValueHeaderValue]:
        """ TryParse(input: str) -> (bool, NameValueHeaderValue) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class NameValueWithParametersHeaderValue(NameValueHeaderValue): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    NameValueWithParametersHeaderValue(name: str)
    NameValueWithParametersHeaderValue(name: str, value: str)
    """
    @property
    def Parameters(self) -> ICollection:
        """ Get: Parameters(self: NameValueWithParametersHeaderValue) -> ICollection[NameValueHeaderValue] """
        ...



class ProductHeaderValue(ICloneable): # skipped bases: <type 'object'>
    """
    ProductHeaderValue(name: str)
    ProductHeaderValue(name: str, version: str)
    """
    @property
    def Name(self) -> str:
        """ Get: Name(self: ProductHeaderValue) -> str """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: ProductHeaderValue) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: ProductHeaderValue, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ProductHeaderValue) -> int """
        ...

    @staticmethod
    def Parse(input:str) -> ProductHeaderValue:
        """ Parse(input: str) -> ProductHeaderValue """
        ...

    def ToString(self) -> str:
        """ ToString(self: ProductHeaderValue) -> str """
        ...

    @staticmethod
    def TryParse(input, parsedValue) -> Tuple_[bool, ProductHeaderValue]:
        """ TryParse(input: str) -> (bool, ProductHeaderValue) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ProductInfoHeaderValue(ICloneable): # skipped bases: <type 'object'>
    """
    ProductInfoHeaderValue(productName: str, productVersion: str)
    ProductInfoHeaderValue(product: ProductHeaderValue)
    ProductInfoHeaderValue(comment: str)
    """
    @property
    def Comment(self) -> str:
        """ Get: Comment(self: ProductInfoHeaderValue) -> str """
        ...

    @property
    def Product(self) -> ProductHeaderValue:
        """ Get: Product(self: ProductInfoHeaderValue) -> ProductHeaderValue """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: ProductInfoHeaderValue, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ProductInfoHeaderValue) -> int """
        ...

    @staticmethod
    def Parse(input:str) -> ProductInfoHeaderValue:
        """ Parse(input: str) -> ProductInfoHeaderValue """
        ...

    def ToString(self) -> str:
        """ ToString(self: ProductInfoHeaderValue) -> str """
        ...

    @staticmethod
    def TryParse(input, parsedValue) -> Tuple_[bool, ProductInfoHeaderValue]:
        """ TryParse(input: str) -> (bool, ProductInfoHeaderValue) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class RangeConditionHeaderValue(ICloneable): # skipped bases: <type 'object'>
    """
    RangeConditionHeaderValue(date: DateTimeOffset)
    RangeConditionHeaderValue(entityTag: EntityTagHeaderValue)
    RangeConditionHeaderValue(entityTag: str)
    """
    @property
    def Date(self) -> Nullable:
        """ Get: Date(self: RangeConditionHeaderValue) -> Nullable[DateTimeOffset] """
        ...

    @property
    def EntityTag(self) -> EntityTagHeaderValue:
        """ Get: EntityTag(self: RangeConditionHeaderValue) -> EntityTagHeaderValue """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: RangeConditionHeaderValue, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: RangeConditionHeaderValue) -> int """
        ...

    @staticmethod
    def Parse(input:str) -> RangeConditionHeaderValue:
        """ Parse(input: str) -> RangeConditionHeaderValue """
        ...

    def ToString(self) -> str:
        """ ToString(self: RangeConditionHeaderValue) -> str """
        ...

    @staticmethod
    def TryParse(input, parsedValue) -> Tuple_[bool, RangeConditionHeaderValue]:
        """ TryParse(input: str) -> (bool, RangeConditionHeaderValue) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class RangeHeaderValue(ICloneable): # skipped bases: <type 'object'>
    """
    RangeHeaderValue()
    RangeHeaderValue(from: Nullable[Int64], to: Nullable[Int64])
    """
    @property
    def Ranges(self) -> ICollection:
        """ Get: Ranges(self: RangeHeaderValue) -> ICollection[RangeItemHeaderValue] """
        ...

    @property
    def Unit(self) -> str:
        """
        Get: Unit(self: RangeHeaderValue) -> str
        Set: Unit(self: RangeHeaderValue) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: RangeHeaderValue, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: RangeHeaderValue) -> int """
        ...

    @staticmethod
    def Parse(input:str) -> RangeHeaderValue:
        """ Parse(input: str) -> RangeHeaderValue """
        ...

    def ToString(self) -> str:
        """ ToString(self: RangeHeaderValue) -> str """
        ...

    @staticmethod
    def TryParse(input, parsedValue) -> Tuple_[bool, RangeHeaderValue]:
        """ TryParse(input: str) -> (bool, RangeHeaderValue) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class RangeItemHeaderValue(ICloneable): # skipped bases: <type 'object'>
    """ RangeItemHeaderValue(from: Nullable[Int64], to: Nullable[Int64]) """
    @property
    def From(self) -> Nullable:
        """ Get: From(self: RangeItemHeaderValue) -> Nullable[Int64] """
        ...

    @property
    def To(self) -> Nullable:
        """ Get: To(self: RangeItemHeaderValue) -> Nullable[Int64] """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: RangeItemHeaderValue, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: RangeItemHeaderValue) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: RangeItemHeaderValue) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class RetryConditionHeaderValue(ICloneable): # skipped bases: <type 'object'>
    """
    RetryConditionHeaderValue(date: DateTimeOffset)
    RetryConditionHeaderValue(delta: TimeSpan)
    """
    @property
    def Date(self) -> Nullable:
        """ Get: Date(self: RetryConditionHeaderValue) -> Nullable[DateTimeOffset] """
        ...

    @property
    def Delta(self) -> Nullable:
        """ Get: Delta(self: RetryConditionHeaderValue) -> Nullable[TimeSpan] """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: RetryConditionHeaderValue, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: RetryConditionHeaderValue) -> int """
        ...

    @staticmethod
    def Parse(input:str) -> RetryConditionHeaderValue:
        """ Parse(input: str) -> RetryConditionHeaderValue """
        ...

    def ToString(self) -> str:
        """ ToString(self: RetryConditionHeaderValue) -> str """
        ...

    @staticmethod
    def TryParse(input, parsedValue) -> Tuple_[bool, RetryConditionHeaderValue]:
        """ TryParse(input: str) -> (bool, RetryConditionHeaderValue) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class StringWithQualityHeaderValue(ICloneable): # skipped bases: <type 'object'>
    """
    StringWithQualityHeaderValue(value: str)
    StringWithQualityHeaderValue(value: str, quality: float)
    """
    @property
    def Quality(self) -> Nullable:
        """ Get: Quality(self: StringWithQualityHeaderValue) -> Nullable[float] """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: StringWithQualityHeaderValue) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: StringWithQualityHeaderValue, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: StringWithQualityHeaderValue) -> int """
        ...

    @staticmethod
    def Parse(input:str) -> StringWithQualityHeaderValue:
        """ Parse(input: str) -> StringWithQualityHeaderValue """
        ...

    def ToString(self) -> str:
        """ ToString(self: StringWithQualityHeaderValue) -> str """
        ...

    @staticmethod
    def TryParse(input, parsedValue) -> Tuple_[bool, StringWithQualityHeaderValue]:
        """ TryParse(input: str) -> (bool, StringWithQualityHeaderValue) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TransferCodingHeaderValue(ICloneable): # skipped bases: <type 'object'>
    """ TransferCodingHeaderValue(value: str) """
    @property
    def Parameters(self) -> ICollection:
        """ Get: Parameters(self: TransferCodingHeaderValue) -> ICollection[NameValueHeaderValue] """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: TransferCodingHeaderValue) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: TransferCodingHeaderValue, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: TransferCodingHeaderValue) -> int """
        ...

    @staticmethod
    def Parse(input:str) -> TransferCodingHeaderValue:
        """ Parse(input: str) -> TransferCodingHeaderValue """
        ...

    def ToString(self) -> str:
        """ ToString(self: TransferCodingHeaderValue) -> str """
        ...

    @staticmethod
    def TryParse(input, parsedValue) -> Tuple_[bool, TransferCodingHeaderValue]:
        """ TryParse(input: str) -> (bool, TransferCodingHeaderValue) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TransferCodingWithQualityHeaderValue(TransferCodingHeaderValue): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    TransferCodingWithQualityHeaderValue(value: str)
    TransferCodingWithQualityHeaderValue(value: str, quality: float)
    """
    @property
    def Quality(self) -> Nullable:
        """
        Get: Quality(self: TransferCodingWithQualityHeaderValue) -> Nullable[float]
        Set: Quality(self: TransferCodingWithQualityHeaderValue) = value
        """
        ...



class ViaHeaderValue(ICloneable): # skipped bases: <type 'object'>
    """
    ViaHeaderValue(protocolVersion: str, receivedBy: str)
    ViaHeaderValue(protocolVersion: str, receivedBy: str, protocolName: str)
    ViaHeaderValue(protocolVersion: str, receivedBy: str, protocolName: str, comment: str)
    """
    @property
    def Comment(self) -> str:
        """ Get: Comment(self: ViaHeaderValue) -> str """
        ...

    @property
    def ProtocolName(self) -> str:
        """ Get: ProtocolName(self: ViaHeaderValue) -> str """
        ...

    @property
    def ProtocolVersion(self) -> str:
        """ Get: ProtocolVersion(self: ViaHeaderValue) -> str """
        ...

    @property
    def ReceivedBy(self) -> str:
        """ Get: ReceivedBy(self: ViaHeaderValue) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: ViaHeaderValue, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ViaHeaderValue) -> int """
        ...

    @staticmethod
    def Parse(input:str) -> ViaHeaderValue:
        """ Parse(input: str) -> ViaHeaderValue """
        ...

    def ToString(self) -> str:
        """ ToString(self: ViaHeaderValue) -> str """
        ...

    @staticmethod
    def TryParse(input, parsedValue) -> Tuple_[bool, ViaHeaderValue]:
        """ TryParse(input: str) -> (bool, ViaHeaderValue) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class WarningHeaderValue(ICloneable): # skipped bases: <type 'object'>
    """
    WarningHeaderValue(code: int, agent: str, text: str)
    WarningHeaderValue(code: int, agent: str, text: str, date: DateTimeOffset)
    """
    @property
    def Agent(self) -> str:
        """ Get: Agent(self: WarningHeaderValue) -> str """
        ...

    @property
    def Code(self) -> int:
        """ Get: Code(self: WarningHeaderValue) -> int """
        ...

    @property
    def Date(self) -> Nullable:
        """ Get: Date(self: WarningHeaderValue) -> Nullable[DateTimeOffset] """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: WarningHeaderValue) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: WarningHeaderValue, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: WarningHeaderValue) -> int """
        ...

    @staticmethod
    def Parse(input:str) -> WarningHeaderValue:
        """ Parse(input: str) -> WarningHeaderValue """
        ...

    def ToString(self) -> str:
        """ ToString(self: WarningHeaderValue) -> str """
        ...

    @staticmethod
    def TryParse(input, parsedValue) -> Tuple_[bool, WarningHeaderValue]:
        """ TryParse(input: str) -> (bool, WarningHeaderValue) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


