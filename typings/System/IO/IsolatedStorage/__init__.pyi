# encoding: utf-8
# module System.IO.IsolatedStorage calls itself IsolatedStorage
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, DateTimeOffset, Enum, IDisposable, Int64, 
    MarshalByRefObject, Type, UInt64)

from System.Collections import IEnumerator

from System.IO import FileAccess, FileMode, FileShare, FileStream

from System.Security import SecurityState

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class INormalizeForIsolatedStorage: # skipped bases: <type 'object'>
    """ no doc """
    def Normalize(self) -> object:
        """ Normalize(self: INormalizeForIsolatedStorage) -> object """
        ...


class IsolatedStorage(MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ApplicationIdentity(self) -> object:
        """ Get: ApplicationIdentity(self: IsolatedStorage) -> object """
        ...

    @property
    def AssemblyIdentity(self) -> object:
        """ Get: AssemblyIdentity(self: IsolatedStorage) -> object """
        ...

    @property
    def AvailableFreeSpace(self) -> Int64:
        """ Get: AvailableFreeSpace(self: IsolatedStorage) -> Int64 """
        ...

    @property
    def CurrentSize(self) -> UInt64:
        """ Get: CurrentSize(self: IsolatedStorage) -> UInt64 """
        ...

    @property
    def DomainIdentity(self) -> object:
        """ Get: DomainIdentity(self: IsolatedStorage) -> object """
        ...

    @property
    def MaximumSize(self) -> UInt64:
        """ Get: MaximumSize(self: IsolatedStorage) -> UInt64 """
        ...

    @property
    def Quota(self) -> Int64:
        """ Get: Quota(self: IsolatedStorage) -> Int64 """
        ...

    @property
    def Scope(self) -> IsolatedStorageScope:
        """ Get: Scope(self: IsolatedStorage) -> IsolatedStorageScope """
        ...

    @property
    def SeparatorExternal(self):
        ...

    @property
    def SeparatorInternal(self):
        ...

    @property
    def UsedSize(self) -> Int64:
        """ Get: UsedSize(self: IsolatedStorage) -> Int64 """
        ...


    def GetPermission(self, *args): #cannot find CLR method
        """ GetPermission(self: IsolatedStorage, ps: PermissionSet) -> IsolatedStoragePermission """
        ...

    def IncreaseQuotaTo(self, newQuotaSize:Int64) -> bool:
        """ IncreaseQuotaTo(self: IsolatedStorage, newQuotaSize: Int64) -> bool """
        ...

    def InitStore(self, *args): #cannot find CLR method
        """ InitStore(self: IsolatedStorage, scope: IsolatedStorageScope, domainEvidenceType: Type, assemblyEvidenceType: Type)InitStore(self: IsolatedStorage, scope: IsolatedStorageScope, appEvidenceType: Type) """
        ...

    def Remove(self): # -> 
        """ Remove(self: IsolatedStorage) """
        ...


class IsolatedStorageException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    IsolatedStorageException()
    IsolatedStorageException(message: str)
    IsolatedStorageException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class IsolatedStorageFile(IDisposable, IsolatedStorage): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsEnabled(self) -> bool:
        """ Get: IsEnabled() -> bool """
        ...


    def Close(self): # -> 
        """ Close(self: IsolatedStorageFile) """
        ...

    def CopyFile(self, sourceFileName:str, destinationFileName:str, overwrite:bool = ...): # -> 
        """ CopyFile(self: IsolatedStorageFile, sourceFileName: str, destinationFileName: str)CopyFile(self: IsolatedStorageFile, sourceFileName: str, destinationFileName: str, overwrite: bool) """
        ...

    def CreateDirectory(self, dir:str): # -> 
        """ CreateDirectory(self: IsolatedStorageFile, dir: str) """
        ...

    def CreateFile(self, path:str) -> IsolatedStorageFileStream:
        """ CreateFile(self: IsolatedStorageFile, path: str) -> IsolatedStorageFileStream """
        ...

    def DeleteDirectory(self, dir:str): # -> 
        """ DeleteDirectory(self: IsolatedStorageFile, dir: str) """
        ...

    def DeleteFile(self, file:str): # -> 
        """ DeleteFile(self: IsolatedStorageFile, file: str) """
        ...

    def DirectoryExists(self, path:str) -> bool:
        """ DirectoryExists(self: IsolatedStorageFile, path: str) -> bool """
        ...

    def FileExists(self, path:str) -> bool:
        """ FileExists(self: IsolatedStorageFile, path: str) -> bool """
        ...

    def GetCreationTime(self, path:str) -> DateTimeOffset:
        """ GetCreationTime(self: IsolatedStorageFile, path: str) -> DateTimeOffset """
        ...

    def GetDirectoryNames(self, searchPattern:str = ...) -> Array:
        """
        GetDirectoryNames(self: IsolatedStorageFile) -> Array[str]
        GetDirectoryNames(self: IsolatedStorageFile, searchPattern: str) -> Array[str]
        """
        ...

    @staticmethod
    def GetEnumerator(scope:IsolatedStorageScope) -> IEnumerator:
        """ GetEnumerator(scope: IsolatedStorageScope) -> IEnumerator """
        ...

    def GetFileNames(self, searchPattern:str = ...) -> Array:
        """
        GetFileNames(self: IsolatedStorageFile) -> Array[str]
        GetFileNames(self: IsolatedStorageFile, searchPattern: str) -> Array[str]
        """
        ...

    def GetLastAccessTime(self, path:str) -> DateTimeOffset:
        """ GetLastAccessTime(self: IsolatedStorageFile, path: str) -> DateTimeOffset """
        ...

    def GetLastWriteTime(self, path:str) -> DateTimeOffset:
        """ GetLastWriteTime(self: IsolatedStorageFile, path: str) -> DateTimeOffset """
        ...

    @staticmethod
    def GetMachineStoreForApplication() -> IsolatedStorageFile:
        """ GetMachineStoreForApplication() -> IsolatedStorageFile """
        ...

    @staticmethod
    def GetMachineStoreForAssembly() -> IsolatedStorageFile:
        """ GetMachineStoreForAssembly() -> IsolatedStorageFile """
        ...

    @staticmethod
    def GetMachineStoreForDomain() -> IsolatedStorageFile:
        """ GetMachineStoreForDomain() -> IsolatedStorageFile """
        ...

    @staticmethod
    def GetStore(scope:IsolatedStorageScope, *__args:Type) -> IsolatedStorageFile:
        """
        GetStore(scope: IsolatedStorageScope, domainEvidenceType: Type, assemblyEvidenceType: Type) -> IsolatedStorageFile
        GetStore(scope: IsolatedStorageScope, domainIdentity: object, assemblyIdentity: object) -> IsolatedStorageFile
        GetStore(scope: IsolatedStorageScope, domainEvidence: Evidence, domainEvidenceType: Type, assemblyEvidence: Evidence, assemblyEvidenceType: Type) -> IsolatedStorageFile
        GetStore(scope: IsolatedStorageScope, applicationEvidenceType: Type) -> IsolatedStorageFile
        GetStore(scope: IsolatedStorageScope, applicationIdentity: object) -> IsolatedStorageFile
        """
        ...

    @staticmethod
    def GetUserStoreForApplication() -> IsolatedStorageFile:
        """ GetUserStoreForApplication() -> IsolatedStorageFile """
        ...

    @staticmethod
    def GetUserStoreForAssembly() -> IsolatedStorageFile:
        """ GetUserStoreForAssembly() -> IsolatedStorageFile """
        ...

    @staticmethod
    def GetUserStoreForDomain() -> IsolatedStorageFile:
        """ GetUserStoreForDomain() -> IsolatedStorageFile """
        ...

    @staticmethod
    def GetUserStoreForSite() -> IsolatedStorageFile:
        """ GetUserStoreForSite() -> IsolatedStorageFile """
        ...

    def MoveDirectory(self, sourceDirectoryName:str, destinationDirectoryName:str): # -> 
        """ MoveDirectory(self: IsolatedStorageFile, sourceDirectoryName: str, destinationDirectoryName: str) """
        ...

    def MoveFile(self, sourceFileName:str, destinationFileName:str): # -> 
        """ MoveFile(self: IsolatedStorageFile, sourceFileName: str, destinationFileName: str) """
        ...

    def OpenFile(self, path:str, mode:FileMode, access:FileAccess = ..., share:FileShare = ...) -> IsolatedStorageFileStream:
        """
        OpenFile(self: IsolatedStorageFile, path: str, mode: FileMode) -> IsolatedStorageFileStream
        OpenFile(self: IsolatedStorageFile, path: str, mode: FileMode, access: FileAccess) -> IsolatedStorageFileStream
        OpenFile(self: IsolatedStorageFile, path: str, mode: FileMode, access: FileAccess, share: FileShare) -> IsolatedStorageFileStream
        """
        ...



class IsolatedStorageFileStream(FileStream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    IsolatedStorageFileStream(path: str, mode: FileMode)
    IsolatedStorageFileStream(path: str, mode: FileMode, isf: IsolatedStorageFile)
    IsolatedStorageFileStream(path: str, mode: FileMode, access: FileAccess)
    IsolatedStorageFileStream(path: str, mode: FileMode, access: FileAccess, isf: IsolatedStorageFile)
    IsolatedStorageFileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare)
    IsolatedStorageFileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare, isf: IsolatedStorageFile)
    IsolatedStorageFileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int)
    IsolatedStorageFileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int, isf: IsolatedStorageFile)
    """
    pass

class IsolatedStorageScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) IsolatedStorageScope, values: Application (32), Assembly (4), Domain (2), Machine (16), None (0), Roaming (8), User (1) """
    Application: IsolatedStorageScope = ...
    Assembly: IsolatedStorageScope = ...
    Domain: IsolatedStorageScope = ...
    Machine: IsolatedStorageScope = ...
    Roaming: IsolatedStorageScope = ...
    User: IsolatedStorageScope = ...
    value__ = ...


class IsolatedStorageSecurityOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum IsolatedStorageSecurityOptions, values: IncreaseQuotaForApplication (4) """
    IncreaseQuotaForApplication: IsolatedStorageSecurityOptions = ...
    value__ = ...


class IsolatedStorageSecurityState(SecurityState): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Options(self) -> IsolatedStorageSecurityOptions:
        """ Get: Options(self: IsolatedStorageSecurityState) -> IsolatedStorageSecurityOptions """
        ...

    @property
    def Quota(self) -> Int64:
        """
        Get: Quota(self: IsolatedStorageSecurityState) -> Int64
        Set: Quota(self: IsolatedStorageSecurityState) = value
        """
        ...

    @property
    def UsedSize(self) -> Int64:
        """ Get: UsedSize(self: IsolatedStorageSecurityState) -> Int64 """
        ...



