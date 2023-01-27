# encoding: utf-8
# module System.IO.MemoryMappedFiles calls itself MemoryMappedFiles
# from System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Win32.SafeHandles import (SafeMemoryMappedFileHandle, 
    SafeMemoryMappedViewHandle)

from System import Enum, IDisposable, Int64

from System.IO import (HandleInheritability, UnmanagedMemoryAccessor, 
    UnmanagedMemoryStream)

from System.Security.AccessControl import ObjectSecurity

"""The following names are not found in the module: field#
"""

# no functions
# classes

class MemoryMappedFile(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SafeMemoryMappedFileHandle(self) -> SafeMemoryMappedFileHandle:
        """ Get: SafeMemoryMappedFileHandle(self: MemoryMappedFile) -> SafeMemoryMappedFileHandle """
        ...


    @staticmethod
    def CreateFromFile(*__args:str) -> MemoryMappedFile:
        """
        CreateFromFile(path: str) -> MemoryMappedFile
        CreateFromFile(path: str, mode: FileMode) -> MemoryMappedFile
        CreateFromFile(path: str, mode: FileMode, mapName: str) -> MemoryMappedFile
        CreateFromFile(path: str, mode: FileMode, mapName: str, capacity: Int64) -> MemoryMappedFile
        CreateFromFile(path: str, mode: FileMode, mapName: str, capacity: Int64, access: MemoryMappedFileAccess) -> MemoryMappedFile
        CreateFromFile(fileStream: FileStream, mapName: str, capacity: Int64, access: MemoryMappedFileAccess, inheritability: HandleInheritability, leaveOpen: bool) -> MemoryMappedFile
        CreateFromFile(fileStream: FileStream, mapName: str, capacity: Int64, access: MemoryMappedFileAccess, memoryMappedFileSecurity: MemoryMappedFileSecurity, inheritability: HandleInheritability, leaveOpen: bool) -> MemoryMappedFile
        """
        ...

    @staticmethod
    def CreateNew(mapName:str, capacity:Int64, access:MemoryMappedFileAccess = ..., options:MemoryMappedFileOptions = ..., *__args:HandleInheritability) -> MemoryMappedFile:
        """
        CreateNew(mapName: str, capacity: Int64) -> MemoryMappedFile
        CreateNew(mapName: str, capacity: Int64, access: MemoryMappedFileAccess) -> MemoryMappedFile
        CreateNew(mapName: str, capacity: Int64, access: MemoryMappedFileAccess, options: MemoryMappedFileOptions, inheritability: HandleInheritability) -> MemoryMappedFile
        CreateNew(mapName: str, capacity: Int64, access: MemoryMappedFileAccess, options: MemoryMappedFileOptions, memoryMappedFileSecurity: MemoryMappedFileSecurity, inheritability: HandleInheritability) -> MemoryMappedFile
        """
        ...

    @staticmethod
    def CreateOrOpen(mapName:str, capacity:Int64, access:MemoryMappedFileAccess = ..., options:MemoryMappedFileOptions = ..., *__args:HandleInheritability) -> MemoryMappedFile:
        """
        CreateOrOpen(mapName: str, capacity: Int64) -> MemoryMappedFile
        CreateOrOpen(mapName: str, capacity: Int64, access: MemoryMappedFileAccess) -> MemoryMappedFile
        CreateOrOpen(mapName: str, capacity: Int64, access: MemoryMappedFileAccess, options: MemoryMappedFileOptions, inheritability: HandleInheritability) -> MemoryMappedFile
        CreateOrOpen(mapName: str, capacity: Int64, access: MemoryMappedFileAccess, options: MemoryMappedFileOptions, memoryMappedFileSecurity: MemoryMappedFileSecurity, inheritability: HandleInheritability) -> MemoryMappedFile
        """
        ...

    def CreateViewAccessor(self, offset:Int64 = ..., size:Int64 = ..., access:MemoryMappedFileAccess = ...) -> MemoryMappedViewAccessor:
        """
        CreateViewAccessor(self: MemoryMappedFile) -> MemoryMappedViewAccessor
        CreateViewAccessor(self: MemoryMappedFile, offset: Int64, size: Int64) -> MemoryMappedViewAccessor
        CreateViewAccessor(self: MemoryMappedFile, offset: Int64, size: Int64, access: MemoryMappedFileAccess) -> MemoryMappedViewAccessor
        """
        ...

    def CreateViewStream(self, offset:Int64 = ..., size:Int64 = ..., access:MemoryMappedFileAccess = ...) -> MemoryMappedViewStream:
        """
        CreateViewStream(self: MemoryMappedFile) -> MemoryMappedViewStream
        CreateViewStream(self: MemoryMappedFile, offset: Int64, size: Int64) -> MemoryMappedViewStream
        CreateViewStream(self: MemoryMappedFile, offset: Int64, size: Int64, access: MemoryMappedFileAccess) -> MemoryMappedViewStream
        """
        ...

    def GetAccessControl(self) -> MemoryMappedFileSecurity:
        """ GetAccessControl(self: MemoryMappedFile) -> MemoryMappedFileSecurity """
        ...

    @staticmethod
    def OpenExisting(mapName:str, desiredAccessRights:MemoryMappedFileRights = ..., inheritability:HandleInheritability = ...) -> MemoryMappedFile:
        """
        OpenExisting(mapName: str) -> MemoryMappedFile
        OpenExisting(mapName: str, desiredAccessRights: MemoryMappedFileRights) -> MemoryMappedFile
        OpenExisting(mapName: str, desiredAccessRights: MemoryMappedFileRights, inheritability: HandleInheritability) -> MemoryMappedFile
        """
        ...

    def SetAccessControl(self, memoryMappedFileSecurity:MemoryMappedFileSecurity): # -> 
        """ SetAccessControl(self: MemoryMappedFile, memoryMappedFileSecurity: MemoryMappedFileSecurity) """
        ...


class MemoryMappedFileAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MemoryMappedFileAccess, values: CopyOnWrite (3), Read (1), ReadExecute (4), ReadWrite (0), ReadWriteExecute (5), Write (2) """
    CopyOnWrite: MemoryMappedFileAccess = ...
    Read: MemoryMappedFileAccess = ...
    ReadExecute: MemoryMappedFileAccess = ...
    ReadWrite: MemoryMappedFileAccess = ...
    ReadWriteExecute: MemoryMappedFileAccess = ...
    value__ = ...
    Write: MemoryMappedFileAccess = ...


class MemoryMappedFileOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) MemoryMappedFileOptions, values: DelayAllocatePages (67108864), None (0) """
    DelayAllocatePages: MemoryMappedFileOptions = ...
    value__ = ...


class MemoryMappedFileRights(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) MemoryMappedFileRights, values: AccessSystemSecurity (16777216), ChangePermissions (262144), CopyOnWrite (1), Delete (65536), Execute (8), FullControl (983055), Read (4), ReadExecute (12), ReadPermissions (131072), ReadWrite (6), ReadWriteExecute (14), TakeOwnership (524288), Write (2) """
    AccessSystemSecurity: MemoryMappedFileRights = ...
    ChangePermissions: MemoryMappedFileRights = ...
    CopyOnWrite: MemoryMappedFileRights = ...
    Delete: MemoryMappedFileRights = ...
    Execute: MemoryMappedFileRights = ...
    FullControl: MemoryMappedFileRights = ...
    Read: MemoryMappedFileRights = ...
    ReadExecute: MemoryMappedFileRights = ...
    ReadPermissions: MemoryMappedFileRights = ...
    ReadWrite: MemoryMappedFileRights = ...
    ReadWriteExecute: MemoryMappedFileRights = ...
    TakeOwnership: MemoryMappedFileRights = ...
    value__ = ...
    Write: MemoryMappedFileRights = ...


class MemoryMappedFileSecurity(ObjectSecurity): # skipped bases: <type 'object'>
    """ MemoryMappedFileSecurity() """
    pass

class MemoryMappedViewAccessor(UnmanagedMemoryAccessor): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def PointerOffset(self) -> Int64:
        """ Get: PointerOffset(self: MemoryMappedViewAccessor) -> Int64 """
        ...

    @property
    def SafeMemoryMappedViewHandle(self) -> SafeMemoryMappedViewHandle:
        """ Get: SafeMemoryMappedViewHandle(self: MemoryMappedViewAccessor) -> SafeMemoryMappedViewHandle """
        ...


    def Flush(self): # -> 
        """ Flush(self: MemoryMappedViewAccessor) """
        ...


class MemoryMappedViewStream(UnmanagedMemoryStream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def PointerOffset(self) -> Int64:
        """ Get: PointerOffset(self: MemoryMappedViewStream) -> Int64 """
        ...

    @property
    def SafeMemoryMappedViewHandle(self) -> SafeMemoryMappedViewHandle:
        """ Get: SafeMemoryMappedViewHandle(self: MemoryMappedViewStream) -> SafeMemoryMappedViewHandle """
        ...



