# encoding: utf-8
# module System.IO calls itself IO
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.IO.Compression.FileSystem, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.ServiceModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.IO.Log, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.IO.Compression, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Runtime.WindowsRuntime, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Win32.SafeHandles import SafeFileHandle

from System import (Array, ArraySegment, AsyncCallback, Byte, Char, DateTime, 
    Decimal, Enum, EventArgs, IAsyncResult, IDisposable, IFormatProvider, 
    Int16, Int64, IntPtr, MarshalByRefObject, MulticastDelegate, SByte, 
    Single, SystemException, UInt16, UInt32, UInt64)

from System.Collections import IEnumerable

from System.ComponentModel import (Component, ISupportInitialize, 
    ISynchronizeInvoke)

from System.EnterpriseServices import DescriptionAttribute

from System.Runtime.Serialization import (ISerializable, SerializationInfo, 
    StreamingContext)

from System.Security.AccessControl import (AccessControlSections, 
    DirectorySecurity, FileSecurity)

from System.Text import Encoding, StringBuilder

from System.Threading import CancellationToken

from System.Threading.Tasks import Task

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (Array[Char], BoundEvent, 
    IInputStream, IOutputStream, IRandomAccessStream, IStorageFile, 
    NullStream, NullStreamReader, NullTextReader, NullTextWriter, T, field#)
"""

# no functions
# classes

class BinaryReader(IDisposable): # skipped bases: <type 'object'>
    """
    BinaryReader(input: Stream)
    BinaryReader(input: Stream, encoding: Encoding)
    BinaryReader(input: Stream, encoding: Encoding, leaveOpen: bool)
    """
    @property
    def BaseStream(self) -> Stream:
        """ Get: BaseStream(self: BinaryReader) -> Stream """
        ...


    def Close(self): # -> 
        """ Close(self: BinaryReader) """
        ...

    def FillBuffer(self, *args): #cannot find CLR method
        """ FillBuffer(self: BinaryReader, numBytes: int) """
        ...

    def PeekChar(self) -> int:
        """ PeekChar(self: BinaryReader) -> int """
        ...

    def Read(self, buffer:Array = ..., index:int = ..., count:int = ...) -> int:
        """
        Read(self: BinaryReader) -> int
        Read(self: BinaryReader, buffer: Array[Char], index: int, count: int) -> int
        Read(self: BinaryReader, buffer: Array[Byte], index: int, count: int) -> int
        """
        ...

    def Read7BitEncodedInt(self, *args): #cannot find CLR method
        """ Read7BitEncodedInt(self: BinaryReader) -> int """
        ...

    def ReadBoolean(self) -> bool:
        """ ReadBoolean(self: BinaryReader) -> bool """
        ...

    def ReadByte(self) -> Byte:
        """ ReadByte(self: BinaryReader) -> Byte """
        ...

    def ReadBytes(self, count:int) -> Array:
        """ ReadBytes(self: BinaryReader, count: int) -> Array[Byte] """
        ...

    def ReadChar(self) -> Char:
        """ ReadChar(self: BinaryReader) -> Char """
        ...

    def ReadChars(self, count:int) -> Array:
        """ ReadChars(self: BinaryReader, count: int) -> Array[Char] """
        ...

    def ReadDecimal(self) -> Decimal:
        """ ReadDecimal(self: BinaryReader) -> Decimal """
        ...

    def ReadDouble(self) -> float:
        """ ReadDouble(self: BinaryReader) -> float """
        ...

    def ReadInt16(self) -> Int16:
        """ ReadInt16(self: BinaryReader) -> Int16 """
        ...

    def ReadInt32(self) -> int:
        """ ReadInt32(self: BinaryReader) -> int """
        ...

    def ReadInt64(self) -> Int64:
        """ ReadInt64(self: BinaryReader) -> Int64 """
        ...

    def ReadSByte(self) -> SByte:
        """ ReadSByte(self: BinaryReader) -> SByte """
        ...

    def ReadSingle(self) -> Single:
        """ ReadSingle(self: BinaryReader) -> Single """
        ...

    def ReadString(self) -> str:
        """ ReadString(self: BinaryReader) -> str """
        ...

    def ReadUInt16(self) -> UInt16:
        """ ReadUInt16(self: BinaryReader) -> UInt16 """
        ...

    def ReadUInt32(self) -> UInt32:
        """ ReadUInt32(self: BinaryReader) -> UInt32 """
        ...

    def ReadUInt64(self) -> UInt64:
        """ ReadUInt64(self: BinaryReader) -> UInt64 """
        ...


class BinaryWriter(IDisposable): # skipped bases: <type 'object'>
    """
    BinaryWriter(output: Stream)
    BinaryWriter(output: Stream, encoding: Encoding)
    BinaryWriter(output: Stream, encoding: Encoding, leaveOpen: bool)
    """
    @property
    def BaseStream(self) -> Stream:
        """ Get: BaseStream(self: BinaryWriter) -> Stream """
        ...


    def Close(self): # -> 
        """ Close(self: BinaryWriter) """
        ...

    def Flush(self): # -> 
        """ Flush(self: BinaryWriter) """
        ...

    def Seek(self, offset:int, origin:SeekOrigin) -> Int64:
        """ Seek(self: BinaryWriter, offset: int, origin: SeekOrigin) -> Int64 """
        ...

    def Write(self, *__args:bool): # -> 
        """ Write(self: BinaryWriter, value: bool)Write(self: BinaryWriter, value: UInt64)Write(self: BinaryWriter, value: Int64)Write(self: BinaryWriter, value: UInt32)Write(self: BinaryWriter, value: int)Write(self: BinaryWriter, value: UInt16)Write(self: BinaryWriter, value: Int16)Write(self: BinaryWriter, value: Decimal)Write(self: BinaryWriter, value: float)Write(self: BinaryWriter, chars: Array[Char], index: int, count: int)Write(self: BinaryWriter, chars: Array[Char])Write(self: BinaryWriter, ch: Char)Write(self: BinaryWriter, buffer: Array[Byte], index: int, count: int)Write(self: BinaryWriter, buffer: Array[Byte])Write(self: BinaryWriter, value: SByte)Write(self: BinaryWriter, value: Byte)Write(self: BinaryWriter, value: Single)Write(self: BinaryWriter, value: str) """
        ...

    def Write7BitEncodedInt(self, *args): #cannot find CLR method
        """ Write7BitEncodedInt(self: BinaryWriter, value: int) """
        ...

    Null: BinaryWriter = ...
    OutStream = ...


class Stream(IDisposable, MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CanRead(self) -> bool:
        """ Get: CanRead(self: Stream) -> bool """
        ...

    @property
    def CanSeek(self) -> bool:
        """ Get: CanSeek(self: Stream) -> bool """
        ...

    @property
    def CanTimeout(self) -> bool:
        """ Get: CanTimeout(self: Stream) -> bool """
        ...

    @property
    def CanWrite(self) -> bool:
        """ Get: CanWrite(self: Stream) -> bool """
        ...

    @property
    def Length(self) -> Int64:
        """ Get: Length(self: Stream) -> Int64 """
        ...

    @property
    def Position(self) -> Int64:
        """
        Get: Position(self: Stream) -> Int64
        Set: Position(self: Stream) = value
        """
        ...

    @property
    def ReadTimeout(self) -> int:
        """
        Get: ReadTimeout(self: Stream) -> int
        Set: ReadTimeout(self: Stream) = value
        """
        ...

    @property
    def WriteTimeout(self) -> int:
        """
        Get: WriteTimeout(self: Stream) -> int
        Set: WriteTimeout(self: Stream) = value
        """
        ...


    def BeginRead(self, buffer:Array, offset:int, count:int, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginRead(self: Stream, buffer: Array[Byte], offset: int, count: int, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginWrite(self, buffer:Array, offset:int, count:int, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginWrite(self: Stream, buffer: Array[Byte], offset: int, count: int, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def Close(self): # -> 
        """ Close(self: Stream) """
        ...

    def CopyTo(self, destination:Stream, bufferSize:int = ...): # -> 
        """ CopyTo(self: Stream, destination: Stream)CopyTo(self: Stream, destination: Stream, bufferSize: int) """
        ...

    def CopyToAsync(self, destination:Stream, bufferSize:int = ..., cancellationToken:CancellationToken = ...) -> Task:
        """
        CopyToAsync(self: Stream, destination: Stream, bufferSize: int, cancellationToken: CancellationToken) -> Task
        CopyToAsync(self: Stream, destination: Stream) -> Task
        CopyToAsync(self: Stream, destination: Stream, bufferSize: int) -> Task
        """
        ...

    def CreateWaitHandle(self, *args): #cannot find CLR method
        """ CreateWaitHandle(self: Stream) -> WaitHandle """
        ...

    def EndRead(self, asyncResult:IAsyncResult) -> int:
        """ EndRead(self: Stream, asyncResult: IAsyncResult) -> int """
        ...

    def EndWrite(self, asyncResult:IAsyncResult): # -> 
        """ EndWrite(self: Stream, asyncResult: IAsyncResult) """
        ...

    def Flush(self): # -> 
        """ Flush(self: Stream) """
        ...

    def FlushAsync(self, cancellationToken:CancellationToken = ...) -> Task:
        """
        FlushAsync(self: Stream) -> Task
        FlushAsync(self: Stream, cancellationToken: CancellationToken) -> Task
        """
        ...

    def ObjectInvariant(self, *args): #cannot find CLR method
        """ ObjectInvariant(self: Stream) """
        ...

    def Read(self, buffer, offset, count) -> Tuple_[int, Array]:
        """ Read(self: Stream, offset: int, count: int) -> (int, Array[Byte]) """
        ...

    def ReadAsync(self, buffer:Array, offset:int, count:int, cancellationToken:CancellationToken = ...) -> Task:
        """
        ReadAsync(self: Stream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task[int]
        ReadAsync(self: Stream, buffer: Array[Byte], offset: int, count: int) -> Task[int]
        """
        ...

    def ReadByte(self) -> int:
        """ ReadByte(self: Stream) -> int """
        ...

    def Seek(self, offset:Int64, origin:SeekOrigin) -> Int64:
        """ Seek(self: Stream, offset: Int64, origin: SeekOrigin) -> Int64 """
        ...

    def SetLength(self, value:Int64): # -> 
        """ SetLength(self: Stream, value: Int64) """
        ...

    @staticmethod
    def Synchronized(stream:Stream) -> Stream:
        """ Synchronized(stream: Stream) -> Stream """
        ...

    def Write(self, buffer:Array, offset:int, count:int): # -> 
        """ Write(self: Stream, buffer: Array[Byte], offset: int, count: int) """
        ...

    def WriteAsync(self, buffer:Array, offset:int, count:int, cancellationToken:CancellationToken = ...) -> Task:
        """
        WriteAsync(self: Stream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task
        WriteAsync(self: Stream, buffer: Array[Byte], offset: int, count: int) -> Task
        """
        ...

    def WriteByte(self, value:Byte): # -> 
        """ WriteByte(self: Stream, value: Byte) """
        ...

    Null = ...


class BufferedStream(Stream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    BufferedStream(stream: Stream)
    BufferedStream(stream: Stream, bufferSize: int)
    """
    def __new__(cls, stream:Stream, bufferSize:int = ...) -> Self:
        """
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, bufferSize: int)
        """
        ...


class Directory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateDirectory(path:str, directorySecurity:DirectorySecurity = ...) -> DirectoryInfo:
        """
        CreateDirectory(path: str) -> DirectoryInfo
        CreateDirectory(path: str, directorySecurity: DirectorySecurity) -> DirectoryInfo
        """
        ...

    @staticmethod
    def Delete(path:str, recursive:bool = ...): # -> 
        """ Delete(path: str)Delete(path: str, recursive: bool) """
        ...

    @staticmethod
    def EnumerateDirectories(path:str, searchPattern:str = ..., searchOption:SearchOption = ...) -> IEnumerable:
        """
        EnumerateDirectories(path: str, searchPattern: str) -> IEnumerable[str]
        EnumerateDirectories(path: str, searchPattern: str, searchOption: SearchOption) -> IEnumerable[str]
        EnumerateDirectories(path: str) -> IEnumerable[str]
        """
        ...

    @staticmethod
    def EnumerateFiles(path:str, searchPattern:str = ..., searchOption:SearchOption = ...) -> IEnumerable:
        """
        EnumerateFiles(path: str, searchPattern: str) -> IEnumerable[str]
        EnumerateFiles(path: str, searchPattern: str, searchOption: SearchOption) -> IEnumerable[str]
        EnumerateFiles(path: str) -> IEnumerable[str]
        """
        ...

    @staticmethod
    def EnumerateFileSystemEntries(path:str, searchPattern:str = ..., searchOption:SearchOption = ...) -> IEnumerable:
        """
        EnumerateFileSystemEntries(path: str, searchPattern: str) -> IEnumerable[str]
        EnumerateFileSystemEntries(path: str, searchPattern: str, searchOption: SearchOption) -> IEnumerable[str]
        EnumerateFileSystemEntries(path: str) -> IEnumerable[str]
        """
        ...

    @staticmethod
    def Exists(path:str) -> bool:
        """ Exists(path: str) -> bool """
        ...

    @staticmethod
    def GetAccessControl(path:str, includeSections:AccessControlSections = ...) -> DirectorySecurity:
        """
        GetAccessControl(path: str) -> DirectorySecurity
        GetAccessControl(path: str, includeSections: AccessControlSections) -> DirectorySecurity
        """
        ...

    @staticmethod
    def GetCreationTime(path:str) -> DateTime:
        """ GetCreationTime(path: str) -> DateTime """
        ...

    @staticmethod
    def GetCreationTimeUtc(path:str) -> DateTime:
        """ GetCreationTimeUtc(path: str) -> DateTime """
        ...

    @staticmethod
    def GetCurrentDirectory() -> str:
        """ GetCurrentDirectory() -> str """
        ...

    @staticmethod
    def GetDirectories(path:str, searchPattern:str = ..., searchOption:SearchOption = ...) -> Array:
        """
        GetDirectories(path: str, searchPattern: str) -> Array[str]
        GetDirectories(path: str, searchPattern: str, searchOption: SearchOption) -> Array[str]
        GetDirectories(path: str) -> Array[str]
        """
        ...

    @staticmethod
    def GetDirectoryRoot(path:str) -> str:
        """ GetDirectoryRoot(path: str) -> str """
        ...

    @staticmethod
    def GetFiles(path:str, searchPattern:str = ..., searchOption:SearchOption = ...) -> Array:
        """
        GetFiles(path: str, searchPattern: str) -> Array[str]
        GetFiles(path: str, searchPattern: str, searchOption: SearchOption) -> Array[str]
        GetFiles(path: str) -> Array[str]
        """
        ...

    @staticmethod
    def GetFileSystemEntries(path:str, searchPattern:str = ..., searchOption:SearchOption = ...) -> Array:
        """
        GetFileSystemEntries(path: str, searchPattern: str) -> Array[str]
        GetFileSystemEntries(path: str, searchPattern: str, searchOption: SearchOption) -> Array[str]
        GetFileSystemEntries(path: str) -> Array[str]
        """
        ...

    @staticmethod
    def GetLastAccessTime(path:str) -> DateTime:
        """ GetLastAccessTime(path: str) -> DateTime """
        ...

    @staticmethod
    def GetLastAccessTimeUtc(path:str) -> DateTime:
        """ GetLastAccessTimeUtc(path: str) -> DateTime """
        ...

    @staticmethod
    def GetLastWriteTime(path:str) -> DateTime:
        """ GetLastWriteTime(path: str) -> DateTime """
        ...

    @staticmethod
    def GetLastWriteTimeUtc(path:str) -> DateTime:
        """ GetLastWriteTimeUtc(path: str) -> DateTime """
        ...

    @staticmethod
    def GetLogicalDrives() -> Array:
        """ GetLogicalDrives() -> Array[str] """
        ...

    @staticmethod
    def GetParent(path:str) -> DirectoryInfo:
        """ GetParent(path: str) -> DirectoryInfo """
        ...

    @staticmethod
    def Move(sourceDirName:str, destDirName:str): # -> 
        """ Move(sourceDirName: str, destDirName: str) """
        ...

    @staticmethod
    def SetAccessControl(path:str, directorySecurity:DirectorySecurity): # -> 
        """ SetAccessControl(path: str, directorySecurity: DirectorySecurity) """
        ...

    @staticmethod
    def SetCreationTime(path:str, creationTime:DateTime): # -> 
        """ SetCreationTime(path: str, creationTime: DateTime) """
        ...

    @staticmethod
    def SetCreationTimeUtc(path:str, creationTimeUtc:DateTime): # -> 
        """ SetCreationTimeUtc(path: str, creationTimeUtc: DateTime) """
        ...

    @staticmethod
    def SetCurrentDirectory(path:str): # -> 
        """ SetCurrentDirectory(path: str) """
        ...

    @staticmethod
    def SetLastAccessTime(path:str, lastAccessTime:DateTime): # -> 
        """ SetLastAccessTime(path: str, lastAccessTime: DateTime) """
        ...

    @staticmethod
    def SetLastAccessTimeUtc(path:str, lastAccessTimeUtc:DateTime): # -> 
        """ SetLastAccessTimeUtc(path: str, lastAccessTimeUtc: DateTime) """
        ...

    @staticmethod
    def SetLastWriteTime(path:str, lastWriteTime:DateTime): # -> 
        """ SetLastWriteTime(path: str, lastWriteTime: DateTime) """
        ...

    @staticmethod
    def SetLastWriteTimeUtc(path:str, lastWriteTimeUtc:DateTime): # -> 
        """ SetLastWriteTimeUtc(path: str, lastWriteTimeUtc: DateTime) """
        ...

    __all__: list = ...


class FileSystemInfo(MarshalByRefObject, ISerializable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> FileAttributes:
        """
        Get: Attributes(self: FileSystemInfo) -> FileAttributes
        Set: Attributes(self: FileSystemInfo) = value
        """
        ...

    @property
    def CreationTime(self) -> DateTime:
        """
        Get: CreationTime(self: FileSystemInfo) -> DateTime
        Set: CreationTime(self: FileSystemInfo) = value
        """
        ...

    @property
    def CreationTimeUtc(self) -> DateTime:
        """
        Get: CreationTimeUtc(self: FileSystemInfo) -> DateTime
        Set: CreationTimeUtc(self: FileSystemInfo) = value
        """
        ...

    @property
    def Exists(self) -> bool:
        """ Get: Exists(self: FileSystemInfo) -> bool """
        ...

    @property
    def Extension(self) -> str:
        """ Get: Extension(self: FileSystemInfo) -> str """
        ...

    @property
    def FullName(self) -> str:
        """ Get: FullName(self: FileSystemInfo) -> str """
        ...

    @property
    def LastAccessTime(self) -> DateTime:
        """
        Get: LastAccessTime(self: FileSystemInfo) -> DateTime
        Set: LastAccessTime(self: FileSystemInfo) = value
        """
        ...

    @property
    def LastAccessTimeUtc(self) -> DateTime:
        """
        Get: LastAccessTimeUtc(self: FileSystemInfo) -> DateTime
        Set: LastAccessTimeUtc(self: FileSystemInfo) = value
        """
        ...

    @property
    def LastWriteTime(self) -> DateTime:
        """
        Get: LastWriteTime(self: FileSystemInfo) -> DateTime
        Set: LastWriteTime(self: FileSystemInfo) = value
        """
        ...

    @property
    def LastWriteTimeUtc(self) -> DateTime:
        """
        Get: LastWriteTimeUtc(self: FileSystemInfo) -> DateTime
        Set: LastWriteTimeUtc(self: FileSystemInfo) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: FileSystemInfo) -> str """
        ...


    def Delete(self): # -> 
        """ Delete(self: FileSystemInfo) """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: FileSystemInfo) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        ...

    FullPath = ...
    OriginalPath = ...


class DirectoryInfo(FileSystemInfo): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ DirectoryInfo(path: str) """
    @property
    def Parent(self) -> DirectoryInfo:
        """ Get: Parent(self: DirectoryInfo) -> DirectoryInfo """
        ...

    @property
    def Root(self) -> DirectoryInfo:
        """ Get: Root(self: DirectoryInfo) -> DirectoryInfo """
        ...


    def Create(self, directorySecurity:DirectorySecurity = ...): # -> 
        """ Create(self: DirectoryInfo)Create(self: DirectoryInfo, directorySecurity: DirectorySecurity) """
        ...

    def CreateSubdirectory(self, path:str, directorySecurity:DirectorySecurity = ...) -> DirectoryInfo:
        """
        CreateSubdirectory(self: DirectoryInfo, path: str) -> DirectoryInfo
        CreateSubdirectory(self: DirectoryInfo, path: str, directorySecurity: DirectorySecurity) -> DirectoryInfo
        """
        ...

    def EnumerateDirectories(self, searchPattern:str = ..., searchOption:SearchOption = ...) -> IEnumerable:
        """
        EnumerateDirectories(self: DirectoryInfo) -> IEnumerable[DirectoryInfo]
        EnumerateDirectories(self: DirectoryInfo, searchPattern: str) -> IEnumerable[DirectoryInfo]
        EnumerateDirectories(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> IEnumerable[DirectoryInfo]
        """
        ...

    def EnumerateFiles(self, searchPattern:str = ..., searchOption:SearchOption = ...) -> IEnumerable:
        """
        EnumerateFiles(self: DirectoryInfo) -> IEnumerable[FileInfo]
        EnumerateFiles(self: DirectoryInfo, searchPattern: str) -> IEnumerable[FileInfo]
        EnumerateFiles(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> IEnumerable[FileInfo]
        """
        ...

    def EnumerateFileSystemInfos(self, searchPattern:str = ..., searchOption:SearchOption = ...) -> IEnumerable:
        """
        EnumerateFileSystemInfos(self: DirectoryInfo) -> IEnumerable[FileSystemInfo]
        EnumerateFileSystemInfos(self: DirectoryInfo, searchPattern: str) -> IEnumerable[FileSystemInfo]
        EnumerateFileSystemInfos(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> IEnumerable[FileSystemInfo]
        """
        ...

    def GetAccessControl(self, includeSections:AccessControlSections = ...) -> DirectorySecurity:
        """
        GetAccessControl(self: DirectoryInfo) -> DirectorySecurity
        GetAccessControl(self: DirectoryInfo, includeSections: AccessControlSections) -> DirectorySecurity
        """
        ...

    def GetDirectories(self, searchPattern:str = ..., searchOption:SearchOption = ...) -> Array:
        """
        GetDirectories(self: DirectoryInfo) -> Array[DirectoryInfo]
        GetDirectories(self: DirectoryInfo, searchPattern: str) -> Array[DirectoryInfo]
        GetDirectories(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> Array[DirectoryInfo]
        """
        ...

    def GetFiles(self, searchPattern:str = ..., searchOption:SearchOption = ...) -> Array:
        """
        GetFiles(self: DirectoryInfo, searchPattern: str) -> Array[FileInfo]
        GetFiles(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> Array[FileInfo]
        GetFiles(self: DirectoryInfo) -> Array[FileInfo]
        """
        ...

    def GetFileSystemInfos(self, searchPattern:str = ..., searchOption:SearchOption = ...) -> Array:
        """
        GetFileSystemInfos(self: DirectoryInfo, searchPattern: str) -> Array[FileSystemInfo]
        GetFileSystemInfos(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> Array[FileSystemInfo]
        GetFileSystemInfos(self: DirectoryInfo) -> Array[FileSystemInfo]
        """
        ...

    def MoveTo(self, destDirName:str): # -> 
        """ MoveTo(self: DirectoryInfo, destDirName: str) """
        ...

    def SetAccessControl(self, directorySecurity:DirectorySecurity): # -> 
        """ SetAccessControl(self: DirectoryInfo, directorySecurity: DirectorySecurity) """
        ...

    def ToString(self) -> str:
        """ ToString(self: DirectoryInfo) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...

    FullPath = ...
    OriginalPath = ...


class IOException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    IOException()
    IOException(message: str)
    IOException(message: str, hresult: int)
    IOException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class DirectoryNotFoundException(IOException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DirectoryNotFoundException()
    DirectoryNotFoundException(message: str)
    DirectoryNotFoundException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class DriveInfo(ISerializable): # skipped bases: <type 'object'>
    """ DriveInfo(driveName: str) """
    @property
    def AvailableFreeSpace(self) -> Int64:
        """ Get: AvailableFreeSpace(self: DriveInfo) -> Int64 """
        ...

    @property
    def DriveFormat(self) -> str:
        """ Get: DriveFormat(self: DriveInfo) -> str """
        ...

    @property
    def DriveType(self) -> DriveType:
        """ Get: DriveType(self: DriveInfo) -> DriveType """
        ...

    @property
    def IsReady(self) -> bool:
        """ Get: IsReady(self: DriveInfo) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DriveInfo) -> str """
        ...

    @property
    def RootDirectory(self) -> DirectoryInfo:
        """ Get: RootDirectory(self: DriveInfo) -> DirectoryInfo """
        ...

    @property
    def TotalFreeSpace(self) -> Int64:
        """ Get: TotalFreeSpace(self: DriveInfo) -> Int64 """
        ...

    @property
    def TotalSize(self) -> Int64:
        """ Get: TotalSize(self: DriveInfo) -> Int64 """
        ...

    @property
    def VolumeLabel(self) -> str:
        """
        Get: VolumeLabel(self: DriveInfo) -> str
        Set: VolumeLabel(self: DriveInfo) = value
        """
        ...


    @staticmethod
    def GetDrives() -> Array:
        """ GetDrives() -> Array[DriveInfo] """
        ...

    def ToString(self) -> str:
        """ ToString(self: DriveInfo) -> str """
        ...


class DriveNotFoundException(IOException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DriveNotFoundException()
    DriveNotFoundException(message: str)
    DriveNotFoundException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class DriveType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DriveType, values: CDRom (5), Fixed (3), Network (4), NoRootDirectory (1), Ram (6), Removable (2), Unknown (0) """
    CDRom: DriveType = ...
    Fixed: DriveType = ...
    Network: DriveType = ...
    NoRootDirectory: DriveType = ...
    Ram: DriveType = ...
    Removable: DriveType = ...
    Unknown: DriveType = ...
    value__ = ...


class EndOfStreamException(IOException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    EndOfStreamException()
    EndOfStreamException(message: str)
    EndOfStreamException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ErrorEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ErrorEventArgs(exception: Exception) """
    def GetException(self) -> Exception:
        """ GetException(self: ErrorEventArgs) -> Exception """
        ...

    def __new__(cls, exception:Exception) -> Self:
        """ __new__(cls: type, exception: Exception) """
        ...


class ErrorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ErrorEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ErrorEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ErrorEventHandler, sender: object, e: ErrorEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ErrorEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ErrorEventArgs): # -> 
        """ Invoke(self: ErrorEventHandler, sender: object, e: ErrorEventArgs) """
        ...


class File: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AppendAllLines(path:str, contents:IEnumerable, encoding:Encoding = ...): # -> 
        """ AppendAllLines(path: str, contents: IEnumerable[str])AppendAllLines(path: str, contents: IEnumerable[str], encoding: Encoding) """
        ...

    @staticmethod
    def AppendAllText(path:str, contents:str, encoding:Encoding = ...): # -> 
        """ AppendAllText(path: str, contents: str)AppendAllText(path: str, contents: str, encoding: Encoding) """
        ...

    @staticmethod
    def AppendText(path:str) -> StreamWriter:
        """ AppendText(path: str) -> StreamWriter """
        ...

    @staticmethod
    def Copy(sourceFileName:str, destFileName:str, overwrite:bool = ...): # -> 
        """ Copy(sourceFileName: str, destFileName: str)Copy(sourceFileName: str, destFileName: str, overwrite: bool) """
        ...

    @staticmethod
    def Create(path:str, bufferSize:int = ..., options:FileOptions = ..., fileSecurity:FileSecurity = ...) -> FileStream:
        """
        Create(path: str) -> FileStream
        Create(path: str, bufferSize: int) -> FileStream
        Create(path: str, bufferSize: int, options: FileOptions) -> FileStream
        Create(path: str, bufferSize: int, options: FileOptions, fileSecurity: FileSecurity) -> FileStream
        """
        ...

    @staticmethod
    def CreateText(path:str) -> StreamWriter:
        """ CreateText(path: str) -> StreamWriter """
        ...

    @staticmethod
    def Decrypt(path:str): # -> 
        """ Decrypt(path: str) """
        ...

    @staticmethod
    def Delete(path:str): # -> 
        """ Delete(path: str) """
        ...

    @staticmethod
    def Encrypt(path:str): # -> 
        """ Encrypt(path: str) """
        ...

    @staticmethod
    def Exists(path:str) -> bool:
        """ Exists(path: str) -> bool """
        ...

    @staticmethod
    def GetAccessControl(path:str, includeSections:AccessControlSections = ...) -> FileSecurity:
        """
        GetAccessControl(path: str) -> FileSecurity
        GetAccessControl(path: str, includeSections: AccessControlSections) -> FileSecurity
        """
        ...

    @staticmethod
    def GetAttributes(path:str) -> FileAttributes:
        """ GetAttributes(path: str) -> FileAttributes """
        ...

    @staticmethod
    def GetCreationTime(path:str) -> DateTime:
        """ GetCreationTime(path: str) -> DateTime """
        ...

    @staticmethod
    def GetCreationTimeUtc(path:str) -> DateTime:
        """ GetCreationTimeUtc(path: str) -> DateTime """
        ...

    @staticmethod
    def GetLastAccessTime(path:str) -> DateTime:
        """ GetLastAccessTime(path: str) -> DateTime """
        ...

    @staticmethod
    def GetLastAccessTimeUtc(path:str) -> DateTime:
        """ GetLastAccessTimeUtc(path: str) -> DateTime """
        ...

    @staticmethod
    def GetLastWriteTime(path:str) -> DateTime:
        """ GetLastWriteTime(path: str) -> DateTime """
        ...

    @staticmethod
    def GetLastWriteTimeUtc(path:str) -> DateTime:
        """ GetLastWriteTimeUtc(path: str) -> DateTime """
        ...

    @staticmethod
    def Move(sourceFileName:str, destFileName:str): # -> 
        """ Move(sourceFileName: str, destFileName: str) """
        ...

    @staticmethod
    def Open(path:str, mode:FileMode, access:FileAccess = ..., share:FileShare = ...) -> FileStream:
        """
        Open(path: str, mode: FileMode) -> FileStream
        Open(path: str, mode: FileMode, access: FileAccess) -> FileStream
        Open(path: str, mode: FileMode, access: FileAccess, share: FileShare) -> FileStream
        """
        ...

    @staticmethod
    def OpenRead(path:str) -> FileStream:
        """ OpenRead(path: str) -> FileStream """
        ...

    @staticmethod
    def OpenText(path:str) -> StreamReader:
        """ OpenText(path: str) -> StreamReader """
        ...

    @staticmethod
    def OpenWrite(path:str) -> FileStream:
        """ OpenWrite(path: str) -> FileStream """
        ...

    @staticmethod
    def ReadAllBytes(path:str) -> Array:
        """ ReadAllBytes(path: str) -> Array[Byte] """
        ...

    @staticmethod
    def ReadAllLines(path:str, encoding:Encoding = ...) -> Array:
        """
        ReadAllLines(path: str) -> Array[str]
        ReadAllLines(path: str, encoding: Encoding) -> Array[str]
        """
        ...

    @staticmethod
    def ReadAllText(path:str, encoding:Encoding = ...) -> str:
        """
        ReadAllText(path: str) -> str
        ReadAllText(path: str, encoding: Encoding) -> str
        """
        ...

    @staticmethod
    def ReadLines(path:str, encoding:Encoding = ...) -> IEnumerable:
        """
        ReadLines(path: str) -> IEnumerable[str]
        ReadLines(path: str, encoding: Encoding) -> IEnumerable[str]
        """
        ...

    @staticmethod
    def Replace(sourceFileName:str, destinationFileName:str, destinationBackupFileName:str, ignoreMetadataErrors:bool = ...): # -> 
        """ Replace(sourceFileName: str, destinationFileName: str, destinationBackupFileName: str)Replace(sourceFileName: str, destinationFileName: str, destinationBackupFileName: str, ignoreMetadataErrors: bool) """
        ...

    @staticmethod
    def SetAccessControl(path:str, fileSecurity:FileSecurity): # -> 
        """ SetAccessControl(path: str, fileSecurity: FileSecurity) """
        ...

    @staticmethod
    def SetAttributes(path:str, fileAttributes:FileAttributes): # -> 
        """ SetAttributes(path: str, fileAttributes: FileAttributes) """
        ...

    @staticmethod
    def SetCreationTime(path:str, creationTime:DateTime): # -> 
        """ SetCreationTime(path: str, creationTime: DateTime) """
        ...

    @staticmethod
    def SetCreationTimeUtc(path:str, creationTimeUtc:DateTime): # -> 
        """ SetCreationTimeUtc(path: str, creationTimeUtc: DateTime) """
        ...

    @staticmethod
    def SetLastAccessTime(path:str, lastAccessTime:DateTime): # -> 
        """ SetLastAccessTime(path: str, lastAccessTime: DateTime) """
        ...

    @staticmethod
    def SetLastAccessTimeUtc(path:str, lastAccessTimeUtc:DateTime): # -> 
        """ SetLastAccessTimeUtc(path: str, lastAccessTimeUtc: DateTime) """
        ...

    @staticmethod
    def SetLastWriteTime(path:str, lastWriteTime:DateTime): # -> 
        """ SetLastWriteTime(path: str, lastWriteTime: DateTime) """
        ...

    @staticmethod
    def SetLastWriteTimeUtc(path:str, lastWriteTimeUtc:DateTime): # -> 
        """ SetLastWriteTimeUtc(path: str, lastWriteTimeUtc: DateTime) """
        ...

    @staticmethod
    def WriteAllBytes(path:str, bytes:Array): # -> 
        """ WriteAllBytes(path: str, bytes: Array[Byte]) """
        ...

    @staticmethod
    def WriteAllLines(path:str, contents:Array, encoding:Encoding = ...): # -> 
        """ WriteAllLines(path: str, contents: Array[str])WriteAllLines(path: str, contents: Array[str], encoding: Encoding)WriteAllLines(path: str, contents: IEnumerable[str])WriteAllLines(path: str, contents: IEnumerable[str], encoding: Encoding) """
        ...

    @staticmethod
    def WriteAllText(path:str, contents:str, encoding:Encoding = ...): # -> 
        """ WriteAllText(path: str, contents: str)WriteAllText(path: str, contents: str, encoding: Encoding) """
        ...

    __all__: list = ...


class FileAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) FileAccess, values: Read (1), ReadWrite (3), Write (2) """
    Read: FileAccess = ...
    ReadWrite: FileAccess = ...
    value__ = ...
    Write: FileAccess = ...


class FileAttributes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) FileAttributes, values: Archive (32), Compressed (2048), Device (64), Directory (16), Encrypted (16384), Hidden (2), IntegrityStream (32768), Normal (128), NoScrubData (131072), NotContentIndexed (8192), Offline (4096), ReadOnly (1), ReparsePoint (1024), SparseFile (512), System (4), Temporary (256) """
    Archive: FileAttributes = ...
    Compressed: FileAttributes = ...
    Device: FileAttributes = ...
    Directory: FileAttributes = ...
    Encrypted: FileAttributes = ...
    Hidden: FileAttributes = ...
    IntegrityStream: FileAttributes = ...
    Normal: FileAttributes = ...
    NoScrubData: FileAttributes = ...
    NotContentIndexed: FileAttributes = ...
    Offline: FileAttributes = ...
    ReadOnly: FileAttributes = ...
    ReparsePoint: FileAttributes = ...
    SparseFile: FileAttributes = ...
    System: FileAttributes = ...
    Temporary: FileAttributes = ...
    value__ = ...


class FileInfo(FileSystemInfo): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ FileInfo(fileName: str) """
    @property
    def Directory(self) -> DirectoryInfo:
        """ Get: Directory(self: FileInfo) -> DirectoryInfo """
        ...

    @property
    def DirectoryName(self) -> str:
        """ Get: DirectoryName(self: FileInfo) -> str """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """
        Get: IsReadOnly(self: FileInfo) -> bool
        Set: IsReadOnly(self: FileInfo) = value
        """
        ...

    @property
    def Length(self) -> Int64:
        """ Get: Length(self: FileInfo) -> Int64 """
        ...


    def AppendText(self) -> StreamWriter:
        """ AppendText(self: FileInfo) -> StreamWriter """
        ...

    def CopyTo(self, destFileName:str, overwrite:bool = ...) -> FileInfo:
        """
        CopyTo(self: FileInfo, destFileName: str) -> FileInfo
        CopyTo(self: FileInfo, destFileName: str, overwrite: bool) -> FileInfo
        """
        ...

    def Create(self) -> FileStream:
        """ Create(self: FileInfo) -> FileStream """
        ...

    def CreateText(self) -> StreamWriter:
        """ CreateText(self: FileInfo) -> StreamWriter """
        ...

    def Decrypt(self): # -> 
        """ Decrypt(self: FileInfo) """
        ...

    def Encrypt(self): # -> 
        """ Encrypt(self: FileInfo) """
        ...

    def GetAccessControl(self, includeSections:AccessControlSections = ...) -> FileSecurity:
        """
        GetAccessControl(self: FileInfo) -> FileSecurity
        GetAccessControl(self: FileInfo, includeSections: AccessControlSections) -> FileSecurity
        """
        ...

    def MoveTo(self, destFileName:str): # -> 
        """ MoveTo(self: FileInfo, destFileName: str) """
        ...

    def Open(self, mode:FileMode, access:FileAccess = ..., share:FileShare = ...) -> FileStream:
        """
        Open(self: FileInfo, mode: FileMode) -> FileStream
        Open(self: FileInfo, mode: FileMode, access: FileAccess) -> FileStream
        Open(self: FileInfo, mode: FileMode, access: FileAccess, share: FileShare) -> FileStream
        """
        ...

    def OpenRead(self) -> FileStream:
        """ OpenRead(self: FileInfo) -> FileStream """
        ...

    def OpenText(self) -> StreamReader:
        """ OpenText(self: FileInfo) -> StreamReader """
        ...

    def OpenWrite(self) -> FileStream:
        """ OpenWrite(self: FileInfo) -> FileStream """
        ...

    def Replace(self, destinationFileName:str, destinationBackupFileName:str, ignoreMetadataErrors:bool = ...) -> FileInfo:
        """
        Replace(self: FileInfo, destinationFileName: str, destinationBackupFileName: str) -> FileInfo
        Replace(self: FileInfo, destinationFileName: str, destinationBackupFileName: str, ignoreMetadataErrors: bool) -> FileInfo
        """
        ...

    def SetAccessControl(self, fileSecurity:FileSecurity): # -> 
        """ SetAccessControl(self: FileInfo, fileSecurity: FileSecurity) """
        ...

    def ToString(self) -> str:
        """ ToString(self: FileInfo) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...

    FullPath = ...
    OriginalPath = ...


class FileLoadException(IOException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    FileLoadException()
    FileLoadException(message: str)
    FileLoadException(message: str, inner: Exception)
    FileLoadException(message: str, fileName: str)
    FileLoadException(message: str, fileName: str, inner: Exception)
    """
    @property
    def FileName(self) -> str:
        """ Get: FileName(self: FileLoadException) -> str """
        ...

    @property
    def FusionLog(self) -> str:
        """ Get: FusionLog(self: FileLoadException) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: FileLoadException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: FileLoadException, info: SerializationInfo, context: StreamingContext) """
        ...

    def ToString(self) -> str:
        """ ToString(self: FileLoadException) -> str """
        ...

    SerializeObjectState = ...


class FileMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FileMode, values: Append (6), Create (2), CreateNew (1), Open (3), OpenOrCreate (4), Truncate (5) """
    Append: FileMode = ...
    Create: FileMode = ...
    CreateNew: FileMode = ...
    Open: FileMode = ...
    OpenOrCreate: FileMode = ...
    Truncate: FileMode = ...
    value__ = ...


class FileNotFoundException(IOException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    FileNotFoundException()
    FileNotFoundException(message: str)
    FileNotFoundException(message: str, innerException: Exception)
    FileNotFoundException(message: str, fileName: str)
    FileNotFoundException(message: str, fileName: str, innerException: Exception)
    """
    @property
    def FileName(self) -> str:
        """ Get: FileName(self: FileNotFoundException) -> str """
        ...

    @property
    def FusionLog(self) -> str:
        """ Get: FusionLog(self: FileNotFoundException) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: FileNotFoundException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: FileNotFoundException, info: SerializationInfo, context: StreamingContext) """
        ...

    def ToString(self) -> str:
        """ ToString(self: FileNotFoundException) -> str """
        ...

    SerializeObjectState = ...


class FileOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) FileOptions, values: Asynchronous (1073741824), DeleteOnClose (67108864), Encrypted (16384), None (0), RandomAccess (268435456), SequentialScan (134217728), WriteThrough (-2147483648) """
    Asynchronous: FileOptions = ...
    DeleteOnClose: FileOptions = ...
    Encrypted: FileOptions = ...
    RandomAccess: FileOptions = ...
    SequentialScan: FileOptions = ...
    value__ = ...
    WriteThrough: FileOptions = ...


class FileShare(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) FileShare, values: Delete (4), Inheritable (16), None (0), Read (1), ReadWrite (3), Write (2) """
    Delete: FileShare = ...
    Inheritable: FileShare = ...
    Read: FileShare = ...
    ReadWrite: FileShare = ...
    value__ = ...
    Write: FileShare = ...


class FileStream(Stream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    FileStream(path: str, mode: FileMode)
    FileStream(path: str, mode: FileMode, access: FileAccess)
    FileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare)
    FileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int)
    FileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int, options: FileOptions)
    FileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int, useAsync: bool)
    FileStream(path: str, mode: FileMode, rights: FileSystemRights, share: FileShare, bufferSize: int, options: FileOptions, fileSecurity: FileSecurity)
    FileStream(path: str, mode: FileMode, rights: FileSystemRights, share: FileShare, bufferSize: int, options: FileOptions)
    FileStream(handle: IntPtr, access: FileAccess)
    FileStream(handle: IntPtr, access: FileAccess, ownsHandle: bool)
    FileStream(handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int)
    FileStream(handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int, isAsync: bool)
    FileStream(handle: SafeFileHandle, access: FileAccess)
    FileStream(handle: SafeFileHandle, access: FileAccess, bufferSize: int)
    FileStream(handle: SafeFileHandle, access: FileAccess, bufferSize: int, isAsync: bool)
    """
    @property
    def Handle(self) -> IntPtr:
        """ Get: Handle(self: FileStream) -> IntPtr """
        ...

    @property
    def IsAsync(self) -> bool:
        """ Get: IsAsync(self: FileStream) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: FileStream) -> str """
        ...

    @property
    def SafeFileHandle(self) -> SafeFileHandle:
        """ Get: SafeFileHandle(self: FileStream) -> SafeFileHandle """
        ...


    def GetAccessControl(self) -> FileSecurity:
        """ GetAccessControl(self: FileStream) -> FileSecurity """
        ...

    def Lock(self, position:Int64, length:Int64): # -> 
        """ Lock(self: FileStream, position: Int64, length: Int64) """
        ...

    def SetAccessControl(self, fileSecurity:FileSecurity): # -> 
        """ SetAccessControl(self: FileStream, fileSecurity: FileSecurity) """
        ...

    def Unlock(self, position:Int64, length:Int64): # -> 
        """ Unlock(self: FileStream, position: Int64, length: Int64) """
        ...

    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, path: str, mode: FileMode)
        __new__(cls: type, path: str, mode: FileMode, access: FileAccess)
        __new__(cls: type, path: str, mode: FileMode, access: FileAccess, share: FileShare)
        __new__(cls: type, path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int)
        __new__(cls: type, path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int, options: FileOptions)
        __new__(cls: type, path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int, useAsync: bool)
        __new__(cls: type, path: str, mode: FileMode, rights: FileSystemRights, share: FileShare, bufferSize: int, options: FileOptions, fileSecurity: FileSecurity)
        __new__(cls: type, path: str, mode: FileMode, rights: FileSystemRights, share: FileShare, bufferSize: int, options: FileOptions)
        __new__(cls: type, handle: IntPtr, access: FileAccess)
        __new__(cls: type, handle: IntPtr, access: FileAccess, ownsHandle: bool)
        __new__(cls: type, handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int)
        __new__(cls: type, handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int, isAsync: bool)
        __new__(cls: type, handle: SafeFileHandle, access: FileAccess)
        __new__(cls: type, handle: SafeFileHandle, access: FileAccess, bufferSize: int)
        __new__(cls: type, handle: SafeFileHandle, access: FileAccess, bufferSize: int, isAsync: bool)
        """
        ...


class FileSystemEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ FileSystemEventArgs(changeType: WatcherChangeTypes, directory: str, name: str) """
    @property
    def ChangeType(self) -> WatcherChangeTypes:
        """ Get: ChangeType(self: FileSystemEventArgs) -> WatcherChangeTypes """
        ...

    @property
    def FullPath(self) -> str:
        """ Get: FullPath(self: FileSystemEventArgs) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: FileSystemEventArgs) -> str """
        ...


    def __new__(cls, changeType:WatcherChangeTypes, directory:str, name:str) -> Self:
        """ __new__(cls: type, changeType: WatcherChangeTypes, directory: str, name: str) """
        ...


class FileSystemEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FileSystemEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:FileSystemEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: FileSystemEventHandler, sender: object, e: FileSystemEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: FileSystemEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:FileSystemEventArgs): # -> 
        """ Invoke(self: FileSystemEventHandler, sender: object, e: FileSystemEventArgs) """
        ...


class FileSystemWatcher(ISupportInitialize, Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    FileSystemWatcher()
    FileSystemWatcher(path: str)
    FileSystemWatcher(path: str, filter: str)
    """
    @property
    def EnableRaisingEvents(self) -> bool:
        """
        Get: EnableRaisingEvents(self: FileSystemWatcher) -> bool
        Set: EnableRaisingEvents(self: FileSystemWatcher) = value
        """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: FileSystemWatcher) -> str
        Set: Filter(self: FileSystemWatcher) = value
        """
        ...

    @property
    def IncludeSubdirectories(self) -> bool:
        """
        Get: IncludeSubdirectories(self: FileSystemWatcher) -> bool
        Set: IncludeSubdirectories(self: FileSystemWatcher) = value
        """
        ...

    @property
    def InternalBufferSize(self) -> int:
        """
        Get: InternalBufferSize(self: FileSystemWatcher) -> int
        Set: InternalBufferSize(self: FileSystemWatcher) = value
        """
        ...

    @property
    def NotifyFilter(self) -> NotifyFilters:
        """
        Get: NotifyFilter(self: FileSystemWatcher) -> NotifyFilters
        Set: NotifyFilter(self: FileSystemWatcher) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: FileSystemWatcher) -> str
        Set: Path(self: FileSystemWatcher) = value
        """
        ...

    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """
        Get: SynchronizingObject(self: FileSystemWatcher) -> ISynchronizeInvoke
        Set: SynchronizingObject(self: FileSystemWatcher) = value
        """
        ...


    def OnChanged(self, *args): #cannot find CLR method
        """ OnChanged(self: FileSystemWatcher, e: FileSystemEventArgs) """
        ...

    def OnCreated(self, *args): #cannot find CLR method
        """ OnCreated(self: FileSystemWatcher, e: FileSystemEventArgs) """
        ...

    def OnDeleted(self, *args): #cannot find CLR method
        """ OnDeleted(self: FileSystemWatcher, e: FileSystemEventArgs) """
        ...

    def OnError(self, *args): #cannot find CLR method
        """ OnError(self: FileSystemWatcher, e: ErrorEventArgs) """
        ...

    def OnRenamed(self, *args): #cannot find CLR method
        """ OnRenamed(self: FileSystemWatcher, e: RenamedEventArgs) """
        ...

    def WaitForChanged(self, changeType:WatcherChangeTypes, timeout:int = ...) -> WaitForChangedResult:
        """
        WaitForChanged(self: FileSystemWatcher, changeType: WatcherChangeTypes) -> WaitForChangedResult
        WaitForChanged(self: FileSystemWatcher, changeType: WatcherChangeTypes, timeout: int) -> WaitForChangedResult
        """
        ...

    def __new__(cls, path:str = ..., filter:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, path: str)
        __new__(cls: type, path: str, filter: str)
        """
        ...

    Changed = ...
    Created = ...
    Deleted = ...
    Error = ...
    Renamed = ...


class HandleInheritability(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HandleInheritability, values: Inheritable (1), None (0) """
    Inheritable: HandleInheritability = ...
    value__ = ...


class InternalBufferOverflowException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InternalBufferOverflowException()
    InternalBufferOverflowException(message: str)
    InternalBufferOverflowException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class InvalidDataException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidDataException()
    InvalidDataException(message: str)
    InvalidDataException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class IODescriptionAttribute(DescriptionAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ IODescriptionAttribute(description: str) """
    pass

class MemoryStream(Stream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    MemoryStream()
    MemoryStream(capacity: int)
    MemoryStream(buffer: Array[Byte])
    MemoryStream(buffer: Array[Byte], writable: bool)
    MemoryStream(buffer: Array[Byte], index: int, count: int)
    MemoryStream(buffer: Array[Byte], index: int, count: int, writable: bool)
    MemoryStream(buffer: Array[Byte], index: int, count: int, writable: bool, publiclyVisible: bool)
    """
    @property
    def Capacity(self) -> int:
        """
        Get: Capacity(self: MemoryStream) -> int
        Set: Capacity(self: MemoryStream) = value
        """
        ...


    def GetBuffer(self) -> Array:
        """ GetBuffer(self: MemoryStream) -> Array[Byte] """
        ...

    def ToArray(self) -> Array:
        """ ToArray(self: MemoryStream) -> Array[Byte] """
        ...

    def TryGetBuffer(self, buffer) -> Tuple_[bool, ArraySegment]:
        """ TryGetBuffer(self: MemoryStream) -> (bool, ArraySegment[Byte]) """
        ...

    def WriteTo(self, stream:Stream): # -> 
        """ WriteTo(self: MemoryStream, stream: Stream) """
        ...

    def __new__(cls, *__args:int) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, capacity: int)
        __new__(cls: type, buffer: Array[Byte])
        __new__(cls: type, buffer: Array[Byte], writable: bool)
        __new__(cls: type, buffer: Array[Byte], index: int, count: int)
        __new__(cls: type, buffer: Array[Byte], index: int, count: int, writable: bool)
        __new__(cls: type, buffer: Array[Byte], index: int, count: int, writable: bool, publiclyVisible: bool)
        """
        ...


class NotifyFilters(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) NotifyFilters, values: Attributes (4), CreationTime (64), DirectoryName (2), FileName (1), LastAccess (32), LastWrite (16), Security (256), Size (8) """
    Attributes: NotifyFilters = ...
    CreationTime: NotifyFilters = ...
    DirectoryName: NotifyFilters = ...
    FileName: NotifyFilters = ...
    LastAccess: NotifyFilters = ...
    LastWrite: NotifyFilters = ...
    Security: NotifyFilters = ...
    Size: NotifyFilters = ...
    value__ = ...


class Path: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ChangeExtension(path:str, extension:str) -> str:
        """ ChangeExtension(path: str, extension: str) -> str """
        ...

    @staticmethod
    def Combine(*__args:Array) -> str:
        """
        Combine(*paths: Array[str]) -> str
        Combine(path1: str, path2: str, path3: str) -> str
        Combine(path1: str, path2: str, path3: str, path4: str) -> str
        Combine(path1: str, path2: str) -> str
        """
        ...

    @staticmethod
    def GetDirectoryName(path:str) -> str:
        """ GetDirectoryName(path: str) -> str """
        ...

    @staticmethod
    def GetExtension(path:str) -> str:
        """ GetExtension(path: str) -> str """
        ...

    @staticmethod
    def GetFileName(path:str) -> str:
        """ GetFileName(path: str) -> str """
        ...

    @staticmethod
    def GetFileNameWithoutExtension(path:str) -> str:
        """ GetFileNameWithoutExtension(path: str) -> str """
        ...

    @staticmethod
    def GetFullPath(path:str) -> str:
        """ GetFullPath(path: str) -> str """
        ...

    @staticmethod
    def GetInvalidFileNameChars() -> Array:
        """ GetInvalidFileNameChars() -> Array[Char] """
        ...

    @staticmethod
    def GetInvalidPathChars() -> Array:
        """ GetInvalidPathChars() -> Array[Char] """
        ...

    @staticmethod
    def GetPathRoot(path:str) -> str:
        """ GetPathRoot(path: str) -> str """
        ...

    @staticmethod
    def GetRandomFileName() -> str:
        """ GetRandomFileName() -> str """
        ...

    @staticmethod
    def GetTempFileName() -> str:
        """ GetTempFileName() -> str """
        ...

    @staticmethod
    def GetTempPath() -> str:
        """ GetTempPath() -> str """
        ...

    @staticmethod
    def HasExtension(path:str) -> bool:
        """ HasExtension(path: str) -> bool """
        ...

    @staticmethod
    def IsPathRooted(path:str) -> bool:
        """ IsPathRooted(path: str) -> bool """
        ...

    AltDirectorySeparatorChar: Char = ...
    DirectorySeparatorChar: Char = ...
    InvalidPathChars = ...
    PathSeparator: Char = ...
    VolumeSeparatorChar: Char = ...
    __all__: list = ...


class PathTooLongException(IOException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PathTooLongException()
    PathTooLongException(message: str)
    PathTooLongException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class PipeException(IOException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PipeException()
    PipeException(message: str)
    PipeException(message: str, errorCode: int)
    PipeException(message: str, inner: Exception)
    """
    @property
    def ErrorCode(self) -> int:
        """ Get: ErrorCode(self: PipeException) -> int """
        ...


    SerializeObjectState = ...


class RenamedEventArgs(FileSystemEventArgs): # skipped bases: <type 'object'>
    """ RenamedEventArgs(changeType: WatcherChangeTypes, directory: str, name: str, oldName: str) """
    @property
    def OldFullPath(self) -> str:
        """ Get: OldFullPath(self: RenamedEventArgs) -> str """
        ...

    @property
    def OldName(self) -> str:
        """ Get: OldName(self: RenamedEventArgs) -> str """
        ...



class RenamedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ RenamedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:RenamedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: RenamedEventHandler, sender: object, e: RenamedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: RenamedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:RenamedEventArgs): # -> 
        """ Invoke(self: RenamedEventHandler, sender: object, e: RenamedEventArgs) """
        ...


class SearchOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SearchOption, values: AllDirectories (1), TopDirectoryOnly (0) """
    AllDirectories: SearchOption = ...
    TopDirectoryOnly: SearchOption = ...
    value__ = ...


class SeekOrigin(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SeekOrigin, values: Begin (0), Current (1), End (2) """
    Begin: SeekOrigin = ...
    Current: SeekOrigin = ...
    End: SeekOrigin = ...
    value__ = ...


class TextReader(IDisposable, MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    def Close(self): # -> 
        """ Close(self: TextReader) """
        ...

    def Peek(self) -> int:
        """ Peek(self: TextReader) -> int """
        ...

    def Read(self, buffer=None, index=None, count=None) -> int:
        """
        Read(self: TextReader) -> int
        Read(self: TextReader, index: int, count: int) -> (int, Array[Char])
        """
        ...

    def ReadAsync(self, buffer:Array, index:int, count:int) -> Task:
        """ ReadAsync(self: TextReader, buffer: Array[Char], index: int, count: int) -> Task[int] """
        ...

    def ReadBlock(self, buffer, index, count) -> Tuple_[int, Array]:
        """ ReadBlock(self: TextReader, index: int, count: int) -> (int, Array[Char]) """
        ...

    def ReadBlockAsync(self, buffer:Array, index:int, count:int) -> Task:
        """ ReadBlockAsync(self: TextReader, buffer: Array[Char], index: int, count: int) -> Task[int] """
        ...

    def ReadLine(self) -> str:
        """ ReadLine(self: TextReader) -> str """
        ...

    def ReadLineAsync(self) -> Task:
        """ ReadLineAsync(self: TextReader) -> Task[str] """
        ...

    def ReadToEnd(self) -> str:
        """ ReadToEnd(self: TextReader) -> str """
        ...

    def ReadToEndAsync(self) -> Task:
        """ ReadToEndAsync(self: TextReader) -> Task[str] """
        ...

    @staticmethod
    def Synchronized(reader:TextReader) -> TextReader:
        """ Synchronized(reader: TextReader) -> TextReader """
        ...

    Null = ...


class StreamReader(TextReader): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    StreamReader(stream: Stream)
    StreamReader(stream: Stream, detectEncodingFromByteOrderMarks: bool)
    StreamReader(stream: Stream, encoding: Encoding)
    StreamReader(stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool)
    StreamReader(stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int)
    StreamReader(stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int, leaveOpen: bool)
    StreamReader(path: str)
    StreamReader(path: str, detectEncodingFromByteOrderMarks: bool)
    StreamReader(path: str, encoding: Encoding)
    StreamReader(path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool)
    StreamReader(path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int)
    """
    @property
    def BaseStream(self) -> Stream:
        """ Get: BaseStream(self: StreamReader) -> Stream """
        ...

    @property
    def CurrentEncoding(self) -> Encoding:
        """ Get: CurrentEncoding(self: StreamReader) -> Encoding """
        ...

    @property
    def EndOfStream(self) -> bool:
        """ Get: EndOfStream(self: StreamReader) -> bool """
        ...


    def DiscardBufferedData(self): # -> 
        """ DiscardBufferedData(self: StreamReader) """
        ...

    def __new__(cls, *__args:Stream) -> Self:
        """
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, detectEncodingFromByteOrderMarks: bool)
        __new__(cls: type, stream: Stream, encoding: Encoding)
        __new__(cls: type, stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool)
        __new__(cls: type, stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int)
        __new__(cls: type, stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int, leaveOpen: bool)
        __new__(cls: type, path: str)
        __new__(cls: type, path: str, detectEncodingFromByteOrderMarks: bool)
        __new__(cls: type, path: str, encoding: Encoding)
        __new__(cls: type, path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool)
        __new__(cls: type, path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int)
        """
        ...

    Null = ...


class TextWriter(IDisposable, MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Encoding(self) -> Encoding:
        """ Get: Encoding(self: TextWriter) -> Encoding """
        ...

    @property
    def FormatProvider(self) -> IFormatProvider:
        """ Get: FormatProvider(self: TextWriter) -> IFormatProvider """
        ...

    @property
    def NewLine(self) -> str:
        """
        Get: NewLine(self: TextWriter) -> str
        Set: NewLine(self: TextWriter) = value
        """
        ...


    def Close(self): # -> 
        """ Close(self: TextWriter) """
        ...

    def Flush(self): # -> 
        """ Flush(self: TextWriter) """
        ...

    def FlushAsync(self) -> Task:
        """ FlushAsync(self: TextWriter) -> Task """
        ...

    @staticmethod
    def Synchronized(writer:TextWriter) -> TextWriter:
        """ Synchronized(writer: TextWriter) -> TextWriter """
        ...

    def Write(self, *__args:Char): # -> 
        """ Write(self: TextWriter, value: Char)Write(self: TextWriter, format: str, arg0: object, arg1: object, arg2: object)Write(self: TextWriter, format: str, arg0: object, arg1: object)Write(self: TextWriter, format: str, arg0: object)Write(self: TextWriter, value: object)Write(self: TextWriter, value: str)Write(self: TextWriter, value: Decimal)Write(self: TextWriter, format: str, *arg: Array[object])Write(self: TextWriter, value: float)Write(self: TextWriter, value: UInt64)Write(self: TextWriter, value: Int64)Write(self: TextWriter, value: UInt32)Write(self: TextWriter, value: int)Write(self: TextWriter, buffer: Array[Char], index: int, count: int)Write(self: TextWriter, buffer: Array[Char])Write(self: TextWriter, value: Single)Write(self: TextWriter, value: bool) """
        ...

    def WriteAsync(self, *__args:Char) -> Task:
        """
        WriteAsync(self: TextWriter, value: Char) -> Task
        WriteAsync(self: TextWriter, value: str) -> Task
        WriteAsync(self: TextWriter, buffer: Array[Char], index: int, count: int) -> Task
        WriteAsync(self: TextWriter, buffer: Array[Char]) -> Task
        """
        ...

    def WriteLine(self, *__args:object): # -> 
        """ WriteLine(self: TextWriter)WriteLine(self: TextWriter, format: str, arg0: object, arg1: object)WriteLine(self: TextWriter, format: str, arg0: object)WriteLine(self: TextWriter, value: object)WriteLine(self: TextWriter, value: str)WriteLine(self: TextWriter, value: Decimal)WriteLine(self: TextWriter, value: float)WriteLine(self: TextWriter, value: Single)WriteLine(self: TextWriter, value: UInt64)WriteLine(self: TextWriter, value: Int64)WriteLine(self: TextWriter, value: UInt32)WriteLine(self: TextWriter, value: int)WriteLine(self: TextWriter, value: bool)WriteLine(self: TextWriter, buffer: Array[Char], index: int, count: int)WriteLine(self: TextWriter, buffer: Array[Char])WriteLine(self: TextWriter, value: Char)WriteLine(self: TextWriter, format: str, arg0: object, arg1: object, arg2: object)WriteLine(self: TextWriter, format: str, *arg: Array[object]) """
        ...

    def WriteLineAsync(self, *__args:Char) -> Task:
        """
        WriteLineAsync(self: TextWriter, value: Char) -> Task
        WriteLineAsync(self: TextWriter, value: str) -> Task
        WriteLineAsync(self: TextWriter, buffer: Array[Char], index: int, count: int) -> Task
        WriteLineAsync(self: TextWriter) -> Task
        WriteLineAsync(self: TextWriter, buffer: Array[Char]) -> Task
        """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, formatProvider: IFormatProvider)
        """
        ...

    CoreNewLine = ...
    Null = ...


class StreamWriter(TextWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    StreamWriter(stream: Stream)
    StreamWriter(stream: Stream, encoding: Encoding)
    StreamWriter(stream: Stream, encoding: Encoding, bufferSize: int)
    StreamWriter(stream: Stream, encoding: Encoding, bufferSize: int, leaveOpen: bool)
    StreamWriter(path: str)
    StreamWriter(path: str, append: bool)
    StreamWriter(path: str, append: bool, encoding: Encoding)
    StreamWriter(path: str, append: bool, encoding: Encoding, bufferSize: int)
    """
    @property
    def AutoFlush(self) -> bool:
        """
        Get: AutoFlush(self: StreamWriter) -> bool
        Set: AutoFlush(self: StreamWriter) = value
        """
        ...

    @property
    def BaseStream(self) -> Stream:
        """ Get: BaseStream(self: StreamWriter) -> Stream """
        ...


    CoreNewLine = ...
    Null: StreamWriter = ...


class StringReader(TextReader): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ StringReader(s: str) """
    def __new__(cls, s:str) -> Self:
        """ __new__(cls: type, s: str) """
        ...


class StringWriter(TextWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    StringWriter()
    StringWriter(formatProvider: IFormatProvider)
    StringWriter(sb: StringBuilder)
    StringWriter(sb: StringBuilder, formatProvider: IFormatProvider)
    """
    def GetStringBuilder(self) -> StringBuilder:
        """ GetStringBuilder(self: StringWriter) -> StringBuilder """
        ...

    def ToString(self) -> str:
        """ ToString(self: StringWriter) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...

    CoreNewLine = ...


class UnmanagedMemoryAccessor(IDisposable): # skipped bases: <type 'object'>
    """
    UnmanagedMemoryAccessor(buffer: SafeBuffer, offset: Int64, capacity: Int64)
    UnmanagedMemoryAccessor(buffer: SafeBuffer, offset: Int64, capacity: Int64, access: FileAccess)
    """
    @property
    def CanRead(self) -> bool:
        """ Get: CanRead(self: UnmanagedMemoryAccessor) -> bool """
        ...

    @property
    def CanWrite(self) -> bool:
        """ Get: CanWrite(self: UnmanagedMemoryAccessor) -> bool """
        ...

    @property
    def Capacity(self) -> Int64:
        """ Get: Capacity(self: UnmanagedMemoryAccessor) -> Int64 """
        ...

    @property
    def IsOpen(self):
        ...


    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: UnmanagedMemoryAccessor, buffer: SafeBuffer, offset: Int64, capacity: Int64, access: FileAccess) """
        ...

    def Read(self, position, structure): # -> T
        """ Read[T](self: UnmanagedMemoryAccessor, position: Int64) -> T """
        ...

    def ReadArray(self, position:Int64, array:Array, offset:int, count:int) -> int:
        """ ReadArray[T](self: UnmanagedMemoryAccessor, position: Int64, array: Array[T], offset: int, count: int) -> int """
        ...

    def ReadBoolean(self, position:Int64) -> bool:
        """ ReadBoolean(self: UnmanagedMemoryAccessor, position: Int64) -> bool """
        ...

    def ReadByte(self, position:Int64) -> Byte:
        """ ReadByte(self: UnmanagedMemoryAccessor, position: Int64) -> Byte """
        ...

    def ReadChar(self, position:Int64) -> Char:
        """ ReadChar(self: UnmanagedMemoryAccessor, position: Int64) -> Char """
        ...

    def ReadDecimal(self, position:Int64) -> Decimal:
        """ ReadDecimal(self: UnmanagedMemoryAccessor, position: Int64) -> Decimal """
        ...

    def ReadDouble(self, position:Int64) -> float:
        """ ReadDouble(self: UnmanagedMemoryAccessor, position: Int64) -> float """
        ...

    def ReadInt16(self, position:Int64) -> Int16:
        """ ReadInt16(self: UnmanagedMemoryAccessor, position: Int64) -> Int16 """
        ...

    def ReadInt32(self, position:Int64) -> int:
        """ ReadInt32(self: UnmanagedMemoryAccessor, position: Int64) -> int """
        ...

    def ReadInt64(self, position:Int64) -> Int64:
        """ ReadInt64(self: UnmanagedMemoryAccessor, position: Int64) -> Int64 """
        ...

    def ReadSByte(self, position:Int64) -> SByte:
        """ ReadSByte(self: UnmanagedMemoryAccessor, position: Int64) -> SByte """
        ...

    def ReadSingle(self, position:Int64) -> Single:
        """ ReadSingle(self: UnmanagedMemoryAccessor, position: Int64) -> Single """
        ...

    def ReadUInt16(self, position:Int64) -> UInt16:
        """ ReadUInt16(self: UnmanagedMemoryAccessor, position: Int64) -> UInt16 """
        ...

    def ReadUInt32(self, position:Int64) -> UInt32:
        """ ReadUInt32(self: UnmanagedMemoryAccessor, position: Int64) -> UInt32 """
        ...

    def ReadUInt64(self, position:Int64) -> UInt64:
        """ ReadUInt64(self: UnmanagedMemoryAccessor, position: Int64) -> UInt64 """
        ...

    def Write(self, position:Int64, *__args:bool): # -> 
        """ Write(self: UnmanagedMemoryAccessor, position: Int64, value: bool)Write(self: UnmanagedMemoryAccessor, position: Int64, value: Byte)Write(self: UnmanagedMemoryAccessor, position: Int64, value: Decimal)Write(self: UnmanagedMemoryAccessor, position: Int64, value: Char)Write(self: UnmanagedMemoryAccessor, position: Int64, value: Int16)Write(self: UnmanagedMemoryAccessor, position: Int64, value: int)Write(self: UnmanagedMemoryAccessor, position: Int64, value: Int64)Write(self: UnmanagedMemoryAccessor, position: Int64, value: Single)Write(self: UnmanagedMemoryAccessor, position: Int64, value: float)Write(self: UnmanagedMemoryAccessor, position: Int64, value: SByte)Write(self: UnmanagedMemoryAccessor, position: Int64, value: UInt16)Write(self: UnmanagedMemoryAccessor, position: Int64, value: UInt32)Write(self: UnmanagedMemoryAccessor, position: Int64, value: UInt64)Write[T](self: UnmanagedMemoryAccessor, position: Int64, structure: T) -> T """
        ...

    def WriteArray(self, position:Int64, array:Array, offset:int, count:int): # -> 
        """ WriteArray[T](self: UnmanagedMemoryAccessor, position: Int64, array: Array[T], offset: int, count: int) """
        ...


class UnmanagedMemoryStream(Stream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    UnmanagedMemoryStream(buffer: SafeBuffer, offset: Int64, length: Int64)
    UnmanagedMemoryStream(buffer: SafeBuffer, offset: Int64, length: Int64, access: FileAccess)
    UnmanagedMemoryStream(pointer: Byte*, length: Int64)
    UnmanagedMemoryStream(pointer: Byte*, length: Int64, capacity: Int64, access: FileAccess)
    """
    @property
    def Capacity(self) -> Int64:
        """ Get: Capacity(self: UnmanagedMemoryStream) -> Int64 """
        ...

    @property
    def PositionPointer(self) -> Byte:
        """
        Get: PositionPointer(self: UnmanagedMemoryStream) -> Byte*
        Set: PositionPointer(self: UnmanagedMemoryStream) = value
        """
        ...


    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: UnmanagedMemoryStream, pointer: Byte*, length: Int64, capacity: Int64, access: FileAccess)Initialize(self: UnmanagedMemoryStream, buffer: SafeBuffer, offset: Int64, length: Int64, access: FileAccess) """
        ...

    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, buffer: SafeBuffer, offset: Int64, length: Int64)
        __new__(cls: type, buffer: SafeBuffer, offset: Int64, length: Int64, access: FileAccess)
        __new__(cls: type, pointer: Byte*, length: Int64)
        __new__(cls: type, pointer: Byte*, length: Int64, capacity: Int64, access: FileAccess)
        """
        ...


class WaitForChangedResult: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ChangeType(self) -> WatcherChangeTypes:
        """
        Get: ChangeType(self: WaitForChangedResult) -> WatcherChangeTypes
        Set: ChangeType(self: WaitForChangedResult) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: WaitForChangedResult) -> str
        Set: Name(self: WaitForChangedResult) = value
        """
        ...

    @property
    def OldName(self) -> str:
        """
        Get: OldName(self: WaitForChangedResult) -> str
        Set: OldName(self: WaitForChangedResult) = value
        """
        ...

    @property
    def TimedOut(self) -> bool:
        """
        Get: TimedOut(self: WaitForChangedResult) -> bool
        Set: TimedOut(self: WaitForChangedResult) = value
        """
        ...



class WatcherChangeTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) WatcherChangeTypes, values: All (15), Changed (4), Created (1), Deleted (2), Renamed (8) """
    All: WatcherChangeTypes = ...
    Changed: WatcherChangeTypes = ...
    Created: WatcherChangeTypes = ...
    Deleted: WatcherChangeTypes = ...
    Renamed: WatcherChangeTypes = ...
    value__ = ...


class WindowsRuntimeStorageExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateSafeFileHandle(*__args) -> SafeFileHandle:
        """
        CreateSafeFileHandle(windowsRuntimeFile: IStorageFile, access: FileAccess, share: FileShare, options: FileOptions) -> SafeFileHandle
        CreateSafeFileHandle(rootDirectory: IStorageFolder, relativePath: str, mode: FileMode) -> SafeFileHandle
        CreateSafeFileHandle(rootDirectory: IStorageFolder, relativePath: str, mode: FileMode, access: FileAccess, share: FileShare, options: FileOptions) -> SafeFileHandle
        """
        ...

    @staticmethod
    def OpenStreamForReadAsync(*__args) -> Task: # Not found arg types: {'*__args': 'IStorageFile'}
        """
        OpenStreamForReadAsync(windowsRuntimeFile: IStorageFile) -> Task[Stream]
        OpenStreamForReadAsync(rootDirectory: IStorageFolder, relativePath: str) -> Task[Stream]
        """
        ...

    @staticmethod
    def OpenStreamForWriteAsync(*__args) -> Task: # Not found arg types: {'*__args': 'IStorageFile'}
        """
        OpenStreamForWriteAsync(windowsRuntimeFile: IStorageFile) -> Task[Stream]
        OpenStreamForWriteAsync(rootDirectory: IStorageFolder, relativePath: str, creationCollisionOption: CreationCollisionOption) -> Task[Stream]
        """
        ...

    __all__: list = ...


class WindowsRuntimeStreamExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AsInputStream(stream:Stream): # -> IInputStream
        """ AsInputStream(stream: Stream) -> IInputStream """
        ...

    @staticmethod
    def AsOutputStream(stream:Stream): # -> IOutputStream
        """ AsOutputStream(stream: Stream) -> IOutputStream """
        ...

    @staticmethod
    def AsRandomAccessStream(stream:Stream): # -> IRandomAccessStream
        """ AsRandomAccessStream(stream: Stream) -> IRandomAccessStream """
        ...

    @staticmethod
    def AsStream(windowsRuntimeStream, bufferSize:int = ...) -> Stream: # Not found arg types: {'windowsRuntimeStream': 'IRandomAccessStream'}
        """
        AsStream(windowsRuntimeStream: IRandomAccessStream) -> Stream
        AsStream(windowsRuntimeStream: IRandomAccessStream, bufferSize: int) -> Stream
        """
        ...

    @staticmethod
    def AsStreamForRead(windowsRuntimeStream, bufferSize:int = ...) -> Stream: # Not found arg types: {'windowsRuntimeStream': 'IInputStream'}
        """
        AsStreamForRead(windowsRuntimeStream: IInputStream) -> Stream
        AsStreamForRead(windowsRuntimeStream: IInputStream, bufferSize: int) -> Stream
        """
        ...

    @staticmethod
    def AsStreamForWrite(windowsRuntimeStream, bufferSize:int = ...) -> Stream: # Not found arg types: {'windowsRuntimeStream': 'IOutputStream'}
        """
        AsStreamForWrite(windowsRuntimeStream: IOutputStream) -> Stream
        AsStreamForWrite(windowsRuntimeStream: IOutputStream, bufferSize: int) -> Stream
        """
        ...

    __all__: list = ...


# variables with complex values

