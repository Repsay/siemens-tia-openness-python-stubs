# encoding: utf-8
# module System.IdentityModel.Configuration calls itself Configuration
# from System.IdentityModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import TimeSpan, Type

from System.Configuration import (ConfigurationElement, 
    ConfigurationElementCollection, ConfigurationSection)

from System.IdentityModel import SecurityTokenService

from System.IdentityModel.Protocols.WSTrust import (
    WSTrust13RequestSerializer, WSTrust13ResponseSerializer, 
    WSTrustFeb2005RequestSerializer, WSTrustFeb2005ResponseSerializer)

from System.IdentityModel.Selectors import (AudienceUriMode, 
    SecurityTokenResolver, X509CertificateValidator)

from System.IdentityModel.Tokens import (AudienceRestriction, 
    IssuerNameRegistry, SecurityTokenHandlerCollection, 
    SecurityTokenHandlerCollectionManager, SessionSecurityTokenCache, 
    SigningCredentials, TokenReplayCache)

from System.Security.Claims import (ClaimsAuthenticationManager, 
    ClaimsAuthorizationManager)

from System.Security.Cryptography.X509Certificates import (StoreLocation, 
    X509Certificate2, X509RevocationMode)

from System.ServiceModel.Security import X509CertificateValidationMode

from System.Xml import XmlElement, XmlNodeList

"""The following names are not found in the module: RuntimeType, T
"""

# no functions
# classes

class AudienceUriElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ AudienceUriElement() """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: AudienceUriElement) -> str
        Set: Value(self: AudienceUriElement) = value
        """
        ...



class AudienceUriElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ AudienceUriElementCollection() """
    @property
    def Mode(self) -> AudienceUriMode:
        """
        Get: Mode(self: AudienceUriElementCollection) -> AudienceUriMode
        Set: Mode(self: AudienceUriElementCollection) = value
        """
        ...



class ConfigurationElementInterceptor(ConfigurationElement): # skipped bases: <type 'object'>
    """ ConfigurationElementInterceptor() """
    @property
    def ChildNodes(self) -> XmlNodeList:
        """ Get: ChildNodes(self: ConfigurationElementInterceptor) -> XmlNodeList """
        ...

    @property
    def ElementAsXml(self) -> XmlElement:
        """ Get: ElementAsXml(self: ConfigurationElementInterceptor) -> XmlElement """
        ...



class CustomTypeElement(ConfigurationElementInterceptor): # skipped bases: <type 'object'>
    """ CustomTypeElement() """
    @property
    def IsConfigured(self) -> bool:
        """ Get: IsConfigured(self: CustomTypeElement) -> bool """
        ...

    @property
    def Type(self) -> Type:
        """
        Get: Type(self: CustomTypeElement) -> Type
        Set: Type(self: CustomTypeElement) = value
        """
        ...


    @staticmethod
    def Resolve(customTypeElement:CustomTypeElement): # -> T
        """ Resolve[T](customTypeElement: CustomTypeElement) -> T """
        ...


class ICustomIdentityConfiguration: # skipped bases: <type 'object'>
    """ no doc """
    def LoadCustomConfiguration(self, nodeList:XmlNodeList): # -> 
        """ LoadCustomConfiguration(self: ICustomIdentityConfiguration, nodeList: XmlNodeList) """
        ...


class IdentityConfiguration: # skipped bases: <type 'object'>, <type 'object'>
    """
    IdentityConfiguration()
    IdentityConfiguration(serviceCertificate: X509Certificate2)
    IdentityConfiguration(loadConfig: bool)
    IdentityConfiguration(loadConfig: bool, serviceCertificate: X509Certificate2)
    IdentityConfiguration(identityConfigurationName: str)
    IdentityConfiguration(identityConfigurationName: str, serviceCertificate: X509Certificate2)
    """
    @property
    def AudienceRestriction(self) -> AudienceRestriction:
        """
        Get: AudienceRestriction(self: IdentityConfiguration) -> AudienceRestriction
        Set: AudienceRestriction(self: IdentityConfiguration) = value
        """
        ...

    @property
    def Caches(self) -> IdentityModelCaches:
        """
        Get: Caches(self: IdentityConfiguration) -> IdentityModelCaches
        Set: Caches(self: IdentityConfiguration) = value
        """
        ...

    @property
    def CertificateValidationMode(self) -> X509CertificateValidationMode:
        """
        Get: CertificateValidationMode(self: IdentityConfiguration) -> X509CertificateValidationMode
        Set: CertificateValidationMode(self: IdentityConfiguration) = value
        """
        ...

    @property
    def CertificateValidator(self) -> X509CertificateValidator:
        """
        Get: CertificateValidator(self: IdentityConfiguration) -> X509CertificateValidator
        Set: CertificateValidator(self: IdentityConfiguration) = value
        """
        ...

    @property
    def ClaimsAuthenticationManager(self) -> ClaimsAuthenticationManager:
        """
        Get: ClaimsAuthenticationManager(self: IdentityConfiguration) -> ClaimsAuthenticationManager
        Set: ClaimsAuthenticationManager(self: IdentityConfiguration) = value
        """
        ...

    @property
    def ClaimsAuthorizationManager(self) -> ClaimsAuthorizationManager:
        """
        Get: ClaimsAuthorizationManager(self: IdentityConfiguration) -> ClaimsAuthorizationManager
        Set: ClaimsAuthorizationManager(self: IdentityConfiguration) = value
        """
        ...

    @property
    def DetectReplayedTokens(self) -> bool:
        """
        Get: DetectReplayedTokens(self: IdentityConfiguration) -> bool
        Set: DetectReplayedTokens(self: IdentityConfiguration) = value
        """
        ...

    @property
    def IsInitialized(self) -> bool:
        """ Get: IsInitialized(self: IdentityConfiguration) -> bool """
        ...

    @property
    def IssuerNameRegistry(self) -> IssuerNameRegistry:
        """
        Get: IssuerNameRegistry(self: IdentityConfiguration) -> IssuerNameRegistry
        Set: IssuerNameRegistry(self: IdentityConfiguration) = value
        """
        ...

    @property
    def IssuerTokenResolver(self) -> SecurityTokenResolver:
        """
        Get: IssuerTokenResolver(self: IdentityConfiguration) -> SecurityTokenResolver
        Set: IssuerTokenResolver(self: IdentityConfiguration) = value
        """
        ...

    @property
    def MaxClockSkew(self) -> TimeSpan:
        """
        Get: MaxClockSkew(self: IdentityConfiguration) -> TimeSpan
        Set: MaxClockSkew(self: IdentityConfiguration) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IdentityConfiguration) -> str """
        ...

    @property
    def RevocationMode(self) -> X509RevocationMode:
        """
        Get: RevocationMode(self: IdentityConfiguration) -> X509RevocationMode
        Set: RevocationMode(self: IdentityConfiguration) = value
        """
        ...

    @property
    def SaveBootstrapContext(self) -> bool:
        """
        Get: SaveBootstrapContext(self: IdentityConfiguration) -> bool
        Set: SaveBootstrapContext(self: IdentityConfiguration) = value
        """
        ...

    @property
    def SecurityTokenHandlerCollectionManager(self) -> SecurityTokenHandlerCollectionManager:
        """ Get: SecurityTokenHandlerCollectionManager(self: IdentityConfiguration) -> SecurityTokenHandlerCollectionManager """
        ...

    @property
    def SecurityTokenHandlers(self) -> SecurityTokenHandlerCollection:
        """ Get: SecurityTokenHandlers(self: IdentityConfiguration) -> SecurityTokenHandlerCollection """
        ...

    @property
    def ServiceCertificate(self) -> X509Certificate2:
        """
        Get: ServiceCertificate(self: IdentityConfiguration) -> X509Certificate2
        Set: ServiceCertificate(self: IdentityConfiguration) = value
        """
        ...

    @property
    def ServiceTokenResolver(self) -> SecurityTokenResolver:
        """
        Get: ServiceTokenResolver(self: IdentityConfiguration) -> SecurityTokenResolver
        Set: ServiceTokenResolver(self: IdentityConfiguration) = value
        """
        ...

    @property
    def TokenReplayCacheExpirationPeriod(self) -> TimeSpan:
        """
        Get: TokenReplayCacheExpirationPeriod(self: IdentityConfiguration) -> TimeSpan
        Set: TokenReplayCacheExpirationPeriod(self: IdentityConfiguration) = value
        """
        ...

    @property
    def TrustedStoreLocation(self) -> StoreLocation:
        """
        Get: TrustedStoreLocation(self: IdentityConfiguration) -> StoreLocation
        Set: TrustedStoreLocation(self: IdentityConfiguration) = value
        """
        ...


    def Initialize(self): # -> 
        """ Initialize(self: IdentityConfiguration) """
        ...

    def LoadConfiguration(self, *args): #cannot find CLR method
        """ LoadConfiguration(self: IdentityConfiguration, element: IdentityConfigurationElement) """
        ...

    def LoadHandlerConfiguration(self, *args): #cannot find CLR method
        """
        LoadHandlerConfiguration(self: IdentityConfiguration, element: IdentityConfigurationElement) -> SecurityTokenHandlerConfiguration
        LoadHandlerConfiguration(self: IdentityConfiguration, baseConfiguration: SecurityTokenHandlerConfiguration, element: SecurityTokenHandlerConfigurationElement) -> SecurityTokenHandlerConfiguration
        """
        ...

    def LoadHandlers(self, *args): #cannot find CLR method
        """ LoadHandlers(self: IdentityConfiguration, serviceElement: IdentityConfigurationElement) -> SecurityTokenHandlerCollectionManager """
        ...

    DefaultCertificateValidationMode: X509CertificateValidationMode = ...
    DefaultIssuerNameRegistryType = ...
    DefaultMaxClockSkew: TimeSpan = ...
    DefaultRevocationMode: X509RevocationMode = ...
    DefaultServiceName: str = ...
    DefaultTrustedStoreLocation: StoreLocation = ...


class IdentityConfigurationElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ IdentityConfigurationElement() """
    @property
    def AudienceUris(self) -> AudienceUriElementCollection:
        """ Get: AudienceUris(self: IdentityConfigurationElement) -> AudienceUriElementCollection """
        ...

    @property
    def Caches(self) -> IdentityModelCachesElement:
        """
        Get: Caches(self: IdentityConfigurationElement) -> IdentityModelCachesElement
        Set: Caches(self: IdentityConfigurationElement) = value
        """
        ...

    @property
    def CertificateValidation(self) -> X509CertificateValidationElement:
        """
        Get: CertificateValidation(self: IdentityConfigurationElement) -> X509CertificateValidationElement
        Set: CertificateValidation(self: IdentityConfigurationElement) = value
        """
        ...

    @property
    def ClaimsAuthenticationManager(self) -> CustomTypeElement:
        """
        Get: ClaimsAuthenticationManager(self: IdentityConfigurationElement) -> CustomTypeElement
        Set: ClaimsAuthenticationManager(self: IdentityConfigurationElement) = value
        """
        ...

    @property
    def ClaimsAuthorizationManager(self) -> CustomTypeElement:
        """
        Get: ClaimsAuthorizationManager(self: IdentityConfigurationElement) -> CustomTypeElement
        Set: ClaimsAuthorizationManager(self: IdentityConfigurationElement) = value
        """
        ...

    @property
    def IssuerNameRegistry(self) -> IssuerNameRegistryElement:
        """
        Get: IssuerNameRegistry(self: IdentityConfigurationElement) -> IssuerNameRegistryElement
        Set: IssuerNameRegistry(self: IdentityConfigurationElement) = value
        """
        ...

    @property
    def IssuerTokenResolver(self) -> CustomTypeElement:
        """
        Get: IssuerTokenResolver(self: IdentityConfigurationElement) -> CustomTypeElement
        Set: IssuerTokenResolver(self: IdentityConfigurationElement) = value
        """
        ...

    @property
    def MaximumClockSkew(self) -> TimeSpan:
        """
        Get: MaximumClockSkew(self: IdentityConfigurationElement) -> TimeSpan
        Set: MaximumClockSkew(self: IdentityConfigurationElement) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: IdentityConfigurationElement) -> str
        Set: Name(self: IdentityConfigurationElement) = value
        """
        ...

    @property
    def SaveBootstrapContext(self) -> bool:
        """
        Get: SaveBootstrapContext(self: IdentityConfigurationElement) -> bool
        Set: SaveBootstrapContext(self: IdentityConfigurationElement) = value
        """
        ...

    @property
    def SecurityTokenHandlerSets(self) -> SecurityTokenHandlerSetElementCollection:
        """ Get: SecurityTokenHandlerSets(self: IdentityConfigurationElement) -> SecurityTokenHandlerSetElementCollection """
        ...

    @property
    def ServiceTokenResolver(self) -> CustomTypeElement:
        """
        Get: ServiceTokenResolver(self: IdentityConfigurationElement) -> CustomTypeElement
        Set: ServiceTokenResolver(self: IdentityConfigurationElement) = value
        """
        ...

    @property
    def TokenReplayDetection(self) -> TokenReplayDetectionElement:
        """
        Get: TokenReplayDetection(self: IdentityConfigurationElement) -> TokenReplayDetectionElement
        Set: TokenReplayDetection(self: IdentityConfigurationElement) = value
        """
        ...



class IdentityConfigurationElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ IdentityConfigurationElementCollection() """
    def GetElement(self, name:str) -> IdentityConfigurationElement:
        """ GetElement(self: IdentityConfigurationElementCollection, name: str) -> IdentityConfigurationElement """
        ...


class IdentityModelCaches: # skipped bases: <type 'object'>, <type 'object'>
    """ IdentityModelCaches() """
    @property
    def SessionSecurityTokenCache(self) -> SessionSecurityTokenCache:
        """
        Get: SessionSecurityTokenCache(self: IdentityModelCaches) -> SessionSecurityTokenCache
        Set: SessionSecurityTokenCache(self: IdentityModelCaches) = value
        """
        ...

    @property
    def TokenReplayCache(self) -> TokenReplayCache:
        """
        Get: TokenReplayCache(self: IdentityModelCaches) -> TokenReplayCache
        Set: TokenReplayCache(self: IdentityModelCaches) = value
        """
        ...



class IdentityModelCachesElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ IdentityModelCachesElement() """
    @property
    def IsConfigured(self) -> bool:
        """ Get: IsConfigured(self: IdentityModelCachesElement) -> bool """
        ...

    @property
    def SessionSecurityTokenCache(self) -> CustomTypeElement:
        """
        Get: SessionSecurityTokenCache(self: IdentityModelCachesElement) -> CustomTypeElement
        Set: SessionSecurityTokenCache(self: IdentityModelCachesElement) = value
        """
        ...

    @property
    def TokenReplayCache(self) -> CustomTypeElement:
        """
        Get: TokenReplayCache(self: IdentityModelCachesElement) -> CustomTypeElement
        Set: TokenReplayCache(self: IdentityModelCachesElement) = value
        """
        ...



class IssuerNameRegistryElement(ConfigurationElementInterceptor): # skipped bases: <type 'object'>
    """ IssuerNameRegistryElement() """
    @property
    def Type(self) -> str:
        """
        Get: Type(self: IssuerNameRegistryElement) -> str
        Set: Type(self: IssuerNameRegistryElement) = value
        """
        ...



class SecurityTokenHandlerConfigurationElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ SecurityTokenHandlerConfigurationElement() """
    @property
    def AudienceUris(self) -> AudienceUriElementCollection:
        """ Get: AudienceUris(self: SecurityTokenHandlerConfigurationElement) -> AudienceUriElementCollection """
        ...

    @property
    def Caches(self) -> IdentityModelCachesElement:
        """
        Get: Caches(self: SecurityTokenHandlerConfigurationElement) -> IdentityModelCachesElement
        Set: Caches(self: SecurityTokenHandlerConfigurationElement) = value
        """
        ...

    @property
    def CertificateValidation(self) -> X509CertificateValidationElement:
        """
        Get: CertificateValidation(self: SecurityTokenHandlerConfigurationElement) -> X509CertificateValidationElement
        Set: CertificateValidation(self: SecurityTokenHandlerConfigurationElement) = value
        """
        ...

    @property
    def IssuerNameRegistry(self) -> IssuerNameRegistryElement:
        """
        Get: IssuerNameRegistry(self: SecurityTokenHandlerConfigurationElement) -> IssuerNameRegistryElement
        Set: IssuerNameRegistry(self: SecurityTokenHandlerConfigurationElement) = value
        """
        ...

    @property
    def IssuerTokenResolver(self) -> CustomTypeElement:
        """
        Get: IssuerTokenResolver(self: SecurityTokenHandlerConfigurationElement) -> CustomTypeElement
        Set: IssuerTokenResolver(self: SecurityTokenHandlerConfigurationElement) = value
        """
        ...

    @property
    def MaximumClockSkew(self) -> TimeSpan:
        """
        Get: MaximumClockSkew(self: SecurityTokenHandlerConfigurationElement) -> TimeSpan
        Set: MaximumClockSkew(self: SecurityTokenHandlerConfigurationElement) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: SecurityTokenHandlerConfigurationElement) -> str
        Set: Name(self: SecurityTokenHandlerConfigurationElement) = value
        """
        ...

    @property
    def SaveBootstrapContext(self) -> bool:
        """
        Get: SaveBootstrapContext(self: SecurityTokenHandlerConfigurationElement) -> bool
        Set: SaveBootstrapContext(self: SecurityTokenHandlerConfigurationElement) = value
        """
        ...

    @property
    def ServiceTokenResolver(self) -> CustomTypeElement:
        """
        Get: ServiceTokenResolver(self: SecurityTokenHandlerConfigurationElement) -> CustomTypeElement
        Set: ServiceTokenResolver(self: SecurityTokenHandlerConfigurationElement) = value
        """
        ...

    @property
    def TokenReplayDetection(self) -> TokenReplayDetectionElement:
        """
        Get: TokenReplayDetection(self: SecurityTokenHandlerConfigurationElement) -> TokenReplayDetectionElement
        Set: TokenReplayDetection(self: SecurityTokenHandlerConfigurationElement) = value
        """
        ...



class SecurityTokenHandlerElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ SecurityTokenHandlerElementCollection() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: SecurityTokenHandlerElementCollection) -> str
        Set: Name(self: SecurityTokenHandlerElementCollection) = value
        """
        ...

    @property
    def SecurityTokenHandlerConfiguration(self) -> SecurityTokenHandlerConfigurationElement:
        """
        Get: SecurityTokenHandlerConfiguration(self: SecurityTokenHandlerElementCollection) -> SecurityTokenHandlerConfigurationElement
        Set: SecurityTokenHandlerConfiguration(self: SecurityTokenHandlerElementCollection) = value
        """
        ...



class SecurityTokenHandlerSetElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ SecurityTokenHandlerSetElementCollection() """
    @property
    def IsConfigured(self) -> bool:
        """ Get: IsConfigured(self: SecurityTokenHandlerSetElementCollection) -> bool """
        ...



class SecurityTokenServiceConfiguration(IdentityConfiguration): # skipped bases: <type 'object'>
    """
    SecurityTokenServiceConfiguration()
    SecurityTokenServiceConfiguration(loadConfig: bool)
    SecurityTokenServiceConfiguration(issuerName: str)
    SecurityTokenServiceConfiguration(issuerName: str, loadConfig: bool)
    SecurityTokenServiceConfiguration(issuerName: str, signingCredentials: SigningCredentials)
    SecurityTokenServiceConfiguration(issuerName: str, signingCredentials: SigningCredentials, loadConfig: bool)
    SecurityTokenServiceConfiguration(issuerName: str, signingCredentials: SigningCredentials, serviceName: str)
    """
    @property
    def DefaultMaxSymmetricKeySizeInBits(self) -> int:
        """
        Get: DefaultMaxSymmetricKeySizeInBits(self: SecurityTokenServiceConfiguration) -> int
        Set: DefaultMaxSymmetricKeySizeInBits(self: SecurityTokenServiceConfiguration) = value
        """
        ...

    @property
    def DefaultSymmetricKeySizeInBits(self) -> int:
        """
        Get: DefaultSymmetricKeySizeInBits(self: SecurityTokenServiceConfiguration) -> int
        Set: DefaultSymmetricKeySizeInBits(self: SecurityTokenServiceConfiguration) = value
        """
        ...

    @property
    def DefaultTokenLifetime(self) -> TimeSpan:
        """
        Get: DefaultTokenLifetime(self: SecurityTokenServiceConfiguration) -> TimeSpan
        Set: DefaultTokenLifetime(self: SecurityTokenServiceConfiguration) = value
        """
        ...

    @property
    def DefaultTokenType(self) -> str:
        """
        Get: DefaultTokenType(self: SecurityTokenServiceConfiguration) -> str
        Set: DefaultTokenType(self: SecurityTokenServiceConfiguration) = value
        """
        ...

    @property
    def DisableWsdl(self) -> bool:
        """
        Get: DisableWsdl(self: SecurityTokenServiceConfiguration) -> bool
        Set: DisableWsdl(self: SecurityTokenServiceConfiguration) = value
        """
        ...

    @property
    def MaximumTokenLifetime(self) -> TimeSpan:
        """
        Get: MaximumTokenLifetime(self: SecurityTokenServiceConfiguration) -> TimeSpan
        Set: MaximumTokenLifetime(self: SecurityTokenServiceConfiguration) = value
        """
        ...

    @property
    def SecurityTokenService(self) -> Type:
        """
        Get: SecurityTokenService(self: SecurityTokenServiceConfiguration) -> Type
        Set: SecurityTokenService(self: SecurityTokenServiceConfiguration) = value
        """
        ...

    @property
    def SigningCredentials(self) -> SigningCredentials:
        """
        Get: SigningCredentials(self: SecurityTokenServiceConfiguration) -> SigningCredentials
        Set: SigningCredentials(self: SecurityTokenServiceConfiguration) = value
        """
        ...

    @property
    def TokenIssuerName(self) -> str:
        """
        Get: TokenIssuerName(self: SecurityTokenServiceConfiguration) -> str
        Set: TokenIssuerName(self: SecurityTokenServiceConfiguration) = value
        """
        ...

    @property
    def WSTrust13RequestSerializer(self) -> WSTrust13RequestSerializer:
        """
        Get: WSTrust13RequestSerializer(self: SecurityTokenServiceConfiguration) -> WSTrust13RequestSerializer
        Set: WSTrust13RequestSerializer(self: SecurityTokenServiceConfiguration) = value
        """
        ...

    @property
    def WSTrust13ResponseSerializer(self) -> WSTrust13ResponseSerializer:
        """
        Get: WSTrust13ResponseSerializer(self: SecurityTokenServiceConfiguration) -> WSTrust13ResponseSerializer
        Set: WSTrust13ResponseSerializer(self: SecurityTokenServiceConfiguration) = value
        """
        ...

    @property
    def WSTrustFeb2005RequestSerializer(self) -> WSTrustFeb2005RequestSerializer:
        """
        Get: WSTrustFeb2005RequestSerializer(self: SecurityTokenServiceConfiguration) -> WSTrustFeb2005RequestSerializer
        Set: WSTrustFeb2005RequestSerializer(self: SecurityTokenServiceConfiguration) = value
        """
        ...

    @property
    def WSTrustFeb2005ResponseSerializer(self) -> WSTrustFeb2005ResponseSerializer:
        """
        Get: WSTrustFeb2005ResponseSerializer(self: SecurityTokenServiceConfiguration) -> WSTrustFeb2005ResponseSerializer
        Set: WSTrustFeb2005ResponseSerializer(self: SecurityTokenServiceConfiguration) = value
        """
        ...


    def CreateSecurityTokenService(self) -> SecurityTokenService:
        """ CreateSecurityTokenService(self: SecurityTokenServiceConfiguration) -> SecurityTokenService """
        ...


class SystemIdentityModelSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ SystemIdentityModelSection() """
    @property
    def Current(self) -> SystemIdentityModelSection:
        """ Get: Current() -> SystemIdentityModelSection """
        ...

    @property
    def DefaultIdentityConfigurationElement(self) -> IdentityConfigurationElement:
        """ Get: DefaultIdentityConfigurationElement() -> IdentityConfigurationElement """
        ...

    @property
    def IdentityConfigurationElements(self) -> IdentityConfigurationElementCollection:
        """ Get: IdentityConfigurationElements(self: SystemIdentityModelSection) -> IdentityConfigurationElementCollection """
        ...


    SectionName: str = ...


class TokenReplayDetectionElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ TokenReplayDetectionElement() """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: TokenReplayDetectionElement) -> bool
        Set: Enabled(self: TokenReplayDetectionElement) = value
        """
        ...

    @property
    def ExpirationPeriod(self) -> TimeSpan:
        """
        Get: ExpirationPeriod(self: TokenReplayDetectionElement) -> TimeSpan
        Set: ExpirationPeriod(self: TokenReplayDetectionElement) = value
        """
        ...



class X509CertificateValidationElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ X509CertificateValidationElement() """
    @property
    def CertificateValidationMode(self) -> X509CertificateValidationMode:
        """
        Get: CertificateValidationMode(self: X509CertificateValidationElement) -> X509CertificateValidationMode
        Set: CertificateValidationMode(self: X509CertificateValidationElement) = value
        """
        ...

    @property
    def CertificateValidator(self) -> CustomTypeElement:
        """
        Get: CertificateValidator(self: X509CertificateValidationElement) -> CustomTypeElement
        Set: CertificateValidator(self: X509CertificateValidationElement) = value
        """
        ...

    @property
    def RevocationMode(self) -> X509RevocationMode:
        """
        Get: RevocationMode(self: X509CertificateValidationElement) -> X509RevocationMode
        Set: RevocationMode(self: X509CertificateValidationElement) = value
        """
        ...

    @property
    def TrustedStoreLocation(self) -> StoreLocation:
        """
        Get: TrustedStoreLocation(self: X509CertificateValidationElement) -> StoreLocation
        Set: TrustedStoreLocation(self: X509CertificateValidationElement) = value
        """
        ...



