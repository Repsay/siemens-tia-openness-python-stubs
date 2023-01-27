# encoding: utf-8
# module Microsoft.VisualBasic.FileIO calls itself FileIO
# from Microsoft.VisualBasic, Version=10.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, IDisposable, Int64

from System.Collections.ObjectModel import ReadOnlyCollection

from System.IO import (DirectoryInfo, DriveInfo, FileInfo, StreamReader, 
    StreamWriter)

from System.Text import Encoding

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class DeleteDirectoryOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DeleteDirectoryOption, values: DeleteAllContents (5), ThrowIfDirectoryNonEmpty (4) """
    DeleteAllContents: DeleteDirectoryOption = ...
    ThrowIfDirectoryNonEmpty: DeleteDirectoryOption = ...
    value__ = ...


class FieldType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FieldType, values: Delimited (0), FixedWidth (1) """
    Delimited: FieldType = ...
    FixedWidth: FieldType = ...
    value__ = ...


class FileSystem: # skipped bases: <type 'object'>, <type 'object'>
    """ FileSystem() """
    @property
    def CurrentDirectory(self) -> str:
        """
        Get: CurrentDirectory() -> str
        Set: CurrentDirectory() = value
        """
        ...

    @property
    def Drives(self) -> ReadOnlyCollection:
        """ Get: Drives() -> ReadOnlyCollection[DriveInfo] """
        ...


    @staticmethod
    def CombinePath(baseDirectory:str, relativePath:str) -> str:
        """ CombinePath(baseDirectory: str, relativePath: str) -> str """
        ...

    @staticmethod
    def CopyDirectory(sourceDirectoryName:str, destinationDirectoryName:str, *__args:bool): # -> 
        """ CopyDirectory(sourceDirectoryName: str, destinationDirectoryName: str)CopyDirectory(sourceDirectoryName: str, destinationDirectoryName: str, overwrite: bool)CopyDirectory(sourceDirectoryName: str, destinationDirectoryName: str, showUI: UIOption)CopyDirectory(sourceDirectoryName: str, destinationDirectoryName: str, showUI: UIOption, onUserCancel: UICancelOption) """
        ...

    @staticmethod
    def CopyFile(sourceFileName:str, destinationFileName:str, *__args:bool): # -> 
        """ CopyFile(sourceFileName: str, destinationFileName: str)CopyFile(sourceFileName: str, destinationFileName: str, overwrite: bool)CopyFile(sourceFileName: str, destinationFileName: str, showUI: UIOption)CopyFile(sourceFileName: str, destinationFileName: str, showUI: UIOption, onUserCancel: UICancelOption) """
        ...

    @staticmethod
    def CreateDirectory(directory:str): # -> 
        """ CreateDirectory(directory: str) """
        ...

    @staticmethod
    def DeleteDirectory(directory:str, *__args:DeleteDirectoryOption): # -> 
        """ DeleteDirectory(directory: str, onDirectoryNotEmpty: DeleteDirectoryOption)DeleteDirectory(directory: str, showUI: UIOption, recycle: RecycleOption)DeleteDirectory(directory: str, showUI: UIOption, recycle: RecycleOption, onUserCancel: UICancelOption) """
        ...

    @staticmethod
    def DeleteFile(file:str, showUI:UIOption = ..., recycle:RecycleOption = ..., onUserCancel:UICancelOption = ...): # -> 
        """ DeleteFile(file: str)DeleteFile(file: str, showUI: UIOption, recycle: RecycleOption)DeleteFile(file: str, showUI: UIOption, recycle: RecycleOption, onUserCancel: UICancelOption) """
        ...

    @staticmethod
    def DirectoryExists(directory:str) -> bool:
        """ DirectoryExists(directory: str) -> bool """
        ...

    @staticmethod
    def FileExists(file:str) -> bool:
        """ FileExists(file: str) -> bool """
        ...

    @staticmethod
    def FindInFiles(directory:str, containsText:str, ignoreCase:bool, searchType:SearchOption, fileWildcards:Array = ...) -> ReadOnlyCollection:
        """
        FindInFiles(directory: str, containsText: str, ignoreCase: bool, searchType: SearchOption) -> ReadOnlyCollection[str]
        FindInFiles(directory: str, containsText: str, ignoreCase: bool, searchType: SearchOption, *fileWildcards: Array[str]) -> ReadOnlyCollection[str]
        """
        ...

    @staticmethod
    def GetDirectories(directory:str, searchType:SearchOption = ..., wildcards:Array = ...) -> ReadOnlyCollection:
        """
        GetDirectories(directory: str) -> ReadOnlyCollection[str]
        GetDirectories(directory: str, searchType: SearchOption, *wildcards: Array[str]) -> ReadOnlyCollection[str]
        """
        ...

    @staticmethod
    def GetDirectoryInfo(directory:str) -> DirectoryInfo:
        """ GetDirectoryInfo(directory: str) -> DirectoryInfo """
        ...

    @staticmethod
    def GetDriveInfo(drive:str) -> DriveInfo:
        """ GetDriveInfo(drive: str) -> DriveInfo """
        ...

    @staticmethod
    def GetFileInfo(file:str) -> FileInfo:
        """ GetFileInfo(file: str) -> FileInfo """
        ...

    @staticmethod
    def GetFiles(directory:str, searchType:SearchOption = ..., wildcards:Array = ...) -> ReadOnlyCollection:
        """
        GetFiles(directory: str) -> ReadOnlyCollection[str]
        GetFiles(directory: str, searchType: SearchOption, *wildcards: Array[str]) -> ReadOnlyCollection[str]
        """
        ...

    @staticmethod
    def GetName(path:str) -> str:
        """ GetName(path: str) -> str """
        ...

    @staticmethod
    def GetParentPath(path:str) -> str:
        """ GetParentPath(path: str) -> str """
        ...

    @staticmethod
    def GetTempFileName() -> str:
        """ GetTempFileName() -> str """
        ...

    @staticmethod
    def MoveDirectory(sourceDirectoryName:str, destinationDirectoryName:str, *__args:bool): # -> 
        """ MoveDirectory(sourceDirectoryName: str, destinationDirectoryName: str)MoveDirectory(sourceDirectoryName: str, destinationDirectoryName: str, overwrite: bool)MoveDirectory(sourceDirectoryName: str, destinationDirectoryName: str, showUI: UIOption)MoveDirectory(sourceDirectoryName: str, destinationDirectoryName: str, showUI: UIOption, onUserCancel: UICancelOption) """
        ...

    @staticmethod
    def MoveFile(sourceFileName:str, destinationFileName:str, *__args:bool): # -> 
        """ MoveFile(sourceFileName: str, destinationFileName: str)MoveFile(sourceFileName: str, destinationFileName: str, overwrite: bool)MoveFile(sourceFileName: str, destinationFileName: str, showUI: UIOption)MoveFile(sourceFileName: str, destinationFileName: str, showUI: UIOption, onUserCancel: UICancelOption) """
        ...

    @staticmethod
    def OpenTextFieldParser(file:str, *__args:Array) -> TextFieldParser:
        """
        OpenTextFieldParser(file: str) -> TextFieldParser
        OpenTextFieldParser(file: str, *delimiters: Array[str]) -> TextFieldParser
        OpenTextFieldParser(file: str, *fieldWidths: Array[int]) -> TextFieldParser
        """
        ...

    @staticmethod
    def OpenTextFileReader(file:str, encoding:Encoding = ...) -> StreamReader:
        """
        OpenTextFileReader(file: str) -> StreamReader
        OpenTextFileReader(file: str, encoding: Encoding) -> StreamReader
        """
        ...

    @staticmethod
    def OpenTextFileWriter(file:str, append:bool, encoding:Encoding = ...) -> StreamWriter:
        """
        OpenTextFileWriter(file: str, append: bool) -> StreamWriter
        OpenTextFileWriter(file: str, append: bool, encoding: Encoding) -> StreamWriter
        """
        ...

    @staticmethod
    def ReadAllBytes(file:str) -> Array:
        """ ReadAllBytes(file: str) -> Array[Byte] """
        ...

    @staticmethod
    def ReadAllText(file:str, encoding:Encoding = ...) -> str:
        """
        ReadAllText(file: str) -> str
        ReadAllText(file: str, encoding: Encoding) -> str
        """
        ...

    @staticmethod
    def RenameDirectory(directory:str, newName:str): # -> 
        """ RenameDirectory(directory: str, newName: str) """
        ...

    @staticmethod
    def RenameFile(file:str, newName:str): # -> 
        """ RenameFile(file: str, newName: str) """
        ...

    @staticmethod
    def WriteAllBytes(file:str, data:Array, append:bool): # -> 
        """ WriteAllBytes(file: str, data: Array[Byte], append: bool) """
        ...

    @staticmethod
    def WriteAllText(file:str, text:str, append:bool, encoding:Encoding = ...): # -> 
        """ WriteAllText(file: str, text: str, append: bool)WriteAllText(file: str, text: str, append: bool, encoding: Encoding) """
        ...



class MalformedLineException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MalformedLineException()
    MalformedLineException(message: str, lineNumber: Int64)
    MalformedLineException(message: str)
    MalformedLineException(message: str, lineNumber: Int64, innerException: Exception)
    MalformedLineException(message: str, innerException: Exception)
    """
    @property
    def LineNumber(self) -> Int64:
        """
        Get: LineNumber(self: MalformedLineException) -> Int64
        Set: LineNumber(self: MalformedLineException) = value
        """
        ...


    SerializeObjectState = ...


class RecycleOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RecycleOption, values: DeletePermanently (2), SendToRecycleBin (3) """
    DeletePermanently: RecycleOption = ...
    SendToRecycleBin: RecycleOption = ...
    value__ = ...


class SearchOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SearchOption, values: SearchAllSubDirectories (3), SearchTopLevelOnly (2) """
    SearchAllSubDirectories: SearchOption = ...
    SearchTopLevelOnly: SearchOption = ...
    value__ = ...


class SpecialDirectories: # skipped bases: <type 'object'>, <type 'object'>
    """ SpecialDirectories() """
    @property
    def AllUsersApplicationData(self) -> str:
        """ Get: AllUsersApplicationData() -> str """
        ...

    @property
    def CurrentUserApplicationData(self) -> str:
        """ Get: CurrentUserApplicationData() -> str """
        ...

    @property
    def Desktop(self) -> str:
        """ Get: Desktop() -> str """
        ...

    @property
    def MyDocuments(self) -> str:
        """ Get: MyDocuments() -> str """
        ...

    @property
    def MyMusic(self) -> str:
        """ Get: MyMusic() -> str """
        ...

    @property
    def MyPictures(self) -> str:
        """ Get: MyPictures() -> str """
        ...

    @property
    def ProgramFiles(self) -> str:
        """ Get: ProgramFiles() -> str """
        ...

    @property
    def Programs(self) -> str:
        """ Get: Programs() -> str """
        ...

    @property
    def Temp(self) -> str:
        """ Get: Temp() -> str """
        ...




class TextFieldParser(IDisposable): # skipped bases: <type 'object'>
    """
    TextFieldParser(path: str)
    TextFieldParser(path: str, defaultEncoding: Encoding)
    TextFieldParser(path: str, defaultEncoding: Encoding, detectEncoding: bool)
    TextFieldParser(stream: Stream)
    TextFieldParser(stream: Stream, defaultEncoding: Encoding)
    TextFieldParser(stream: Stream, defaultEncoding: Encoding, detectEncoding: bool)
    TextFieldParser(stream: Stream, defaultEncoding: Encoding, detectEncoding: bool, leaveOpen: bool)
    TextFieldParser(reader: TextReader)
    """
    @property
    def CommentTokens(self) -> Array:
        """
        Get: CommentTokens(self: TextFieldParser) -> Array[str]
        Set: CommentTokens(self: TextFieldParser) = value
        """
        ...

    @property
    def Delimiters(self) -> Array:
        """
        Get: Delimiters(self: TextFieldParser) -> Array[str]
        Set: Delimiters(self: TextFieldParser) = value
        """
        ...

    @property
    def EndOfData(self) -> bool:
        """ Get: EndOfData(self: TextFieldParser) -> bool """
        ...

    @property
    def ErrorLine(self) -> str:
        """ Get: ErrorLine(self: TextFieldParser) -> str """
        ...

    @property
    def ErrorLineNumber(self) -> Int64:
        """ Get: ErrorLineNumber(self: TextFieldParser) -> Int64 """
        ...

    @property
    def FieldWidths(self) -> Array:
        """
        Get: FieldWidths(self: TextFieldParser) -> Array[int]
        Set: FieldWidths(self: TextFieldParser) = value
        """
        ...

    @property
    def HasFieldsEnclosedInQuotes(self) -> bool:
        """
        Get: HasFieldsEnclosedInQuotes(self: TextFieldParser) -> bool
        Set: HasFieldsEnclosedInQuotes(self: TextFieldParser) = value
        """
        ...

    @property
    def LineNumber(self) -> Int64:
        """ Get: LineNumber(self: TextFieldParser) -> Int64 """
        ...

    @property
    def TextFieldType(self) -> FieldType:
        """
        Get: TextFieldType(self: TextFieldParser) -> FieldType
        Set: TextFieldType(self: TextFieldParser) = value
        """
        ...

    @property
    def TrimWhiteSpace(self) -> bool:
        """
        Get: TrimWhiteSpace(self: TextFieldParser) -> bool
        Set: TrimWhiteSpace(self: TextFieldParser) = value
        """
        ...


    def Close(self): # -> 
        """ Close(self: TextFieldParser) """
        ...

    def PeekChars(self, numberOfChars:int) -> str:
        """ PeekChars(self: TextFieldParser, numberOfChars: int) -> str """
        ...

    def ReadFields(self) -> Array:
        """ ReadFields(self: TextFieldParser) -> Array[str] """
        ...

    def ReadLine(self) -> str:
        """ ReadLine(self: TextFieldParser) -> str """
        ...

    def ReadToEnd(self) -> str:
        """ ReadToEnd(self: TextFieldParser) -> str """
        ...

    def SetDelimiters(self, delimiters:Array): # -> 
        """ SetDelimiters(self: TextFieldParser, *delimiters: Array[str]) """
        ...

    def SetFieldWidths(self, fieldWidths:Array): # -> 
        """ SetFieldWidths(self: TextFieldParser, *fieldWidths: Array[int]) """
        ...


class UICancelOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UICancelOption, values: DoNothing (2), ThrowException (3) """
    DoNothing: UICancelOption = ...
    ThrowException: UICancelOption = ...
    value__ = ...


class UIOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UIOption, values: AllDialogs (3), OnlyErrorDialogs (2) """
    AllDialogs: UIOption = ...
    OnlyErrorDialogs: UIOption = ...
    value__ = ...


