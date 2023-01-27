# encoding: utf-8
# module System.Runtime.InteropServices.WindowsRuntime calls itself WindowsRuntime
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Runtime.WindowsRuntime, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import (Action, Array, Attribute, Byte, EventArgs, IntPtr, Type, 
    UInt32)

from System.Collections import IEnumerable

from System.IO import MemoryStream, Stream

from System.Reflection import Assembly

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, Func, 
    IAgileObject, IAsyncAction, IBuffer, IBufferByteAccess, IMarshal, T)
"""

# no functions
# classes

class AsyncInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Run(taskProvider): # -> IAsyncAction # Not found arg types: {'taskProvider': 'Func'}
        """
        Run(taskProvider: Func[CancellationToken, Task]) -> IAsyncAction
        Run[TProgress](taskProvider: Func[CancellationToken, IProgress[TProgress], Task]) -> IAsyncActionWithProgress[TProgress]
        Run[TResult](taskProvider: Func[CancellationToken, Task[TResult]]) -> IAsyncOperation[TResult]
        Run[(TResult, TProgress)](taskProvider: Func[CancellationToken, IProgress[TProgress], Task[TResult]]) -> IAsyncOperationWithProgress[TResult, TProgress]
        """
        ...

    __all__: list = ...


class DefaultInterfaceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DefaultInterfaceAttribute(defaultInterface: Type) """
    @property
    def DefaultInterface(self) -> Type:
        """ Get: DefaultInterface(self: DefaultInterfaceAttribute) -> Type """
        ...


    def __new__(cls, defaultInterface:Type) -> Self:
        """ __new__(cls: type, defaultInterface: Type) """
        ...


class DesignerNamespaceResolveEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DesignerNamespaceResolveEventArgs(namespaceName: str) """
    @property
    def NamespaceName(self) -> str:
        """ Get: NamespaceName(self: DesignerNamespaceResolveEventArgs) -> str """
        ...

    @property
    def ResolvedAssemblyFiles(self) -> Collection:
        """ Get: ResolvedAssemblyFiles(self: DesignerNamespaceResolveEventArgs) -> Collection[str] """
        ...


    def __new__(cls, namespaceName:str) -> Self:
        """ __new__(cls: type, namespaceName: str) """
        ...


class EventRegistrationToken: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Equals(self, obj:object) -> bool:
        """ Equals(self: EventRegistrationToken, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: EventRegistrationToken) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class EventRegistrationTokenTable: # skipped bases: <type 'object'>, <type 'object'>
    """ EventRegistrationTokenTable[T]() """
    @property
    def InvocationList(self): # -> T
        """
        Get: InvocationList(self: EventRegistrationTokenTable[T]) -> T
        Set: InvocationList(self: EventRegistrationTokenTable[T]) = value
        """
        ...


    def AddEventHandler(self, handler) -> EventRegistrationToken: # Not found arg types: {'handler': 'T'}
        """ AddEventHandler(self: EventRegistrationTokenTable[T], handler: T) -> EventRegistrationToken """
        ...

    @staticmethod
    def GetOrCreateEventRegistrationTokenTable(refEventTable:EventRegistrationTokenTable) -> Tuple_[EventRegistrationTokenTable, EventRegistrationTokenTable]:
        """ GetOrCreateEventRegistrationTokenTable(refEventTable: EventRegistrationTokenTable[T]) -> (EventRegistrationTokenTable[T], EventRegistrationTokenTable[T]) """
        ...

    def RemoveEventHandler(self, *__args:EventRegistrationToken): # -> 
        """ RemoveEventHandler(self: EventRegistrationTokenTable[T], token: EventRegistrationToken)RemoveEventHandler(self: EventRegistrationTokenTable[T], handler: T) """
        ...


class IActivationFactory: # skipped bases: <type 'object'>
    """ no doc """
    def ActivateInstance(self) -> object:
        """ ActivateInstance(self: IActivationFactory) -> object """
        ...


class InterfaceImplementedInVersionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ InterfaceImplementedInVersionAttribute(interfaceType: Type, majorVersion: Byte, minorVersion: Byte, buildVersion: Byte, revisionVersion: Byte) """
    @property
    def BuildVersion(self) -> Byte:
        """ Get: BuildVersion(self: InterfaceImplementedInVersionAttribute) -> Byte """
        ...

    @property
    def InterfaceType(self) -> Type:
        """ Get: InterfaceType(self: InterfaceImplementedInVersionAttribute) -> Type """
        ...

    @property
    def MajorVersion(self) -> Byte:
        """ Get: MajorVersion(self: InterfaceImplementedInVersionAttribute) -> Byte """
        ...

    @property
    def MinorVersion(self) -> Byte:
        """ Get: MinorVersion(self: InterfaceImplementedInVersionAttribute) -> Byte """
        ...

    @property
    def RevisionVersion(self) -> Byte:
        """ Get: RevisionVersion(self: InterfaceImplementedInVersionAttribute) -> Byte """
        ...


    def __new__(cls, interfaceType:Type, majorVersion:Byte, minorVersion:Byte, buildVersion:Byte, revisionVersion:Byte) -> Self:
        """ __new__(cls: type, interfaceType: Type, majorVersion: Byte, minorVersion: Byte, buildVersion: Byte, revisionVersion: Byte) """
        ...


class NamespaceResolveEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ NamespaceResolveEventArgs(namespaceName: str, requestingAssembly: Assembly) """
    @property
    def NamespaceName(self) -> str:
        """ Get: NamespaceName(self: NamespaceResolveEventArgs) -> str """
        ...

    @property
    def RequestingAssembly(self) -> Assembly:
        """ Get: RequestingAssembly(self: NamespaceResolveEventArgs) -> Assembly """
        ...

    @property
    def ResolvedAssemblies(self) -> Collection:
        """ Get: ResolvedAssemblies(self: NamespaceResolveEventArgs) -> Collection[Assembly] """
        ...


    def __new__(cls, namespaceName:str, requestingAssembly:Assembly) -> Self:
        """ __new__(cls: type, namespaceName: str, requestingAssembly: Assembly) """
        ...


class ReadOnlyArrayAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ReadOnlyArrayAttribute() """
    pass

class ReturnValueNameAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ReturnValueNameAttribute(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: ReturnValueNameAttribute) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class WindowsRuntimeBuffer(IAgileObject, IBuffer, IBufferByteAccess, IMarshal): # skipped bases: <type 'object'>
    """ no doc """
    @staticmethod
    def Create(*__args:int): # -> IBuffer
        """
        Create(capacity: int) -> IBuffer
        Create(data: Array[Byte], offset: int, length: int, capacity: int) -> IBuffer
        """
        ...


class WindowsRuntimeBufferExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AsBuffer(source:Array, offset:int = ..., length:int = ..., capacity:int = ...): # -> IBuffer
        """
        AsBuffer(source: Array[Byte]) -> IBuffer
        AsBuffer(source: Array[Byte], offset: int, length: int) -> IBuffer
        AsBuffer(source: Array[Byte], offset: int, length: int, capacity: int) -> IBuffer
        """
        ...

    @staticmethod
    def AsStream(source) -> Stream: # Not found arg types: {'source': 'IBuffer'}
        """ AsStream(source: IBuffer) -> Stream """
        ...

    @staticmethod
    def CopyTo(source:Array, *__args): # ->  # Not found arg types: {'*__args': 'IBuffer'}
        """ CopyTo(source: Array[Byte], destination: IBuffer)CopyTo(source: Array[Byte], sourceIndex: int, destination: IBuffer, destinationIndex: UInt32, count: int)CopyTo(source: IBuffer, destination: Array[Byte])CopyTo(source: IBuffer, sourceIndex: UInt32, destination: Array[Byte], destinationIndex: int, count: int)CopyTo(source: IBuffer, destination: IBuffer)CopyTo(source: IBuffer, sourceIndex: UInt32, destination: IBuffer, destinationIndex: UInt32, count: UInt32) """
        ...

    @staticmethod
    def GetByte(source, byteOffset:UInt32) -> Byte: # Not found arg types: {'source': 'IBuffer'}
        """ GetByte(source: IBuffer, byteOffset: UInt32) -> Byte """
        ...

    @staticmethod
    def GetWindowsRuntimeBuffer(underlyingStream:MemoryStream, positionInStream:int = ..., length:int = ...): # -> IBuffer
        """
        GetWindowsRuntimeBuffer(underlyingStream: MemoryStream) -> IBuffer
        GetWindowsRuntimeBuffer(underlyingStream: MemoryStream, positionInStream: int, length: int) -> IBuffer
        """
        ...

    @staticmethod
    def IsSameData(buffer, otherBuffer) -> bool: # Not found arg types: {'otherBuffer': 'IBuffer', 'buffer': 'IBuffer'}
        """ IsSameData(buffer: IBuffer, otherBuffer: IBuffer) -> bool """
        ...

    @staticmethod
    def ToArray(source, sourceIndex:UInt32 = ..., count:int = ...) -> Array: # Not found arg types: {'source': 'IBuffer'}
        """
        ToArray(source: IBuffer) -> Array[Byte]
        ToArray(source: IBuffer, sourceIndex: UInt32, count: int) -> Array[Byte]
        """
        ...

    __all__: list = ...


class WindowsRuntimeMarshal: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AddEventHandler(addMethod, removeMethod:Action, handler): # ->  # Not found arg types: {'addMethod': 'Func', 'handler': 'T'}
        """ AddEventHandler[T](addMethod: Func[T, EventRegistrationToken], removeMethod: Action[EventRegistrationToken], handler: T) """
        ...

    @staticmethod
    def FreeHString(ptr:IntPtr): # -> 
        """ FreeHString(ptr: IntPtr) """
        ...

    @staticmethod
    def GetActivationFactory(type:Type) -> IActivationFactory:
        """ GetActivationFactory(type: Type) -> IActivationFactory """
        ...

    @staticmethod
    def PtrToStringHString(ptr:IntPtr) -> str:
        """ PtrToStringHString(ptr: IntPtr) -> str """
        ...

    @staticmethod
    def RemoveAllEventHandlers(removeMethod:Action): # -> 
        """ RemoveAllEventHandlers(removeMethod: Action[EventRegistrationToken]) """
        ...

    @staticmethod
    def RemoveEventHandler(removeMethod:Action, handler): # ->  # Not found arg types: {'handler': 'T'}
        """ RemoveEventHandler[T](removeMethod: Action[EventRegistrationToken], handler: T) """
        ...

    @staticmethod
    def StringToHString(s:str) -> IntPtr:
        """ StringToHString(s: str) -> IntPtr """
        ...

    __all__: list = ...


class WindowsRuntimeMetadata: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ResolveNamespace(namespaceName:str, *__args:IEnumerable) -> IEnumerable:
        """
        ResolveNamespace(namespaceName: str, packageGraphFilePaths: IEnumerable[str]) -> IEnumerable[str]
        ResolveNamespace(namespaceName: str, windowsSdkFilePath: str, packageGraphFilePaths: IEnumerable[str]) -> IEnumerable[str]
        """
        ...

    DesignerNamespaceResolve = ...
    ReflectionOnlyNamespaceResolve = ...
    __all__: list = ...


class WriteOnlyArrayAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ WriteOnlyArrayAttribute() """
    pass

