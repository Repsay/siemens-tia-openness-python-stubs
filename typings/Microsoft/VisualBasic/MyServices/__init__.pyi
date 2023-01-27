# encoding: utf-8
# module Microsoft.VisualBasic.MyServices calls itself MyServices
# from Microsoft.VisualBasic, Version=10.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic.FileIO import (DeleteDirectoryOption, 
    RecycleOption, TextFieldParser, UICancelOption, UIOption)

from Microsoft.Win32 import RegistryKey, RegistryValueKind

from System import Array

from System.Collections.ObjectModel import ReadOnlyCollection

from System.Collections.Specialized import StringCollection

from System.Drawing import Image

from System.IO import (DirectoryInfo, DriveInfo, FileInfo, SearchOption, 
    Stream, StreamReader, StreamWriter)

from System.Text import Encoding

from System.Windows.Forms import DataObject, IDataObject, TextDataFormat


# no functions
# classes

class ClipboardProxy: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Clear(self): # -> 
        """ Clear(self: ClipboardProxy) """
        ...

    def ContainsAudio(self) -> bool:
        """ ContainsAudio(self: ClipboardProxy) -> bool """
        ...

    def ContainsData(self, format:str) -> bool:
        """ ContainsData(self: ClipboardProxy, format: str) -> bool """
        ...

    def ContainsFileDropList(self) -> bool:
        """ ContainsFileDropList(self: ClipboardProxy) -> bool """
        ...

    def ContainsImage(self) -> bool:
        """ ContainsImage(self: ClipboardProxy) -> bool """
        ...

    def ContainsText(self, format:TextDataFormat = ...) -> bool:
        """
        ContainsText(self: ClipboardProxy) -> bool
        ContainsText(self: ClipboardProxy, format: TextDataFormat) -> bool
        """
        ...

    def GetAudioStream(self) -> Stream:
        """ GetAudioStream(self: ClipboardProxy) -> Stream """
        ...

    def GetData(self, format:str) -> object:
        """ GetData(self: ClipboardProxy, format: str) -> object """
        ...

    def GetDataObject(self) -> IDataObject:
        """ GetDataObject(self: ClipboardProxy) -> IDataObject """
        ...

    def GetFileDropList(self) -> StringCollection:
        """ GetFileDropList(self: ClipboardProxy) -> StringCollection """
        ...

    def GetImage(self) -> Image:
        """ GetImage(self: ClipboardProxy) -> Image """
        ...

    def GetText(self, format:TextDataFormat = ...) -> str:
        """
        GetText(self: ClipboardProxy) -> str
        GetText(self: ClipboardProxy, format: TextDataFormat) -> str
        """
        ...

    def SetAudio(self, *__args:Array): # -> 
        """ SetAudio(self: ClipboardProxy, audioBytes: Array[Byte])SetAudio(self: ClipboardProxy, audioStream: Stream) """
        ...

    def SetData(self, format:str, data:object): # -> 
        """ SetData(self: ClipboardProxy, format: str, data: object) """
        ...

    def SetDataObject(self, data:DataObject): # -> 
        """ SetDataObject(self: ClipboardProxy, data: DataObject) """
        ...

    def SetFileDropList(self, filePaths:StringCollection): # -> 
        """ SetFileDropList(self: ClipboardProxy, filePaths: StringCollection) """
        ...

    def SetImage(self, image:Image): # -> 
        """ SetImage(self: ClipboardProxy, image: Image) """
        ...

    def SetText(self, text:str, format:TextDataFormat = ...): # -> 
        """ SetText(self: ClipboardProxy, text: str)SetText(self: ClipboardProxy, text: str, format: TextDataFormat) """
        ...


class FileSystemProxy: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CurrentDirectory(self) -> str:
        """
        Get: CurrentDirectory(self: FileSystemProxy) -> str
        Set: CurrentDirectory(self: FileSystemProxy) = value
        """
        ...

    @property
    def Drives(self) -> ReadOnlyCollection:
        """ Get: Drives(self: FileSystemProxy) -> ReadOnlyCollection[DriveInfo] """
        ...

    @property
    def SpecialDirectories(self) -> SpecialDirectoriesProxy:
        """ Get: SpecialDirectories(self: FileSystemProxy) -> SpecialDirectoriesProxy """
        ...


    def CombinePath(self, baseDirectory:str, relativePath:str) -> str:
        """ CombinePath(self: FileSystemProxy, baseDirectory: str, relativePath: str) -> str """
        ...

    def CopyDirectory(self, sourceDirectoryName:str, destinationDirectoryName:str, *__args:bool): # -> 
        """ CopyDirectory(self: FileSystemProxy, sourceDirectoryName: str, destinationDirectoryName: str)CopyDirectory(self: FileSystemProxy, sourceDirectoryName: str, destinationDirectoryName: str, overwrite: bool)CopyDirectory(self: FileSystemProxy, sourceDirectoryName: str, destinationDirectoryName: str, showUI: UIOption)CopyDirectory(self: FileSystemProxy, sourceDirectoryName: str, destinationDirectoryName: str, showUI: UIOption, onUserCancel: UICancelOption) """
        ...

    def CopyFile(self, sourceFileName:str, destinationFileName:str, *__args:bool): # -> 
        """ CopyFile(self: FileSystemProxy, sourceFileName: str, destinationFileName: str)CopyFile(self: FileSystemProxy, sourceFileName: str, destinationFileName: str, overwrite: bool)CopyFile(self: FileSystemProxy, sourceFileName: str, destinationFileName: str, showUI: UIOption)CopyFile(self: FileSystemProxy, sourceFileName: str, destinationFileName: str, showUI: UIOption, onUserCancel: UICancelOption) """
        ...

    def CreateDirectory(self, directory:str): # -> 
        """ CreateDirectory(self: FileSystemProxy, directory: str) """
        ...

    def DeleteDirectory(self, directory:str, *__args:DeleteDirectoryOption): # -> 
        """ DeleteDirectory(self: FileSystemProxy, directory: str, onDirectoryNotEmpty: DeleteDirectoryOption)DeleteDirectory(self: FileSystemProxy, directory: str, showUI: UIOption, recycle: RecycleOption)DeleteDirectory(self: FileSystemProxy, directory: str, showUI: UIOption, recycle: RecycleOption, onUserCancel: UICancelOption) """
        ...

    def DeleteFile(self, file:str, showUI:UIOption = ..., recycle:RecycleOption = ..., onUserCancel:UICancelOption = ...): # -> 
        """ DeleteFile(self: FileSystemProxy, file: str)DeleteFile(self: FileSystemProxy, file: str, showUI: UIOption, recycle: RecycleOption)DeleteFile(self: FileSystemProxy, file: str, showUI: UIOption, recycle: RecycleOption, onUserCancel: UICancelOption) """
        ...

    def DirectoryExists(self, directory:str) -> bool:
        """ DirectoryExists(self: FileSystemProxy, directory: str) -> bool """
        ...

    def FileExists(self, file:str) -> bool:
        """ FileExists(self: FileSystemProxy, file: str) -> bool """
        ...

    def FindInFiles(self, directory:str, containsText:str, ignoreCase:bool, searchType:SearchOption, fileWildcards:Array = ...) -> ReadOnlyCollection:
        """
        FindInFiles(self: FileSystemProxy, directory: str, containsText: str, ignoreCase: bool, searchType: SearchOption) -> ReadOnlyCollection[str]
        FindInFiles(self: FileSystemProxy, directory: str, containsText: str, ignoreCase: bool, searchType: SearchOption, *fileWildcards: Array[str]) -> ReadOnlyCollection[str]
        """
        ...

    def GetDirectories(self, directory:str, searchType:SearchOption = ..., wildcards:Array = ...) -> ReadOnlyCollection:
        """
        GetDirectories(self: FileSystemProxy, directory: str) -> ReadOnlyCollection[str]
        GetDirectories(self: FileSystemProxy, directory: str, searchType: SearchOption, *wildcards: Array[str]) -> ReadOnlyCollection[str]
        """
        ...

    def GetDirectoryInfo(self, directory:str) -> DirectoryInfo:
        """ GetDirectoryInfo(self: FileSystemProxy, directory: str) -> DirectoryInfo """
        ...

    def GetDriveInfo(self, drive:str) -> DriveInfo:
        """ GetDriveInfo(self: FileSystemProxy, drive: str) -> DriveInfo """
        ...

    def GetFileInfo(self, file:str) -> FileInfo:
        """ GetFileInfo(self: FileSystemProxy, file: str) -> FileInfo """
        ...

    def GetFiles(self, directory:str, searchType:SearchOption = ..., wildcards:Array = ...) -> ReadOnlyCollection:
        """
        GetFiles(self: FileSystemProxy, directory: str) -> ReadOnlyCollection[str]
        GetFiles(self: FileSystemProxy, directory: str, searchType: SearchOption, *wildcards: Array[str]) -> ReadOnlyCollection[str]
        """
        ...

    def GetName(self, path:str) -> str:
        """ GetName(self: FileSystemProxy, path: str) -> str """
        ...

    def GetParentPath(self, path:str) -> str:
        """ GetParentPath(self: FileSystemProxy, path: str) -> str """
        ...

    def GetTempFileName(self) -> str:
        """ GetTempFileName(self: FileSystemProxy) -> str """
        ...

    def MoveDirectory(self, sourceDirectoryName:str, destinationDirectoryName:str, *__args:bool): # -> 
        """ MoveDirectory(self: FileSystemProxy, sourceDirectoryName: str, destinationDirectoryName: str)MoveDirectory(self: FileSystemProxy, sourceDirectoryName: str, destinationDirectoryName: str, overwrite: bool)MoveDirectory(self: FileSystemProxy, sourceDirectoryName: str, destinationDirectoryName: str, showUI: UIOption)MoveDirectory(self: FileSystemProxy, sourceDirectoryName: str, destinationDirectoryName: str, showUI: UIOption, onUserCancel: UICancelOption) """
        ...

    def MoveFile(self, sourceFileName:str, destinationFileName:str, *__args:bool): # -> 
        """ MoveFile(self: FileSystemProxy, sourceFileName: str, destinationFileName: str)MoveFile(self: FileSystemProxy, sourceFileName: str, destinationFileName: str, overwrite: bool)MoveFile(self: FileSystemProxy, sourceFileName: str, destinationFileName: str, showUI: UIOption)MoveFile(self: FileSystemProxy, sourceFileName: str, destinationFileName: str, showUI: UIOption, onUserCancel: UICancelOption) """
        ...

    def OpenTextFieldParser(self, file:str, *__args:Array) -> TextFieldParser:
        """
        OpenTextFieldParser(self: FileSystemProxy, file: str) -> TextFieldParser
        OpenTextFieldParser(self: FileSystemProxy, file: str, *delimiters: Array[str]) -> TextFieldParser
        OpenTextFieldParser(self: FileSystemProxy, file: str, *fieldWidths: Array[int]) -> TextFieldParser
        """
        ...

    def OpenTextFileReader(self, file:str, encoding:Encoding = ...) -> StreamReader:
        """
        OpenTextFileReader(self: FileSystemProxy, file: str) -> StreamReader
        OpenTextFileReader(self: FileSystemProxy, file: str, encoding: Encoding) -> StreamReader
        """
        ...

    def OpenTextFileWriter(self, file:str, append:bool, encoding:Encoding = ...) -> StreamWriter:
        """
        OpenTextFileWriter(self: FileSystemProxy, file: str, append: bool) -> StreamWriter
        OpenTextFileWriter(self: FileSystemProxy, file: str, append: bool, encoding: Encoding) -> StreamWriter
        """
        ...

    def ReadAllBytes(self, file:str) -> Array:
        """ ReadAllBytes(self: FileSystemProxy, file: str) -> Array[Byte] """
        ...

    def ReadAllText(self, file:str, encoding:Encoding = ...) -> str:
        """
        ReadAllText(self: FileSystemProxy, file: str) -> str
        ReadAllText(self: FileSystemProxy, file: str, encoding: Encoding) -> str
        """
        ...

    def RenameDirectory(self, directory:str, newName:str): # -> 
        """ RenameDirectory(self: FileSystemProxy, directory: str, newName: str) """
        ...

    def RenameFile(self, file:str, newName:str): # -> 
        """ RenameFile(self: FileSystemProxy, file: str, newName: str) """
        ...

    def WriteAllBytes(self, file:str, data:Array, append:bool): # -> 
        """ WriteAllBytes(self: FileSystemProxy, file: str, data: Array[Byte], append: bool) """
        ...

    def WriteAllText(self, file:str, text:str, append:bool, encoding:Encoding = ...): # -> 
        """ WriteAllText(self: FileSystemProxy, file: str, text: str, append: bool)WriteAllText(self: FileSystemProxy, file: str, text: str, append: bool, encoding: Encoding) """
        ...


class RegistryProxy: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ClassesRoot(self) -> RegistryKey:
        """ Get: ClassesRoot(self: RegistryProxy) -> RegistryKey """
        ...

    @property
    def CurrentConfig(self) -> RegistryKey:
        """ Get: CurrentConfig(self: RegistryProxy) -> RegistryKey """
        ...

    @property
    def CurrentUser(self) -> RegistryKey:
        """ Get: CurrentUser(self: RegistryProxy) -> RegistryKey """
        ...

    @property
    def DynData(self) -> RegistryKey:
        """ Get: DynData(self: RegistryProxy) -> RegistryKey """
        ...

    @property
    def LocalMachine(self) -> RegistryKey:
        """ Get: LocalMachine(self: RegistryProxy) -> RegistryKey """
        ...

    @property
    def PerformanceData(self) -> RegistryKey:
        """ Get: PerformanceData(self: RegistryProxy) -> RegistryKey """
        ...

    @property
    def Users(self) -> RegistryKey:
        """ Get: Users(self: RegistryProxy) -> RegistryKey """
        ...


    def GetValue(self, keyName:str, valueName:str, defaultValue:object) -> object:
        """ GetValue(self: RegistryProxy, keyName: str, valueName: str, defaultValue: object) -> object """
        ...

    def SetValue(self, keyName:str, valueName:str, value:object, valueKind:RegistryValueKind = ...): # -> 
        """ SetValue(self: RegistryProxy, keyName: str, valueName: str, value: object)SetValue(self: RegistryProxy, keyName: str, valueName: str, value: object, valueKind: RegistryValueKind) """
        ...


class SpecialDirectoriesProxy: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AllUsersApplicationData(self) -> str:
        """ Get: AllUsersApplicationData(self: SpecialDirectoriesProxy) -> str """
        ...

    @property
    def CurrentUserApplicationData(self) -> str:
        """ Get: CurrentUserApplicationData(self: SpecialDirectoriesProxy) -> str """
        ...

    @property
    def Desktop(self) -> str:
        """ Get: Desktop(self: SpecialDirectoriesProxy) -> str """
        ...

    @property
    def MyDocuments(self) -> str:
        """ Get: MyDocuments(self: SpecialDirectoriesProxy) -> str """
        ...

    @property
    def MyMusic(self) -> str:
        """ Get: MyMusic(self: SpecialDirectoriesProxy) -> str """
        ...

    @property
    def MyPictures(self) -> str:
        """ Get: MyPictures(self: SpecialDirectoriesProxy) -> str """
        ...

    @property
    def ProgramFiles(self) -> str:
        """ Get: ProgramFiles(self: SpecialDirectoriesProxy) -> str """
        ...

    @property
    def Programs(self) -> str:
        """ Get: Programs(self: SpecialDirectoriesProxy) -> str """
        ...

    @property
    def Temp(self) -> str:
        """ Get: Temp(self: SpecialDirectoriesProxy) -> str """
        ...



# variables with complex values

