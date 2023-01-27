# encoding: utf-8
# module System.ServiceModel.Security.Tokens calls itself Tokens
# from System.ServiceModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.IdentityModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.JScript import Binding

from Microsoft.VisualBasic import Collection

from System import (Array, AsyncCallback, DateTime, Enum, IAsyncResult, 
    IDisposable, MulticastDelegate, TimeSpan, Uri)

from System.Collections.Generic import KeyedByTypeCollection

from System.Collections.ObjectModel import ReadOnlyCollection

from System.IdentityModel.Selectors import (SecurityTokenAuthenticator, 
    SecurityTokenProvider, SecurityTokenRequirement, SecurityTokenResolver, 
    SecurityTokenSerializer, SecurityTokenVersion)

from System.IdentityModel.Tokens import (SecurityKeyIdentifier, 
    SecurityKeyType, SecurityToken)

from System.Net import NetworkCredential

from System.Security.Principal import TokenImpersonationLevel

from System.ServiceModel import (AuditLevel, AuditLogLocation, 
    EndpointAddress, ICommunicationObject, MessageSecurityVersion)

from System.ServiceModel.Channels import SecurityBindingElement

from System.ServiceModel.Security import (ChannelProtectionRequirements, 
    IdentityVerifier, SecurityAlgorithmSuite, SecurityKeyEntropyMode, 
    SecurityMessageProperty, SecurityStateEncoder)

from System.Xml import UniqueId

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    IExpirableItem, field#)
"""

# no functions
# classes

class BinarySecretSecurityToken(SecurityToken): # skipped bases: <type 'object'>
    """
    BinarySecretSecurityToken(keySizeInBits: int)
    BinarySecretSecurityToken(id: str, keySizeInBits: int)
    BinarySecretSecurityToken(key: Array[Byte])
    BinarySecretSecurityToken(id: str, key: Array[Byte])
    """
    @property
    def KeySize(self) -> int:
        """ Get: KeySize(self: BinarySecretSecurityToken) -> int """
        ...


    def GetKeyBytes(self) -> Array:
        """ GetKeyBytes(self: BinarySecretSecurityToken) -> Array[Byte] """
        ...

    def __new__(cls, *__args:int) -> Self:
        """
        __new__(cls: type, keySizeInBits: int)
        __new__(cls: type, id: str, keySizeInBits: int)
        __new__(cls: type, key: Array[Byte])
        __new__(cls: type, id: str, key: Array[Byte])
        __new__(cls: type, id: str, keySizeInBits: int, allowCrypto: bool)
        __new__(cls: type, id: str, key: Array[Byte], allowCrypto: bool)
        """
        ...


class ClaimTypeRequirement: # skipped bases: <type 'object'>, <type 'object'>
    """
    ClaimTypeRequirement(claimType: str)
    ClaimTypeRequirement(claimType: str, isOptional: bool)
    """
    @property
    def ClaimType(self) -> str:
        """ Get: ClaimType(self: ClaimTypeRequirement) -> str """
        ...

    @property
    def IsOptional(self) -> bool:
        """ Get: IsOptional(self: ClaimTypeRequirement) -> bool """
        ...



class IIssuanceSecurityTokenAuthenticator: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IssuedSecurityTokenHandler(self) -> IssuedSecurityTokenHandler:
        """
        Get: IssuedSecurityTokenHandler(self: IIssuanceSecurityTokenAuthenticator) -> IssuedSecurityTokenHandler
        Set: IssuedSecurityTokenHandler(self: IIssuanceSecurityTokenAuthenticator) = value
        """
        ...

    @property
    def RenewedSecurityTokenHandler(self) -> RenewedSecurityTokenHandler:
        """
        Get: RenewedSecurityTokenHandler(self: IIssuanceSecurityTokenAuthenticator) -> RenewedSecurityTokenHandler
        Set: RenewedSecurityTokenHandler(self: IIssuanceSecurityTokenAuthenticator) = value
        """
        ...



class ILogonTokenCacheManager: # skipped bases: <type 'object'>
    """ no doc """
    def FlushLogonTokenCache(self): # -> 
        """ FlushLogonTokenCache(self: ILogonTokenCacheManager) """
        ...

    def RemoveCachedLogonToken(self, username:str) -> bool:
        """ RemoveCachedLogonToken(self: ILogonTokenCacheManager, username: str) -> bool """
        ...


class ServiceModelSecurityTokenRequirement(SecurityTokenRequirement): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AuditLogLocationProperty(self) -> str:
        """ Get: AuditLogLocationProperty() -> str """
        ...

    @property
    def ChannelParametersCollectionProperty(self) -> str:
        """ Get: ChannelParametersCollectionProperty() -> str """
        ...

    @property
    def DuplexClientLocalAddressProperty(self) -> str:
        """ Get: DuplexClientLocalAddressProperty() -> str """
        ...

    @property
    def EndpointFilterTableProperty(self) -> str:
        """ Get: EndpointFilterTableProperty() -> str """
        ...

    @property
    def ExtendedProtectionPolicy(self) -> str:
        """ Get: ExtendedProtectionPolicy() -> str """
        ...

    @property
    def HttpAuthenticationSchemeProperty(self) -> str:
        """ Get: HttpAuthenticationSchemeProperty() -> str """
        ...

    @property
    def IsInitiator(self) -> bool:
        """ Get: IsInitiator(self: ServiceModelSecurityTokenRequirement) -> bool """
        ...

    @property
    def IsInitiatorProperty(self) -> str:
        """ Get: IsInitiatorProperty() -> str """
        ...

    @property
    def IsOutOfBandTokenProperty(self) -> str:
        """ Get: IsOutOfBandTokenProperty() -> str """
        ...

    @property
    def IssuedSecurityTokenParametersProperty(self) -> str:
        """ Get: IssuedSecurityTokenParametersProperty() -> str """
        ...

    @property
    def IssuerAddress(self) -> EndpointAddress:
        """
        Get: IssuerAddress(self: ServiceModelSecurityTokenRequirement) -> EndpointAddress
        Set: IssuerAddress(self: ServiceModelSecurityTokenRequirement) = value
        """
        ...

    @property
    def IssuerAddressProperty(self) -> str:
        """ Get: IssuerAddressProperty() -> str """
        ...

    @property
    def IssuerBinding(self) -> Binding:
        """
        Get: IssuerBinding(self: ServiceModelSecurityTokenRequirement) -> Binding
        Set: IssuerBinding(self: ServiceModelSecurityTokenRequirement) = value
        """
        ...

    @property
    def IssuerBindingContextProperty(self) -> str:
        """ Get: IssuerBindingContextProperty() -> str """
        ...

    @property
    def IssuerBindingProperty(self) -> str:
        """ Get: IssuerBindingProperty() -> str """
        ...

    @property
    def ListenUriProperty(self) -> str:
        """ Get: ListenUriProperty() -> str """
        ...

    @property
    def MessageAuthenticationAuditLevelProperty(self) -> str:
        """ Get: MessageAuthenticationAuditLevelProperty() -> str """
        ...

    @property
    def MessageDirectionProperty(self) -> str:
        """ Get: MessageDirectionProperty() -> str """
        ...

    @property
    def MessageSecurityVersion(self) -> SecurityTokenVersion:
        """
        Get: MessageSecurityVersion(self: ServiceModelSecurityTokenRequirement) -> SecurityTokenVersion
        Set: MessageSecurityVersion(self: ServiceModelSecurityTokenRequirement) = value
        """
        ...

    @property
    def MessageSecurityVersionProperty(self) -> str:
        """ Get: MessageSecurityVersionProperty() -> str """
        ...

    @property
    def PreferSslCertificateAuthenticatorProperty(self) -> str:
        """ Get: PreferSslCertificateAuthenticatorProperty() -> str """
        ...

    @property
    def PrivacyNoticeUriProperty(self) -> str:
        """ Get: PrivacyNoticeUriProperty() -> str """
        ...

    @property
    def PrivacyNoticeVersionProperty(self) -> str:
        """ Get: PrivacyNoticeVersionProperty() -> str """
        ...

    @property
    def SecureConversationSecurityBindingElement(self) -> SecurityBindingElement:
        """
        Get: SecureConversationSecurityBindingElement(self: ServiceModelSecurityTokenRequirement) -> SecurityBindingElement
        Set: SecureConversationSecurityBindingElement(self: ServiceModelSecurityTokenRequirement) = value
        """
        ...

    @property
    def SecureConversationSecurityBindingElementProperty(self) -> str:
        """ Get: SecureConversationSecurityBindingElementProperty() -> str """
        ...

    @property
    def SecurityAlgorithmSuite(self) -> SecurityAlgorithmSuite:
        """
        Get: SecurityAlgorithmSuite(self: ServiceModelSecurityTokenRequirement) -> SecurityAlgorithmSuite
        Set: SecurityAlgorithmSuite(self: ServiceModelSecurityTokenRequirement) = value
        """
        ...

    @property
    def SecurityAlgorithmSuiteProperty(self) -> str:
        """ Get: SecurityAlgorithmSuiteProperty() -> str """
        ...

    @property
    def SecurityBindingElement(self) -> SecurityBindingElement:
        """
        Get: SecurityBindingElement(self: ServiceModelSecurityTokenRequirement) -> SecurityBindingElement
        Set: SecurityBindingElement(self: ServiceModelSecurityTokenRequirement) = value
        """
        ...

    @property
    def SecurityBindingElementProperty(self) -> str:
        """ Get: SecurityBindingElementProperty() -> str """
        ...

    @property
    def SupportingTokenAttachmentModeProperty(self) -> str:
        """ Get: SupportingTokenAttachmentModeProperty() -> str """
        ...

    @property
    def SupportSecurityContextCancellationProperty(self) -> str:
        """ Get: SupportSecurityContextCancellationProperty() -> str """
        ...

    @property
    def SuppressAuditFailureProperty(self) -> str:
        """ Get: SuppressAuditFailureProperty() -> str """
        ...

    @property
    def TargetAddressProperty(self) -> str:
        """ Get: TargetAddressProperty() -> str """
        ...

    @property
    def TransportScheme(self) -> str:
        """
        Get: TransportScheme(self: ServiceModelSecurityTokenRequirement) -> str
        Set: TransportScheme(self: ServiceModelSecurityTokenRequirement) = value
        """
        ...

    @property
    def TransportSchemeProperty(self) -> str:
        """ Get: TransportSchemeProperty() -> str """
        ...

    @property
    def ViaProperty(self) -> str:
        """ Get: ViaProperty() -> str """
        ...


    Namespace: str = ...


class InitiatorServiceModelSecurityTokenRequirement(ServiceModelSecurityTokenRequirement): # skipped bases: <type 'object'>
    """ InitiatorServiceModelSecurityTokenRequirement() """
    @property
    def TargetAddress(self) -> EndpointAddress:
        """
        Get: TargetAddress(self: InitiatorServiceModelSecurityTokenRequirement) -> EndpointAddress
        Set: TargetAddress(self: InitiatorServiceModelSecurityTokenRequirement) = value
        """
        ...

    @property
    def Via(self) -> Uri:
        """
        Get: Via(self: InitiatorServiceModelSecurityTokenRequirement) -> Uri
        Set: Via(self: InitiatorServiceModelSecurityTokenRequirement) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: InitiatorServiceModelSecurityTokenRequirement) -> str """
        ...


class ISecurityContextSecurityTokenCache: # skipped bases: <type 'object'>
    """ no doc """
    def AddContext(self, token:SecurityContextSecurityToken): # -> 
        """ AddContext(self: ISecurityContextSecurityTokenCache, token: SecurityContextSecurityToken) """
        ...

    def ClearContexts(self): # -> 
        """ ClearContexts(self: ISecurityContextSecurityTokenCache) """
        ...

    def GetAllContexts(self, contextId:UniqueId) -> Collection:
        """ GetAllContexts(self: ISecurityContextSecurityTokenCache, contextId: UniqueId) -> Collection[SecurityContextSecurityToken] """
        ...

    def GetContext(self, contextId:UniqueId, generation:UniqueId) -> SecurityContextSecurityToken:
        """ GetContext(self: ISecurityContextSecurityTokenCache, contextId: UniqueId, generation: UniqueId) -> SecurityContextSecurityToken """
        ...

    def RemoveAllContexts(self, contextId:UniqueId): # -> 
        """ RemoveAllContexts(self: ISecurityContextSecurityTokenCache, contextId: UniqueId) """
        ...

    def RemoveContext(self, contextId:UniqueId, generation:UniqueId): # -> 
        """ RemoveContext(self: ISecurityContextSecurityTokenCache, contextId: UniqueId, generation: UniqueId) """
        ...

    def TryAddContext(self, token:SecurityContextSecurityToken) -> bool:
        """ TryAddContext(self: ISecurityContextSecurityTokenCache, token: SecurityContextSecurityToken) -> bool """
        ...

    def UpdateContextCachingTime(self, context:SecurityContextSecurityToken, expirationTime:DateTime): # -> 
        """ UpdateContextCachingTime(self: ISecurityContextSecurityTokenCache, context: SecurityContextSecurityToken, expirationTime: DateTime) """
        ...


class IssuedSecurityTokenHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ IssuedSecurityTokenHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, issuedToken:SecurityToken, tokenRequestor:EndpointAddress, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: IssuedSecurityTokenHandler, issuedToken: SecurityToken, tokenRequestor: EndpointAddress, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: IssuedSecurityTokenHandler, result: IAsyncResult) """
        ...

    def Invoke(self, issuedToken:SecurityToken, tokenRequestor:EndpointAddress): # -> 
        """ Invoke(self: IssuedSecurityTokenHandler, issuedToken: SecurityToken, tokenRequestor: EndpointAddress) """
        ...


class SecurityTokenParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def HasAsymmetricKey(self):
        ...

    @property
    def InclusionMode(self) -> SecurityTokenInclusionMode:
        """
        Get: InclusionMode(self: SecurityTokenParameters) -> SecurityTokenInclusionMode
        Set: InclusionMode(self: SecurityTokenParameters) = value
        """
        ...

    @property
    def ReferenceStyle(self) -> SecurityTokenReferenceStyle:
        """
        Get: ReferenceStyle(self: SecurityTokenParameters) -> SecurityTokenReferenceStyle
        Set: ReferenceStyle(self: SecurityTokenParameters) = value
        """
        ...

    @property
    def RequireDerivedKeys(self) -> bool:
        """
        Get: RequireDerivedKeys(self: SecurityTokenParameters) -> bool
        Set: RequireDerivedKeys(self: SecurityTokenParameters) = value
        """
        ...

    @property
    def SupportsClientAuthentication(self):
        ...

    @property
    def SupportsClientWindowsIdentity(self):
        ...

    @property
    def SupportsServerAuthentication(self):
        ...


    def Clone(self) -> SecurityTokenParameters:
        """ Clone(self: SecurityTokenParameters) -> SecurityTokenParameters """
        ...

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: SecurityTokenParameters) -> SecurityTokenParameters """
        ...

    def CreateKeyIdentifierClause(self, *args): #cannot find CLR method
        """ CreateKeyIdentifierClause(self: SecurityTokenParameters, token: SecurityToken, referenceStyle: SecurityTokenReferenceStyle) -> SecurityKeyIdentifierClause """
        ...

    def InitializeSecurityTokenRequirement(self, *args): #cannot find CLR method
        """ InitializeSecurityTokenRequirement(self: SecurityTokenParameters, requirement: SecurityTokenRequirement) """
        ...

    def MatchesKeyIdentifierClause(self, *args): #cannot find CLR method
        """ MatchesKeyIdentifierClause(self: SecurityTokenParameters, token: SecurityToken, keyIdentifierClause: SecurityKeyIdentifierClause, referenceStyle: SecurityTokenReferenceStyle) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: SecurityTokenParameters) -> str """
        ...


class IssuedSecurityTokenParameters(SecurityTokenParameters): # skipped bases: <type 'object'>
    """
    IssuedSecurityTokenParameters()
    IssuedSecurityTokenParameters(tokenType: str)
    IssuedSecurityTokenParameters(tokenType: str, issuerAddress: EndpointAddress)
    IssuedSecurityTokenParameters(tokenType: str, issuerAddress: EndpointAddress, issuerBinding: Binding)
    """
    @property
    def AdditionalRequestParameters(self) -> Collection:
        """ Get: AdditionalRequestParameters(self: IssuedSecurityTokenParameters) -> Collection[XmlElement] """
        ...

    @property
    def ClaimTypeRequirements(self) -> Collection:
        """ Get: ClaimTypeRequirements(self: IssuedSecurityTokenParameters) -> Collection[ClaimTypeRequirement] """
        ...

    @property
    def DefaultMessageSecurityVersion(self) -> MessageSecurityVersion:
        """
        Get: DefaultMessageSecurityVersion(self: IssuedSecurityTokenParameters) -> MessageSecurityVersion
        Set: DefaultMessageSecurityVersion(self: IssuedSecurityTokenParameters) = value
        """
        ...

    @property
    def IssuerAddress(self) -> EndpointAddress:
        """
        Get: IssuerAddress(self: IssuedSecurityTokenParameters) -> EndpointAddress
        Set: IssuerAddress(self: IssuedSecurityTokenParameters) = value
        """
        ...

    @property
    def IssuerBinding(self) -> Binding:
        """
        Get: IssuerBinding(self: IssuedSecurityTokenParameters) -> Binding
        Set: IssuerBinding(self: IssuedSecurityTokenParameters) = value
        """
        ...

    @property
    def IssuerMetadataAddress(self) -> EndpointAddress:
        """
        Get: IssuerMetadataAddress(self: IssuedSecurityTokenParameters) -> EndpointAddress
        Set: IssuerMetadataAddress(self: IssuedSecurityTokenParameters) = value
        """
        ...

    @property
    def KeySize(self) -> int:
        """
        Get: KeySize(self: IssuedSecurityTokenParameters) -> int
        Set: KeySize(self: IssuedSecurityTokenParameters) = value
        """
        ...

    @property
    def KeyType(self) -> SecurityKeyType:
        """
        Get: KeyType(self: IssuedSecurityTokenParameters) -> SecurityKeyType
        Set: KeyType(self: IssuedSecurityTokenParameters) = value
        """
        ...

    @property
    def TokenType(self) -> str:
        """
        Get: TokenType(self: IssuedSecurityTokenParameters) -> str
        Set: TokenType(self: IssuedSecurityTokenParameters) = value
        """
        ...

    @property
    def UseStrTransform(self) -> bool:
        """
        Get: UseStrTransform(self: IssuedSecurityTokenParameters) -> bool
        Set: UseStrTransform(self: IssuedSecurityTokenParameters) = value
        """
        ...


    def CreateRequestParameters(self, messageSecurityVersion:MessageSecurityVersion, securityTokenSerializer:SecurityTokenSerializer) -> Collection:
        """ CreateRequestParameters(self: IssuedSecurityTokenParameters, messageSecurityVersion: MessageSecurityVersion, securityTokenSerializer: SecurityTokenSerializer) -> Collection[XmlElement] """
        ...


class IssuedSecurityTokenProvider(ICommunicationObject, SecurityTokenProvider): # skipped bases: <type 'object'>
    """ IssuedSecurityTokenProvider() """
    @property
    def CacheIssuedTokens(self) -> bool:
        """
        Get: CacheIssuedTokens(self: IssuedSecurityTokenProvider) -> bool
        Set: CacheIssuedTokens(self: IssuedSecurityTokenProvider) = value
        """
        ...

    @property
    def DefaultCloseTimeout(self) -> TimeSpan:
        """ Get: DefaultCloseTimeout(self: IssuedSecurityTokenProvider) -> TimeSpan """
        ...

    @property
    def DefaultOpenTimeout(self) -> TimeSpan:
        """ Get: DefaultOpenTimeout(self: IssuedSecurityTokenProvider) -> TimeSpan """
        ...

    @property
    def IdentityVerifier(self) -> IdentityVerifier:
        """
        Get: IdentityVerifier(self: IssuedSecurityTokenProvider) -> IdentityVerifier
        Set: IdentityVerifier(self: IssuedSecurityTokenProvider) = value
        """
        ...

    @property
    def IssuedTokenRenewalThresholdPercentage(self) -> int:
        """
        Get: IssuedTokenRenewalThresholdPercentage(self: IssuedSecurityTokenProvider) -> int
        Set: IssuedTokenRenewalThresholdPercentage(self: IssuedSecurityTokenProvider) = value
        """
        ...

    @property
    def IssuerAddress(self) -> EndpointAddress:
        """
        Get: IssuerAddress(self: IssuedSecurityTokenProvider) -> EndpointAddress
        Set: IssuerAddress(self: IssuedSecurityTokenProvider) = value
        """
        ...

    @property
    def IssuerBinding(self) -> Binding:
        """
        Get: IssuerBinding(self: IssuedSecurityTokenProvider) -> Binding
        Set: IssuerBinding(self: IssuedSecurityTokenProvider) = value
        """
        ...

    @property
    def IssuerChannelBehaviors(self) -> KeyedByTypeCollection:
        """ Get: IssuerChannelBehaviors(self: IssuedSecurityTokenProvider) -> KeyedByTypeCollection[IEndpointBehavior] """
        ...

    @property
    def KeyEntropyMode(self) -> SecurityKeyEntropyMode:
        """
        Get: KeyEntropyMode(self: IssuedSecurityTokenProvider) -> SecurityKeyEntropyMode
        Set: KeyEntropyMode(self: IssuedSecurityTokenProvider) = value
        """
        ...

    @property
    def MaxIssuedTokenCachingTime(self) -> TimeSpan:
        """
        Get: MaxIssuedTokenCachingTime(self: IssuedSecurityTokenProvider) -> TimeSpan
        Set: MaxIssuedTokenCachingTime(self: IssuedSecurityTokenProvider) = value
        """
        ...

    @property
    def MessageSecurityVersion(self) -> MessageSecurityVersion:
        """
        Get: MessageSecurityVersion(self: IssuedSecurityTokenProvider) -> MessageSecurityVersion
        Set: MessageSecurityVersion(self: IssuedSecurityTokenProvider) = value
        """
        ...

    @property
    def SecurityAlgorithmSuite(self) -> SecurityAlgorithmSuite:
        """
        Get: SecurityAlgorithmSuite(self: IssuedSecurityTokenProvider) -> SecurityAlgorithmSuite
        Set: SecurityAlgorithmSuite(self: IssuedSecurityTokenProvider) = value
        """
        ...

    @property
    def SecurityTokenSerializer(self) -> SecurityTokenSerializer:
        """
        Get: SecurityTokenSerializer(self: IssuedSecurityTokenProvider) -> SecurityTokenSerializer
        Set: SecurityTokenSerializer(self: IssuedSecurityTokenProvider) = value
        """
        ...

    @property
    def TargetAddress(self) -> EndpointAddress:
        """
        Get: TargetAddress(self: IssuedSecurityTokenProvider) -> EndpointAddress
        Set: TargetAddress(self: IssuedSecurityTokenProvider) = value
        """
        ...

    @property
    def TokenRequestParameters(self) -> Collection:
        """ Get: TokenRequestParameters(self: IssuedSecurityTokenProvider) -> Collection[XmlElement] """
        ...


    def Dispose(self): # -> 
        """ Dispose(self: IssuedSecurityTokenProvider) """
        ...

    Closed = ...
    Closing = ...
    Faulted = ...
    Opened = ...
    Opening = ...


class KerberosSecurityTokenParameters(SecurityTokenParameters): # skipped bases: <type 'object'>
    """ KerberosSecurityTokenParameters() """
    pass

class RecipientServiceModelSecurityTokenRequirement(ServiceModelSecurityTokenRequirement): # skipped bases: <type 'object'>
    """ RecipientServiceModelSecurityTokenRequirement() """
    @property
    def AuditLogLocation(self) -> AuditLogLocation:
        """
        Get: AuditLogLocation(self: RecipientServiceModelSecurityTokenRequirement) -> AuditLogLocation
        Set: AuditLogLocation(self: RecipientServiceModelSecurityTokenRequirement) = value
        """
        ...

    @property
    def ListenUri(self) -> Uri:
        """
        Get: ListenUri(self: RecipientServiceModelSecurityTokenRequirement) -> Uri
        Set: ListenUri(self: RecipientServiceModelSecurityTokenRequirement) = value
        """
        ...

    @property
    def MessageAuthenticationAuditLevel(self) -> AuditLevel:
        """
        Get: MessageAuthenticationAuditLevel(self: RecipientServiceModelSecurityTokenRequirement) -> AuditLevel
        Set: MessageAuthenticationAuditLevel(self: RecipientServiceModelSecurityTokenRequirement) = value
        """
        ...

    @property
    def SuppressAuditFailure(self) -> bool:
        """
        Get: SuppressAuditFailure(self: RecipientServiceModelSecurityTokenRequirement) -> bool
        Set: SuppressAuditFailure(self: RecipientServiceModelSecurityTokenRequirement) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: RecipientServiceModelSecurityTokenRequirement) -> str """
        ...


class RenewedSecurityTokenHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ RenewedSecurityTokenHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, newSecurityToken:SecurityToken, oldSecurityToken:SecurityToken, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: RenewedSecurityTokenHandler, newSecurityToken: SecurityToken, oldSecurityToken: SecurityToken, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: RenewedSecurityTokenHandler, result: IAsyncResult) """
        ...

    def Invoke(self, newSecurityToken:SecurityToken, oldSecurityToken:SecurityToken): # -> 
        """ Invoke(self: RenewedSecurityTokenHandler, newSecurityToken: SecurityToken, oldSecurityToken: SecurityToken) """
        ...


class RsaSecurityTokenParameters(SecurityTokenParameters): # skipped bases: <type 'object'>
    """ RsaSecurityTokenParameters() """
    pass

class SecureConversationSecurityTokenParameters(SecurityTokenParameters): # skipped bases: <type 'object'>
    """
    SecureConversationSecurityTokenParameters()
    SecureConversationSecurityTokenParameters(bootstrapSecurityBindingElement: SecurityBindingElement)
    SecureConversationSecurityTokenParameters(bootstrapSecurityBindingElement: SecurityBindingElement, requireCancellation: bool)
    SecureConversationSecurityTokenParameters(bootstrapSecurityBindingElement: SecurityBindingElement, requireCancellation: bool, canRenewSession: bool)
    SecureConversationSecurityTokenParameters(bootstrapSecurityBindingElement: SecurityBindingElement, requireCancellation: bool, bootstrapProtectionRequirements: ChannelProtectionRequirements)
    SecureConversationSecurityTokenParameters(bootstrapSecurityBindingElement: SecurityBindingElement, requireCancellation: bool, canRenewSession: bool, bootstrapProtectionRequirements: ChannelProtectionRequirements)
    """
    @property
    def BootstrapProtectionRequirements(self) -> ChannelProtectionRequirements:
        """ Get: BootstrapProtectionRequirements(self: SecureConversationSecurityTokenParameters) -> ChannelProtectionRequirements """
        ...

    @property
    def BootstrapSecurityBindingElement(self) -> SecurityBindingElement:
        """
        Get: BootstrapSecurityBindingElement(self: SecureConversationSecurityTokenParameters) -> SecurityBindingElement
        Set: BootstrapSecurityBindingElement(self: SecureConversationSecurityTokenParameters) = value
        """
        ...

    @property
    def CanRenewSession(self) -> bool:
        """
        Get: CanRenewSession(self: SecureConversationSecurityTokenParameters) -> bool
        Set: CanRenewSession(self: SecureConversationSecurityTokenParameters) = value
        """
        ...

    @property
    def RequireCancellation(self) -> bool:
        """
        Get: RequireCancellation(self: SecureConversationSecurityTokenParameters) -> bool
        Set: RequireCancellation(self: SecureConversationSecurityTokenParameters) = value
        """
        ...



class SecurityContextSecurityToken(IExpirableItem, IDisposable, SecurityToken): # skipped bases: <type 'object'>
    """
    SecurityContextSecurityToken(contextId: UniqueId, key: Array[Byte], validFrom: DateTime, validTo: DateTime)
    SecurityContextSecurityToken(contextId: UniqueId, id: str, key: Array[Byte], validFrom: DateTime, validTo: DateTime)
    SecurityContextSecurityToken(contextId: UniqueId, id: str, key: Array[Byte], validFrom: DateTime, validTo: DateTime, authorizationPolicies: ReadOnlyCollection[IAuthorizationPolicy])
    SecurityContextSecurityToken(contextId: UniqueId, id: str, key: Array[Byte], validFrom: DateTime, validTo: DateTime, keyGeneration: UniqueId, keyEffectiveTime: DateTime, keyExpirationTime: DateTime, authorizationPolicies: ReadOnlyCollection[IAuthorizationPolicy])
    """
    @property
    def AuthorizationPolicies(self) -> ReadOnlyCollection:
        """ Get: AuthorizationPolicies(self: SecurityContextSecurityToken) -> ReadOnlyCollection[IAuthorizationPolicy] """
        ...

    @property
    def BootstrapMessageProperty(self) -> SecurityMessageProperty:
        """
        Get: BootstrapMessageProperty(self: SecurityContextSecurityToken) -> SecurityMessageProperty
        Set: BootstrapMessageProperty(self: SecurityContextSecurityToken) = value
        """
        ...

    @property
    def ContextId(self) -> UniqueId:
        """ Get: ContextId(self: SecurityContextSecurityToken) -> UniqueId """
        ...

    @property
    def IsCookieMode(self) -> bool:
        """ Get: IsCookieMode(self: SecurityContextSecurityToken) -> bool """
        ...

    @property
    def KeyEffectiveTime(self) -> DateTime:
        """ Get: KeyEffectiveTime(self: SecurityContextSecurityToken) -> DateTime """
        ...

    @property
    def KeyExpirationTime(self) -> DateTime:
        """ Get: KeyExpirationTime(self: SecurityContextSecurityToken) -> DateTime """
        ...

    @property
    def KeyGeneration(self) -> UniqueId:
        """ Get: KeyGeneration(self: SecurityContextSecurityToken) -> UniqueId """
        ...


    @staticmethod
    def CreateCookieSecurityContextToken(contextId, id, key, validFrom, validTo, *__args) -> SecurityContextSecurityToken:
        """
        CreateCookieSecurityContextToken(contextId: UniqueId, id: str, key: Array[Byte], validFrom: DateTime, validTo: DateTime, authorizationPolicies: ReadOnlyCollection[IAuthorizationPolicy], securityStateEncoder: SecurityStateEncoder) -> SecurityContextSecurityToken
        CreateCookieSecurityContextToken(contextId: UniqueId, id: str, key: Array[Byte], validFrom: DateTime, validTo: DateTime, keyGeneration: UniqueId, keyEffectiveTime: DateTime, keyExpirationTime: DateTime, authorizationPolicies: ReadOnlyCollection[IAuthorizationPolicy], securityStateEncoder: SecurityStateEncoder) -> SecurityContextSecurityToken
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: SecurityContextSecurityToken) -> str """
        ...

    def __new__(cls, contextId, *__args) -> Self:
        """
        __new__(cls: type, contextId: UniqueId, key: Array[Byte], validFrom: DateTime, validTo: DateTime)
        __new__(cls: type, contextId: UniqueId, id: str, key: Array[Byte], validFrom: DateTime, validTo: DateTime)
        __new__(cls: type, contextId: UniqueId, id: str, key: Array[Byte], validFrom: DateTime, validTo: DateTime, authorizationPolicies: ReadOnlyCollection[IAuthorizationPolicy])
        __new__(cls: type, contextId: UniqueId, id: str, key: Array[Byte], validFrom: DateTime, validTo: DateTime, keyGeneration: UniqueId, keyEffectiveTime: DateTime, keyExpirationTime: DateTime, authorizationPolicies: ReadOnlyCollection[IAuthorizationPolicy])
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class SecurityContextSecurityTokenAuthenticator(SecurityTokenAuthenticator): # skipped bases: <type 'object'>
    """ SecurityContextSecurityTokenAuthenticator() """
    pass

class SecurityContextSecurityTokenResolver(ISecurityContextSecurityTokenCache, SecurityTokenResolver): # skipped bases: <type 'ICustomIdentityConfiguration'>, <type 'object'>
    """
    SecurityContextSecurityTokenResolver(securityContextCacheCapacity: int, removeOldestTokensOnCacheFull: bool)
    SecurityContextSecurityTokenResolver(securityContextCacheCapacity: int, removeOldestTokensOnCacheFull: bool, clockSkew: TimeSpan)
    """
    @property
    def ClockSkew(self) -> TimeSpan:
        """ Get: ClockSkew(self: SecurityContextSecurityTokenResolver) -> TimeSpan """
        ...

    @property
    def RemoveOldestTokensOnCacheFull(self) -> bool:
        """ Get: RemoveOldestTokensOnCacheFull(self: SecurityContextSecurityTokenResolver) -> bool """
        ...

    @property
    def SecurityContextTokenCacheCapacity(self) -> int:
        """ Get: SecurityContextTokenCacheCapacity(self: SecurityContextSecurityTokenResolver) -> int """
        ...


    def __new__(cls, securityContextCacheCapacity:int, removeOldestTokensOnCacheFull:bool, clockSkew:TimeSpan = ...) -> Self:
        """
        __new__(cls: type, securityContextCacheCapacity: int, removeOldestTokensOnCacheFull: bool)
        __new__(cls: type, securityContextCacheCapacity: int, removeOldestTokensOnCacheFull: bool, clockSkew: TimeSpan)
        """
        ...


class SecurityTokenInclusionMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SecurityTokenInclusionMode, values: AlwaysToInitiator (3), AlwaysToRecipient (0), Never (1), Once (2) """
    AlwaysToInitiator: SecurityTokenInclusionMode = ...
    AlwaysToRecipient: SecurityTokenInclusionMode = ...
    Never: SecurityTokenInclusionMode = ...
    Once: SecurityTokenInclusionMode = ...
    value__ = ...


class SecurityTokenReferenceStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SecurityTokenReferenceStyle, values: External (1), Internal (0) """
    External: SecurityTokenReferenceStyle = ...
    Internal: SecurityTokenReferenceStyle = ...
    value__ = ...


class ServiceModelSecurityTokenTypes: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AnonymousSslnego(self) -> str:
        """ Get: AnonymousSslnego() -> str """
        ...

    @property
    def MutualSslnego(self) -> str:
        """ Get: MutualSslnego() -> str """
        ...

    @property
    def SecureConversation(self) -> str:
        """ Get: SecureConversation() -> str """
        ...

    @property
    def SecurityContext(self) -> str:
        """ Get: SecurityContext() -> str """
        ...

    @property
    def Spnego(self) -> str:
        """ Get: Spnego() -> str """
        ...

    @property
    def SspiCredential(self) -> str:
        """ Get: SspiCredential() -> str """
        ...


    __all__: list = ...


class SslSecurityTokenParameters(SecurityTokenParameters): # skipped bases: <type 'object'>
    """
    SslSecurityTokenParameters()
    SslSecurityTokenParameters(requireClientCertificate: bool)
    SslSecurityTokenParameters(requireClientCertificate: bool, requireCancellation: bool)
    """
    @property
    def RequireCancellation(self) -> bool:
        """
        Get: RequireCancellation(self: SslSecurityTokenParameters) -> bool
        Set: RequireCancellation(self: SslSecurityTokenParameters) = value
        """
        ...

    @property
    def RequireClientCertificate(self) -> bool:
        """
        Get: RequireClientCertificate(self: SslSecurityTokenParameters) -> bool
        Set: RequireClientCertificate(self: SslSecurityTokenParameters) = value
        """
        ...



class SspiSecurityToken(SecurityToken): # skipped bases: <type 'object'>
    """
    SspiSecurityToken(impersonationLevel: TokenImpersonationLevel, allowNtlm: bool, networkCredential: NetworkCredential)
    SspiSecurityToken(networkCredential: NetworkCredential, extractGroupsForWindowsAccounts: bool, allowUnauthenticatedCallers: bool)
    """
    @property
    def AllowNtlm(self) -> bool:
        """ Get: AllowNtlm(self: SspiSecurityToken) -> bool """
        ...

    @property
    def AllowUnauthenticatedCallers(self) -> bool:
        """ Get: AllowUnauthenticatedCallers(self: SspiSecurityToken) -> bool """
        ...

    @property
    def ExtractGroupsForWindowsAccounts(self) -> bool:
        """ Get: ExtractGroupsForWindowsAccounts(self: SspiSecurityToken) -> bool """
        ...

    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel:
        """ Get: ImpersonationLevel(self: SspiSecurityToken) -> TokenImpersonationLevel """
        ...

    @property
    def NetworkCredential(self) -> NetworkCredential:
        """ Get: NetworkCredential(self: SspiSecurityToken) -> NetworkCredential """
        ...


    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, impersonationLevel: TokenImpersonationLevel, allowNtlm: bool, networkCredential: NetworkCredential)
        __new__(cls: type, networkCredential: NetworkCredential, extractGroupsForWindowsAccounts: bool, allowUnauthenticatedCallers: bool)
        """
        ...


class SspiSecurityTokenParameters(SecurityTokenParameters): # skipped bases: <type 'object'>
    """
    SspiSecurityTokenParameters()
    SspiSecurityTokenParameters(requireCancellation: bool)
    """
    @property
    def RequireCancellation(self) -> bool:
        """
        Get: RequireCancellation(self: SspiSecurityTokenParameters) -> bool
        Set: RequireCancellation(self: SspiSecurityTokenParameters) = value
        """
        ...



class SupportingTokenParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ SupportingTokenParameters() """
    @property
    def Endorsing(self) -> Collection:
        """ Get: Endorsing(self: SupportingTokenParameters) -> Collection[SecurityTokenParameters] """
        ...

    @property
    def Signed(self) -> Collection:
        """ Get: Signed(self: SupportingTokenParameters) -> Collection[SecurityTokenParameters] """
        ...

    @property
    def SignedEncrypted(self) -> Collection:
        """ Get: SignedEncrypted(self: SupportingTokenParameters) -> Collection[SecurityTokenParameters] """
        ...

    @property
    def SignedEndorsing(self) -> Collection:
        """ Get: SignedEndorsing(self: SupportingTokenParameters) -> Collection[SecurityTokenParameters] """
        ...


    def Clone(self) -> SupportingTokenParameters:
        """ Clone(self: SupportingTokenParameters) -> SupportingTokenParameters """
        ...

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: SupportingTokenParameters) -> SupportingTokenParameters """
        ...

    def SetKeyDerivation(self, requireDerivedKeys:bool): # -> 
        """ SetKeyDerivation(self: SupportingTokenParameters, requireDerivedKeys: bool) """
        ...

    def ToString(self) -> str:
        """ ToString(self: SupportingTokenParameters) -> str """
        ...


class UserNameSecurityTokenParameters(SecurityTokenParameters): # skipped bases: <type 'object'>
    """ UserNameSecurityTokenParameters() """
    pass

class WrappedKeySecurityToken(SecurityToken): # skipped bases: <type 'object'>
    """ WrappedKeySecurityToken(id: str, keyToWrap: Array[Byte], wrappingAlgorithm: str, wrappingToken: SecurityToken, wrappingTokenReference: SecurityKeyIdentifier) """
    @property
    def WrappingAlgorithm(self) -> str:
        """ Get: WrappingAlgorithm(self: WrappedKeySecurityToken) -> str """
        ...

    @property
    def WrappingToken(self) -> SecurityToken:
        """ Get: WrappingToken(self: WrappedKeySecurityToken) -> SecurityToken """
        ...

    @property
    def WrappingTokenReference(self) -> SecurityKeyIdentifier:
        """ Get: WrappingTokenReference(self: WrappedKeySecurityToken) -> SecurityKeyIdentifier """
        ...


    def GetWrappedKey(self) -> Array:
        """ GetWrappedKey(self: WrappedKeySecurityToken) -> Array[Byte] """
        ...

    def __new__(cls, id:str, keyToWrap:Array, wrappingAlgorithm:str, wrappingToken:SecurityToken, wrappingTokenReference:SecurityKeyIdentifier) -> Self:
        """ __new__(cls: type, id: str, keyToWrap: Array[Byte], wrappingAlgorithm: str, wrappingToken: SecurityToken, wrappingTokenReference: SecurityKeyIdentifier) """
        ...


class X509KeyIdentifierClauseType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum X509KeyIdentifierClauseType, values: Any (0), IssuerSerial (2), RawDataKeyIdentifier (4), SubjectKeyIdentifier (3), Thumbprint (1) """
    Any: X509KeyIdentifierClauseType = ...
    IssuerSerial: X509KeyIdentifierClauseType = ...
    RawDataKeyIdentifier: X509KeyIdentifierClauseType = ...
    SubjectKeyIdentifier: X509KeyIdentifierClauseType = ...
    Thumbprint: X509KeyIdentifierClauseType = ...
    value__ = ...


class X509SecurityTokenParameters(SecurityTokenParameters): # skipped bases: <type 'object'>
    """
    X509SecurityTokenParameters()
    X509SecurityTokenParameters(x509ReferenceStyle: X509KeyIdentifierClauseType)
    X509SecurityTokenParameters(x509ReferenceStyle: X509KeyIdentifierClauseType, inclusionMode: SecurityTokenInclusionMode)
    """
    @property
    def X509ReferenceStyle(self) -> X509KeyIdentifierClauseType:
        """
        Get: X509ReferenceStyle(self: X509SecurityTokenParameters) -> X509KeyIdentifierClauseType
        Set: X509ReferenceStyle(self: X509SecurityTokenParameters) = value
        """
        ...



