# encoding: utf-8
# module System.IdentityModel calls itself IdentityModel
# from System.IdentityModel.Selectors, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.IdentityModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Char, IAsyncResult, IDisposable, 
    SystemException, Type)

from System.Collections.Generic import Dictionary

from System.IdentityModel.Configuration import (
    SecurityTokenServiceConfiguration)

from System.IdentityModel.Protocols.WSTrust import (RequestSecurityToken, 
    RequestSecurityTokenResponse)

from System.IdentityModel.Selectors import (SecurityTokenResolver, 
    SecurityTokenSerializer)

from System.IdentityModel.Tokens import (EncryptingCredentials, 
    SecurityTokenException, SigningCredentials)

from System.Runtime.Remoting.Messaging import AsyncResult

from System.Runtime.Serialization import SerializationInfo, StreamingContext

from System.Security.Claims import ClaimsPrincipal

from System.Security.Cryptography import RSA

from System.Xml import (ReadState, WriteState, XmlDictionaryReader, 
    XmlDictionaryWriter, XmlNameTable, XmlNodeType, XmlReader, XmlSpace, 
    XmlWriter)

from typing import Self

"""The following names are not found in the module: BoundEvent, T
"""

# no functions
# classes

class AsynchronousOperationException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    AsynchronousOperationException()
    AsynchronousOperationException(message: str)
    AsynchronousOperationException(message: str, innerException: Exception)
    AsynchronousOperationException(innerException: Exception)
    """
    SerializeObjectState = ...


class AsyncResult(IDisposable, IAsyncResult): # skipped bases: <type 'object'>
    """ no doc """
    def Complete(self, *args): #cannot find CLR method
        """ Complete(self: AsyncResult, completedSynchronously: bool)Complete(self: AsyncResult, completedSynchronously: bool, exception: Exception) """
        ...

    @staticmethod
    def End(result:IAsyncResult): # -> 
        """ End(result: IAsyncResult) """
        ...


class RequestException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    SerializeObjectState = ...


class BadRequestException(RequestException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    BadRequestException()
    BadRequestException(message: str)
    BadRequestException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class CookieTransform: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Decode(self, encoded:Array) -> Array:
        """ Decode(self: CookieTransform, encoded: Array[Byte]) -> Array[Byte] """
        ...

    def Encode(self, value:Array) -> Array:
        """ Encode(self: CookieTransform, value: Array[Byte]) -> Array[Byte] """
        ...


class DeflateCookieTransform(CookieTransform): # skipped bases: <type 'object'>
    """ DeflateCookieTransform() """
    @property
    def MaxDecompressedSize(self) -> int:
        """
        Get: MaxDecompressedSize(self: DeflateCookieTransform) -> int
        Set: MaxDecompressedSize(self: DeflateCookieTransform) = value
        """
        ...



class DelegatingXmlDictionaryReader(XmlDictionaryReader): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def AttributeCount(self) -> int:
        """ Get: AttributeCount(self: DelegatingXmlDictionaryReader) -> int """
        ...

    @property
    def BaseURI(self) -> str:
        """ Get: BaseURI(self: DelegatingXmlDictionaryReader) -> str """
        ...

    @property
    def Depth(self) -> int:
        """ Get: Depth(self: DelegatingXmlDictionaryReader) -> int """
        ...

    @property
    def EOF(self) -> bool:
        """ Get: EOF(self: DelegatingXmlDictionaryReader) -> bool """
        ...

    @property
    def HasValue(self) -> bool:
        """ Get: HasValue(self: DelegatingXmlDictionaryReader) -> bool """
        ...

    @property
    def InnerReader(self):
        ...

    @property
    def IsDefault(self) -> bool:
        """ Get: IsDefault(self: DelegatingXmlDictionaryReader) -> bool """
        ...

    @property
    def IsEmptyElement(self) -> bool:
        """ Get: IsEmptyElement(self: DelegatingXmlDictionaryReader) -> bool """
        ...

    @property
    def LocalName(self) -> str:
        """ Get: LocalName(self: DelegatingXmlDictionaryReader) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DelegatingXmlDictionaryReader) -> str """
        ...

    @property
    def NamespaceURI(self) -> str:
        """ Get: NamespaceURI(self: DelegatingXmlDictionaryReader) -> str """
        ...

    @property
    def NameTable(self) -> XmlNameTable:
        """ Get: NameTable(self: DelegatingXmlDictionaryReader) -> XmlNameTable """
        ...

    @property
    def NodeType(self) -> XmlNodeType:
        """ Get: NodeType(self: DelegatingXmlDictionaryReader) -> XmlNodeType """
        ...

    @property
    def Prefix(self) -> str:
        """ Get: Prefix(self: DelegatingXmlDictionaryReader) -> str """
        ...

    @property
    def QuoteChar(self) -> Char:
        """ Get: QuoteChar(self: DelegatingXmlDictionaryReader) -> Char """
        ...

    @property
    def ReadState(self) -> ReadState:
        """ Get: ReadState(self: DelegatingXmlDictionaryReader) -> ReadState """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: DelegatingXmlDictionaryReader) -> str """
        ...

    @property
    def ValueType(self) -> Type:
        """ Get: ValueType(self: DelegatingXmlDictionaryReader) -> Type """
        ...

    @property
    def XmlLang(self) -> str:
        """ Get: XmlLang(self: DelegatingXmlDictionaryReader) -> str """
        ...

    @property
    def XmlSpace(self) -> XmlSpace:
        """ Get: XmlSpace(self: DelegatingXmlDictionaryReader) -> XmlSpace """
        ...


    def Close(self): # -> 
        """ Close(self: DelegatingXmlDictionaryReader) """
        ...

    def InitializeInnerReader(self, *args): #cannot find CLR method
        """ InitializeInnerReader(self: DelegatingXmlDictionaryReader, innerReader: XmlDictionaryReader) """
        ...

    def LookupNamespace(self, prefix:str) -> str:
        """ LookupNamespace(self: DelegatingXmlDictionaryReader, prefix: str) -> str """
        ...

    def MoveToAttribute(self, *__args:int): # -> 
        """
        MoveToAttribute(self: DelegatingXmlDictionaryReader, i: int)MoveToAttribute(self: DelegatingXmlDictionaryReader, name: str) -> bool
        MoveToAttribute(self: DelegatingXmlDictionaryReader, name: str, ns: str) -> bool
        """
        ...

    def MoveToElement(self) -> bool:
        """ MoveToElement(self: DelegatingXmlDictionaryReader) -> bool """
        ...

    def MoveToFirstAttribute(self) -> bool:
        """ MoveToFirstAttribute(self: DelegatingXmlDictionaryReader) -> bool """
        ...

    def MoveToNextAttribute(self) -> bool:
        """ MoveToNextAttribute(self: DelegatingXmlDictionaryReader) -> bool """
        ...

    def Read(self) -> bool:
        """ Read(self: DelegatingXmlDictionaryReader) -> bool """
        ...

    def ReadAttributeValue(self) -> bool:
        """ ReadAttributeValue(self: DelegatingXmlDictionaryReader) -> bool """
        ...

    def ReadValueChunk(self, buffer:Array, index:int, count:int) -> int:
        """ ReadValueChunk(self: DelegatingXmlDictionaryReader, buffer: Array[Char], index: int, count: int) -> int """
        ...

    def ResolveEntity(self): # -> 
        """ ResolveEntity(self: DelegatingXmlDictionaryReader) """
        ...


class DelegatingXmlDictionaryWriter(XmlDictionaryWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def InnerWriter(self):
        ...

    @property
    def WriteState(self) -> WriteState:
        """ Get: WriteState(self: DelegatingXmlDictionaryWriter) -> WriteState """
        ...


    def Close(self): # -> 
        """ Close(self: DelegatingXmlDictionaryWriter) """
        ...

    def Flush(self): # -> 
        """ Flush(self: DelegatingXmlDictionaryWriter) """
        ...

    def InitializeInnerWriter(self, *args): #cannot find CLR method
        """ InitializeInnerWriter(self: DelegatingXmlDictionaryWriter, innerWriter: XmlDictionaryWriter) """
        ...

    def InitializeTracingWriter(self, *args): #cannot find CLR method
        """ InitializeTracingWriter(self: DelegatingXmlDictionaryWriter, tracingWriter: XmlWriter) """
        ...

    def LookupPrefix(self, ns:str) -> str:
        """ LookupPrefix(self: DelegatingXmlDictionaryWriter, ns: str) -> str """
        ...

    def WriteBase64(self, buffer:Array, index:int, count:int): # -> 
        """ WriteBase64(self: DelegatingXmlDictionaryWriter, buffer: Array[Byte], index: int, count: int) """
        ...

    def WriteCData(self, text:str): # -> 
        """ WriteCData(self: DelegatingXmlDictionaryWriter, text: str) """
        ...

    def WriteCharEntity(self, ch:Char): # -> 
        """ WriteCharEntity(self: DelegatingXmlDictionaryWriter, ch: Char) """
        ...

    def WriteChars(self, buffer:Array, index:int, count:int): # -> 
        """ WriteChars(self: DelegatingXmlDictionaryWriter, buffer: Array[Char], index: int, count: int) """
        ...

    def WriteComment(self, text:str): # -> 
        """ WriteComment(self: DelegatingXmlDictionaryWriter, text: str) """
        ...

    def WriteDocType(self, name:str, pubid:str, sysid:str, subset:str): # -> 
        """ WriteDocType(self: DelegatingXmlDictionaryWriter, name: str, pubid: str, sysid: str, subset: str) """
        ...

    def WriteEndAttribute(self): # -> 
        """ WriteEndAttribute(self: DelegatingXmlDictionaryWriter) """
        ...

    def WriteEndDocument(self): # -> 
        """ WriteEndDocument(self: DelegatingXmlDictionaryWriter) """
        ...

    def WriteEndElement(self): # -> 
        """ WriteEndElement(self: DelegatingXmlDictionaryWriter) """
        ...

    def WriteEntityRef(self, name:str): # -> 
        """ WriteEntityRef(self: DelegatingXmlDictionaryWriter, name: str) """
        ...

    def WriteFullEndElement(self): # -> 
        """ WriteFullEndElement(self: DelegatingXmlDictionaryWriter) """
        ...

    def WriteProcessingInstruction(self, name:str, text:str): # -> 
        """ WriteProcessingInstruction(self: DelegatingXmlDictionaryWriter, name: str, text: str) """
        ...

    def WriteRaw(self, *__args:str): # -> 
        """ WriteRaw(self: DelegatingXmlDictionaryWriter, buffer: Array[Char], index: int, count: int)WriteRaw(self: DelegatingXmlDictionaryWriter, data: str) """
        ...

    def WriteStartDocument(self, standalone:bool = ...): # -> 
        """ WriteStartDocument(self: DelegatingXmlDictionaryWriter)WriteStartDocument(self: DelegatingXmlDictionaryWriter, standalone: bool) """
        ...

    def WriteSurrogateCharEntity(self, lowChar:Char, highChar:Char): # -> 
        """ WriteSurrogateCharEntity(self: DelegatingXmlDictionaryWriter, lowChar: Char, highChar: Char) """
        ...

    def WriteWhitespace(self, ws:str): # -> 
        """ WriteWhitespace(self: DelegatingXmlDictionaryWriter, ws: str) """
        ...


class EnvelopedSignatureReader(DelegatingXmlDictionaryReader): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    EnvelopedSignatureReader(reader: XmlReader, securityTokenSerializer: SecurityTokenSerializer)
    EnvelopedSignatureReader(reader: XmlReader, securityTokenSerializer: SecurityTokenSerializer, signingTokenResolver: SecurityTokenResolver)
    EnvelopedSignatureReader(reader: XmlReader, securityTokenSerializer: SecurityTokenSerializer, signingTokenResolver: SecurityTokenResolver, requireSignature: bool, automaticallyReadSignature: bool, resolveIntrinsicSigningKeys: bool)
    """
    @property
    def SigningCredentials(self) -> SigningCredentials:
        """ Get: SigningCredentials(self: EnvelopedSignatureReader) -> SigningCredentials """
        ...


    def TryReadSignature(self) -> bool:
        """ TryReadSignature(self: EnvelopedSignatureReader) -> bool """
        ...

    def __new__(cls, reader:XmlReader, securityTokenSerializer:SecurityTokenSerializer, signingTokenResolver:SecurityTokenResolver = ..., requireSignature:bool = ..., automaticallyReadSignature:bool = ..., resolveIntrinsicSigningKeys:bool = ...) -> Self:
        """
        __new__(cls: type, reader: XmlReader, securityTokenSerializer: SecurityTokenSerializer)
        __new__(cls: type, reader: XmlReader, securityTokenSerializer: SecurityTokenSerializer, signingTokenResolver: SecurityTokenResolver)
        __new__(cls: type, reader: XmlReader, securityTokenSerializer: SecurityTokenSerializer, signingTokenResolver: SecurityTokenResolver, requireSignature: bool, automaticallyReadSignature: bool, resolveIntrinsicSigningKeys: bool)
        """
        ...


class EnvelopedSignatureWriter(DelegatingXmlDictionaryWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ EnvelopedSignatureWriter(innerWriter: XmlWriter, signingCredentials: SigningCredentials, referenceId: str, securityTokenSerializer: SecurityTokenSerializer) """
    def WriteSignature(self): # -> 
        """ WriteSignature(self: EnvelopedSignatureWriter) """
        ...

    def __new__(cls, innerWriter:XmlWriter, signingCredentials:SigningCredentials, referenceId:str, securityTokenSerializer:SecurityTokenSerializer) -> Self:
        """ __new__(cls: type, innerWriter: XmlWriter, signingCredentials: SigningCredentials, referenceId: str, securityTokenSerializer: SecurityTokenSerializer) """
        ...


class LimitExceededException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    LimitExceededException()
    LimitExceededException(message: str)
    LimitExceededException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class OpenObject: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Properties(self) -> Dictionary:
        """ Get: Properties(self: OpenObject) -> Dictionary[str, object] """
        ...



class ProtectedDataCookieTransform(CookieTransform): # skipped bases: <type 'object'>
    """ ProtectedDataCookieTransform() """
    pass

class RequestFailedException(RequestException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RequestFailedException()
    RequestFailedException(message: str)
    RequestFailedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class RsaEncryptionCookieTransform(CookieTransform): # skipped bases: <type 'object'>
    """
    RsaEncryptionCookieTransform(key: RSA)
    RsaEncryptionCookieTransform(certificate: X509Certificate2)
    """
    @property
    def DecryptionKeys(self):
        ...

    @property
    def EncryptionKey(self) -> RSA:
        """
        Get: EncryptionKey(self: RsaEncryptionCookieTransform) -> RSA
        Set: EncryptionKey(self: RsaEncryptionCookieTransform) = value
        """
        ...

    @property
    def HashName(self) -> str:
        """
        Get: HashName(self: RsaEncryptionCookieTransform) -> str
        Set: HashName(self: RsaEncryptionCookieTransform) = value
        """
        ...


    def __new__(cls, *__args:RSA) -> Self:
        """
        __new__(cls: type, key: RSA)
        __new__(cls: type, certificate: X509Certificate2)
        """
        ...


class RsaSignatureCookieTransform(CookieTransform): # skipped bases: <type 'object'>
    """
    RsaSignatureCookieTransform(key: RSA)
    RsaSignatureCookieTransform(certificate: X509Certificate2)
    """
    @property
    def HashName(self) -> str:
        """
        Get: HashName(self: RsaSignatureCookieTransform) -> str
        Set: HashName(self: RsaSignatureCookieTransform) = value
        """
        ...

    @property
    def SigningKey(self) -> RSA:
        """
        Get: SigningKey(self: RsaSignatureCookieTransform) -> RSA
        Set: SigningKey(self: RsaSignatureCookieTransform) = value
        """
        ...

    @property
    def VerificationKeys(self):
        ...


    def __new__(cls, *__args:RSA) -> Self:
        """
        __new__(cls: type, key: RSA)
        __new__(cls: type, certificate: X509Certificate2)
        """
        ...


class Scope: # skipped bases: <type 'object'>, <type 'object'>
    """
    Scope()
    Scope(appliesToAddress: str)
    Scope(appliesToAddress: str, signingCredentials: SigningCredentials)
    Scope(appliesToAddress: str, encryptingCredentials: EncryptingCredentials)
    Scope(appliesToAddress: str, signingCredentials: SigningCredentials, encryptingCredentials: EncryptingCredentials)
    """
    @property
    def AppliesToAddress(self) -> str:
        """
        Get: AppliesToAddress(self: Scope) -> str
        Set: AppliesToAddress(self: Scope) = value
        """
        ...

    @property
    def EncryptingCredentials(self) -> EncryptingCredentials:
        """
        Get: EncryptingCredentials(self: Scope) -> EncryptingCredentials
        Set: EncryptingCredentials(self: Scope) = value
        """
        ...

    @property
    def Properties(self) -> Dictionary:
        """ Get: Properties(self: Scope) -> Dictionary[str, object] """
        ...

    @property
    def ReplyToAddress(self) -> str:
        """
        Get: ReplyToAddress(self: Scope) -> str
        Set: ReplyToAddress(self: Scope) = value
        """
        ...

    @property
    def SigningCredentials(self) -> SigningCredentials:
        """
        Get: SigningCredentials(self: Scope) -> SigningCredentials
        Set: SigningCredentials(self: Scope) = value
        """
        ...

    @property
    def SymmetricKeyEncryptionRequired(self) -> bool:
        """
        Get: SymmetricKeyEncryptionRequired(self: Scope) -> bool
        Set: SymmetricKeyEncryptionRequired(self: Scope) = value
        """
        ...

    @property
    def TokenEncryptionRequired(self) -> bool:
        """
        Get: TokenEncryptionRequired(self: Scope) -> bool
        Set: TokenEncryptionRequired(self: Scope) = value
        """
        ...



class SecurityMessageSerializationException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SecurityMessageSerializationException()
    SecurityMessageSerializationException(message: str)
    SecurityMessageSerializationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SecurityTokenService: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Principal(self) -> ClaimsPrincipal:
        """
        Get: Principal(self: SecurityTokenService) -> ClaimsPrincipal
        Set: Principal(self: SecurityTokenService) = value
        """
        ...

    @property
    def Request(self) -> RequestSecurityToken:
        """
        Get: Request(self: SecurityTokenService) -> RequestSecurityToken
        Set: Request(self: SecurityTokenService) = value
        """
        ...

    @property
    def Scope(self) -> Scope:
        """
        Get: Scope(self: SecurityTokenService) -> Scope
        Set: Scope(self: SecurityTokenService) = value
        """
        ...

    @property
    def SecurityTokenDescriptor(self):
        ...

    @property
    def SecurityTokenServiceConfiguration(self) -> SecurityTokenServiceConfiguration:
        """ Get: SecurityTokenServiceConfiguration(self: SecurityTokenService) -> SecurityTokenServiceConfiguration """
        ...


    def BeginCancel(self, principal:ClaimsPrincipal, request:RequestSecurityToken, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginCancel(self: SecurityTokenService, principal: ClaimsPrincipal, request: RequestSecurityToken, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginGetOutputClaimsIdentity(self, *args): #cannot find CLR method
        """ BeginGetOutputClaimsIdentity(self: SecurityTokenService, principal: ClaimsPrincipal, request: RequestSecurityToken, scope: Scope, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginGetScope(self, *args): #cannot find CLR method
        """ BeginGetScope(self: SecurityTokenService, principal: ClaimsPrincipal, request: RequestSecurityToken, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginIssue(self, principal:ClaimsPrincipal, request:RequestSecurityToken, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginIssue(self: SecurityTokenService, principal: ClaimsPrincipal, request: RequestSecurityToken, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginRenew(self, principal:ClaimsPrincipal, request:RequestSecurityToken, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginRenew(self: SecurityTokenService, principal: ClaimsPrincipal, request: RequestSecurityToken, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginValidate(self, principal:ClaimsPrincipal, request:RequestSecurityToken, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginValidate(self: SecurityTokenService, principal: ClaimsPrincipal, request: RequestSecurityToken, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def Cancel(self, principal:ClaimsPrincipal, request:RequestSecurityToken) -> RequestSecurityTokenResponse:
        """ Cancel(self: SecurityTokenService, principal: ClaimsPrincipal, request: RequestSecurityToken) -> RequestSecurityTokenResponse """
        ...

    def CreateSecurityTokenDescriptor(self, *args): #cannot find CLR method
        """ CreateSecurityTokenDescriptor(self: SecurityTokenService, request: RequestSecurityToken, scope: Scope) -> SecurityTokenDescriptor """
        ...

    def EndCancel(self, result:IAsyncResult) -> RequestSecurityTokenResponse:
        """ EndCancel(self: SecurityTokenService, result: IAsyncResult) -> RequestSecurityTokenResponse """
        ...

    def EndGetOutputClaimsIdentity(self, *args): #cannot find CLR method
        """ EndGetOutputClaimsIdentity(self: SecurityTokenService, result: IAsyncResult) -> ClaimsIdentity """
        ...

    def EndGetScope(self, *args): #cannot find CLR method
        """ EndGetScope(self: SecurityTokenService, result: IAsyncResult) -> Scope """
        ...

    def EndIssue(self, result:IAsyncResult) -> RequestSecurityTokenResponse:
        """ EndIssue(self: SecurityTokenService, result: IAsyncResult) -> RequestSecurityTokenResponse """
        ...

    def EndRenew(self, result:IAsyncResult) -> RequestSecurityTokenResponse:
        """ EndRenew(self: SecurityTokenService, result: IAsyncResult) -> RequestSecurityTokenResponse """
        ...

    def EndValidate(self, result:IAsyncResult) -> RequestSecurityTokenResponse:
        """ EndValidate(self: SecurityTokenService, result: IAsyncResult) -> RequestSecurityTokenResponse """
        ...

    def FederatedAsyncState(self, *args): #cannot find CLR method
        """
        FederatedAsyncState(federatedAsyncState: FederatedAsyncState)
        FederatedAsyncState(request: RequestSecurityToken, principal: ClaimsPrincipal, result: IAsyncResult)
        """
        ...

    def GetIssuerName(self, *args): #cannot find CLR method
        """ GetIssuerName(self: SecurityTokenService) -> str """
        ...

    def GetOutputClaimsIdentity(self, *args): #cannot find CLR method
        """ GetOutputClaimsIdentity(self: SecurityTokenService, principal: ClaimsPrincipal, request: RequestSecurityToken, scope: Scope) -> ClaimsIdentity """
        ...

    def GetProofToken(self, *args): #cannot find CLR method
        """ GetProofToken(self: SecurityTokenService, request: RequestSecurityToken, scope: Scope) -> ProofDescriptor """
        ...

    def GetRequestorProofEncryptingCredentials(self, *args): #cannot find CLR method
        """ GetRequestorProofEncryptingCredentials(self: SecurityTokenService, request: RequestSecurityToken) -> EncryptingCredentials """
        ...

    def GetResponse(self, *args): #cannot find CLR method
        """ GetResponse(self: SecurityTokenService, request: RequestSecurityToken, tokenDescriptor: SecurityTokenDescriptor) -> RequestSecurityTokenResponse """
        ...

    def GetScope(self, *args): #cannot find CLR method
        """ GetScope(self: SecurityTokenService, principal: ClaimsPrincipal, request: RequestSecurityToken) -> Scope """
        ...

    def GetSecurityTokenHandler(self, *args): #cannot find CLR method
        """ GetSecurityTokenHandler(self: SecurityTokenService, requestedTokenType: str) -> SecurityTokenHandler """
        ...

    def GetTokenLifetime(self, *args): #cannot find CLR method
        """ GetTokenLifetime(self: SecurityTokenService, requestLifetime: Lifetime) -> Lifetime """
        ...

    def Issue(self, principal:ClaimsPrincipal, request:RequestSecurityToken) -> RequestSecurityTokenResponse:
        """ Issue(self: SecurityTokenService, principal: ClaimsPrincipal, request: RequestSecurityToken) -> RequestSecurityTokenResponse """
        ...

    def Renew(self, principal:ClaimsPrincipal, request:RequestSecurityToken) -> RequestSecurityTokenResponse:
        """ Renew(self: SecurityTokenService, principal: ClaimsPrincipal, request: RequestSecurityToken) -> RequestSecurityTokenResponse """
        ...

    def Validate(self, principal:ClaimsPrincipal, request:RequestSecurityToken) -> RequestSecurityTokenResponse:
        """ Validate(self: SecurityTokenService, principal: ClaimsPrincipal, request: RequestSecurityToken) -> RequestSecurityTokenResponse """
        ...

    def ValidateRequest(self, *args): #cannot find CLR method
        """ ValidateRequest(self: SecurityTokenService, request: RequestSecurityToken) """
        ...



class SignatureVerificationFailedException(SecurityTokenException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SignatureVerificationFailedException()
    SignatureVerificationFailedException(message: str)
    SignatureVerificationFailedException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class TypedAsyncResult(AsyncResult): # skipped bases: <type 'IDisposable'>, <type 'IAsyncResult'>, <type 'object'>
    """
    TypedAsyncResult[T](state: object)
    TypedAsyncResult[T](callback: AsyncCallback, state: object)
    """
    @property
    def Result(self): # -> T
        """ Get: Result(self: TypedAsyncResult[T]) -> T """
        ...



class UnsupportedTokenTypeBadRequestException(BadRequestException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    UnsupportedTokenTypeBadRequestException()
    UnsupportedTokenTypeBadRequestException(tokenType: str)
    UnsupportedTokenTypeBadRequestException(message: str, exception: Exception)
    """
    @property
    def TokenType(self) -> str:
        """
        Get: TokenType(self: UnsupportedTokenTypeBadRequestException) -> str
        Set: TokenType(self: UnsupportedTokenTypeBadRequestException) = value
        """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: UnsupportedTokenTypeBadRequestException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


# variables with complex values

