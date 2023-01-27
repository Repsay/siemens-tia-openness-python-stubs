# encoding: utf-8
# module System.IO.Compression calls itself Compression
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.IO.Compression.FileSystem, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.IO.Compression, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import DateTimeOffset, Enum, IDisposable, Int64

from System.Collections.ObjectModel import ReadOnlyCollection

from System.IO import Stream

from System.Text import Encoding

from typing import Self

"""The following names are not found in the module: (ZipArchiveEntry, 
    ZipArchiveMode, field#)
"""

# no functions
# classes

class CompressionLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CompressionLevel, values: Fastest (1), NoCompression (2), Optimal (0) """
    Fastest: CompressionLevel = ...
    NoCompression: CompressionLevel = ...
    Optimal: CompressionLevel = ...
    value__ = ...


class CompressionMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CompressionMode, values: Compress (1), Decompress (0) """
    Compress: CompressionMode = ...
    Decompress: CompressionMode = ...
    value__ = ...


class DeflateStream(Stream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    DeflateStream(stream: Stream, mode: CompressionMode)
    DeflateStream(stream: Stream, mode: CompressionMode, leaveOpen: bool)
    DeflateStream(stream: Stream, compressionLevel: CompressionLevel)
    DeflateStream(stream: Stream, compressionLevel: CompressionLevel, leaveOpen: bool)
    """
    @property
    def BaseStream(self) -> Stream:
        """ Get: BaseStream(self: DeflateStream) -> Stream """
        ...


    def __new__(cls, stream:Stream, *__args:CompressionMode) -> Self:
        """
        __new__(cls: type, stream: Stream, mode: CompressionMode)
        __new__(cls: type, stream: Stream, mode: CompressionMode, leaveOpen: bool)
        __new__(cls: type, stream: Stream, compressionLevel: CompressionLevel)
        __new__(cls: type, stream: Stream, compressionLevel: CompressionLevel, leaveOpen: bool)
        """
        ...


class GZipStream(Stream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    GZipStream(stream: Stream, mode: CompressionMode)
    GZipStream(stream: Stream, mode: CompressionMode, leaveOpen: bool)
    GZipStream(stream: Stream, compressionLevel: CompressionLevel)
    GZipStream(stream: Stream, compressionLevel: CompressionLevel, leaveOpen: bool)
    """
    @property
    def BaseStream(self) -> Stream:
        """ Get: BaseStream(self: GZipStream) -> Stream """
        ...


    def __new__(cls, stream:Stream, *__args:CompressionMode) -> Self:
        """
        __new__(cls: type, stream: Stream, mode: CompressionMode)
        __new__(cls: type, stream: Stream, mode: CompressionMode, leaveOpen: bool)
        __new__(cls: type, stream: Stream, compressionLevel: CompressionLevel)
        __new__(cls: type, stream: Stream, compressionLevel: CompressionLevel, leaveOpen: bool)
        """
        ...


class ZipArchive(IDisposable): # skipped bases: <type 'object'>
    """
    ZipArchive(stream: Stream)
    ZipArchive(stream: Stream, mode: ZipArchiveMode)
    ZipArchive(stream: Stream, mode: ZipArchiveMode, leaveOpen: bool)
    ZipArchive(stream: Stream, mode: ZipArchiveMode, leaveOpen: bool, entryNameEncoding: Encoding)
    """
    @property
    def Entries(self) -> ReadOnlyCollection:
        """ Get: Entries(self: ZipArchive) -> ReadOnlyCollection[ZipArchiveEntry] """
        ...

    @property
    def Mode(self): # -> ZipArchiveMode
        """ Get: Mode(self: ZipArchive) -> ZipArchiveMode """
        ...


    def CreateEntry(self, entryName:str, compressionLevel:CompressionLevel = ...): # -> ZipArchiveEntry
        """
        CreateEntry(self: ZipArchive, entryName: str) -> ZipArchiveEntry
        CreateEntry(self: ZipArchive, entryName: str, compressionLevel: CompressionLevel) -> ZipArchiveEntry
        """
        ...

    def GetEntry(self, entryName:str): # -> ZipArchiveEntry
        """ GetEntry(self: ZipArchive, entryName: str) -> ZipArchiveEntry """
        ...


class ZipArchiveEntry: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Archive(self) -> ZipArchive:
        """ Get: Archive(self: ZipArchiveEntry) -> ZipArchive """
        ...

    @property
    def CompressedLength(self) -> Int64:
        """ Get: CompressedLength(self: ZipArchiveEntry) -> Int64 """
        ...

    @property
    def ExternalAttributes(self) -> int:
        """
        Get: ExternalAttributes(self: ZipArchiveEntry) -> int
        Set: ExternalAttributes(self: ZipArchiveEntry) = value
        """
        ...

    @property
    def FullName(self) -> str:
        """ Get: FullName(self: ZipArchiveEntry) -> str """
        ...

    @property
    def LastWriteTime(self) -> DateTimeOffset:
        """
        Get: LastWriteTime(self: ZipArchiveEntry) -> DateTimeOffset
        Set: LastWriteTime(self: ZipArchiveEntry) = value
        """
        ...

    @property
    def Length(self) -> Int64:
        """ Get: Length(self: ZipArchiveEntry) -> Int64 """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ZipArchiveEntry) -> str """
        ...


    def Delete(self): # -> 
        """ Delete(self: ZipArchiveEntry) """
        ...

    def Open(self) -> Stream:
        """ Open(self: ZipArchiveEntry) -> Stream """
        ...

    def ToString(self) -> str:
        """ ToString(self: ZipArchiveEntry) -> str """
        ...


class ZipArchiveMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ZipArchiveMode, values: Create (1), Read (0), Update (2) """
    Create: ZipArchiveMode = ...
    Read: ZipArchiveMode = ...
    Update: ZipArchiveMode = ...
    value__ = ...


class ZipFile: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateFromDirectory(sourceDirectoryName:str, destinationArchiveFileName:str, compressionLevel:CompressionLevel = ..., includeBaseDirectory:bool = ..., entryNameEncoding:Encoding = ...): # -> 
        """ CreateFromDirectory(sourceDirectoryName: str, destinationArchiveFileName: str)CreateFromDirectory(sourceDirectoryName: str, destinationArchiveFileName: str, compressionLevel: CompressionLevel, includeBaseDirectory: bool)CreateFromDirectory(sourceDirectoryName: str, destinationArchiveFileName: str, compressionLevel: CompressionLevel, includeBaseDirectory: bool, entryNameEncoding: Encoding) """
        ...

    @staticmethod
    def ExtractToDirectory(sourceArchiveFileName:str, destinationDirectoryName:str, entryNameEncoding:Encoding = ...): # -> 
        """ ExtractToDirectory(sourceArchiveFileName: str, destinationDirectoryName: str)ExtractToDirectory(sourceArchiveFileName: str, destinationDirectoryName: str, entryNameEncoding: Encoding) """
        ...

    @staticmethod
    def Open(archiveFileName:str, mode:ZipArchiveMode, entryNameEncoding:Encoding = ...) -> ZipArchive:
        """
        Open(archiveFileName: str, mode: ZipArchiveMode) -> ZipArchive
        Open(archiveFileName: str, mode: ZipArchiveMode, entryNameEncoding: Encoding) -> ZipArchive
        """
        ...

    @staticmethod
    def OpenRead(archiveFileName:str) -> ZipArchive:
        """ OpenRead(archiveFileName: str) -> ZipArchive """
        ...

    __all__: list = ...


class ZipFileExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateEntryFromFile(destination:ZipArchive, sourceFileName:str, entryName:str, compressionLevel:CompressionLevel = ...) -> ZipArchiveEntry:
        """
        CreateEntryFromFile(destination: ZipArchive, sourceFileName: str, entryName: str) -> ZipArchiveEntry
        CreateEntryFromFile(destination: ZipArchive, sourceFileName: str, entryName: str, compressionLevel: CompressionLevel) -> ZipArchiveEntry
        """
        ...

    @staticmethod
    def ExtractToDirectory(source:ZipArchive, destinationDirectoryName:str): # -> 
        """ ExtractToDirectory(source: ZipArchive, destinationDirectoryName: str) """
        ...

    @staticmethod
    def ExtractToFile(source:ZipArchiveEntry, destinationFileName:str, overwrite:bool = ...): # -> 
        """ ExtractToFile(source: ZipArchiveEntry, destinationFileName: str)ExtractToFile(source: ZipArchiveEntry, destinationFileName: str, overwrite: bool) """
        ...

    __all__: list = ...


