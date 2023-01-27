# encoding: utf-8
# module System.ServiceModel.Security calls itself Security
# from System.ServiceModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.IdentityModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.JScript import Binding

from Microsoft.VisualBasic import Collection

from System import (Array, AsyncCallback, Enum, EventArgs, IAsyncResult, 
    IDisposable, TimeSpan, Uri)

from System.Collections import ICollection, IList

from System.Collections.Generic import Dictionary, KeyedByTypeCollection

from System.Collections.ObjectModel import ReadOnlyCollection

from System.IdentityModel import SecurityTokenService

from System.IdentityModel.Configuration import (
    SecurityTokenServiceConfiguration)

from System.IdentityModel.Policy import AuthorizationContext

from System.IdentityModel.Protocols.WSTrust import (RequestSecurityToken, 
    RequestSecurityTokenResponse, WSTrustMessage, WSTrustRequestSerializer, 
    WSTrustResponseSerializer, WSTrustSerializationContext)

from System.IdentityModel.Selectors import (AudienceUriMode, 
    SecurityTokenManager, SecurityTokenProvider, SecurityTokenRequirement, 
    SecurityTokenResolver, SecurityTokenSerializer, UserNamePasswordValidator, 
    X509CertificateValidator)

from System.IdentityModel.Tokens import (BinaryKeyIdentifierClause, 
    SamlSerializer, SecurityKey, SecurityKeyIdentifierClause, SecurityToken, 
    SecurityTokenHandlerCollectionManager)

from System.Messaging import Message

from System.Net import NetworkCredential

from System.Security.Claims import ClaimsPrincipal

from System.Security.Cryptography.X509Certificates import (StoreLocation, 
    StoreName, X509Certificate2, X509RevocationMode)

from System.Security.Principal import IPrincipal, TokenImpersonationLevel

from System.ServiceModel import (ChannelFactory, CommunicationException, 
    CommunicationState, EndpointAddress, EndpointIdentity, ServiceHost, 
    ServiceSecurityContext)

from System.ServiceModel.Channels import (BodyWriter, IChannel, 
    IMessageProperty, ISession)

from System.ServiceModel.Description import (IContractBehavior, 
    IWsdlExportExtension, ServiceCredentials)

from System.ServiceModel.Dispatcher import IInteractiveChannelInitializer

from System.ServiceModel.Security.Tokens import SecurityTokenReferenceStyle

from System.Web.Security import MembershipProvider

from System.Xml import (UniqueId, XmlDictionaryString, XmlDictionaryWriter, 
    XmlElement, XmlReader)

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    X509CertificateValidationMode, field#)
"""

# no functions
# classes

class SecurityAlgorithmSuite: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Basic128(self) -> SecurityAlgorithmSuite:
        """ Get: Basic128() -> SecurityAlgorithmSuite """
        ...

    @property
    def Basic128Rsa15(self) -> SecurityAlgorithmSuite:
        """ Get: Basic128Rsa15() -> SecurityAlgorithmSuite """
        ...

    @property
    def Basic128Sha256(self) -> SecurityAlgorithmSuite:
        """ Get: Basic128Sha256() -> SecurityAlgorithmSuite """
        ...

    @property
    def Basic128Sha256Rsa15(self) -> SecurityAlgorithmSuite:
        """ Get: Basic128Sha256Rsa15() -> SecurityAlgorithmSuite """
        ...

    @property
    def Basic192(self) -> SecurityAlgorithmSuite:
        """ Get: Basic192() -> SecurityAlgorithmSuite """
        ...

    @property
    def Basic192Rsa15(self) -> SecurityAlgorithmSuite:
        """ Get: Basic192Rsa15() -> SecurityAlgorithmSuite """
        ...

    @property
    def Basic192Sha256(self) -> SecurityAlgorithmSuite:
        """ Get: Basic192Sha256() -> SecurityAlgorithmSuite """
        ...

    @property
    def Basic192Sha256Rsa15(self) -> SecurityAlgorithmSuite:
        """ Get: Basic192Sha256Rsa15() -> SecurityAlgorithmSuite """
        ...

    @property
    def Basic256(self) -> SecurityAlgorithmSuite:
        """ Get: Basic256() -> SecurityAlgorithmSuite """
        ...

    @property
    def Basic256Rsa15(self) -> SecurityAlgorithmSuite:
        """ Get: Basic256Rsa15() -> SecurityAlgorithmSuite """
        ...

    @property
    def Basic256Sha256(self) -> SecurityAlgorithmSuite:
        """ Get: Basic256Sha256() -> SecurityAlgorithmSuite """
        ...

    @property
    def Basic256Sha256Rsa15(self) -> SecurityAlgorithmSuite:
        """ Get: Basic256Sha256Rsa15() -> SecurityAlgorithmSuite """
        ...

    @property
    def Default(self) -> SecurityAlgorithmSuite:
        """ Get: Default() -> SecurityAlgorithmSuite """
        ...

    @property
    def DefaultAsymmetricKeyWrapAlgorithm(self) -> str:
        """ Get: DefaultAsymmetricKeyWrapAlgorithm(self: SecurityAlgorithmSuite) -> str """
        ...

    @property
    def DefaultAsymmetricSignatureAlgorithm(self) -> str:
        """ Get: DefaultAsymmetricSignatureAlgorithm(self: SecurityAlgorithmSuite) -> str """
        ...

    @property
    def DefaultCanonicalizationAlgorithm(self) -> str:
        """ Get: DefaultCanonicalizationAlgorithm(self: SecurityAlgorithmSuite) -> str """
        ...

    @property
    def DefaultDigestAlgorithm(self) -> str:
        """ Get: DefaultDigestAlgorithm(self: SecurityAlgorithmSuite) -> str """
        ...

    @property
    def DefaultEncryptionAlgorithm(self) -> str:
        """ Get: DefaultEncryptionAlgorithm(self: SecurityAlgorithmSuite) -> str """
        ...

    @property
    def DefaultEncryptionKeyDerivationLength(self) -> int:
        """ Get: DefaultEncryptionKeyDerivationLength(self: SecurityAlgorithmSuite) -> int """
        ...

    @property
    def DefaultSignatureKeyDerivationLength(self) -> int:
        """ Get: DefaultSignatureKeyDerivationLength(self: SecurityAlgorithmSuite) -> int """
        ...

    @property
    def DefaultSymmetricKeyLength(self) -> int:
        """ Get: DefaultSymmetricKeyLength(self: SecurityAlgorithmSuite) -> int """
        ...

    @property
    def DefaultSymmetricKeyWrapAlgorithm(self) -> str:
        """ Get: DefaultSymmetricKeyWrapAlgorithm(self: SecurityAlgorithmSuite) -> str """
        ...

    @property
    def DefaultSymmetricSignatureAlgorithm(self) -> str:
        """ Get: DefaultSymmetricSignatureAlgorithm(self: SecurityAlgorithmSuite) -> str """
        ...

    @property
    def TripleDes(self) -> SecurityAlgorithmSuite:
        """ Get: TripleDes() -> SecurityAlgorithmSuite """
        ...

    @property
    def TripleDesRsa15(self) -> SecurityAlgorithmSuite:
        """ Get: TripleDesRsa15() -> SecurityAlgorithmSuite """
        ...

    @property
    def TripleDesSha256(self) -> SecurityAlgorithmSuite:
        """ Get: TripleDesSha256() -> SecurityAlgorithmSuite """
        ...

    @property
    def TripleDesSha256Rsa15(self) -> SecurityAlgorithmSuite:
        """ Get: TripleDesSha256Rsa15() -> SecurityAlgorithmSuite """
        ...


    def IsAsymmetricKeyLengthSupported(self, length:int) -> bool:
        """ IsAsymmetricKeyLengthSupported(self: SecurityAlgorithmSuite, length: int) -> bool """
        ...

    def IsAsymmetricKeyWrapAlgorithmSupported(self, algorithm:str) -> bool:
        """ IsAsymmetricKeyWrapAlgorithmSupported(self: SecurityAlgorithmSuite, algorithm: str) -> bool """
        ...

    def IsAsymmetricSignatureAlgorithmSupported(self, algorithm:str) -> bool:
        """ IsAsymmetricSignatureAlgorithmSupported(self: SecurityAlgorithmSuite, algorithm: str) -> bool """
        ...

    def IsCanonicalizationAlgorithmSupported(self, algorithm:str) -> bool:
        """ IsCanonicalizationAlgorithmSupported(self: SecurityAlgorithmSuite, algorithm: str) -> bool """
        ...

    def IsDigestAlgorithmSupported(self, algorithm:str) -> bool:
        """ IsDigestAlgorithmSupported(self: SecurityAlgorithmSuite, algorithm: str) -> bool """
        ...

    def IsEncryptionAlgorithmSupported(self, algorithm:str) -> bool:
        """ IsEncryptionAlgorithmSupported(self: SecurityAlgorithmSuite, algorithm: str) -> bool """
        ...

    def IsEncryptionKeyDerivationAlgorithmSupported(self, algorithm:str) -> bool:
        """ IsEncryptionKeyDerivationAlgorithmSupported(self: SecurityAlgorithmSuite, algorithm: str) -> bool """
        ...

    def IsSignatureKeyDerivationAlgorithmSupported(self, algorithm:str) -> bool:
        """ IsSignatureKeyDerivationAlgorithmSupported(self: SecurityAlgorithmSuite, algorithm: str) -> bool """
        ...

    def IsSymmetricKeyLengthSupported(self, length:int) -> bool:
        """ IsSymmetricKeyLengthSupported(self: SecurityAlgorithmSuite, length: int) -> bool """
        ...

    def IsSymmetricKeyWrapAlgorithmSupported(self, algorithm:str) -> bool:
        """ IsSymmetricKeyWrapAlgorithmSupported(self: SecurityAlgorithmSuite, algorithm: str) -> bool """
        ...

    def IsSymmetricSignatureAlgorithmSupported(self, algorithm:str) -> bool:
        """ IsSymmetricSignatureAlgorithmSupported(self: SecurityAlgorithmSuite, algorithm: str) -> bool """
        ...



class Basic128SecurityAlgorithmSuite(SecurityAlgorithmSuite): # skipped bases: <type 'object'>
    """ Basic128SecurityAlgorithmSuite() """
    def ToString(self) -> str:
        """ ToString(self: Basic128SecurityAlgorithmSuite) -> str """
        ...


class Basic192SecurityAlgorithmSuite(SecurityAlgorithmSuite): # skipped bases: <type 'object'>
    """ Basic192SecurityAlgorithmSuite() """
    def ToString(self) -> str:
        """ ToString(self: Basic192SecurityAlgorithmSuite) -> str """
        ...


class Basic256SecurityAlgorithmSuite(SecurityAlgorithmSuite): # skipped bases: <type 'object'>
    """ Basic256SecurityAlgorithmSuite() """
    def ToString(self) -> str:
        """ ToString(self: Basic256SecurityAlgorithmSuite) -> str """
        ...


class BasicSecurityProfileVersion: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BasicSecurityProfile10(self) -> BasicSecurityProfileVersion:
        """ Get: BasicSecurityProfile10() -> BasicSecurityProfileVersion """
        ...




class BinarySecretKeyIdentifierClause(BinaryKeyIdentifierClause): # skipped bases: <type 'object'>
    """
    BinarySecretKeyIdentifierClause(key: Array[Byte])
    BinarySecretKeyIdentifierClause(key: Array[Byte], cloneBuffer: bool)
    BinarySecretKeyIdentifierClause(key: Array[Byte], cloneBuffer: bool, derivationNonce: Array[Byte], derivationLength: int)
    """
    @property
    def CanCreateKey(self) -> bool:
        """ Get: CanCreateKey(self: BinarySecretKeyIdentifierClause) -> bool """
        ...


    def CreateKey(self) -> SecurityKey:
        """ CreateKey(self: BinarySecretKeyIdentifierClause) -> SecurityKey """
        ...

    def GetKeyBytes(self) -> Array:
        """ GetKeyBytes(self: BinarySecretKeyIdentifierClause) -> Array[Byte] """
        ...


class ChannelProtectionRequirements: # skipped bases: <type 'object'>, <type 'object'>
    """
    ChannelProtectionRequirements()
    ChannelProtectionRequirements(other: ChannelProtectionRequirements)
    """
    @property
    def IncomingEncryptionParts(self) -> ScopedMessagePartSpecification:
        """ Get: IncomingEncryptionParts(self: ChannelProtectionRequirements) -> ScopedMessagePartSpecification """
        ...

    @property
    def IncomingSignatureParts(self) -> ScopedMessagePartSpecification:
        """ Get: IncomingSignatureParts(self: ChannelProtectionRequirements) -> ScopedMessagePartSpecification """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ChannelProtectionRequirements) -> bool """
        ...

    @property
    def OutgoingEncryptionParts(self) -> ScopedMessagePartSpecification:
        """ Get: OutgoingEncryptionParts(self: ChannelProtectionRequirements) -> ScopedMessagePartSpecification """
        ...

    @property
    def OutgoingSignatureParts(self) -> ScopedMessagePartSpecification:
        """ Get: OutgoingSignatureParts(self: ChannelProtectionRequirements) -> ScopedMessagePartSpecification """
        ...


    def Add(self, protectionRequirements:ChannelProtectionRequirements, channelScopeOnly:bool = ...): # -> 
        """ Add(self: ChannelProtectionRequirements, protectionRequirements: ChannelProtectionRequirements, channelScopeOnly: bool)Add(self: ChannelProtectionRequirements, protectionRequirements: ChannelProtectionRequirements) """
        ...

    def CreateInverse(self) -> ChannelProtectionRequirements:
        """ CreateInverse(self: ChannelProtectionRequirements) -> ChannelProtectionRequirements """
        ...

    def MakeReadOnly(self): # -> 
        """ MakeReadOnly(self: ChannelProtectionRequirements) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...


class SecurityStateEncoder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def DecodeSecurityState(self, *args): #cannot find CLR method
        """ DecodeSecurityState(self: SecurityStateEncoder, data: Array[Byte]) -> Array[Byte] """
        ...

    def EncodeSecurityState(self, *args): #cannot find CLR method
        """ EncodeSecurityState(self: SecurityStateEncoder, data: Array[Byte]) -> Array[Byte] """
        ...


class DataProtectionSecurityStateEncoder(SecurityStateEncoder): # skipped bases: <type 'object'>
    """
    DataProtectionSecurityStateEncoder()
    DataProtectionSecurityStateEncoder(useCurrentUserProtectionScope: bool)
    DataProtectionSecurityStateEncoder(useCurrentUserProtectionScope: bool, entropy: Array[Byte])
    """
    @property
    def UseCurrentUserProtectionScope(self) -> bool:
        """ Get: UseCurrentUserProtectionScope(self: DataProtectionSecurityStateEncoder) -> bool """
        ...


    def GetEntropy(self) -> Array:
        """ GetEntropy(self: DataProtectionSecurityStateEncoder) -> Array[Byte] """
        ...

    def ToString(self) -> str:
        """ ToString(self: DataProtectionSecurityStateEncoder) -> str """
        ...

    def __new__(cls, useCurrentUserProtectionScope:bool = ..., entropy:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, useCurrentUserProtectionScope: bool)
        __new__(cls: type, useCurrentUserProtectionScope: bool, entropy: Array[Byte])
        """
        ...


class DispatchContext: # skipped bases: <type 'object'>, <type 'object'>
    """ DispatchContext() """
    @property
    def Principal(self) -> ClaimsPrincipal:
        """
        Get: Principal(self: DispatchContext) -> ClaimsPrincipal
        Set: Principal(self: DispatchContext) = value
        """
        ...

    @property
    def RequestAction(self) -> str:
        """
        Get: RequestAction(self: DispatchContext) -> str
        Set: RequestAction(self: DispatchContext) = value
        """
        ...

    @property
    def RequestMessage(self) -> WSTrustMessage:
        """
        Get: RequestMessage(self: DispatchContext) -> WSTrustMessage
        Set: RequestMessage(self: DispatchContext) = value
        """
        ...

    @property
    def ResponseAction(self) -> str:
        """
        Get: ResponseAction(self: DispatchContext) -> str
        Set: ResponseAction(self: DispatchContext) = value
        """
        ...

    @property
    def ResponseMessage(self) -> RequestSecurityTokenResponse:
        """
        Get: ResponseMessage(self: DispatchContext) -> RequestSecurityTokenResponse
        Set: ResponseMessage(self: DispatchContext) = value
        """
        ...

    @property
    def SecurityTokenService(self) -> SecurityTokenService:
        """
        Get: SecurityTokenService(self: DispatchContext) -> SecurityTokenService
        Set: SecurityTokenService(self: DispatchContext) = value
        """
        ...

    @property
    def TrustNamespace(self) -> str:
        """
        Get: TrustNamespace(self: DispatchContext) -> str
        Set: TrustNamespace(self: DispatchContext) = value
        """
        ...



class MessageSecurityException(CommunicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MessageSecurityException()
    MessageSecurityException(message: str)
    MessageSecurityException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ExpiredSecurityTokenException(MessageSecurityException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ExpiredSecurityTokenException()
    ExpiredSecurityTokenException(message: str)
    ExpiredSecurityTokenException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class HttpDigestClientCredential: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AllowedImpersonationLevel(self) -> TokenImpersonationLevel:
        """
        Get: AllowedImpersonationLevel(self: HttpDigestClientCredential) -> TokenImpersonationLevel
        Set: AllowedImpersonationLevel(self: HttpDigestClientCredential) = value
        """
        ...

    @property
    def ClientCredential(self) -> NetworkCredential:
        """
        Get: ClientCredential(self: HttpDigestClientCredential) -> NetworkCredential
        Set: ClientCredential(self: HttpDigestClientCredential) = value
        """
        ...



class IdentityVerifier: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CheckAccess(self, identity:EndpointIdentity, authContext:AuthorizationContext) -> bool:
        """ CheckAccess(self: IdentityVerifier, identity: EndpointIdentity, authContext: AuthorizationContext) -> bool """
        ...

    @staticmethod
    def CreateDefault() -> IdentityVerifier:
        """ CreateDefault() -> IdentityVerifier """
        ...

    def TryGetIdentity(self, reference, identity) -> Tuple_[bool, EndpointIdentity]:
        """ TryGetIdentity(self: IdentityVerifier, reference: EndpointAddress) -> (bool, EndpointIdentity) """
        ...


class IEndpointIdentityProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetIdentityOfSelf(self, tokenRequirement:SecurityTokenRequirement) -> EndpointIdentity:
        """ GetIdentityOfSelf(self: IEndpointIdentityProvider, tokenRequirement: SecurityTokenRequirement) -> EndpointIdentity """
        ...


class ImpersonateOnSerializingReplyMessageProperty(IMessageProperty): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name() -> str """
        ...


    def StartImpersonation(self, impersonationContext, originalPrincipal, isThreadPrincipalSet) -> Tuple_[IDisposable, IPrincipal, bool]:
        """ StartImpersonation(self: ImpersonateOnSerializingReplyMessageProperty) -> (IDisposable, IPrincipal, bool) """
        ...

    def StopImpersonation(self, impersonationContext:IDisposable, originalPrincipal:IPrincipal, isThreadPrincipalSet:bool): # -> 
        """ StopImpersonation(self: ImpersonateOnSerializingReplyMessageProperty, impersonationContext: IDisposable, originalPrincipal: IPrincipal, isThreadPrincipalSet: bool) """
        ...

    @staticmethod
    def TryGet(*__args:Message) -> Tuple_[bool, ImpersonateOnSerializingReplyMessageProperty]:
        """
        TryGet(message: Message) -> (bool, ImpersonateOnSerializingReplyMessageProperty)
        TryGet(properties: MessageProperties) -> (bool, ImpersonateOnSerializingReplyMessageProperty)
        """
        ...



class InfocardInteractiveChannelInitializer(IInteractiveChannelInitializer): # skipped bases: <type 'object'>
    """ InfocardInteractiveChannelInitializer(credentials: ClientCredentials, binding: Binding) """
    @property
    def Binding(self) -> Binding:
        """ Get: Binding(self: InfocardInteractiveChannelInitializer) -> Binding """
        ...



class ISecuritySession(ISession): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RemoteIdentity(self) -> EndpointIdentity:
        """ Get: RemoteIdentity(self: ISecuritySession) -> EndpointIdentity """
        ...



class ISecureConversationSession(ISecuritySession): # skipped bases: <type 'ISession'>, <type 'object'>
    """ no doc """
    def TryReadSessionTokenIdentifier(self, reader:XmlReader) -> bool:
        """ TryReadSessionTokenIdentifier(self: ISecureConversationSession, reader: XmlReader) -> bool """
        ...

    def WriteSessionTokenIdentifier(self, writer:XmlDictionaryWriter): # -> 
        """ WriteSessionTokenIdentifier(self: ISecureConversationSession, writer: XmlDictionaryWriter) """
        ...


class IssuedTokenClientCredential: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CacheIssuedTokens(self) -> bool:
        """
        Get: CacheIssuedTokens(self: IssuedTokenClientCredential) -> bool
        Set: CacheIssuedTokens(self: IssuedTokenClientCredential) = value
        """
        ...

    @property
    def DefaultKeyEntropyMode(self) -> SecurityKeyEntropyMode:
        """
        Get: DefaultKeyEntropyMode(self: IssuedTokenClientCredential) -> SecurityKeyEntropyMode
        Set: DefaultKeyEntropyMode(self: IssuedTokenClientCredential) = value
        """
        ...

    @property
    def IssuedTokenRenewalThresholdPercentage(self) -> int:
        """
        Get: IssuedTokenRenewalThresholdPercentage(self: IssuedTokenClientCredential) -> int
        Set: IssuedTokenRenewalThresholdPercentage(self: IssuedTokenClientCredential) = value
        """
        ...

    @property
    def IssuerChannelBehaviors(self) -> Dictionary:
        """ Get: IssuerChannelBehaviors(self: IssuedTokenClientCredential) -> Dictionary[Uri, KeyedByTypeCollection[IEndpointBehavior]] """
        ...

    @property
    def LocalIssuerAddress(self) -> EndpointAddress:
        """
        Get: LocalIssuerAddress(self: IssuedTokenClientCredential) -> EndpointAddress
        Set: LocalIssuerAddress(self: IssuedTokenClientCredential) = value
        """
        ...

    @property
    def LocalIssuerBinding(self) -> Binding:
        """
        Get: LocalIssuerBinding(self: IssuedTokenClientCredential) -> Binding
        Set: LocalIssuerBinding(self: IssuedTokenClientCredential) = value
        """
        ...

    @property
    def LocalIssuerChannelBehaviors(self) -> KeyedByTypeCollection:
        """ Get: LocalIssuerChannelBehaviors(self: IssuedTokenClientCredential) -> KeyedByTypeCollection[IEndpointBehavior] """
        ...

    @property
    def MaxIssuedTokenCachingTime(self) -> TimeSpan:
        """
        Get: MaxIssuedTokenCachingTime(self: IssuedTokenClientCredential) -> TimeSpan
        Set: MaxIssuedTokenCachingTime(self: IssuedTokenClientCredential) = value
        """
        ...



class IssuedTokenServiceCredential: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AllowedAudienceUris(self) -> IList:
        """ Get: AllowedAudienceUris(self: IssuedTokenServiceCredential) -> IList[str] """
        ...

    @property
    def AllowUntrustedRsaIssuers(self) -> bool:
        """
        Get: AllowUntrustedRsaIssuers(self: IssuedTokenServiceCredential) -> bool
        Set: AllowUntrustedRsaIssuers(self: IssuedTokenServiceCredential) = value
        """
        ...

    @property
    def AudienceUriMode(self) -> AudienceUriMode:
        """
        Get: AudienceUriMode(self: IssuedTokenServiceCredential) -> AudienceUriMode
        Set: AudienceUriMode(self: IssuedTokenServiceCredential) = value
        """
        ...

    @property
    def CertificateValidationMode(self): # -> X509CertificateValidationMode
        """
        Get: CertificateValidationMode(self: IssuedTokenServiceCredential) -> X509CertificateValidationMode
        Set: CertificateValidationMode(self: IssuedTokenServiceCredential) = value
        """
        ...

    @property
    def CustomCertificateValidator(self) -> X509CertificateValidator:
        """
        Get: CustomCertificateValidator(self: IssuedTokenServiceCredential) -> X509CertificateValidator
        Set: CustomCertificateValidator(self: IssuedTokenServiceCredential) = value
        """
        ...

    @property
    def KnownCertificates(self) -> IList:
        """ Get: KnownCertificates(self: IssuedTokenServiceCredential) -> IList[X509Certificate2] """
        ...

    @property
    def RevocationMode(self) -> X509RevocationMode:
        """
        Get: RevocationMode(self: IssuedTokenServiceCredential) -> X509RevocationMode
        Set: RevocationMode(self: IssuedTokenServiceCredential) = value
        """
        ...

    @property
    def SamlSerializer(self) -> SamlSerializer:
        """
        Get: SamlSerializer(self: IssuedTokenServiceCredential) -> SamlSerializer
        Set: SamlSerializer(self: IssuedTokenServiceCredential) = value
        """
        ...

    @property
    def TrustedStoreLocation(self) -> StoreLocation:
        """
        Get: TrustedStoreLocation(self: IssuedTokenServiceCredential) -> StoreLocation
        Set: TrustedStoreLocation(self: IssuedTokenServiceCredential) = value
        """
        ...



class IWSTrust13AsyncContract: # skipped bases: <type 'object'>
    """ no doc """
    def BeginTrust13Cancel(self, request:Message, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTrust13Cancel(self: IWSTrust13AsyncContract, request: Message, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTrust13CancelResponse(self, request:Message, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTrust13CancelResponse(self: IWSTrust13AsyncContract, request: Message, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTrust13Issue(self, request:Message, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTrust13Issue(self: IWSTrust13AsyncContract, request: Message, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTrust13IssueResponse(self, request:Message, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTrust13IssueResponse(self: IWSTrust13AsyncContract, request: Message, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTrust13Renew(self, request:Message, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTrust13Renew(self: IWSTrust13AsyncContract, request: Message, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTrust13RenewResponse(self, request:Message, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTrust13RenewResponse(self: IWSTrust13AsyncContract, request: Message, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTrust13Validate(self, request:Message, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTrust13Validate(self: IWSTrust13AsyncContract, request: Message, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTrust13ValidateResponse(self, request:Message, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTrust13ValidateResponse(self: IWSTrust13AsyncContract, request: Message, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndTrust13Cancel(self, ar:IAsyncResult) -> Message:
        """ EndTrust13Cancel(self: IWSTrust13AsyncContract, ar: IAsyncResult) -> Message """
        ...

    def EndTrust13CancelResponse(self, ar:IAsyncResult) -> Message:
        """ EndTrust13CancelResponse(self: IWSTrust13AsyncContract, ar: IAsyncResult) -> Message """
        ...

    def EndTrust13Issue(self, ar:IAsyncResult) -> Message:
        """ EndTrust13Issue(self: IWSTrust13AsyncContract, ar: IAsyncResult) -> Message """
        ...

    def EndTrust13IssueResponse(self, ar:IAsyncResult) -> Message:
        """ EndTrust13IssueResponse(self: IWSTrust13AsyncContract, ar: IAsyncResult) -> Message """
        ...

    def EndTrust13Renew(self, ar:IAsyncResult) -> Message:
        """ EndTrust13Renew(self: IWSTrust13AsyncContract, ar: IAsyncResult) -> Message """
        ...

    def EndTrust13RenewResponse(self, ar:IAsyncResult) -> Message:
        """ EndTrust13RenewResponse(self: IWSTrust13AsyncContract, ar: IAsyncResult) -> Message """
        ...

    def EndTrust13Validate(self, ar:IAsyncResult) -> Message:
        """ EndTrust13Validate(self: IWSTrust13AsyncContract, ar: IAsyncResult) -> Message """
        ...

    def EndTrust13ValidateResponse(self, ar:IAsyncResult) -> Message:
        """ EndTrust13ValidateResponse(self: IWSTrust13AsyncContract, ar: IAsyncResult) -> Message """
        ...


class IWSTrust13SyncContract: # skipped bases: <type 'object'>
    """ no doc """
    def ProcessTrust13Cancel(self, message:Message) -> Message:
        """ ProcessTrust13Cancel(self: IWSTrust13SyncContract, message: Message) -> Message """
        ...

    def ProcessTrust13CancelResponse(self, message:Message) -> Message:
        """ ProcessTrust13CancelResponse(self: IWSTrust13SyncContract, message: Message) -> Message """
        ...

    def ProcessTrust13Issue(self, message:Message) -> Message:
        """ ProcessTrust13Issue(self: IWSTrust13SyncContract, message: Message) -> Message """
        ...

    def ProcessTrust13IssueResponse(self, message:Message) -> Message:
        """ ProcessTrust13IssueResponse(self: IWSTrust13SyncContract, message: Message) -> Message """
        ...

    def ProcessTrust13Renew(self, message:Message) -> Message:
        """ ProcessTrust13Renew(self: IWSTrust13SyncContract, message: Message) -> Message """
        ...

    def ProcessTrust13RenewResponse(self, message:Message) -> Message:
        """ ProcessTrust13RenewResponse(self: IWSTrust13SyncContract, message: Message) -> Message """
        ...

    def ProcessTrust13Validate(self, message:Message) -> Message:
        """ ProcessTrust13Validate(self: IWSTrust13SyncContract, message: Message) -> Message """
        ...

    def ProcessTrust13ValidateResponse(self, message:Message) -> Message:
        """ ProcessTrust13ValidateResponse(self: IWSTrust13SyncContract, message: Message) -> Message """
        ...


class IWSTrustContract: # skipped bases: <type 'object'>
    """ no doc """
    def BeginCancel(self, message:Message, callback:AsyncCallback, asyncState:object) -> IAsyncResult:
        """ BeginCancel(self: IWSTrustContract, message: Message, callback: AsyncCallback, asyncState: object) -> IAsyncResult """
        ...

    def BeginIssue(self, message:Message, callback:AsyncCallback, asyncState:object) -> IAsyncResult:
        """ BeginIssue(self: IWSTrustContract, message: Message, callback: AsyncCallback, asyncState: object) -> IAsyncResult """
        ...

    def BeginRenew(self, message:Message, callback:AsyncCallback, asyncState:object) -> IAsyncResult:
        """ BeginRenew(self: IWSTrustContract, message: Message, callback: AsyncCallback, asyncState: object) -> IAsyncResult """
        ...

    def BeginValidate(self, message:Message, callback:AsyncCallback, asyncState:object) -> IAsyncResult:
        """ BeginValidate(self: IWSTrustContract, message: Message, callback: AsyncCallback, asyncState: object) -> IAsyncResult """
        ...

    def Cancel(self, message:Message) -> Message:
        """ Cancel(self: IWSTrustContract, message: Message) -> Message """
        ...

    def EndCancel(self, asyncResult:IAsyncResult) -> Message:
        """ EndCancel(self: IWSTrustContract, asyncResult: IAsyncResult) -> Message """
        ...

    def EndIssue(self, asyncResult:IAsyncResult) -> Message:
        """ EndIssue(self: IWSTrustContract, asyncResult: IAsyncResult) -> Message """
        ...

    def EndRenew(self, asyncResult:IAsyncResult) -> Message:
        """ EndRenew(self: IWSTrustContract, asyncResult: IAsyncResult) -> Message """
        ...

    def EndValidate(self, asyncResult:IAsyncResult) -> Message:
        """ EndValidate(self: IWSTrustContract, asyncResult: IAsyncResult) -> Message """
        ...

    def Issue(self, message:Message) -> Message:
        """ Issue(self: IWSTrustContract, message: Message) -> Message """
        ...

    def Renew(self, message:Message) -> Message:
        """ Renew(self: IWSTrustContract, message: Message) -> Message """
        ...

    def Validate(self, message:Message) -> Message:
        """ Validate(self: IWSTrustContract, message: Message) -> Message """
        ...


class IWSTrustChannelContract(IWSTrustContract): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IWSTrustFeb2005AsyncContract: # skipped bases: <type 'object'>
    """ no doc """
    def BeginTrustFeb2005Cancel(self, request:Message, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTrustFeb2005Cancel(self: IWSTrustFeb2005AsyncContract, request: Message, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTrustFeb2005CancelResponse(self, request:Message, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTrustFeb2005CancelResponse(self: IWSTrustFeb2005AsyncContract, request: Message, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTrustFeb2005Issue(self, request:Message, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTrustFeb2005Issue(self: IWSTrustFeb2005AsyncContract, request: Message, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTrustFeb2005IssueResponse(self, request:Message, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTrustFeb2005IssueResponse(self: IWSTrustFeb2005AsyncContract, request: Message, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTrustFeb2005Renew(self, request:Message, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTrustFeb2005Renew(self: IWSTrustFeb2005AsyncContract, request: Message, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTrustFeb2005RenewResponse(self, request:Message, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTrustFeb2005RenewResponse(self: IWSTrustFeb2005AsyncContract, request: Message, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTrustFeb2005Validate(self, request:Message, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTrustFeb2005Validate(self: IWSTrustFeb2005AsyncContract, request: Message, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTrustFeb2005ValidateResponse(self, request:Message, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTrustFeb2005ValidateResponse(self: IWSTrustFeb2005AsyncContract, request: Message, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndTrustFeb2005Cancel(self, ar:IAsyncResult) -> Message:
        """ EndTrustFeb2005Cancel(self: IWSTrustFeb2005AsyncContract, ar: IAsyncResult) -> Message """
        ...

    def EndTrustFeb2005CancelResponse(self, ar:IAsyncResult) -> Message:
        """ EndTrustFeb2005CancelResponse(self: IWSTrustFeb2005AsyncContract, ar: IAsyncResult) -> Message """
        ...

    def EndTrustFeb2005Issue(self, ar:IAsyncResult) -> Message:
        """ EndTrustFeb2005Issue(self: IWSTrustFeb2005AsyncContract, ar: IAsyncResult) -> Message """
        ...

    def EndTrustFeb2005IssueResponse(self, ar:IAsyncResult) -> Message:
        """ EndTrustFeb2005IssueResponse(self: IWSTrustFeb2005AsyncContract, ar: IAsyncResult) -> Message """
        ...

    def EndTrustFeb2005Renew(self, ar:IAsyncResult) -> Message:
        """ EndTrustFeb2005Renew(self: IWSTrustFeb2005AsyncContract, ar: IAsyncResult) -> Message """
        ...

    def EndTrustFeb2005RenewResponse(self, ar:IAsyncResult) -> Message:
        """ EndTrustFeb2005RenewResponse(self: IWSTrustFeb2005AsyncContract, ar: IAsyncResult) -> Message """
        ...

    def EndTrustFeb2005Validate(self, ar:IAsyncResult) -> Message:
        """ EndTrustFeb2005Validate(self: IWSTrustFeb2005AsyncContract, ar: IAsyncResult) -> Message """
        ...

    def EndTrustFeb2005ValidateResponse(self, ar:IAsyncResult) -> Message:
        """ EndTrustFeb2005ValidateResponse(self: IWSTrustFeb2005AsyncContract, ar: IAsyncResult) -> Message """
        ...


class IWSTrustFeb2005SyncContract: # skipped bases: <type 'object'>
    """ no doc """
    def ProcessTrustFeb2005Cancel(self, message:Message) -> Message:
        """ ProcessTrustFeb2005Cancel(self: IWSTrustFeb2005SyncContract, message: Message) -> Message """
        ...

    def ProcessTrustFeb2005CancelResponse(self, message:Message) -> Message:
        """ ProcessTrustFeb2005CancelResponse(self: IWSTrustFeb2005SyncContract, message: Message) -> Message """
        ...

    def ProcessTrustFeb2005Issue(self, message:Message) -> Message:
        """ ProcessTrustFeb2005Issue(self: IWSTrustFeb2005SyncContract, message: Message) -> Message """
        ...

    def ProcessTrustFeb2005IssueResponse(self, message:Message) -> Message:
        """ ProcessTrustFeb2005IssueResponse(self: IWSTrustFeb2005SyncContract, message: Message) -> Message """
        ...

    def ProcessTrustFeb2005Renew(self, message:Message) -> Message:
        """ ProcessTrustFeb2005Renew(self: IWSTrustFeb2005SyncContract, message: Message) -> Message """
        ...

    def ProcessTrustFeb2005RenewResponse(self, message:Message) -> Message:
        """ ProcessTrustFeb2005RenewResponse(self: IWSTrustFeb2005SyncContract, message: Message) -> Message """
        ...

    def ProcessTrustFeb2005Validate(self, message:Message) -> Message:
        """ ProcessTrustFeb2005Validate(self: IWSTrustFeb2005SyncContract, message: Message) -> Message """
        ...

    def ProcessTrustFeb2005ValidateResponse(self, message:Message) -> Message:
        """ ProcessTrustFeb2005ValidateResponse(self: IWSTrustFeb2005SyncContract, message: Message) -> Message """
        ...


class KeyNameIdentifierClause(SecurityKeyIdentifierClause): # skipped bases: <type 'object'>
    """ KeyNameIdentifierClause(keyName: str) """
    @property
    def KeyName(self) -> str:
        """ Get: KeyName(self: KeyNameIdentifierClause) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: KeyNameIdentifierClause) -> str """
        ...


class MessagePartSpecification: # skipped bases: <type 'object'>, <type 'object'>
    """
    MessagePartSpecification()
    MessagePartSpecification(isBodyIncluded: bool)
    MessagePartSpecification(*headerTypes: Array[XmlQualifiedName])
    MessagePartSpecification(isBodyIncluded: bool, *headerTypes: Array[XmlQualifiedName])
    """
    @property
    def HeaderTypes(self) -> ICollection:
        """ Get: HeaderTypes(self: MessagePartSpecification) -> ICollection[XmlQualifiedName] """
        ...

    @property
    def IsBodyIncluded(self) -> bool:
        """
        Get: IsBodyIncluded(self: MessagePartSpecification) -> bool
        Set: IsBodyIncluded(self: MessagePartSpecification) = value
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: MessagePartSpecification) -> bool """
        ...

    @property
    def NoParts(self) -> MessagePartSpecification:
        """ Get: NoParts() -> MessagePartSpecification """
        ...


    def Clear(self): # -> 
        """ Clear(self: MessagePartSpecification) """
        ...

    def MakeReadOnly(self): # -> 
        """ MakeReadOnly(self: MessagePartSpecification) """
        ...

    def Union(self, specification:MessagePartSpecification): # -> 
        """ Union(self: MessagePartSpecification, specification: MessagePartSpecification) """
        ...



class MessageProtectionOrder(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MessageProtectionOrder, values: EncryptBeforeSign (2), SignBeforeEncrypt (0), SignBeforeEncryptAndEncryptSignature (1) """
    EncryptBeforeSign: MessageProtectionOrder = ...
    SignBeforeEncrypt: MessageProtectionOrder = ...
    SignBeforeEncryptAndEncryptSignature: MessageProtectionOrder = ...
    value__ = ...


class NonceCache: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CacheSize(self) -> int:
        """
        Get: CacheSize(self: NonceCache) -> int
        Set: CacheSize(self: NonceCache) = value
        """
        ...

    @property
    def CachingTimeSpan(self) -> TimeSpan:
        """
        Get: CachingTimeSpan(self: NonceCache) -> TimeSpan
        Set: CachingTimeSpan(self: NonceCache) = value
        """
        ...


    def CheckNonce(self, nonce:Array) -> bool:
        """ CheckNonce(self: NonceCache, nonce: Array[Byte]) -> bool """
        ...

    def TryAddNonce(self, nonce:Array) -> bool:
        """ TryAddNonce(self: NonceCache, nonce: Array[Byte]) -> bool """
        ...


class PeerCredential: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Certificate(self) -> X509Certificate2:
        """
        Get: Certificate(self: PeerCredential) -> X509Certificate2
        Set: Certificate(self: PeerCredential) = value
        """
        ...

    @property
    def MeshPassword(self) -> str:
        """
        Get: MeshPassword(self: PeerCredential) -> str
        Set: MeshPassword(self: PeerCredential) = value
        """
        ...

    @property
    def MessageSenderAuthentication(self) -> X509PeerCertificateAuthentication:
        """
        Get: MessageSenderAuthentication(self: PeerCredential) -> X509PeerCertificateAuthentication
        Set: MessageSenderAuthentication(self: PeerCredential) = value
        """
        ...

    @property
    def PeerAuthentication(self) -> X509PeerCertificateAuthentication:
        """
        Get: PeerAuthentication(self: PeerCredential) -> X509PeerCertificateAuthentication
        Set: PeerAuthentication(self: PeerCredential) = value
        """
        ...


    def SetCertificate(self, *__args): # -> 
        """ SetCertificate(self: PeerCredential, subjectName: str, storeLocation: StoreLocation, storeName: StoreName)SetCertificate(self: PeerCredential, storeLocation: StoreLocation, storeName: StoreName, findType: X509FindType, findValue: object) """
        ...


class ScopedMessagePartSpecification: # skipped bases: <type 'object'>, <type 'object'>
    """
    ScopedMessagePartSpecification()
    ScopedMessagePartSpecification(other: ScopedMessagePartSpecification)
    """
    @property
    def Actions(self) -> ICollection:
        """ Get: Actions(self: ScopedMessagePartSpecification) -> ICollection[str] """
        ...

    @property
    def ChannelParts(self) -> MessagePartSpecification:
        """ Get: ChannelParts(self: ScopedMessagePartSpecification) -> MessagePartSpecification """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ScopedMessagePartSpecification) -> bool """
        ...


    def AddParts(self, parts:MessagePartSpecification, action:str = ...): # -> 
        """ AddParts(self: ScopedMessagePartSpecification, parts: MessagePartSpecification)AddParts(self: ScopedMessagePartSpecification, parts: MessagePartSpecification, action: str) """
        ...

    def MakeReadOnly(self): # -> 
        """ MakeReadOnly(self: ScopedMessagePartSpecification) """
        ...

    def TryGetParts(self, action:str, *__args:bool) -> Tuple_[bool, MessagePartSpecification]:
        """
        TryGetParts(self: ScopedMessagePartSpecification, action: str, excludeChannelScope: bool) -> (bool, MessagePartSpecification)
        TryGetParts(self: ScopedMessagePartSpecification, action: str) -> (bool, MessagePartSpecification)
        """
        ...


class SecureConversationServiceCredential: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def SecurityContextClaimTypes(self) -> Collection:
        """ Get: SecurityContextClaimTypes(self: SecureConversationServiceCredential) -> Collection[Type] """
        ...

    @property
    def SecurityStateEncoder(self) -> SecurityStateEncoder:
        """
        Get: SecurityStateEncoder(self: SecureConversationServiceCredential) -> SecurityStateEncoder
        Set: SecurityStateEncoder(self: SecureConversationServiceCredential) = value
        """
        ...



class SecureConversationVersion: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Default(self) -> SecureConversationVersion:
        """ Get: Default() -> SecureConversationVersion """
        ...

    @property
    def Namespace(self) -> XmlDictionaryString:
        """ Get: Namespace(self: SecureConversationVersion) -> XmlDictionaryString """
        ...

    @property
    def Prefix(self) -> XmlDictionaryString:
        """ Get: Prefix(self: SecureConversationVersion) -> XmlDictionaryString """
        ...

    @property
    def WSSecureConversation13(self) -> SecureConversationVersion:
        """ Get: WSSecureConversation13() -> SecureConversationVersion """
        ...

    @property
    def WSSecureConversationFeb2005(self) -> SecureConversationVersion:
        """ Get: WSSecureConversationFeb2005() -> SecureConversationVersion """
        ...




class SecurityAccessDeniedException(CommunicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SecurityAccessDeniedException()
    SecurityAccessDeniedException(message: str)
    SecurityAccessDeniedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SecurityContextKeyIdentifierClause(SecurityKeyIdentifierClause): # skipped bases: <type 'object'>
    """
    SecurityContextKeyIdentifierClause(contextId: UniqueId)
    SecurityContextKeyIdentifierClause(contextId: UniqueId, generation: UniqueId)
    SecurityContextKeyIdentifierClause(contextId: UniqueId, generation: UniqueId, derivationNonce: Array[Byte], derivationLength: int)
    """
    @property
    def ContextId(self) -> UniqueId:
        """ Get: ContextId(self: SecurityContextKeyIdentifierClause) -> UniqueId """
        ...

    @property
    def Generation(self) -> UniqueId:
        """ Get: Generation(self: SecurityContextKeyIdentifierClause) -> UniqueId """
        ...


    def ToString(self) -> str:
        """ ToString(self: SecurityContextKeyIdentifierClause) -> str """
        ...


class SecurityCredentialsManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateSecurityTokenManager(self) -> SecurityTokenManager:
        """ CreateSecurityTokenManager(self: SecurityCredentialsManager) -> SecurityTokenManager """
        ...


class SecurityKeyEntropyMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SecurityKeyEntropyMode, values: ClientEntropy (0), CombinedEntropy (2), ServerEntropy (1) """
    ClientEntropy: SecurityKeyEntropyMode = ...
    CombinedEntropy: SecurityKeyEntropyMode = ...
    ServerEntropy: SecurityKeyEntropyMode = ...
    value__ = ...


class SecurityMessageProperty(IMessageProperty, IDisposable): # skipped bases: <type 'object'>
    """ SecurityMessageProperty() """
    @property
    def ExternalAuthorizationPolicies(self) -> ReadOnlyCollection:
        """
        Get: ExternalAuthorizationPolicies(self: SecurityMessageProperty) -> ReadOnlyCollection[IAuthorizationPolicy]
        Set: ExternalAuthorizationPolicies(self: SecurityMessageProperty) = value
        """
        ...

    @property
    def HasIncomingSupportingTokens(self) -> bool:
        """ Get: HasIncomingSupportingTokens(self: SecurityMessageProperty) -> bool """
        ...

    @property
    def IncomingSupportingTokens(self) -> Collection:
        """ Get: IncomingSupportingTokens(self: SecurityMessageProperty) -> Collection[SupportingTokenSpecification] """
        ...

    @property
    def InitiatorToken(self) -> SecurityTokenSpecification:
        """
        Get: InitiatorToken(self: SecurityMessageProperty) -> SecurityTokenSpecification
        Set: InitiatorToken(self: SecurityMessageProperty) = value
        """
        ...

    @property
    def OutgoingSupportingTokens(self) -> Collection:
        """ Get: OutgoingSupportingTokens(self: SecurityMessageProperty) -> Collection[SupportingTokenSpecification] """
        ...

    @property
    def ProtectionToken(self) -> SecurityTokenSpecification:
        """
        Get: ProtectionToken(self: SecurityMessageProperty) -> SecurityTokenSpecification
        Set: ProtectionToken(self: SecurityMessageProperty) = value
        """
        ...

    @property
    def RecipientToken(self) -> SecurityTokenSpecification:
        """
        Get: RecipientToken(self: SecurityMessageProperty) -> SecurityTokenSpecification
        Set: RecipientToken(self: SecurityMessageProperty) = value
        """
        ...

    @property
    def SenderIdPrefix(self) -> str:
        """
        Get: SenderIdPrefix(self: SecurityMessageProperty) -> str
        Set: SenderIdPrefix(self: SecurityMessageProperty) = value
        """
        ...

    @property
    def ServiceSecurityContext(self) -> ServiceSecurityContext:
        """
        Get: ServiceSecurityContext(self: SecurityMessageProperty) -> ServiceSecurityContext
        Set: ServiceSecurityContext(self: SecurityMessageProperty) = value
        """
        ...

    @property
    def TransportToken(self) -> SecurityTokenSpecification:
        """
        Get: TransportToken(self: SecurityMessageProperty) -> SecurityTokenSpecification
        Set: TransportToken(self: SecurityMessageProperty) = value
        """
        ...


    @staticmethod
    def GetOrCreate(message:Message) -> SecurityMessageProperty:
        """ GetOrCreate(message: Message) -> SecurityMessageProperty """
        ...


class SecurityNegotiationException(CommunicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SecurityNegotiationException()
    SecurityNegotiationException(message: str)
    SecurityNegotiationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SecurityPolicyVersion: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Namespace(self) -> str:
        """ Get: Namespace(self: SecurityPolicyVersion) -> str """
        ...

    @property
    def Prefix(self) -> str:
        """ Get: Prefix(self: SecurityPolicyVersion) -> str """
        ...

    @property
    def WSSecurityPolicy11(self) -> SecurityPolicyVersion:
        """ Get: WSSecurityPolicy11() -> SecurityPolicyVersion """
        ...

    @property
    def WSSecurityPolicy12(self) -> SecurityPolicyVersion:
        """ Get: WSSecurityPolicy12() -> SecurityPolicyVersion """
        ...




class SecurityTokenAttachmentMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SecurityTokenAttachmentMode, values: Endorsing (1), Signed (0), SignedEncrypted (3), SignedEndorsing (2) """
    Endorsing: SecurityTokenAttachmentMode = ...
    Signed: SecurityTokenAttachmentMode = ...
    SignedEncrypted: SecurityTokenAttachmentMode = ...
    SignedEndorsing: SecurityTokenAttachmentMode = ...
    value__ = ...


class SecurityTokenSpecification: # skipped bases: <type 'object'>, <type 'object'>
    """ SecurityTokenSpecification(token: SecurityToken, tokenPolicies: ReadOnlyCollection[IAuthorizationPolicy]) """
    @property
    def SecurityToken(self) -> SecurityToken:
        """ Get: SecurityToken(self: SecurityTokenSpecification) -> SecurityToken """
        ...

    @property
    def SecurityTokenPolicies(self) -> ReadOnlyCollection:
        """ Get: SecurityTokenPolicies(self: SecurityTokenSpecification) -> ReadOnlyCollection[IAuthorizationPolicy] """
        ...



class SecurityVersion: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def WSSecurity10(self) -> SecurityVersion:
        """ Get: WSSecurity10() -> SecurityVersion """
        ...

    @property
    def WSSecurity11(self) -> SecurityVersion:
        """ Get: WSSecurity11() -> SecurityVersion """
        ...




class ServiceCredentialsSecurityTokenManager(IEndpointIdentityProvider, SecurityTokenManager): # skipped bases: <type 'object'>
    """ ServiceCredentialsSecurityTokenManager(parent: ServiceCredentials) """
    @property
    def ServiceCredentials(self) -> ServiceCredentials:
        """ Get: ServiceCredentials(self: ServiceCredentialsSecurityTokenManager) -> ServiceCredentials """
        ...


    def CreateSecureConversationTokenAuthenticator(self, *args): #cannot find CLR method
        """ CreateSecureConversationTokenAuthenticator(self: ServiceCredentialsSecurityTokenManager, recipientRequirement: RecipientServiceModelSecurityTokenRequirement, preserveBootstrapTokens: bool) -> (SecurityTokenAuthenticator, SecurityTokenResolver) """
        ...

    def IsIssuedSecurityTokenRequirement(self, *args): #cannot find CLR method
        """ IsIssuedSecurityTokenRequirement(self: ServiceCredentialsSecurityTokenManager, requirement: SecurityTokenRequirement) -> bool """
        ...

    def __new__(cls, parent:ServiceCredentials) -> Self:
        """ __new__(cls: type, parent: ServiceCredentials) """
        ...


class SimpleSecurityTokenProvider(SecurityTokenProvider): # skipped bases: <type 'object'>
    """ SimpleSecurityTokenProvider(token: SecurityToken, tokenRequirement: SecurityTokenRequirement) """
    def __new__(cls, token:SecurityToken, tokenRequirement:SecurityTokenRequirement) -> Self:
        """ __new__(cls: type, token: SecurityToken, tokenRequirement: SecurityTokenRequirement) """
        ...


class SspiSecurityTokenProvider(SecurityTokenProvider): # skipped bases: <type 'object'>
    """
    SspiSecurityTokenProvider(credential: NetworkCredential, allowNtlm: bool, impersonationLevel: TokenImpersonationLevel)
    SspiSecurityTokenProvider(credential: NetworkCredential, extractGroupsForWindowsAccounts: bool, allowUnauthenticatedCallers: bool)
    """
    def __new__(cls, credential, *__args) -> Self:
        """
        __new__(cls: type, credential: NetworkCredential, allowNtlm: bool, impersonationLevel: TokenImpersonationLevel)
        __new__(cls: type, credential: NetworkCredential, extractGroupsForWindowsAccounts: bool, allowUnauthenticatedCallers: bool)
        """
        ...


class SupportingTokenSpecification(SecurityTokenSpecification): # skipped bases: <type 'object'>
    """
    SupportingTokenSpecification(token: SecurityToken, tokenPolicies: ReadOnlyCollection[IAuthorizationPolicy], attachmentMode: SecurityTokenAttachmentMode)
    SupportingTokenSpecification(token: SecurityToken, tokenPolicies: ReadOnlyCollection[IAuthorizationPolicy], attachmentMode: SecurityTokenAttachmentMode, tokenParameters: SecurityTokenParameters)
    """
    @property
    def SecurityTokenAttachmentMode(self) -> SecurityTokenAttachmentMode:
        """ Get: SecurityTokenAttachmentMode(self: SupportingTokenSpecification) -> SecurityTokenAttachmentMode """
        ...



class TripleDesSecurityAlgorithmSuite(SecurityAlgorithmSuite): # skipped bases: <type 'object'>
    """ TripleDesSecurityAlgorithmSuite() """
    def ToString(self) -> str:
        """ ToString(self: TripleDesSecurityAlgorithmSuite) -> str """
        ...


class TrustVersion: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Default(self) -> TrustVersion:
        """ Get: Default() -> TrustVersion """
        ...

    @property
    def Namespace(self) -> XmlDictionaryString:
        """ Get: Namespace(self: TrustVersion) -> XmlDictionaryString """
        ...

    @property
    def Prefix(self) -> XmlDictionaryString:
        """ Get: Prefix(self: TrustVersion) -> XmlDictionaryString """
        ...

    @property
    def WSTrust13(self) -> TrustVersion:
        """ Get: WSTrust13() -> TrustVersion """
        ...

    @property
    def WSTrustFeb2005(self) -> TrustVersion:
        """ Get: WSTrustFeb2005() -> TrustVersion """
        ...




class UserNamePasswordClientCredential: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Password(self) -> str:
        """
        Get: Password(self: UserNamePasswordClientCredential) -> str
        Set: Password(self: UserNamePasswordClientCredential) = value
        """
        ...

    @property
    def UserName(self) -> str:
        """
        Get: UserName(self: UserNamePasswordClientCredential) -> str
        Set: UserName(self: UserNamePasswordClientCredential) = value
        """
        ...



class UserNamePasswordServiceCredential: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CachedLogonTokenLifetime(self) -> TimeSpan:
        """
        Get: CachedLogonTokenLifetime(self: UserNamePasswordServiceCredential) -> TimeSpan
        Set: CachedLogonTokenLifetime(self: UserNamePasswordServiceCredential) = value
        """
        ...

    @property
    def CacheLogonTokens(self) -> bool:
        """
        Get: CacheLogonTokens(self: UserNamePasswordServiceCredential) -> bool
        Set: CacheLogonTokens(self: UserNamePasswordServiceCredential) = value
        """
        ...

    @property
    def CustomUserNamePasswordValidator(self) -> UserNamePasswordValidator:
        """
        Get: CustomUserNamePasswordValidator(self: UserNamePasswordServiceCredential) -> UserNamePasswordValidator
        Set: CustomUserNamePasswordValidator(self: UserNamePasswordServiceCredential) = value
        """
        ...

    @property
    def IncludeWindowsGroups(self) -> bool:
        """
        Get: IncludeWindowsGroups(self: UserNamePasswordServiceCredential) -> bool
        Set: IncludeWindowsGroups(self: UserNamePasswordServiceCredential) = value
        """
        ...

    @property
    def MaxCachedLogonTokens(self) -> int:
        """
        Get: MaxCachedLogonTokens(self: UserNamePasswordServiceCredential) -> int
        Set: MaxCachedLogonTokens(self: UserNamePasswordServiceCredential) = value
        """
        ...

    @property
    def MembershipProvider(self) -> MembershipProvider:
        """
        Get: MembershipProvider(self: UserNamePasswordServiceCredential) -> MembershipProvider
        Set: MembershipProvider(self: UserNamePasswordServiceCredential) = value
        """
        ...

    @property
    def UserNamePasswordValidationMode(self) -> UserNamePasswordValidationMode:
        """
        Get: UserNamePasswordValidationMode(self: UserNamePasswordServiceCredential) -> UserNamePasswordValidationMode
        Set: UserNamePasswordValidationMode(self: UserNamePasswordServiceCredential) = value
        """
        ...



class UserNamePasswordValidationMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UserNamePasswordValidationMode, values: Custom (2), MembershipProvider (1), Windows (0) """
    Custom: UserNamePasswordValidationMode = ...
    MembershipProvider: UserNamePasswordValidationMode = ...
    value__ = ...
    Windows: UserNamePasswordValidationMode = ...


class WindowsClientCredential: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AllowedImpersonationLevel(self) -> TokenImpersonationLevel:
        """
        Get: AllowedImpersonationLevel(self: WindowsClientCredential) -> TokenImpersonationLevel
        Set: AllowedImpersonationLevel(self: WindowsClientCredential) = value
        """
        ...

    @property
    def AllowNtlm(self) -> bool:
        """
        Get: AllowNtlm(self: WindowsClientCredential) -> bool
        Set: AllowNtlm(self: WindowsClientCredential) = value
        """
        ...

    @property
    def ClientCredential(self) -> NetworkCredential:
        """
        Get: ClientCredential(self: WindowsClientCredential) -> NetworkCredential
        Set: ClientCredential(self: WindowsClientCredential) = value
        """
        ...



class WindowsServiceCredential: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AllowAnonymousLogons(self) -> bool:
        """
        Get: AllowAnonymousLogons(self: WindowsServiceCredential) -> bool
        Set: AllowAnonymousLogons(self: WindowsServiceCredential) = value
        """
        ...

    @property
    def IncludeWindowsGroups(self) -> bool:
        """
        Get: IncludeWindowsGroups(self: WindowsServiceCredential) -> bool
        Set: IncludeWindowsGroups(self: WindowsServiceCredential) = value
        """
        ...



class WSSecurityTokenSerializer(SecurityTokenSerializer): # skipped bases: <type 'object'>
    """
    WSSecurityTokenSerializer()
    WSSecurityTokenSerializer(emitBspRequiredAttributes: bool)
    WSSecurityTokenSerializer(securityVersion: SecurityVersion)
    WSSecurityTokenSerializer(securityVersion: SecurityVersion, emitBspRequiredAttributes: bool)
    WSSecurityTokenSerializer(securityVersion: SecurityVersion, emitBspRequiredAttributes: bool, samlSerializer: SamlSerializer)
    WSSecurityTokenSerializer(securityVersion: SecurityVersion, emitBspRequiredAttributes: bool, samlSerializer: SamlSerializer, securityStateEncoder: SecurityStateEncoder, knownTypes: IEnumerable[Type])
    WSSecurityTokenSerializer(securityVersion: SecurityVersion, trustVersion: TrustVersion, secureConversationVersion: SecureConversationVersion, emitBspRequiredAttributes: bool, samlSerializer: SamlSerializer, securityStateEncoder: SecurityStateEncoder, knownTypes: IEnumerable[Type])
    WSSecurityTokenSerializer(securityVersion: SecurityVersion, emitBspRequiredAttributes: bool, samlSerializer: SamlSerializer, securityStateEncoder: SecurityStateEncoder, knownTypes: IEnumerable[Type], maximumKeyDerivationOffset: int, maximumKeyDerivationLabelLength: int, maximumKeyDerivationNonceLength: int)
    WSSecurityTokenSerializer(securityVersion: SecurityVersion, trustVersion: TrustVersion, secureConversationVersion: SecureConversationVersion, emitBspRequiredAttributes: bool, samlSerializer: SamlSerializer, securityStateEncoder: SecurityStateEncoder, knownTypes: IEnumerable[Type], maximumKeyDerivationOffset: int, maximumKeyDerivationLabelLength: int, maximumKeyDerivationNonceLength: int)
    """
    @property
    def DefaultInstance(self) -> WSSecurityTokenSerializer:
        """ Get: DefaultInstance() -> WSSecurityTokenSerializer """
        ...

    @property
    def EmitBspRequiredAttributes(self) -> bool:
        """ Get: EmitBspRequiredAttributes(self: WSSecurityTokenSerializer) -> bool """
        ...

    @property
    def MaximumKeyDerivationLabelLength(self) -> int:
        """ Get: MaximumKeyDerivationLabelLength(self: WSSecurityTokenSerializer) -> int """
        ...

    @property
    def MaximumKeyDerivationNonceLength(self) -> int:
        """ Get: MaximumKeyDerivationNonceLength(self: WSSecurityTokenSerializer) -> int """
        ...

    @property
    def MaximumKeyDerivationOffset(self) -> int:
        """ Get: MaximumKeyDerivationOffset(self: WSSecurityTokenSerializer) -> int """
        ...

    @property
    def SecurityVersion(self) -> SecurityVersion:
        """ Get: SecurityVersion(self: WSSecurityTokenSerializer) -> SecurityVersion """
        ...


    def CreateKeyIdentifierClauseFromTokenXml(self, element:XmlElement, tokenReferenceStyle:SecurityTokenReferenceStyle) -> SecurityKeyIdentifierClause:
        """ CreateKeyIdentifierClauseFromTokenXml(self: WSSecurityTokenSerializer, element: XmlElement, tokenReferenceStyle: SecurityTokenReferenceStyle) -> SecurityKeyIdentifierClause """
        ...

    def GetTokenTypeUri(self, *args): #cannot find CLR method
        """ GetTokenTypeUri(self: WSSecurityTokenSerializer, tokenType: Type) -> str """
        ...

    def TryCreateKeyIdentifierClauseFromTokenXml(self, element, tokenReferenceStyle, securityKeyIdentifierClause) -> Tuple_[bool, SecurityKeyIdentifierClause]:
        """ TryCreateKeyIdentifierClauseFromTokenXml(self: WSSecurityTokenSerializer, element: XmlElement, tokenReferenceStyle: SecurityTokenReferenceStyle) -> (bool, SecurityKeyIdentifierClause) """
        ...

    def __new__(cls, *__args:bool) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, emitBspRequiredAttributes: bool)
        __new__(cls: type, securityVersion: SecurityVersion)
        __new__(cls: type, securityVersion: SecurityVersion, emitBspRequiredAttributes: bool)
        __new__(cls: type, securityVersion: SecurityVersion, emitBspRequiredAttributes: bool, samlSerializer: SamlSerializer)
        __new__(cls: type, securityVersion: SecurityVersion, emitBspRequiredAttributes: bool, samlSerializer: SamlSerializer, securityStateEncoder: SecurityStateEncoder, knownTypes: IEnumerable[Type])
        __new__(cls: type, securityVersion: SecurityVersion, trustVersion: TrustVersion, secureConversationVersion: SecureConversationVersion, emitBspRequiredAttributes: bool, samlSerializer: SamlSerializer, securityStateEncoder: SecurityStateEncoder, knownTypes: IEnumerable[Type])
        __new__(cls: type, securityVersion: SecurityVersion, emitBspRequiredAttributes: bool, samlSerializer: SamlSerializer, securityStateEncoder: SecurityStateEncoder, knownTypes: IEnumerable[Type], maximumKeyDerivationOffset: int, maximumKeyDerivationLabelLength: int, maximumKeyDerivationNonceLength: int)
        __new__(cls: type, securityVersion: SecurityVersion, trustVersion: TrustVersion, secureConversationVersion: SecureConversationVersion, emitBspRequiredAttributes: bool, samlSerializer: SamlSerializer, securityStateEncoder: SecurityStateEncoder, knownTypes: IEnumerable[Type], maximumKeyDerivationOffset: int, maximumKeyDerivationLabelLength: int, maximumKeyDerivationNonceLength: int)
        """
        ...



class WSTrustChannel(IWSTrustChannelContract, IChannel): # skipped bases: <type 'IWSTrustContract'>, <type 'ICommunicationObject'>, <type 'object'>
    """ WSTrustChannel(factory: WSTrustChannelFactory, inner: IWSTrustChannelContract, trustVersion: TrustVersion, context: WSTrustSerializationContext, requestSerializer: WSTrustRequestSerializer, responseSerializer: WSTrustResponseSerializer) """
    @property
    def Channel(self) -> IChannel:
        """ Get: Channel(self: WSTrustChannel) -> IChannel """
        ...

    @property
    def ChannelFactory(self) -> WSTrustChannelFactory:
        """ Get: ChannelFactory(self: WSTrustChannel) -> WSTrustChannelFactory """
        ...

    @property
    def Contract(self) -> IWSTrustChannelContract:
        """ Get: Contract(self: WSTrustChannel) -> IWSTrustChannelContract """
        ...

    @property
    def State(self) -> CommunicationState:
        """ Get: State(self: WSTrustChannel) -> CommunicationState """
        ...

    @property
    def TrustVersion(self) -> TrustVersion:
        """ Get: TrustVersion(self: WSTrustChannel) -> TrustVersion """
        ...

    @property
    def WSTrustRequestSerializer(self) -> WSTrustRequestSerializer:
        """ Get: WSTrustRequestSerializer(self: WSTrustChannel) -> WSTrustRequestSerializer """
        ...

    @property
    def WSTrustResponseSerializer(self) -> WSTrustResponseSerializer:
        """ Get: WSTrustResponseSerializer(self: WSTrustChannel) -> WSTrustResponseSerializer """
        ...

    @property
    def WSTrustSerializationContext(self) -> WSTrustSerializationContext:
        """ Get: WSTrustSerializationContext(self: WSTrustChannel) -> WSTrustSerializationContext """
        ...


    def Abort(self): # -> 
        """ Abort(self: WSTrustChannel) """
        ...

    def BeginClose(self, *__args) -> IAsyncResult:
        """
        BeginClose(self: WSTrustChannel, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginClose(self: WSTrustChannel, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginOpen(self, *__args) -> IAsyncResult:
        """
        BeginOpen(self: WSTrustChannel, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginOpen(self: WSTrustChannel, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def Close(self, timeout:TimeSpan = ...): # -> 
        """ Close(self: WSTrustChannel, timeout: TimeSpan)Close(self: WSTrustChannel) """
        ...

    def CreateRequest(self, *args): #cannot find CLR method
        """ CreateRequest(self: WSTrustChannel, request: RequestSecurityToken, requestType: str) -> Message """
        ...

    def EndClose(self, result:IAsyncResult): # -> 
        """ EndClose(self: WSTrustChannel, result: IAsyncResult) """
        ...

    def EndOpen(self, result:IAsyncResult): # -> 
        """ EndOpen(self: WSTrustChannel, result: IAsyncResult) """
        ...

    def GetRequestAction(self, *args): #cannot find CLR method
        """ GetRequestAction(requestType: str, trustVersion: TrustVersion) -> str """
        ...

    def GetTokenFromResponse(self, request:RequestSecurityToken, response:RequestSecurityTokenResponse) -> SecurityToken:
        """ GetTokenFromResponse(self: WSTrustChannel, request: RequestSecurityToken, response: RequestSecurityTokenResponse) -> SecurityToken """
        ...

    def Open(self, timeout:TimeSpan = ...): # -> 
        """ Open(self: WSTrustChannel, timeout: TimeSpan)Open(self: WSTrustChannel) """
        ...

    def ReadResponse(self, *args): #cannot find CLR method
        """ ReadResponse(self: WSTrustChannel, response: Message) -> RequestSecurityTokenResponse """
        ...

    Closed = ...
    Closing = ...
    Faulted = ...
    Opened = ...
    Opening = ...


class WSTrustChannelFactory(ChannelFactory): # skipped bases: <type 'IDisposable'>, <type 'IChannelFactory[IWSTrustChannelContract]'>, <type 'IChannelFactory'>, <type 'ICommunicationObject'>, <type 'object'>
    """
    WSTrustChannelFactory()
    WSTrustChannelFactory(endpointConfigurationName: str)
    WSTrustChannelFactory(binding: Binding)
    WSTrustChannelFactory(endpoint: ServiceEndpoint)
    WSTrustChannelFactory(endpointConfigurationName: str, remoteAddress: EndpointAddress)
    WSTrustChannelFactory(binding: Binding, remoteAddress: EndpointAddress)
    WSTrustChannelFactory(binding: Binding, remoteAddress: str)
    """
    @property
    def SecurityTokenHandlerCollectionManager(self) -> SecurityTokenHandlerCollectionManager:
        """
        Get: SecurityTokenHandlerCollectionManager(self: WSTrustChannelFactory) -> SecurityTokenHandlerCollectionManager
        Set: SecurityTokenHandlerCollectionManager(self: WSTrustChannelFactory) = value
        """
        ...

    @property
    def SecurityTokenResolver(self) -> SecurityTokenResolver:
        """
        Get: SecurityTokenResolver(self: WSTrustChannelFactory) -> SecurityTokenResolver
        Set: SecurityTokenResolver(self: WSTrustChannelFactory) = value
        """
        ...

    @property
    def TrustVersion(self) -> TrustVersion:
        """
        Get: TrustVersion(self: WSTrustChannelFactory) -> TrustVersion
        Set: TrustVersion(self: WSTrustChannelFactory) = value
        """
        ...

    @property
    def UseKeyTokenResolver(self) -> SecurityTokenResolver:
        """
        Get: UseKeyTokenResolver(self: WSTrustChannelFactory) -> SecurityTokenResolver
        Set: UseKeyTokenResolver(self: WSTrustChannelFactory) = value
        """
        ...

    @property
    def WSTrustRequestSerializer(self) -> WSTrustRequestSerializer:
        """
        Get: WSTrustRequestSerializer(self: WSTrustChannelFactory) -> WSTrustRequestSerializer
        Set: WSTrustRequestSerializer(self: WSTrustChannelFactory) = value
        """
        ...

    @property
    def WSTrustResponseSerializer(self) -> WSTrustResponseSerializer:
        """
        Get: WSTrustResponseSerializer(self: WSTrustChannelFactory) -> WSTrustResponseSerializer
        Set: WSTrustResponseSerializer(self: WSTrustChannelFactory) = value
        """
        ...


    def CreateSerializationContext(self, *args): #cannot find CLR method
        """ CreateSerializationContext(self: WSTrustChannelFactory) -> WSTrustSerializationContext """
        ...

    def CreateTrustChannel(self, *args): #cannot find CLR method
        """ CreateTrustChannel(self: WSTrustChannelFactory, innerChannel: IWSTrustChannelContract, trustVersion: TrustVersion, context: WSTrustSerializationContext, requestSerializer: WSTrustRequestSerializer, responseSerializer: WSTrustResponseSerializer) -> WSTrustChannel """
        ...


class WSTrustRequestBodyWriter(BodyWriter): # skipped bases: <type 'object'>
    """ WSTrustRequestBodyWriter(requestSecurityToken: RequestSecurityToken, serializer: WSTrustRequestSerializer, serializationContext: WSTrustSerializationContext) """
    pass

class WSTrustRequestProcessingErrorEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ WSTrustRequestProcessingErrorEventArgs(requestType: str, exception: Exception) """
    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: WSTrustRequestProcessingErrorEventArgs) -> Exception """
        ...

    @property
    def RequestType(self) -> str:
        """ Get: RequestType(self: WSTrustRequestProcessingErrorEventArgs) -> str """
        ...


    def __new__(cls, requestType:str, exception:Exception) -> Self:
        """ __new__(cls: type, requestType: str, exception: Exception) """
        ...


class WSTrustResponseBodyWriter(BodyWriter): # skipped bases: <type 'object'>
    """ WSTrustResponseBodyWriter(requestSecurityTokenResponse: RequestSecurityTokenResponse, serializer: WSTrustResponseSerializer, context: WSTrustSerializationContext) """
    pass

class WSTrustServiceContract(IWSTrustFeb2005SyncContract, IWSTrust13SyncContract, IWSTrust13AsyncContract, IWSTrustFeb2005AsyncContract, IWsdlExportExtension, IContractBehavior): # skipped bases: <type 'object'>
    """ WSTrustServiceContract(securityTokenServiceConfiguration: SecurityTokenServiceConfiguration) """
    @property
    def SecurityTokenServiceConfiguration(self) -> SecurityTokenServiceConfiguration:
        """ Get: SecurityTokenServiceConfiguration(self: WSTrustServiceContract) -> SecurityTokenServiceConfiguration """
        ...


    def BeginDispatchRequest(self, *args): #cannot find CLR method
        """ BeginDispatchRequest(self: WSTrustServiceContract, dispatchContext: DispatchContext, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult """
        ...

    def BeginProcessCore(self, *args): #cannot find CLR method
        """ BeginProcessCore(self: WSTrustServiceContract, requestMessage: Message, requestSerializer: WSTrustRequestSerializer, responseSerializer: WSTrustResponseSerializer, requestAction: str, responseAction: str, trustNamespace: str, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def CreateDispatchContext(self, *args): #cannot find CLR method
        """ CreateDispatchContext(self: WSTrustServiceContract, requestMessage: Message, requestAction: str, responseAction: str, trustNamespace: str, requestSerializer: WSTrustRequestSerializer, responseSerializer: WSTrustResponseSerializer, serializationContext: WSTrustSerializationContext) -> DispatchContext """
        ...

    def CreateSerializationContext(self, *args): #cannot find CLR method
        """ CreateSerializationContext(self: WSTrustServiceContract) -> WSTrustSerializationContext """
        ...

    def DispatchRequest(self, *args): #cannot find CLR method
        """ DispatchRequest(self: WSTrustServiceContract, dispatchContext: DispatchContext) """
        ...

    def EndDispatchRequest(self, *args): #cannot find CLR method
        """ EndDispatchRequest(self: WSTrustServiceContract, ar: IAsyncResult) -> DispatchContext """
        ...

    def EndProcessCore(self, *args): #cannot find CLR method
        """ EndProcessCore(self: WSTrustServiceContract, ar: IAsyncResult, requestAction: str, responseAction: str, trustNamespace: str) -> Message """
        ...

    def FixMessageElement(self, *args): #cannot find CLR method
        """ FixMessageElement(self: WSTrustServiceContract, serviceDescription: ServiceDescription, portType: PortType, context: WsdlEndpointConversionContext, operationName: str, inputMessageElement: XmlQualifiedName, outputMessageElement: XmlQualifiedName) """
        ...

    def GetRstSecurityTokenResolver(self, *args): #cannot find CLR method
        """ GetRstSecurityTokenResolver(self: WSTrustServiceContract) -> SecurityTokenResolver """
        ...

    def GetSecurityHeaderTokenResolver(self, *args): #cannot find CLR method
        """ GetSecurityHeaderTokenResolver(self: WSTrustServiceContract, requestContext: RequestContext) -> SecurityTokenResolver """
        ...

    def HandleException(self, *args): #cannot find CLR method
        """ HandleException(self: WSTrustServiceContract, ex: Exception, trustNamespace: str, action: str, requestEnvelopeVersion: EnvelopeVersion) -> bool """
        ...

    def ImportSchema(self, *args): #cannot find CLR method
        """ ImportSchema(self: WSTrustServiceContract, exporter: WsdlExporter, context: WsdlEndpointConversionContext, ns: str) """
        ...

    def IncludeNamespace(self, *args): #cannot find CLR method
        """ IncludeNamespace(self: WSTrustServiceContract, context: WsdlEndpointConversionContext, prefix: str, ns: str) """
        ...

    def ProcessCore(self, *args): #cannot find CLR method
        """ ProcessCore(self: WSTrustServiceContract, requestMessage: Message, requestSerializer: WSTrustRequestSerializer, responseSerializer: WSTrustResponseSerializer, requestAction: str, responseAction: str, trustNamespace: str) -> Message """
        ...

    def ValidateDispatchContext(self, *args): #cannot find CLR method
        """ ValidateDispatchContext(self: WSTrustServiceContract, dispatchContext: DispatchContext) """
        ...

    RequestFailed = ...


class WSTrustServiceHost(ServiceHost): # skipped bases: <type 'IDisposable'>, <type 'ICommunicationObject'>, <type 'IExtensibleObject[ServiceHostBase]'>, <type 'object'>
    """
    WSTrustServiceHost(securityTokenServiceConfiguration: SecurityTokenServiceConfiguration, *baseAddresses: Array[Uri])
    WSTrustServiceHost(serviceContract: WSTrustServiceContract, *baseAddresses: Array[Uri])
    """
    @property
    def SecurityTokenServiceConfiguration(self) -> SecurityTokenServiceConfiguration:
        """ Get: SecurityTokenServiceConfiguration(self: WSTrustServiceHost) -> SecurityTokenServiceConfiguration """
        ...

    @property
    def ServiceContract(self) -> WSTrustServiceContract:
        """ Get: ServiceContract(self: WSTrustServiceHost) -> WSTrustServiceContract """
        ...


    def ConfigureMetadata(self, *args): #cannot find CLR method
        """ ConfigureMetadata(self: WSTrustServiceHost) """
        ...

    def UpdateServiceConfiguration(self, *args): #cannot find CLR method
        """ UpdateServiceConfiguration(self: WSTrustServiceHost) """
        ...


class X509CertificateInitiatorClientCredential: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Certificate(self) -> X509Certificate2:
        """
        Get: Certificate(self: X509CertificateInitiatorClientCredential) -> X509Certificate2
        Set: Certificate(self: X509CertificateInitiatorClientCredential) = value
        """
        ...


    def SetCertificate(self, *__args): # -> 
        """ SetCertificate(self: X509CertificateInitiatorClientCredential, subjectName: str, storeLocation: StoreLocation, storeName: StoreName)SetCertificate(self: X509CertificateInitiatorClientCredential, storeLocation: StoreLocation, storeName: StoreName, findType: X509FindType, findValue: object) """
        ...


class X509CertificateInitiatorServiceCredential: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Authentication(self) -> X509ClientCertificateAuthentication:
        """ Get: Authentication(self: X509CertificateInitiatorServiceCredential) -> X509ClientCertificateAuthentication """
        ...

    @property
    def Certificate(self) -> X509Certificate2:
        """
        Get: Certificate(self: X509CertificateInitiatorServiceCredential) -> X509Certificate2
        Set: Certificate(self: X509CertificateInitiatorServiceCredential) = value
        """
        ...


    def SetCertificate(self, *__args): # -> 
        """ SetCertificate(self: X509CertificateInitiatorServiceCredential, subjectName: str, storeLocation: StoreLocation, storeName: StoreName)SetCertificate(self: X509CertificateInitiatorServiceCredential, storeLocation: StoreLocation, storeName: StoreName, findType: X509FindType, findValue: object) """
        ...


class X509CertificateRecipientClientCredential: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Authentication(self) -> X509ServiceCertificateAuthentication:
        """ Get: Authentication(self: X509CertificateRecipientClientCredential) -> X509ServiceCertificateAuthentication """
        ...

    @property
    def DefaultCertificate(self) -> X509Certificate2:
        """
        Get: DefaultCertificate(self: X509CertificateRecipientClientCredential) -> X509Certificate2
        Set: DefaultCertificate(self: X509CertificateRecipientClientCredential) = value
        """
        ...

    @property
    def ScopedCertificates(self) -> Dictionary:
        """ Get: ScopedCertificates(self: X509CertificateRecipientClientCredential) -> Dictionary[Uri, X509Certificate2] """
        ...

    @property
    def SslCertificateAuthentication(self) -> X509ServiceCertificateAuthentication:
        """
        Get: SslCertificateAuthentication(self: X509CertificateRecipientClientCredential) -> X509ServiceCertificateAuthentication
        Set: SslCertificateAuthentication(self: X509CertificateRecipientClientCredential) = value
        """
        ...


    def SetDefaultCertificate(self, *__args): # -> 
        """ SetDefaultCertificate(self: X509CertificateRecipientClientCredential, subjectName: str, storeLocation: StoreLocation, storeName: StoreName)SetDefaultCertificate(self: X509CertificateRecipientClientCredential, storeLocation: StoreLocation, storeName: StoreName, findType: X509FindType, findValue: object) """
        ...

    def SetScopedCertificate(self, *__args): # -> 
        """ SetScopedCertificate(self: X509CertificateRecipientClientCredential, subjectName: str, storeLocation: StoreLocation, storeName: StoreName, targetService: Uri)SetScopedCertificate(self: X509CertificateRecipientClientCredential, storeLocation: StoreLocation, storeName: StoreName, findType: X509FindType, findValue: object, targetService: Uri) """
        ...


class X509CertificateRecipientServiceCredential: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Certificate(self) -> X509Certificate2:
        """
        Get: Certificate(self: X509CertificateRecipientServiceCredential) -> X509Certificate2
        Set: Certificate(self: X509CertificateRecipientServiceCredential) = value
        """
        ...


    def SetCertificate(self, *__args:str): # -> 
        """ SetCertificate(self: X509CertificateRecipientServiceCredential, subjectName: str)SetCertificate(self: X509CertificateRecipientServiceCredential, subjectName: str, storeLocation: StoreLocation, storeName: StoreName)SetCertificate(self: X509CertificateRecipientServiceCredential, storeLocation: StoreLocation, storeName: StoreName, findType: X509FindType, findValue: object) """
        ...


class X509CertificateValidationMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum X509CertificateValidationMode, values: ChainTrust (2), Custom (4), None (0), PeerOrChainTrust (3), PeerTrust (1) """
    ChainTrust: X509CertificateValidationMode = ...
    Custom: X509CertificateValidationMode = ...
    PeerOrChainTrust: X509CertificateValidationMode = ...
    PeerTrust: X509CertificateValidationMode = ...
    value__ = ...


class X509ClientCertificateAuthentication: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CertificateValidationMode(self) -> X509CertificateValidationMode:
        """
        Get: CertificateValidationMode(self: X509ClientCertificateAuthentication) -> X509CertificateValidationMode
        Set: CertificateValidationMode(self: X509ClientCertificateAuthentication) = value
        """
        ...

    @property
    def CustomCertificateValidator(self) -> X509CertificateValidator:
        """
        Get: CustomCertificateValidator(self: X509ClientCertificateAuthentication) -> X509CertificateValidator
        Set: CustomCertificateValidator(self: X509ClientCertificateAuthentication) = value
        """
        ...

    @property
    def IncludeWindowsGroups(self) -> bool:
        """
        Get: IncludeWindowsGroups(self: X509ClientCertificateAuthentication) -> bool
        Set: IncludeWindowsGroups(self: X509ClientCertificateAuthentication) = value
        """
        ...

    @property
    def MapClientCertificateToWindowsAccount(self) -> bool:
        """
        Get: MapClientCertificateToWindowsAccount(self: X509ClientCertificateAuthentication) -> bool
        Set: MapClientCertificateToWindowsAccount(self: X509ClientCertificateAuthentication) = value
        """
        ...

    @property
    def RevocationMode(self) -> X509RevocationMode:
        """
        Get: RevocationMode(self: X509ClientCertificateAuthentication) -> X509RevocationMode
        Set: RevocationMode(self: X509ClientCertificateAuthentication) = value
        """
        ...

    @property
    def TrustedStoreLocation(self) -> StoreLocation:
        """
        Get: TrustedStoreLocation(self: X509ClientCertificateAuthentication) -> StoreLocation
        Set: TrustedStoreLocation(self: X509ClientCertificateAuthentication) = value
        """
        ...



class X509PeerCertificateAuthentication: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CertificateValidationMode(self) -> X509CertificateValidationMode:
        """
        Get: CertificateValidationMode(self: X509PeerCertificateAuthentication) -> X509CertificateValidationMode
        Set: CertificateValidationMode(self: X509PeerCertificateAuthentication) = value
        """
        ...

    @property
    def CustomCertificateValidator(self) -> X509CertificateValidator:
        """
        Get: CustomCertificateValidator(self: X509PeerCertificateAuthentication) -> X509CertificateValidator
        Set: CustomCertificateValidator(self: X509PeerCertificateAuthentication) = value
        """
        ...

    @property
    def RevocationMode(self) -> X509RevocationMode:
        """
        Get: RevocationMode(self: X509PeerCertificateAuthentication) -> X509RevocationMode
        Set: RevocationMode(self: X509PeerCertificateAuthentication) = value
        """
        ...

    @property
    def TrustedStoreLocation(self) -> StoreLocation:
        """
        Get: TrustedStoreLocation(self: X509PeerCertificateAuthentication) -> StoreLocation
        Set: TrustedStoreLocation(self: X509PeerCertificateAuthentication) = value
        """
        ...



class X509ServiceCertificateAuthentication: # skipped bases: <type 'object'>, <type 'object'>
    """ X509ServiceCertificateAuthentication() """
    @property
    def CertificateValidationMode(self) -> X509CertificateValidationMode:
        """
        Get: CertificateValidationMode(self: X509ServiceCertificateAuthentication) -> X509CertificateValidationMode
        Set: CertificateValidationMode(self: X509ServiceCertificateAuthentication) = value
        """
        ...

    @property
    def CustomCertificateValidator(self) -> X509CertificateValidator:
        """
        Get: CustomCertificateValidator(self: X509ServiceCertificateAuthentication) -> X509CertificateValidator
        Set: CustomCertificateValidator(self: X509ServiceCertificateAuthentication) = value
        """
        ...

    @property
    def RevocationMode(self) -> X509RevocationMode:
        """
        Get: RevocationMode(self: X509ServiceCertificateAuthentication) -> X509RevocationMode
        Set: RevocationMode(self: X509ServiceCertificateAuthentication) = value
        """
        ...

    @property
    def TrustedStoreLocation(self) -> StoreLocation:
        """
        Get: TrustedStoreLocation(self: X509ServiceCertificateAuthentication) -> StoreLocation
        Set: TrustedStoreLocation(self: X509ServiceCertificateAuthentication) = value
        """
        ...



# variables with complex values

