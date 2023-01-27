# encoding: utf-8
# module System.IdentityModel.Tokens calls itself Tokens
# from System.IdentityModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import (Array, DateTime, Enum, IDisposable, Nullable, 
    SystemException, TimeSpan, Type, Uri)

from System.Collections import IDictionary, IEnumerable, IList

from System.Collections.Generic import Dictionary

from System.Collections.ObjectModel import ReadOnlyCollection

from System.IdentityModel.Claims import ClaimSet

from System.IdentityModel.Configuration import (ICustomIdentityConfiguration, 
    IdentityModelCaches)

from System.IdentityModel.Policy import IAuthorizationPolicy

from System.IdentityModel.Protocols.WSTrust import (Lifetime, 
    RequestSecurityTokenResponse)

from System.IdentityModel.Selectors import (AudienceUriMode, 
    SamlSecurityTokenAuthenticator, SecurityTokenResolver, 
    SecurityTokenSerializer, X509CertificateValidator)

from System.Messaging import HashAlgorithm

from System.Net import NetworkCredential

from System.Runtime.Serialization import ISerializable

from System.Security.Claims import (AuthenticationInformation, ClaimsIdentity, 
    ClaimsPrincipal)

from System.Security.Cryptography import (AsymmetricAlgorithm, 
    AsymmetricSignatureDeformatter, AsymmetricSignatureFormatter, 
    ICryptoTransform, KeyedHashAlgorithm, RSA, SymmetricAlgorithm)

from System.Security.Cryptography.X509Certificates import (StoreLocation, 
    StoreName, X509Certificate2, X509ChainPolicy, X509RevocationMode)

from System.Security.Principal import (TokenImpersonationLevel, 
    WindowsIdentity)

from System.ServiceModel.Security import X509CertificateValidationMode

from System.Xml import (IXmlDictionary, UniqueId, XmlDictionaryReader, 
    XmlDictionaryWriter, XmlElement, XmlQualifiedName, XmlReader, XmlWriter)

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    ICanonicalWriterEndRootElementCallback, 
    ReadOnlyCollection[CookieTransform], T, TClause, 
    X509CertificateValidatorEx, field#)
"""

# no functions
# classes

class AggregateTokenResolver(SecurityTokenResolver): # skipped bases: <type 'ICustomIdentityConfiguration'>, <type 'object'>
    """ AggregateTokenResolver(tokenResolvers: IEnumerable[SecurityTokenResolver]) """
    @property
    def TokenResolvers(self) -> ReadOnlyCollection:
        """ Get: TokenResolvers(self: AggregateTokenResolver) -> ReadOnlyCollection[SecurityTokenResolver] """
        ...


    def __new__(cls, tokenResolvers:IEnumerable) -> Self:
        """ __new__(cls: type, tokenResolvers: IEnumerable[SecurityTokenResolver]) """
        ...


class ProofDescriptor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def KeyIdentifier(self) -> SecurityKeyIdentifier:
        """ Get: KeyIdentifier(self: ProofDescriptor) -> SecurityKeyIdentifier """
        ...


    def ApplyTo(self, response:RequestSecurityTokenResponse): # -> 
        """ ApplyTo(self: ProofDescriptor, response: RequestSecurityTokenResponse) """
        ...


class AsymmetricProofDescriptor(ProofDescriptor): # skipped bases: <type 'object'>
    """
    AsymmetricProofDescriptor()
    AsymmetricProofDescriptor(rsaAlgorithm: RSA)
    AsymmetricProofDescriptor(keyIdentifier: SecurityKeyIdentifier)
    """
    def __new__(cls, *__args:RSA) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, rsaAlgorithm: RSA)
        __new__(cls: type, keyIdentifier: SecurityKeyIdentifier)
        """
        ...


class SecurityKey: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def KeySize(self) -> int:
        """ Get: KeySize(self: SecurityKey) -> int """
        ...


    def DecryptKey(self, algorithm:str, keyData:Array) -> Array:
        """ DecryptKey(self: SecurityKey, algorithm: str, keyData: Array[Byte]) -> Array[Byte] """
        ...

    def EncryptKey(self, algorithm:str, keyData:Array) -> Array:
        """ EncryptKey(self: SecurityKey, algorithm: str, keyData: Array[Byte]) -> Array[Byte] """
        ...

    def IsAsymmetricAlgorithm(self, algorithm:str) -> bool:
        """ IsAsymmetricAlgorithm(self: SecurityKey, algorithm: str) -> bool """
        ...

    def IsSupportedAlgorithm(self, algorithm:str) -> bool:
        """ IsSupportedAlgorithm(self: SecurityKey, algorithm: str) -> bool """
        ...

    def IsSymmetricAlgorithm(self, algorithm:str) -> bool:
        """ IsSymmetricAlgorithm(self: SecurityKey, algorithm: str) -> bool """
        ...


class AsymmetricSecurityKey(SecurityKey): # skipped bases: <type 'object'>
    """ no doc """
    def GetAsymmetricAlgorithm(self, algorithm:str, privateKey:bool) -> AsymmetricAlgorithm:
        """ GetAsymmetricAlgorithm(self: AsymmetricSecurityKey, algorithm: str, privateKey: bool) -> AsymmetricAlgorithm """
        ...

    def GetHashAlgorithmForSignature(self, algorithm:str) -> HashAlgorithm:
        """ GetHashAlgorithmForSignature(self: AsymmetricSecurityKey, algorithm: str) -> HashAlgorithm """
        ...

    def GetSignatureDeformatter(self, algorithm:str) -> AsymmetricSignatureDeformatter:
        """ GetSignatureDeformatter(self: AsymmetricSecurityKey, algorithm: str) -> AsymmetricSignatureDeformatter """
        ...

    def GetSignatureFormatter(self, algorithm:str) -> AsymmetricSignatureFormatter:
        """ GetSignatureFormatter(self: AsymmetricSecurityKey, algorithm: str) -> AsymmetricSignatureFormatter """
        ...

    def HasPrivateKey(self) -> bool:
        """ HasPrivateKey(self: AsymmetricSecurityKey) -> bool """
        ...


class AudienceRestriction: # skipped bases: <type 'object'>, <type 'object'>
    """
    AudienceRestriction()
    AudienceRestriction(audienceMode: AudienceUriMode)
    """
    @property
    def AllowedAudienceUris(self) -> Collection:
        """ Get: AllowedAudienceUris(self: AudienceRestriction) -> Collection[Uri] """
        ...

    @property
    def AudienceMode(self) -> AudienceUriMode:
        """
        Get: AudienceMode(self: AudienceRestriction) -> AudienceUriMode
        Set: AudienceMode(self: AudienceRestriction) = value
        """
        ...



class SecurityTokenException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SecurityTokenException()
    SecurityTokenException(message: str)
    SecurityTokenException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SecurityTokenValidationException(SecurityTokenException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SecurityTokenValidationException()
    SecurityTokenValidationException(message: str)
    SecurityTokenValidationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class AudienceUriValidationFailedException(SecurityTokenValidationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    AudienceUriValidationFailedException()
    AudienceUriValidationFailedException(message: str)
    AudienceUriValidationFailedException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class AuthenticationContext: # skipped bases: <type 'object'>, <type 'object'>
    """ AuthenticationContext() """
    @property
    def Authorities(self) -> Collection:
        """ Get: Authorities(self: AuthenticationContext) -> Collection[str] """
        ...

    @property
    def ContextClass(self) -> str:
        """
        Get: ContextClass(self: AuthenticationContext) -> str
        Set: ContextClass(self: AuthenticationContext) = value
        """
        ...

    @property
    def ContextDeclaration(self) -> str:
        """
        Get: ContextDeclaration(self: AuthenticationContext) -> str
        Set: ContextDeclaration(self: AuthenticationContext) = value
        """
        ...



class AuthenticationMethods: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    HardwareToken: str = ...
    Kerberos: str = ...
    Namespace: str = ...
    Password: str = ...
    Pgp: str = ...
    SecureRemotePassword: str = ...
    Signature: str = ...
    Smartcard: str = ...
    SmartcardPki: str = ...
    Spki: str = ...
    TlsClient: str = ...
    Unspecified: str = ...
    Windows: str = ...
    X509: str = ...
    Xkms: str = ...
    __all__: list = ...


class SecurityKeyIdentifierClause: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CanCreateKey(self) -> bool:
        """ Get: CanCreateKey(self: SecurityKeyIdentifierClause) -> bool """
        ...

    @property
    def ClauseType(self) -> str:
        """ Get: ClauseType(self: SecurityKeyIdentifierClause) -> str """
        ...

    @property
    def DerivationLength(self) -> int:
        """ Get: DerivationLength(self: SecurityKeyIdentifierClause) -> int """
        ...

    @property
    def Id(self) -> str:
        """
        Get: Id(self: SecurityKeyIdentifierClause) -> str
        Set: Id(self: SecurityKeyIdentifierClause) = value
        """
        ...


    def CreateKey(self) -> SecurityKey:
        """ CreateKey(self: SecurityKeyIdentifierClause) -> SecurityKey """
        ...

    def GetDerivationNonce(self) -> Array:
        """ GetDerivationNonce(self: SecurityKeyIdentifierClause) -> Array[Byte] """
        ...

    def Matches(self, keyIdentifierClause:SecurityKeyIdentifierClause) -> bool:
        """ Matches(self: SecurityKeyIdentifierClause, keyIdentifierClause: SecurityKeyIdentifierClause) -> bool """
        ...


class BinaryKeyIdentifierClause(SecurityKeyIdentifierClause): # skipped bases: <type 'object'>
    """ no doc """
    def GetBuffer(self) -> Array:
        """ GetBuffer(self: BinaryKeyIdentifierClause) -> Array[Byte] """
        ...

    def GetRawBuffer(self, *args): #cannot find CLR method
        """ GetRawBuffer(self: BinaryKeyIdentifierClause) -> Array[Byte] """
        ...


class BootstrapContext(ISerializable): # skipped bases: <type 'object'>
    """
    BootstrapContext(token: SecurityToken, tokenHandler: SecurityTokenHandler)
    BootstrapContext(token: str)
    BootstrapContext(token: Array[Byte])
    """
    @property
    def SecurityToken(self) -> SecurityToken:
        """ Get: SecurityToken(self: BootstrapContext) -> SecurityToken """
        ...

    @property
    def SecurityTokenHandler(self) -> SecurityTokenHandler:
        """ Get: SecurityTokenHandler(self: BootstrapContext) -> SecurityTokenHandler """
        ...

    @property
    def Token(self) -> str:
        """ Get: Token(self: BootstrapContext) -> str """
        ...

    @property
    def TokenBytes(self) -> Array:
        """ Get: TokenBytes(self: BootstrapContext) -> Array[Byte] """
        ...



class ComputedKeyAlgorithms: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Psha1: str = ...
    __all__: list = ...


class IssuerNameRegistry(ICustomIdentityConfiguration): # skipped bases: <type 'object'>
    """ no doc """
    def GetIssuerName(self, securityToken:SecurityToken, requestedIssuerName:str = ...) -> str:
        """
        GetIssuerName(self: IssuerNameRegistry, securityToken: SecurityToken, requestedIssuerName: str) -> str
        GetIssuerName(self: IssuerNameRegistry, securityToken: SecurityToken) -> str
        """
        ...

    def GetWindowsIssuerName(self) -> str:
        """ GetWindowsIssuerName(self: IssuerNameRegistry) -> str """
        ...


class ConfigurationBasedIssuerNameRegistry(IssuerNameRegistry): # skipped bases: <type 'ICustomIdentityConfiguration'>, <type 'object'>
    """ ConfigurationBasedIssuerNameRegistry() """
    @property
    def ConfiguredTrustedIssuers(self) -> IDictionary:
        """ Get: ConfiguredTrustedIssuers(self: ConfigurationBasedIssuerNameRegistry) -> IDictionary[str, str] """
        ...


    def AddTrustedIssuer(self, certificateThumbprint:str, name:str): # -> 
        """ AddTrustedIssuer(self: ConfigurationBasedIssuerNameRegistry, certificateThumbprint: str, name: str) """
        ...


class EmptySecurityKeyIdentifierClause(SecurityKeyIdentifierClause): # skipped bases: <type 'object'>
    """
    EmptySecurityKeyIdentifierClause()
    EmptySecurityKeyIdentifierClause(context: object)
    """
    @property
    def Context(self) -> object:
        """ Get: Context(self: EmptySecurityKeyIdentifierClause) -> object """
        ...



class EncryptingCredentials: # skipped bases: <type 'object'>, <type 'object'>
    """
    EncryptingCredentials()
    EncryptingCredentials(key: SecurityKey, keyIdentifier: SecurityKeyIdentifier, algorithm: str)
    """
    @property
    def Algorithm(self) -> str:
        """
        Get: Algorithm(self: EncryptingCredentials) -> str
        Set: Algorithm(self: EncryptingCredentials) = value
        """
        ...

    @property
    def SecurityKey(self) -> SecurityKey:
        """
        Get: SecurityKey(self: EncryptingCredentials) -> SecurityKey
        Set: SecurityKey(self: EncryptingCredentials) = value
        """
        ...

    @property
    def SecurityKeyIdentifier(self) -> SecurityKeyIdentifier:
        """
        Get: SecurityKeyIdentifier(self: EncryptingCredentials) -> SecurityKeyIdentifier
        Set: SecurityKeyIdentifier(self: EncryptingCredentials) = value
        """
        ...



class EncryptedKeyEncryptingCredentials(EncryptingCredentials): # skipped bases: <type 'object'>
    """
    EncryptedKeyEncryptingCredentials(certificate: X509Certificate2)
    EncryptedKeyEncryptingCredentials(certificate: X509Certificate2, keyWrappingAlgorithm: str, keySizeInBits: int, encryptionAlgorithm: str)
    EncryptedKeyEncryptingCredentials(wrappingCredentials: EncryptingCredentials, keySizeInBits: int, encryptionAlgorithm: str)
    """
    @property
    def WrappingCredentials(self) -> EncryptingCredentials:
        """ Get: WrappingCredentials(self: EncryptedKeyEncryptingCredentials) -> EncryptingCredentials """
        ...



class EncryptedKeyIdentifierClause(BinaryKeyIdentifierClause): # skipped bases: <type 'object'>
    """
    EncryptedKeyIdentifierClause(encryptedKey: Array[Byte], encryptionMethod: str)
    EncryptedKeyIdentifierClause(encryptedKey: Array[Byte], encryptionMethod: str, encryptingKeyIdentifier: SecurityKeyIdentifier)
    EncryptedKeyIdentifierClause(encryptedKey: Array[Byte], encryptionMethod: str, encryptingKeyIdentifier: SecurityKeyIdentifier, carriedKeyName: str)
    EncryptedKeyIdentifierClause(encryptedKey: Array[Byte], encryptionMethod: str, encryptingKeyIdentifier: SecurityKeyIdentifier, carriedKeyName: str, derivationNonce: Array[Byte], derivationLength: int)
    """
    @property
    def CarriedKeyName(self) -> str:
        """ Get: CarriedKeyName(self: EncryptedKeyIdentifierClause) -> str """
        ...

    @property
    def EncryptingKeyIdentifier(self) -> SecurityKeyIdentifier:
        """ Get: EncryptingKeyIdentifier(self: EncryptedKeyIdentifierClause) -> SecurityKeyIdentifier """
        ...

    @property
    def EncryptionMethod(self) -> str:
        """ Get: EncryptionMethod(self: EncryptedKeyIdentifierClause) -> str """
        ...


    def GetEncryptedKey(self) -> Array:
        """ GetEncryptedKey(self: EncryptedKeyIdentifierClause) -> Array[Byte] """
        ...

    def ToString(self) -> str:
        """ ToString(self: EncryptedKeyIdentifierClause) -> str """
        ...


class SecurityToken: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Id(self) -> str:
        """ Get: Id(self: SecurityToken) -> str """
        ...

    @property
    def SecurityKeys(self) -> ReadOnlyCollection:
        """ Get: SecurityKeys(self: SecurityToken) -> ReadOnlyCollection[SecurityKey] """
        ...

    @property
    def ValidFrom(self) -> DateTime:
        """ Get: ValidFrom(self: SecurityToken) -> DateTime """
        ...

    @property
    def ValidTo(self) -> DateTime:
        """ Get: ValidTo(self: SecurityToken) -> DateTime """
        ...


    def CanCreateKeyIdentifierClause(self) -> bool:
        """ CanCreateKeyIdentifierClause[T](self: SecurityToken) -> bool """
        ...

    def CreateKeyIdentifierClause(self): # -> T
        """ CreateKeyIdentifierClause[T](self: SecurityToken) -> T """
        ...

    def MatchesKeyIdentifierClause(self, keyIdentifierClause:SecurityKeyIdentifierClause) -> bool:
        """ MatchesKeyIdentifierClause(self: SecurityToken, keyIdentifierClause: SecurityKeyIdentifierClause) -> bool """
        ...

    def ResolveKeyIdentifierClause(self, keyIdentifierClause:SecurityKeyIdentifierClause) -> SecurityKey:
        """ ResolveKeyIdentifierClause(self: SecurityToken, keyIdentifierClause: SecurityKeyIdentifierClause) -> SecurityKey """
        ...


class EncryptedSecurityToken(SecurityToken): # skipped bases: <type 'object'>
    """ EncryptedSecurityToken(token: SecurityToken, encryptingCredentials: EncryptingCredentials) """
    @property
    def EncryptingCredentials(self) -> EncryptingCredentials:
        """ Get: EncryptingCredentials(self: EncryptedSecurityToken) -> EncryptingCredentials """
        ...

    @property
    def Token(self) -> SecurityToken:
        """ Get: Token(self: EncryptedSecurityToken) -> SecurityToken """
        ...


    def __new__(cls, token:SecurityToken, encryptingCredentials:EncryptingCredentials) -> Self:
        """ __new__(cls: type, token: SecurityToken, encryptingCredentials: EncryptingCredentials) """
        ...


class SecurityTokenHandler(ICustomIdentityConfiguration): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CanValidateToken(self) -> bool:
        """ Get: CanValidateToken(self: SecurityTokenHandler) -> bool """
        ...

    @property
    def CanWriteToken(self) -> bool:
        """ Get: CanWriteToken(self: SecurityTokenHandler) -> bool """
        ...

    @property
    def Configuration(self) -> SecurityTokenHandlerConfiguration:
        """
        Get: Configuration(self: SecurityTokenHandler) -> SecurityTokenHandlerConfiguration
        Set: Configuration(self: SecurityTokenHandler) = value
        """
        ...

    @property
    def ContainingCollection(self) -> SecurityTokenHandlerCollection:
        """ Get: ContainingCollection(self: SecurityTokenHandler) -> SecurityTokenHandlerCollection """
        ...

    @property
    def TokenType(self) -> Type:
        """ Get: TokenType(self: SecurityTokenHandler) -> Type """
        ...


    def CanReadKeyIdentifierClause(self, reader:XmlReader) -> bool:
        """ CanReadKeyIdentifierClause(self: SecurityTokenHandler, reader: XmlReader) -> bool """
        ...

    def CanReadToken(self, *__args:XmlReader) -> bool:
        """
        CanReadToken(self: SecurityTokenHandler, reader: XmlReader) -> bool
        CanReadToken(self: SecurityTokenHandler, tokenString: str) -> bool
        """
        ...

    def CanWriteKeyIdentifierClause(self, securityKeyIdentifierClause:SecurityKeyIdentifierClause) -> bool:
        """ CanWriteKeyIdentifierClause(self: SecurityTokenHandler, securityKeyIdentifierClause: SecurityKeyIdentifierClause) -> bool """
        ...

    def CreateSecurityTokenReference(self, token:SecurityToken, attached:bool) -> SecurityKeyIdentifierClause:
        """ CreateSecurityTokenReference(self: SecurityTokenHandler, token: SecurityToken, attached: bool) -> SecurityKeyIdentifierClause """
        ...

    def CreateToken(self, tokenDescriptor:SecurityTokenDescriptor) -> SecurityToken:
        """ CreateToken(self: SecurityTokenHandler, tokenDescriptor: SecurityTokenDescriptor) -> SecurityToken """
        ...

    def DetectReplayedToken(self, *args): #cannot find CLR method
        """ DetectReplayedToken(self: SecurityTokenHandler, token: SecurityToken) """
        ...

    def GetTokenTypeIdentifiers(self) -> Array:
        """ GetTokenTypeIdentifiers(self: SecurityTokenHandler) -> Array[str] """
        ...

    def ReadKeyIdentifierClause(self, reader:XmlReader) -> SecurityKeyIdentifierClause:
        """ ReadKeyIdentifierClause(self: SecurityTokenHandler, reader: XmlReader) -> SecurityKeyIdentifierClause """
        ...

    def ReadToken(self, *__args:XmlReader) -> SecurityToken:
        """
        ReadToken(self: SecurityTokenHandler, reader: XmlReader, tokenResolver: SecurityTokenResolver) -> SecurityToken
        ReadToken(self: SecurityTokenHandler, reader: XmlReader) -> SecurityToken
        ReadToken(self: SecurityTokenHandler, tokenString: str) -> SecurityToken
        """
        ...

    def TraceTokenValidationFailure(self, *args): #cannot find CLR method
        """ TraceTokenValidationFailure(self: SecurityTokenHandler, token: SecurityToken, errorMessage: str) """
        ...

    def TraceTokenValidationSuccess(self, *args): #cannot find CLR method
        """ TraceTokenValidationSuccess(self: SecurityTokenHandler, token: SecurityToken) """
        ...

    def ValidateToken(self, token:SecurityToken) -> ReadOnlyCollection:
        """ ValidateToken(self: SecurityTokenHandler, token: SecurityToken) -> ReadOnlyCollection[ClaimsIdentity] """
        ...

    def WriteKeyIdentifierClause(self, writer:XmlWriter, securityKeyIdentifierClause:SecurityKeyIdentifierClause): # -> 
        """ WriteKeyIdentifierClause(self: SecurityTokenHandler, writer: XmlWriter, securityKeyIdentifierClause: SecurityKeyIdentifierClause) """
        ...

    def WriteToken(self, *__args:SecurityToken) -> str:
        """ WriteToken(self: SecurityTokenHandler, writer: XmlWriter, token: SecurityToken)WriteToken(self: SecurityTokenHandler, token: SecurityToken) -> str """
        ...


class EncryptedSecurityTokenHandler(SecurityTokenHandler): # skipped bases: <type 'ICustomIdentityConfiguration'>, <type 'object'>
    """ EncryptedSecurityTokenHandler() """
    @property
    def KeyInfoSerializer(self) -> SecurityTokenSerializer:
        """
        Get: KeyInfoSerializer(self: EncryptedSecurityTokenHandler) -> SecurityTokenSerializer
        Set: KeyInfoSerializer(self: EncryptedSecurityTokenHandler) = value
        """
        ...



class EncryptedTokenDecryptionFailedException(SecurityTokenException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    EncryptedTokenDecryptionFailedException()
    EncryptedTokenDecryptionFailedException(message: str)
    EncryptedTokenDecryptionFailedException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class GenericXmlSecurityKeyIdentifierClause(SecurityKeyIdentifierClause): # skipped bases: <type 'object'>
    """
    GenericXmlSecurityKeyIdentifierClause(referenceXml: XmlElement)
    GenericXmlSecurityKeyIdentifierClause(referenceXml: XmlElement, derivationNonce: Array[Byte], derivationLength: int)
    """
    @property
    def ReferenceXml(self) -> XmlElement:
        """ Get: ReferenceXml(self: GenericXmlSecurityKeyIdentifierClause) -> XmlElement """
        ...



class GenericXmlSecurityToken(SecurityToken): # skipped bases: <type 'object'>
    """ GenericXmlSecurityToken(tokenXml: XmlElement, proofToken: SecurityToken, effectiveTime: DateTime, expirationTime: DateTime, internalTokenReference: SecurityKeyIdentifierClause, externalTokenReference: SecurityKeyIdentifierClause, authorizationPolicies: ReadOnlyCollection[IAuthorizationPolicy]) """
    @property
    def AuthorizationPolicies(self) -> ReadOnlyCollection:
        """ Get: AuthorizationPolicies(self: GenericXmlSecurityToken) -> ReadOnlyCollection[IAuthorizationPolicy] """
        ...

    @property
    def ExternalTokenReference(self) -> SecurityKeyIdentifierClause:
        """ Get: ExternalTokenReference(self: GenericXmlSecurityToken) -> SecurityKeyIdentifierClause """
        ...

    @property
    def InternalTokenReference(self) -> SecurityKeyIdentifierClause:
        """ Get: InternalTokenReference(self: GenericXmlSecurityToken) -> SecurityKeyIdentifierClause """
        ...

    @property
    def ProofToken(self) -> SecurityToken:
        """ Get: ProofToken(self: GenericXmlSecurityToken) -> SecurityToken """
        ...

    @property
    def TokenXml(self) -> XmlElement:
        """ Get: TokenXml(self: GenericXmlSecurityToken) -> XmlElement """
        ...


    def ToString(self) -> str:
        """ ToString(self: GenericXmlSecurityToken) -> str """
        ...

    def __new__(cls, tokenXml:XmlElement, proofToken:SecurityToken, effectiveTime:DateTime, expirationTime:DateTime, internalTokenReference:SecurityKeyIdentifierClause, externalTokenReference:SecurityKeyIdentifierClause, authorizationPolicies:ReadOnlyCollection) -> Self:
        """ __new__(cls: type, tokenXml: XmlElement, proofToken: SecurityToken, effectiveTime: DateTime, expirationTime: DateTime, internalTokenReference: SecurityKeyIdentifierClause, externalTokenReference: SecurityKeyIdentifierClause, authorizationPolicies: ReadOnlyCollection[IAuthorizationPolicy]) """
        ...


class SymmetricSecurityKey(SecurityKey): # skipped bases: <type 'object'>
    """ no doc """
    def GenerateDerivedKey(self, algorithm:str, label:Array, nonce:Array, derivedKeyLength:int, offset:int) -> Array:
        """ GenerateDerivedKey(self: SymmetricSecurityKey, algorithm: str, label: Array[Byte], nonce: Array[Byte], derivedKeyLength: int, offset: int) -> Array[Byte] """
        ...

    def GetDecryptionTransform(self, algorithm:str, iv:Array) -> ICryptoTransform:
        """ GetDecryptionTransform(self: SymmetricSecurityKey, algorithm: str, iv: Array[Byte]) -> ICryptoTransform """
        ...

    def GetEncryptionTransform(self, algorithm:str, iv:Array) -> ICryptoTransform:
        """ GetEncryptionTransform(self: SymmetricSecurityKey, algorithm: str, iv: Array[Byte]) -> ICryptoTransform """
        ...

    def GetIVSize(self, algorithm:str) -> int:
        """ GetIVSize(self: SymmetricSecurityKey, algorithm: str) -> int """
        ...

    def GetKeyedHashAlgorithm(self, algorithm:str) -> KeyedHashAlgorithm:
        """ GetKeyedHashAlgorithm(self: SymmetricSecurityKey, algorithm: str) -> KeyedHashAlgorithm """
        ...

    def GetSymmetricAlgorithm(self, algorithm:str) -> SymmetricAlgorithm:
        """ GetSymmetricAlgorithm(self: SymmetricSecurityKey, algorithm: str) -> SymmetricAlgorithm """
        ...

    def GetSymmetricKey(self) -> Array:
        """ GetSymmetricKey(self: SymmetricSecurityKey) -> Array[Byte] """
        ...


class InMemorySymmetricSecurityKey(SymmetricSecurityKey): # skipped bases: <type 'object'>
    """
    InMemorySymmetricSecurityKey(symmetricKey: Array[Byte])
    InMemorySymmetricSecurityKey(symmetricKey: Array[Byte], cloneBuffer: bool)
    """
    @property
    def KeySize(self) -> int:
        """ Get: KeySize(self: InMemorySymmetricSecurityKey) -> int """
        ...


    def DecryptKey(self, algorithm:str, keyData:Array) -> Array:
        """ DecryptKey(self: InMemorySymmetricSecurityKey, algorithm: str, keyData: Array[Byte]) -> Array[Byte] """
        ...

    def EncryptKey(self, algorithm:str, keyData:Array) -> Array:
        """ EncryptKey(self: InMemorySymmetricSecurityKey, algorithm: str, keyData: Array[Byte]) -> Array[Byte] """
        ...

    def IsAsymmetricAlgorithm(self, algorithm:str) -> bool:
        """ IsAsymmetricAlgorithm(self: InMemorySymmetricSecurityKey, algorithm: str) -> bool """
        ...

    def IsSupportedAlgorithm(self, algorithm:str) -> bool:
        """ IsSupportedAlgorithm(self: InMemorySymmetricSecurityKey, algorithm: str) -> bool """
        ...

    def IsSymmetricAlgorithm(self, algorithm:str) -> bool:
        """ IsSymmetricAlgorithm(self: InMemorySymmetricSecurityKey, algorithm: str) -> bool """
        ...

    def __new__(cls, symmetricKey:Array, cloneBuffer:bool = ...) -> Self:
        """
        __new__(cls: type, symmetricKey: Array[Byte])
        __new__(cls: type, symmetricKey: Array[Byte], cloneBuffer: bool)
        """
        ...


class IssuerTokenResolver(SecurityTokenResolver): # skipped bases: <type 'ICustomIdentityConfiguration'>, <type 'object'>
    """
    IssuerTokenResolver()
    IssuerTokenResolver(wrappedTokenResolver: SecurityTokenResolver)
    """
    @property
    def WrappedTokenResolver(self) -> SecurityTokenResolver:
        """ Get: WrappedTokenResolver(self: IssuerTokenResolver) -> SecurityTokenResolver """
        ...


    def __new__(cls, wrappedTokenResolver:SecurityTokenResolver = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, wrappedTokenResolver: SecurityTokenResolver)
        """
        ...

    DefaultStoreLocation: StoreLocation = ...
    DefaultStoreName: StoreName = ...


class WindowsSecurityToken(IDisposable, SecurityToken): # skipped bases: <type 'object'>
    """
    WindowsSecurityToken(windowsIdentity: WindowsIdentity)
    WindowsSecurityToken(windowsIdentity: WindowsIdentity, id: str)
    WindowsSecurityToken(windowsIdentity: WindowsIdentity, id: str, authenticationType: str)
    """
    @property
    def AuthenticationType(self) -> str:
        """ Get: AuthenticationType(self: WindowsSecurityToken) -> str """
        ...

    @property
    def WindowsIdentity(self) -> WindowsIdentity:
        """ Get: WindowsIdentity(self: WindowsSecurityToken) -> WindowsIdentity """
        ...


    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: WindowsSecurityToken, id: str, effectiveTime: DateTime, expirationTime: DateTime, windowsIdentity: WindowsIdentity, clone: bool)Initialize(self: WindowsSecurityToken, id: str, authenticationType: str, effectiveTime: DateTime, expirationTime: DateTime, windowsIdentity: WindowsIdentity, clone: bool) """
        ...

    def ThrowIfDisposed(self, *args): #cannot find CLR method
        """ ThrowIfDisposed(self: WindowsSecurityToken) """
        ...

    def __new__(cls, windowsIdentity:WindowsIdentity, id:str = ..., authenticationType:str = ...) -> Self:
        """
        __new__(cls: type, windowsIdentity: WindowsIdentity)
        __new__(cls: type, windowsIdentity: WindowsIdentity, id: str)
        __new__(cls: type, windowsIdentity: WindowsIdentity, id: str, authenticationType: str)
        __new__(cls: type)
        """
        ...


class KerberosReceiverSecurityToken(WindowsSecurityToken): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    KerberosReceiverSecurityToken(request: Array[Byte])
    KerberosReceiverSecurityToken(request: Array[Byte], id: str)
    KerberosReceiverSecurityToken(request: Array[Byte], id: str, valueTypeUri: str)
    """
    @property
    def SecurityKey(self) -> SymmetricSecurityKey:
        """ Get: SecurityKey(self: KerberosReceiverSecurityToken) -> SymmetricSecurityKey """
        ...

    @property
    def ValueTypeUri(self) -> str:
        """ Get: ValueTypeUri(self: KerberosReceiverSecurityToken) -> str """
        ...


    def CanCreateKeyIdentifierClause(self) -> bool:
        """ CanCreateKeyIdentifierClause[T](self: KerberosReceiverSecurityToken) -> bool """
        ...

    def CreateKeyIdentifierClause(self): # -> T
        """ CreateKeyIdentifierClause[T](self: KerberosReceiverSecurityToken) -> T """
        ...

    def GetRequest(self) -> Array:
        """ GetRequest(self: KerberosReceiverSecurityToken) -> Array[Byte] """
        ...

    def MatchesKeyIdentifierClause(self, keyIdentifierClause:SecurityKeyIdentifierClause) -> bool:
        """ MatchesKeyIdentifierClause(self: KerberosReceiverSecurityToken, keyIdentifierClause: SecurityKeyIdentifierClause) -> bool """
        ...


class KerberosRequestorSecurityToken(SecurityToken): # skipped bases: <type 'object'>
    """
    KerberosRequestorSecurityToken(servicePrincipalName: str)
    KerberosRequestorSecurityToken(servicePrincipalName: str, tokenImpersonationLevel: TokenImpersonationLevel, networkCredential: NetworkCredential, id: str)
    """
    @property
    def SecurityKey(self) -> SymmetricSecurityKey:
        """ Get: SecurityKey(self: KerberosRequestorSecurityToken) -> SymmetricSecurityKey """
        ...

    @property
    def ServicePrincipalName(self) -> str:
        """ Get: ServicePrincipalName(self: KerberosRequestorSecurityToken) -> str """
        ...


    def GetRequest(self) -> Array:
        """ GetRequest(self: KerberosRequestorSecurityToken) -> Array[Byte] """
        ...

    def __new__(cls, servicePrincipalName:str, tokenImpersonationLevel:TokenImpersonationLevel = ..., networkCredential:NetworkCredential = ..., id:str = ...) -> Self:
        """
        __new__(cls: type, servicePrincipalName: str)
        __new__(cls: type, servicePrincipalName: str, tokenImpersonationLevel: TokenImpersonationLevel, networkCredential: NetworkCredential, id: str)
        """
        ...


class KerberosSecurityTokenHandler(SecurityTokenHandler): # skipped bases: <type 'ICustomIdentityConfiguration'>, <type 'object'>
    """ KerberosSecurityTokenHandler() """
    pass

class KerberosTicketHashKeyIdentifierClause(BinaryKeyIdentifierClause): # skipped bases: <type 'object'>
    """
    KerberosTicketHashKeyIdentifierClause(ticketHash: Array[Byte])
    KerberosTicketHashKeyIdentifierClause(ticketHash: Array[Byte], derivationNonce: Array[Byte], derivationLength: int)
    """
    def GetKerberosTicketHash(self) -> Array:
        """ GetKerberosTicketHash(self: KerberosTicketHashKeyIdentifierClause) -> Array[Byte] """
        ...

    def ToString(self) -> str:
        """ ToString(self: KerberosTicketHashKeyIdentifierClause) -> str """
        ...


class LocalIdKeyIdentifierClause(SecurityKeyIdentifierClause): # skipped bases: <type 'object'>
    """
    LocalIdKeyIdentifierClause(localId: str)
    LocalIdKeyIdentifierClause(localId: str, ownerType: Type)
    LocalIdKeyIdentifierClause(localId: str, derivationNonce: Array[Byte], derivationLength: int, ownerType: Type)
    """
    @property
    def LocalId(self) -> str:
        """ Get: LocalId(self: LocalIdKeyIdentifierClause) -> str """
        ...

    @property
    def OwnerType(self) -> Type:
        """ Get: OwnerType(self: LocalIdKeyIdentifierClause) -> Type """
        ...


    def ToString(self) -> str:
        """ ToString(self: LocalIdKeyIdentifierClause) -> str """
        ...


class RsaKeyIdentifierClause(SecurityKeyIdentifierClause): # skipped bases: <type 'object'>
    """ RsaKeyIdentifierClause(rsa: RSA) """
    @property
    def Rsa(self) -> RSA:
        """ Get: Rsa(self: RsaKeyIdentifierClause) -> RSA """
        ...


    def GetExponent(self) -> Array:
        """ GetExponent(self: RsaKeyIdentifierClause) -> Array[Byte] """
        ...

    def GetModulus(self) -> Array:
        """ GetModulus(self: RsaKeyIdentifierClause) -> Array[Byte] """
        ...

    def ToString(self) -> str:
        """ ToString(self: RsaKeyIdentifierClause) -> str """
        ...

    def WriteExponentAsBase64(self, writer:XmlWriter): # -> 
        """ WriteExponentAsBase64(self: RsaKeyIdentifierClause, writer: XmlWriter) """
        ...

    def WriteModulusAsBase64(self, writer:XmlWriter): # -> 
        """ WriteModulusAsBase64(self: RsaKeyIdentifierClause, writer: XmlWriter) """
        ...


class RsaSecurityKey(AsymmetricSecurityKey): # skipped bases: <type 'object'>
    """ RsaSecurityKey(rsa: RSA) """
    @property
    def KeySize(self) -> int:
        """ Get: KeySize(self: RsaSecurityKey) -> int """
        ...


    def DecryptKey(self, algorithm:str, keyData:Array) -> Array:
        """ DecryptKey(self: RsaSecurityKey, algorithm: str, keyData: Array[Byte]) -> Array[Byte] """
        ...

    def EncryptKey(self, algorithm:str, keyData:Array) -> Array:
        """ EncryptKey(self: RsaSecurityKey, algorithm: str, keyData: Array[Byte]) -> Array[Byte] """
        ...

    def IsAsymmetricAlgorithm(self, algorithm:str) -> bool:
        """ IsAsymmetricAlgorithm(self: RsaSecurityKey, algorithm: str) -> bool """
        ...

    def IsSupportedAlgorithm(self, algorithm:str) -> bool:
        """ IsSupportedAlgorithm(self: RsaSecurityKey, algorithm: str) -> bool """
        ...

    def IsSymmetricAlgorithm(self, algorithm:str) -> bool:
        """ IsSymmetricAlgorithm(self: RsaSecurityKey, algorithm: str) -> bool """
        ...

    def __new__(cls, rsa:RSA) -> Self:
        """ __new__(cls: type, rsa: RSA) """
        ...


class RsaSecurityToken(SecurityToken): # skipped bases: <type 'object'>
    """
    RsaSecurityToken(rsa: RSA)
    RsaSecurityToken(rsa: RSA, id: str)
    """
    @property
    def Rsa(self) -> RSA:
        """ Get: Rsa(self: RsaSecurityToken) -> RSA """
        ...


    def __new__(cls, rsa:RSA, id:str = ...) -> Self:
        """
        __new__(cls: type, rsa: RSA)
        __new__(cls: type, rsa: RSA, id: str)
        """
        ...


class RsaSecurityTokenHandler(SecurityTokenHandler): # skipped bases: <type 'ICustomIdentityConfiguration'>, <type 'object'>
    """ RsaSecurityTokenHandler() """
    pass

class Saml2Action: # skipped bases: <type 'object'>, <type 'object'>
    """ Saml2Action(value: str, actionNamespace: Uri) """
    @property
    def Namespace(self) -> Uri:
        """
        Get: Namespace(self: Saml2Action) -> Uri
        Set: Namespace(self: Saml2Action) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: Saml2Action) -> str
        Set: Value(self: Saml2Action) = value
        """
        ...



class Saml2Advice: # skipped bases: <type 'object'>, <type 'object'>
    """ Saml2Advice() """
    @property
    def AssertionIdReferences(self) -> Collection:
        """ Get: AssertionIdReferences(self: Saml2Advice) -> Collection[Saml2Id] """
        ...

    @property
    def Assertions(self) -> Collection:
        """ Get: Assertions(self: Saml2Advice) -> Collection[Saml2Assertion] """
        ...

    @property
    def AssertionUriReferences(self) -> Collection:
        """ Get: AssertionUriReferences(self: Saml2Advice) -> Collection[Uri] """
        ...



class Saml2Assertion: # skipped bases: <type 'object'>, <type 'object'>
    """ Saml2Assertion(issuer: Saml2NameIdentifier) """
    @property
    def Advice(self) -> Saml2Advice:
        """
        Get: Advice(self: Saml2Assertion) -> Saml2Advice
        Set: Advice(self: Saml2Assertion) = value
        """
        ...

    @property
    def CanWriteSourceData(self) -> bool:
        """ Get: CanWriteSourceData(self: Saml2Assertion) -> bool """
        ...

    @property
    def Conditions(self) -> Saml2Conditions:
        """
        Get: Conditions(self: Saml2Assertion) -> Saml2Conditions
        Set: Conditions(self: Saml2Assertion) = value
        """
        ...

    @property
    def EncryptingCredentials(self) -> EncryptingCredentials:
        """
        Get: EncryptingCredentials(self: Saml2Assertion) -> EncryptingCredentials
        Set: EncryptingCredentials(self: Saml2Assertion) = value
        """
        ...

    @property
    def ExternalEncryptedKeys(self) -> Collection:
        """ Get: ExternalEncryptedKeys(self: Saml2Assertion) -> Collection[EncryptedKeyIdentifierClause] """
        ...

    @property
    def Id(self) -> Saml2Id:
        """
        Get: Id(self: Saml2Assertion) -> Saml2Id
        Set: Id(self: Saml2Assertion) = value
        """
        ...

    @property
    def IssueInstant(self) -> DateTime:
        """
        Get: IssueInstant(self: Saml2Assertion) -> DateTime
        Set: IssueInstant(self: Saml2Assertion) = value
        """
        ...

    @property
    def Issuer(self) -> Saml2NameIdentifier:
        """
        Get: Issuer(self: Saml2Assertion) -> Saml2NameIdentifier
        Set: Issuer(self: Saml2Assertion) = value
        """
        ...

    @property
    def SigningCredentials(self) -> SigningCredentials:
        """
        Get: SigningCredentials(self: Saml2Assertion) -> SigningCredentials
        Set: SigningCredentials(self: Saml2Assertion) = value
        """
        ...

    @property
    def Statements(self) -> Collection:
        """ Get: Statements(self: Saml2Assertion) -> Collection[Saml2Statement] """
        ...

    @property
    def Subject(self) -> Saml2Subject:
        """
        Get: Subject(self: Saml2Assertion) -> Saml2Subject
        Set: Subject(self: Saml2Assertion) = value
        """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: Saml2Assertion) -> str """
        ...


    def WriteSourceData(self, writer:XmlWriter): # -> 
        """ WriteSourceData(self: Saml2Assertion, writer: XmlWriter) """
        ...


class Saml2AssertionKeyIdentifierClause(SecurityKeyIdentifierClause): # skipped bases: <type 'object'>
    """
    Saml2AssertionKeyIdentifierClause(id: str)
    Saml2AssertionKeyIdentifierClause(id: str, derivationNonce: Array[Byte], derivationLength: int)
    """
    def ToString(self) -> str:
        """ ToString(self: Saml2AssertionKeyIdentifierClause) -> str """
        ...


class Saml2Attribute: # skipped bases: <type 'object'>, <type 'object'>
    """
    Saml2Attribute(name: str)
    Saml2Attribute(name: str, values: IEnumerable[str])
    Saml2Attribute(name: str, value: str)
    """
    @property
    def AttributeValueXsiType(self) -> str:
        """
        Get: AttributeValueXsiType(self: Saml2Attribute) -> str
        Set: AttributeValueXsiType(self: Saml2Attribute) = value
        """
        ...

    @property
    def FriendlyName(self) -> str:
        """
        Get: FriendlyName(self: Saml2Attribute) -> str
        Set: FriendlyName(self: Saml2Attribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Saml2Attribute) -> str
        Set: Name(self: Saml2Attribute) = value
        """
        ...

    @property
    def NameFormat(self) -> Uri:
        """
        Get: NameFormat(self: Saml2Attribute) -> Uri
        Set: NameFormat(self: Saml2Attribute) = value
        """
        ...

    @property
    def OriginalIssuer(self) -> str:
        """
        Get: OriginalIssuer(self: Saml2Attribute) -> str
        Set: OriginalIssuer(self: Saml2Attribute) = value
        """
        ...

    @property
    def Values(self) -> Collection:
        """ Get: Values(self: Saml2Attribute) -> Collection[str] """
        ...



class Saml2Statement: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class Saml2AttributeStatement(Saml2Statement): # skipped bases: <type 'object'>
    """
    Saml2AttributeStatement()
    Saml2AttributeStatement(attribute: Saml2Attribute)
    Saml2AttributeStatement(attributes: IEnumerable[Saml2Attribute])
    """
    @property
    def Attributes(self) -> Collection:
        """ Get: Attributes(self: Saml2AttributeStatement) -> Collection[Saml2Attribute] """
        ...


    def __new__(cls, *__args:Saml2Attribute) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, attribute: Saml2Attribute)
        __new__(cls: type, attributes: IEnumerable[Saml2Attribute])
        """
        ...


class Saml2AudienceRestriction: # skipped bases: <type 'object'>, <type 'object'>
    """
    Saml2AudienceRestriction()
    Saml2AudienceRestriction(audience: Uri)
    Saml2AudienceRestriction(audiences: IEnumerable[Uri])
    """
    @property
    def Audiences(self) -> Collection:
        """ Get: Audiences(self: Saml2AudienceRestriction) -> Collection[Uri] """
        ...



class Saml2AuthenticationContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    Saml2AuthenticationContext()
    Saml2AuthenticationContext(classReference: Uri)
    Saml2AuthenticationContext(classReference: Uri, declarationReference: Uri)
    """
    @property
    def AuthenticatingAuthorities(self) -> Collection:
        """ Get: AuthenticatingAuthorities(self: Saml2AuthenticationContext) -> Collection[Uri] """
        ...

    @property
    def ClassReference(self) -> Uri:
        """
        Get: ClassReference(self: Saml2AuthenticationContext) -> Uri
        Set: ClassReference(self: Saml2AuthenticationContext) = value
        """
        ...

    @property
    def DeclarationReference(self) -> Uri:
        """
        Get: DeclarationReference(self: Saml2AuthenticationContext) -> Uri
        Set: DeclarationReference(self: Saml2AuthenticationContext) = value
        """
        ...



class Saml2AuthenticationStatement(Saml2Statement): # skipped bases: <type 'object'>
    """
    Saml2AuthenticationStatement(authenticationContext: Saml2AuthenticationContext)
    Saml2AuthenticationStatement(authenticationContext: Saml2AuthenticationContext, authenticationInstant: DateTime)
    """
    @property
    def AuthenticationContext(self) -> Saml2AuthenticationContext:
        """
        Get: AuthenticationContext(self: Saml2AuthenticationStatement) -> Saml2AuthenticationContext
        Set: AuthenticationContext(self: Saml2AuthenticationStatement) = value
        """
        ...

    @property
    def AuthenticationInstant(self) -> DateTime:
        """
        Get: AuthenticationInstant(self: Saml2AuthenticationStatement) -> DateTime
        Set: AuthenticationInstant(self: Saml2AuthenticationStatement) = value
        """
        ...

    @property
    def SessionIndex(self) -> str:
        """
        Get: SessionIndex(self: Saml2AuthenticationStatement) -> str
        Set: SessionIndex(self: Saml2AuthenticationStatement) = value
        """
        ...

    @property
    def SessionNotOnOrAfter(self) -> Nullable:
        """
        Get: SessionNotOnOrAfter(self: Saml2AuthenticationStatement) -> Nullable[DateTime]
        Set: SessionNotOnOrAfter(self: Saml2AuthenticationStatement) = value
        """
        ...

    @property
    def SubjectLocality(self) -> Saml2SubjectLocality:
        """
        Get: SubjectLocality(self: Saml2AuthenticationStatement) -> Saml2SubjectLocality
        Set: SubjectLocality(self: Saml2AuthenticationStatement) = value
        """
        ...


    def __new__(cls, authenticationContext:Saml2AuthenticationContext, authenticationInstant:DateTime = ...) -> Self:
        """
        __new__(cls: type, authenticationContext: Saml2AuthenticationContext)
        __new__(cls: type, authenticationContext: Saml2AuthenticationContext, authenticationInstant: DateTime)
        """
        ...


class Saml2AuthorizationDecisionStatement(Saml2Statement): # skipped bases: <type 'object'>
    """
    Saml2AuthorizationDecisionStatement(resource: Uri, decision: SamlAccessDecision)
    Saml2AuthorizationDecisionStatement(resource: Uri, decision: SamlAccessDecision, actions: IEnumerable[Saml2Action])
    """
    @property
    def Actions(self) -> Collection:
        """ Get: Actions(self: Saml2AuthorizationDecisionStatement) -> Collection[Saml2Action] """
        ...

    @property
    def Decision(self) -> SamlAccessDecision:
        """
        Get: Decision(self: Saml2AuthorizationDecisionStatement) -> SamlAccessDecision
        Set: Decision(self: Saml2AuthorizationDecisionStatement) = value
        """
        ...

    @property
    def Evidence(self) -> Saml2Evidence:
        """
        Get: Evidence(self: Saml2AuthorizationDecisionStatement) -> Saml2Evidence
        Set: Evidence(self: Saml2AuthorizationDecisionStatement) = value
        """
        ...

    @property
    def Resource(self) -> Uri:
        """
        Get: Resource(self: Saml2AuthorizationDecisionStatement) -> Uri
        Set: Resource(self: Saml2AuthorizationDecisionStatement) = value
        """
        ...


    def __new__(cls, resource:Uri, decision:SamlAccessDecision, actions:IEnumerable = ...) -> Self:
        """
        __new__(cls: type, resource: Uri, decision: SamlAccessDecision)
        __new__(cls: type, resource: Uri, decision: SamlAccessDecision, actions: IEnumerable[Saml2Action])
        """
        ...

    EmptyResource: Uri = ...


class Saml2Conditions: # skipped bases: <type 'object'>, <type 'object'>
    """ Saml2Conditions() """
    @property
    def AudienceRestrictions(self) -> Collection:
        """ Get: AudienceRestrictions(self: Saml2Conditions) -> Collection[Saml2AudienceRestriction] """
        ...

    @property
    def NotBefore(self) -> Nullable:
        """
        Get: NotBefore(self: Saml2Conditions) -> Nullable[DateTime]
        Set: NotBefore(self: Saml2Conditions) = value
        """
        ...

    @property
    def NotOnOrAfter(self) -> Nullable:
        """
        Get: NotOnOrAfter(self: Saml2Conditions) -> Nullable[DateTime]
        Set: NotOnOrAfter(self: Saml2Conditions) = value
        """
        ...

    @property
    def OneTimeUse(self) -> bool:
        """
        Get: OneTimeUse(self: Saml2Conditions) -> bool
        Set: OneTimeUse(self: Saml2Conditions) = value
        """
        ...

    @property
    def ProxyRestriction(self) -> Saml2ProxyRestriction:
        """
        Get: ProxyRestriction(self: Saml2Conditions) -> Saml2ProxyRestriction
        Set: ProxyRestriction(self: Saml2Conditions) = value
        """
        ...



class Saml2Evidence: # skipped bases: <type 'object'>, <type 'object'>
    """
    Saml2Evidence()
    Saml2Evidence(assertion: Saml2Assertion)
    Saml2Evidence(idReference: Saml2Id)
    Saml2Evidence(uriReference: Uri)
    """
    @property
    def AssertionIdReferences(self) -> Collection:
        """ Get: AssertionIdReferences(self: Saml2Evidence) -> Collection[Saml2Id] """
        ...

    @property
    def Assertions(self) -> Collection:
        """ Get: Assertions(self: Saml2Evidence) -> Collection[Saml2Assertion] """
        ...

    @property
    def AssertionUriReferences(self) -> Collection:
        """ Get: AssertionUriReferences(self: Saml2Evidence) -> Collection[Uri] """
        ...



class Saml2Id: # skipped bases: <type 'object'>, <type 'object'>
    """
    Saml2Id()
    Saml2Id(value: str)
    """
    @property
    def Value(self) -> str:
        """ Get: Value(self: Saml2Id) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Saml2Id, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Saml2Id) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Saml2Id) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Saml2NameIdentifier: # skipped bases: <type 'object'>, <type 'object'>
    """
    Saml2NameIdentifier(name: str)
    Saml2NameIdentifier(name: str, format: Uri)
    """
    @property
    def EncryptingCredentials(self) -> EncryptingCredentials:
        """
        Get: EncryptingCredentials(self: Saml2NameIdentifier) -> EncryptingCredentials
        Set: EncryptingCredentials(self: Saml2NameIdentifier) = value
        """
        ...

    @property
    def ExternalEncryptedKeys(self) -> Collection:
        """ Get: ExternalEncryptedKeys(self: Saml2NameIdentifier) -> Collection[EncryptedKeyIdentifierClause] """
        ...

    @property
    def Format(self) -> Uri:
        """
        Get: Format(self: Saml2NameIdentifier) -> Uri
        Set: Format(self: Saml2NameIdentifier) = value
        """
        ...

    @property
    def NameQualifier(self) -> str:
        """
        Get: NameQualifier(self: Saml2NameIdentifier) -> str
        Set: NameQualifier(self: Saml2NameIdentifier) = value
        """
        ...

    @property
    def SPNameQualifier(self) -> str:
        """
        Get: SPNameQualifier(self: Saml2NameIdentifier) -> str
        Set: SPNameQualifier(self: Saml2NameIdentifier) = value
        """
        ...

    @property
    def SPProvidedId(self) -> str:
        """
        Get: SPProvidedId(self: Saml2NameIdentifier) -> str
        Set: SPProvidedId(self: Saml2NameIdentifier) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: Saml2NameIdentifier) -> str
        Set: Value(self: Saml2NameIdentifier) = value
        """
        ...



class Saml2ProxyRestriction: # skipped bases: <type 'object'>, <type 'object'>
    """ Saml2ProxyRestriction() """
    @property
    def Audiences(self) -> Collection:
        """ Get: Audiences(self: Saml2ProxyRestriction) -> Collection[Uri] """
        ...

    @property
    def Count(self) -> Nullable:
        """
        Get: Count(self: Saml2ProxyRestriction) -> Nullable[int]
        Set: Count(self: Saml2ProxyRestriction) = value
        """
        ...



class Saml2SecurityKeyIdentifierClause(SecurityKeyIdentifierClause): # skipped bases: <type 'object'>
    """ Saml2SecurityKeyIdentifierClause(assertion: Saml2Assertion) """
    @property
    def Assertion(self) -> Saml2Assertion:
        """ Get: Assertion(self: Saml2SecurityKeyIdentifierClause) -> Saml2Assertion """
        ...



class Saml2SecurityToken(SecurityToken): # skipped bases: <type 'object'>
    """
    Saml2SecurityToken(assertion: Saml2Assertion)
    Saml2SecurityToken(assertion: Saml2Assertion, keys: ReadOnlyCollection[SecurityKey], issuerToken: SecurityToken)
    """
    @property
    def Assertion(self) -> Saml2Assertion:
        """ Get: Assertion(self: Saml2SecurityToken) -> Saml2Assertion """
        ...

    @property
    def IssuerToken(self) -> SecurityToken:
        """ Get: IssuerToken(self: Saml2SecurityToken) -> SecurityToken """
        ...


    def __new__(cls, assertion:Saml2Assertion, keys:ReadOnlyCollection = ..., issuerToken:SecurityToken = ...) -> Self:
        """
        __new__(cls: type, assertion: Saml2Assertion)
        __new__(cls: type, assertion: Saml2Assertion, keys: ReadOnlyCollection[SecurityKey], issuerToken: SecurityToken)
        """
        ...


class Saml2SecurityTokenHandler(SecurityTokenHandler): # skipped bases: <type 'ICustomIdentityConfiguration'>, <type 'object'>
    """
    Saml2SecurityTokenHandler()
    Saml2SecurityTokenHandler(samlSecurityTokenRequirement: SamlSecurityTokenRequirement)
    """
    @property
    def CertificateValidator(self) -> X509CertificateValidator:
        """
        Get: CertificateValidator(self: Saml2SecurityTokenHandler) -> X509CertificateValidator
        Set: CertificateValidator(self: Saml2SecurityTokenHandler) = value
        """
        ...

    @property
    def KeyInfoSerializer(self) -> SecurityTokenSerializer:
        """
        Get: KeyInfoSerializer(self: Saml2SecurityTokenHandler) -> SecurityTokenSerializer
        Set: KeyInfoSerializer(self: Saml2SecurityTokenHandler) = value
        """
        ...

    @property
    def SamlSecurityTokenRequirement(self) -> SamlSecurityTokenRequirement:
        """
        Get: SamlSecurityTokenRequirement(self: Saml2SecurityTokenHandler) -> SamlSecurityTokenRequirement
        Set: SamlSecurityTokenRequirement(self: Saml2SecurityTokenHandler) = value
        """
        ...


    def AddDelegateToAttributes(self, *args): #cannot find CLR method
        """ AddDelegateToAttributes(self: Saml2SecurityTokenHandler, subject: ClaimsIdentity, attributes: ICollection[Saml2Attribute], tokenDescriptor: SecurityTokenDescriptor) """
        ...

    def CollectAttributeValues(self, *args): #cannot find CLR method
        """ CollectAttributeValues(self: Saml2SecurityTokenHandler, attributes: ICollection[Saml2Attribute]) -> ICollection[Saml2Attribute] """
        ...

    def CreateAdvice(self, *args): #cannot find CLR method
        """ CreateAdvice(self: Saml2SecurityTokenHandler, tokenDescriptor: SecurityTokenDescriptor) -> Saml2Advice """
        ...

    def CreateAttribute(self, *args): #cannot find CLR method
        """ CreateAttribute(self: Saml2SecurityTokenHandler, claim: Claim, tokenDescriptor: SecurityTokenDescriptor) -> Saml2Attribute """
        ...

    def CreateAttributeStatement(self, *args): #cannot find CLR method
        """ CreateAttributeStatement(self: Saml2SecurityTokenHandler, subject: ClaimsIdentity, tokenDescriptor: SecurityTokenDescriptor) -> Saml2AttributeStatement """
        ...

    def CreateAuthenticationStatement(self, *args): #cannot find CLR method
        """ CreateAuthenticationStatement(self: Saml2SecurityTokenHandler, authInfo: AuthenticationInformation, tokenDescriptor: SecurityTokenDescriptor) -> Saml2AuthenticationStatement """
        ...

    def CreateClaims(self, *args): #cannot find CLR method
        """ CreateClaims(self: Saml2SecurityTokenHandler, samlToken: Saml2SecurityToken) -> ClaimsIdentity """
        ...

    def CreateConditions(self, *args): #cannot find CLR method
        """ CreateConditions(self: Saml2SecurityTokenHandler, tokenLifetime: Lifetime, relyingPartyAddress: str, tokenDescriptor: SecurityTokenDescriptor) -> Saml2Conditions """
        ...

    def CreateIssuerNameIdentifier(self, *args): #cannot find CLR method
        """ CreateIssuerNameIdentifier(self: Saml2SecurityTokenHandler, tokenDescriptor: SecurityTokenDescriptor) -> Saml2NameIdentifier """
        ...

    def CreateSamlSubject(self, *args): #cannot find CLR method
        """ CreateSamlSubject(self: Saml2SecurityTokenHandler, tokenDescriptor: SecurityTokenDescriptor) -> Saml2Subject """
        ...

    def CreateStatements(self, *args): #cannot find CLR method
        """ CreateStatements(self: Saml2SecurityTokenHandler, tokenDescriptor: SecurityTokenDescriptor) -> IEnumerable[Saml2Statement] """
        ...

    def CreateWindowsIdentity(self, *args): #cannot find CLR method
        """ CreateWindowsIdentity(self: Saml2SecurityTokenHandler, upn: str) -> WindowsIdentity """
        ...

    def CreateXmlStringFromAttributes(self, *args): #cannot find CLR method
        """ CreateXmlStringFromAttributes(self: Saml2SecurityTokenHandler, attributes: IEnumerable[Saml2Attribute]) -> str """
        ...

    def DenormalizeAuthenticationType(self, *args): #cannot find CLR method
        """ DenormalizeAuthenticationType(self: Saml2SecurityTokenHandler, normalizedAuthenticationType: str) -> str """
        ...

    def FindUpn(self, *args): #cannot find CLR method
        """ FindUpn(self: Saml2SecurityTokenHandler, claimsIdentity: ClaimsIdentity) -> str """
        ...

    def GetEncryptingCredentials(self, *args): #cannot find CLR method
        """ GetEncryptingCredentials(self: Saml2SecurityTokenHandler, tokenDescriptor: SecurityTokenDescriptor) -> EncryptingCredentials """
        ...

    def GetSigningCredentials(self, *args): #cannot find CLR method
        """ GetSigningCredentials(self: Saml2SecurityTokenHandler, tokenDescriptor: SecurityTokenDescriptor) -> SigningCredentials """
        ...

    def GetTokenReplayCacheEntryExpirationTime(self, *args): #cannot find CLR method
        """ GetTokenReplayCacheEntryExpirationTime(self: Saml2SecurityTokenHandler, token: Saml2SecurityToken) -> DateTime """
        ...

    def NormalizeAuthenticationContextClassReference(self, *args): #cannot find CLR method
        """ NormalizeAuthenticationContextClassReference(self: Saml2SecurityTokenHandler, saml2AuthenticationContextClassReference: str) -> str """
        ...

    def ProcessAttributeStatement(self, *args): #cannot find CLR method
        """ ProcessAttributeStatement(self: Saml2SecurityTokenHandler, statement: Saml2AttributeStatement, subject: ClaimsIdentity, issuer: str) """
        ...

    def ProcessAuthenticationStatement(self, *args): #cannot find CLR method
        """ ProcessAuthenticationStatement(self: Saml2SecurityTokenHandler, statement: Saml2AuthenticationStatement, subject: ClaimsIdentity, issuer: str) """
        ...

    def ProcessAuthorizationDecisionStatement(self, *args): #cannot find CLR method
        """ ProcessAuthorizationDecisionStatement(self: Saml2SecurityTokenHandler, statement: Saml2AuthorizationDecisionStatement, subject: ClaimsIdentity, issuer: str) """
        ...

    def ProcessSamlSubject(self, *args): #cannot find CLR method
        """ ProcessSamlSubject(self: Saml2SecurityTokenHandler, assertionSubject: Saml2Subject, subject: ClaimsIdentity, issuer: str) """
        ...

    def ProcessStatement(self, *args): #cannot find CLR method
        """ ProcessStatement(self: Saml2SecurityTokenHandler, statements: Collection[Saml2Statement], subject: ClaimsIdentity, issuer: str) """
        ...

    def ReadAction(self, *args): #cannot find CLR method
        """ ReadAction(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2Action """
        ...

    def ReadAdvice(self, *args): #cannot find CLR method
        """ ReadAdvice(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2Advice """
        ...

    def ReadAssertion(self, *args): #cannot find CLR method
        """ ReadAssertion(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2Assertion """
        ...

    def ReadAttribute(self, *args): #cannot find CLR method
        """ ReadAttribute(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2Attribute """
        ...

    def ReadAttributeStatement(self, *args): #cannot find CLR method
        """ ReadAttributeStatement(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2AttributeStatement """
        ...

    def ReadAttributeValue(self, *args): #cannot find CLR method
        """ ReadAttributeValue(self: Saml2SecurityTokenHandler, reader: XmlReader, attribute: Saml2Attribute) -> str """
        ...

    def ReadAudienceRestriction(self, *args): #cannot find CLR method
        """ ReadAudienceRestriction(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2AudienceRestriction """
        ...

    def ReadAuthenticationContext(self, *args): #cannot find CLR method
        """ ReadAuthenticationContext(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2AuthenticationContext """
        ...

    def ReadAuthenticationStatement(self, *args): #cannot find CLR method
        """ ReadAuthenticationStatement(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2AuthenticationStatement """
        ...

    def ReadAuthorizationDecisionStatement(self, *args): #cannot find CLR method
        """ ReadAuthorizationDecisionStatement(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2AuthorizationDecisionStatement """
        ...

    def ReadConditions(self, *args): #cannot find CLR method
        """ ReadConditions(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2Conditions """
        ...

    def ReadEncryptedId(self, *args): #cannot find CLR method
        """ ReadEncryptedId(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2NameIdentifier """
        ...

    def ReadEvidence(self, *args): #cannot find CLR method
        """ ReadEvidence(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2Evidence """
        ...

    def ReadIssuer(self, *args): #cannot find CLR method
        """ ReadIssuer(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2NameIdentifier """
        ...

    def ReadNameId(self, *args): #cannot find CLR method
        """ ReadNameId(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2NameIdentifier """
        ...

    def ReadNameIdType(self, *args): #cannot find CLR method
        """ ReadNameIdType(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2NameIdentifier """
        ...

    def ReadProxyRestriction(self, *args): #cannot find CLR method
        """ ReadProxyRestriction(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2ProxyRestriction """
        ...

    def ReadSigningKeyInfo(self, *args): #cannot find CLR method
        """ ReadSigningKeyInfo(self: Saml2SecurityTokenHandler, reader: XmlReader, assertion: Saml2Assertion) -> SecurityKeyIdentifier """
        ...

    def ReadStatement(self, *args): #cannot find CLR method
        """ ReadStatement(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2Statement """
        ...

    def ReadSubject(self, *args): #cannot find CLR method
        """ ReadSubject(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2Subject """
        ...

    def ReadSubjectConfirmation(self, *args): #cannot find CLR method
        """ ReadSubjectConfirmation(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2SubjectConfirmation """
        ...

    def ReadSubjectConfirmationData(self, *args): #cannot find CLR method
        """ ReadSubjectConfirmationData(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2SubjectConfirmationData """
        ...

    def ReadSubjectId(self, *args): #cannot find CLR method
        """ ReadSubjectId(self: Saml2SecurityTokenHandler, reader: XmlReader, parentElement: str) -> Saml2NameIdentifier """
        ...

    def ReadSubjectKeyInfo(self, *args): #cannot find CLR method
        """ ReadSubjectKeyInfo(self: Saml2SecurityTokenHandler, reader: XmlReader) -> SecurityKeyIdentifier """
        ...

    def ReadSubjectLocality(self, *args): #cannot find CLR method
        """ ReadSubjectLocality(self: Saml2SecurityTokenHandler, reader: XmlReader) -> Saml2SubjectLocality """
        ...

    def ResolveIssuerToken(self, *args): #cannot find CLR method
        """ ResolveIssuerToken(self: Saml2SecurityTokenHandler, assertion: Saml2Assertion, issuerResolver: SecurityTokenResolver) -> SecurityToken """
        ...

    def ResolveSecurityKeys(self, *args): #cannot find CLR method
        """ ResolveSecurityKeys(self: Saml2SecurityTokenHandler, assertion: Saml2Assertion, resolver: SecurityTokenResolver) -> ReadOnlyCollection[SecurityKey] """
        ...

    def SetDelegateFromAttribute(self, *args): #cannot find CLR method
        """ SetDelegateFromAttribute(self: Saml2SecurityTokenHandler, attribute: Saml2Attribute, subject: ClaimsIdentity, issuer: str) """
        ...

    def TryResolveIssuerToken(self, *args): #cannot find CLR method
        """ TryResolveIssuerToken(self: Saml2SecurityTokenHandler, assertion: Saml2Assertion, issuerResolver: SecurityTokenResolver) -> (bool, SecurityToken) """
        ...

    def ValidateConditions(self, *args): #cannot find CLR method
        """ ValidateConditions(self: Saml2SecurityTokenHandler, conditions: Saml2Conditions, enforceAudienceRestriction: bool) """
        ...

    def ValidateConfirmationData(self, *args): #cannot find CLR method
        """ ValidateConfirmationData(self: Saml2SecurityTokenHandler, confirmationData: Saml2SubjectConfirmationData) """
        ...

    def WriteAction(self, *args): #cannot find CLR method
        """ WriteAction(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2Action) """
        ...

    def WriteAdvice(self, *args): #cannot find CLR method
        """ WriteAdvice(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2Advice) """
        ...

    def WriteAssertion(self, *args): #cannot find CLR method
        """ WriteAssertion(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2Assertion) """
        ...

    def WriteAttribute(self, *args): #cannot find CLR method
        """ WriteAttribute(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2Attribute) """
        ...

    def WriteAttributeStatement(self, *args): #cannot find CLR method
        """ WriteAttributeStatement(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2AttributeStatement) """
        ...

    def WriteAttributeValue(self, *args): #cannot find CLR method
        """ WriteAttributeValue(self: Saml2SecurityTokenHandler, writer: XmlWriter, value: str, attribute: Saml2Attribute) """
        ...

    def WriteAudienceRestriction(self, *args): #cannot find CLR method
        """ WriteAudienceRestriction(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2AudienceRestriction) """
        ...

    def WriteAuthenticationContext(self, *args): #cannot find CLR method
        """ WriteAuthenticationContext(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2AuthenticationContext) """
        ...

    def WriteAuthenticationStatement(self, *args): #cannot find CLR method
        """ WriteAuthenticationStatement(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2AuthenticationStatement) """
        ...

    def WriteAuthorizationDecisionStatement(self, *args): #cannot find CLR method
        """ WriteAuthorizationDecisionStatement(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2AuthorizationDecisionStatement) """
        ...

    def WriteConditions(self, *args): #cannot find CLR method
        """ WriteConditions(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2Conditions) """
        ...

    def WriteEvidence(self, *args): #cannot find CLR method
        """ WriteEvidence(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2Evidence) """
        ...

    def WriteIssuer(self, *args): #cannot find CLR method
        """ WriteIssuer(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2NameIdentifier) """
        ...

    def WriteNameId(self, *args): #cannot find CLR method
        """ WriteNameId(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2NameIdentifier) """
        ...

    def WriteNameIdType(self, *args): #cannot find CLR method
        """ WriteNameIdType(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2NameIdentifier) """
        ...

    def WriteProxyRestriction(self, *args): #cannot find CLR method
        """ WriteProxyRestriction(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2ProxyRestriction) """
        ...

    def WriteSigningKeyInfo(self, *args): #cannot find CLR method
        """ WriteSigningKeyInfo(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: SecurityKeyIdentifier) """
        ...

    def WriteStatement(self, *args): #cannot find CLR method
        """ WriteStatement(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2Statement) """
        ...

    def WriteSubject(self, *args): #cannot find CLR method
        """ WriteSubject(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2Subject) """
        ...

    def WriteSubjectConfirmation(self, *args): #cannot find CLR method
        """ WriteSubjectConfirmation(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2SubjectConfirmation) """
        ...

    def WriteSubjectConfirmationData(self, *args): #cannot find CLR method
        """ WriteSubjectConfirmationData(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2SubjectConfirmationData) """
        ...

    def WriteSubjectKeyInfo(self, *args): #cannot find CLR method
        """ WriteSubjectKeyInfo(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: SecurityKeyIdentifier) """
        ...

    def WriteSubjectLocality(self, *args): #cannot find CLR method
        """ WriteSubjectLocality(self: Saml2SecurityTokenHandler, writer: XmlWriter, data: Saml2SubjectLocality) """
        ...

    def __new__(cls, samlSecurityTokenRequirement:SamlSecurityTokenRequirement = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, samlSecurityTokenRequirement: SamlSecurityTokenRequirement)
        """
        ...

    TokenProfile11ValueType: str = ...


class Saml2Subject: # skipped bases: <type 'object'>, <type 'object'>
    """
    Saml2Subject()
    Saml2Subject(nameId: Saml2NameIdentifier)
    Saml2Subject(subjectConfirmation: Saml2SubjectConfirmation)
    """
    @property
    def NameId(self) -> Saml2NameIdentifier:
        """
        Get: NameId(self: Saml2Subject) -> Saml2NameIdentifier
        Set: NameId(self: Saml2Subject) = value
        """
        ...

    @property
    def SubjectConfirmations(self) -> Collection:
        """ Get: SubjectConfirmations(self: Saml2Subject) -> Collection[Saml2SubjectConfirmation] """
        ...



class Saml2SubjectConfirmation: # skipped bases: <type 'object'>, <type 'object'>
    """
    Saml2SubjectConfirmation(method: Uri)
    Saml2SubjectConfirmation(method: Uri, data: Saml2SubjectConfirmationData)
    """
    @property
    def Method(self) -> Uri:
        """
        Get: Method(self: Saml2SubjectConfirmation) -> Uri
        Set: Method(self: Saml2SubjectConfirmation) = value
        """
        ...

    @property
    def NameIdentifier(self) -> Saml2NameIdentifier:
        """
        Get: NameIdentifier(self: Saml2SubjectConfirmation) -> Saml2NameIdentifier
        Set: NameIdentifier(self: Saml2SubjectConfirmation) = value
        """
        ...

    @property
    def SubjectConfirmationData(self) -> Saml2SubjectConfirmationData:
        """
        Get: SubjectConfirmationData(self: Saml2SubjectConfirmation) -> Saml2SubjectConfirmationData
        Set: SubjectConfirmationData(self: Saml2SubjectConfirmation) = value
        """
        ...



class Saml2SubjectConfirmationData: # skipped bases: <type 'object'>, <type 'object'>
    """ Saml2SubjectConfirmationData() """
    @property
    def Address(self) -> str:
        """
        Get: Address(self: Saml2SubjectConfirmationData) -> str
        Set: Address(self: Saml2SubjectConfirmationData) = value
        """
        ...

    @property
    def InResponseTo(self) -> Saml2Id:
        """
        Get: InResponseTo(self: Saml2SubjectConfirmationData) -> Saml2Id
        Set: InResponseTo(self: Saml2SubjectConfirmationData) = value
        """
        ...

    @property
    def KeyIdentifiers(self) -> Collection:
        """ Get: KeyIdentifiers(self: Saml2SubjectConfirmationData) -> Collection[SecurityKeyIdentifier] """
        ...

    @property
    def NotBefore(self) -> Nullable:
        """
        Get: NotBefore(self: Saml2SubjectConfirmationData) -> Nullable[DateTime]
        Set: NotBefore(self: Saml2SubjectConfirmationData) = value
        """
        ...

    @property
    def NotOnOrAfter(self) -> Nullable:
        """
        Get: NotOnOrAfter(self: Saml2SubjectConfirmationData) -> Nullable[DateTime]
        Set: NotOnOrAfter(self: Saml2SubjectConfirmationData) = value
        """
        ...

    @property
    def Recipient(self) -> Uri:
        """
        Get: Recipient(self: Saml2SubjectConfirmationData) -> Uri
        Set: Recipient(self: Saml2SubjectConfirmationData) = value
        """
        ...



class Saml2SubjectLocality: # skipped bases: <type 'object'>, <type 'object'>
    """
    Saml2SubjectLocality()
    Saml2SubjectLocality(address: str, dnsName: str)
    """
    @property
    def Address(self) -> str:
        """
        Get: Address(self: Saml2SubjectLocality) -> str
        Set: Address(self: Saml2SubjectLocality) = value
        """
        ...

    @property
    def DnsName(self) -> str:
        """
        Get: DnsName(self: Saml2SubjectLocality) -> str
        Set: DnsName(self: Saml2SubjectLocality) = value
        """
        ...



class SamlAccessDecision(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SamlAccessDecision, values: Deny (1), Indeterminate (2), Permit (0) """
    Deny: SamlAccessDecision = ...
    Indeterminate: SamlAccessDecision = ...
    Permit: SamlAccessDecision = ...
    value__ = ...


class SamlAction: # skipped bases: <type 'object'>, <type 'object'>
    """
    SamlAction(action: str)
    SamlAction(action: str, ns: str)
    SamlAction()
    """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: SamlAction) -> str
        Set: Action(self: SamlAction) = value
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: SamlAction) -> bool """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: SamlAction) -> str
        Set: Namespace(self: SamlAction) = value
        """
        ...


    def MakeReadOnly(self): # -> 
        """ MakeReadOnly(self: SamlAction) """
        ...

    def ReadXml(self, reader:XmlDictionaryReader, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver): # -> 
        """ ReadXml(self: SamlAction, reader: XmlDictionaryReader, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) """
        ...

    def WriteXml(self, writer:XmlDictionaryWriter, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer): # -> 
        """ WriteXml(self: SamlAction, writer: XmlDictionaryWriter, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer) """
        ...


class SamlAdvice: # skipped bases: <type 'object'>, <type 'object'>
    """
    SamlAdvice()
    SamlAdvice(references: IEnumerable[str])
    SamlAdvice(assertions: IEnumerable[SamlAssertion])
    SamlAdvice(references: IEnumerable[str], assertions: IEnumerable[SamlAssertion])
    """
    @property
    def AssertionIdReferences(self) -> IList:
        """ Get: AssertionIdReferences(self: SamlAdvice) -> IList[str] """
        ...

    @property
    def Assertions(self) -> IList:
        """ Get: Assertions(self: SamlAdvice) -> IList[SamlAssertion] """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: SamlAdvice) -> bool """
        ...


    def MakeReadOnly(self): # -> 
        """ MakeReadOnly(self: SamlAdvice) """
        ...

    def ReadXml(self, reader:XmlDictionaryReader, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver): # -> 
        """ ReadXml(self: SamlAdvice, reader: XmlDictionaryReader, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) """
        ...

    def WriteXml(self, writer:XmlDictionaryWriter, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer): # -> 
        """ WriteXml(self: SamlAdvice, writer: XmlDictionaryWriter, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer) """
        ...


class SamlAssertion(ICanonicalWriterEndRootElementCallback): # skipped bases: <type 'object'>
    """
    SamlAssertion()
    SamlAssertion(assertionId: str, issuer: str, issueInstant: DateTime, samlConditions: SamlConditions, samlAdvice: SamlAdvice, samlStatements: IEnumerable[SamlStatement])
    """
    @property
    def Advice(self) -> SamlAdvice:
        """
        Get: Advice(self: SamlAssertion) -> SamlAdvice
        Set: Advice(self: SamlAssertion) = value
        """
        ...

    @property
    def AssertionId(self) -> str:
        """
        Get: AssertionId(self: SamlAssertion) -> str
        Set: AssertionId(self: SamlAssertion) = value
        """
        ...

    @property
    def CanWriteSourceData(self) -> bool:
        """ Get: CanWriteSourceData(self: SamlAssertion) -> bool """
        ...

    @property
    def Conditions(self) -> SamlConditions:
        """
        Get: Conditions(self: SamlAssertion) -> SamlConditions
        Set: Conditions(self: SamlAssertion) = value
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: SamlAssertion) -> bool """
        ...

    @property
    def IssueInstant(self) -> DateTime:
        """
        Get: IssueInstant(self: SamlAssertion) -> DateTime
        Set: IssueInstant(self: SamlAssertion) = value
        """
        ...

    @property
    def Issuer(self) -> str:
        """
        Get: Issuer(self: SamlAssertion) -> str
        Set: Issuer(self: SamlAssertion) = value
        """
        ...

    @property
    def MajorVersion(self) -> int:
        """ Get: MajorVersion(self: SamlAssertion) -> int """
        ...

    @property
    def MinorVersion(self) -> int:
        """ Get: MinorVersion(self: SamlAssertion) -> int """
        ...

    @property
    def SigningCredentials(self) -> SigningCredentials:
        """
        Get: SigningCredentials(self: SamlAssertion) -> SigningCredentials
        Set: SigningCredentials(self: SamlAssertion) = value
        """
        ...

    @property
    def SigningToken(self) -> SecurityToken:
        """
        Get: SigningToken(self: SamlAssertion) -> SecurityToken
        Set: SigningToken(self: SamlAssertion) = value
        """
        ...

    @property
    def Statements(self) -> IList:
        """ Get: Statements(self: SamlAssertion) -> IList[SamlStatement] """
        ...


    def MakeReadOnly(self): # -> 
        """ MakeReadOnly(self: SamlAssertion) """
        ...

    def ReadSignature(self, *args): #cannot find CLR method
        """ ReadSignature(self: SamlAssertion, reader: XmlDictionaryReader, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver, samlSerializer: SamlSerializer) """
        ...

    def ReadXml(self, reader:XmlDictionaryReader, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver): # -> 
        """ ReadXml(self: SamlAssertion, reader: XmlDictionaryReader, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) """
        ...

    def WriteSourceData(self, writer:XmlWriter): # -> 
        """ WriteSourceData(self: SamlAssertion, writer: XmlWriter) """
        ...

    def WriteXml(self, writer:XmlDictionaryWriter, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer): # -> 
        """ WriteXml(self: SamlAssertion, writer: XmlDictionaryWriter, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer) """
        ...


class SamlAssertionKeyIdentifierClause(SecurityKeyIdentifierClause): # skipped bases: <type 'object'>
    """
    SamlAssertionKeyIdentifierClause(assertionId: str)
    SamlAssertionKeyIdentifierClause(assertionId: str, derivationNonce: Array[Byte], derivationLength: int)
    """
    @property
    def AssertionId(self) -> str:
        """ Get: AssertionId(self: SamlAssertionKeyIdentifierClause) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: SamlAssertionKeyIdentifierClause) -> str """
        ...


class SamlAttribute: # skipped bases: <type 'object'>, <type 'object'>
    """
    SamlAttribute()
    SamlAttribute(attributeNamespace: str, attributeName: str, attributeValues: IEnumerable[str])
    SamlAttribute(claim: Claim)
    """
    @property
    def AttributeValues(self) -> IList:
        """ Get: AttributeValues(self: SamlAttribute) -> IList[str] """
        ...

    @property
    def AttributeValueXsiType(self) -> str:
        """
        Get: AttributeValueXsiType(self: SamlAttribute) -> str
        Set: AttributeValueXsiType(self: SamlAttribute) = value
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: SamlAttribute) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: SamlAttribute) -> str
        Set: Name(self: SamlAttribute) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: SamlAttribute) -> str
        Set: Namespace(self: SamlAttribute) = value
        """
        ...

    @property
    def OriginalIssuer(self) -> str:
        """
        Get: OriginalIssuer(self: SamlAttribute) -> str
        Set: OriginalIssuer(self: SamlAttribute) = value
        """
        ...


    def ExtractClaims(self) -> ReadOnlyCollection:
        """ ExtractClaims(self: SamlAttribute) -> ReadOnlyCollection[Claim] """
        ...

    def MakeReadOnly(self): # -> 
        """ MakeReadOnly(self: SamlAttribute) """
        ...

    def ReadXml(self, reader:XmlDictionaryReader, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver): # -> 
        """ ReadXml(self: SamlAttribute, reader: XmlDictionaryReader, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) """
        ...

    def WriteXml(self, writer:XmlDictionaryWriter, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer): # -> 
        """ WriteXml(self: SamlAttribute, writer: XmlDictionaryWriter, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer) """
        ...


class SamlStatement: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: SamlStatement) -> bool """
        ...


    def CreatePolicy(self, issuer:ClaimSet, samlAuthenticator:SamlSecurityTokenAuthenticator) -> IAuthorizationPolicy:
        """ CreatePolicy(self: SamlStatement, issuer: ClaimSet, samlAuthenticator: SamlSecurityTokenAuthenticator) -> IAuthorizationPolicy """
        ...

    def MakeReadOnly(self): # -> 
        """ MakeReadOnly(self: SamlStatement) """
        ...

    def ReadXml(self, reader:XmlDictionaryReader, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver): # -> 
        """ ReadXml(self: SamlStatement, reader: XmlDictionaryReader, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) """
        ...

    def WriteXml(self, writer:XmlDictionaryWriter, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer): # -> 
        """ WriteXml(self: SamlStatement, writer: XmlDictionaryWriter, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer) """
        ...


class SamlSubjectStatement(SamlStatement): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SamlSubject(self) -> SamlSubject:
        """
        Get: SamlSubject(self: SamlSubjectStatement) -> SamlSubject
        Set: SamlSubject(self: SamlSubjectStatement) = value
        """
        ...


    def AddClaimsToList(self, *args): #cannot find CLR method
        """ AddClaimsToList(self: SamlSubjectStatement, claims: IList[Claim]) """
        ...

    def SetSubject(self, *args): #cannot find CLR method
        """ SetSubject(self: SamlSubjectStatement, samlSubject: SamlSubject) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, samlSubject: SamlSubject)
        """
        ...


class SamlAttributeStatement(SamlSubjectStatement): # skipped bases: <type 'object'>
    """
    SamlAttributeStatement()
    SamlAttributeStatement(samlSubject: SamlSubject, attributes: IEnumerable[SamlAttribute])
    """
    @property
    def Attributes(self) -> IList:
        """ Get: Attributes(self: SamlAttributeStatement) -> IList[SamlAttribute] """
        ...


    def ReadXml(self, reader:XmlDictionaryReader, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver): # -> 
        """ ReadXml(self: SamlAttributeStatement, reader: XmlDictionaryReader, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) """
        ...

    def WriteXml(self, writer:XmlDictionaryWriter, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer): # -> 
        """ WriteXml(self: SamlAttributeStatement, writer: XmlDictionaryWriter, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer) """
        ...


class SamlCondition: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: SamlCondition) -> bool """
        ...


    def MakeReadOnly(self): # -> 
        """ MakeReadOnly(self: SamlCondition) """
        ...

    def ReadXml(self, reader:XmlDictionaryReader, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver): # -> 
        """ ReadXml(self: SamlCondition, reader: XmlDictionaryReader, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) """
        ...

    def WriteXml(self, writer:XmlDictionaryWriter, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer): # -> 
        """ WriteXml(self: SamlCondition, writer: XmlDictionaryWriter, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer) """
        ...


class SamlAudienceRestrictionCondition(SamlCondition): # skipped bases: <type 'object'>
    """
    SamlAudienceRestrictionCondition(audiences: IEnumerable[Uri])
    SamlAudienceRestrictionCondition()
    """
    @property
    def Audiences(self) -> IList:
        """ Get: Audiences(self: SamlAudienceRestrictionCondition) -> IList[Uri] """
        ...


    def __new__(cls, audiences:IEnumerable = ...) -> Self:
        """
        __new__(cls: type, audiences: IEnumerable[Uri])
        __new__(cls: type)
        """
        ...


class SamlAuthenticationClaimResource: # skipped bases: <type 'object'>, <type 'object'>
    """
    SamlAuthenticationClaimResource(authenticationInstant: DateTime, authenticationMethod: str, dnsAddress: str, ipAddress: str)
    SamlAuthenticationClaimResource(authenticationInstant: DateTime, authenticationMethod: str, dnsAddress: str, ipAddress: str, authorityBindings: IEnumerable[SamlAuthorityBinding])
    SamlAuthenticationClaimResource(authenticationInstant: DateTime, authenticationMethod: str, dnsAddress: str, ipAddress: str, authorityBindings: ReadOnlyCollection[SamlAuthorityBinding])
    """
    @property
    def AuthenticationInstant(self) -> DateTime:
        """ Get: AuthenticationInstant(self: SamlAuthenticationClaimResource) -> DateTime """
        ...

    @property
    def AuthenticationMethod(self) -> str:
        """ Get: AuthenticationMethod(self: SamlAuthenticationClaimResource) -> str """
        ...

    @property
    def AuthorityBindings(self) -> ReadOnlyCollection:
        """ Get: AuthorityBindings(self: SamlAuthenticationClaimResource) -> ReadOnlyCollection[SamlAuthorityBinding] """
        ...

    @property
    def DnsAddress(self) -> str:
        """ Get: DnsAddress(self: SamlAuthenticationClaimResource) -> str """
        ...

    @property
    def IPAddress(self) -> str:
        """ Get: IPAddress(self: SamlAuthenticationClaimResource) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: SamlAuthenticationClaimResource, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SamlAuthenticationClaimResource) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SamlAuthenticationStatement(SamlSubjectStatement): # skipped bases: <type 'object'>
    """
    SamlAuthenticationStatement()
    SamlAuthenticationStatement(samlSubject: SamlSubject, authenticationMethod: str, authenticationInstant: DateTime, dnsAddress: str, ipAddress: str, authorityBindings: IEnumerable[SamlAuthorityBinding])
    """
    @property
    def AuthenticationInstant(self) -> DateTime:
        """
        Get: AuthenticationInstant(self: SamlAuthenticationStatement) -> DateTime
        Set: AuthenticationInstant(self: SamlAuthenticationStatement) = value
        """
        ...

    @property
    def AuthenticationMethod(self) -> str:
        """
        Get: AuthenticationMethod(self: SamlAuthenticationStatement) -> str
        Set: AuthenticationMethod(self: SamlAuthenticationStatement) = value
        """
        ...

    @property
    def AuthorityBindings(self) -> IList:
        """ Get: AuthorityBindings(self: SamlAuthenticationStatement) -> IList[SamlAuthorityBinding] """
        ...

    @property
    def ClaimType(self) -> str:
        """ Get: ClaimType() -> str """
        ...

    @property
    def DnsAddress(self) -> str:
        """
        Get: DnsAddress(self: SamlAuthenticationStatement) -> str
        Set: DnsAddress(self: SamlAuthenticationStatement) = value
        """
        ...

    @property
    def IPAddress(self) -> str:
        """
        Get: IPAddress(self: SamlAuthenticationStatement) -> str
        Set: IPAddress(self: SamlAuthenticationStatement) = value
        """
        ...


    def ReadXml(self, reader:XmlDictionaryReader, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver): # -> 
        """ ReadXml(self: SamlAuthenticationStatement, reader: XmlDictionaryReader, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) """
        ...

    def WriteXml(self, writer:XmlDictionaryWriter, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer): # -> 
        """ WriteXml(self: SamlAuthenticationStatement, writer: XmlDictionaryWriter, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer) """
        ...



class SamlAuthorityBinding: # skipped bases: <type 'object'>, <type 'object'>
    """
    SamlAuthorityBinding(authorityKind: XmlQualifiedName, binding: str, location: str)
    SamlAuthorityBinding()
    """
    @property
    def AuthorityKind(self) -> XmlQualifiedName:
        """
        Get: AuthorityKind(self: SamlAuthorityBinding) -> XmlQualifiedName
        Set: AuthorityKind(self: SamlAuthorityBinding) = value
        """
        ...

    @property
    def Binding(self) -> str:
        """
        Get: Binding(self: SamlAuthorityBinding) -> str
        Set: Binding(self: SamlAuthorityBinding) = value
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: SamlAuthorityBinding) -> bool """
        ...

    @property
    def Location(self) -> str:
        """
        Get: Location(self: SamlAuthorityBinding) -> str
        Set: Location(self: SamlAuthorityBinding) = value
        """
        ...


    def MakeReadOnly(self): # -> 
        """ MakeReadOnly(self: SamlAuthorityBinding) """
        ...

    def ReadXml(self, reader:XmlDictionaryReader, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver): # -> 
        """ ReadXml(self: SamlAuthorityBinding, reader: XmlDictionaryReader, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) """
        ...

    def WriteXml(self, writer:XmlDictionaryWriter, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer): # -> 
        """ WriteXml(self: SamlAuthorityBinding, writer: XmlDictionaryWriter, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer) """
        ...


class SamlAuthorizationDecisionClaimResource: # skipped bases: <type 'object'>, <type 'object'>
    """ SamlAuthorizationDecisionClaimResource(resource: str, accessDecision: SamlAccessDecision, actionNamespace: str, actionName: str) """
    @property
    def AccessDecision(self) -> SamlAccessDecision:
        """ Get: AccessDecision(self: SamlAuthorizationDecisionClaimResource) -> SamlAccessDecision """
        ...

    @property
    def ActionName(self) -> str:
        """ Get: ActionName(self: SamlAuthorizationDecisionClaimResource) -> str """
        ...

    @property
    def ActionNamespace(self) -> str:
        """ Get: ActionNamespace(self: SamlAuthorizationDecisionClaimResource) -> str """
        ...

    @property
    def Resource(self) -> str:
        """ Get: Resource(self: SamlAuthorizationDecisionClaimResource) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: SamlAuthorizationDecisionClaimResource, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SamlAuthorizationDecisionClaimResource) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SamlAuthorizationDecisionStatement(SamlSubjectStatement): # skipped bases: <type 'object'>
    """
    SamlAuthorizationDecisionStatement()
    SamlAuthorizationDecisionStatement(samlSubject: SamlSubject, resource: str, accessDecision: SamlAccessDecision, samlActions: IEnumerable[SamlAction])
    SamlAuthorizationDecisionStatement(samlSubject: SamlSubject, resource: str, accessDecision: SamlAccessDecision, samlActions: IEnumerable[SamlAction], samlEvidence: SamlEvidence)
    """
    @property
    def AccessDecision(self) -> SamlAccessDecision:
        """
        Get: AccessDecision(self: SamlAuthorizationDecisionStatement) -> SamlAccessDecision
        Set: AccessDecision(self: SamlAuthorizationDecisionStatement) = value
        """
        ...

    @property
    def ClaimType(self) -> str:
        """ Get: ClaimType() -> str """
        ...

    @property
    def Evidence(self) -> SamlEvidence:
        """
        Get: Evidence(self: SamlAuthorizationDecisionStatement) -> SamlEvidence
        Set: Evidence(self: SamlAuthorizationDecisionStatement) = value
        """
        ...

    @property
    def Resource(self) -> str:
        """
        Get: Resource(self: SamlAuthorizationDecisionStatement) -> str
        Set: Resource(self: SamlAuthorizationDecisionStatement) = value
        """
        ...

    @property
    def SamlActions(self) -> IList:
        """ Get: SamlActions(self: SamlAuthorizationDecisionStatement) -> IList[SamlAction] """
        ...


    def ReadXml(self, reader:XmlDictionaryReader, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver): # -> 
        """ ReadXml(self: SamlAuthorizationDecisionStatement, reader: XmlDictionaryReader, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) """
        ...

    def WriteXml(self, writer:XmlDictionaryWriter, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer): # -> 
        """ WriteXml(self: SamlAuthorizationDecisionStatement, writer: XmlDictionaryWriter, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer) """
        ...



class SamlConditions: # skipped bases: <type 'object'>, <type 'object'>
    """
    SamlConditions()
    SamlConditions(notBefore: DateTime, notOnOrAfter: DateTime)
    SamlConditions(notBefore: DateTime, notOnOrAfter: DateTime, conditions: IEnumerable[SamlCondition])
    """
    @property
    def Conditions(self) -> IList:
        """ Get: Conditions(self: SamlConditions) -> IList[SamlCondition] """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: SamlConditions) -> bool """
        ...

    @property
    def NotBefore(self) -> DateTime:
        """
        Get: NotBefore(self: SamlConditions) -> DateTime
        Set: NotBefore(self: SamlConditions) = value
        """
        ...

    @property
    def NotOnOrAfter(self) -> DateTime:
        """
        Get: NotOnOrAfter(self: SamlConditions) -> DateTime
        Set: NotOnOrAfter(self: SamlConditions) = value
        """
        ...


    def MakeReadOnly(self): # -> 
        """ MakeReadOnly(self: SamlConditions) """
        ...

    def ReadXml(self, reader:XmlDictionaryReader, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver): # -> 
        """ ReadXml(self: SamlConditions, reader: XmlDictionaryReader, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) """
        ...

    def WriteXml(self, writer:XmlDictionaryWriter, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer): # -> 
        """ WriteXml(self: SamlConditions, writer: XmlDictionaryWriter, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer) """
        ...


class SamlConstants: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def EmailName(self) -> str:
        """ Get: EmailName() -> str """
        ...

    @property
    def EmailNamespace(self) -> str:
        """ Get: EmailNamespace() -> str """
        ...

    @property
    def HolderOfKey(self) -> str:
        """ Get: HolderOfKey() -> str """
        ...

    @property
    def MajorVersionValue(self) -> int:
        """ Get: MajorVersionValue() -> int """
        ...

    @property
    def MinorVersionValue(self) -> int:
        """ Get: MinorVersionValue() -> int """
        ...

    @property
    def Namespace(self) -> str:
        """ Get: Namespace() -> str """
        ...

    @property
    def SenderVouches(self) -> str:
        """ Get: SenderVouches() -> str """
        ...

    @property
    def UserName(self) -> str:
        """ Get: UserName() -> str """
        ...

    @property
    def UserNameNamespace(self) -> str:
        """ Get: UserNameNamespace() -> str """
        ...


    Prefix: str = ...
    __all__: list = ...


class SamlDoNotCacheCondition(SamlCondition): # skipped bases: <type 'object'>
    """ SamlDoNotCacheCondition() """
    pass

class SamlEvidence: # skipped bases: <type 'object'>, <type 'object'>
    """
    SamlEvidence(assertionIdReferences: IEnumerable[str])
    SamlEvidence(assertions: IEnumerable[SamlAssertion])
    SamlEvidence(assertionIdReferences: IEnumerable[str], assertions: IEnumerable[SamlAssertion])
    SamlEvidence()
    """
    @property
    def AssertionIdReferences(self) -> IList:
        """ Get: AssertionIdReferences(self: SamlEvidence) -> IList[str] """
        ...

    @property
    def Assertions(self) -> IList:
        """ Get: Assertions(self: SamlEvidence) -> IList[SamlAssertion] """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: SamlEvidence) -> bool """
        ...


    def MakeReadOnly(self): # -> 
        """ MakeReadOnly(self: SamlEvidence) """
        ...

    def ReadXml(self, reader:XmlDictionaryReader, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver): # -> 
        """ ReadXml(self: SamlEvidence, reader: XmlDictionaryReader, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) """
        ...

    def WriteXml(self, writer:XmlDictionaryWriter, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer): # -> 
        """ WriteXml(self: SamlEvidence, writer: XmlDictionaryWriter, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer) """
        ...


class SamlNameIdentifierClaimResource: # skipped bases: <type 'object'>, <type 'object'>
    """ SamlNameIdentifierClaimResource(name: str, nameQualifier: str, format: str) """
    @property
    def Format(self) -> str:
        """ Get: Format(self: SamlNameIdentifierClaimResource) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: SamlNameIdentifierClaimResource) -> str """
        ...

    @property
    def NameQualifier(self) -> str:
        """ Get: NameQualifier(self: SamlNameIdentifierClaimResource) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: SamlNameIdentifierClaimResource, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SamlNameIdentifierClaimResource) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SamlSecurityKeyIdentifierClause(SecurityKeyIdentifierClause): # skipped bases: <type 'object'>
    """ SamlSecurityKeyIdentifierClause(assertion: SamlAssertion) """
    @property
    def Assertion(self) -> SamlAssertion:
        """ Get: Assertion(self: SamlSecurityKeyIdentifierClause) -> SamlAssertion """
        ...



class SamlSecurityToken(SecurityToken): # skipped bases: <type 'object'>
    """ SamlSecurityToken(assertion: SamlAssertion) """
    @property
    def Assertion(self) -> SamlAssertion:
        """ Get: Assertion(self: SamlSecurityToken) -> SamlAssertion """
        ...


    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: SamlSecurityToken, assertion: SamlAssertion) """
        ...

    def __new__(cls, assertion:SamlAssertion) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, assertion: SamlAssertion)
        """
        ...


class SamlSecurityTokenHandler(SecurityTokenHandler): # skipped bases: <type 'ICustomIdentityConfiguration'>, <type 'object'>
    """
    SamlSecurityTokenHandler()
    SamlSecurityTokenHandler(samlSecurityTokenRequirement: SamlSecurityTokenRequirement)
    """
    @property
    def CertificateValidator(self) -> X509CertificateValidator:
        """
        Get: CertificateValidator(self: SamlSecurityTokenHandler) -> X509CertificateValidator
        Set: CertificateValidator(self: SamlSecurityTokenHandler) = value
        """
        ...

    @property
    def KeyInfoSerializer(self) -> SecurityTokenSerializer:
        """
        Get: KeyInfoSerializer(self: SamlSecurityTokenHandler) -> SecurityTokenSerializer
        Set: KeyInfoSerializer(self: SamlSecurityTokenHandler) = value
        """
        ...

    @property
    def SamlSecurityTokenRequirement(self) -> SamlSecurityTokenRequirement:
        """
        Get: SamlSecurityTokenRequirement(self: SamlSecurityTokenHandler) -> SamlSecurityTokenRequirement
        Set: SamlSecurityTokenRequirement(self: SamlSecurityTokenHandler) = value
        """
        ...


    def AddDelegateToAttributes(self, *args): #cannot find CLR method
        """ AddDelegateToAttributes(self: SamlSecurityTokenHandler, subject: ClaimsIdentity, attributes: ICollection[SamlAttribute], tokenDescriptor: SecurityTokenDescriptor) """
        ...

    def CollectAttributeValues(self, *args): #cannot find CLR method
        """ CollectAttributeValues(self: SamlSecurityTokenHandler, attributes: ICollection[SamlAttribute]) -> ICollection[SamlAttribute] """
        ...

    def CreateAdvice(self, *args): #cannot find CLR method
        """ CreateAdvice(self: SamlSecurityTokenHandler, tokenDescriptor: SecurityTokenDescriptor) -> SamlAdvice """
        ...

    def CreateAssertion(self, *args): #cannot find CLR method
        """ CreateAssertion(self: SamlSecurityTokenHandler, issuer: str, conditions: SamlConditions, advice: SamlAdvice, statements: IEnumerable[SamlStatement]) -> SamlAssertion """
        ...

    def CreateAttribute(self, *args): #cannot find CLR method
        """ CreateAttribute(self: SamlSecurityTokenHandler, claim: Claim, tokenDescriptor: SecurityTokenDescriptor) -> SamlAttribute """
        ...

    def CreateAttributeStatement(self, *args): #cannot find CLR method
        """ CreateAttributeStatement(self: SamlSecurityTokenHandler, samlSubject: SamlSubject, subject: ClaimsIdentity, tokenDescriptor: SecurityTokenDescriptor) -> SamlAttributeStatement """
        ...

    def CreateAuthenticationStatement(self, *args): #cannot find CLR method
        """ CreateAuthenticationStatement(self: SamlSecurityTokenHandler, samlSubject: SamlSubject, authInfo: AuthenticationInformation, tokenDescriptor: SecurityTokenDescriptor) -> SamlAuthenticationStatement """
        ...

    def CreateClaims(self, *args): #cannot find CLR method
        """ CreateClaims(self: SamlSecurityTokenHandler, samlSecurityToken: SamlSecurityToken) -> ClaimsIdentity """
        ...

    def CreateConditions(self, *args): #cannot find CLR method
        """ CreateConditions(self: SamlSecurityTokenHandler, tokenLifetime: Lifetime, relyingPartyAddress: str, tokenDescriptor: SecurityTokenDescriptor) -> SamlConditions """
        ...

    def CreateSamlSubject(self, *args): #cannot find CLR method
        """ CreateSamlSubject(self: SamlSecurityTokenHandler, tokenDescriptor: SecurityTokenDescriptor) -> SamlSubject """
        ...

    def CreateStatements(self, *args): #cannot find CLR method
        """ CreateStatements(self: SamlSecurityTokenHandler, tokenDescriptor: SecurityTokenDescriptor) -> IEnumerable[SamlStatement] """
        ...

    def CreateWindowsIdentity(self, *args): #cannot find CLR method
        """ CreateWindowsIdentity(self: SamlSecurityTokenHandler, upn: str) -> WindowsIdentity """
        ...

    def CreateXmlStringFromAttributes(self, *args): #cannot find CLR method
        """ CreateXmlStringFromAttributes(self: SamlSecurityTokenHandler, attributes: IEnumerable[SamlAttribute]) -> str """
        ...

    def DenormalizeAuthenticationType(self, *args): #cannot find CLR method
        """ DenormalizeAuthenticationType(self: SamlSecurityTokenHandler, normalizedAuthenticationType: str) -> str """
        ...

    def FindUpn(self, *args): #cannot find CLR method
        """ FindUpn(self: SamlSecurityTokenHandler, claimsIdentity: ClaimsIdentity) -> str """
        ...

    def GetEncryptingCredentials(self, *args): #cannot find CLR method
        """ GetEncryptingCredentials(self: SamlSecurityTokenHandler, tokenDescriptor: SecurityTokenDescriptor) -> EncryptingCredentials """
        ...

    def GetSigningCredentials(self, *args): #cannot find CLR method
        """ GetSigningCredentials(self: SamlSecurityTokenHandler, tokenDescriptor: SecurityTokenDescriptor) -> SigningCredentials """
        ...

    def GetTokenReplayCacheEntryExpirationTime(self, *args): #cannot find CLR method
        """ GetTokenReplayCacheEntryExpirationTime(self: SamlSecurityTokenHandler, token: SamlSecurityToken) -> DateTime """
        ...

    def NormalizeAuthenticationType(self, *args): #cannot find CLR method
        """ NormalizeAuthenticationType(self: SamlSecurityTokenHandler, saml11AuthenticationMethod: str) -> str """
        ...

    def ProcessAttributeStatement(self, *args): #cannot find CLR method
        """ ProcessAttributeStatement(self: SamlSecurityTokenHandler, samlStatement: SamlAttributeStatement, subject: ClaimsIdentity, issuer: str) """
        ...

    def ProcessAuthenticationStatement(self, *args): #cannot find CLR method
        """ ProcessAuthenticationStatement(self: SamlSecurityTokenHandler, samlStatement: SamlAuthenticationStatement, subject: ClaimsIdentity, issuer: str) """
        ...

    def ProcessAuthorizationDecisionStatement(self, *args): #cannot find CLR method
        """ ProcessAuthorizationDecisionStatement(self: SamlSecurityTokenHandler, samlStatement: SamlAuthorizationDecisionStatement, subject: ClaimsIdentity, issuer: str) """
        ...

    def ProcessSamlSubject(self, *args): #cannot find CLR method
        """ ProcessSamlSubject(self: SamlSecurityTokenHandler, samlSubject: SamlSubject, subject: ClaimsIdentity, issuer: str) """
        ...

    def ProcessStatement(self, *args): #cannot find CLR method
        """ ProcessStatement(self: SamlSecurityTokenHandler, statements: IList[SamlStatement], subject: ClaimsIdentity, issuer: str) """
        ...

    def ReadAction(self, *args): #cannot find CLR method
        """ ReadAction(self: SamlSecurityTokenHandler, reader: XmlReader) -> SamlAction """
        ...

    def ReadAdvice(self, *args): #cannot find CLR method
        """ ReadAdvice(self: SamlSecurityTokenHandler, reader: XmlReader) -> SamlAdvice """
        ...

    def ReadAssertion(self, *args): #cannot find CLR method
        """ ReadAssertion(self: SamlSecurityTokenHandler, reader: XmlReader) -> SamlAssertion """
        ...

    def ReadAttribute(self, *args): #cannot find CLR method
        """ ReadAttribute(self: SamlSecurityTokenHandler, reader: XmlReader) -> SamlAttribute """
        ...

    def ReadAttributeStatement(self, *args): #cannot find CLR method
        """ ReadAttributeStatement(self: SamlSecurityTokenHandler, reader: XmlReader) -> SamlAttributeStatement """
        ...

    def ReadAttributeValue(self, *args): #cannot find CLR method
        """ ReadAttributeValue(self: SamlSecurityTokenHandler, reader: XmlReader, attribute: SamlAttribute) -> str """
        ...

    def ReadAudienceRestrictionCondition(self, *args): #cannot find CLR method
        """ ReadAudienceRestrictionCondition(self: SamlSecurityTokenHandler, reader: XmlReader) -> SamlAudienceRestrictionCondition """
        ...

    def ReadAuthenticationStatement(self, *args): #cannot find CLR method
        """ ReadAuthenticationStatement(self: SamlSecurityTokenHandler, reader: XmlReader) -> SamlAuthenticationStatement """
        ...

    def ReadAuthorityBinding(self, *args): #cannot find CLR method
        """ ReadAuthorityBinding(self: SamlSecurityTokenHandler, reader: XmlReader) -> SamlAuthorityBinding """
        ...

    def ReadAuthorizationDecisionStatement(self, *args): #cannot find CLR method
        """ ReadAuthorizationDecisionStatement(self: SamlSecurityTokenHandler, reader: XmlReader) -> SamlAuthorizationDecisionStatement """
        ...

    def ReadCondition(self, *args): #cannot find CLR method
        """ ReadCondition(self: SamlSecurityTokenHandler, reader: XmlReader) -> SamlCondition """
        ...

    def ReadConditions(self, *args): #cannot find CLR method
        """ ReadConditions(self: SamlSecurityTokenHandler, reader: XmlReader) -> SamlConditions """
        ...

    def ReadDoNotCacheCondition(self, *args): #cannot find CLR method
        """ ReadDoNotCacheCondition(self: SamlSecurityTokenHandler, reader: XmlReader) -> SamlDoNotCacheCondition """
        ...

    def ReadEvidence(self, *args): #cannot find CLR method
        """ ReadEvidence(self: SamlSecurityTokenHandler, reader: XmlReader) -> SamlEvidence """
        ...

    def ReadSigningKeyInfo(self, *args): #cannot find CLR method
        """ ReadSigningKeyInfo(self: SamlSecurityTokenHandler, reader: XmlReader, assertion: SamlAssertion) -> SecurityKeyIdentifier """
        ...

    def ReadStatement(self, *args): #cannot find CLR method
        """ ReadStatement(self: SamlSecurityTokenHandler, reader: XmlReader) -> SamlStatement """
        ...

    def ReadSubject(self, *args): #cannot find CLR method
        """ ReadSubject(self: SamlSecurityTokenHandler, reader: XmlReader) -> SamlSubject """
        ...

    def ReadSubjectKeyInfo(self, *args): #cannot find CLR method
        """ ReadSubjectKeyInfo(self: SamlSecurityTokenHandler, reader: XmlReader) -> SecurityKeyIdentifier """
        ...

    def ResolveIssuerToken(self, *args): #cannot find CLR method
        """ ResolveIssuerToken(self: SamlSecurityTokenHandler, assertion: SamlAssertion, issuerResolver: SecurityTokenResolver) -> SecurityToken """
        ...

    def ResolveSubjectKeyIdentifier(self, *args): #cannot find CLR method
        """ ResolveSubjectKeyIdentifier(self: SamlSecurityTokenHandler, subjectKeyIdentifier: SecurityKeyIdentifier) -> SecurityKey """
        ...

    def SetDelegateFromAttribute(self, *args): #cannot find CLR method
        """ SetDelegateFromAttribute(self: SamlSecurityTokenHandler, attribute: SamlAttribute, subject: ClaimsIdentity, issuer: str) """
        ...

    def TryResolveIssuerToken(self, *args): #cannot find CLR method
        """ TryResolveIssuerToken(self: SamlSecurityTokenHandler, assertion: SamlAssertion, issuerResolver: SecurityTokenResolver) -> (bool, SecurityToken) """
        ...

    def ValidateConditions(self, *args): #cannot find CLR method
        """ ValidateConditions(self: SamlSecurityTokenHandler, conditions: SamlConditions, enforceAudienceRestriction: bool) """
        ...

    def WriteAction(self, *args): #cannot find CLR method
        """ WriteAction(self: SamlSecurityTokenHandler, writer: XmlWriter, action: SamlAction) """
        ...

    def WriteAdvice(self, *args): #cannot find CLR method
        """ WriteAdvice(self: SamlSecurityTokenHandler, writer: XmlWriter, advice: SamlAdvice) """
        ...

    def WriteAssertion(self, *args): #cannot find CLR method
        """ WriteAssertion(self: SamlSecurityTokenHandler, writer: XmlWriter, assertion: SamlAssertion) """
        ...

    def WriteAttribute(self, *args): #cannot find CLR method
        """ WriteAttribute(self: SamlSecurityTokenHandler, writer: XmlWriter, attribute: SamlAttribute) """
        ...

    def WriteAttributeStatement(self, *args): #cannot find CLR method
        """ WriteAttributeStatement(self: SamlSecurityTokenHandler, writer: XmlWriter, statement: SamlAttributeStatement) """
        ...

    def WriteAttributeValue(self, *args): #cannot find CLR method
        """ WriteAttributeValue(self: SamlSecurityTokenHandler, writer: XmlWriter, value: str, attribute: SamlAttribute) """
        ...

    def WriteAudienceRestrictionCondition(self, *args): #cannot find CLR method
        """ WriteAudienceRestrictionCondition(self: SamlSecurityTokenHandler, writer: XmlWriter, condition: SamlAudienceRestrictionCondition) """
        ...

    def WriteAuthenticationStatement(self, *args): #cannot find CLR method
        """ WriteAuthenticationStatement(self: SamlSecurityTokenHandler, writer: XmlWriter, statement: SamlAuthenticationStatement) """
        ...

    def WriteAuthorityBinding(self, *args): #cannot find CLR method
        """ WriteAuthorityBinding(self: SamlSecurityTokenHandler, writer: XmlWriter, authorityBinding: SamlAuthorityBinding) """
        ...

    def WriteAuthorizationDecisionStatement(self, *args): #cannot find CLR method
        """ WriteAuthorizationDecisionStatement(self: SamlSecurityTokenHandler, writer: XmlWriter, statement: SamlAuthorizationDecisionStatement) """
        ...

    def WriteCondition(self, *args): #cannot find CLR method
        """ WriteCondition(self: SamlSecurityTokenHandler, writer: XmlWriter, condition: SamlCondition) """
        ...

    def WriteConditions(self, *args): #cannot find CLR method
        """ WriteConditions(self: SamlSecurityTokenHandler, writer: XmlWriter, conditions: SamlConditions) """
        ...

    def WriteDoNotCacheCondition(self, *args): #cannot find CLR method
        """ WriteDoNotCacheCondition(self: SamlSecurityTokenHandler, writer: XmlWriter, condition: SamlDoNotCacheCondition) """
        ...

    def WriteEvidence(self, *args): #cannot find CLR method
        """ WriteEvidence(self: SamlSecurityTokenHandler, writer: XmlWriter, evidence: SamlEvidence) """
        ...

    def WriteSigningKeyInfo(self, *args): #cannot find CLR method
        """ WriteSigningKeyInfo(self: SamlSecurityTokenHandler, writer: XmlWriter, signingKeyIdentifier: SecurityKeyIdentifier) """
        ...

    def WriteStatement(self, *args): #cannot find CLR method
        """ WriteStatement(self: SamlSecurityTokenHandler, writer: XmlWriter, statement: SamlStatement) """
        ...

    def WriteSubject(self, *args): #cannot find CLR method
        """ WriteSubject(self: SamlSecurityTokenHandler, writer: XmlWriter, subject: SamlSubject) """
        ...

    def WriteSubjectKeyInfo(self, *args): #cannot find CLR method
        """ WriteSubjectKeyInfo(self: SamlSecurityTokenHandler, writer: XmlWriter, subjectSki: SecurityKeyIdentifier) """
        ...

    def __new__(cls, samlSecurityTokenRequirement:SamlSecurityTokenRequirement = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, samlSecurityTokenRequirement: SamlSecurityTokenRequirement)
        """
        ...

    Assertion: str = ...
    BearerConfirmationMethod: str = ...
    Namespace: str = ...
    UnspecifiedAuthenticationMethod: str = ...


class SamlSecurityTokenRequirement: # skipped bases: <type 'object'>, <type 'object'>
    """
    SamlSecurityTokenRequirement()
    SamlSecurityTokenRequirement(element: XmlElement)
    """
    @property
    def CertificateValidator(self) -> X509CertificateValidator:
        """
        Get: CertificateValidator(self: SamlSecurityTokenRequirement) -> X509CertificateValidator
        Set: CertificateValidator(self: SamlSecurityTokenRequirement) = value
        """
        ...

    @property
    def MapToWindows(self) -> bool:
        """
        Get: MapToWindows(self: SamlSecurityTokenRequirement) -> bool
        Set: MapToWindows(self: SamlSecurityTokenRequirement) = value
        """
        ...

    @property
    def NameClaimType(self) -> str:
        """
        Get: NameClaimType(self: SamlSecurityTokenRequirement) -> str
        Set: NameClaimType(self: SamlSecurityTokenRequirement) = value
        """
        ...

    @property
    def RoleClaimType(self) -> str:
        """
        Get: RoleClaimType(self: SamlSecurityTokenRequirement) -> str
        Set: RoleClaimType(self: SamlSecurityTokenRequirement) = value
        """
        ...


    def ShouldEnforceAudienceRestriction(self, audienceUriMode:AudienceUriMode, token:SecurityToken) -> bool:
        """ ShouldEnforceAudienceRestriction(self: SamlSecurityTokenRequirement, audienceUriMode: AudienceUriMode, token: SecurityToken) -> bool """
        ...

    def ValidateAudienceRestriction(self, allowedAudienceUris:IList, tokenAudiences:IList): # -> 
        """ ValidateAudienceRestriction(self: SamlSecurityTokenRequirement, allowedAudienceUris: IList[Uri], tokenAudiences: IList[Uri]) """
        ...


class SamlSerializer: # skipped bases: <type 'object'>, <type 'object'>
    """ SamlSerializer() """
    def LoadAdvice(self, reader:XmlDictionaryReader, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver) -> SamlAdvice:
        """ LoadAdvice(self: SamlSerializer, reader: XmlDictionaryReader, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) -> SamlAdvice """
        ...

    def LoadAssertion(self, reader:XmlDictionaryReader, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver) -> SamlAssertion:
        """ LoadAssertion(self: SamlSerializer, reader: XmlDictionaryReader, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) -> SamlAssertion """
        ...

    def LoadAttribute(self, reader:XmlDictionaryReader, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver) -> SamlAttribute:
        """ LoadAttribute(self: SamlSerializer, reader: XmlDictionaryReader, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) -> SamlAttribute """
        ...

    def LoadCondition(self, reader:XmlDictionaryReader, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver) -> SamlCondition:
        """ LoadCondition(self: SamlSerializer, reader: XmlDictionaryReader, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) -> SamlCondition """
        ...

    def LoadConditions(self, reader:XmlDictionaryReader, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver) -> SamlConditions:
        """ LoadConditions(self: SamlSerializer, reader: XmlDictionaryReader, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) -> SamlConditions """
        ...

    def LoadStatement(self, reader:XmlDictionaryReader, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver) -> SamlStatement:
        """ LoadStatement(self: SamlSerializer, reader: XmlDictionaryReader, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) -> SamlStatement """
        ...

    def PopulateDictionary(self, dictionary:IXmlDictionary): # -> 
        """ PopulateDictionary(self: SamlSerializer, dictionary: IXmlDictionary) """
        ...

    def ReadToken(self, reader:XmlReader, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver) -> SamlSecurityToken:
        """ ReadToken(self: SamlSerializer, reader: XmlReader, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) -> SamlSecurityToken """
        ...

    def WriteToken(self, token:SamlSecurityToken, writer:XmlWriter, keyInfoSerializer:SecurityTokenSerializer): # -> 
        """ WriteToken(self: SamlSerializer, token: SamlSecurityToken, writer: XmlWriter, keyInfoSerializer: SecurityTokenSerializer) """
        ...


class SamlSubject: # skipped bases: <type 'object'>, <type 'object'>
    """
    SamlSubject()
    SamlSubject(nameFormat: str, nameQualifier: str, name: str)
    SamlSubject(nameFormat: str, nameQualifier: str, name: str, confirmations: IEnumerable[str], confirmationData: str, securityKeyIdentifier: SecurityKeyIdentifier)
    """
    @property
    def ConfirmationMethods(self) -> IList:
        """ Get: ConfirmationMethods(self: SamlSubject) -> IList[str] """
        ...

    @property
    def Crypto(self) -> SecurityKey:
        """
        Get: Crypto(self: SamlSubject) -> SecurityKey
        Set: Crypto(self: SamlSubject) = value
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: SamlSubject) -> bool """
        ...

    @property
    def KeyIdentifier(self) -> SecurityKeyIdentifier:
        """
        Get: KeyIdentifier(self: SamlSubject) -> SecurityKeyIdentifier
        Set: KeyIdentifier(self: SamlSubject) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: SamlSubject) -> str
        Set: Name(self: SamlSubject) = value
        """
        ...

    @property
    def NameClaimType(self) -> str:
        """ Get: NameClaimType() -> str """
        ...

    @property
    def NameFormat(self) -> str:
        """
        Get: NameFormat(self: SamlSubject) -> str
        Set: NameFormat(self: SamlSubject) = value
        """
        ...

    @property
    def NameQualifier(self) -> str:
        """
        Get: NameQualifier(self: SamlSubject) -> str
        Set: NameQualifier(self: SamlSubject) = value
        """
        ...

    @property
    def SubjectConfirmationData(self) -> str:
        """
        Get: SubjectConfirmationData(self: SamlSubject) -> str
        Set: SubjectConfirmationData(self: SamlSubject) = value
        """
        ...


    def ExtractClaims(self) -> ReadOnlyCollection:
        """ ExtractClaims(self: SamlSubject) -> ReadOnlyCollection[Claim] """
        ...

    def ExtractSubjectKeyClaimSet(self, samlAuthenticator:SamlSecurityTokenAuthenticator) -> ClaimSet:
        """ ExtractSubjectKeyClaimSet(self: SamlSubject, samlAuthenticator: SamlSecurityTokenAuthenticator) -> ClaimSet """
        ...

    def MakeReadOnly(self): # -> 
        """ MakeReadOnly(self: SamlSubject) """
        ...

    def ReadXml(self, reader:XmlDictionaryReader, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer, outOfBandTokenResolver:SecurityTokenResolver): # -> 
        """ ReadXml(self: SamlSubject, reader: XmlDictionaryReader, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer, outOfBandTokenResolver: SecurityTokenResolver) """
        ...

    def WriteXml(self, writer:XmlDictionaryWriter, samlSerializer:SamlSerializer, keyInfoSerializer:SecurityTokenSerializer): # -> 
        """ WriteXml(self: SamlSubject, writer: XmlDictionaryWriter, samlSerializer: SamlSerializer, keyInfoSerializer: SecurityTokenSerializer) """
        ...



class SecurityAlgorithms: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Aes128Encryption: str = ...
    Aes128KeyWrap: str = ...
    Aes192Encryption: str = ...
    Aes192KeyWrap: str = ...
    Aes256Encryption: str = ...
    Aes256KeyWrap: str = ...
    DesEncryption: str = ...
    DsaSha1Signature: str = ...
    ExclusiveC14n: str = ...
    ExclusiveC14nWithComments: str = ...
    HmacSha1Signature: str = ...
    HmacSha256Signature: str = ...
    Psha1KeyDerivation: str = ...
    Psha1KeyDerivationDec2005: str = ...
    Ripemd160Digest: str = ...
    RsaOaepKeyWrap: str = ...
    RsaSha1Signature: str = ...
    RsaSha256Signature: str = ...
    RsaV15KeyWrap: str = ...
    Sha1Digest: str = ...
    Sha256Digest: str = ...
    Sha512Digest: str = ...
    StrTransform: str = ...
    TlsSspiKeyWrap: str = ...
    TripleDesEncryption: str = ...
    TripleDesKeyWrap: str = ...
    WindowsSspiKeyWrap: str = ...
    __all__: list = ...


class SecurityKeyElement(SecurityKey): # skipped bases: <type 'object'>
    """
    SecurityKeyElement(securityKeyIdentifierClause: SecurityKeyIdentifierClause, securityTokenResolver: SecurityTokenResolver)
    SecurityKeyElement(securityKeyIdentifier: SecurityKeyIdentifier, securityTokenResolver: SecurityTokenResolver)
    """
    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, securityKeyIdentifierClause: SecurityKeyIdentifierClause, securityTokenResolver: SecurityTokenResolver)
        __new__(cls: type, securityKeyIdentifier: SecurityKeyIdentifier, securityTokenResolver: SecurityTokenResolver)
        """
        ...


class SecurityKeyIdentifier(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """
    SecurityKeyIdentifier()
    SecurityKeyIdentifier(*clauses: Array[SecurityKeyIdentifierClause])
    """
    @property
    def CanCreateKey(self) -> bool:
        """ Get: CanCreateKey(self: SecurityKeyIdentifier) -> bool """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: SecurityKeyIdentifier) -> int """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: SecurityKeyIdentifier) -> bool """
        ...


    def Add(self, clause:SecurityKeyIdentifierClause): # -> 
        """ Add(self: SecurityKeyIdentifier, clause: SecurityKeyIdentifierClause) """
        ...

    def CreateKey(self) -> SecurityKey:
        """ CreateKey(self: SecurityKeyIdentifier) -> SecurityKey """
        ...

    def Find(self): # -> TClause
        """ Find[TClause](self: SecurityKeyIdentifier) -> TClause """
        ...

    def MakeReadOnly(self): # -> 
        """ MakeReadOnly(self: SecurityKeyIdentifier) """
        ...

    def ToString(self) -> str:
        """ ToString(self: SecurityKeyIdentifier) -> str """
        ...

    def TryFind(self, clause): # -> Tuple_[bool, TClause]
        """ TryFind[TClause](self: SecurityKeyIdentifier) -> (bool, TClause) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SecurityKeyIdentifierClause](enumerable: IEnumerable[SecurityKeyIdentifierClause], value: SecurityKeyIdentifierClause) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class SecurityKeyIdentifierClauseSerializer: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CanReadKeyIdentifierClause(self, reader:XmlReader) -> bool:
        """ CanReadKeyIdentifierClause(self: SecurityKeyIdentifierClauseSerializer, reader: XmlReader) -> bool """
        ...

    def CanWriteKeyIdentifierClause(self, securityKeyIdentifierClause:SecurityKeyIdentifierClause) -> bool:
        """ CanWriteKeyIdentifierClause(self: SecurityKeyIdentifierClauseSerializer, securityKeyIdentifierClause: SecurityKeyIdentifierClause) -> bool """
        ...

    def ReadKeyIdentifierClause(self, reader:XmlReader) -> SecurityKeyIdentifierClause:
        """ ReadKeyIdentifierClause(self: SecurityKeyIdentifierClauseSerializer, reader: XmlReader) -> SecurityKeyIdentifierClause """
        ...

    def WriteKeyIdentifierClause(self, writer:XmlWriter, securityKeyIdentifierClause:SecurityKeyIdentifierClause): # -> 
        """ WriteKeyIdentifierClause(self: SecurityKeyIdentifierClauseSerializer, writer: XmlWriter, securityKeyIdentifierClause: SecurityKeyIdentifierClause) """
        ...


class SecurityKeyType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SecurityKeyType, values: AsymmetricKey (1), BearerKey (2), SymmetricKey (0) """
    AsymmetricKey: SecurityKeyType = ...
    BearerKey: SecurityKeyType = ...
    SymmetricKey: SecurityKeyType = ...
    value__ = ...


class SecurityKeyUsage(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SecurityKeyUsage, values: Exchange (0), Signature (1) """
    Exchange: SecurityKeyUsage = ...
    Signature: SecurityKeyUsage = ...
    value__ = ...


class SecurityTokenDescriptor: # skipped bases: <type 'object'>, <type 'object'>
    """ SecurityTokenDescriptor() """
    @property
    def AppliesToAddress(self) -> str:
        """
        Get: AppliesToAddress(self: SecurityTokenDescriptor) -> str
        Set: AppliesToAddress(self: SecurityTokenDescriptor) = value
        """
        ...

    @property
    def AttachedReference(self) -> SecurityKeyIdentifierClause:
        """
        Get: AttachedReference(self: SecurityTokenDescriptor) -> SecurityKeyIdentifierClause
        Set: AttachedReference(self: SecurityTokenDescriptor) = value
        """
        ...

    @property
    def AuthenticationInfo(self) -> AuthenticationInformation:
        """
        Get: AuthenticationInfo(self: SecurityTokenDescriptor) -> AuthenticationInformation
        Set: AuthenticationInfo(self: SecurityTokenDescriptor) = value
        """
        ...

    @property
    def EncryptingCredentials(self) -> EncryptingCredentials:
        """
        Get: EncryptingCredentials(self: SecurityTokenDescriptor) -> EncryptingCredentials
        Set: EncryptingCredentials(self: SecurityTokenDescriptor) = value
        """
        ...

    @property
    def Lifetime(self) -> Lifetime:
        """
        Get: Lifetime(self: SecurityTokenDescriptor) -> Lifetime
        Set: Lifetime(self: SecurityTokenDescriptor) = value
        """
        ...

    @property
    def Proof(self) -> ProofDescriptor:
        """
        Get: Proof(self: SecurityTokenDescriptor) -> ProofDescriptor
        Set: Proof(self: SecurityTokenDescriptor) = value
        """
        ...

    @property
    def Properties(self) -> Dictionary:
        """ Get: Properties(self: SecurityTokenDescriptor) -> Dictionary[str, object] """
        ...

    @property
    def ReplyToAddress(self) -> str:
        """
        Get: ReplyToAddress(self: SecurityTokenDescriptor) -> str
        Set: ReplyToAddress(self: SecurityTokenDescriptor) = value
        """
        ...

    @property
    def SigningCredentials(self) -> SigningCredentials:
        """
        Get: SigningCredentials(self: SecurityTokenDescriptor) -> SigningCredentials
        Set: SigningCredentials(self: SecurityTokenDescriptor) = value
        """
        ...

    @property
    def Subject(self) -> ClaimsIdentity:
        """
        Get: Subject(self: SecurityTokenDescriptor) -> ClaimsIdentity
        Set: Subject(self: SecurityTokenDescriptor) = value
        """
        ...

    @property
    def Token(self) -> SecurityToken:
        """
        Get: Token(self: SecurityTokenDescriptor) -> SecurityToken
        Set: Token(self: SecurityTokenDescriptor) = value
        """
        ...

    @property
    def TokenIssuerName(self) -> str:
        """
        Get: TokenIssuerName(self: SecurityTokenDescriptor) -> str
        Set: TokenIssuerName(self: SecurityTokenDescriptor) = value
        """
        ...

    @property
    def TokenType(self) -> str:
        """
        Get: TokenType(self: SecurityTokenDescriptor) -> str
        Set: TokenType(self: SecurityTokenDescriptor) = value
        """
        ...

    @property
    def UnattachedReference(self) -> SecurityKeyIdentifierClause:
        """
        Get: UnattachedReference(self: SecurityTokenDescriptor) -> SecurityKeyIdentifierClause
        Set: UnattachedReference(self: SecurityTokenDescriptor) = value
        """
        ...


    def AddAuthenticationClaims(self, authType:str, time:DateTime = ...): # -> 
        """ AddAuthenticationClaims(self: SecurityTokenDescriptor, authType: str)AddAuthenticationClaims(self: SecurityTokenDescriptor, authType: str, time: DateTime) """
        ...

    def ApplyTo(self, response:RequestSecurityTokenResponse): # -> 
        """ ApplyTo(self: SecurityTokenDescriptor, response: RequestSecurityTokenResponse) """
        ...


class SecurityTokenElement: # skipped bases: <type 'object'>, <type 'object'>
    """
    SecurityTokenElement(securityToken: SecurityToken)
    SecurityTokenElement(securityTokenXml: XmlElement, securityTokenHandlers: SecurityTokenHandlerCollection)
    """
    @property
    def SecurityTokenXml(self) -> XmlElement:
        """ Get: SecurityTokenXml(self: SecurityTokenElement) -> XmlElement """
        ...


    def GetIdentities(self) -> ReadOnlyCollection:
        """ GetIdentities(self: SecurityTokenElement) -> ReadOnlyCollection[ClaimsIdentity] """
        ...

    def GetSecurityToken(self) -> SecurityToken:
        """ GetSecurityToken(self: SecurityTokenElement) -> SecurityToken """
        ...

    def ReadSecurityToken(self, *args): #cannot find CLR method
        """ ReadSecurityToken(self: SecurityTokenElement, securityTokenXml: XmlElement, securityTokenHandlers: SecurityTokenHandlerCollection) -> SecurityToken """
        ...

    def ValidateToken(self, *args): #cannot find CLR method
        """ ValidateToken(self: SecurityTokenElement, securityTokenXml: XmlElement, securityTokenHandlers: SecurityTokenHandlerCollection) -> ReadOnlyCollection[ClaimsIdentity] """
        ...


class SecurityTokenExpiredException(SecurityTokenValidationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SecurityTokenExpiredException()
    SecurityTokenExpiredException(message: str)
    SecurityTokenExpiredException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class SecurityTokenHandlerCollection(Collection): # skipped bases: <type 'ICollection'>, <type 'IReadOnlyList[SecurityTokenHandler]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IEnumerable[SecurityTokenHandler]'>, <type 'ICollection[SecurityTokenHandler]'>, <type 'IReadOnlyCollection[SecurityTokenHandler]'>, <type 'IList[SecurityTokenHandler]'>, <type 'object'>
    """
    SecurityTokenHandlerCollection()
    SecurityTokenHandlerCollection(configuration: SecurityTokenHandlerConfiguration)
    SecurityTokenHandlerCollection(handlers: IEnumerable[SecurityTokenHandler])
    SecurityTokenHandlerCollection(handlers: IEnumerable[SecurityTokenHandler], configuration: SecurityTokenHandlerConfiguration)
    """
    @property
    def Configuration(self) -> SecurityTokenHandlerConfiguration:
        """ Get: Configuration(self: SecurityTokenHandlerCollection) -> SecurityTokenHandlerConfiguration """
        ...

    @property
    def TokenTypeIdentifiers(self) -> IEnumerable:
        """ Get: TokenTypeIdentifiers(self: SecurityTokenHandlerCollection) -> IEnumerable[str] """
        ...

    @property
    def TokenTypes(self) -> IEnumerable:
        """ Get: TokenTypes(self: SecurityTokenHandlerCollection) -> IEnumerable[Type] """
        ...


    def AddOrReplace(self, handler:SecurityTokenHandler): # -> 
        """ AddOrReplace(self: SecurityTokenHandlerCollection, handler: SecurityTokenHandler) """
        ...

    def CanReadKeyIdentifierClause(self, reader:XmlReader) -> bool:
        """ CanReadKeyIdentifierClause(self: SecurityTokenHandlerCollection, reader: XmlReader) -> bool """
        ...

    def CanReadKeyIdentifierClauseCore(self, *args): #cannot find CLR method
        """ CanReadKeyIdentifierClauseCore(self: SecurityTokenHandlerCollection, reader: XmlReader) -> bool """
        ...

    def CanReadToken(self, *__args:XmlReader) -> bool:
        """
        CanReadToken(self: SecurityTokenHandlerCollection, reader: XmlReader) -> bool
        CanReadToken(self: SecurityTokenHandlerCollection, tokenString: str) -> bool
        """
        ...

    def CanWriteToken(self, token:SecurityToken) -> bool:
        """ CanWriteToken(self: SecurityTokenHandlerCollection, token: SecurityToken) -> bool """
        ...

    @staticmethod
    def CreateDefaultSecurityTokenHandlerCollection(configuration=None) -> SecurityTokenHandlerCollection:
        """
        CreateDefaultSecurityTokenHandlerCollection() -> SecurityTokenHandlerCollection
        CreateDefaultSecurityTokenHandlerCollection(configuration: SecurityTokenHandlerConfiguration) -> SecurityTokenHandlerCollection
        """
        ...

    def CreateToken(self, tokenDescriptor:SecurityTokenDescriptor) -> SecurityToken:
        """ CreateToken(self: SecurityTokenHandlerCollection, tokenDescriptor: SecurityTokenDescriptor) -> SecurityToken """
        ...

    def ReadKeyIdentifierClause(self, reader:XmlReader) -> SecurityKeyIdentifierClause:
        """ ReadKeyIdentifierClause(self: SecurityTokenHandlerCollection, reader: XmlReader) -> SecurityKeyIdentifierClause """
        ...

    def ReadKeyIdentifierClauseCore(self, *args): #cannot find CLR method
        """ ReadKeyIdentifierClauseCore(self: SecurityTokenHandlerCollection, reader: XmlReader) -> SecurityKeyIdentifierClause """
        ...

    def ReadToken(self, *__args:XmlReader) -> SecurityToken:
        """
        ReadToken(self: SecurityTokenHandlerCollection, reader: XmlReader) -> SecurityToken
        ReadToken(self: SecurityTokenHandlerCollection, tokenString: str) -> SecurityToken
        """
        ...

    def ValidateToken(self, token:SecurityToken) -> ReadOnlyCollection:
        """ ValidateToken(self: SecurityTokenHandlerCollection, token: SecurityToken) -> ReadOnlyCollection[ClaimsIdentity] """
        ...

    def WriteKeyIdentifierClause(self, writer:XmlWriter, keyIdentifierClause:SecurityKeyIdentifierClause): # -> 
        """ WriteKeyIdentifierClause(self: SecurityTokenHandlerCollection, writer: XmlWriter, keyIdentifierClause: SecurityKeyIdentifierClause) """
        ...

    def WriteKeyIdentifierClauseCore(self, *args): #cannot find CLR method
        """ WriteKeyIdentifierClauseCore(self: SecurityTokenHandlerCollection, writer: XmlWriter, keyIdentifierClause: SecurityKeyIdentifierClause) """
        ...

    def WriteToken(self, *__args:SecurityToken) -> str:
        """ WriteToken(self: SecurityTokenHandlerCollection, writer: XmlWriter, token: SecurityToken)WriteToken(self: SecurityTokenHandlerCollection, token: SecurityToken) -> str """
        ...


class SecurityTokenHandlerCollectionManager: # skipped bases: <type 'object'>, <type 'object'>
    """ SecurityTokenHandlerCollectionManager(serviceName: str) """
    @property
    def Count(self) -> int:
        """ Get: Count(self: SecurityTokenHandlerCollectionManager) -> int """
        ...

    @property
    def SecurityTokenHandlerCollections(self) -> IEnumerable:
        """ Get: SecurityTokenHandlerCollections(self: SecurityTokenHandlerCollectionManager) -> IEnumerable[SecurityTokenHandlerCollection] """
        ...

    @property
    def ServiceName(self) -> str:
        """ Get: ServiceName(self: SecurityTokenHandlerCollectionManager) -> str """
        ...


    def ContainsKey(self, usage:str) -> bool:
        """ ContainsKey(self: SecurityTokenHandlerCollectionManager, usage: str) -> bool """
        ...

    @staticmethod
    def CreateDefaultSecurityTokenHandlerCollectionManager() -> SecurityTokenHandlerCollectionManager:
        """ CreateDefaultSecurityTokenHandlerCollectionManager() -> SecurityTokenHandlerCollectionManager """
        ...

    @staticmethod
    def CreateEmptySecurityTokenHandlerCollectionManager() -> SecurityTokenHandlerCollectionManager:
        """ CreateEmptySecurityTokenHandlerCollectionManager() -> SecurityTokenHandlerCollectionManager """
        ...

    def Usage(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...



class SecurityTokenHandlerConfiguration: # skipped bases: <type 'object'>, <type 'object'>
    """ SecurityTokenHandlerConfiguration() """
    @property
    def AudienceRestriction(self) -> AudienceRestriction:
        """
        Get: AudienceRestriction(self: SecurityTokenHandlerConfiguration) -> AudienceRestriction
        Set: AudienceRestriction(self: SecurityTokenHandlerConfiguration) = value
        """
        ...

    @property
    def Caches(self) -> IdentityModelCaches:
        """
        Get: Caches(self: SecurityTokenHandlerConfiguration) -> IdentityModelCaches
        Set: Caches(self: SecurityTokenHandlerConfiguration) = value
        """
        ...

    @property
    def CertificateValidationMode(self) -> X509CertificateValidationMode:
        """
        Get: CertificateValidationMode(self: SecurityTokenHandlerConfiguration) -> X509CertificateValidationMode
        Set: CertificateValidationMode(self: SecurityTokenHandlerConfiguration) = value
        """
        ...

    @property
    def CertificateValidator(self) -> X509CertificateValidator:
        """
        Get: CertificateValidator(self: SecurityTokenHandlerConfiguration) -> X509CertificateValidator
        Set: CertificateValidator(self: SecurityTokenHandlerConfiguration) = value
        """
        ...

    @property
    def DetectReplayedTokens(self) -> bool:
        """
        Get: DetectReplayedTokens(self: SecurityTokenHandlerConfiguration) -> bool
        Set: DetectReplayedTokens(self: SecurityTokenHandlerConfiguration) = value
        """
        ...

    @property
    def IssuerNameRegistry(self) -> IssuerNameRegistry:
        """
        Get: IssuerNameRegistry(self: SecurityTokenHandlerConfiguration) -> IssuerNameRegistry
        Set: IssuerNameRegistry(self: SecurityTokenHandlerConfiguration) = value
        """
        ...

    @property
    def IssuerTokenResolver(self) -> SecurityTokenResolver:
        """
        Get: IssuerTokenResolver(self: SecurityTokenHandlerConfiguration) -> SecurityTokenResolver
        Set: IssuerTokenResolver(self: SecurityTokenHandlerConfiguration) = value
        """
        ...

    @property
    def MaxClockSkew(self) -> TimeSpan:
        """
        Get: MaxClockSkew(self: SecurityTokenHandlerConfiguration) -> TimeSpan
        Set: MaxClockSkew(self: SecurityTokenHandlerConfiguration) = value
        """
        ...

    @property
    def RevocationMode(self) -> X509RevocationMode:
        """
        Get: RevocationMode(self: SecurityTokenHandlerConfiguration) -> X509RevocationMode
        Set: RevocationMode(self: SecurityTokenHandlerConfiguration) = value
        """
        ...

    @property
    def SaveBootstrapContext(self) -> bool:
        """
        Get: SaveBootstrapContext(self: SecurityTokenHandlerConfiguration) -> bool
        Set: SaveBootstrapContext(self: SecurityTokenHandlerConfiguration) = value
        """
        ...

    @property
    def ServiceTokenResolver(self) -> SecurityTokenResolver:
        """
        Get: ServiceTokenResolver(self: SecurityTokenHandlerConfiguration) -> SecurityTokenResolver
        Set: ServiceTokenResolver(self: SecurityTokenHandlerConfiguration) = value
        """
        ...

    @property
    def TokenReplayCacheExpirationPeriod(self) -> TimeSpan:
        """
        Get: TokenReplayCacheExpirationPeriod(self: SecurityTokenHandlerConfiguration) -> TimeSpan
        Set: TokenReplayCacheExpirationPeriod(self: SecurityTokenHandlerConfiguration) = value
        """
        ...

    @property
    def TrustedStoreLocation(self) -> StoreLocation:
        """
        Get: TrustedStoreLocation(self: SecurityTokenHandlerConfiguration) -> StoreLocation
        Set: TrustedStoreLocation(self: SecurityTokenHandlerConfiguration) = value
        """
        ...


    DefaultCertificateValidationMode: X509CertificateValidationMode = ...
    DefaultCertificateValidator = ...
    DefaultDetectReplayedTokens: bool = ...
    DefaultIssuerNameRegistry: ConfigurationBasedIssuerNameRegistry = ...
    DefaultIssuerTokenResolver: IssuerTokenResolver = ...
    DefaultMaxClockSkew: TimeSpan = ...
    DefaultRevocationMode: X509RevocationMode = ...
    DefaultSaveBootstrapContext: bool = ...
    DefaultTokenReplayCacheExpirationPeriod: TimeSpan = ...
    DefaultTrustedStoreLocation: StoreLocation = ...


class SecurityTokenNotYetValidException(SecurityTokenValidationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SecurityTokenNotYetValidException()
    SecurityTokenNotYetValidException(message: str)
    SecurityTokenNotYetValidException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class SecurityTokenReplayDetectedException(SecurityTokenValidationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SecurityTokenReplayDetectedException()
    SecurityTokenReplayDetectedException(message: str)
    SecurityTokenReplayDetectedException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class SecurityTokenTypes: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Kerberos(self) -> str:
        """ Get: Kerberos() -> str """
        ...

    @property
    def Rsa(self) -> str:
        """ Get: Rsa() -> str """
        ...

    @property
    def Saml(self) -> str:
        """ Get: Saml() -> str """
        ...

    @property
    def UserName(self) -> str:
        """ Get: UserName() -> str """
        ...

    @property
    def X509Certificate(self) -> str:
        """ Get: X509Certificate() -> str """
        ...


    __all__: list = ...


class SessionSecurityToken(SecurityToken, ISerializable): # skipped bases: <type 'object'>
    """
    SessionSecurityToken(claimsPrincipal: ClaimsPrincipal)
    SessionSecurityToken(claimsPrincipal: ClaimsPrincipal, lifetime: TimeSpan)
    SessionSecurityToken(claimsPrincipal: ClaimsPrincipal, context: str)
    SessionSecurityToken(claimsPrincipal: ClaimsPrincipal, context: str, validFrom: Nullable[DateTime], validTo: Nullable[DateTime])
    SessionSecurityToken(claimsPrincipal: ClaimsPrincipal, context: str, endpointId: str, validFrom: Nullable[DateTime], validTo: Nullable[DateTime])
    SessionSecurityToken(claimsPrincipal: ClaimsPrincipal, contextId: UniqueId, context: str, endpointId: str, lifetime: TimeSpan, key: SymmetricSecurityKey)
    SessionSecurityToken(claimsPrincipal: ClaimsPrincipal, contextId: UniqueId, context: str, endpointId: str, validFrom: DateTime, lifetime: TimeSpan, key: SymmetricSecurityKey)
    SessionSecurityToken(claimsPrincipal: ClaimsPrincipal, contextId: UniqueId, context: str, endpointId: str, validFrom: Nullable[DateTime], validTo: Nullable[DateTime], key: SymmetricSecurityKey)
    """
    @property
    def ClaimsPrincipal(self) -> ClaimsPrincipal:
        """ Get: ClaimsPrincipal(self: SessionSecurityToken) -> ClaimsPrincipal """
        ...

    @property
    def Context(self) -> str:
        """ Get: Context(self: SessionSecurityToken) -> str """
        ...

    @property
    def ContextId(self) -> UniqueId:
        """ Get: ContextId(self: SessionSecurityToken) -> UniqueId """
        ...

    @property
    def EndpointId(self) -> str:
        """ Get: EndpointId(self: SessionSecurityToken) -> str """
        ...

    @property
    def IsPersistent(self) -> bool:
        """
        Get: IsPersistent(self: SessionSecurityToken) -> bool
        Set: IsPersistent(self: SessionSecurityToken) = value
        """
        ...

    @property
    def IsReferenceMode(self) -> bool:
        """
        Get: IsReferenceMode(self: SessionSecurityToken) -> bool
        Set: IsReferenceMode(self: SessionSecurityToken) = value
        """
        ...

    @property
    def KeyEffectiveTime(self) -> DateTime:
        """ Get: KeyEffectiveTime(self: SessionSecurityToken) -> DateTime """
        ...

    @property
    def KeyExpirationTime(self) -> DateTime:
        """ Get: KeyExpirationTime(self: SessionSecurityToken) -> DateTime """
        ...

    @property
    def KeyGeneration(self) -> UniqueId:
        """ Get: KeyGeneration(self: SessionSecurityToken) -> UniqueId """
        ...

    @property
    def SecureConversationVersion(self) -> Uri:
        """ Get: SecureConversationVersion(self: SessionSecurityToken) -> Uri """
        ...


    def __new__(cls, claimsPrincipal:ClaimsPrincipal, *__args:TimeSpan) -> Self:
        """
        __new__(cls: type, claimsPrincipal: ClaimsPrincipal)
        __new__(cls: type, claimsPrincipal: ClaimsPrincipal, lifetime: TimeSpan)
        __new__(cls: type, claimsPrincipal: ClaimsPrincipal, context: str)
        __new__(cls: type, claimsPrincipal: ClaimsPrincipal, context: str, validFrom: Nullable[DateTime], validTo: Nullable[DateTime])
        __new__(cls: type, claimsPrincipal: ClaimsPrincipal, context: str, endpointId: str, validFrom: Nullable[DateTime], validTo: Nullable[DateTime])
        __new__(cls: type, claimsPrincipal: ClaimsPrincipal, contextId: UniqueId, context: str, endpointId: str, lifetime: TimeSpan, key: SymmetricSecurityKey)
        __new__(cls: type, claimsPrincipal: ClaimsPrincipal, contextId: UniqueId, context: str, endpointId: str, validFrom: DateTime, lifetime: TimeSpan, key: SymmetricSecurityKey)
        __new__(cls: type, claimsPrincipal: ClaimsPrincipal, contextId: UniqueId, context: str, endpointId: str, validFrom: Nullable[DateTime], validTo: Nullable[DateTime], key: SymmetricSecurityKey)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        ...

    def __reduce_ex__(self, *args): #cannot find CLR method
        ...


class SessionSecurityTokenCache(ICustomIdentityConfiguration): # skipped bases: <type 'object'>
    """ no doc """
    def AddOrUpdate(self, key:SessionSecurityTokenCacheKey, value:SessionSecurityToken, expiryTime:DateTime): # -> 
        """ AddOrUpdate(self: SessionSecurityTokenCache, key: SessionSecurityTokenCacheKey, value: SessionSecurityToken, expiryTime: DateTime) """
        ...

    def Get(self, key:SessionSecurityTokenCacheKey) -> SessionSecurityToken:
        """ Get(self: SessionSecurityTokenCache, key: SessionSecurityTokenCacheKey) -> SessionSecurityToken """
        ...

    def GetAll(self, endpointId:str, contextId:UniqueId) -> IEnumerable:
        """ GetAll(self: SessionSecurityTokenCache, endpointId: str, contextId: UniqueId) -> IEnumerable[SessionSecurityToken] """
        ...

    def Remove(self, key:SessionSecurityTokenCacheKey): # -> 
        """ Remove(self: SessionSecurityTokenCache, key: SessionSecurityTokenCacheKey) """
        ...

    def RemoveAll(self, endpointId:str, contextId:UniqueId = ...): # -> 
        """ RemoveAll(self: SessionSecurityTokenCache, endpointId: str, contextId: UniqueId)RemoveAll(self: SessionSecurityTokenCache, endpointId: str) """
        ...


class SessionSecurityTokenCacheKey: # skipped bases: <type 'object'>, <type 'object'>
    """ SessionSecurityTokenCacheKey(endpointId: str, contextId: UniqueId, keyGeneration: UniqueId) """
    @property
    def ContextId(self) -> UniqueId:
        """ Get: ContextId(self: SessionSecurityTokenCacheKey) -> UniqueId """
        ...

    @property
    def EndpointId(self) -> str:
        """ Get: EndpointId(self: SessionSecurityTokenCacheKey) -> str """
        ...

    @property
    def IgnoreKeyGeneration(self) -> bool:
        """
        Get: IgnoreKeyGeneration(self: SessionSecurityTokenCacheKey) -> bool
        Set: IgnoreKeyGeneration(self: SessionSecurityTokenCacheKey) = value
        """
        ...

    @property
    def KeyGeneration(self) -> UniqueId:
        """ Get: KeyGeneration(self: SessionSecurityTokenCacheKey) -> UniqueId """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: SessionSecurityTokenCacheKey, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SessionSecurityTokenCacheKey) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: SessionSecurityTokenCacheKey) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SessionSecurityTokenHandler(SecurityTokenHandler): # skipped bases: <type 'ICustomIdentityConfiguration'>, <type 'object'>
    """
    SessionSecurityTokenHandler()
    SessionSecurityTokenHandler(transforms: ReadOnlyCollection[CookieTransform])
    SessionSecurityTokenHandler(transforms: ReadOnlyCollection[CookieTransform], tokenLifetime: TimeSpan)
    """
    @property
    def CookieElementName(self) -> str:
        """ Get: CookieElementName(self: SessionSecurityTokenHandler) -> str """
        ...

    @property
    def CookieNamespace(self) -> str:
        """ Get: CookieNamespace(self: SessionSecurityTokenHandler) -> str """
        ...

    @property
    def DefaultTokenLifetime(self) -> TimeSpan:
        """ Get: DefaultTokenLifetime() -> TimeSpan """
        ...

    @property
    def TokenLifetime(self) -> TimeSpan:
        """
        Get: TokenLifetime(self: SessionSecurityTokenHandler) -> TimeSpan
        Set: TokenLifetime(self: SessionSecurityTokenHandler) = value
        """
        ...

    @property
    def Transforms(self) -> ReadOnlyCollection:
        """ Get: Transforms(self: SessionSecurityTokenHandler) -> ReadOnlyCollection[CookieTransform] """
        ...


    def ApplyTransforms(self, *args): #cannot find CLR method
        """ ApplyTransforms(self: SessionSecurityTokenHandler, cookie: Array[Byte], outbound: bool) -> Array[Byte] """
        ...

    def CreateSessionSecurityToken(self, principal:ClaimsPrincipal, context:str, endpointId:str, validFrom:DateTime, validTo:DateTime) -> SessionSecurityToken:
        """ CreateSessionSecurityToken(self: SessionSecurityTokenHandler, principal: ClaimsPrincipal, context: str, endpointId: str, validFrom: DateTime, validTo: DateTime) -> SessionSecurityToken """
        ...

    def SetTransforms(self, *args): #cannot find CLR method
        """ SetTransforms(self: SessionSecurityTokenHandler, transforms: IEnumerable[CookieTransform]) """
        ...

    def ValidateSession(self, *args): #cannot find CLR method
        """ ValidateSession(self: SessionSecurityTokenHandler, securityToken: SessionSecurityToken) """
        ...

    def __new__(cls, transforms:ReadOnlyCollection = ..., tokenLifetime:TimeSpan = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, transforms: ReadOnlyCollection[CookieTransform])
        __new__(cls: type, transforms: ReadOnlyCollection[CookieTransform], tokenLifetime: TimeSpan)
        """
        ...

    DefaultCookieTransforms = ...
    DefaultLifetime: TimeSpan = ...


class SigningCredentials: # skipped bases: <type 'object'>, <type 'object'>
    """
    SigningCredentials(signingKey: SecurityKey, signatureAlgorithm: str, digestAlgorithm: str)
    SigningCredentials(signingKey: SecurityKey, signatureAlgorithm: str, digestAlgorithm: str, signingKeyIdentifier: SecurityKeyIdentifier)
    """
    @property
    def DigestAlgorithm(self) -> str:
        """ Get: DigestAlgorithm(self: SigningCredentials) -> str """
        ...

    @property
    def SignatureAlgorithm(self) -> str:
        """ Get: SignatureAlgorithm(self: SigningCredentials) -> str """
        ...

    @property
    def SigningKey(self) -> SecurityKey:
        """ Get: SigningKey(self: SigningCredentials) -> SecurityKey """
        ...

    @property
    def SigningKeyIdentifier(self) -> SecurityKeyIdentifier:
        """ Get: SigningKeyIdentifier(self: SigningCredentials) -> SecurityKeyIdentifier """
        ...



class SymmetricProofDescriptor(ProofDescriptor): # skipped bases: <type 'object'>
    """
    SymmetricProofDescriptor(key: Array[Byte], targetWrappingCredentials: EncryptingCredentials)
    SymmetricProofDescriptor(targetWrappingCredentials: EncryptingCredentials)
    SymmetricProofDescriptor(keySizeInBits: int, targetWrappingCredentials: EncryptingCredentials)
    SymmetricProofDescriptor(keySizeInBits: int, targetWrappingCredentials: EncryptingCredentials, requestorWrappingCredentials: EncryptingCredentials)
    SymmetricProofDescriptor(keySizeInBits: int, targetWrappingCredentials: EncryptingCredentials, requestorWrappingCredentials: EncryptingCredentials, encryptWith: str)
    SymmetricProofDescriptor(keySizeInBits: int, targetWrappingCredentials: EncryptingCredentials, requestorWrappingCredentials: EncryptingCredentials, sourceEntropy: Array[Byte])
    SymmetricProofDescriptor(keySizeInBits: int, targetWrappingCredentials: EncryptingCredentials, requestorWrappingCredentials: EncryptingCredentials, sourceEntropy: Array[Byte], encryptWith: str)
    """
    @property
    def RequestorEncryptingCredentials(self):
        ...

    @property
    def TargetEncryptingCredentials(self):
        ...


    def GetKeyBytes(self) -> Array:
        """ GetKeyBytes(self: SymmetricProofDescriptor) -> Array[Byte] """
        ...

    def GetSourceEntropy(self, *args): #cannot find CLR method
        """ GetSourceEntropy(self: SymmetricProofDescriptor) -> Array[Byte] """
        ...

    def GetTargetEntropy(self, *args): #cannot find CLR method
        """ GetTargetEntropy(self: SymmetricProofDescriptor) -> Array[Byte] """
        ...

    def __new__(cls, *__args:EncryptingCredentials) -> Self:
        """
        __new__(cls: type, key: Array[Byte], targetWrappingCredentials: EncryptingCredentials)
        __new__(cls: type, targetWrappingCredentials: EncryptingCredentials)
        __new__(cls: type, keySizeInBits: int, targetWrappingCredentials: EncryptingCredentials)
        __new__(cls: type, keySizeInBits: int, targetWrappingCredentials: EncryptingCredentials, requestorWrappingCredentials: EncryptingCredentials)
        __new__(cls: type, keySizeInBits: int, targetWrappingCredentials: EncryptingCredentials, requestorWrappingCredentials: EncryptingCredentials, encryptWith: str)
        __new__(cls: type, keySizeInBits: int, targetWrappingCredentials: EncryptingCredentials, requestorWrappingCredentials: EncryptingCredentials, sourceEntropy: Array[Byte])
        __new__(cls: type, keySizeInBits: int, targetWrappingCredentials: EncryptingCredentials, requestorWrappingCredentials: EncryptingCredentials, sourceEntropy: Array[Byte], encryptWith: str)
        """
        ...


class TokenReplayCache(ICustomIdentityConfiguration): # skipped bases: <type 'object'>
    """ no doc """
    def AddOrUpdate(self, key:str, securityToken:SecurityToken, expirationTime:DateTime): # -> 
        """ AddOrUpdate(self: TokenReplayCache, key: str, securityToken: SecurityToken, expirationTime: DateTime) """
        ...

    def Contains(self, key:str) -> bool:
        """ Contains(self: TokenReplayCache, key: str) -> bool """
        ...

    def Get(self, key:str) -> SecurityToken:
        """ Get(self: TokenReplayCache, key: str) -> SecurityToken """
        ...

    def Remove(self, key:str): # -> 
        """ Remove(self: TokenReplayCache, key: str) """
        ...


class UserNameSecurityToken(SecurityToken): # skipped bases: <type 'object'>
    """
    UserNameSecurityToken(userName: str, password: str)
    UserNameSecurityToken(userName: str, password: str, id: str)
    """
    @property
    def Password(self) -> str:
        """ Get: Password(self: UserNameSecurityToken) -> str """
        ...

    @property
    def UserName(self) -> str:
        """ Get: UserName(self: UserNameSecurityToken) -> str """
        ...


    def __new__(cls, userName:str, password:str, id:str = ...) -> Self:
        """
        __new__(cls: type, userName: str, password: str)
        __new__(cls: type, userName: str, password: str, id: str)
        """
        ...


class UserNameSecurityTokenHandler(SecurityTokenHandler): # skipped bases: <type 'ICustomIdentityConfiguration'>, <type 'object'>
    """ no doc """
    @property
    def RetainPassword(self) -> bool:
        """
        Get: RetainPassword(self: UserNameSecurityTokenHandler) -> bool
        Set: RetainPassword(self: UserNameSecurityTokenHandler) = value
        """
        ...



class WindowsUserNameSecurityTokenHandler(UserNameSecurityTokenHandler): # skipped bases: <type 'ICustomIdentityConfiguration'>, <type 'object'>
    """ WindowsUserNameSecurityTokenHandler() """
    @property
    def CanValidateToken(self) -> bool:
        """ Get: CanValidateToken(self: WindowsUserNameSecurityTokenHandler) -> bool """
        ...


    def ValidateToken(self, token:SecurityToken) -> ReadOnlyCollection:
        """ ValidateToken(self: WindowsUserNameSecurityTokenHandler, token: SecurityToken) -> ReadOnlyCollection[ClaimsIdentity] """
        ...


class X509AsymmetricSecurityKey(AsymmetricSecurityKey): # skipped bases: <type 'object'>
    """ X509AsymmetricSecurityKey(certificate: X509Certificate2) """
    @property
    def KeySize(self) -> int:
        """ Get: KeySize(self: X509AsymmetricSecurityKey) -> int """
        ...


    def DecryptKey(self, algorithm:str, keyData:Array) -> Array:
        """ DecryptKey(self: X509AsymmetricSecurityKey, algorithm: str, keyData: Array[Byte]) -> Array[Byte] """
        ...

    def EncryptKey(self, algorithm:str, keyData:Array) -> Array:
        """ EncryptKey(self: X509AsymmetricSecurityKey, algorithm: str, keyData: Array[Byte]) -> Array[Byte] """
        ...

    def IsAsymmetricAlgorithm(self, algorithm:str) -> bool:
        """ IsAsymmetricAlgorithm(self: X509AsymmetricSecurityKey, algorithm: str) -> bool """
        ...

    def IsSupportedAlgorithm(self, algorithm:str) -> bool:
        """ IsSupportedAlgorithm(self: X509AsymmetricSecurityKey, algorithm: str) -> bool """
        ...

    def IsSymmetricAlgorithm(self, algorithm:str) -> bool:
        """ IsSymmetricAlgorithm(self: X509AsymmetricSecurityKey, algorithm: str) -> bool """
        ...

    def __new__(cls, certificate:X509Certificate2) -> Self:
        """ __new__(cls: type, certificate: X509Certificate2) """
        ...


class X509CertificateStoreTokenResolver(SecurityTokenResolver): # skipped bases: <type 'ICustomIdentityConfiguration'>, <type 'object'>
    """
    X509CertificateStoreTokenResolver()
    X509CertificateStoreTokenResolver(storeName: StoreName, storeLocation: StoreLocation)
    X509CertificateStoreTokenResolver(storeName: str, storeLocation: StoreLocation)
    """
    @property
    def StoreLocation(self) -> StoreLocation:
        """ Get: StoreLocation(self: X509CertificateStoreTokenResolver) -> StoreLocation """
        ...

    @property
    def StoreName(self) -> str:
        """ Get: StoreName(self: X509CertificateStoreTokenResolver) -> str """
        ...


    def __new__(cls, storeName:StoreName = ..., storeLocation:StoreLocation = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, storeName: StoreName, storeLocation: StoreLocation)
        __new__(cls: type, storeName: str, storeLocation: StoreLocation)
        """
        ...


class X509DataSecurityKeyIdentifierClauseSerializer(SecurityKeyIdentifierClauseSerializer): # skipped bases: <type 'object'>
    """ X509DataSecurityKeyIdentifierClauseSerializer() """
    pass

class X509EncryptingCredentials(EncryptingCredentials): # skipped bases: <type 'object'>
    """
    X509EncryptingCredentials(certificate: X509Certificate2)
    X509EncryptingCredentials(certificate: X509Certificate2, keyWrappingAlgorithm: str)
    X509EncryptingCredentials(certificate: X509Certificate2, ski: SecurityKeyIdentifier)
    X509EncryptingCredentials(certificate: X509Certificate2, ski: SecurityKeyIdentifier, keyWrappingAlgorithm: str)
    """
    @property
    def Certificate(self) -> X509Certificate2:
        """ Get: Certificate(self: X509EncryptingCredentials) -> X509Certificate2 """
        ...



class X509IssuerSerialKeyIdentifierClause(SecurityKeyIdentifierClause): # skipped bases: <type 'object'>
    """
    X509IssuerSerialKeyIdentifierClause(issuerName: str, issuerSerialNumber: str)
    X509IssuerSerialKeyIdentifierClause(certificate: X509Certificate2)
    """
    @property
    def IssuerName(self) -> str:
        """ Get: IssuerName(self: X509IssuerSerialKeyIdentifierClause) -> str """
        ...

    @property
    def IssuerSerialNumber(self) -> str:
        """ Get: IssuerSerialNumber(self: X509IssuerSerialKeyIdentifierClause) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: X509IssuerSerialKeyIdentifierClause) -> str """
        ...


class X509NTAuthChainTrustValidator(X509CertificateValidator): # skipped bases: <type 'ICustomIdentityConfiguration'>, <type 'object'>
    """
    X509NTAuthChainTrustValidator()
    X509NTAuthChainTrustValidator(useMachineContext: bool, chainPolicy: X509ChainPolicy)
    """
    def __new__(cls, useMachineContext:bool = ..., chainPolicy:X509ChainPolicy = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, useMachineContext: bool, chainPolicy: X509ChainPolicy)
        """
        ...


class X509RawDataKeyIdentifierClause(BinaryKeyIdentifierClause): # skipped bases: <type 'object'>
    """
    X509RawDataKeyIdentifierClause(certificate: X509Certificate2)
    X509RawDataKeyIdentifierClause(certificateRawData: Array[Byte])
    """
    @property
    def CanCreateKey(self) -> bool:
        """ Get: CanCreateKey(self: X509RawDataKeyIdentifierClause) -> bool """
        ...


    def CreateKey(self) -> SecurityKey:
        """ CreateKey(self: X509RawDataKeyIdentifierClause) -> SecurityKey """
        ...

    def GetX509RawData(self) -> Array:
        """ GetX509RawData(self: X509RawDataKeyIdentifierClause) -> Array[Byte] """
        ...

    def ToString(self) -> str:
        """ ToString(self: X509RawDataKeyIdentifierClause) -> str """
        ...


class X509SecurityToken(IDisposable, SecurityToken): # skipped bases: <type 'object'>
    """
    X509SecurityToken(certificate: X509Certificate2)
    X509SecurityToken(certificate: X509Certificate2, id: str)
    """
    @property
    def Certificate(self) -> X509Certificate2:
        """ Get: Certificate(self: X509SecurityToken) -> X509Certificate2 """
        ...


    def ThrowIfDisposed(self, *args): #cannot find CLR method
        """ ThrowIfDisposed(self: X509SecurityToken) """
        ...

    def __new__(cls, certificate:X509Certificate2, id:str = ...) -> Self:
        """
        __new__(cls: type, certificate: X509Certificate2)
        __new__(cls: type, certificate: X509Certificate2, id: str)
        """
        ...


class X509SecurityTokenHandler(SecurityTokenHandler): # skipped bases: <type 'ICustomIdentityConfiguration'>, <type 'object'>
    """
    X509SecurityTokenHandler()
    X509SecurityTokenHandler(certificateValidator: X509CertificateValidator)
    X509SecurityTokenHandler(mapToWindows: bool)
    X509SecurityTokenHandler(mapToWindows: bool, certificateValidator: X509CertificateValidator)
    """
    @property
    def CertificateValidator(self) -> X509CertificateValidator:
        """
        Get: CertificateValidator(self: X509SecurityTokenHandler) -> X509CertificateValidator
        Set: CertificateValidator(self: X509SecurityTokenHandler) = value
        """
        ...

    @property
    def MapToWindows(self) -> bool:
        """
        Get: MapToWindows(self: X509SecurityTokenHandler) -> bool
        Set: MapToWindows(self: X509SecurityTokenHandler) = value
        """
        ...

    @property
    def WriteXmlDSigDefinedClauseTypes(self) -> bool:
        """
        Get: WriteXmlDSigDefinedClauseTypes(self: X509SecurityTokenHandler) -> bool
        Set: WriteXmlDSigDefinedClauseTypes(self: X509SecurityTokenHandler) = value
        """
        ...

    @property
    def X509NTAuthChainTrustValidator(self) -> X509NTAuthChainTrustValidator:
        """
        Get: X509NTAuthChainTrustValidator(self: X509SecurityTokenHandler) -> X509NTAuthChainTrustValidator
        Set: X509NTAuthChainTrustValidator(self: X509SecurityTokenHandler) = value
        """
        ...


    def __new__(cls, *__args:X509CertificateValidator) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, certificateValidator: X509CertificateValidator)
        __new__(cls: type, mapToWindows: bool)
        __new__(cls: type, mapToWindows: bool, certificateValidator: X509CertificateValidator)
        """
        ...


class X509SigningCredentials(SigningCredentials): # skipped bases: <type 'object'>
    """
    X509SigningCredentials(certificate: X509Certificate2)
    X509SigningCredentials(certificate: X509Certificate2, signatureAlgorithm: str, digestAlgorithm: str)
    X509SigningCredentials(certificate: X509Certificate2, ski: SecurityKeyIdentifier)
    X509SigningCredentials(certificate: X509Certificate2, ski: SecurityKeyIdentifier, signatureAlgorithm: str, digestAlgorithm: str)
    """
    @property
    def Certificate(self) -> X509Certificate2:
        """ Get: Certificate(self: X509SigningCredentials) -> X509Certificate2 """
        ...



class X509SubjectKeyIdentifierClause(BinaryKeyIdentifierClause): # skipped bases: <type 'object'>
    """ X509SubjectKeyIdentifierClause(ski: Array[Byte]) """
    @staticmethod
    def CanCreateFrom(certificate:X509Certificate2) -> bool:
        """ CanCreateFrom(certificate: X509Certificate2) -> bool """
        ...

    def GetX509SubjectKeyIdentifier(self) -> Array:
        """ GetX509SubjectKeyIdentifier(self: X509SubjectKeyIdentifierClause) -> Array[Byte] """
        ...

    def ToString(self) -> str:
        """ ToString(self: X509SubjectKeyIdentifierClause) -> str """
        ...

    @staticmethod
    def TryCreateFrom(certificate, keyIdentifierClause) -> Tuple_[bool, X509SubjectKeyIdentifierClause]:
        """ TryCreateFrom(certificate: X509Certificate2) -> (bool, X509SubjectKeyIdentifierClause) """
        ...


class X509ThumbprintKeyIdentifierClause(BinaryKeyIdentifierClause): # skipped bases: <type 'object'>
    """
    X509ThumbprintKeyIdentifierClause(certificate: X509Certificate2)
    X509ThumbprintKeyIdentifierClause(thumbprint: Array[Byte])
    """
    def GetX509Thumbprint(self) -> Array:
        """ GetX509Thumbprint(self: X509ThumbprintKeyIdentifierClause) -> Array[Byte] """
        ...

    def ToString(self) -> str:
        """ ToString(self: X509ThumbprintKeyIdentifierClause) -> str """
        ...


class X509WindowsSecurityToken(X509SecurityToken): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    X509WindowsSecurityToken(certificate: X509Certificate2, windowsIdentity: WindowsIdentity)
    X509WindowsSecurityToken(certificate: X509Certificate2, windowsIdentity: WindowsIdentity, id: str)
    X509WindowsSecurityToken(certificate: X509Certificate2, windowsIdentity: WindowsIdentity, authenticationType: str, id: str)
    """
    @property
    def AuthenticationType(self) -> str:
        """ Get: AuthenticationType(self: X509WindowsSecurityToken) -> str """
        ...

    @property
    def WindowsIdentity(self) -> WindowsIdentity:
        """ Get: WindowsIdentity(self: X509WindowsSecurityToken) -> WindowsIdentity """
        ...



