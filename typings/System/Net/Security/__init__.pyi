# encoding: utf-8
# module System.Net.Security calls itself Security
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Enum, IAsyncResult, Int64, 
    MulticastDelegate)

from System.IO import SeekOrigin, Stream

from System.Net import NetworkCredential, TransportContext

from System.Security.Authentication import (CipherAlgorithmType, 
    ExchangeAlgorithmType, HashAlgorithmType, SslProtocols)

from System.Security.Authentication.ExtendedProtection import (
    ExtendedProtectionPolicy)

from System.Security.Cryptography.X509Certificates import (X509Certificate, 
    X509CertificateCollection, X509Chain)

from System.Security.Principal import IIdentity, TokenImpersonationLevel

from System.Threading.Tasks import Task

"""The following names are not found in the module: field#
"""

# no functions
# classes

class AuthenticatedStream(Stream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def InnerStream(self):
        ...

    @property
    def IsAuthenticated(self) -> bool:
        """ Get: IsAuthenticated(self: AuthenticatedStream) -> bool """
        ...

    @property
    def IsEncrypted(self) -> bool:
        """ Get: IsEncrypted(self: AuthenticatedStream) -> bool """
        ...

    @property
    def IsMutuallyAuthenticated(self) -> bool:
        """ Get: IsMutuallyAuthenticated(self: AuthenticatedStream) -> bool """
        ...

    @property
    def IsServer(self) -> bool:
        """ Get: IsServer(self: AuthenticatedStream) -> bool """
        ...

    @property
    def IsSigned(self) -> bool:
        """ Get: IsSigned(self: AuthenticatedStream) -> bool """
        ...

    @property
    def LeaveInnerStreamOpen(self) -> bool:
        """ Get: LeaveInnerStreamOpen(self: AuthenticatedStream) -> bool """
        ...


    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, innerStream: Stream, leaveInnerStreamOpen: bool) """
        ...


class AuthenticationLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AuthenticationLevel, values: MutualAuthRequested (1), MutualAuthRequired (2), None (0) """
    MutualAuthRequested: AuthenticationLevel = ...
    MutualAuthRequired: AuthenticationLevel = ...
    value__ = ...


class EncryptionPolicy(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EncryptionPolicy, values: AllowNoEncryption (1), NoEncryption (2), RequireEncryption (0) """
    AllowNoEncryption: EncryptionPolicy = ...
    NoEncryption: EncryptionPolicy = ...
    RequireEncryption: EncryptionPolicy = ...
    value__ = ...


class LocalCertificateSelectionCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ LocalCertificateSelectionCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, targetHost:str, localCertificates:X509CertificateCollection, remoteCertificate:X509Certificate, acceptableIssuers:Array, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: LocalCertificateSelectionCallback, sender: object, targetHost: str, localCertificates: X509CertificateCollection, remoteCertificate: X509Certificate, acceptableIssuers: Array[str], callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> X509Certificate:
        """ EndInvoke(self: LocalCertificateSelectionCallback, result: IAsyncResult) -> X509Certificate """
        ...

    def Invoke(self, sender:object, targetHost:str, localCertificates:X509CertificateCollection, remoteCertificate:X509Certificate, acceptableIssuers:Array) -> X509Certificate:
        """ Invoke(self: LocalCertificateSelectionCallback, sender: object, targetHost: str, localCertificates: X509CertificateCollection, remoteCertificate: X509Certificate, acceptableIssuers: Array[str]) -> X509Certificate """
        ...


class NegotiateStream(AuthenticatedStream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    NegotiateStream(innerStream: Stream)
    NegotiateStream(innerStream: Stream, leaveInnerStreamOpen: bool)
    """
    @property
    def CanRead(self) -> bool:
        """ Get: CanRead(self: NegotiateStream) -> bool """
        ...

    @property
    def CanSeek(self) -> bool:
        """ Get: CanSeek(self: NegotiateStream) -> bool """
        ...

    @property
    def CanTimeout(self) -> bool:
        """ Get: CanTimeout(self: NegotiateStream) -> bool """
        ...

    @property
    def CanWrite(self) -> bool:
        """ Get: CanWrite(self: NegotiateStream) -> bool """
        ...

    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel:
        """ Get: ImpersonationLevel(self: NegotiateStream) -> TokenImpersonationLevel """
        ...

    @property
    def Length(self) -> Int64:
        """ Get: Length(self: NegotiateStream) -> Int64 """
        ...

    @property
    def Position(self) -> Int64:
        """
        Get: Position(self: NegotiateStream) -> Int64
        Set: Position(self: NegotiateStream) = value
        """
        ...

    @property
    def ReadTimeout(self) -> int:
        """
        Get: ReadTimeout(self: NegotiateStream) -> int
        Set: ReadTimeout(self: NegotiateStream) = value
        """
        ...

    @property
    def RemoteIdentity(self) -> IIdentity:
        """ Get: RemoteIdentity(self: NegotiateStream) -> IIdentity """
        ...

    @property
    def WriteTimeout(self) -> int:
        """
        Get: WriteTimeout(self: NegotiateStream) -> int
        Set: WriteTimeout(self: NegotiateStream) = value
        """
        ...


    def AuthenticateAsClient(self, credential:NetworkCredential = ..., *__args:str): # -> 
        """ AuthenticateAsClient(self: NegotiateStream)AuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, targetName: str)AuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, binding: ChannelBinding, targetName: str)AuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel)AuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, binding: ChannelBinding, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel) """
        ...

    def AuthenticateAsClientAsync(self, credential:NetworkCredential = ..., *__args:str) -> Task:
        """
        AuthenticateAsClientAsync(self: NegotiateStream) -> Task
        AuthenticateAsClientAsync(self: NegotiateStream, credential: NetworkCredential, targetName: str) -> Task
        AuthenticateAsClientAsync(self: NegotiateStream, credential: NetworkCredential, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel) -> Task
        AuthenticateAsClientAsync(self: NegotiateStream, credential: NetworkCredential, binding: ChannelBinding, targetName: str) -> Task
        AuthenticateAsClientAsync(self: NegotiateStream, credential: NetworkCredential, binding: ChannelBinding, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel) -> Task
        """
        ...

    def AuthenticateAsServer(self, *__args:ExtendedProtectionPolicy): # -> 
        """ AuthenticateAsServer(self: NegotiateStream)AuthenticateAsServer(self: NegotiateStream, policy: ExtendedProtectionPolicy)AuthenticateAsServer(self: NegotiateStream, credential: NetworkCredential, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel)AuthenticateAsServer(self: NegotiateStream, credential: NetworkCredential, policy: ExtendedProtectionPolicy, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel) """
        ...

    def AuthenticateAsServerAsync(self, *__args:ExtendedProtectionPolicy) -> Task:
        """
        AuthenticateAsServerAsync(self: NegotiateStream) -> Task
        AuthenticateAsServerAsync(self: NegotiateStream, policy: ExtendedProtectionPolicy) -> Task
        AuthenticateAsServerAsync(self: NegotiateStream, credential: NetworkCredential, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel) -> Task
        AuthenticateAsServerAsync(self: NegotiateStream, credential: NetworkCredential, policy: ExtendedProtectionPolicy, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel) -> Task
        """
        ...

    def BeginAuthenticateAsClient(self, *__args) -> IAsyncResult:
        """
        BeginAuthenticateAsClient(self: NegotiateStream, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginAuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, targetName: str, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginAuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, binding: ChannelBinding, targetName: str, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginAuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginAuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, binding: ChannelBinding, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        """
        ...

    def BeginAuthenticateAsServer(self, *__args) -> IAsyncResult:
        """
        BeginAuthenticateAsServer(self: NegotiateStream, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginAuthenticateAsServer(self: NegotiateStream, policy: ExtendedProtectionPolicy, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginAuthenticateAsServer(self: NegotiateStream, credential: NetworkCredential, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginAuthenticateAsServer(self: NegotiateStream, credential: NetworkCredential, policy: ExtendedProtectionPolicy, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        """
        ...

    def BeginRead(self, buffer:Array, offset:int, count:int, asyncCallback:AsyncCallback, asyncState:object) -> IAsyncResult:
        """ BeginRead(self: NegotiateStream, buffer: Array[Byte], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult """
        ...

    def BeginWrite(self, buffer:Array, offset:int, count:int, asyncCallback:AsyncCallback, asyncState:object) -> IAsyncResult:
        """ BeginWrite(self: NegotiateStream, buffer: Array[Byte], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult """
        ...

    def EndAuthenticateAsClient(self, asyncResult:IAsyncResult): # -> 
        """ EndAuthenticateAsClient(self: NegotiateStream, asyncResult: IAsyncResult) """
        ...

    def EndAuthenticateAsServer(self, asyncResult:IAsyncResult): # -> 
        """ EndAuthenticateAsServer(self: NegotiateStream, asyncResult: IAsyncResult) """
        ...

    def EndRead(self, asyncResult:IAsyncResult) -> int:
        """ EndRead(self: NegotiateStream, asyncResult: IAsyncResult) -> int """
        ...

    def EndWrite(self, asyncResult:IAsyncResult): # -> 
        """ EndWrite(self: NegotiateStream, asyncResult: IAsyncResult) """
        ...

    def Flush(self): # -> 
        """ Flush(self: NegotiateStream) """
        ...

    def Read(self, buffer:Array, offset:int, count:int) -> int:
        """ Read(self: NegotiateStream, buffer: Array[Byte], offset: int, count: int) -> int """
        ...

    def Seek(self, offset:Int64, origin:SeekOrigin) -> Int64:
        """ Seek(self: NegotiateStream, offset: Int64, origin: SeekOrigin) -> Int64 """
        ...

    def SetLength(self, value:Int64): # -> 
        """ SetLength(self: NegotiateStream, value: Int64) """
        ...

    def Write(self, buffer:Array, offset:int, count:int): # -> 
        """ Write(self: NegotiateStream, buffer: Array[Byte], offset: int, count: int) """
        ...


class ProtectionLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProtectionLevel, values: EncryptAndSign (2), None (0), Sign (1) """
    EncryptAndSign: ProtectionLevel = ...
    Sign: ProtectionLevel = ...
    value__ = ...


class RemoteCertificateValidationCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ RemoteCertificateValidationCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, certificate:X509Certificate, chain:X509Chain, sslPolicyErrors:SslPolicyErrors, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: RemoteCertificateValidationCallback, sender: object, certificate: X509Certificate, chain: X509Chain, sslPolicyErrors: SslPolicyErrors, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> bool:
        """ EndInvoke(self: RemoteCertificateValidationCallback, result: IAsyncResult) -> bool """
        ...

    def Invoke(self, sender:object, certificate:X509Certificate, chain:X509Chain, sslPolicyErrors:SslPolicyErrors) -> bool:
        """ Invoke(self: RemoteCertificateValidationCallback, sender: object, certificate: X509Certificate, chain: X509Chain, sslPolicyErrors: SslPolicyErrors) -> bool """
        ...


class SslPolicyErrors(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SslPolicyErrors, values: None (0), RemoteCertificateChainErrors (4), RemoteCertificateNameMismatch (2), RemoteCertificateNotAvailable (1) """
    RemoteCertificateChainErrors: SslPolicyErrors = ...
    RemoteCertificateNameMismatch: SslPolicyErrors = ...
    RemoteCertificateNotAvailable: SslPolicyErrors = ...
    value__ = ...


class SslStream(AuthenticatedStream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    SslStream(innerStream: Stream)
    SslStream(innerStream: Stream, leaveInnerStreamOpen: bool)
    SslStream(innerStream: Stream, leaveInnerStreamOpen: bool, userCertificateValidationCallback: RemoteCertificateValidationCallback)
    SslStream(innerStream: Stream, leaveInnerStreamOpen: bool, userCertificateValidationCallback: RemoteCertificateValidationCallback, userCertificateSelectionCallback: LocalCertificateSelectionCallback)
    SslStream(innerStream: Stream, leaveInnerStreamOpen: bool, userCertificateValidationCallback: RemoteCertificateValidationCallback, userCertificateSelectionCallback: LocalCertificateSelectionCallback, encryptionPolicy: EncryptionPolicy)
    """
    @property
    def CanRead(self) -> bool:
        """ Get: CanRead(self: SslStream) -> bool """
        ...

    @property
    def CanSeek(self) -> bool:
        """ Get: CanSeek(self: SslStream) -> bool """
        ...

    @property
    def CanTimeout(self) -> bool:
        """ Get: CanTimeout(self: SslStream) -> bool """
        ...

    @property
    def CanWrite(self) -> bool:
        """ Get: CanWrite(self: SslStream) -> bool """
        ...

    @property
    def CheckCertRevocationStatus(self) -> bool:
        """ Get: CheckCertRevocationStatus(self: SslStream) -> bool """
        ...

    @property
    def CipherAlgorithm(self) -> CipherAlgorithmType:
        """ Get: CipherAlgorithm(self: SslStream) -> CipherAlgorithmType """
        ...

    @property
    def CipherStrength(self) -> int:
        """ Get: CipherStrength(self: SslStream) -> int """
        ...

    @property
    def HashAlgorithm(self) -> HashAlgorithmType:
        """ Get: HashAlgorithm(self: SslStream) -> HashAlgorithmType """
        ...

    @property
    def HashStrength(self) -> int:
        """ Get: HashStrength(self: SslStream) -> int """
        ...

    @property
    def KeyExchangeAlgorithm(self) -> ExchangeAlgorithmType:
        """ Get: KeyExchangeAlgorithm(self: SslStream) -> ExchangeAlgorithmType """
        ...

    @property
    def KeyExchangeStrength(self) -> int:
        """ Get: KeyExchangeStrength(self: SslStream) -> int """
        ...

    @property
    def Length(self) -> Int64:
        """ Get: Length(self: SslStream) -> Int64 """
        ...

    @property
    def LocalCertificate(self) -> X509Certificate:
        """ Get: LocalCertificate(self: SslStream) -> X509Certificate """
        ...

    @property
    def Position(self) -> Int64:
        """
        Get: Position(self: SslStream) -> Int64
        Set: Position(self: SslStream) = value
        """
        ...

    @property
    def ReadTimeout(self) -> int:
        """
        Get: ReadTimeout(self: SslStream) -> int
        Set: ReadTimeout(self: SslStream) = value
        """
        ...

    @property
    def RemoteCertificate(self) -> X509Certificate:
        """ Get: RemoteCertificate(self: SslStream) -> X509Certificate """
        ...

    @property
    def SslProtocol(self) -> SslProtocols:
        """ Get: SslProtocol(self: SslStream) -> SslProtocols """
        ...

    @property
    def TransportContext(self) -> TransportContext:
        """ Get: TransportContext(self: SslStream) -> TransportContext """
        ...

    @property
    def WriteTimeout(self) -> int:
        """
        Get: WriteTimeout(self: SslStream) -> int
        Set: WriteTimeout(self: SslStream) = value
        """
        ...


    def AuthenticateAsClient(self, targetHost:str, clientCertificates:X509CertificateCollection = ..., *__args:bool): # -> 
        """ AuthenticateAsClient(self: SslStream, targetHost: str, clientCertificates: X509CertificateCollection, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool)AuthenticateAsClient(self: SslStream, targetHost: str)AuthenticateAsClient(self: SslStream, targetHost: str, clientCertificates: X509CertificateCollection, checkCertificateRevocation: bool) """
        ...

    def AuthenticateAsClientAsync(self, targetHost:str, clientCertificates:X509CertificateCollection = ..., *__args:bool) -> Task:
        """
        AuthenticateAsClientAsync(self: SslStream, targetHost: str, clientCertificates: X509CertificateCollection, checkCertificateRevocation: bool) -> Task
        AuthenticateAsClientAsync(self: SslStream, targetHost: str) -> Task
        AuthenticateAsClientAsync(self: SslStream, targetHost: str, clientCertificates: X509CertificateCollection, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool) -> Task
        """
        ...

    def AuthenticateAsServer(self, serverCertificate:X509Certificate, clientCertificateRequired:bool = ..., *__args:bool): # -> 
        """ AuthenticateAsServer(self: SslStream, serverCertificate: X509Certificate)AuthenticateAsServer(self: SslStream, serverCertificate: X509Certificate, clientCertificateRequired: bool, checkCertificateRevocation: bool)AuthenticateAsServer(self: SslStream, serverCertificate: X509Certificate, clientCertificateRequired: bool, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool) """
        ...

    def AuthenticateAsServerAsync(self, serverCertificate:X509Certificate, clientCertificateRequired:bool = ..., *__args:bool) -> Task:
        """
        AuthenticateAsServerAsync(self: SslStream, serverCertificate: X509Certificate, clientCertificateRequired: bool, checkCertificateRevocation: bool) -> Task
        AuthenticateAsServerAsync(self: SslStream, serverCertificate: X509Certificate) -> Task
        AuthenticateAsServerAsync(self: SslStream, serverCertificate: X509Certificate, clientCertificateRequired: bool, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool) -> Task
        """
        ...

    def BeginAuthenticateAsClient(self, targetHost, *__args) -> IAsyncResult:
        """
        BeginAuthenticateAsClient(self: SslStream, targetHost: str, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginAuthenticateAsClient(self: SslStream, targetHost: str, clientCertificates: X509CertificateCollection, checkCertificateRevocation: bool, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginAuthenticateAsClient(self: SslStream, targetHost: str, clientCertificates: X509CertificateCollection, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        """
        ...

    def BeginAuthenticateAsServer(self, serverCertificate, *__args) -> IAsyncResult:
        """
        BeginAuthenticateAsServer(self: SslStream, serverCertificate: X509Certificate, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginAuthenticateAsServer(self: SslStream, serverCertificate: X509Certificate, clientCertificateRequired: bool, checkCertificateRevocation: bool, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginAuthenticateAsServer(self: SslStream, serverCertificate: X509Certificate, clientCertificateRequired: bool, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult
        """
        ...

    def BeginRead(self, buffer:Array, offset:int, count:int, asyncCallback:AsyncCallback, asyncState:object) -> IAsyncResult:
        """ BeginRead(self: SslStream, buffer: Array[Byte], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult """
        ...

    def BeginWrite(self, buffer:Array, offset:int, count:int, asyncCallback:AsyncCallback, asyncState:object) -> IAsyncResult:
        """ BeginWrite(self: SslStream, buffer: Array[Byte], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult """
        ...

    def EndAuthenticateAsClient(self, asyncResult:IAsyncResult): # -> 
        """ EndAuthenticateAsClient(self: SslStream, asyncResult: IAsyncResult) """
        ...

    def EndAuthenticateAsServer(self, asyncResult:IAsyncResult): # -> 
        """ EndAuthenticateAsServer(self: SslStream, asyncResult: IAsyncResult) """
        ...

    def EndRead(self, asyncResult:IAsyncResult) -> int:
        """ EndRead(self: SslStream, asyncResult: IAsyncResult) -> int """
        ...

    def EndWrite(self, asyncResult:IAsyncResult): # -> 
        """ EndWrite(self: SslStream, asyncResult: IAsyncResult) """
        ...

    def Flush(self): # -> 
        """ Flush(self: SslStream) """
        ...

    def Read(self, buffer:Array, offset:int, count:int) -> int:
        """ Read(self: SslStream, buffer: Array[Byte], offset: int, count: int) -> int """
        ...

    def Seek(self, offset:Int64, origin:SeekOrigin) -> Int64:
        """ Seek(self: SslStream, offset: Int64, origin: SeekOrigin) -> Int64 """
        ...

    def SetLength(self, value:Int64): # -> 
        """ SetLength(self: SslStream, value: Int64) """
        ...

    def ShutdownAsync(self) -> Task:
        """ ShutdownAsync(self: SslStream) -> Task """
        ...

    def Write(self, buffer:Array, offset:int = ..., count:int = ...): # -> 
        """ Write(self: SslStream, buffer: Array[Byte], offset: int, count: int)Write(self: SslStream, buffer: Array[Byte]) """
        ...


