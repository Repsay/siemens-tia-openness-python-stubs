# encoding: utf-8
# module System.IO.Pipes calls itself Pipes
# from System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Win32.SafeHandles import SafePipeHandle

from System import (AsyncCallback, Enum, IAsyncResult, MulticastDelegate, 
    Type)

from System.IO import Stream

from System.Security.AccessControl import (AccessControlType, AccessRule, 
    AuditFlags, AuditRule, InheritanceFlags, NativeObjectSecurity, 
    PropagationFlags)

from System.Security.Principal import IdentityReference

from System.Threading import CancellationToken

from System.Threading.Tasks import Task

"""The following names are not found in the module: field#
"""

# no functions
# classes

class PipeStream(Stream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def InBufferSize(self) -> int:
        """ Get: InBufferSize(self: PipeStream) -> int """
        ...

    @property
    def IsAsync(self) -> bool:
        """ Get: IsAsync(self: PipeStream) -> bool """
        ...

    @property
    def IsConnected(self) -> bool:
        """ Get: IsConnected(self: PipeStream) -> bool """
        ...

    @property
    def IsHandleExposed(self):
        ...

    @property
    def IsMessageComplete(self) -> bool:
        """ Get: IsMessageComplete(self: PipeStream) -> bool """
        ...

    @property
    def OutBufferSize(self) -> int:
        """ Get: OutBufferSize(self: PipeStream) -> int """
        ...

    @property
    def ReadMode(self) -> PipeTransmissionMode:
        """
        Get: ReadMode(self: PipeStream) -> PipeTransmissionMode
        Set: ReadMode(self: PipeStream) = value
        """
        ...

    @property
    def SafePipeHandle(self) -> SafePipeHandle:
        """ Get: SafePipeHandle(self: PipeStream) -> SafePipeHandle """
        ...

    @property
    def TransmissionMode(self) -> PipeTransmissionMode:
        """ Get: TransmissionMode(self: PipeStream) -> PipeTransmissionMode """
        ...


    def CheckPipePropertyOperations(self, *args): #cannot find CLR method
        """ CheckPipePropertyOperations(self: PipeStream) """
        ...

    def CheckReadOperations(self, *args): #cannot find CLR method
        """ CheckReadOperations(self: PipeStream) """
        ...

    def CheckWriteOperations(self, *args): #cannot find CLR method
        """ CheckWriteOperations(self: PipeStream) """
        ...

    def GetAccessControl(self) -> PipeSecurity:
        """ GetAccessControl(self: PipeStream) -> PipeSecurity """
        ...

    def InitializeHandle(self, *args): #cannot find CLR method
        """ InitializeHandle(self: PipeStream, handle: SafePipeHandle, isExposed: bool, isAsync: bool) """
        ...

    def SetAccessControl(self, pipeSecurity:PipeSecurity): # -> 
        """ SetAccessControl(self: PipeStream, pipeSecurity: PipeSecurity) """
        ...

    def WaitForPipeDrain(self): # -> 
        """ WaitForPipeDrain(self: PipeStream) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type, direction: PipeDirection, bufferSize: int)
        __new__(cls: type, direction: PipeDirection, transmissionMode: PipeTransmissionMode, outBufferSize: int)
        """
        ...


class AnonymousPipeClientStream(PipeStream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    AnonymousPipeClientStream(pipeHandleAsString: str)
    AnonymousPipeClientStream(direction: PipeDirection, pipeHandleAsString: str)
    AnonymousPipeClientStream(direction: PipeDirection, safePipeHandle: SafePipeHandle)
    """
    pass

class AnonymousPipeServerStream(PipeStream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    AnonymousPipeServerStream()
    AnonymousPipeServerStream(direction: PipeDirection)
    AnonymousPipeServerStream(direction: PipeDirection, inheritability: HandleInheritability)
    AnonymousPipeServerStream(direction: PipeDirection, inheritability: HandleInheritability, bufferSize: int)
    AnonymousPipeServerStream(direction: PipeDirection, inheritability: HandleInheritability, bufferSize: int, pipeSecurity: PipeSecurity)
    AnonymousPipeServerStream(direction: PipeDirection, serverSafePipeHandle: SafePipeHandle, clientSafePipeHandle: SafePipeHandle)
    """
    @property
    def ClientSafePipeHandle(self) -> SafePipeHandle:
        """ Get: ClientSafePipeHandle(self: AnonymousPipeServerStream) -> SafePipeHandle """
        ...


    def DisposeLocalCopyOfClientHandle(self): # -> 
        """ DisposeLocalCopyOfClientHandle(self: AnonymousPipeServerStream) """
        ...

    def GetClientHandleAsString(self) -> str:
        """ GetClientHandleAsString(self: AnonymousPipeServerStream) -> str """
        ...


class NamedPipeClientStream(PipeStream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    NamedPipeClientStream(pipeName: str)
    NamedPipeClientStream(serverName: str, pipeName: str)
    NamedPipeClientStream(serverName: str, pipeName: str, direction: PipeDirection)
    NamedPipeClientStream(serverName: str, pipeName: str, direction: PipeDirection, options: PipeOptions)
    NamedPipeClientStream(serverName: str, pipeName: str, direction: PipeDirection, options: PipeOptions, impersonationLevel: TokenImpersonationLevel)
    NamedPipeClientStream(serverName: str, pipeName: str, direction: PipeDirection, options: PipeOptions, impersonationLevel: TokenImpersonationLevel, inheritability: HandleInheritability)
    NamedPipeClientStream(serverName: str, pipeName: str, desiredAccessRights: PipeAccessRights, options: PipeOptions, impersonationLevel: TokenImpersonationLevel, inheritability: HandleInheritability)
    NamedPipeClientStream(direction: PipeDirection, isAsync: bool, isConnected: bool, safePipeHandle: SafePipeHandle)
    """
    @property
    def NumberOfServerInstances(self) -> int:
        """ Get: NumberOfServerInstances(self: NamedPipeClientStream) -> int """
        ...


    def Connect(self, timeout:int = ...): # -> 
        """ Connect(self: NamedPipeClientStream)Connect(self: NamedPipeClientStream, timeout: int) """
        ...

    def ConnectAsync(self, *__args:int) -> Task:
        """
        ConnectAsync(self: NamedPipeClientStream) -> Task
        ConnectAsync(self: NamedPipeClientStream, timeout: int) -> Task
        ConnectAsync(self: NamedPipeClientStream, cancellationToken: CancellationToken) -> Task
        ConnectAsync(self: NamedPipeClientStream, timeout: int, cancellationToken: CancellationToken) -> Task
        """
        ...


class NamedPipeServerStream(PipeStream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    NamedPipeServerStream(pipeName: str)
    NamedPipeServerStream(pipeName: str, direction: PipeDirection)
    NamedPipeServerStream(pipeName: str, direction: PipeDirection, maxNumberOfServerInstances: int)
    NamedPipeServerStream(pipeName: str, direction: PipeDirection, maxNumberOfServerInstances: int, transmissionMode: PipeTransmissionMode)
    NamedPipeServerStream(pipeName: str, direction: PipeDirection, maxNumberOfServerInstances: int, transmissionMode: PipeTransmissionMode, options: PipeOptions)
    NamedPipeServerStream(pipeName: str, direction: PipeDirection, maxNumberOfServerInstances: int, transmissionMode: PipeTransmissionMode, options: PipeOptions, inBufferSize: int, outBufferSize: int)
    NamedPipeServerStream(pipeName: str, direction: PipeDirection, maxNumberOfServerInstances: int, transmissionMode: PipeTransmissionMode, options: PipeOptions, inBufferSize: int, outBufferSize: int, pipeSecurity: PipeSecurity)
    NamedPipeServerStream(pipeName: str, direction: PipeDirection, maxNumberOfServerInstances: int, transmissionMode: PipeTransmissionMode, options: PipeOptions, inBufferSize: int, outBufferSize: int, pipeSecurity: PipeSecurity, inheritability: HandleInheritability)
    NamedPipeServerStream(pipeName: str, direction: PipeDirection, maxNumberOfServerInstances: int, transmissionMode: PipeTransmissionMode, options: PipeOptions, inBufferSize: int, outBufferSize: int, pipeSecurity: PipeSecurity, inheritability: HandleInheritability, additionalAccessRights: PipeAccessRights)
    NamedPipeServerStream(direction: PipeDirection, isAsync: bool, isConnected: bool, safePipeHandle: SafePipeHandle)
    """
    def BeginWaitForConnection(self, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginWaitForConnection(self: NamedPipeServerStream, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def Disconnect(self): # -> 
        """ Disconnect(self: NamedPipeServerStream) """
        ...

    def EndWaitForConnection(self, asyncResult:IAsyncResult): # -> 
        """ EndWaitForConnection(self: NamedPipeServerStream, asyncResult: IAsyncResult) """
        ...

    def GetImpersonationUserName(self) -> str:
        """ GetImpersonationUserName(self: NamedPipeServerStream) -> str """
        ...

    def RunAsClient(self, impersonationWorker:PipeStreamImpersonationWorker): # -> 
        """ RunAsClient(self: NamedPipeServerStream, impersonationWorker: PipeStreamImpersonationWorker) """
        ...

    def WaitForConnection(self): # -> 
        """ WaitForConnection(self: NamedPipeServerStream) """
        ...

    def WaitForConnectionAsync(self, cancellationToken:CancellationToken = ...) -> Task:
        """
        WaitForConnectionAsync(self: NamedPipeServerStream, cancellationToken: CancellationToken) -> Task
        WaitForConnectionAsync(self: NamedPipeServerStream) -> Task
        """
        ...

    MaxAllowedServerInstances: int = ...


class PipeAccessRights(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PipeAccessRights, values: AccessSystemSecurity (16777216), ChangePermissions (262144), CreateNewInstance (4), Delete (65536), FullControl (2032031), Read (131209), ReadAttributes (128), ReadData (1), ReadExtendedAttributes (8), ReadPermissions (131072), ReadWrite (131483), Synchronize (1048576), TakeOwnership (524288), Write (274), WriteAttributes (256), WriteData (2), WriteExtendedAttributes (16) """
    AccessSystemSecurity: PipeAccessRights = ...
    ChangePermissions: PipeAccessRights = ...
    CreateNewInstance: PipeAccessRights = ...
    Delete: PipeAccessRights = ...
    FullControl: PipeAccessRights = ...
    Read: PipeAccessRights = ...
    ReadAttributes: PipeAccessRights = ...
    ReadData: PipeAccessRights = ...
    ReadExtendedAttributes: PipeAccessRights = ...
    ReadPermissions: PipeAccessRights = ...
    ReadWrite: PipeAccessRights = ...
    Synchronize: PipeAccessRights = ...
    TakeOwnership: PipeAccessRights = ...
    value__ = ...
    Write: PipeAccessRights = ...
    WriteAttributes: PipeAccessRights = ...
    WriteData: PipeAccessRights = ...
    WriteExtendedAttributes: PipeAccessRights = ...


class PipeAccessRule(AccessRule): # skipped bases: <type 'object'>
    """
    PipeAccessRule(identity: str, rights: PipeAccessRights, type: AccessControlType)
    PipeAccessRule(identity: IdentityReference, rights: PipeAccessRights, type: AccessControlType)
    """
    @property
    def PipeAccessRights(self) -> PipeAccessRights:
        """ Get: PipeAccessRights(self: PipeAccessRule) -> PipeAccessRights """
        ...



class PipeAuditRule(AuditRule): # skipped bases: <type 'object'>
    """
    PipeAuditRule(identity: IdentityReference, rights: PipeAccessRights, flags: AuditFlags)
    PipeAuditRule(identity: str, rights: PipeAccessRights, flags: AuditFlags)
    """
    @property
    def PipeAccessRights(self) -> PipeAccessRights:
        """ Get: PipeAccessRights(self: PipeAuditRule) -> PipeAccessRights """
        ...



class PipeDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PipeDirection, values: In (1), InOut (3), Out (2) """
    In: PipeDirection = ...
    InOut: PipeDirection = ...
    Out: PipeDirection = ...
    value__ = ...


class PipeOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PipeOptions, values: Asynchronous (1073741824), None (0), WriteThrough (-2147483648) """
    Asynchronous: PipeOptions = ...
    value__ = ...
    WriteThrough: PipeOptions = ...


class PipeSecurity(NativeObjectSecurity): # skipped bases: <type 'object'>
    """ PipeSecurity() """
    @property
    def AccessRightType(self) -> Type:
        """ Get: AccessRightType(self: PipeSecurity) -> Type """
        ...

    @property
    def AccessRuleType(self) -> Type:
        """ Get: AccessRuleType(self: PipeSecurity) -> Type """
        ...

    @property
    def AuditRuleType(self) -> Type:
        """ Get: AuditRuleType(self: PipeSecurity) -> Type """
        ...


    def AccessRuleFactory(self, identityReference:IdentityReference, accessMask:int, isInherited:bool, inheritanceFlags:InheritanceFlags, propagationFlags:PropagationFlags, type:AccessControlType) -> AccessRule:
        """ AccessRuleFactory(self: PipeSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule """
        ...

    def AuditRuleFactory(self, identityReference:IdentityReference, accessMask:int, isInherited:bool, inheritanceFlags:InheritanceFlags, propagationFlags:PropagationFlags, flags:AuditFlags) -> AuditRule:
        """ AuditRuleFactory(self: PipeSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule """
        ...


class PipeStreamImpersonationWorker(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ PipeStreamImpersonationWorker(object: object, method: IntPtr) """
    def BeginInvoke(self, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: PipeStreamImpersonationWorker, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: PipeStreamImpersonationWorker, result: IAsyncResult) """
        ...

    def Invoke(self): # -> 
        """ Invoke(self: PipeStreamImpersonationWorker) """
        ...


class PipeTransmissionMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PipeTransmissionMode, values: Byte (0), Message (1) """
    Byte: PipeTransmissionMode = ...
    Message: PipeTransmissionMode = ...
    value__ = ...


