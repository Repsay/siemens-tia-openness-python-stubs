# encoding: utf-8
# module System.Net.Mime calls itself Mime
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import DateTime, Enum, Int64

from System.Collections.Specialized import StringDictionary

"""The following names are not found in the module: field#
"""

# no functions
# classes

class ContentDisposition: # skipped bases: <type 'object'>, <type 'object'>
    """
    ContentDisposition()
    ContentDisposition(disposition: str)
    """
    @property
    def CreationDate(self) -> DateTime:
        """
        Get: CreationDate(self: ContentDisposition) -> DateTime
        Set: CreationDate(self: ContentDisposition) = value
        """
        ...

    @property
    def DispositionType(self) -> str:
        """
        Get: DispositionType(self: ContentDisposition) -> str
        Set: DispositionType(self: ContentDisposition) = value
        """
        ...

    @property
    def FileName(self) -> str:
        """
        Get: FileName(self: ContentDisposition) -> str
        Set: FileName(self: ContentDisposition) = value
        """
        ...

    @property
    def Inline(self) -> bool:
        """
        Get: Inline(self: ContentDisposition) -> bool
        Set: Inline(self: ContentDisposition) = value
        """
        ...

    @property
    def ModificationDate(self) -> DateTime:
        """
        Get: ModificationDate(self: ContentDisposition) -> DateTime
        Set: ModificationDate(self: ContentDisposition) = value
        """
        ...

    @property
    def Parameters(self) -> StringDictionary:
        """ Get: Parameters(self: ContentDisposition) -> StringDictionary """
        ...

    @property
    def ReadDate(self) -> DateTime:
        """
        Get: ReadDate(self: ContentDisposition) -> DateTime
        Set: ReadDate(self: ContentDisposition) = value
        """
        ...

    @property
    def Size(self) -> Int64:
        """
        Get: Size(self: ContentDisposition) -> Int64
        Set: Size(self: ContentDisposition) = value
        """
        ...


    def Equals(self, rparam:object) -> bool:
        """ Equals(self: ContentDisposition, rparam: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ContentDisposition) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: ContentDisposition) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ContentType: # skipped bases: <type 'object'>, <type 'object'>
    """
    ContentType()
    ContentType(contentType: str)
    """
    @property
    def Boundary(self) -> str:
        """
        Get: Boundary(self: ContentType) -> str
        Set: Boundary(self: ContentType) = value
        """
        ...

    @property
    def CharSet(self) -> str:
        """
        Get: CharSet(self: ContentType) -> str
        Set: CharSet(self: ContentType) = value
        """
        ...

    @property
    def MediaType(self) -> str:
        """
        Get: MediaType(self: ContentType) -> str
        Set: MediaType(self: ContentType) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ContentType) -> str
        Set: Name(self: ContentType) = value
        """
        ...

    @property
    def Parameters(self) -> StringDictionary:
        """ Get: Parameters(self: ContentType) -> StringDictionary """
        ...


    def Equals(self, rparam:object) -> bool:
        """ Equals(self: ContentType, rparam: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ContentType) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: ContentType) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DispositionTypeNames: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Attachment: str = ...
    Inline: str = ...
    __all__: list = ...


class MediaTypeNames: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Application(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Image(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Text(self, *args): #cannot find CLR method
        """ no doc """
        ...

    __all__: list = ...


class TransferEncoding(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TransferEncoding, values: Base64 (1), EightBit (3), QuotedPrintable (0), SevenBit (2), Unknown (-1) """
    Base64: TransferEncoding = ...
    EightBit: TransferEncoding = ...
    QuotedPrintable: TransferEncoding = ...
    SevenBit: TransferEncoding = ...
    Unknown: TransferEncoding = ...
    value__ = ...


