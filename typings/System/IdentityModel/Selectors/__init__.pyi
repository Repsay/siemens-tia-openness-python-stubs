# encoding: utf-8
# module System.IdentityModel.Selectors calls itself Selectors
# from System.IdentityModel.Selectors, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.IdentityModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (AsyncCallback, Enum, IAsyncResult, IDisposable, TimeSpan, 
    Uri)

from System.Collections import IDictionary, IEnumerable, IList

from System.Collections.ObjectModel import Collection, ReadOnlyCollection

from System.IdentityModel.Claims import ClaimSet

from System.IdentityModel.Configuration import ICustomIdentityConfiguration

from System.IdentityModel.Tokens import (GenericXmlSecurityToken, SecurityKey, 
    SecurityKeyIdentifier, SecurityKeyIdentifierClause, SecurityKeyType, 
    SecurityKeyUsage, SecurityToken)

from System.Net import NetworkCredential

from System.Security.Cryptography.X509Certificates import (X509Certificate2, 
    X509ChainPolicy)

from System.Security.Principal import IIdentity, TokenImpersonationLevel

from System.Web.Security import MembershipProvider

from System.Xml import XmlElement, XmlReader, XmlWriter

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    SecurityTokenRequirement, SecurityTokenResolver, SecurityTokenSerializer, 
    SecurityTokenVersion, TValue, UserNamePasswordValidator, field#)
"""

# no functions
# classes

class AudienceUriMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AudienceUriMode, values: Always (1), BearerKeyOnly (2), Never (0) """
    Always: AudienceUriMode = ...
    BearerKeyOnly: AudienceUriMode = ...
    Never: AudienceUriMode = ...
    value__ = ...


class AudienceUriModeValidationHelper: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def IsDefined(validationMode:AudienceUriMode) -> bool:
        """ IsDefined(validationMode: AudienceUriMode) -> bool """
        ...

    __all__: list = ...


class CardSpaceException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CardSpaceException()
    CardSpaceException(message: str)
    CardSpaceException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class CardSpacePolicyElement: # skipped bases: <type 'object'>, <type 'object'>
    """ CardSpacePolicyElement(target: XmlElement, issuer: XmlElement, parameters: Collection[XmlElement], privacyNoticeLink: Uri, privacyNoticeVersion: int, isManagedIssuer: bool) """
    @property
    def IsManagedIssuer(self) -> bool:
        """
        Get: IsManagedIssuer(self: CardSpacePolicyElement) -> bool
        Set: IsManagedIssuer(self: CardSpacePolicyElement) = value
        """
        ...

    @property
    def Issuer(self) -> XmlElement:
        """
        Get: Issuer(self: CardSpacePolicyElement) -> XmlElement
        Set: Issuer(self: CardSpacePolicyElement) = value
        """
        ...

    @property
    def Parameters(self) -> Collection:
        """ Get: Parameters(self: CardSpacePolicyElement) -> Collection[XmlElement] """
        ...

    @property
    def PolicyNoticeLink(self) -> Uri:
        """
        Get: PolicyNoticeLink(self: CardSpacePolicyElement) -> Uri
        Set: PolicyNoticeLink(self: CardSpacePolicyElement) = value
        """
        ...

    @property
    def PolicyNoticeVersion(self) -> int:
        """
        Get: PolicyNoticeVersion(self: CardSpacePolicyElement) -> int
        Set: PolicyNoticeVersion(self: CardSpacePolicyElement) = value
        """
        ...

    @property
    def Target(self) -> XmlElement:
        """
        Get: Target(self: CardSpacePolicyElement) -> XmlElement
        Set: Target(self: CardSpacePolicyElement) = value
        """
        ...



class CardSpaceSelector: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetToken(*__args) -> GenericXmlSecurityToken:
        """
        GetToken(endpoint: XmlElement, policy: IEnumerable[XmlElement], requiredRemoteTokenIssuer: XmlElement, tokenSerializer: SecurityTokenSerializer) -> GenericXmlSecurityToken
        GetToken(policyChain: Array[CardSpacePolicyElement], tokenSerializer: SecurityTokenSerializer) -> GenericXmlSecurityToken
        """
        ...

    @staticmethod
    def Import(fileName:str): # -> 
        """ Import(fileName: str) """
        ...

    @staticmethod
    def Manage(): # -> 
        """ Manage() """
        ...

    __all__: list = ...


class SecurityTokenAuthenticator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CanValidateToken(self, token:SecurityToken) -> bool:
        """ CanValidateToken(self: SecurityTokenAuthenticator, token: SecurityToken) -> bool """
        ...

    def CanValidateTokenCore(self, *args): #cannot find CLR method
        """ CanValidateTokenCore(self: SecurityTokenAuthenticator, token: SecurityToken) -> bool """
        ...

    def ValidateToken(self, token:SecurityToken) -> ReadOnlyCollection:
        """ ValidateToken(self: SecurityTokenAuthenticator, token: SecurityToken) -> ReadOnlyCollection[IAuthorizationPolicy] """
        ...

    def ValidateTokenCore(self, *args): #cannot find CLR method
        """ ValidateTokenCore(self: SecurityTokenAuthenticator, token: SecurityToken) -> ReadOnlyCollection[IAuthorizationPolicy] """
        ...


class UserNameSecurityTokenAuthenticator(SecurityTokenAuthenticator): # skipped bases: <type 'object'>
    """ no doc """
    def ValidateUserNamePasswordCore(self, *args): #cannot find CLR method
        """ ValidateUserNamePasswordCore(self: UserNameSecurityTokenAuthenticator, userName: str, password: str) -> ReadOnlyCollection[IAuthorizationPolicy] """
        ...


class CustomUserNameSecurityTokenAuthenticator(UserNameSecurityTokenAuthenticator): # skipped bases: <type 'object'>
    """ CustomUserNameSecurityTokenAuthenticator(validator: UserNamePasswordValidator) """
    def __new__(cls, validator) -> Self: # Not found arg types: {'validator': 'UserNamePasswordValidator'}
        """ __new__(cls: type, validator: UserNamePasswordValidator) """
        ...


class IdentityValidationException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    IdentityValidationException()
    IdentityValidationException(message: str)
    IdentityValidationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class WindowsSecurityTokenAuthenticator(SecurityTokenAuthenticator): # skipped bases: <type 'object'>
    """
    WindowsSecurityTokenAuthenticator()
    WindowsSecurityTokenAuthenticator(includeWindowsGroups: bool)
    """
    def __new__(cls, includeWindowsGroups:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, includeWindowsGroups: bool)
        """
        ...


class KerberosSecurityTokenAuthenticator(WindowsSecurityTokenAuthenticator): # skipped bases: <type 'object'>
    """
    KerberosSecurityTokenAuthenticator()
    KerberosSecurityTokenAuthenticator(includeWindowsGroups: bool)
    """
    pass

class SecurityTokenProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def SupportsTokenCancellation(self) -> bool:
        """ Get: SupportsTokenCancellation(self: SecurityTokenProvider) -> bool """
        ...

    @property
    def SupportsTokenRenewal(self) -> bool:
        """ Get: SupportsTokenRenewal(self: SecurityTokenProvider) -> bool """
        ...


    def BeginCancelToken(self, timeout:TimeSpan, token:SecurityToken, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginCancelToken(self: SecurityTokenProvider, timeout: TimeSpan, token: SecurityToken, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginCancelTokenCore(self, *args): #cannot find CLR method
        """ BeginCancelTokenCore(self: SecurityTokenProvider, timeout: TimeSpan, token: SecurityToken, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginGetToken(self, timeout:TimeSpan, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginGetToken(self: SecurityTokenProvider, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginGetTokenCore(self, *args): #cannot find CLR method
        """ BeginGetTokenCore(self: SecurityTokenProvider, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginRenewToken(self, timeout:TimeSpan, tokenToBeRenewed:SecurityToken, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginRenewToken(self: SecurityTokenProvider, timeout: TimeSpan, tokenToBeRenewed: SecurityToken, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginRenewTokenCore(self, *args): #cannot find CLR method
        """ BeginRenewTokenCore(self: SecurityTokenProvider, timeout: TimeSpan, tokenToBeRenewed: SecurityToken, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def CancelToken(self, timeout:TimeSpan, token:SecurityToken): # -> 
        """ CancelToken(self: SecurityTokenProvider, timeout: TimeSpan, token: SecurityToken) """
        ...

    def CancelTokenCore(self, *args): #cannot find CLR method
        """ CancelTokenCore(self: SecurityTokenProvider, timeout: TimeSpan, token: SecurityToken) """
        ...

    def EndCancelToken(self, result:IAsyncResult): # -> 
        """ EndCancelToken(self: SecurityTokenProvider, result: IAsyncResult) """
        ...

    def EndCancelTokenCore(self, *args): #cannot find CLR method
        """ EndCancelTokenCore(self: SecurityTokenProvider, result: IAsyncResult) """
        ...

    def EndGetToken(self, result:IAsyncResult) -> SecurityToken:
        """ EndGetToken(self: SecurityTokenProvider, result: IAsyncResult) -> SecurityToken """
        ...

    def EndGetTokenCore(self, *args): #cannot find CLR method
        """ EndGetTokenCore(self: SecurityTokenProvider, result: IAsyncResult) -> SecurityToken """
        ...

    def EndRenewToken(self, result:IAsyncResult) -> SecurityToken:
        """ EndRenewToken(self: SecurityTokenProvider, result: IAsyncResult) -> SecurityToken """
        ...

    def EndRenewTokenCore(self, *args): #cannot find CLR method
        """ EndRenewTokenCore(self: SecurityTokenProvider, result: IAsyncResult) -> SecurityToken """
        ...

    def GetToken(self, timeout:TimeSpan) -> SecurityToken:
        """ GetToken(self: SecurityTokenProvider, timeout: TimeSpan) -> SecurityToken """
        ...

    def GetTokenCore(self, *args): #cannot find CLR method
        """ GetTokenCore(self: SecurityTokenProvider, timeout: TimeSpan) -> SecurityToken """
        ...

    def RenewToken(self, timeout:TimeSpan, tokenToBeRenewed:SecurityToken) -> SecurityToken:
        """ RenewToken(self: SecurityTokenProvider, timeout: TimeSpan, tokenToBeRenewed: SecurityToken) -> SecurityToken """
        ...

    def RenewTokenCore(self, *args): #cannot find CLR method
        """ RenewTokenCore(self: SecurityTokenProvider, timeout: TimeSpan, tokenToBeRenewed: SecurityToken) -> SecurityToken """
        ...

    def SecurityTokenAsyncResult(self, *args): #cannot find CLR method
        """ SecurityTokenAsyncResult(token: SecurityToken, callback: AsyncCallback, state: object) """
        ...



class KerberosSecurityTokenProvider(SecurityTokenProvider): # skipped bases: <type 'object'>
    """
    KerberosSecurityTokenProvider(servicePrincipalName: str)
    KerberosSecurityTokenProvider(servicePrincipalName: str, tokenImpersonationLevel: TokenImpersonationLevel)
    KerberosSecurityTokenProvider(servicePrincipalName: str, tokenImpersonationLevel: TokenImpersonationLevel, networkCredential: NetworkCredential)
    """
    @property
    def NetworkCredential(self) -> NetworkCredential:
        """ Get: NetworkCredential(self: KerberosSecurityTokenProvider) -> NetworkCredential """
        ...

    @property
    def ServicePrincipalName(self) -> str:
        """ Get: ServicePrincipalName(self: KerberosSecurityTokenProvider) -> str """
        ...

    @property
    def TokenImpersonationLevel(self) -> TokenImpersonationLevel:
        """ Get: TokenImpersonationLevel(self: KerberosSecurityTokenProvider) -> TokenImpersonationLevel """
        ...


    def __new__(cls, servicePrincipalName:str, tokenImpersonationLevel:TokenImpersonationLevel = ..., networkCredential:NetworkCredential = ...) -> Self:
        """
        __new__(cls: type, servicePrincipalName: str)
        __new__(cls: type, servicePrincipalName: str, tokenImpersonationLevel: TokenImpersonationLevel)
        __new__(cls: type, servicePrincipalName: str, tokenImpersonationLevel: TokenImpersonationLevel, networkCredential: NetworkCredential)
        """
        ...


class PolicyValidationException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PolicyValidationException()
    PolicyValidationException(message: str)
    PolicyValidationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class RsaSecurityTokenAuthenticator(SecurityTokenAuthenticator): # skipped bases: <type 'object'>
    """ RsaSecurityTokenAuthenticator() """
    pass

class SamlSecurityTokenAuthenticator(SecurityTokenAuthenticator): # skipped bases: <type 'object'>
    """
    SamlSecurityTokenAuthenticator(supportingAuthenticators: IList[SecurityTokenAuthenticator])
    SamlSecurityTokenAuthenticator(supportingAuthenticators: IList[SecurityTokenAuthenticator], maxClockSkew: TimeSpan)
    """
    @property
    def AllowedAudienceUris(self) -> IList:
        """ Get: AllowedAudienceUris(self: SamlSecurityTokenAuthenticator) -> IList[str] """
        ...

    @property
    def AudienceUriMode(self) -> AudienceUriMode:
        """
        Get: AudienceUriMode(self: SamlSecurityTokenAuthenticator) -> AudienceUriMode
        Set: AudienceUriMode(self: SamlSecurityTokenAuthenticator) = value
        """
        ...


    def ResolveClaimSet(self, *__args:SecurityToken) -> ClaimSet:
        """
        ResolveClaimSet(self: SamlSecurityTokenAuthenticator, token: SecurityToken) -> ClaimSet
        ResolveClaimSet(self: SamlSecurityTokenAuthenticator, keyIdentifier: SecurityKeyIdentifier) -> ClaimSet
        """
        ...

    def ResolveIdentity(self, *__args:SecurityToken) -> IIdentity:
        """
        ResolveIdentity(self: SamlSecurityTokenAuthenticator, token: SecurityToken) -> IIdentity
        ResolveIdentity(self: SamlSecurityTokenAuthenticator, keyIdentifier: SecurityKeyIdentifier) -> IIdentity
        """
        ...

    def ValidateAudienceRestriction(self, *args): #cannot find CLR method
        """ ValidateAudienceRestriction(self: SamlSecurityTokenAuthenticator, audienceRestrictionCondition: SamlAudienceRestrictionCondition) -> bool """
        ...

    def __new__(cls, supportingAuthenticators:IList, maxClockSkew:TimeSpan = ...) -> Self:
        """
        __new__(cls: type, supportingAuthenticators: IList[SecurityTokenAuthenticator])
        __new__(cls: type, supportingAuthenticators: IList[SecurityTokenAuthenticator], maxClockSkew: TimeSpan)
        """
        ...


class SecurityTokenManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateSecurityTokenAuthenticator(self, tokenRequirement, outOfBandTokenResolver): # -> Tuple_[SecurityTokenAuthenticator, SecurityTokenResolver]
        """ CreateSecurityTokenAuthenticator(self: SecurityTokenManager, tokenRequirement: SecurityTokenRequirement) -> (SecurityTokenAuthenticator, SecurityTokenResolver) """
        ...

    def CreateSecurityTokenProvider(self, tokenRequirement) -> SecurityTokenProvider: # Not found arg types: {'tokenRequirement': 'SecurityTokenRequirement'}
        """ CreateSecurityTokenProvider(self: SecurityTokenManager, tokenRequirement: SecurityTokenRequirement) -> SecurityTokenProvider """
        ...

    def CreateSecurityTokenSerializer(self, version): # -> SecurityTokenSerializer # Not found arg types: {'version': 'SecurityTokenVersion'}
        """ CreateSecurityTokenSerializer(self: SecurityTokenManager, version: SecurityTokenVersion) -> SecurityTokenSerializer """
        ...


class SecurityTokenRequirement: # skipped bases: <type 'object'>, <type 'object'>
    """ SecurityTokenRequirement() """
    @property
    def IsOptionalTokenProperty(self) -> str:
        """ Get: IsOptionalTokenProperty() -> str """
        ...

    @property
    def KeySize(self) -> int:
        """
        Get: KeySize(self: SecurityTokenRequirement) -> int
        Set: KeySize(self: SecurityTokenRequirement) = value
        """
        ...

    @property
    def KeySizeProperty(self) -> str:
        """ Get: KeySizeProperty() -> str """
        ...

    @property
    def KeyType(self) -> SecurityKeyType:
        """
        Get: KeyType(self: SecurityTokenRequirement) -> SecurityKeyType
        Set: KeyType(self: SecurityTokenRequirement) = value
        """
        ...

    @property
    def KeyTypeProperty(self) -> str:
        """ Get: KeyTypeProperty() -> str """
        ...

    @property
    def KeyUsage(self) -> SecurityKeyUsage:
        """
        Get: KeyUsage(self: SecurityTokenRequirement) -> SecurityKeyUsage
        Set: KeyUsage(self: SecurityTokenRequirement) = value
        """
        ...

    @property
    def KeyUsageProperty(self) -> str:
        """ Get: KeyUsageProperty() -> str """
        ...

    @property
    def PeerAuthenticationMode(self) -> str:
        """ Get: PeerAuthenticationMode() -> str """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: SecurityTokenRequirement) -> IDictionary[str, object] """
        ...

    @property
    def RequireCryptographicToken(self) -> bool:
        """
        Get: RequireCryptographicToken(self: SecurityTokenRequirement) -> bool
        Set: RequireCryptographicToken(self: SecurityTokenRequirement) = value
        """
        ...

    @property
    def RequireCryptographicTokenProperty(self) -> str:
        """ Get: RequireCryptographicTokenProperty() -> str """
        ...

    @property
    def TokenType(self) -> str:
        """
        Get: TokenType(self: SecurityTokenRequirement) -> str
        Set: TokenType(self: SecurityTokenRequirement) = value
        """
        ...

    @property
    def TokenTypeProperty(self) -> str:
        """ Get: TokenTypeProperty() -> str """
        ...


    def GetProperty(self, propertyName:str): # -> TValue
        """ GetProperty[TValue](self: SecurityTokenRequirement, propertyName: str) -> TValue """
        ...

    def TryGetProperty(self, propertyName, result): # -> Tuple_[bool, TValue]
        """ TryGetProperty[TValue](self: SecurityTokenRequirement, propertyName: str) -> (bool, TValue) """
        ...



class SecurityTokenResolver(ICustomIdentityConfiguration): # skipped bases: <type 'object'>
    """ no doc """
    @staticmethod
    def CreateDefaultSecurityTokenResolver(tokens:ReadOnlyCollection, canMatchLocalId:bool) -> SecurityTokenResolver:
        """ CreateDefaultSecurityTokenResolver(tokens: ReadOnlyCollection[SecurityToken], canMatchLocalId: bool) -> SecurityTokenResolver """
        ...

    def ResolveSecurityKey(self, keyIdentifierClause:SecurityKeyIdentifierClause) -> SecurityKey:
        """ ResolveSecurityKey(self: SecurityTokenResolver, keyIdentifierClause: SecurityKeyIdentifierClause) -> SecurityKey """
        ...

    def ResolveToken(self, *__args:SecurityKeyIdentifier) -> SecurityToken:
        """
        ResolveToken(self: SecurityTokenResolver, keyIdentifier: SecurityKeyIdentifier) -> SecurityToken
        ResolveToken(self: SecurityTokenResolver, keyIdentifierClause: SecurityKeyIdentifierClause) -> SecurityToken
        """
        ...

    def TryResolveSecurityKey(self, keyIdentifierClause, key) -> Tuple_[bool, SecurityKey]:
        """ TryResolveSecurityKey(self: SecurityTokenResolver, keyIdentifierClause: SecurityKeyIdentifierClause) -> (bool, SecurityKey) """
        ...

    def TryResolveSecurityKeyCore(self, *args): #cannot find CLR method
        """ TryResolveSecurityKeyCore(self: SecurityTokenResolver, keyIdentifierClause: SecurityKeyIdentifierClause) -> (bool, SecurityKey) """
        ...

    def TryResolveToken(self, *__args:SecurityKeyIdentifier) -> Tuple_[bool, SecurityToken]:
        """
        TryResolveToken(self: SecurityTokenResolver, keyIdentifier: SecurityKeyIdentifier) -> (bool, SecurityToken)
        TryResolveToken(self: SecurityTokenResolver, keyIdentifierClause: SecurityKeyIdentifierClause) -> (bool, SecurityToken)
        """
        ...

    def TryResolveTokenCore(self, *args): #cannot find CLR method
        """
        TryResolveTokenCore(self: SecurityTokenResolver, keyIdentifier: SecurityKeyIdentifier) -> (bool, SecurityToken)
        TryResolveTokenCore(self: SecurityTokenResolver, keyIdentifierClause: SecurityKeyIdentifierClause) -> (bool, SecurityToken)
        """
        ...


class SecurityTokenSerializer: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CanReadKeyIdentifier(self, reader:XmlReader) -> bool:
        """ CanReadKeyIdentifier(self: SecurityTokenSerializer, reader: XmlReader) -> bool """
        ...

    def CanReadKeyIdentifierClause(self, reader:XmlReader) -> bool:
        """ CanReadKeyIdentifierClause(self: SecurityTokenSerializer, reader: XmlReader) -> bool """
        ...

    def CanReadKeyIdentifierClauseCore(self, *args): #cannot find CLR method
        """ CanReadKeyIdentifierClauseCore(self: SecurityTokenSerializer, reader: XmlReader) -> bool """
        ...

    def CanReadKeyIdentifierCore(self, *args): #cannot find CLR method
        """ CanReadKeyIdentifierCore(self: SecurityTokenSerializer, reader: XmlReader) -> bool """
        ...

    def CanReadToken(self, reader:XmlReader) -> bool:
        """ CanReadToken(self: SecurityTokenSerializer, reader: XmlReader) -> bool """
        ...

    def CanReadTokenCore(self, *args): #cannot find CLR method
        """ CanReadTokenCore(self: SecurityTokenSerializer, reader: XmlReader) -> bool """
        ...

    def CanWriteKeyIdentifier(self, keyIdentifier:SecurityKeyIdentifier) -> bool:
        """ CanWriteKeyIdentifier(self: SecurityTokenSerializer, keyIdentifier: SecurityKeyIdentifier) -> bool """
        ...

    def CanWriteKeyIdentifierClause(self, keyIdentifierClause:SecurityKeyIdentifierClause) -> bool:
        """ CanWriteKeyIdentifierClause(self: SecurityTokenSerializer, keyIdentifierClause: SecurityKeyIdentifierClause) -> bool """
        ...

    def CanWriteKeyIdentifierClauseCore(self, *args): #cannot find CLR method
        """ CanWriteKeyIdentifierClauseCore(self: SecurityTokenSerializer, keyIdentifierClause: SecurityKeyIdentifierClause) -> bool """
        ...

    def CanWriteKeyIdentifierCore(self, *args): #cannot find CLR method
        """ CanWriteKeyIdentifierCore(self: SecurityTokenSerializer, keyIdentifier: SecurityKeyIdentifier) -> bool """
        ...

    def CanWriteToken(self, token:SecurityToken) -> bool:
        """ CanWriteToken(self: SecurityTokenSerializer, token: SecurityToken) -> bool """
        ...

    def CanWriteTokenCore(self, *args): #cannot find CLR method
        """ CanWriteTokenCore(self: SecurityTokenSerializer, token: SecurityToken) -> bool """
        ...

    def ReadKeyIdentifier(self, reader:XmlReader) -> SecurityKeyIdentifier:
        """ ReadKeyIdentifier(self: SecurityTokenSerializer, reader: XmlReader) -> SecurityKeyIdentifier """
        ...

    def ReadKeyIdentifierClause(self, reader:XmlReader) -> SecurityKeyIdentifierClause:
        """ ReadKeyIdentifierClause(self: SecurityTokenSerializer, reader: XmlReader) -> SecurityKeyIdentifierClause """
        ...

    def ReadKeyIdentifierClauseCore(self, *args): #cannot find CLR method
        """ ReadKeyIdentifierClauseCore(self: SecurityTokenSerializer, reader: XmlReader) -> SecurityKeyIdentifierClause """
        ...

    def ReadKeyIdentifierCore(self, *args): #cannot find CLR method
        """ ReadKeyIdentifierCore(self: SecurityTokenSerializer, reader: XmlReader) -> SecurityKeyIdentifier """
        ...

    def ReadToken(self, reader:XmlReader, tokenResolver:SecurityTokenResolver) -> SecurityToken:
        """ ReadToken(self: SecurityTokenSerializer, reader: XmlReader, tokenResolver: SecurityTokenResolver) -> SecurityToken """
        ...

    def ReadTokenCore(self, *args): #cannot find CLR method
        """ ReadTokenCore(self: SecurityTokenSerializer, reader: XmlReader, tokenResolver: SecurityTokenResolver) -> SecurityToken """
        ...

    def WriteKeyIdentifier(self, writer:XmlWriter, keyIdentifier:SecurityKeyIdentifier): # -> 
        """ WriteKeyIdentifier(self: SecurityTokenSerializer, writer: XmlWriter, keyIdentifier: SecurityKeyIdentifier) """
        ...

    def WriteKeyIdentifierClause(self, writer:XmlWriter, keyIdentifierClause:SecurityKeyIdentifierClause): # -> 
        """ WriteKeyIdentifierClause(self: SecurityTokenSerializer, writer: XmlWriter, keyIdentifierClause: SecurityKeyIdentifierClause) """
        ...

    def WriteKeyIdentifierClauseCore(self, *args): #cannot find CLR method
        """ WriteKeyIdentifierClauseCore(self: SecurityTokenSerializer, writer: XmlWriter, keyIdentifierClause: SecurityKeyIdentifierClause) """
        ...

    def WriteKeyIdentifierCore(self, *args): #cannot find CLR method
        """ WriteKeyIdentifierCore(self: SecurityTokenSerializer, writer: XmlWriter, keyIdentifier: SecurityKeyIdentifier) """
        ...

    def WriteToken(self, writer:XmlWriter, token:SecurityToken): # -> 
        """ WriteToken(self: SecurityTokenSerializer, writer: XmlWriter, token: SecurityToken) """
        ...

    def WriteTokenCore(self, *args): #cannot find CLR method
        """ WriteTokenCore(self: SecurityTokenSerializer, writer: XmlWriter, token: SecurityToken) """
        ...


class SecurityTokenVersion: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetSecuritySpecifications(self) -> ReadOnlyCollection:
        """ GetSecuritySpecifications(self: SecurityTokenVersion) -> ReadOnlyCollection[str] """
        ...


class ServiceBusyException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ServiceBusyException()
    ServiceBusyException(message: str)
    ServiceBusyException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ServiceNotStartedException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ServiceNotStartedException()
    ServiceNotStartedException(message: str)
    ServiceNotStartedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class StsCommunicationException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    StsCommunicationException()
    StsCommunicationException(message: str)
    StsCommunicationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class UnsupportedPolicyOptionsException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    UnsupportedPolicyOptionsException()
    UnsupportedPolicyOptionsException(message: str)
    UnsupportedPolicyOptionsException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class UntrustedRecipientException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    UntrustedRecipientException()
    UntrustedRecipientException(message: str)
    UntrustedRecipientException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class UserCancellationException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    UserCancellationException()
    UserCancellationException(message: str)
    UserCancellationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class UserNamePasswordValidator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """

    @staticmethod
    def CreateMembershipProviderValidator(provider:MembershipProvider) -> UserNamePasswordValidator:
        """ CreateMembershipProviderValidator(provider: MembershipProvider) -> UserNamePasswordValidator """
        ...

    def Validate(self, userName:str, password:str): # -> 
        """ Validate(self: UserNamePasswordValidator, userName: str, password: str) """
        ...


class UserNameSecurityTokenProvider(SecurityTokenProvider): # skipped bases: <type 'object'>
    """ UserNameSecurityTokenProvider(userName: str, password: str) """
    def __new__(cls, userName:str, password:str) -> Self:
        """ __new__(cls: type, userName: str, password: str) """
        ...


class WindowsUserNameSecurityTokenAuthenticator(UserNameSecurityTokenAuthenticator): # skipped bases: <type 'object'>
    """
    WindowsUserNameSecurityTokenAuthenticator()
    WindowsUserNameSecurityTokenAuthenticator(includeWindowsGroups: bool)
    """
    def __new__(cls, includeWindowsGroups:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, includeWindowsGroups: bool)
        """
        ...


class X509CertificateValidator(ICustomIdentityConfiguration): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ChainTrust(self) -> X509CertificateValidator:
        """ Get: ChainTrust() -> X509CertificateValidator """
        ...

    @property
    def PeerOrChainTrust(self) -> X509CertificateValidator:
        """ Get: PeerOrChainTrust() -> X509CertificateValidator """
        ...

    @property
    def PeerTrust(self) -> X509CertificateValidator:
        """ Get: PeerTrust() -> X509CertificateValidator """
        ...


    @staticmethod
    def CreateChainTrustValidator(useMachineContext:bool, chainPolicy:X509ChainPolicy) -> X509CertificateValidator:
        """ CreateChainTrustValidator(useMachineContext: bool, chainPolicy: X509ChainPolicy) -> X509CertificateValidator """
        ...

    @staticmethod
    def CreatePeerOrChainTrustValidator(useMachineContext:bool, chainPolicy:X509ChainPolicy) -> X509CertificateValidator:
        """ CreatePeerOrChainTrustValidator(useMachineContext: bool, chainPolicy: X509ChainPolicy) -> X509CertificateValidator """
        ...

    def Validate(self, certificate:X509Certificate2): # -> 
        """ Validate(self: X509CertificateValidator, certificate: X509Certificate2) """
        ...



class X509SecurityTokenAuthenticator(SecurityTokenAuthenticator): # skipped bases: <type 'object'>
    """
    X509SecurityTokenAuthenticator()
    X509SecurityTokenAuthenticator(validator: X509CertificateValidator)
    X509SecurityTokenAuthenticator(validator: X509CertificateValidator, mapToWindows: bool)
    X509SecurityTokenAuthenticator(validator: X509CertificateValidator, mapToWindows: bool, includeWindowsGroups: bool)
    """
    @property
    def MapCertificateToWindowsAccount(self) -> bool:
        """ Get: MapCertificateToWindowsAccount(self: X509SecurityTokenAuthenticator) -> bool """
        ...


    def __new__(cls, validator:X509CertificateValidator = ..., mapToWindows:bool = ..., includeWindowsGroups:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, validator: X509CertificateValidator)
        __new__(cls: type, validator: X509CertificateValidator, mapToWindows: bool)
        __new__(cls: type, validator: X509CertificateValidator, mapToWindows: bool, includeWindowsGroups: bool)
        """
        ...


class X509SecurityTokenProvider(IDisposable, SecurityTokenProvider): # skipped bases: <type 'object'>
    """
    X509SecurityTokenProvider(certificate: X509Certificate2)
    X509SecurityTokenProvider(storeLocation: StoreLocation, storeName: StoreName, findType: X509FindType, findValue: object)
    """
    @property
    def Certificate(self) -> X509Certificate2:
        """ Get: Certificate(self: X509SecurityTokenProvider) -> X509Certificate2 """
        ...


    def __new__(cls, *__args:X509Certificate2) -> Self:
        """
        __new__(cls: type, certificate: X509Certificate2)
        __new__(cls: type, storeLocation: StoreLocation, storeName: StoreName, findType: X509FindType, findValue: object)
        """
        ...


