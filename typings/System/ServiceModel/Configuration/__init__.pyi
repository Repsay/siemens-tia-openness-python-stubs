# encoding: utf-8
# module System.ServiceModel.Configuration calls itself Configuration
# from System.WorkflowServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.ServiceModel.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.ServiceModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.ServiceModel.Channels, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.JScript import Binding

from Microsoft.VisualBasic.ApplicationServices import AuthenticationMode

from System import Enum, Int64, TimeSpan, Type, Uri

from System.Collections import ICollection, IComparer, IEnumerator

from System.Collections.Generic import List

from System.Collections.ObjectModel import Collection, ReadOnlyCollection

from System.Collections.Specialized import NameValueCollection

from System.Configuration import (Configuration, ConfigurationElement, 
    ConfigurationElementCollection, ConfigurationSection, 
    ConfigurationSectionGroup, NameValueConfigurationCollection)

from System.IdentityModel.Selectors import AudienceUriMode

from System.IdentityModel.Tokens import SecurityKeyType

from System.Net import AuthenticationSchemes, IPAddress

from System.Net.Security import ProtectionLevel

from System.Security.Authentication import SslProtocols

from System.Security.Authentication.ExtendedProtection.Configuration import (
    ExtendedProtectionPolicyElement)

from System.Security.Cryptography.X509Certificates import (StoreLocation, 
    StoreName, X509FindType, X509RevocationMode)

from System.Security.Principal import TokenImpersonationLevel

from System.ServiceModel import (AuditLevel, AuditLogLocation, 
    BasicHttpMessageCredentialType, BasicHttpSecurityMode, 
    BasicHttpsSecurityMode, ChannelFactory, DeadLetterQueue, 
    DuplexChannelFactory, EndpointAddress, EndpointIdentity, 
    HostNameComparisonMode, HttpClientCredentialType, HttpProxyCredentialType, 
    MessageCredentialType, MessageSecurityVersion, MsmqAuthenticationMode, 
    MsmqEncryptionAlgorithm, MsmqSecureHashAlgorithm, NetHttpMessageEncoding, 
    NetMsmqSecurityMode, NetNamedPipeSecurityMode, 
    PeerTransportCredentialType, QueueTransferProtocol, ReceiveErrorHandling, 
    ReliableMessagingVersion, ReliableSession, SecurityMode, 
    TcpClientCredentialType, TransactionProtocol, TransferMode, 
    WSDualHttpSecurityMode, WSFederationHttpSecurityMode, WSMessageEncoding, 
    WebHttpSecurityMode)

from System.ServiceModel.Activation.Configuration import DiagnosticSection

from System.ServiceModel.Diagnostics import PerformanceCounterScope

from System.ServiceModel.Dispatcher import XPathMessageFilter

from System.ServiceModel.MsmqIntegration import (MsmqIntegrationSecurityMode, 
    MsmqMessageSerializationFormat)

from System.ServiceModel.PeerResolvers import (PeerReferralPolicy, 
    PeerResolverMode)

from System.ServiceModel.Security import (MessageProtectionOrder, 
    SecurityAlgorithmSuite, SecurityKeyEntropyMode, 
    UserNamePasswordValidationMode)

from System.ServiceModel.Web import WebMessageBodyStyle, WebMessageFormat

from System.Text import Encoding

from System.Workflow.Runtime.Configuration import (
    WorkflowRuntimeServiceElement, WorkflowRuntimeServiceElementCollection)

from System.Xml import XmlElement

from typing import Self

"""The following names are not found in the module: (AddressHeaderCollection, 
    BasicHttpSecurityElement, BasicHttpsSecurityElement, BindingElement, 
    ComMethodElementCollection, ComPersistableTypeElementCollection, 
    ComUdtElementCollection, CommonEndpointBehaviorElement, 
    CommonServiceBehaviorElement, CompressionFormat, ConfigurationElementType, 
    ContextExchangeMechanism, CustomBindingCollectionElement, 
    CustomBindingElementCollection, EndToEndTracingElement, 
    EndpointBehaviorElementCollection, HostTimeoutsElement, 
    HttpDigestClientElement, HttpTransportSecurityElement, 
    IConfigurationContextProviderInternal, IdentityElement, 
    IssuedTokenClientElement, IssuedTokenParametersEndpointAddressElement, 
    ListenUriMode, MessageLoggingElement, MessageVersion, MetadataElement, 
    MsmqIntegrationBindingCollectionElement, MsmqIntegrationSecurityElement, 
    MsmqTransportSecurityElement, NamedServiceModelExtensionCollectionElement, 
    NetHttpBindingCollectionElement, NetHttpWebSocketTransportSettingsElement, 
    NetHttpsBindingCollectionElement, NetMsmqBindingCollectionElement, 
    NetMsmqSecurityElement, NetNamedPipeBindingCollectionElement, 
    NetNamedPipeSecurityElement, NetPeerTcpBindingCollectionElement, 
    NetTcpBindingCollectionElement, NetTcpSecurityElement, 
    PeerCredentialElement, PeerResolverElement, PeerSecurityElement, 
    PeerTransportSecurityElement, PolicyImporterElementCollection, 
    PolicyVersion, PrincipalPermissionMode, RsaElement, SecurityHeaderLayout, 
    ServiceBehaviorElementCollection, ServiceEndpoint, 
    ServiceEndpointElementCollection, 
    ServiceModelConfigurationElementCollection, 
    ServiceModelEnhancedConfigurationElementCollection, 
    ServiceModelExtensionCollectionElement, ServicePrincipalNameElement, 
    ServicesSection, StandardBindingCollectionElement, 
    StandardBindingElementCollection, 
    StandardBindingOptionalReliableSessionElement, 
    StandardEndpointCollectionElement, StandardEndpointElementCollection, 
    StandardEndpointsSection, TServiceModelExtensionElement, 
    TcpTransportSecurityElement, TransportConfigurationTypeElementCollection, 
    UserNameServiceElement, UserPrincipalNameElement, 
    WS2007FederationHttpBindingCollectionElement, 
    WS2007HttpBindingCollectionElement, WSDualHttpBindingCollectionElement, 
    WSDualHttpSecurityElement, WSFederationHttpBindingCollectionElement, 
    WSFederationHttpSecurityElement, WSHttpBindingCollectionElement, 
    WSHttpSecurityElement, WSHttpTransportSecurityElement, 
    WebHttpSecurityElement, WebSocketTransportSettings, 
    WebSocketTransportSettingsElement, WebSocketTransportUsage, 
    WindowsClientElement, WindowsServiceElement, 
    WsdlImporterElementCollection, 
    X509CertificateTrustedIssuerElementCollection, 
    X509CertificateValidationMode, X509InitiatorCertificateClientElement, 
    X509InitiatorCertificateServiceElement, 
    X509PeerCertificateAuthenticationElement, X509PeerCertificateElement, 
    X509RecipientCertificateClientElement, 
    X509RecipientCertificateServiceElement, 
    X509ScopedServiceCertificateElementCollection, 
    X509ServiceCertificateAuthenticationElement, 
    XPathMessageFilterElementCollection, XmlDictionaryReaderQuotasElement, 
    XmlElementElementCollection, field#)
"""

# no functions
# classes

class ServiceModelConfigurationElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ no doc """
    def SetPropertyValueIfNotDefaultValue(self, *args): #cannot find CLR method
        """ SetPropertyValueIfNotDefaultValue[T](self: ServiceModelConfigurationElement, propertyName: str, value: T) """
        ...


class AddressHeaderCollectionElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ AddressHeaderCollectionElement() """
    @property
    def Headers(self): # -> AddressHeaderCollection
        """
        Get: Headers(self: AddressHeaderCollectionElement) -> AddressHeaderCollection
        Set: Headers(self: AddressHeaderCollectionElement) = value
        """
        ...



class AllowedAudienceUriElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ AllowedAudienceUriElement() """
    @property
    def AllowedAudienceUri(self) -> str:
        """
        Get: AllowedAudienceUri(self: AllowedAudienceUriElement) -> str
        Set: AllowedAudienceUri(self: AllowedAudienceUriElement) = value
        """
        ...



class AllowedAudienceUriElementCollection(ServiceModelConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ AllowedAudienceUriElementCollection() """
    pass

class ApplicationContainerSettingsElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ ApplicationContainerSettingsElement() """
    @property
    def PackageFullName(self) -> str:
        """
        Get: PackageFullName(self: ApplicationContainerSettingsElement) -> str
        Set: PackageFullName(self: ApplicationContainerSettingsElement) = value
        """
        ...

    @property
    def SessionId(self) -> int:
        """
        Get: SessionId(self: ApplicationContainerSettingsElement) -> int
        Set: SessionId(self: ApplicationContainerSettingsElement) = value
        """
        ...



class AuthenticationMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AuthenticationMode, values: AnonymousForCertificate (0), AnonymousForSslNegotiated (1), CertificateOverTransport (2), IssuedToken (3), IssuedTokenForCertificate (4), IssuedTokenForSslNegotiated (5), IssuedTokenOverTransport (6), Kerberos (7), KerberosOverTransport (8), MutualCertificate (9), MutualCertificateDuplex (10), MutualSslNegotiated (11), SecureConversation (12), SspiNegotiated (13), SspiNegotiatedOverTransport (17), UserNameForCertificate (14), UserNameForSslNegotiated (15), UserNameOverTransport (16) """
    AnonymousForCertificate: AuthenticationMode = ...
    AnonymousForSslNegotiated: AuthenticationMode = ...
    CertificateOverTransport: AuthenticationMode = ...
    IssuedToken: AuthenticationMode = ...
    IssuedTokenForCertificate: AuthenticationMode = ...
    IssuedTokenForSslNegotiated: AuthenticationMode = ...
    IssuedTokenOverTransport: AuthenticationMode = ...
    Kerberos: AuthenticationMode = ...
    KerberosOverTransport: AuthenticationMode = ...
    MutualCertificate: AuthenticationMode = ...
    MutualCertificateDuplex: AuthenticationMode = ...
    MutualSslNegotiated: AuthenticationMode = ...
    SecureConversation: AuthenticationMode = ...
    SspiNegotiated: AuthenticationMode = ...
    SspiNegotiatedOverTransport: AuthenticationMode = ...
    UserNameForCertificate: AuthenticationMode = ...
    UserNameForSslNegotiated: AuthenticationMode = ...
    UserNameOverTransport: AuthenticationMode = ...
    value__ = ...


class AuthorizationPolicyTypeElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    AuthorizationPolicyTypeElement()
    AuthorizationPolicyTypeElement(policyType: str)
    """
    @property
    def PolicyType(self) -> str:
        """
        Get: PolicyType(self: AuthorizationPolicyTypeElement) -> str
        Set: PolicyType(self: AuthorizationPolicyTypeElement) = value
        """
        ...


    def __new__(cls, policyType:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, policyType: str)
        """
        ...


class AuthorizationPolicyTypeElementCollection(ServiceModelConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ AuthorizationPolicyTypeElementCollection() """
    pass

class BaseAddressElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ BaseAddressElement() """
    @property
    def BaseAddress(self) -> str:
        """
        Get: BaseAddress(self: BaseAddressElement) -> str
        Set: BaseAddress(self: BaseAddressElement) = value
        """
        ...



class BaseAddressElementCollection(ServiceModelConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ BaseAddressElementCollection() """
    pass

class BaseAddressPrefixFilterElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    BaseAddressPrefixFilterElement()
    BaseAddressPrefixFilterElement(prefix: Uri)
    """
    @property
    def Prefix(self) -> Uri:
        """
        Get: Prefix(self: BaseAddressPrefixFilterElement) -> Uri
        Set: Prefix(self: BaseAddressPrefixFilterElement) = value
        """
        ...


    def __new__(cls, prefix:Uri = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, prefix: Uri)
        """
        ...


class BaseAddressPrefixFilterElementCollection(ServiceModelConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ BaseAddressPrefixFilterElementCollection() """
    pass

class BindingCollectionElement(IConfigurationContextProviderInternal, ConfigurationElement): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BindingName(self) -> str:
        """ Get: BindingName(self: BindingCollectionElement) -> str """
        ...

    @property
    def BindingType(self) -> Type:
        """ Get: BindingType(self: BindingCollectionElement) -> Type """
        ...

    @property
    def ConfiguredBindings(self) -> ReadOnlyCollection:
        """ Get: ConfiguredBindings(self: BindingCollectionElement) -> ReadOnlyCollection[IBindingConfigurationElement] """
        ...


    def ContainsKey(self, name:str) -> bool:
        """ ContainsKey(self: BindingCollectionElement, name: str) -> bool """
        ...

    def GetDefault(self, *args): #cannot find CLR method
        """ GetDefault(self: BindingCollectionElement) -> Binding """
        ...

    def TryAdd(self, *args): #cannot find CLR method
        """ TryAdd(self: BindingCollectionElement, name: str, binding: Binding, config: Configuration) -> bool """
        ...


class BasicHttpBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ BasicHttpBindingCollectionElement() """
    pass

class IBindingConfigurationElement: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CloseTimeout(self) -> TimeSpan:
        """ Get: CloseTimeout(self: IBindingConfigurationElement) -> TimeSpan """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IBindingConfigurationElement) -> str """
        ...

    @property
    def OpenTimeout(self) -> TimeSpan:
        """ Get: OpenTimeout(self: IBindingConfigurationElement) -> TimeSpan """
        ...

    @property
    def ReceiveTimeout(self) -> TimeSpan:
        """ Get: ReceiveTimeout(self: IBindingConfigurationElement) -> TimeSpan """
        ...

    @property
    def SendTimeout(self) -> TimeSpan:
        """ Get: SendTimeout(self: IBindingConfigurationElement) -> TimeSpan """
        ...


    def ApplyConfiguration(self, binding:Binding): # -> 
        """ ApplyConfiguration(self: IBindingConfigurationElement, binding: Binding) """
        ...


class StandardBindingElement(ServiceModelConfigurationElement, IConfigurationContextProviderInternal, IBindingConfigurationElement): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BindingElementType(self):
        ...


    def InitializeFrom(self, *args): #cannot find CLR method
        """ InitializeFrom(self: StandardBindingElement, binding: Binding) """
        ...

    def OnApplyConfiguration(self, *args): #cannot find CLR method
        """ OnApplyConfiguration(self: StandardBindingElement, binding: Binding) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...


class HttpBindingBaseElement(StandardBindingElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ no doc """
    @property
    def AllowCookies(self) -> bool:
        """
        Get: AllowCookies(self: HttpBindingBaseElement) -> bool
        Set: AllowCookies(self: HttpBindingBaseElement) = value
        """
        ...

    @property
    def BypassProxyOnLocal(self) -> bool:
        """
        Get: BypassProxyOnLocal(self: HttpBindingBaseElement) -> bool
        Set: BypassProxyOnLocal(self: HttpBindingBaseElement) = value
        """
        ...

    @property
    def HostNameComparisonMode(self) -> HostNameComparisonMode:
        """
        Get: HostNameComparisonMode(self: HttpBindingBaseElement) -> HostNameComparisonMode
        Set: HostNameComparisonMode(self: HttpBindingBaseElement) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: HttpBindingBaseElement) -> Int64
        Set: MaxBufferPoolSize(self: HttpBindingBaseElement) = value
        """
        ...

    @property
    def MaxBufferSize(self) -> int:
        """
        Get: MaxBufferSize(self: HttpBindingBaseElement) -> int
        Set: MaxBufferSize(self: HttpBindingBaseElement) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: HttpBindingBaseElement) -> Int64
        Set: MaxReceivedMessageSize(self: HttpBindingBaseElement) = value
        """
        ...

    @property
    def ProxyAddress(self) -> Uri:
        """
        Get: ProxyAddress(self: HttpBindingBaseElement) -> Uri
        Set: ProxyAddress(self: HttpBindingBaseElement) = value
        """
        ...

    @property
    def ReaderQuotas(self): # -> XmlDictionaryReaderQuotasElement
        """ Get: ReaderQuotas(self: HttpBindingBaseElement) -> XmlDictionaryReaderQuotasElement """
        ...

    @property
    def TextEncoding(self) -> Encoding:
        """
        Get: TextEncoding(self: HttpBindingBaseElement) -> Encoding
        Set: TextEncoding(self: HttpBindingBaseElement) = value
        """
        ...

    @property
    def TransferMode(self) -> TransferMode:
        """
        Get: TransferMode(self: HttpBindingBaseElement) -> TransferMode
        Set: TransferMode(self: HttpBindingBaseElement) = value
        """
        ...

    @property
    def UseDefaultWebProxy(self) -> bool:
        """
        Get: UseDefaultWebProxy(self: HttpBindingBaseElement) -> bool
        Set: UseDefaultWebProxy(self: HttpBindingBaseElement) = value
        """
        ...



class BasicHttpBindingElement(HttpBindingBaseElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    BasicHttpBindingElement(name: str)
    BasicHttpBindingElement()
    """
    @property
    def MessageEncoding(self) -> WSMessageEncoding:
        """
        Get: MessageEncoding(self: BasicHttpBindingElement) -> WSMessageEncoding
        Set: MessageEncoding(self: BasicHttpBindingElement) = value
        """
        ...

    @property
    def Security(self): # -> BasicHttpSecurityElement
        """ Get: Security(self: BasicHttpBindingElement) -> BasicHttpSecurityElement """
        ...



class BasicHttpContextBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ BasicHttpContextBindingCollectionElement() """
    pass

class BasicHttpContextBindingElement(BasicHttpBindingElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    BasicHttpContextBindingElement()
    BasicHttpContextBindingElement(name: str)
    """
    @property
    def ContextManagementEnabled(self) -> bool:
        """
        Get: ContextManagementEnabled(self: BasicHttpContextBindingElement) -> bool
        Set: ContextManagementEnabled(self: BasicHttpContextBindingElement) = value
        """
        ...



class BasicHttpMessageSecurityElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ BasicHttpMessageSecurityElement() """
    @property
    def AlgorithmSuite(self) -> SecurityAlgorithmSuite:
        """
        Get: AlgorithmSuite(self: BasicHttpMessageSecurityElement) -> SecurityAlgorithmSuite
        Set: AlgorithmSuite(self: BasicHttpMessageSecurityElement) = value
        """
        ...

    @property
    def ClientCredentialType(self) -> BasicHttpMessageCredentialType:
        """
        Get: ClientCredentialType(self: BasicHttpMessageSecurityElement) -> BasicHttpMessageCredentialType
        Set: ClientCredentialType(self: BasicHttpMessageSecurityElement) = value
        """
        ...



class BasicHttpsBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ BasicHttpsBindingCollectionElement() """
    pass

class BasicHttpsBindingElement(HttpBindingBaseElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    BasicHttpsBindingElement(name: str)
    BasicHttpsBindingElement()
    """
    @property
    def MessageEncoding(self) -> WSMessageEncoding:
        """
        Get: MessageEncoding(self: BasicHttpsBindingElement) -> WSMessageEncoding
        Set: MessageEncoding(self: BasicHttpsBindingElement) = value
        """
        ...

    @property
    def Security(self): # -> BasicHttpsSecurityElement
        """ Get: Security(self: BasicHttpsBindingElement) -> BasicHttpsSecurityElement """
        ...



class BasicHttpSecurityElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ BasicHttpSecurityElement() """
    @property
    def Message(self) -> BasicHttpMessageSecurityElement:
        """ Get: Message(self: BasicHttpSecurityElement) -> BasicHttpMessageSecurityElement """
        ...

    @property
    def Mode(self) -> BasicHttpSecurityMode:
        """
        Get: Mode(self: BasicHttpSecurityElement) -> BasicHttpSecurityMode
        Set: Mode(self: BasicHttpSecurityElement) = value
        """
        ...

    @property
    def Transport(self): # -> HttpTransportSecurityElement
        """ Get: Transport(self: BasicHttpSecurityElement) -> HttpTransportSecurityElement """
        ...



class BasicHttpsSecurityElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ BasicHttpsSecurityElement() """
    @property
    def Message(self) -> BasicHttpMessageSecurityElement:
        """ Get: Message(self: BasicHttpsSecurityElement) -> BasicHttpMessageSecurityElement """
        ...

    @property
    def Mode(self) -> BasicHttpsSecurityMode:
        """
        Get: Mode(self: BasicHttpsSecurityElement) -> BasicHttpsSecurityMode
        Set: Mode(self: BasicHttpsSecurityElement) = value
        """
        ...

    @property
    def Transport(self): # -> HttpTransportSecurityElement
        """ Get: Transport(self: BasicHttpsSecurityElement) -> HttpTransportSecurityElement """
        ...



class ServiceModelExtensionElement(ServiceModelConfigurationElement, IConfigurationContextProviderInternal): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ConfigurationElementName(self) -> str:
        """ Get: ConfigurationElementName(self: ServiceModelExtensionElement) -> str """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: ServiceModelExtensionElement, from: ServiceModelExtensionElement) """
        ...


class BehaviorExtensionElement(ServiceModelExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ no doc """
    @property
    def BehaviorType(self) -> Type:
        """ Get: BehaviorType(self: BehaviorExtensionElement) -> Type """
        ...


    def CreateBehavior(self, *args): #cannot find CLR method
        """ CreateBehavior(self: BehaviorExtensionElement) -> object """
        ...


class BehaviorsSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ BehaviorsSection() """
    @property
    def EndpointBehaviors(self): # -> EndpointBehaviorElementCollection
        """ Get: EndpointBehaviors(self: BehaviorsSection) -> EndpointBehaviorElementCollection """
        ...

    @property
    def ServiceBehaviors(self): # -> ServiceBehaviorElementCollection
        """ Get: ServiceBehaviors(self: BehaviorsSection) -> ServiceBehaviorElementCollection """
        ...



class BindingElementExtensionElement(ServiceModelExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ no doc """
    @property
    def BindingElementType(self) -> Type:
        """ Get: BindingElementType(self: BindingElementExtensionElement) -> Type """
        ...


    def ApplyConfiguration(self, bindingElement): # ->  # Not found arg types: {'bindingElement': 'BindingElement'}
        """ ApplyConfiguration(self: BindingElementExtensionElement, bindingElement: BindingElement) """
        ...

    def CreateBindingElement(self, *args): #cannot find CLR method
        """ CreateBindingElement(self: BindingElementExtensionElement) -> BindingElement """
        ...

    def InitializeFrom(self, *args): #cannot find CLR method
        """ InitializeFrom(self: BindingElementExtensionElement, bindingElement: BindingElement) """
        ...


class BinaryMessageEncodingElement(BindingElementExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ BinaryMessageEncodingElement() """
    @property
    def CompressionFormat(self): # -> CompressionFormat
        """
        Get: CompressionFormat(self: BinaryMessageEncodingElement) -> CompressionFormat
        Set: CompressionFormat(self: BinaryMessageEncodingElement) = value
        """
        ...

    @property
    def MaxReadPoolSize(self) -> int:
        """
        Get: MaxReadPoolSize(self: BinaryMessageEncodingElement) -> int
        Set: MaxReadPoolSize(self: BinaryMessageEncodingElement) = value
        """
        ...

    @property
    def MaxSessionSize(self) -> int:
        """
        Get: MaxSessionSize(self: BinaryMessageEncodingElement) -> int
        Set: MaxSessionSize(self: BinaryMessageEncodingElement) = value
        """
        ...

    @property
    def MaxWritePoolSize(self) -> int:
        """
        Get: MaxWritePoolSize(self: BinaryMessageEncodingElement) -> int
        Set: MaxWritePoolSize(self: BinaryMessageEncodingElement) = value
        """
        ...

    @property
    def ReaderQuotas(self): # -> XmlDictionaryReaderQuotasElement
        """ Get: ReaderQuotas(self: BinaryMessageEncodingElement) -> XmlDictionaryReaderQuotasElement """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: BinaryMessageEncodingElement, from: ServiceModelExtensionElement) """
        ...


class BindingsSection(IConfigurationContextProviderInternal, ConfigurationSection): # skipped bases: <type 'object'>
    """ BindingsSection() """
    @property
    def BasicHttpBinding(self) -> BasicHttpBindingCollectionElement:
        """ Get: BasicHttpBinding(self: BindingsSection) -> BasicHttpBindingCollectionElement """
        ...

    @property
    def BasicHttpsBinding(self) -> BasicHttpsBindingCollectionElement:
        """ Get: BasicHttpsBinding(self: BindingsSection) -> BasicHttpsBindingCollectionElement """
        ...

    @property
    def BindingCollections(self) -> List:
        """ Get: BindingCollections(self: BindingsSection) -> List[BindingCollectionElement] """
        ...

    @property
    def CustomBinding(self): # -> CustomBindingCollectionElement
        """ Get: CustomBinding(self: BindingsSection) -> CustomBindingCollectionElement """
        ...

    @property
    def MsmqIntegrationBinding(self): # -> MsmqIntegrationBindingCollectionElement
        """ Get: MsmqIntegrationBinding(self: BindingsSection) -> MsmqIntegrationBindingCollectionElement """
        ...

    @property
    def NetHttpBinding(self): # -> NetHttpBindingCollectionElement
        """ Get: NetHttpBinding(self: BindingsSection) -> NetHttpBindingCollectionElement """
        ...

    @property
    def NetHttpsBinding(self): # -> NetHttpsBindingCollectionElement
        """ Get: NetHttpsBinding(self: BindingsSection) -> NetHttpsBindingCollectionElement """
        ...

    @property
    def NetMsmqBinding(self): # -> NetMsmqBindingCollectionElement
        """ Get: NetMsmqBinding(self: BindingsSection) -> NetMsmqBindingCollectionElement """
        ...

    @property
    def NetNamedPipeBinding(self): # -> NetNamedPipeBindingCollectionElement
        """ Get: NetNamedPipeBinding(self: BindingsSection) -> NetNamedPipeBindingCollectionElement """
        ...

    @property
    def NetPeerTcpBinding(self): # -> NetPeerTcpBindingCollectionElement
        """ Get: NetPeerTcpBinding(self: BindingsSection) -> NetPeerTcpBindingCollectionElement """
        ...

    @property
    def NetTcpBinding(self): # -> NetTcpBindingCollectionElement
        """ Get: NetTcpBinding(self: BindingsSection) -> NetTcpBindingCollectionElement """
        ...

    @property
    def WS2007FederationHttpBinding(self): # -> WS2007FederationHttpBindingCollectionElement
        """ Get: WS2007FederationHttpBinding(self: BindingsSection) -> WS2007FederationHttpBindingCollectionElement """
        ...

    @property
    def WS2007HttpBinding(self): # -> WS2007HttpBindingCollectionElement
        """ Get: WS2007HttpBinding(self: BindingsSection) -> WS2007HttpBindingCollectionElement """
        ...

    @property
    def WSDualHttpBinding(self): # -> WSDualHttpBindingCollectionElement
        """ Get: WSDualHttpBinding(self: BindingsSection) -> WSDualHttpBindingCollectionElement """
        ...

    @property
    def WSFederationHttpBinding(self): # -> WSFederationHttpBindingCollectionElement
        """ Get: WSFederationHttpBinding(self: BindingsSection) -> WSFederationHttpBindingCollectionElement """
        ...

    @property
    def WSHttpBinding(self): # -> WSHttpBindingCollectionElement
        """ Get: WSHttpBinding(self: BindingsSection) -> WSHttpBindingCollectionElement """
        ...


    @staticmethod
    def GetSection(config:Configuration) -> BindingsSection:
        """ GetSection(config: Configuration) -> BindingsSection """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ByteStreamMessageEncodingElement(BindingElementExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ ByteStreamMessageEncodingElement() """
    @property
    def ReaderQuotas(self): # -> XmlDictionaryReaderQuotasElement
        """ Get: ReaderQuotas(self: ByteStreamMessageEncodingElement) -> XmlDictionaryReaderQuotasElement """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: ByteStreamMessageEncodingElement, from: ServiceModelExtensionElement) """
        ...


class CallbackDebugElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ CallbackDebugElement() """
    @property
    def IncludeExceptionDetailInFaults(self) -> bool:
        """
        Get: IncludeExceptionDetailInFaults(self: CallbackDebugElement) -> bool
        Set: IncludeExceptionDetailInFaults(self: CallbackDebugElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: CallbackDebugElement, from: ServiceModelExtensionElement) """
        ...


class CallbackTimeoutsElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ CallbackTimeoutsElement() """
    @property
    def TransactionTimeout(self) -> TimeSpan:
        """
        Get: TransactionTimeout(self: CallbackTimeoutsElement) -> TimeSpan
        Set: TransactionTimeout(self: CallbackTimeoutsElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: CallbackTimeoutsElement, from: ServiceModelExtensionElement) """
        ...


class CertificateElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ CertificateElement() """
    @property
    def EncodedValue(self) -> str:
        """
        Get: EncodedValue(self: CertificateElement) -> str
        Set: EncodedValue(self: CertificateElement) = value
        """
        ...



class CertificateReferenceElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ CertificateReferenceElement() """
    @property
    def FindValue(self) -> str:
        """
        Get: FindValue(self: CertificateReferenceElement) -> str
        Set: FindValue(self: CertificateReferenceElement) = value
        """
        ...

    @property
    def IsChainIncluded(self) -> bool:
        """
        Get: IsChainIncluded(self: CertificateReferenceElement) -> bool
        Set: IsChainIncluded(self: CertificateReferenceElement) = value
        """
        ...

    @property
    def StoreLocation(self) -> StoreLocation:
        """
        Get: StoreLocation(self: CertificateReferenceElement) -> StoreLocation
        Set: StoreLocation(self: CertificateReferenceElement) = value
        """
        ...

    @property
    def StoreName(self) -> StoreName:
        """
        Get: StoreName(self: CertificateReferenceElement) -> StoreName
        Set: StoreName(self: CertificateReferenceElement) = value
        """
        ...

    @property
    def X509FindType(self) -> X509FindType:
        """
        Get: X509FindType(self: CertificateReferenceElement) -> X509FindType
        Set: X509FindType(self: CertificateReferenceElement) = value
        """
        ...



class ChannelEndpointElement(IConfigurationContextProviderInternal, ConfigurationElement): # skipped bases: <type 'object'>
    """
    ChannelEndpointElement()
    ChannelEndpointElement(address: EndpointAddress, contractType: str)
    """
    @property
    def Address(self) -> Uri:
        """
        Get: Address(self: ChannelEndpointElement) -> Uri
        Set: Address(self: ChannelEndpointElement) = value
        """
        ...

    @property
    def BehaviorConfiguration(self) -> str:
        """
        Get: BehaviorConfiguration(self: ChannelEndpointElement) -> str
        Set: BehaviorConfiguration(self: ChannelEndpointElement) = value
        """
        ...

    @property
    def Binding(self) -> str:
        """
        Get: Binding(self: ChannelEndpointElement) -> str
        Set: Binding(self: ChannelEndpointElement) = value
        """
        ...

    @property
    def BindingConfiguration(self) -> str:
        """
        Get: BindingConfiguration(self: ChannelEndpointElement) -> str
        Set: BindingConfiguration(self: ChannelEndpointElement) = value
        """
        ...

    @property
    def Contract(self) -> str:
        """
        Get: Contract(self: ChannelEndpointElement) -> str
        Set: Contract(self: ChannelEndpointElement) = value
        """
        ...

    @property
    def EndpointConfiguration(self) -> str:
        """
        Get: EndpointConfiguration(self: ChannelEndpointElement) -> str
        Set: EndpointConfiguration(self: ChannelEndpointElement) = value
        """
        ...

    @property
    def Headers(self) -> AddressHeaderCollectionElement:
        """ Get: Headers(self: ChannelEndpointElement) -> AddressHeaderCollectionElement """
        ...

    @property
    def Identity(self): # -> IdentityElement
        """ Get: Identity(self: ChannelEndpointElement) -> IdentityElement """
        ...

    @property
    def Kind(self) -> str:
        """
        Get: Kind(self: ChannelEndpointElement) -> str
        Set: Kind(self: ChannelEndpointElement) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ChannelEndpointElement) -> str
        Set: Name(self: ChannelEndpointElement) = value
        """
        ...


    def __new__(cls, address:EndpointAddress = ..., contractType:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, address: EndpointAddress, contractType: str)
        """
        ...


class ChannelEndpointElementCollection(ServiceModelEnhancedConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ChannelEndpointElementCollection() """
    pass

class ChannelPoolSettingsElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ ChannelPoolSettingsElement() """
    @property
    def IdleTimeout(self) -> TimeSpan:
        """
        Get: IdleTimeout(self: ChannelPoolSettingsElement) -> TimeSpan
        Set: IdleTimeout(self: ChannelPoolSettingsElement) = value
        """
        ...

    @property
    def LeaseTimeout(self) -> TimeSpan:
        """
        Get: LeaseTimeout(self: ChannelPoolSettingsElement) -> TimeSpan
        Set: LeaseTimeout(self: ChannelPoolSettingsElement) = value
        """
        ...

    @property
    def MaxOutboundChannelsPerEndpoint(self) -> int:
        """
        Get: MaxOutboundChannelsPerEndpoint(self: ChannelPoolSettingsElement) -> int
        Set: MaxOutboundChannelsPerEndpoint(self: ChannelPoolSettingsElement) = value
        """
        ...



class ClaimTypeElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    ClaimTypeElement()
    ClaimTypeElement(claimType: str, isOptional: bool)
    """
    @property
    def ClaimType(self) -> str:
        """
        Get: ClaimType(self: ClaimTypeElement) -> str
        Set: ClaimType(self: ClaimTypeElement) = value
        """
        ...

    @property
    def IsOptional(self) -> bool:
        """
        Get: IsOptional(self: ClaimTypeElement) -> bool
        Set: IsOptional(self: ClaimTypeElement) = value
        """
        ...


    def __new__(cls, claimType:str = ..., isOptional:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, claimType: str, isOptional: bool)
        """
        ...


class ClaimTypeElementCollection(ServiceModelConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ClaimTypeElementCollection() """
    pass

class ClearBehaviorElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ ClearBehaviorElement() """
    pass

class ClientCredentialsElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ ClientCredentialsElement() """
    @property
    def ClientCertificate(self): # -> X509InitiatorCertificateClientElement
        """ Get: ClientCertificate(self: ClientCredentialsElement) -> X509InitiatorCertificateClientElement """
        ...

    @property
    def HttpDigest(self): # -> HttpDigestClientElement
        """ Get: HttpDigest(self: ClientCredentialsElement) -> HttpDigestClientElement """
        ...

    @property
    def IssuedToken(self): # -> IssuedTokenClientElement
        """ Get: IssuedToken(self: ClientCredentialsElement) -> IssuedTokenClientElement """
        ...

    @property
    def Peer(self): # -> PeerCredentialElement
        """ Get: Peer(self: ClientCredentialsElement) -> PeerCredentialElement """
        ...

    @property
    def ServiceCertificate(self): # -> X509RecipientCertificateClientElement
        """ Get: ServiceCertificate(self: ClientCredentialsElement) -> X509RecipientCertificateClientElement """
        ...

    @property
    def SupportInteractive(self) -> bool:
        """
        Get: SupportInteractive(self: ClientCredentialsElement) -> bool
        Set: SupportInteractive(self: ClientCredentialsElement) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: ClientCredentialsElement) -> str
        Set: Type(self: ClientCredentialsElement) = value
        """
        ...

    @property
    def UseIdentityConfiguration(self) -> bool:
        """
        Get: UseIdentityConfiguration(self: ClientCredentialsElement) -> bool
        Set: UseIdentityConfiguration(self: ClientCredentialsElement) = value
        """
        ...

    @property
    def Windows(self): # -> WindowsClientElement
        """ Get: Windows(self: ClientCredentialsElement) -> WindowsClientElement """
        ...


    def ApplyConfiguration(self, *args): #cannot find CLR method
        """ ApplyConfiguration(self: ClientCredentialsElement, behavior: ClientCredentials) """
        ...

    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: ClientCredentialsElement, from: ServiceModelExtensionElement) """
        ...


class ClientSection(IConfigurationContextProviderInternal, ConfigurationSection): # skipped bases: <type 'object'>
    """ ClientSection() """
    @property
    def Endpoints(self) -> ChannelEndpointElementCollection:
        """ Get: Endpoints(self: ClientSection) -> ChannelEndpointElementCollection """
        ...

    @property
    def Metadata(self): # -> MetadataElement
        """ Get: Metadata(self: ClientSection) -> MetadataElement """
        ...



class ClientViaElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ ClientViaElement() """
    @property
    def ViaUri(self) -> Uri:
        """
        Get: ViaUri(self: ClientViaElement) -> Uri
        Set: ViaUri(self: ClientViaElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: ClientViaElement, from: ServiceModelExtensionElement) """
        ...


class ComContractElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    ComContractElement()
    ComContractElement(contractType: str)
    """
    @property
    def Contract(self) -> str:
        """
        Get: Contract(self: ComContractElement) -> str
        Set: Contract(self: ComContractElement) = value
        """
        ...

    @property
    def ExposedMethods(self): # -> ComMethodElementCollection
        """ Get: ExposedMethods(self: ComContractElement) -> ComMethodElementCollection """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ComContractElement) -> str
        Set: Name(self: ComContractElement) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: ComContractElement) -> str
        Set: Namespace(self: ComContractElement) = value
        """
        ...

    @property
    def PersistableTypes(self): # -> ComPersistableTypeElementCollection
        """ Get: PersistableTypes(self: ComContractElement) -> ComPersistableTypeElementCollection """
        ...

    @property
    def RequiresSession(self) -> bool:
        """
        Get: RequiresSession(self: ComContractElement) -> bool
        Set: RequiresSession(self: ComContractElement) = value
        """
        ...

    @property
    def UserDefinedTypes(self): # -> ComUdtElementCollection
        """ Get: UserDefinedTypes(self: ComContractElement) -> ComUdtElementCollection """
        ...


    def __new__(cls, contractType:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, contractType: str)
        """
        ...


class ComContractElementCollection(ServiceModelEnhancedConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ComContractElementCollection() """
    pass

class ComContractsSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ ComContractsSection() """
    @property
    def ComContracts(self) -> ComContractElementCollection:
        """ Get: ComContracts(self: ComContractsSection) -> ComContractElementCollection """
        ...



class ComMethodElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    ComMethodElement()
    ComMethodElement(method: str)
    """
    @property
    def ExposedMethod(self) -> str:
        """
        Get: ExposedMethod(self: ComMethodElement) -> str
        Set: ExposedMethod(self: ComMethodElement) = value
        """
        ...


    def __new__(cls, method:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, method: str)
        """
        ...


class ComMethodElementCollection(ServiceModelEnhancedConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ComMethodElementCollection() """
    pass

class CommonBehaviorsSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ CommonBehaviorsSection() """
    @property
    def EndpointBehaviors(self): # -> CommonEndpointBehaviorElement
        """ Get: EndpointBehaviors(self: CommonBehaviorsSection) -> CommonEndpointBehaviorElement """
        ...

    @property
    def ServiceBehaviors(self): # -> CommonServiceBehaviorElement
        """ Get: ServiceBehaviors(self: CommonBehaviorsSection) -> CommonServiceBehaviorElement """
        ...



class CommonEndpointBehaviorElement(ServiceModelExtensionCollectionElement): # skipped bases: <type 'IEnumerable[BehaviorExtensionElement]'>, <type 'IEnumerable'>, <type 'ICollection[BehaviorExtensionElement]'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ CommonEndpointBehaviorElement() """
    pass

class CommonServiceBehaviorElement(ServiceModelExtensionCollectionElement): # skipped bases: <type 'IEnumerable[BehaviorExtensionElement]'>, <type 'IEnumerable'>, <type 'ICollection[BehaviorExtensionElement]'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ CommonServiceBehaviorElement() """
    pass

class ComPersistableTypeElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    ComPersistableTypeElement()
    ComPersistableTypeElement(ID: str)
    """
    @property
    def ID(self) -> str:
        """
        Get: ID(self: ComPersistableTypeElement) -> str
        Set: ID(self: ComPersistableTypeElement) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ComPersistableTypeElement) -> str
        Set: Name(self: ComPersistableTypeElement) = value
        """
        ...


    def __new__(cls, ID:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, ID: str)
        """
        ...


class ComPersistableTypeElementCollection(ServiceModelEnhancedConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ComPersistableTypeElementCollection() """
    pass

class CompositeDuplexElement(BindingElementExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ CompositeDuplexElement() """
    @property
    def ClientBaseAddress(self) -> Uri:
        """
        Get: ClientBaseAddress(self: CompositeDuplexElement) -> Uri
        Set: ClientBaseAddress(self: CompositeDuplexElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: CompositeDuplexElement, from: ServiceModelExtensionElement) """
        ...


class ComUdtElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    ComUdtElement()
    ComUdtElement(typeDefID: str)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: ComUdtElement) -> str
        Set: Name(self: ComUdtElement) = value
        """
        ...

    @property
    def TypeDefID(self) -> str:
        """
        Get: TypeDefID(self: ComUdtElement) -> str
        Set: TypeDefID(self: ComUdtElement) = value
        """
        ...

    @property
    def TypeLibID(self) -> str:
        """
        Get: TypeLibID(self: ComUdtElement) -> str
        Set: TypeLibID(self: ComUdtElement) = value
        """
        ...

    @property
    def TypeLibVersion(self) -> str:
        """
        Get: TypeLibVersion(self: ComUdtElement) -> str
        Set: TypeLibVersion(self: ComUdtElement) = value
        """
        ...


    def __new__(cls, typeDefID:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, typeDefID: str)
        """
        ...


class ComUdtElementCollection(ServiceModelEnhancedConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ComUdtElementCollection() """
    pass

class ConfigurationChannelFactory(ChannelFactory): # skipped bases: <type 'IDisposable'>, <type 'IChannelFactory'>, <type 'ICommunicationObject'>, <type 'IChannelFactory[TChannel]'>, <type 'object'>
    """ ConfigurationChannelFactory[TChannel](endpointConfigurationName: str, configuration: Configuration, remoteAddress: EndpointAddress) """
    pass

class ConfigurationDuplexChannelFactory(DuplexChannelFactory): # skipped bases: <type 'IDisposable'>, <type 'IChannelFactory[TChannel]'>, <type 'IChannelFactory'>, <type 'ICommunicationObject'>, <type 'object'>
    """ ConfigurationDuplexChannelFactory[TChannel](callbackObject: object, endpointConfigurationName: str, remoteAddress: EndpointAddress, configuration: Configuration) """
    pass

class TransportElement(BindingElementExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ no doc """
    @property
    def ManualAddressing(self) -> bool:
        """
        Get: ManualAddressing(self: TransportElement) -> bool
        Set: ManualAddressing(self: TransportElement) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: TransportElement) -> Int64
        Set: MaxBufferPoolSize(self: TransportElement) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: TransportElement) -> Int64
        Set: MaxReceivedMessageSize(self: TransportElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: TransportElement, from: ServiceModelExtensionElement) """
        ...

    def CreateDefaultBindingElement(self, *args): #cannot find CLR method
        """ CreateDefaultBindingElement(self: TransportElement) -> TransportBindingElement """
        ...


class ConnectionOrientedTransportElement(TransportElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ no doc """
    @property
    def ChannelInitializationTimeout(self) -> TimeSpan:
        """
        Get: ChannelInitializationTimeout(self: ConnectionOrientedTransportElement) -> TimeSpan
        Set: ChannelInitializationTimeout(self: ConnectionOrientedTransportElement) = value
        """
        ...

    @property
    def ConnectionBufferSize(self) -> int:
        """
        Get: ConnectionBufferSize(self: ConnectionOrientedTransportElement) -> int
        Set: ConnectionBufferSize(self: ConnectionOrientedTransportElement) = value
        """
        ...

    @property
    def HostNameComparisonMode(self) -> HostNameComparisonMode:
        """
        Get: HostNameComparisonMode(self: ConnectionOrientedTransportElement) -> HostNameComparisonMode
        Set: HostNameComparisonMode(self: ConnectionOrientedTransportElement) = value
        """
        ...

    @property
    def MaxBufferSize(self) -> int:
        """
        Get: MaxBufferSize(self: ConnectionOrientedTransportElement) -> int
        Set: MaxBufferSize(self: ConnectionOrientedTransportElement) = value
        """
        ...

    @property
    def MaxOutputDelay(self) -> TimeSpan:
        """
        Get: MaxOutputDelay(self: ConnectionOrientedTransportElement) -> TimeSpan
        Set: MaxOutputDelay(self: ConnectionOrientedTransportElement) = value
        """
        ...

    @property
    def MaxPendingAccepts(self) -> int:
        """
        Get: MaxPendingAccepts(self: ConnectionOrientedTransportElement) -> int
        Set: MaxPendingAccepts(self: ConnectionOrientedTransportElement) = value
        """
        ...

    @property
    def MaxPendingConnections(self) -> int:
        """
        Get: MaxPendingConnections(self: ConnectionOrientedTransportElement) -> int
        Set: MaxPendingConnections(self: ConnectionOrientedTransportElement) = value
        """
        ...

    @property
    def TransferMode(self) -> TransferMode:
        """
        Get: TransferMode(self: ConnectionOrientedTransportElement) -> TransferMode
        Set: TransferMode(self: ConnectionOrientedTransportElement) = value
        """
        ...



class ContextBindingElementExtensionElement(BindingElementExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ ContextBindingElementExtensionElement() """
    @property
    def ClientCallbackAddress(self) -> Uri:
        """
        Get: ClientCallbackAddress(self: ContextBindingElementExtensionElement) -> Uri
        Set: ClientCallbackAddress(self: ContextBindingElementExtensionElement) = value
        """
        ...

    @property
    def ContextExchangeMechanism(self): # -> ContextExchangeMechanism
        """
        Get: ContextExchangeMechanism(self: ContextBindingElementExtensionElement) -> ContextExchangeMechanism
        Set: ContextExchangeMechanism(self: ContextBindingElementExtensionElement) = value
        """
        ...

    @property
    def ContextManagementEnabled(self) -> bool:
        """
        Get: ContextManagementEnabled(self: ContextBindingElementExtensionElement) -> bool
        Set: ContextManagementEnabled(self: ContextBindingElementExtensionElement) = value
        """
        ...

    @property
    def ProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ProtectionLevel(self: ContextBindingElementExtensionElement) -> ProtectionLevel
        Set: ProtectionLevel(self: ContextBindingElementExtensionElement) = value
        """
        ...



class CustomBindingCollectionElement(BindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ CustomBindingCollectionElement() """
    @property
    def Bindings(self): # -> CustomBindingElementCollection
        """ Get: Bindings(self: CustomBindingCollectionElement) -> CustomBindingElementCollection """
        ...



class CustomBindingElement(NamedServiceModelExtensionCollectionElement, IBindingConfigurationElement): # skipped bases: <type 'IEnumerable[BindingElementExtensionElement]'>, <type 'ICollection[BindingElementExtensionElement]'>, <type 'IEnumerable'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    CustomBindingElement()
    CustomBindingElement(name: str)
    """
    def CanAdd(self, element:BindingElementExtensionElement) -> bool:
        """ CanAdd(self: CustomBindingElement, element: BindingElementExtensionElement) -> bool """
        ...

    def OnApplyConfiguration(self, *args): #cannot find CLR method
        """ OnApplyConfiguration(self: CustomBindingElement, binding: Binding) """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __new__(cls, name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...


class CustomBindingElementCollection(ServiceModelEnhancedConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ CustomBindingElementCollection() """
    pass

class DataContractSerializerElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ DataContractSerializerElement() """
    @property
    def IgnoreExtensionDataObject(self) -> bool:
        """
        Get: IgnoreExtensionDataObject(self: DataContractSerializerElement) -> bool
        Set: IgnoreExtensionDataObject(self: DataContractSerializerElement) = value
        """
        ...

    @property
    def MaxItemsInObjectGraph(self) -> int:
        """
        Get: MaxItemsInObjectGraph(self: DataContractSerializerElement) -> int
        Set: MaxItemsInObjectGraph(self: DataContractSerializerElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: DataContractSerializerElement, from: ServiceModelExtensionElement) """
        ...


class DefaultPortElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    DefaultPortElement()
    DefaultPortElement(other: DefaultPortElement)
    """
    @property
    def Port(self) -> int:
        """
        Get: Port(self: DefaultPortElement) -> int
        Set: Port(self: DefaultPortElement) = value
        """
        ...

    @property
    def Scheme(self) -> str:
        """
        Get: Scheme(self: DefaultPortElement) -> str
        Set: Scheme(self: DefaultPortElement) = value
        """
        ...


    def __new__(cls, other:DefaultPortElement = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, other: DefaultPortElement)
        """
        ...


class DefaultPortElementCollection(ServiceModelEnhancedConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ DefaultPortElementCollection() """
    pass

class DelegatingHandlerElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ DelegatingHandlerElement() """
    @property
    def Type(self) -> str:
        """
        Get: Type(self: DelegatingHandlerElement) -> str
        Set: Type(self: DelegatingHandlerElement) = value
        """
        ...



class DelegatingHandlerElementCollection(ServiceModelConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ DelegatingHandlerElementCollection() """
    pass

class DiagnosticSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ DiagnosticSection() """
    @property
    def EndToEndTracing(self): # -> EndToEndTracingElement
        """ Get: EndToEndTracing(self: DiagnosticSection) -> EndToEndTracingElement """
        ...

    @property
    def EtwProviderId(self) -> str:
        """
        Get: EtwProviderId(self: DiagnosticSection) -> str
        Set: EtwProviderId(self: DiagnosticSection) = value
        """
        ...

    @property
    def MessageLogging(self): # -> MessageLoggingElement
        """ Get: MessageLogging(self: DiagnosticSection) -> MessageLoggingElement """
        ...

    @property
    def PerformanceCounters(self) -> PerformanceCounterScope:
        """
        Get: PerformanceCounters(self: DiagnosticSection) -> PerformanceCounterScope
        Set: PerformanceCounters(self: DiagnosticSection) = value
        """
        ...

    @property
    def WmiProviderEnabled(self) -> bool:
        """
        Get: WmiProviderEnabled(self: DiagnosticSection) -> bool
        Set: WmiProviderEnabled(self: DiagnosticSection) = value
        """
        ...



class DispatcherSynchronizationElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ DispatcherSynchronizationElement() """
    @property
    def AsynchronousSendEnabled(self) -> bool:
        """
        Get: AsynchronousSendEnabled(self: DispatcherSynchronizationElement) -> bool
        Set: AsynchronousSendEnabled(self: DispatcherSynchronizationElement) = value
        """
        ...

    @property
    def MaxPendingReceives(self) -> int:
        """
        Get: MaxPendingReceives(self: DispatcherSynchronizationElement) -> int
        Set: MaxPendingReceives(self: DispatcherSynchronizationElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: DispatcherSynchronizationElement, from: ServiceModelExtensionElement) """
        ...


class DnsElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ DnsElement() """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: DnsElement) -> str
        Set: Value(self: DnsElement) = value
        """
        ...



class EndpointAddressElementBase(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Address(self) -> Uri:
        """
        Get: Address(self: EndpointAddressElementBase) -> Uri
        Set: Address(self: EndpointAddressElementBase) = value
        """
        ...

    @property
    def Headers(self) -> AddressHeaderCollectionElement:
        """ Get: Headers(self: EndpointAddressElementBase) -> AddressHeaderCollectionElement """
        ...

    @property
    def Identity(self): # -> IdentityElement
        """ Get: Identity(self: EndpointAddressElementBase) -> IdentityElement """
        ...


    def Copy(self, *args): #cannot find CLR method
        """ Copy(self: EndpointAddressElementBase, source: EndpointAddressElementBase) """
        ...

    def InitializeFrom(self, endpointAddress:EndpointAddress): # -> 
        """ InitializeFrom(self: EndpointAddressElementBase, endpointAddress: EndpointAddress) """
        ...


class EndpointBehaviorElement(NamedServiceModelExtensionCollectionElement): # skipped bases: <type 'IEnumerable[BehaviorExtensionElement]'>, <type 'IEnumerable'>, <type 'ICollection[BehaviorExtensionElement]'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    EndpointBehaviorElement()
    EndpointBehaviorElement(name: str)
    """
    def CanAdd(self, element:BehaviorExtensionElement) -> bool:
        """ CanAdd(self: EndpointBehaviorElement, element: BehaviorExtensionElement) -> bool """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __new__(cls, name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...


class EndpointBehaviorElementCollection(ServiceModelEnhancedConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ EndpointBehaviorElementCollection() """
    pass

class EndpointCollectionElement(IConfigurationContextProviderInternal, ConfigurationElement): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ConfiguredEndpoints(self) -> ReadOnlyCollection:
        """ Get: ConfiguredEndpoints(self: EndpointCollectionElement) -> ReadOnlyCollection[StandardEndpointElement] """
        ...

    @property
    def EndpointName(self) -> str:
        """ Get: EndpointName(self: EndpointCollectionElement) -> str """
        ...

    @property
    def EndpointType(self) -> Type:
        """ Get: EndpointType(self: EndpointCollectionElement) -> Type """
        ...


    def ContainsKey(self, name:str) -> bool:
        """ ContainsKey(self: EndpointCollectionElement, name: str) -> bool """
        ...

    def GetDefaultStandardEndpointElement(self, *args): #cannot find CLR method
        """ GetDefaultStandardEndpointElement(self: EndpointCollectionElement) -> StandardEndpointElement """
        ...

    def TryAdd(self, *args): #cannot find CLR method
        """ TryAdd(self: EndpointCollectionElement, name: str, endpoint: ServiceEndpoint, config: Configuration) -> bool """
        ...


class EndToEndTracingElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ EndToEndTracingElement() """
    @property
    def ActivityTracing(self) -> bool:
        """
        Get: ActivityTracing(self: EndToEndTracingElement) -> bool
        Set: ActivityTracing(self: EndToEndTracingElement) = value
        """
        ...

    @property
    def MessageFlowTracing(self) -> bool:
        """
        Get: MessageFlowTracing(self: EndToEndTracingElement) -> bool
        Set: MessageFlowTracing(self: EndToEndTracingElement) = value
        """
        ...

    @property
    def PropagateActivity(self) -> bool:
        """
        Get: PropagateActivity(self: EndToEndTracingElement) -> bool
        Set: PropagateActivity(self: EndToEndTracingElement) = value
        """
        ...



class ExtendedWorkflowRuntimeServiceElementCollection(WorkflowRuntimeServiceElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ExtendedWorkflowRuntimeServiceElementCollection() """
    def Remove(self, *__args:WorkflowRuntimeServiceElement): # -> 
        """ Remove(self: ExtendedWorkflowRuntimeServiceElementCollection, serviceSettings: WorkflowRuntimeServiceElement)Remove(self: ExtendedWorkflowRuntimeServiceElementCollection, key: str) """
        ...


class ExtensionElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    ExtensionElement()
    ExtensionElement(name: str)
    ExtensionElement(name: str, type: str)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: ExtensionElement) -> str
        Set: Name(self: ExtensionElement) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: ExtensionElement) -> str
        Set: Type(self: ExtensionElement) = value
        """
        ...


    def __new__(cls, name:str = ..., type:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, type: str)
        """
        ...


class ExtensionElementCollection(ServiceModelConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ExtensionElementCollection() """
    pass

class ExtensionsSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ ExtensionsSection() """
    @property
    def BehaviorExtensions(self) -> ExtensionElementCollection:
        """ Get: BehaviorExtensions(self: ExtensionsSection) -> ExtensionElementCollection """
        ...

    @property
    def BindingElementExtensions(self) -> ExtensionElementCollection:
        """ Get: BindingElementExtensions(self: ExtensionsSection) -> ExtensionElementCollection """
        ...

    @property
    def BindingExtensions(self) -> ExtensionElementCollection:
        """ Get: BindingExtensions(self: ExtensionsSection) -> ExtensionElementCollection """
        ...

    @property
    def EndpointExtensions(self) -> ExtensionElementCollection:
        """ Get: EndpointExtensions(self: ExtensionsSection) -> ExtensionElementCollection """
        ...



class FederatedMessageSecurityOverHttpElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ FederatedMessageSecurityOverHttpElement() """
    @property
    def AlgorithmSuite(self) -> SecurityAlgorithmSuite:
        """
        Get: AlgorithmSuite(self: FederatedMessageSecurityOverHttpElement) -> SecurityAlgorithmSuite
        Set: AlgorithmSuite(self: FederatedMessageSecurityOverHttpElement) = value
        """
        ...

    @property
    def ClaimTypeRequirements(self) -> ClaimTypeElementCollection:
        """ Get: ClaimTypeRequirements(self: FederatedMessageSecurityOverHttpElement) -> ClaimTypeElementCollection """
        ...

    @property
    def EstablishSecurityContext(self) -> bool:
        """
        Get: EstablishSecurityContext(self: FederatedMessageSecurityOverHttpElement) -> bool
        Set: EstablishSecurityContext(self: FederatedMessageSecurityOverHttpElement) = value
        """
        ...

    @property
    def IssuedKeyType(self) -> SecurityKeyType:
        """
        Get: IssuedKeyType(self: FederatedMessageSecurityOverHttpElement) -> SecurityKeyType
        Set: IssuedKeyType(self: FederatedMessageSecurityOverHttpElement) = value
        """
        ...

    @property
    def IssuedTokenType(self) -> str:
        """
        Get: IssuedTokenType(self: FederatedMessageSecurityOverHttpElement) -> str
        Set: IssuedTokenType(self: FederatedMessageSecurityOverHttpElement) = value
        """
        ...

    @property
    def Issuer(self): # -> IssuedTokenParametersEndpointAddressElement
        """ Get: Issuer(self: FederatedMessageSecurityOverHttpElement) -> IssuedTokenParametersEndpointAddressElement """
        ...

    @property
    def IssuerMetadata(self) -> EndpointAddressElementBase:
        """ Get: IssuerMetadata(self: FederatedMessageSecurityOverHttpElement) -> EndpointAddressElementBase """
        ...

    @property
    def NegotiateServiceCredential(self) -> bool:
        """
        Get: NegotiateServiceCredential(self: FederatedMessageSecurityOverHttpElement) -> bool
        Set: NegotiateServiceCredential(self: FederatedMessageSecurityOverHttpElement) = value
        """
        ...

    @property
    def TokenRequestParameters(self): # -> XmlElementElementCollection
        """ Get: TokenRequestParameters(self: FederatedMessageSecurityOverHttpElement) -> XmlElementElementCollection """
        ...



class HostElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ HostElement() """
    @property
    def BaseAddresses(self) -> BaseAddressElementCollection:
        """ Get: BaseAddresses(self: HostElement) -> BaseAddressElementCollection """
        ...

    @property
    def Timeouts(self): # -> HostTimeoutsElement
        """ Get: Timeouts(self: HostElement) -> HostTimeoutsElement """
        ...



class HostTimeoutsElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ HostTimeoutsElement() """
    @property
    def CloseTimeout(self) -> TimeSpan:
        """
        Get: CloseTimeout(self: HostTimeoutsElement) -> TimeSpan
        Set: CloseTimeout(self: HostTimeoutsElement) = value
        """
        ...

    @property
    def OpenTimeout(self) -> TimeSpan:
        """
        Get: OpenTimeout(self: HostTimeoutsElement) -> TimeSpan
        Set: OpenTimeout(self: HostTimeoutsElement) = value
        """
        ...



class HttpDigestClientElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ HttpDigestClientElement() """
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel:
        """
        Get: ImpersonationLevel(self: HttpDigestClientElement) -> TokenImpersonationLevel
        Set: ImpersonationLevel(self: HttpDigestClientElement) = value
        """
        ...


    def Copy(self, from_:HttpDigestClientElement): # -> 
        """ Copy(self: HttpDigestClientElement, from: HttpDigestClientElement) """
        ...


class HttpMessageHandlerFactoryElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ HttpMessageHandlerFactoryElement() """
    @property
    def Handlers(self) -> DelegatingHandlerElementCollection:
        """ Get: Handlers(self: HttpMessageHandlerFactoryElement) -> DelegatingHandlerElementCollection """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: HttpMessageHandlerFactoryElement) -> str
        Set: Type(self: HttpMessageHandlerFactoryElement) = value
        """
        ...



class HttpTransportElement(TransportElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ HttpTransportElement() """
    @property
    def AllowCookies(self) -> bool:
        """
        Get: AllowCookies(self: HttpTransportElement) -> bool
        Set: AllowCookies(self: HttpTransportElement) = value
        """
        ...

    @property
    def AuthenticationScheme(self) -> AuthenticationSchemes:
        """
        Get: AuthenticationScheme(self: HttpTransportElement) -> AuthenticationSchemes
        Set: AuthenticationScheme(self: HttpTransportElement) = value
        """
        ...

    @property
    def BindingElementType(self) -> Type:
        """ Get: BindingElementType(self: HttpTransportElement) -> Type """
        ...

    @property
    def BypassProxyOnLocal(self) -> bool:
        """
        Get: BypassProxyOnLocal(self: HttpTransportElement) -> bool
        Set: BypassProxyOnLocal(self: HttpTransportElement) = value
        """
        ...

    @property
    def DecompressionEnabled(self) -> bool:
        """
        Get: DecompressionEnabled(self: HttpTransportElement) -> bool
        Set: DecompressionEnabled(self: HttpTransportElement) = value
        """
        ...

    @property
    def ExtendedProtectionPolicy(self) -> ExtendedProtectionPolicyElement:
        """ Get: ExtendedProtectionPolicy(self: HttpTransportElement) -> ExtendedProtectionPolicyElement """
        ...

    @property
    def HostNameComparisonMode(self) -> HostNameComparisonMode:
        """
        Get: HostNameComparisonMode(self: HttpTransportElement) -> HostNameComparisonMode
        Set: HostNameComparisonMode(self: HttpTransportElement) = value
        """
        ...

    @property
    def KeepAliveEnabled(self) -> bool:
        """
        Get: KeepAliveEnabled(self: HttpTransportElement) -> bool
        Set: KeepAliveEnabled(self: HttpTransportElement) = value
        """
        ...

    @property
    def MaxBufferSize(self) -> int:
        """
        Get: MaxBufferSize(self: HttpTransportElement) -> int
        Set: MaxBufferSize(self: HttpTransportElement) = value
        """
        ...

    @property
    def MaxPendingAccepts(self) -> int:
        """
        Get: MaxPendingAccepts(self: HttpTransportElement) -> int
        Set: MaxPendingAccepts(self: HttpTransportElement) = value
        """
        ...

    @property
    def MessageHandlerFactory(self) -> HttpMessageHandlerFactoryElement:
        """
        Get: MessageHandlerFactory(self: HttpTransportElement) -> HttpMessageHandlerFactoryElement
        Set: MessageHandlerFactory(self: HttpTransportElement) = value
        """
        ...

    @property
    def ProxyAddress(self) -> Uri:
        """
        Get: ProxyAddress(self: HttpTransportElement) -> Uri
        Set: ProxyAddress(self: HttpTransportElement) = value
        """
        ...

    @property
    def ProxyAuthenticationScheme(self) -> AuthenticationSchemes:
        """
        Get: ProxyAuthenticationScheme(self: HttpTransportElement) -> AuthenticationSchemes
        Set: ProxyAuthenticationScheme(self: HttpTransportElement) = value
        """
        ...

    @property
    def Realm(self) -> str:
        """
        Get: Realm(self: HttpTransportElement) -> str
        Set: Realm(self: HttpTransportElement) = value
        """
        ...

    @property
    def RequestInitializationTimeout(self) -> TimeSpan:
        """
        Get: RequestInitializationTimeout(self: HttpTransportElement) -> TimeSpan
        Set: RequestInitializationTimeout(self: HttpTransportElement) = value
        """
        ...

    @property
    def TransferMode(self) -> TransferMode:
        """
        Get: TransferMode(self: HttpTransportElement) -> TransferMode
        Set: TransferMode(self: HttpTransportElement) = value
        """
        ...

    @property
    def UnsafeConnectionNtlmAuthentication(self) -> bool:
        """
        Get: UnsafeConnectionNtlmAuthentication(self: HttpTransportElement) -> bool
        Set: UnsafeConnectionNtlmAuthentication(self: HttpTransportElement) = value
        """
        ...

    @property
    def UseDefaultWebProxy(self) -> bool:
        """
        Get: UseDefaultWebProxy(self: HttpTransportElement) -> bool
        Set: UseDefaultWebProxy(self: HttpTransportElement) = value
        """
        ...

    @property
    def WebSocketSettings(self): # -> WebSocketTransportSettingsElement
        """
        Get: WebSocketSettings(self: HttpTransportElement) -> WebSocketTransportSettingsElement
        Set: WebSocketSettings(self: HttpTransportElement) = value
        """
        ...



class HttpsTransportElement(HttpTransportElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ HttpsTransportElement() """
    @property
    def RequireClientCertificate(self) -> bool:
        """
        Get: RequireClientCertificate(self: HttpsTransportElement) -> bool
        Set: RequireClientCertificate(self: HttpsTransportElement) = value
        """
        ...



class HttpTransportSecurityElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ HttpTransportSecurityElement() """
    @property
    def ClientCredentialType(self) -> HttpClientCredentialType:
        """
        Get: ClientCredentialType(self: HttpTransportSecurityElement) -> HttpClientCredentialType
        Set: ClientCredentialType(self: HttpTransportSecurityElement) = value
        """
        ...

    @property
    def ExtendedProtectionPolicy(self) -> ExtendedProtectionPolicyElement:
        """ Get: ExtendedProtectionPolicy(self: HttpTransportSecurityElement) -> ExtendedProtectionPolicyElement """
        ...

    @property
    def ProxyCredentialType(self) -> HttpProxyCredentialType:
        """
        Get: ProxyCredentialType(self: HttpTransportSecurityElement) -> HttpProxyCredentialType
        Set: ProxyCredentialType(self: HttpTransportSecurityElement) = value
        """
        ...

    @property
    def Realm(self) -> str:
        """
        Get: Realm(self: HttpTransportSecurityElement) -> str
        Set: Realm(self: HttpTransportSecurityElement) = value
        """
        ...



class IdentityElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ IdentityElement() """
    @property
    def Certificate(self) -> CertificateElement:
        """ Get: Certificate(self: IdentityElement) -> CertificateElement """
        ...

    @property
    def CertificateReference(self) -> CertificateReferenceElement:
        """ Get: CertificateReference(self: IdentityElement) -> CertificateReferenceElement """
        ...

    @property
    def Dns(self) -> DnsElement:
        """ Get: Dns(self: IdentityElement) -> DnsElement """
        ...

    @property
    def Rsa(self): # -> RsaElement
        """ Get: Rsa(self: IdentityElement) -> RsaElement """
        ...

    @property
    def ServicePrincipalName(self): # -> ServicePrincipalNameElement
        """ Get: ServicePrincipalName(self: IdentityElement) -> ServicePrincipalNameElement """
        ...

    @property
    def UserPrincipalName(self): # -> UserPrincipalNameElement
        """ Get: UserPrincipalName(self: IdentityElement) -> UserPrincipalNameElement """
        ...


    def InitializeFrom(self, identity:EndpointIdentity): # -> 
        """ InitializeFrom(self: IdentityElement, identity: EndpointIdentity) """
        ...


class IssuedTokenClientBehaviorsElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ IssuedTokenClientBehaviorsElement() """
    @property
    def BehaviorConfiguration(self) -> str:
        """
        Get: BehaviorConfiguration(self: IssuedTokenClientBehaviorsElement) -> str
        Set: BehaviorConfiguration(self: IssuedTokenClientBehaviorsElement) = value
        """
        ...

    @property
    def IssuerAddress(self) -> str:
        """
        Get: IssuerAddress(self: IssuedTokenClientBehaviorsElement) -> str
        Set: IssuerAddress(self: IssuedTokenClientBehaviorsElement) = value
        """
        ...



class IssuedTokenClientBehaviorsElementCollection(ServiceModelConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ IssuedTokenClientBehaviorsElementCollection() """
    pass

class IssuedTokenClientElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ IssuedTokenClientElement() """
    @property
    def CacheIssuedTokens(self) -> bool:
        """
        Get: CacheIssuedTokens(self: IssuedTokenClientElement) -> bool
        Set: CacheIssuedTokens(self: IssuedTokenClientElement) = value
        """
        ...

    @property
    def DefaultKeyEntropyMode(self) -> SecurityKeyEntropyMode:
        """
        Get: DefaultKeyEntropyMode(self: IssuedTokenClientElement) -> SecurityKeyEntropyMode
        Set: DefaultKeyEntropyMode(self: IssuedTokenClientElement) = value
        """
        ...

    @property
    def IssuedTokenRenewalThresholdPercentage(self) -> int:
        """
        Get: IssuedTokenRenewalThresholdPercentage(self: IssuedTokenClientElement) -> int
        Set: IssuedTokenRenewalThresholdPercentage(self: IssuedTokenClientElement) = value
        """
        ...

    @property
    def IssuerChannelBehaviors(self) -> IssuedTokenClientBehaviorsElementCollection:
        """ Get: IssuerChannelBehaviors(self: IssuedTokenClientElement) -> IssuedTokenClientBehaviorsElementCollection """
        ...

    @property
    def LocalIssuer(self): # -> IssuedTokenParametersEndpointAddressElement
        """ Get: LocalIssuer(self: IssuedTokenClientElement) -> IssuedTokenParametersEndpointAddressElement """
        ...

    @property
    def LocalIssuerChannelBehaviors(self) -> str:
        """
        Get: LocalIssuerChannelBehaviors(self: IssuedTokenClientElement) -> str
        Set: LocalIssuerChannelBehaviors(self: IssuedTokenClientElement) = value
        """
        ...

    @property
    def MaxIssuedTokenCachingTime(self) -> TimeSpan:
        """
        Get: MaxIssuedTokenCachingTime(self: IssuedTokenClientElement) -> TimeSpan
        Set: MaxIssuedTokenCachingTime(self: IssuedTokenClientElement) = value
        """
        ...


    def Copy(self, from_:IssuedTokenClientElement): # -> 
        """ Copy(self: IssuedTokenClientElement, from: IssuedTokenClientElement) """
        ...


class IssuedTokenParametersElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ IssuedTokenParametersElement() """
    @property
    def AdditionalRequestParameters(self): # -> XmlElementElementCollection
        """ Get: AdditionalRequestParameters(self: IssuedTokenParametersElement) -> XmlElementElementCollection """
        ...

    @property
    def ClaimTypeRequirements(self) -> ClaimTypeElementCollection:
        """ Get: ClaimTypeRequirements(self: IssuedTokenParametersElement) -> ClaimTypeElementCollection """
        ...

    @property
    def DefaultMessageSecurityVersion(self) -> MessageSecurityVersion:
        """
        Get: DefaultMessageSecurityVersion(self: IssuedTokenParametersElement) -> MessageSecurityVersion
        Set: DefaultMessageSecurityVersion(self: IssuedTokenParametersElement) = value
        """
        ...

    @property
    def Issuer(self): # -> IssuedTokenParametersEndpointAddressElement
        """ Get: Issuer(self: IssuedTokenParametersElement) -> IssuedTokenParametersEndpointAddressElement """
        ...

    @property
    def IssuerMetadata(self) -> EndpointAddressElementBase:
        """ Get: IssuerMetadata(self: IssuedTokenParametersElement) -> EndpointAddressElementBase """
        ...

    @property
    def KeySize(self) -> int:
        """
        Get: KeySize(self: IssuedTokenParametersElement) -> int
        Set: KeySize(self: IssuedTokenParametersElement) = value
        """
        ...

    @property
    def KeyType(self) -> SecurityKeyType:
        """
        Get: KeyType(self: IssuedTokenParametersElement) -> SecurityKeyType
        Set: KeyType(self: IssuedTokenParametersElement) = value
        """
        ...

    @property
    def TokenType(self) -> str:
        """
        Get: TokenType(self: IssuedTokenParametersElement) -> str
        Set: TokenType(self: IssuedTokenParametersElement) = value
        """
        ...

    @property
    def UseStrTransform(self) -> bool:
        """
        Get: UseStrTransform(self: IssuedTokenParametersElement) -> bool
        Set: UseStrTransform(self: IssuedTokenParametersElement) = value
        """
        ...



class IssuedTokenParametersEndpointAddressElement(IConfigurationContextProviderInternal, EndpointAddressElementBase): # skipped bases: <type 'object'>
    """ IssuedTokenParametersEndpointAddressElement() """
    @property
    def Binding(self) -> str:
        """
        Get: Binding(self: IssuedTokenParametersEndpointAddressElement) -> str
        Set: Binding(self: IssuedTokenParametersEndpointAddressElement) = value
        """
        ...

    @property
    def BindingConfiguration(self) -> str:
        """
        Get: BindingConfiguration(self: IssuedTokenParametersEndpointAddressElement) -> str
        Set: BindingConfiguration(self: IssuedTokenParametersEndpointAddressElement) = value
        """
        ...



class IssuedTokenServiceElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ IssuedTokenServiceElement() """
    @property
    def AllowedAudienceUris(self) -> AllowedAudienceUriElementCollection:
        """ Get: AllowedAudienceUris(self: IssuedTokenServiceElement) -> AllowedAudienceUriElementCollection """
        ...

    @property
    def AllowUntrustedRsaIssuers(self) -> bool:
        """
        Get: AllowUntrustedRsaIssuers(self: IssuedTokenServiceElement) -> bool
        Set: AllowUntrustedRsaIssuers(self: IssuedTokenServiceElement) = value
        """
        ...

    @property
    def AudienceUriMode(self) -> AudienceUriMode:
        """
        Get: AudienceUriMode(self: IssuedTokenServiceElement) -> AudienceUriMode
        Set: AudienceUriMode(self: IssuedTokenServiceElement) = value
        """
        ...

    @property
    def CertificateValidationMode(self): # -> X509CertificateValidationMode
        """
        Get: CertificateValidationMode(self: IssuedTokenServiceElement) -> X509CertificateValidationMode
        Set: CertificateValidationMode(self: IssuedTokenServiceElement) = value
        """
        ...

    @property
    def CustomCertificateValidatorType(self) -> str:
        """
        Get: CustomCertificateValidatorType(self: IssuedTokenServiceElement) -> str
        Set: CustomCertificateValidatorType(self: IssuedTokenServiceElement) = value
        """
        ...

    @property
    def KnownCertificates(self): # -> X509CertificateTrustedIssuerElementCollection
        """ Get: KnownCertificates(self: IssuedTokenServiceElement) -> X509CertificateTrustedIssuerElementCollection """
        ...

    @property
    def RevocationMode(self) -> X509RevocationMode:
        """
        Get: RevocationMode(self: IssuedTokenServiceElement) -> X509RevocationMode
        Set: RevocationMode(self: IssuedTokenServiceElement) = value
        """
        ...

    @property
    def SamlSerializerType(self) -> str:
        """
        Get: SamlSerializerType(self: IssuedTokenServiceElement) -> str
        Set: SamlSerializerType(self: IssuedTokenServiceElement) = value
        """
        ...

    @property
    def TrustedStoreLocation(self) -> StoreLocation:
        """
        Get: TrustedStoreLocation(self: IssuedTokenServiceElement) -> StoreLocation
        Set: TrustedStoreLocation(self: IssuedTokenServiceElement) = value
        """
        ...


    def Copy(self, from_:IssuedTokenServiceElement): # -> 
        """ Copy(self: IssuedTokenServiceElement, from: IssuedTokenServiceElement) """
        ...


class LocalClientSecuritySettingsElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ LocalClientSecuritySettingsElement() """
    @property
    def CacheCookies(self) -> bool:
        """
        Get: CacheCookies(self: LocalClientSecuritySettingsElement) -> bool
        Set: CacheCookies(self: LocalClientSecuritySettingsElement) = value
        """
        ...

    @property
    def CookieRenewalThresholdPercentage(self) -> int:
        """
        Get: CookieRenewalThresholdPercentage(self: LocalClientSecuritySettingsElement) -> int
        Set: CookieRenewalThresholdPercentage(self: LocalClientSecuritySettingsElement) = value
        """
        ...

    @property
    def DetectReplays(self) -> bool:
        """
        Get: DetectReplays(self: LocalClientSecuritySettingsElement) -> bool
        Set: DetectReplays(self: LocalClientSecuritySettingsElement) = value
        """
        ...

    @property
    def MaxClockSkew(self) -> TimeSpan:
        """
        Get: MaxClockSkew(self: LocalClientSecuritySettingsElement) -> TimeSpan
        Set: MaxClockSkew(self: LocalClientSecuritySettingsElement) = value
        """
        ...

    @property
    def MaxCookieCachingTime(self) -> TimeSpan:
        """
        Get: MaxCookieCachingTime(self: LocalClientSecuritySettingsElement) -> TimeSpan
        Set: MaxCookieCachingTime(self: LocalClientSecuritySettingsElement) = value
        """
        ...

    @property
    def ReconnectTransportOnFailure(self) -> bool:
        """
        Get: ReconnectTransportOnFailure(self: LocalClientSecuritySettingsElement) -> bool
        Set: ReconnectTransportOnFailure(self: LocalClientSecuritySettingsElement) = value
        """
        ...

    @property
    def ReplayCacheSize(self) -> int:
        """
        Get: ReplayCacheSize(self: LocalClientSecuritySettingsElement) -> int
        Set: ReplayCacheSize(self: LocalClientSecuritySettingsElement) = value
        """
        ...

    @property
    def ReplayWindow(self) -> TimeSpan:
        """
        Get: ReplayWindow(self: LocalClientSecuritySettingsElement) -> TimeSpan
        Set: ReplayWindow(self: LocalClientSecuritySettingsElement) = value
        """
        ...

    @property
    def SessionKeyRenewalInterval(self) -> TimeSpan:
        """
        Get: SessionKeyRenewalInterval(self: LocalClientSecuritySettingsElement) -> TimeSpan
        Set: SessionKeyRenewalInterval(self: LocalClientSecuritySettingsElement) = value
        """
        ...

    @property
    def SessionKeyRolloverInterval(self) -> TimeSpan:
        """
        Get: SessionKeyRolloverInterval(self: LocalClientSecuritySettingsElement) -> TimeSpan
        Set: SessionKeyRolloverInterval(self: LocalClientSecuritySettingsElement) = value
        """
        ...

    @property
    def TimestampValidityDuration(self) -> TimeSpan:
        """
        Get: TimestampValidityDuration(self: LocalClientSecuritySettingsElement) -> TimeSpan
        Set: TimestampValidityDuration(self: LocalClientSecuritySettingsElement) = value
        """
        ...



class LocalServiceSecuritySettingsElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ LocalServiceSecuritySettingsElement() """
    @property
    def DetectReplays(self) -> bool:
        """
        Get: DetectReplays(self: LocalServiceSecuritySettingsElement) -> bool
        Set: DetectReplays(self: LocalServiceSecuritySettingsElement) = value
        """
        ...

    @property
    def InactivityTimeout(self) -> TimeSpan:
        """
        Get: InactivityTimeout(self: LocalServiceSecuritySettingsElement) -> TimeSpan
        Set: InactivityTimeout(self: LocalServiceSecuritySettingsElement) = value
        """
        ...

    @property
    def IssuedCookieLifetime(self) -> TimeSpan:
        """
        Get: IssuedCookieLifetime(self: LocalServiceSecuritySettingsElement) -> TimeSpan
        Set: IssuedCookieLifetime(self: LocalServiceSecuritySettingsElement) = value
        """
        ...

    @property
    def MaxCachedCookies(self) -> int:
        """
        Get: MaxCachedCookies(self: LocalServiceSecuritySettingsElement) -> int
        Set: MaxCachedCookies(self: LocalServiceSecuritySettingsElement) = value
        """
        ...

    @property
    def MaxClockSkew(self) -> TimeSpan:
        """
        Get: MaxClockSkew(self: LocalServiceSecuritySettingsElement) -> TimeSpan
        Set: MaxClockSkew(self: LocalServiceSecuritySettingsElement) = value
        """
        ...

    @property
    def MaxPendingSessions(self) -> int:
        """
        Get: MaxPendingSessions(self: LocalServiceSecuritySettingsElement) -> int
        Set: MaxPendingSessions(self: LocalServiceSecuritySettingsElement) = value
        """
        ...

    @property
    def MaxStatefulNegotiations(self) -> int:
        """
        Get: MaxStatefulNegotiations(self: LocalServiceSecuritySettingsElement) -> int
        Set: MaxStatefulNegotiations(self: LocalServiceSecuritySettingsElement) = value
        """
        ...

    @property
    def NegotiationTimeout(self) -> TimeSpan:
        """
        Get: NegotiationTimeout(self: LocalServiceSecuritySettingsElement) -> TimeSpan
        Set: NegotiationTimeout(self: LocalServiceSecuritySettingsElement) = value
        """
        ...

    @property
    def ReconnectTransportOnFailure(self) -> bool:
        """
        Get: ReconnectTransportOnFailure(self: LocalServiceSecuritySettingsElement) -> bool
        Set: ReconnectTransportOnFailure(self: LocalServiceSecuritySettingsElement) = value
        """
        ...

    @property
    def ReplayCacheSize(self) -> int:
        """
        Get: ReplayCacheSize(self: LocalServiceSecuritySettingsElement) -> int
        Set: ReplayCacheSize(self: LocalServiceSecuritySettingsElement) = value
        """
        ...

    @property
    def ReplayWindow(self) -> TimeSpan:
        """
        Get: ReplayWindow(self: LocalServiceSecuritySettingsElement) -> TimeSpan
        Set: ReplayWindow(self: LocalServiceSecuritySettingsElement) = value
        """
        ...

    @property
    def SessionKeyRenewalInterval(self) -> TimeSpan:
        """
        Get: SessionKeyRenewalInterval(self: LocalServiceSecuritySettingsElement) -> TimeSpan
        Set: SessionKeyRenewalInterval(self: LocalServiceSecuritySettingsElement) = value
        """
        ...

    @property
    def SessionKeyRolloverInterval(self) -> TimeSpan:
        """
        Get: SessionKeyRolloverInterval(self: LocalServiceSecuritySettingsElement) -> TimeSpan
        Set: SessionKeyRolloverInterval(self: LocalServiceSecuritySettingsElement) = value
        """
        ...

    @property
    def TimestampValidityDuration(self) -> TimeSpan:
        """
        Get: TimestampValidityDuration(self: LocalServiceSecuritySettingsElement) -> TimeSpan
        Set: TimestampValidityDuration(self: LocalServiceSecuritySettingsElement) = value
        """
        ...



class MessageLoggingElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ MessageLoggingElement() """
    @property
    def Filters(self): # -> XPathMessageFilterElementCollection
        """ Get: Filters(self: MessageLoggingElement) -> XPathMessageFilterElementCollection """
        ...

    @property
    def LogEntireMessage(self) -> bool:
        """
        Get: LogEntireMessage(self: MessageLoggingElement) -> bool
        Set: LogEntireMessage(self: MessageLoggingElement) = value
        """
        ...

    @property
    def LogKnownPii(self) -> bool:
        """
        Get: LogKnownPii(self: MessageLoggingElement) -> bool
        Set: LogKnownPii(self: MessageLoggingElement) = value
        """
        ...

    @property
    def LogMalformedMessages(self) -> bool:
        """
        Get: LogMalformedMessages(self: MessageLoggingElement) -> bool
        Set: LogMalformedMessages(self: MessageLoggingElement) = value
        """
        ...

    @property
    def LogMessagesAtServiceLevel(self) -> bool:
        """
        Get: LogMessagesAtServiceLevel(self: MessageLoggingElement) -> bool
        Set: LogMessagesAtServiceLevel(self: MessageLoggingElement) = value
        """
        ...

    @property
    def LogMessagesAtTransportLevel(self) -> bool:
        """
        Get: LogMessagesAtTransportLevel(self: MessageLoggingElement) -> bool
        Set: LogMessagesAtTransportLevel(self: MessageLoggingElement) = value
        """
        ...

    @property
    def MaxMessagesToLog(self) -> int:
        """
        Get: MaxMessagesToLog(self: MessageLoggingElement) -> int
        Set: MaxMessagesToLog(self: MessageLoggingElement) = value
        """
        ...

    @property
    def MaxSizeOfMessageToLog(self) -> int:
        """
        Get: MaxSizeOfMessageToLog(self: MessageLoggingElement) -> int
        Set: MaxSizeOfMessageToLog(self: MessageLoggingElement) = value
        """
        ...



class MessageSecurityOverHttpElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AlgorithmSuite(self) -> SecurityAlgorithmSuite:
        """
        Get: AlgorithmSuite(self: MessageSecurityOverHttpElement) -> SecurityAlgorithmSuite
        Set: AlgorithmSuite(self: MessageSecurityOverHttpElement) = value
        """
        ...

    @property
    def ClientCredentialType(self) -> MessageCredentialType:
        """
        Get: ClientCredentialType(self: MessageSecurityOverHttpElement) -> MessageCredentialType
        Set: ClientCredentialType(self: MessageSecurityOverHttpElement) = value
        """
        ...

    @property
    def NegotiateServiceCredential(self) -> bool:
        """
        Get: NegotiateServiceCredential(self: MessageSecurityOverHttpElement) -> bool
        Set: NegotiateServiceCredential(self: MessageSecurityOverHttpElement) = value
        """
        ...



class MessageSecurityOverMsmqElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ MessageSecurityOverMsmqElement() """
    @property
    def AlgorithmSuite(self) -> SecurityAlgorithmSuite:
        """
        Get: AlgorithmSuite(self: MessageSecurityOverMsmqElement) -> SecurityAlgorithmSuite
        Set: AlgorithmSuite(self: MessageSecurityOverMsmqElement) = value
        """
        ...

    @property
    def ClientCredentialType(self) -> MessageCredentialType:
        """
        Get: ClientCredentialType(self: MessageSecurityOverMsmqElement) -> MessageCredentialType
        Set: ClientCredentialType(self: MessageSecurityOverMsmqElement) = value
        """
        ...



class MessageSecurityOverTcpElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ MessageSecurityOverTcpElement() """
    @property
    def AlgorithmSuite(self) -> SecurityAlgorithmSuite:
        """
        Get: AlgorithmSuite(self: MessageSecurityOverTcpElement) -> SecurityAlgorithmSuite
        Set: AlgorithmSuite(self: MessageSecurityOverTcpElement) = value
        """
        ...

    @property
    def ClientCredentialType(self) -> MessageCredentialType:
        """
        Get: ClientCredentialType(self: MessageSecurityOverTcpElement) -> MessageCredentialType
        Set: ClientCredentialType(self: MessageSecurityOverTcpElement) = value
        """
        ...



class MetadataElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ MetadataElement() """
    @property
    def PolicyImporters(self): # -> PolicyImporterElementCollection
        """ Get: PolicyImporters(self: MetadataElement) -> PolicyImporterElementCollection """
        ...

    @property
    def WsdlImporters(self): # -> WsdlImporterElementCollection
        """ Get: WsdlImporters(self: MetadataElement) -> WsdlImporterElementCollection """
        ...


    def LoadPolicyImportExtensions(self) -> Collection:
        """ LoadPolicyImportExtensions(self: MetadataElement) -> Collection[IPolicyImportExtension] """
        ...

    def LoadWsdlImportExtensions(self) -> Collection:
        """ LoadWsdlImportExtensions(self: MetadataElement) -> Collection[IWsdlImportExtension] """
        ...


class MexBindingBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ no doc """
    pass

class MexBindingElement(StandardBindingElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ no doc """
    pass

class MexHttpBindingCollectionElement(MexBindingBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ MexHttpBindingCollectionElement() """
    pass

class MexHttpBindingElement(MexBindingElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    MexHttpBindingElement(name: str)
    MexHttpBindingElement()
    """
    pass

class MexHttpsBindingCollectionElement(MexBindingBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ MexHttpsBindingCollectionElement() """
    pass

class MexHttpsBindingElement(MexBindingElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    MexHttpsBindingElement(name: str)
    MexHttpsBindingElement()
    """
    pass

class MexNamedPipeBindingCollectionElement(MexBindingBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ MexNamedPipeBindingCollectionElement() """
    pass

class MexNamedPipeBindingElement(MexBindingElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    MexNamedPipeBindingElement(name: str)
    MexNamedPipeBindingElement()
    """
    pass

class MexTcpBindingCollectionElement(MexBindingBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ MexTcpBindingCollectionElement() """
    pass

class MexTcpBindingElement(MexBindingElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    MexTcpBindingElement(name: str)
    MexTcpBindingElement()
    """
    pass

class MsmqBindingElementBase(StandardBindingElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ no doc """
    @property
    def CustomDeadLetterQueue(self) -> Uri:
        """
        Get: CustomDeadLetterQueue(self: MsmqBindingElementBase) -> Uri
        Set: CustomDeadLetterQueue(self: MsmqBindingElementBase) = value
        """
        ...

    @property
    def DeadLetterQueue(self) -> DeadLetterQueue:
        """
        Get: DeadLetterQueue(self: MsmqBindingElementBase) -> DeadLetterQueue
        Set: DeadLetterQueue(self: MsmqBindingElementBase) = value
        """
        ...

    @property
    def Durable(self) -> bool:
        """
        Get: Durable(self: MsmqBindingElementBase) -> bool
        Set: Durable(self: MsmqBindingElementBase) = value
        """
        ...

    @property
    def ExactlyOnce(self) -> bool:
        """
        Get: ExactlyOnce(self: MsmqBindingElementBase) -> bool
        Set: ExactlyOnce(self: MsmqBindingElementBase) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: MsmqBindingElementBase) -> Int64
        Set: MaxReceivedMessageSize(self: MsmqBindingElementBase) = value
        """
        ...

    @property
    def MaxRetryCycles(self) -> int:
        """
        Get: MaxRetryCycles(self: MsmqBindingElementBase) -> int
        Set: MaxRetryCycles(self: MsmqBindingElementBase) = value
        """
        ...

    @property
    def ReceiveContextEnabled(self) -> bool:
        """
        Get: ReceiveContextEnabled(self: MsmqBindingElementBase) -> bool
        Set: ReceiveContextEnabled(self: MsmqBindingElementBase) = value
        """
        ...

    @property
    def ReceiveErrorHandling(self) -> ReceiveErrorHandling:
        """
        Get: ReceiveErrorHandling(self: MsmqBindingElementBase) -> ReceiveErrorHandling
        Set: ReceiveErrorHandling(self: MsmqBindingElementBase) = value
        """
        ...

    @property
    def ReceiveRetryCount(self) -> int:
        """
        Get: ReceiveRetryCount(self: MsmqBindingElementBase) -> int
        Set: ReceiveRetryCount(self: MsmqBindingElementBase) = value
        """
        ...

    @property
    def RetryCycleDelay(self) -> TimeSpan:
        """
        Get: RetryCycleDelay(self: MsmqBindingElementBase) -> TimeSpan
        Set: RetryCycleDelay(self: MsmqBindingElementBase) = value
        """
        ...

    @property
    def TimeToLive(self) -> TimeSpan:
        """
        Get: TimeToLive(self: MsmqBindingElementBase) -> TimeSpan
        Set: TimeToLive(self: MsmqBindingElementBase) = value
        """
        ...

    @property
    def UseMsmqTracing(self) -> bool:
        """
        Get: UseMsmqTracing(self: MsmqBindingElementBase) -> bool
        Set: UseMsmqTracing(self: MsmqBindingElementBase) = value
        """
        ...

    @property
    def UseSourceJournal(self) -> bool:
        """
        Get: UseSourceJournal(self: MsmqBindingElementBase) -> bool
        Set: UseSourceJournal(self: MsmqBindingElementBase) = value
        """
        ...

    @property
    def ValidityDuration(self) -> TimeSpan:
        """
        Get: ValidityDuration(self: MsmqBindingElementBase) -> TimeSpan
        Set: ValidityDuration(self: MsmqBindingElementBase) = value
        """
        ...



class MsmqElementBase(TransportElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ no doc """
    @property
    def CustomDeadLetterQueue(self) -> Uri:
        """
        Get: CustomDeadLetterQueue(self: MsmqElementBase) -> Uri
        Set: CustomDeadLetterQueue(self: MsmqElementBase) = value
        """
        ...

    @property
    def DeadLetterQueue(self) -> DeadLetterQueue:
        """
        Get: DeadLetterQueue(self: MsmqElementBase) -> DeadLetterQueue
        Set: DeadLetterQueue(self: MsmqElementBase) = value
        """
        ...

    @property
    def Durable(self) -> bool:
        """
        Get: Durable(self: MsmqElementBase) -> bool
        Set: Durable(self: MsmqElementBase) = value
        """
        ...

    @property
    def ExactlyOnce(self) -> bool:
        """
        Get: ExactlyOnce(self: MsmqElementBase) -> bool
        Set: ExactlyOnce(self: MsmqElementBase) = value
        """
        ...

    @property
    def MaxRetryCycles(self) -> int:
        """
        Get: MaxRetryCycles(self: MsmqElementBase) -> int
        Set: MaxRetryCycles(self: MsmqElementBase) = value
        """
        ...

    @property
    def MsmqTransportSecurity(self): # -> MsmqTransportSecurityElement
        """ Get: MsmqTransportSecurity(self: MsmqElementBase) -> MsmqTransportSecurityElement """
        ...

    @property
    def ReceiveContextEnabled(self) -> bool:
        """
        Get: ReceiveContextEnabled(self: MsmqElementBase) -> bool
        Set: ReceiveContextEnabled(self: MsmqElementBase) = value
        """
        ...

    @property
    def ReceiveErrorHandling(self) -> ReceiveErrorHandling:
        """
        Get: ReceiveErrorHandling(self: MsmqElementBase) -> ReceiveErrorHandling
        Set: ReceiveErrorHandling(self: MsmqElementBase) = value
        """
        ...

    @property
    def ReceiveRetryCount(self) -> int:
        """
        Get: ReceiveRetryCount(self: MsmqElementBase) -> int
        Set: ReceiveRetryCount(self: MsmqElementBase) = value
        """
        ...

    @property
    def RetryCycleDelay(self) -> TimeSpan:
        """
        Get: RetryCycleDelay(self: MsmqElementBase) -> TimeSpan
        Set: RetryCycleDelay(self: MsmqElementBase) = value
        """
        ...

    @property
    def TimeToLive(self) -> TimeSpan:
        """
        Get: TimeToLive(self: MsmqElementBase) -> TimeSpan
        Set: TimeToLive(self: MsmqElementBase) = value
        """
        ...

    @property
    def UseMsmqTracing(self) -> bool:
        """
        Get: UseMsmqTracing(self: MsmqElementBase) -> bool
        Set: UseMsmqTracing(self: MsmqElementBase) = value
        """
        ...

    @property
    def UseSourceJournal(self) -> bool:
        """
        Get: UseSourceJournal(self: MsmqElementBase) -> bool
        Set: UseSourceJournal(self: MsmqElementBase) = value
        """
        ...

    @property
    def ValidityDuration(self) -> TimeSpan:
        """
        Get: ValidityDuration(self: MsmqElementBase) -> TimeSpan
        Set: ValidityDuration(self: MsmqElementBase) = value
        """
        ...



class MsmqIntegrationBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ MsmqIntegrationBindingCollectionElement() """
    pass

class MsmqIntegrationBindingElement(MsmqBindingElementBase): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    MsmqIntegrationBindingElement(name: str)
    MsmqIntegrationBindingElement()
    """
    @property
    def Security(self): # -> MsmqIntegrationSecurityElement
        """ Get: Security(self: MsmqIntegrationBindingElement) -> MsmqIntegrationSecurityElement """
        ...

    @property
    def SerializationFormat(self) -> MsmqMessageSerializationFormat:
        """
        Get: SerializationFormat(self: MsmqIntegrationBindingElement) -> MsmqMessageSerializationFormat
        Set: SerializationFormat(self: MsmqIntegrationBindingElement) = value
        """
        ...



class MsmqIntegrationElement(MsmqElementBase): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ MsmqIntegrationElement() """
    @property
    def BindingElementType(self) -> Type:
        """ Get: BindingElementType(self: MsmqIntegrationElement) -> Type """
        ...

    @property
    def SerializationFormat(self) -> MsmqMessageSerializationFormat:
        """
        Get: SerializationFormat(self: MsmqIntegrationElement) -> MsmqMessageSerializationFormat
        Set: SerializationFormat(self: MsmqIntegrationElement) = value
        """
        ...



class MsmqIntegrationSecurityElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ MsmqIntegrationSecurityElement() """
    @property
    def Mode(self) -> MsmqIntegrationSecurityMode:
        """
        Get: Mode(self: MsmqIntegrationSecurityElement) -> MsmqIntegrationSecurityMode
        Set: Mode(self: MsmqIntegrationSecurityElement) = value
        """
        ...

    @property
    def Transport(self): # -> MsmqTransportSecurityElement
        """ Get: Transport(self: MsmqIntegrationSecurityElement) -> MsmqTransportSecurityElement """
        ...



class MsmqTransportElement(MsmqElementBase): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ MsmqTransportElement() """
    @property
    def BindingElementType(self) -> Type:
        """ Get: BindingElementType(self: MsmqTransportElement) -> Type """
        ...

    @property
    def MaxPoolSize(self) -> int:
        """
        Get: MaxPoolSize(self: MsmqTransportElement) -> int
        Set: MaxPoolSize(self: MsmqTransportElement) = value
        """
        ...

    @property
    def QueueTransferProtocol(self) -> QueueTransferProtocol:
        """
        Get: QueueTransferProtocol(self: MsmqTransportElement) -> QueueTransferProtocol
        Set: QueueTransferProtocol(self: MsmqTransportElement) = value
        """
        ...

    @property
    def UseActiveDirectory(self) -> bool:
        """
        Get: UseActiveDirectory(self: MsmqTransportElement) -> bool
        Set: UseActiveDirectory(self: MsmqTransportElement) = value
        """
        ...



class MsmqTransportSecurityElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ MsmqTransportSecurityElement() """
    @property
    def MsmqAuthenticationMode(self) -> MsmqAuthenticationMode:
        """
        Get: MsmqAuthenticationMode(self: MsmqTransportSecurityElement) -> MsmqAuthenticationMode
        Set: MsmqAuthenticationMode(self: MsmqTransportSecurityElement) = value
        """
        ...

    @property
    def MsmqEncryptionAlgorithm(self) -> MsmqEncryptionAlgorithm:
        """
        Get: MsmqEncryptionAlgorithm(self: MsmqTransportSecurityElement) -> MsmqEncryptionAlgorithm
        Set: MsmqEncryptionAlgorithm(self: MsmqTransportSecurityElement) = value
        """
        ...

    @property
    def MsmqProtectionLevel(self) -> ProtectionLevel:
        """
        Get: MsmqProtectionLevel(self: MsmqTransportSecurityElement) -> ProtectionLevel
        Set: MsmqProtectionLevel(self: MsmqTransportSecurityElement) = value
        """
        ...

    @property
    def MsmqSecureHashAlgorithm(self) -> MsmqSecureHashAlgorithm:
        """
        Get: MsmqSecureHashAlgorithm(self: MsmqTransportSecurityElement) -> MsmqSecureHashAlgorithm
        Set: MsmqSecureHashAlgorithm(self: MsmqTransportSecurityElement) = value
        """
        ...



class MtomMessageEncodingElement(BindingElementExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ MtomMessageEncodingElement() """
    @property
    def MaxBufferSize(self) -> int:
        """
        Get: MaxBufferSize(self: MtomMessageEncodingElement) -> int
        Set: MaxBufferSize(self: MtomMessageEncodingElement) = value
        """
        ...

    @property
    def MaxReadPoolSize(self) -> int:
        """
        Get: MaxReadPoolSize(self: MtomMessageEncodingElement) -> int
        Set: MaxReadPoolSize(self: MtomMessageEncodingElement) = value
        """
        ...

    @property
    def MaxWritePoolSize(self) -> int:
        """
        Get: MaxWritePoolSize(self: MtomMessageEncodingElement) -> int
        Set: MaxWritePoolSize(self: MtomMessageEncodingElement) = value
        """
        ...

    @property
    def MessageVersion(self): # -> MessageVersion
        """
        Get: MessageVersion(self: MtomMessageEncodingElement) -> MessageVersion
        Set: MessageVersion(self: MtomMessageEncodingElement) = value
        """
        ...

    @property
    def ReaderQuotas(self): # -> XmlDictionaryReaderQuotasElement
        """ Get: ReaderQuotas(self: MtomMessageEncodingElement) -> XmlDictionaryReaderQuotasElement """
        ...

    @property
    def WriteEncoding(self) -> Encoding:
        """
        Get: WriteEncoding(self: MtomMessageEncodingElement) -> Encoding
        Set: WriteEncoding(self: MtomMessageEncodingElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: MtomMessageEncodingElement, from: ServiceModelExtensionElement) """
        ...


class NamedPipeConnectionPoolSettingsElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ NamedPipeConnectionPoolSettingsElement() """
    @property
    def GroupName(self) -> str:
        """
        Get: GroupName(self: NamedPipeConnectionPoolSettingsElement) -> str
        Set: GroupName(self: NamedPipeConnectionPoolSettingsElement) = value
        """
        ...

    @property
    def IdleTimeout(self) -> TimeSpan:
        """
        Get: IdleTimeout(self: NamedPipeConnectionPoolSettingsElement) -> TimeSpan
        Set: IdleTimeout(self: NamedPipeConnectionPoolSettingsElement) = value
        """
        ...

    @property
    def MaxOutboundConnectionsPerEndpoint(self) -> int:
        """
        Get: MaxOutboundConnectionsPerEndpoint(self: NamedPipeConnectionPoolSettingsElement) -> int
        Set: MaxOutboundConnectionsPerEndpoint(self: NamedPipeConnectionPoolSettingsElement) = value
        """
        ...



class NamedPipeSettingsElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ NamedPipeSettingsElement() """
    @property
    def ApplicationContainerSettings(self) -> ApplicationContainerSettingsElement:
        """
        Get: ApplicationContainerSettings(self: NamedPipeSettingsElement) -> ApplicationContainerSettingsElement
        Set: ApplicationContainerSettings(self: NamedPipeSettingsElement) = value
        """
        ...



class NamedPipeTransportElement(ConnectionOrientedTransportElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ NamedPipeTransportElement() """
    @property
    def BindingElementType(self) -> Type:
        """ Get: BindingElementType(self: NamedPipeTransportElement) -> Type """
        ...

    @property
    def ConnectionPoolSettings(self) -> NamedPipeConnectionPoolSettingsElement:
        """
        Get: ConnectionPoolSettings(self: NamedPipeTransportElement) -> NamedPipeConnectionPoolSettingsElement
        Set: ConnectionPoolSettings(self: NamedPipeTransportElement) = value
        """
        ...

    @property
    def PipeSettings(self) -> NamedPipeSettingsElement:
        """
        Get: PipeSettings(self: NamedPipeTransportElement) -> NamedPipeSettingsElement
        Set: PipeSettings(self: NamedPipeTransportElement) = value
        """
        ...



class NamedPipeTransportSecurityElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ NamedPipeTransportSecurityElement() """
    @property
    def ProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ProtectionLevel(self: NamedPipeTransportSecurityElement) -> ProtectionLevel
        Set: ProtectionLevel(self: NamedPipeTransportSecurityElement) = value
        """
        ...



class NamedServiceModelExtensionCollectionElement(ServiceModelExtensionCollectionElement): # skipped bases: <type 'IEnumerable[TServiceModelExtensionElement]'>, <type 'ICollection[TServiceModelExtensionElement]'>, <type 'IEnumerable'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: NamedServiceModelExtensionCollectionElement[TServiceModelExtensionElement]) -> str
        Set: Name(self: NamedServiceModelExtensionCollectionElement[TServiceModelExtensionElement]) = value
        """
        ...



class NetHttpBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ NetHttpBindingCollectionElement() """
    pass

class NetHttpBindingElement(HttpBindingBaseElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    NetHttpBindingElement(name: str)
    NetHttpBindingElement()
    """
    @property
    def MessageEncoding(self) -> NetHttpMessageEncoding:
        """
        Get: MessageEncoding(self: NetHttpBindingElement) -> NetHttpMessageEncoding
        Set: MessageEncoding(self: NetHttpBindingElement) = value
        """
        ...

    @property
    def ReliableSession(self): # -> StandardBindingOptionalReliableSessionElement
        """ Get: ReliableSession(self: NetHttpBindingElement) -> StandardBindingOptionalReliableSessionElement """
        ...

    @property
    def Security(self) -> BasicHttpSecurityElement:
        """ Get: Security(self: NetHttpBindingElement) -> BasicHttpSecurityElement """
        ...

    @property
    def WebSocketSettings(self): # -> NetHttpWebSocketTransportSettingsElement
        """
        Get: WebSocketSettings(self: NetHttpBindingElement) -> NetHttpWebSocketTransportSettingsElement
        Set: WebSocketSettings(self: NetHttpBindingElement) = value
        """
        ...



class NetHttpsBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ NetHttpsBindingCollectionElement() """
    pass

class NetHttpsBindingElement(HttpBindingBaseElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    NetHttpsBindingElement(name: str)
    NetHttpsBindingElement()
    """
    @property
    def MessageEncoding(self) -> NetHttpMessageEncoding:
        """
        Get: MessageEncoding(self: NetHttpsBindingElement) -> NetHttpMessageEncoding
        Set: MessageEncoding(self: NetHttpsBindingElement) = value
        """
        ...

    @property
    def ReliableSession(self): # -> StandardBindingOptionalReliableSessionElement
        """ Get: ReliableSession(self: NetHttpsBindingElement) -> StandardBindingOptionalReliableSessionElement """
        ...

    @property
    def Security(self) -> BasicHttpsSecurityElement:
        """ Get: Security(self: NetHttpsBindingElement) -> BasicHttpsSecurityElement """
        ...

    @property
    def WebSocketSettings(self): # -> NetHttpWebSocketTransportSettingsElement
        """
        Get: WebSocketSettings(self: NetHttpsBindingElement) -> NetHttpWebSocketTransportSettingsElement
        Set: WebSocketSettings(self: NetHttpsBindingElement) = value
        """
        ...



class WebSocketTransportSettingsElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ WebSocketTransportSettingsElement() """
    @property
    def CreateNotificationOnConnection(self) -> bool:
        """
        Get: CreateNotificationOnConnection(self: WebSocketTransportSettingsElement) -> bool
        Set: CreateNotificationOnConnection(self: WebSocketTransportSettingsElement) = value
        """
        ...

    @property
    def DisablePayloadMasking(self) -> bool:
        """
        Get: DisablePayloadMasking(self: WebSocketTransportSettingsElement) -> bool
        Set: DisablePayloadMasking(self: WebSocketTransportSettingsElement) = value
        """
        ...

    @property
    def KeepAliveInterval(self) -> TimeSpan:
        """
        Get: KeepAliveInterval(self: WebSocketTransportSettingsElement) -> TimeSpan
        Set: KeepAliveInterval(self: WebSocketTransportSettingsElement) = value
        """
        ...

    @property
    def MaxPendingConnections(self) -> int:
        """
        Get: MaxPendingConnections(self: WebSocketTransportSettingsElement) -> int
        Set: MaxPendingConnections(self: WebSocketTransportSettingsElement) = value
        """
        ...

    @property
    def SubProtocol(self) -> str:
        """
        Get: SubProtocol(self: WebSocketTransportSettingsElement) -> str
        Set: SubProtocol(self: WebSocketTransportSettingsElement) = value
        """
        ...

    @property
    def TransportUsage(self): # -> WebSocketTransportUsage
        """
        Get: TransportUsage(self: WebSocketTransportSettingsElement) -> WebSocketTransportUsage
        Set: TransportUsage(self: WebSocketTransportSettingsElement) = value
        """
        ...


    def ApplyConfiguration(self, settings): # ->  # Not found arg types: {'settings': 'WebSocketTransportSettings'}
        """ ApplyConfiguration(self: WebSocketTransportSettingsElement, settings: WebSocketTransportSettings) """
        ...

    def InitializeFrom(self, settings): # ->  # Not found arg types: {'settings': 'WebSocketTransportSettings'}
        """ InitializeFrom(self: WebSocketTransportSettingsElement, settings: WebSocketTransportSettings) """
        ...


class NetHttpWebSocketTransportSettingsElement(WebSocketTransportSettingsElement): # skipped bases: <type 'object'>
    """ NetHttpWebSocketTransportSettingsElement() """
    pass

class NetMsmqBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ NetMsmqBindingCollectionElement() """
    pass

class NetMsmqBindingElement(MsmqBindingElementBase): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    NetMsmqBindingElement(name: str)
    NetMsmqBindingElement()
    """
    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: NetMsmqBindingElement) -> Int64
        Set: MaxBufferPoolSize(self: NetMsmqBindingElement) = value
        """
        ...

    @property
    def QueueTransferProtocol(self) -> QueueTransferProtocol:
        """
        Get: QueueTransferProtocol(self: NetMsmqBindingElement) -> QueueTransferProtocol
        Set: QueueTransferProtocol(self: NetMsmqBindingElement) = value
        """
        ...

    @property
    def ReaderQuotas(self): # -> XmlDictionaryReaderQuotasElement
        """ Get: ReaderQuotas(self: NetMsmqBindingElement) -> XmlDictionaryReaderQuotasElement """
        ...

    @property
    def Security(self): # -> NetMsmqSecurityElement
        """ Get: Security(self: NetMsmqBindingElement) -> NetMsmqSecurityElement """
        ...

    @property
    def UseActiveDirectory(self) -> bool:
        """
        Get: UseActiveDirectory(self: NetMsmqBindingElement) -> bool
        Set: UseActiveDirectory(self: NetMsmqBindingElement) = value
        """
        ...



class NetMsmqSecurityElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ NetMsmqSecurityElement() """
    @property
    def Message(self) -> MessageSecurityOverMsmqElement:
        """ Get: Message(self: NetMsmqSecurityElement) -> MessageSecurityOverMsmqElement """
        ...

    @property
    def Mode(self) -> NetMsmqSecurityMode:
        """
        Get: Mode(self: NetMsmqSecurityElement) -> NetMsmqSecurityMode
        Set: Mode(self: NetMsmqSecurityElement) = value
        """
        ...

    @property
    def Transport(self) -> MsmqTransportSecurityElement:
        """ Get: Transport(self: NetMsmqSecurityElement) -> MsmqTransportSecurityElement """
        ...



class NetNamedPipeBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ NetNamedPipeBindingCollectionElement() """
    pass

class NetNamedPipeBindingElement(StandardBindingElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    NetNamedPipeBindingElement(name: str)
    NetNamedPipeBindingElement()
    """
    @property
    def HostNameComparisonMode(self) -> HostNameComparisonMode:
        """
        Get: HostNameComparisonMode(self: NetNamedPipeBindingElement) -> HostNameComparisonMode
        Set: HostNameComparisonMode(self: NetNamedPipeBindingElement) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: NetNamedPipeBindingElement) -> Int64
        Set: MaxBufferPoolSize(self: NetNamedPipeBindingElement) = value
        """
        ...

    @property
    def MaxBufferSize(self) -> int:
        """
        Get: MaxBufferSize(self: NetNamedPipeBindingElement) -> int
        Set: MaxBufferSize(self: NetNamedPipeBindingElement) = value
        """
        ...

    @property
    def MaxConnections(self) -> int:
        """
        Get: MaxConnections(self: NetNamedPipeBindingElement) -> int
        Set: MaxConnections(self: NetNamedPipeBindingElement) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: NetNamedPipeBindingElement) -> Int64
        Set: MaxReceivedMessageSize(self: NetNamedPipeBindingElement) = value
        """
        ...

    @property
    def ReaderQuotas(self): # -> XmlDictionaryReaderQuotasElement
        """ Get: ReaderQuotas(self: NetNamedPipeBindingElement) -> XmlDictionaryReaderQuotasElement """
        ...

    @property
    def Security(self): # -> NetNamedPipeSecurityElement
        """ Get: Security(self: NetNamedPipeBindingElement) -> NetNamedPipeSecurityElement """
        ...

    @property
    def TransactionFlow(self) -> bool:
        """
        Get: TransactionFlow(self: NetNamedPipeBindingElement) -> bool
        Set: TransactionFlow(self: NetNamedPipeBindingElement) = value
        """
        ...

    @property
    def TransactionProtocol(self) -> TransactionProtocol:
        """
        Get: TransactionProtocol(self: NetNamedPipeBindingElement) -> TransactionProtocol
        Set: TransactionProtocol(self: NetNamedPipeBindingElement) = value
        """
        ...

    @property
    def TransferMode(self) -> TransferMode:
        """
        Get: TransferMode(self: NetNamedPipeBindingElement) -> TransferMode
        Set: TransferMode(self: NetNamedPipeBindingElement) = value
        """
        ...



class NetNamedPipeSecurityElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ NetNamedPipeSecurityElement() """
    @property
    def Mode(self) -> NetNamedPipeSecurityMode:
        """
        Get: Mode(self: NetNamedPipeSecurityElement) -> NetNamedPipeSecurityMode
        Set: Mode(self: NetNamedPipeSecurityElement) = value
        """
        ...

    @property
    def Transport(self) -> NamedPipeTransportSecurityElement:
        """ Get: Transport(self: NetNamedPipeSecurityElement) -> NamedPipeTransportSecurityElement """
        ...



class NetPeerTcpBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ NetPeerTcpBindingCollectionElement() """
    pass

class NetPeerTcpBindingElement(StandardBindingElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    NetPeerTcpBindingElement(name: str)
    NetPeerTcpBindingElement()
    """
    @property
    def ListenIPAddress(self) -> IPAddress:
        """
        Get: ListenIPAddress(self: NetPeerTcpBindingElement) -> IPAddress
        Set: ListenIPAddress(self: NetPeerTcpBindingElement) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: NetPeerTcpBindingElement) -> Int64
        Set: MaxBufferPoolSize(self: NetPeerTcpBindingElement) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: NetPeerTcpBindingElement) -> Int64
        Set: MaxReceivedMessageSize(self: NetPeerTcpBindingElement) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: NetPeerTcpBindingElement) -> int
        Set: Port(self: NetPeerTcpBindingElement) = value
        """
        ...

    @property
    def ReaderQuotas(self): # -> XmlDictionaryReaderQuotasElement
        """ Get: ReaderQuotas(self: NetPeerTcpBindingElement) -> XmlDictionaryReaderQuotasElement """
        ...

    @property
    def Resolver(self): # -> PeerResolverElement
        """ Get: Resolver(self: NetPeerTcpBindingElement) -> PeerResolverElement """
        ...

    @property
    def Security(self): # -> PeerSecurityElement
        """ Get: Security(self: NetPeerTcpBindingElement) -> PeerSecurityElement """
        ...



class NetTcpBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ NetTcpBindingCollectionElement() """
    pass

class NetTcpBindingElement(StandardBindingElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    NetTcpBindingElement(name: str)
    NetTcpBindingElement()
    """
    @property
    def HostNameComparisonMode(self) -> HostNameComparisonMode:
        """
        Get: HostNameComparisonMode(self: NetTcpBindingElement) -> HostNameComparisonMode
        Set: HostNameComparisonMode(self: NetTcpBindingElement) = value
        """
        ...

    @property
    def ListenBacklog(self) -> int:
        """
        Get: ListenBacklog(self: NetTcpBindingElement) -> int
        Set: ListenBacklog(self: NetTcpBindingElement) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: NetTcpBindingElement) -> Int64
        Set: MaxBufferPoolSize(self: NetTcpBindingElement) = value
        """
        ...

    @property
    def MaxBufferSize(self) -> int:
        """
        Get: MaxBufferSize(self: NetTcpBindingElement) -> int
        Set: MaxBufferSize(self: NetTcpBindingElement) = value
        """
        ...

    @property
    def MaxConnections(self) -> int:
        """
        Get: MaxConnections(self: NetTcpBindingElement) -> int
        Set: MaxConnections(self: NetTcpBindingElement) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: NetTcpBindingElement) -> Int64
        Set: MaxReceivedMessageSize(self: NetTcpBindingElement) = value
        """
        ...

    @property
    def PortSharingEnabled(self) -> bool:
        """
        Get: PortSharingEnabled(self: NetTcpBindingElement) -> bool
        Set: PortSharingEnabled(self: NetTcpBindingElement) = value
        """
        ...

    @property
    def ReaderQuotas(self): # -> XmlDictionaryReaderQuotasElement
        """ Get: ReaderQuotas(self: NetTcpBindingElement) -> XmlDictionaryReaderQuotasElement """
        ...

    @property
    def ReliableSession(self): # -> StandardBindingOptionalReliableSessionElement
        """ Get: ReliableSession(self: NetTcpBindingElement) -> StandardBindingOptionalReliableSessionElement """
        ...

    @property
    def Security(self): # -> NetTcpSecurityElement
        """ Get: Security(self: NetTcpBindingElement) -> NetTcpSecurityElement """
        ...

    @property
    def TransactionFlow(self) -> bool:
        """
        Get: TransactionFlow(self: NetTcpBindingElement) -> bool
        Set: TransactionFlow(self: NetTcpBindingElement) = value
        """
        ...

    @property
    def TransactionProtocol(self) -> TransactionProtocol:
        """
        Get: TransactionProtocol(self: NetTcpBindingElement) -> TransactionProtocol
        Set: TransactionProtocol(self: NetTcpBindingElement) = value
        """
        ...

    @property
    def TransferMode(self) -> TransferMode:
        """
        Get: TransferMode(self: NetTcpBindingElement) -> TransferMode
        Set: TransferMode(self: NetTcpBindingElement) = value
        """
        ...



class NetTcpContextBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ NetTcpContextBindingCollectionElement() """
    pass

class NetTcpContextBindingElement(NetTcpBindingElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    NetTcpContextBindingElement()
    NetTcpContextBindingElement(name: str)
    """
    @property
    def ClientCallbackAddress(self) -> Uri:
        """
        Get: ClientCallbackAddress(self: NetTcpContextBindingElement) -> Uri
        Set: ClientCallbackAddress(self: NetTcpContextBindingElement) = value
        """
        ...

    @property
    def ContextManagementEnabled(self) -> bool:
        """
        Get: ContextManagementEnabled(self: NetTcpContextBindingElement) -> bool
        Set: ContextManagementEnabled(self: NetTcpContextBindingElement) = value
        """
        ...

    @property
    def ContextProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ContextProtectionLevel(self: NetTcpContextBindingElement) -> ProtectionLevel
        Set: ContextProtectionLevel(self: NetTcpContextBindingElement) = value
        """
        ...



class NetTcpSecurityElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ NetTcpSecurityElement() """
    @property
    def Message(self) -> MessageSecurityOverTcpElement:
        """ Get: Message(self: NetTcpSecurityElement) -> MessageSecurityOverTcpElement """
        ...

    @property
    def Mode(self) -> SecurityMode:
        """
        Get: Mode(self: NetTcpSecurityElement) -> SecurityMode
        Set: Mode(self: NetTcpSecurityElement) = value
        """
        ...

    @property
    def Transport(self): # -> TcpTransportSecurityElement
        """ Get: Transport(self: NetTcpSecurityElement) -> TcpTransportSecurityElement """
        ...



class NonDualMessageSecurityOverHttpElement(MessageSecurityOverHttpElement): # skipped bases: <type 'object'>
    """ NonDualMessageSecurityOverHttpElement() """
    @property
    def EstablishSecurityContext(self) -> bool:
        """
        Get: EstablishSecurityContext(self: NonDualMessageSecurityOverHttpElement) -> bool
        Set: EstablishSecurityContext(self: NonDualMessageSecurityOverHttpElement) = value
        """
        ...



class OneWayElement(BindingElementExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ OneWayElement() """
    @property
    def ChannelPoolSettings(self) -> ChannelPoolSettingsElement:
        """ Get: ChannelPoolSettings(self: OneWayElement) -> ChannelPoolSettingsElement """
        ...

    @property
    def MaxAcceptedChannels(self) -> int:
        """
        Get: MaxAcceptedChannels(self: OneWayElement) -> int
        Set: MaxAcceptedChannels(self: OneWayElement) = value
        """
        ...

    @property
    def PacketRoutable(self) -> bool:
        """
        Get: PacketRoutable(self: OneWayElement) -> bool
        Set: PacketRoutable(self: OneWayElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: OneWayElement, from: ServiceModelExtensionElement) """
        ...


class PeerCredentialElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ PeerCredentialElement() """
    @property
    def Certificate(self): # -> X509PeerCertificateElement
        """ Get: Certificate(self: PeerCredentialElement) -> X509PeerCertificateElement """
        ...

    @property
    def MessageSenderAuthentication(self): # -> X509PeerCertificateAuthenticationElement
        """ Get: MessageSenderAuthentication(self: PeerCredentialElement) -> X509PeerCertificateAuthenticationElement """
        ...

    @property
    def PeerAuthentication(self): # -> X509PeerCertificateAuthenticationElement
        """ Get: PeerAuthentication(self: PeerCredentialElement) -> X509PeerCertificateAuthenticationElement """
        ...


    def Copy(self, from_:PeerCredentialElement): # -> 
        """ Copy(self: PeerCredentialElement, from: PeerCredentialElement) """
        ...


class PeerCustomResolverElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ PeerCustomResolverElement() """
    @property
    def Address(self) -> Uri:
        """
        Get: Address(self: PeerCustomResolverElement) -> Uri
        Set: Address(self: PeerCustomResolverElement) = value
        """
        ...

    @property
    def Binding(self) -> str:
        """
        Get: Binding(self: PeerCustomResolverElement) -> str
        Set: Binding(self: PeerCustomResolverElement) = value
        """
        ...

    @property
    def BindingConfiguration(self) -> str:
        """
        Get: BindingConfiguration(self: PeerCustomResolverElement) -> str
        Set: BindingConfiguration(self: PeerCustomResolverElement) = value
        """
        ...

    @property
    def Headers(self) -> AddressHeaderCollectionElement:
        """ Get: Headers(self: PeerCustomResolverElement) -> AddressHeaderCollectionElement """
        ...

    @property
    def Identity(self) -> IdentityElement:
        """ Get: Identity(self: PeerCustomResolverElement) -> IdentityElement """
        ...

    @property
    def ResolverType(self) -> str:
        """
        Get: ResolverType(self: PeerCustomResolverElement) -> str
        Set: ResolverType(self: PeerCustomResolverElement) = value
        """
        ...



class PeerResolverElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ PeerResolverElement() """
    @property
    def Custom(self) -> PeerCustomResolverElement:
        """ Get: Custom(self: PeerResolverElement) -> PeerCustomResolverElement """
        ...

    @property
    def Mode(self) -> PeerResolverMode:
        """
        Get: Mode(self: PeerResolverElement) -> PeerResolverMode
        Set: Mode(self: PeerResolverElement) = value
        """
        ...

    @property
    def ReferralPolicy(self) -> PeerReferralPolicy:
        """
        Get: ReferralPolicy(self: PeerResolverElement) -> PeerReferralPolicy
        Set: ReferralPolicy(self: PeerResolverElement) = value
        """
        ...



class PeerSecurityElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ PeerSecurityElement() """
    @property
    def Mode(self) -> SecurityMode:
        """
        Get: Mode(self: PeerSecurityElement) -> SecurityMode
        Set: Mode(self: PeerSecurityElement) = value
        """
        ...

    @property
    def Transport(self): # -> PeerTransportSecurityElement
        """ Get: Transport(self: PeerSecurityElement) -> PeerTransportSecurityElement """
        ...



class PeerTransportElement(BindingElementExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ PeerTransportElement() """
    @property
    def ListenIPAddress(self) -> IPAddress:
        """
        Get: ListenIPAddress(self: PeerTransportElement) -> IPAddress
        Set: ListenIPAddress(self: PeerTransportElement) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: PeerTransportElement) -> Int64
        Set: MaxBufferPoolSize(self: PeerTransportElement) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: PeerTransportElement) -> Int64
        Set: MaxReceivedMessageSize(self: PeerTransportElement) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: PeerTransportElement) -> int
        Set: Port(self: PeerTransportElement) = value
        """
        ...

    @property
    def Security(self) -> PeerSecurityElement:
        """ Get: Security(self: PeerTransportElement) -> PeerSecurityElement """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: PeerTransportElement, from: ServiceModelExtensionElement) """
        ...


class PeerTransportSecurityElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ PeerTransportSecurityElement() """
    @property
    def CredentialType(self) -> PeerTransportCredentialType:
        """
        Get: CredentialType(self: PeerTransportSecurityElement) -> PeerTransportCredentialType
        Set: CredentialType(self: PeerTransportSecurityElement) = value
        """
        ...



class PersistenceProviderElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ PersistenceProviderElement() """
    @property
    def PersistenceOperationTimeout(self) -> TimeSpan:
        """
        Get: PersistenceOperationTimeout(self: PersistenceProviderElement) -> TimeSpan
        Set: PersistenceOperationTimeout(self: PersistenceProviderElement) = value
        """
        ...

    @property
    def PersistenceProviderArguments(self) -> NameValueCollection:
        """ Get: PersistenceProviderArguments(self: PersistenceProviderElement) -> NameValueCollection """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: PersistenceProviderElement) -> str
        Set: Type(self: PersistenceProviderElement) = value
        """
        ...



class PnrpPeerResolverElement(BindingElementExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ PnrpPeerResolverElement() """
    pass

class PolicyImporterElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    PolicyImporterElement()
    PolicyImporterElement(type: str)
    PolicyImporterElement(type: Type)
    """
    @property
    def Type(self) -> str:
        """
        Get: Type(self: PolicyImporterElement) -> str
        Set: Type(self: PolicyImporterElement) = value
        """
        ...


    def __new__(cls, type:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: str)
        __new__(cls: type, type: Type)
        """
        ...


class PolicyImporterElementCollection(ServiceModelEnhancedConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ PolicyImporterElementCollection() """
    pass

class PrivacyNoticeElement(BindingElementExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ PrivacyNoticeElement() """
    @property
    def Url(self) -> Uri:
        """
        Get: Url(self: PrivacyNoticeElement) -> Uri
        Set: Url(self: PrivacyNoticeElement) = value
        """
        ...

    @property
    def Version(self) -> int:
        """
        Get: Version(self: PrivacyNoticeElement) -> int
        Set: Version(self: PrivacyNoticeElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: PrivacyNoticeElement, from: ServiceModelExtensionElement) """
        ...


class ProtocolMappingElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    ProtocolMappingElement()
    ProtocolMappingElement(schemeType: str, binding: str, bindingConfiguration: str)
    """
    @property
    def Binding(self) -> str:
        """
        Get: Binding(self: ProtocolMappingElement) -> str
        Set: Binding(self: ProtocolMappingElement) = value
        """
        ...

    @property
    def BindingConfiguration(self) -> str:
        """
        Get: BindingConfiguration(self: ProtocolMappingElement) -> str
        Set: BindingConfiguration(self: ProtocolMappingElement) = value
        """
        ...

    @property
    def Scheme(self) -> str:
        """
        Get: Scheme(self: ProtocolMappingElement) -> str
        Set: Scheme(self: ProtocolMappingElement) = value
        """
        ...


    def __new__(cls, schemeType:str = ..., binding:str = ..., bindingConfiguration:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, schemeType: str, binding: str, bindingConfiguration: str)
        """
        ...


class ProtocolMappingElementCollection(ServiceModelEnhancedConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ProtocolMappingElementCollection() """
    pass

class ProtocolMappingSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ ProtocolMappingSection() """
    @property
    def ProtocolMappingCollection(self) -> ProtocolMappingElementCollection:
        """ Get: ProtocolMappingCollection(self: ProtocolMappingSection) -> ProtocolMappingElementCollection """
        ...



class ReliableSessionElement(BindingElementExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ ReliableSessionElement() """
    @property
    def AcknowledgementInterval(self) -> TimeSpan:
        """
        Get: AcknowledgementInterval(self: ReliableSessionElement) -> TimeSpan
        Set: AcknowledgementInterval(self: ReliableSessionElement) = value
        """
        ...

    @property
    def FlowControlEnabled(self) -> bool:
        """
        Get: FlowControlEnabled(self: ReliableSessionElement) -> bool
        Set: FlowControlEnabled(self: ReliableSessionElement) = value
        """
        ...

    @property
    def InactivityTimeout(self) -> TimeSpan:
        """
        Get: InactivityTimeout(self: ReliableSessionElement) -> TimeSpan
        Set: InactivityTimeout(self: ReliableSessionElement) = value
        """
        ...

    @property
    def MaxPendingChannels(self) -> int:
        """
        Get: MaxPendingChannels(self: ReliableSessionElement) -> int
        Set: MaxPendingChannels(self: ReliableSessionElement) = value
        """
        ...

    @property
    def MaxRetryCount(self) -> int:
        """
        Get: MaxRetryCount(self: ReliableSessionElement) -> int
        Set: MaxRetryCount(self: ReliableSessionElement) = value
        """
        ...

    @property
    def MaxTransferWindowSize(self) -> int:
        """
        Get: MaxTransferWindowSize(self: ReliableSessionElement) -> int
        Set: MaxTransferWindowSize(self: ReliableSessionElement) = value
        """
        ...

    @property
    def Ordered(self) -> bool:
        """
        Get: Ordered(self: ReliableSessionElement) -> bool
        Set: Ordered(self: ReliableSessionElement) = value
        """
        ...

    @property
    def ReliableMessagingVersion(self) -> ReliableMessagingVersion:
        """
        Get: ReliableMessagingVersion(self: ReliableSessionElement) -> ReliableMessagingVersion
        Set: ReliableMessagingVersion(self: ReliableSessionElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: ReliableSessionElement, from: ServiceModelExtensionElement) """
        ...


class RemoveBehaviorElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ RemoveBehaviorElement() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: RemoveBehaviorElement) -> str
        Set: Name(self: RemoveBehaviorElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: RemoveBehaviorElement, from: ServiceModelExtensionElement) """
        ...


class RsaElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ RsaElement() """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: RsaElement) -> str
        Set: Value(self: RsaElement) = value
        """
        ...



class SecureConversationServiceElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ SecureConversationServiceElement() """
    @property
    def SecurityStateEncoderType(self) -> str:
        """
        Get: SecurityStateEncoderType(self: SecureConversationServiceElement) -> str
        Set: SecurityStateEncoderType(self: SecureConversationServiceElement) = value
        """
        ...


    def Copy(self, from_:SecureConversationServiceElement): # -> 
        """ Copy(self: SecureConversationServiceElement, from: SecureConversationServiceElement) """
        ...


class SecurityElementBase(BindingElementExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ no doc """
    @property
    def AllowInsecureTransport(self) -> bool:
        """
        Get: AllowInsecureTransport(self: SecurityElementBase) -> bool
        Set: AllowInsecureTransport(self: SecurityElementBase) = value
        """
        ...

    @property
    def AllowSerializedSigningTokenOnReply(self) -> bool:
        """
        Get: AllowSerializedSigningTokenOnReply(self: SecurityElementBase) -> bool
        Set: AllowSerializedSigningTokenOnReply(self: SecurityElementBase) = value
        """
        ...

    @property
    def AuthenticationMode(self) -> AuthenticationMode:
        """
        Get: AuthenticationMode(self: SecurityElementBase) -> AuthenticationMode
        Set: AuthenticationMode(self: SecurityElementBase) = value
        """
        ...

    @property
    def CanRenewSecurityContextToken(self) -> bool:
        """
        Get: CanRenewSecurityContextToken(self: SecurityElementBase) -> bool
        Set: CanRenewSecurityContextToken(self: SecurityElementBase) = value
        """
        ...

    @property
    def DefaultAlgorithmSuite(self) -> SecurityAlgorithmSuite:
        """
        Get: DefaultAlgorithmSuite(self: SecurityElementBase) -> SecurityAlgorithmSuite
        Set: DefaultAlgorithmSuite(self: SecurityElementBase) = value
        """
        ...

    @property
    def EnableUnsecuredResponse(self) -> bool:
        """
        Get: EnableUnsecuredResponse(self: SecurityElementBase) -> bool
        Set: EnableUnsecuredResponse(self: SecurityElementBase) = value
        """
        ...

    @property
    def IncludeTimestamp(self) -> bool:
        """
        Get: IncludeTimestamp(self: SecurityElementBase) -> bool
        Set: IncludeTimestamp(self: SecurityElementBase) = value
        """
        ...

    @property
    def IssuedTokenParameters(self) -> IssuedTokenParametersElement:
        """ Get: IssuedTokenParameters(self: SecurityElementBase) -> IssuedTokenParametersElement """
        ...

    @property
    def KeyEntropyMode(self) -> SecurityKeyEntropyMode:
        """
        Get: KeyEntropyMode(self: SecurityElementBase) -> SecurityKeyEntropyMode
        Set: KeyEntropyMode(self: SecurityElementBase) = value
        """
        ...

    @property
    def LocalClientSettings(self) -> LocalClientSecuritySettingsElement:
        """ Get: LocalClientSettings(self: SecurityElementBase) -> LocalClientSecuritySettingsElement """
        ...

    @property
    def LocalServiceSettings(self) -> LocalServiceSecuritySettingsElement:
        """ Get: LocalServiceSettings(self: SecurityElementBase) -> LocalServiceSecuritySettingsElement """
        ...

    @property
    def MessageProtectionOrder(self) -> MessageProtectionOrder:
        """
        Get: MessageProtectionOrder(self: SecurityElementBase) -> MessageProtectionOrder
        Set: MessageProtectionOrder(self: SecurityElementBase) = value
        """
        ...

    @property
    def MessageSecurityVersion(self) -> MessageSecurityVersion:
        """
        Get: MessageSecurityVersion(self: SecurityElementBase) -> MessageSecurityVersion
        Set: MessageSecurityVersion(self: SecurityElementBase) = value
        """
        ...

    @property
    def ProtectTokens(self) -> bool:
        """
        Get: ProtectTokens(self: SecurityElementBase) -> bool
        Set: ProtectTokens(self: SecurityElementBase) = value
        """
        ...

    @property
    def RequireDerivedKeys(self) -> bool:
        """
        Get: RequireDerivedKeys(self: SecurityElementBase) -> bool
        Set: RequireDerivedKeys(self: SecurityElementBase) = value
        """
        ...

    @property
    def RequireSecurityContextCancellation(self) -> bool:
        """
        Get: RequireSecurityContextCancellation(self: SecurityElementBase) -> bool
        Set: RequireSecurityContextCancellation(self: SecurityElementBase) = value
        """
        ...

    @property
    def RequireSignatureConfirmation(self) -> bool:
        """
        Get: RequireSignatureConfirmation(self: SecurityElementBase) -> bool
        Set: RequireSignatureConfirmation(self: SecurityElementBase) = value
        """
        ...

    @property
    def SecurityHeaderLayout(self): # -> SecurityHeaderLayout
        """
        Get: SecurityHeaderLayout(self: SecurityElementBase) -> SecurityHeaderLayout
        Set: SecurityHeaderLayout(self: SecurityElementBase) = value
        """
        ...


    def AddBindingTemplate(self, *args): #cannot find CLR method
        """ AddBindingTemplate(self: SecurityElementBase, bindingTemplates: Dictionary[AuthenticationMode, SecurityBindingElement], mode: AuthenticationMode) """
        ...

    def AddBindingTemplates(self, *args): #cannot find CLR method
        """ AddBindingTemplates(self: SecurityElementBase, bindingTemplates: Dictionary[AuthenticationMode, SecurityBindingElement]) """
        ...

    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: SecurityElementBase, from: ServiceModelExtensionElement) """
        ...

    def InitializeNestedTokenParameterSettings(self, *args): #cannot find CLR method
        """ InitializeNestedTokenParameterSettings(self: SecurityElementBase, sp: SecurityTokenParameters, initializeNestedBindings: bool) """
        ...


class SecurityElement(SecurityElementBase): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ SecurityElement() """
    @property
    def SecureConversationBootstrap(self) -> SecurityElementBase:
        """ Get: SecureConversationBootstrap(self: SecurityElement) -> SecurityElementBase """
        ...



class ServiceActivationElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    ServiceActivationElement()
    ServiceActivationElement(relativeAddress: str)
    ServiceActivationElement(relativeAddress: str, service: str)
    ServiceActivationElement(relativeAddress: str, service: str, factory: str)
    """
    @property
    def Factory(self) -> str:
        """
        Get: Factory(self: ServiceActivationElement) -> str
        Set: Factory(self: ServiceActivationElement) = value
        """
        ...

    @property
    def RelativeAddress(self) -> str:
        """
        Get: RelativeAddress(self: ServiceActivationElement) -> str
        Set: RelativeAddress(self: ServiceActivationElement) = value
        """
        ...

    @property
    def Service(self) -> str:
        """
        Get: Service(self: ServiceActivationElement) -> str
        Set: Service(self: ServiceActivationElement) = value
        """
        ...


    def __new__(cls, relativeAddress:str = ..., service:str = ..., factory:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, relativeAddress: str)
        __new__(cls: type, relativeAddress: str, service: str)
        __new__(cls: type, relativeAddress: str, service: str, factory: str)
        """
        ...


class ServiceActivationElementCollection(ServiceModelConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ServiceActivationElementCollection() """
    pass

class ServiceAuthenticationElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ ServiceAuthenticationElement() """
    @property
    def AuthenticationSchemes(self) -> AuthenticationSchemes:
        """
        Get: AuthenticationSchemes(self: ServiceAuthenticationElement) -> AuthenticationSchemes
        Set: AuthenticationSchemes(self: ServiceAuthenticationElement) = value
        """
        ...

    @property
    def ServiceAuthenticationManagerType(self) -> str:
        """
        Get: ServiceAuthenticationManagerType(self: ServiceAuthenticationElement) -> str
        Set: ServiceAuthenticationManagerType(self: ServiceAuthenticationElement) = value
        """
        ...



class ServiceAuthorizationElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ ServiceAuthorizationElement() """
    @property
    def AuthorizationPolicies(self) -> AuthorizationPolicyTypeElementCollection:
        """ Get: AuthorizationPolicies(self: ServiceAuthorizationElement) -> AuthorizationPolicyTypeElementCollection """
        ...

    @property
    def ImpersonateCallerForAllOperations(self) -> bool:
        """
        Get: ImpersonateCallerForAllOperations(self: ServiceAuthorizationElement) -> bool
        Set: ImpersonateCallerForAllOperations(self: ServiceAuthorizationElement) = value
        """
        ...

    @property
    def ImpersonateOnSerializingReply(self) -> bool:
        """
        Get: ImpersonateOnSerializingReply(self: ServiceAuthorizationElement) -> bool
        Set: ImpersonateOnSerializingReply(self: ServiceAuthorizationElement) = value
        """
        ...

    @property
    def PrincipalPermissionMode(self): # -> PrincipalPermissionMode
        """
        Get: PrincipalPermissionMode(self: ServiceAuthorizationElement) -> PrincipalPermissionMode
        Set: PrincipalPermissionMode(self: ServiceAuthorizationElement) = value
        """
        ...

    @property
    def RoleProviderName(self) -> str:
        """
        Get: RoleProviderName(self: ServiceAuthorizationElement) -> str
        Set: RoleProviderName(self: ServiceAuthorizationElement) = value
        """
        ...

    @property
    def ServiceAuthorizationManagerType(self) -> str:
        """
        Get: ServiceAuthorizationManagerType(self: ServiceAuthorizationElement) -> str
        Set: ServiceAuthorizationManagerType(self: ServiceAuthorizationElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: ServiceAuthorizationElement, from: ServiceModelExtensionElement) """
        ...


class ServiceBehaviorElement(NamedServiceModelExtensionCollectionElement): # skipped bases: <type 'IEnumerable[BehaviorExtensionElement]'>, <type 'IEnumerable'>, <type 'ICollection[BehaviorExtensionElement]'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    ServiceBehaviorElement()
    ServiceBehaviorElement(name: str)
    """
    def CanAdd(self, element:BehaviorExtensionElement) -> bool:
        """ CanAdd(self: ServiceBehaviorElement, element: BehaviorExtensionElement) -> bool """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __new__(cls, name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...


class ServiceBehaviorElementCollection(ServiceModelEnhancedConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ServiceBehaviorElementCollection() """
    pass

class ServiceCredentialsElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ ServiceCredentialsElement() """
    @property
    def ClientCertificate(self): # -> X509InitiatorCertificateServiceElement
        """ Get: ClientCertificate(self: ServiceCredentialsElement) -> X509InitiatorCertificateServiceElement """
        ...

    @property
    def IdentityConfiguration(self) -> str:
        """
        Get: IdentityConfiguration(self: ServiceCredentialsElement) -> str
        Set: IdentityConfiguration(self: ServiceCredentialsElement) = value
        """
        ...

    @property
    def IssuedTokenAuthentication(self) -> IssuedTokenServiceElement:
        """ Get: IssuedTokenAuthentication(self: ServiceCredentialsElement) -> IssuedTokenServiceElement """
        ...

    @property
    def Peer(self) -> PeerCredentialElement:
        """ Get: Peer(self: ServiceCredentialsElement) -> PeerCredentialElement """
        ...

    @property
    def SecureConversationAuthentication(self) -> SecureConversationServiceElement:
        """ Get: SecureConversationAuthentication(self: ServiceCredentialsElement) -> SecureConversationServiceElement """
        ...

    @property
    def ServiceCertificate(self): # -> X509RecipientCertificateServiceElement
        """ Get: ServiceCertificate(self: ServiceCredentialsElement) -> X509RecipientCertificateServiceElement """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: ServiceCredentialsElement) -> str
        Set: Type(self: ServiceCredentialsElement) = value
        """
        ...

    @property
    def UseIdentityConfiguration(self) -> bool:
        """
        Get: UseIdentityConfiguration(self: ServiceCredentialsElement) -> bool
        Set: UseIdentityConfiguration(self: ServiceCredentialsElement) = value
        """
        ...

    @property
    def UserNameAuthentication(self): # -> UserNameServiceElement
        """ Get: UserNameAuthentication(self: ServiceCredentialsElement) -> UserNameServiceElement """
        ...

    @property
    def WindowsAuthentication(self): # -> WindowsServiceElement
        """ Get: WindowsAuthentication(self: ServiceCredentialsElement) -> WindowsServiceElement """
        ...


    def ApplyConfiguration(self, *args): #cannot find CLR method
        """ ApplyConfiguration(self: ServiceCredentialsElement, behavior: ServiceCredentials) """
        ...

    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: ServiceCredentialsElement, from: ServiceModelExtensionElement) """
        ...


class ServiceDebugElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ ServiceDebugElement() """
    @property
    def HttpHelpPageBinding(self) -> str:
        """
        Get: HttpHelpPageBinding(self: ServiceDebugElement) -> str
        Set: HttpHelpPageBinding(self: ServiceDebugElement) = value
        """
        ...

    @property
    def HttpHelpPageBindingConfiguration(self) -> str:
        """
        Get: HttpHelpPageBindingConfiguration(self: ServiceDebugElement) -> str
        Set: HttpHelpPageBindingConfiguration(self: ServiceDebugElement) = value
        """
        ...

    @property
    def HttpHelpPageEnabled(self) -> bool:
        """
        Get: HttpHelpPageEnabled(self: ServiceDebugElement) -> bool
        Set: HttpHelpPageEnabled(self: ServiceDebugElement) = value
        """
        ...

    @property
    def HttpHelpPageUrl(self) -> Uri:
        """
        Get: HttpHelpPageUrl(self: ServiceDebugElement) -> Uri
        Set: HttpHelpPageUrl(self: ServiceDebugElement) = value
        """
        ...

    @property
    def HttpsHelpPageBinding(self) -> str:
        """
        Get: HttpsHelpPageBinding(self: ServiceDebugElement) -> str
        Set: HttpsHelpPageBinding(self: ServiceDebugElement) = value
        """
        ...

    @property
    def HttpsHelpPageBindingConfiguration(self) -> str:
        """
        Get: HttpsHelpPageBindingConfiguration(self: ServiceDebugElement) -> str
        Set: HttpsHelpPageBindingConfiguration(self: ServiceDebugElement) = value
        """
        ...

    @property
    def HttpsHelpPageEnabled(self) -> bool:
        """
        Get: HttpsHelpPageEnabled(self: ServiceDebugElement) -> bool
        Set: HttpsHelpPageEnabled(self: ServiceDebugElement) = value
        """
        ...

    @property
    def HttpsHelpPageUrl(self) -> Uri:
        """
        Get: HttpsHelpPageUrl(self: ServiceDebugElement) -> Uri
        Set: HttpsHelpPageUrl(self: ServiceDebugElement) = value
        """
        ...

    @property
    def IncludeExceptionDetailInFaults(self) -> bool:
        """
        Get: IncludeExceptionDetailInFaults(self: ServiceDebugElement) -> bool
        Set: IncludeExceptionDetailInFaults(self: ServiceDebugElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: ServiceDebugElement, from: ServiceModelExtensionElement) """
        ...


class ServiceElement(IConfigurationContextProviderInternal, ConfigurationElement): # skipped bases: <type 'object'>
    """
    ServiceElement()
    ServiceElement(serviceName: str)
    """
    @property
    def BehaviorConfiguration(self) -> str:
        """
        Get: BehaviorConfiguration(self: ServiceElement) -> str
        Set: BehaviorConfiguration(self: ServiceElement) = value
        """
        ...

    @property
    def Endpoints(self): # -> ServiceEndpointElementCollection
        """ Get: Endpoints(self: ServiceElement) -> ServiceEndpointElementCollection """
        ...

    @property
    def Host(self) -> HostElement:
        """ Get: Host(self: ServiceElement) -> HostElement """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ServiceElement) -> str
        Set: Name(self: ServiceElement) = value
        """
        ...


    def __new__(cls, serviceName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, serviceName: str)
        """
        ...


class ServiceElementCollection(ServiceModelEnhancedConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ServiceElementCollection() """
    pass

class ServiceEndpointElement(IConfigurationContextProviderInternal, ConfigurationElement): # skipped bases: <type 'object'>
    """
    ServiceEndpointElement()
    ServiceEndpointElement(address: Uri, contractType: str)
    """
    @property
    def Address(self) -> Uri:
        """
        Get: Address(self: ServiceEndpointElement) -> Uri
        Set: Address(self: ServiceEndpointElement) = value
        """
        ...

    @property
    def BehaviorConfiguration(self) -> str:
        """
        Get: BehaviorConfiguration(self: ServiceEndpointElement) -> str
        Set: BehaviorConfiguration(self: ServiceEndpointElement) = value
        """
        ...

    @property
    def Binding(self) -> str:
        """
        Get: Binding(self: ServiceEndpointElement) -> str
        Set: Binding(self: ServiceEndpointElement) = value
        """
        ...

    @property
    def BindingConfiguration(self) -> str:
        """
        Get: BindingConfiguration(self: ServiceEndpointElement) -> str
        Set: BindingConfiguration(self: ServiceEndpointElement) = value
        """
        ...

    @property
    def BindingName(self) -> str:
        """
        Get: BindingName(self: ServiceEndpointElement) -> str
        Set: BindingName(self: ServiceEndpointElement) = value
        """
        ...

    @property
    def BindingNamespace(self) -> str:
        """
        Get: BindingNamespace(self: ServiceEndpointElement) -> str
        Set: BindingNamespace(self: ServiceEndpointElement) = value
        """
        ...

    @property
    def Contract(self) -> str:
        """
        Get: Contract(self: ServiceEndpointElement) -> str
        Set: Contract(self: ServiceEndpointElement) = value
        """
        ...

    @property
    def EndpointConfiguration(self) -> str:
        """
        Get: EndpointConfiguration(self: ServiceEndpointElement) -> str
        Set: EndpointConfiguration(self: ServiceEndpointElement) = value
        """
        ...

    @property
    def Headers(self) -> AddressHeaderCollectionElement:
        """ Get: Headers(self: ServiceEndpointElement) -> AddressHeaderCollectionElement """
        ...

    @property
    def Identity(self) -> IdentityElement:
        """ Get: Identity(self: ServiceEndpointElement) -> IdentityElement """
        ...

    @property
    def IsSystemEndpoint(self) -> bool:
        """
        Get: IsSystemEndpoint(self: ServiceEndpointElement) -> bool
        Set: IsSystemEndpoint(self: ServiceEndpointElement) = value
        """
        ...

    @property
    def Kind(self) -> str:
        """
        Get: Kind(self: ServiceEndpointElement) -> str
        Set: Kind(self: ServiceEndpointElement) = value
        """
        ...

    @property
    def ListenUri(self) -> Uri:
        """
        Get: ListenUri(self: ServiceEndpointElement) -> Uri
        Set: ListenUri(self: ServiceEndpointElement) = value
        """
        ...

    @property
    def ListenUriMode(self): # -> ListenUriMode
        """
        Get: ListenUriMode(self: ServiceEndpointElement) -> ListenUriMode
        Set: ListenUriMode(self: ServiceEndpointElement) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ServiceEndpointElement) -> str
        Set: Name(self: ServiceEndpointElement) = value
        """
        ...


    def __new__(cls, address:Uri = ..., contractType:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, address: Uri, contractType: str)
        """
        ...


class ServiceEndpointElementCollection(ServiceModelEnhancedConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ServiceEndpointElementCollection() """
    pass

class ServiceHealthElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ ServiceHealthElement() """
    @property
    def HealthDetailsEnabled(self) -> bool:
        """
        Get: HealthDetailsEnabled(self: ServiceHealthElement) -> bool
        Set: HealthDetailsEnabled(self: ServiceHealthElement) = value
        """
        ...

    @property
    def HttpGetBinding(self) -> str:
        """
        Get: HttpGetBinding(self: ServiceHealthElement) -> str
        Set: HttpGetBinding(self: ServiceHealthElement) = value
        """
        ...

    @property
    def HttpGetBindingConfiguration(self) -> str:
        """
        Get: HttpGetBindingConfiguration(self: ServiceHealthElement) -> str
        Set: HttpGetBindingConfiguration(self: ServiceHealthElement) = value
        """
        ...

    @property
    def HttpGetEnabled(self) -> bool:
        """
        Get: HttpGetEnabled(self: ServiceHealthElement) -> bool
        Set: HttpGetEnabled(self: ServiceHealthElement) = value
        """
        ...

    @property
    def HttpGetUrl(self) -> Uri:
        """
        Get: HttpGetUrl(self: ServiceHealthElement) -> Uri
        Set: HttpGetUrl(self: ServiceHealthElement) = value
        """
        ...

    @property
    def HttpsGetBinding(self) -> str:
        """
        Get: HttpsGetBinding(self: ServiceHealthElement) -> str
        Set: HttpsGetBinding(self: ServiceHealthElement) = value
        """
        ...

    @property
    def HttpsGetBindingConfiguration(self) -> str:
        """
        Get: HttpsGetBindingConfiguration(self: ServiceHealthElement) -> str
        Set: HttpsGetBindingConfiguration(self: ServiceHealthElement) = value
        """
        ...

    @property
    def HttpsGetEnabled(self) -> bool:
        """
        Get: HttpsGetEnabled(self: ServiceHealthElement) -> bool
        Set: HttpsGetEnabled(self: ServiceHealthElement) = value
        """
        ...

    @property
    def HttpsGetUrl(self) -> Uri:
        """
        Get: HttpsGetUrl(self: ServiceHealthElement) -> Uri
        Set: HttpsGetUrl(self: ServiceHealthElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: ServiceHealthElement, from: ServiceModelExtensionElement) """
        ...


class ServiceHostingEnvironmentSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ ServiceHostingEnvironmentSection() """
    @property
    def AspNetCompatibilityEnabled(self) -> bool:
        """
        Get: AspNetCompatibilityEnabled(self: ServiceHostingEnvironmentSection) -> bool
        Set: AspNetCompatibilityEnabled(self: ServiceHostingEnvironmentSection) = value
        """
        ...

    @property
    def BaseAddressPrefixFilters(self) -> BaseAddressPrefixFilterElementCollection:
        """ Get: BaseAddressPrefixFilters(self: ServiceHostingEnvironmentSection) -> BaseAddressPrefixFilterElementCollection """
        ...

    @property
    def CloseIdleServicesAtLowMemory(self) -> bool:
        """
        Get: CloseIdleServicesAtLowMemory(self: ServiceHostingEnvironmentSection) -> bool
        Set: CloseIdleServicesAtLowMemory(self: ServiceHostingEnvironmentSection) = value
        """
        ...

    @property
    def MinFreeMemoryPercentageToActivateService(self) -> int:
        """
        Get: MinFreeMemoryPercentageToActivateService(self: ServiceHostingEnvironmentSection) -> int
        Set: MinFreeMemoryPercentageToActivateService(self: ServiceHostingEnvironmentSection) = value
        """
        ...

    @property
    def MultipleSiteBindingsEnabled(self) -> bool:
        """
        Get: MultipleSiteBindingsEnabled(self: ServiceHostingEnvironmentSection) -> bool
        Set: MultipleSiteBindingsEnabled(self: ServiceHostingEnvironmentSection) = value
        """
        ...

    @property
    def ServiceActivations(self) -> ServiceActivationElementCollection:
        """ Get: ServiceActivations(self: ServiceHostingEnvironmentSection) -> ServiceActivationElementCollection """
        ...

    @property
    def TransportConfigurationTypes(self): # -> TransportConfigurationTypeElementCollection
        """ Get: TransportConfigurationTypes(self: ServiceHostingEnvironmentSection) -> TransportConfigurationTypeElementCollection """
        ...



class ServiceMetadataEndpointCollectionElement(StandardEndpointCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ ServiceMetadataEndpointCollectionElement() """
    pass

class StandardEndpointElement(IConfigurationContextProviderInternal, ConfigurationElement): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def EndpointType(self):
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: StandardEndpointElement) -> str
        Set: Name(self: StandardEndpointElement) = value
        """
        ...


    def ApplyConfiguration(self, endpoint, *__args:ChannelEndpointElement): # ->  # Not found arg types: {'endpoint': 'ServiceEndpoint'}
        """ ApplyConfiguration(self: StandardEndpointElement, endpoint: ServiceEndpoint, channelEndpointElement: ChannelEndpointElement)ApplyConfiguration(self: StandardEndpointElement, endpoint: ServiceEndpoint, serviceEndpointElement: ServiceEndpointElement) """
        ...

    def CreateServiceEndpoint(self, *args): #cannot find CLR method
        """ CreateServiceEndpoint(self: StandardEndpointElement, contractDescription: ContractDescription) -> ServiceEndpoint """
        ...

    def InitializeAndValidate(self, *__args:ChannelEndpointElement): # -> 
        """ InitializeAndValidate(self: StandardEndpointElement, channelEndpointElement: ChannelEndpointElement)InitializeAndValidate(self: StandardEndpointElement, serviceEndpointElement: ServiceEndpointElement) """
        ...

    def InitializeFrom(self, *args): #cannot find CLR method
        """ InitializeFrom(self: StandardEndpointElement, endpoint: ServiceEndpoint) """
        ...

    def OnApplyConfiguration(self, *args): #cannot find CLR method
        """ OnApplyConfiguration(self: StandardEndpointElement, endpoint: ServiceEndpoint, channelEndpointElement: ChannelEndpointElement)OnApplyConfiguration(self: StandardEndpointElement, endpoint: ServiceEndpoint, serviceEndpointElement: ServiceEndpointElement) """
        ...

    def OnInitializeAndValidate(self, *args): #cannot find CLR method
        """ OnInitializeAndValidate(self: StandardEndpointElement, channelEndpointElement: ChannelEndpointElement)OnInitializeAndValidate(self: StandardEndpointElement, serviceEndpointElement: ServiceEndpointElement) """
        ...


class ServiceMetadataEndpointElement(StandardEndpointElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ ServiceMetadataEndpointElement() """
    pass

class ServiceMetadataPublishingElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ ServiceMetadataPublishingElement() """
    @property
    def ExternalMetadataLocation(self) -> Uri:
        """
        Get: ExternalMetadataLocation(self: ServiceMetadataPublishingElement) -> Uri
        Set: ExternalMetadataLocation(self: ServiceMetadataPublishingElement) = value
        """
        ...

    @property
    def HttpGetBinding(self) -> str:
        """
        Get: HttpGetBinding(self: ServiceMetadataPublishingElement) -> str
        Set: HttpGetBinding(self: ServiceMetadataPublishingElement) = value
        """
        ...

    @property
    def HttpGetBindingConfiguration(self) -> str:
        """
        Get: HttpGetBindingConfiguration(self: ServiceMetadataPublishingElement) -> str
        Set: HttpGetBindingConfiguration(self: ServiceMetadataPublishingElement) = value
        """
        ...

    @property
    def HttpGetEnabled(self) -> bool:
        """
        Get: HttpGetEnabled(self: ServiceMetadataPublishingElement) -> bool
        Set: HttpGetEnabled(self: ServiceMetadataPublishingElement) = value
        """
        ...

    @property
    def HttpGetUrl(self) -> Uri:
        """
        Get: HttpGetUrl(self: ServiceMetadataPublishingElement) -> Uri
        Set: HttpGetUrl(self: ServiceMetadataPublishingElement) = value
        """
        ...

    @property
    def HttpsGetBinding(self) -> str:
        """
        Get: HttpsGetBinding(self: ServiceMetadataPublishingElement) -> str
        Set: HttpsGetBinding(self: ServiceMetadataPublishingElement) = value
        """
        ...

    @property
    def HttpsGetBindingConfiguration(self) -> str:
        """
        Get: HttpsGetBindingConfiguration(self: ServiceMetadataPublishingElement) -> str
        Set: HttpsGetBindingConfiguration(self: ServiceMetadataPublishingElement) = value
        """
        ...

    @property
    def HttpsGetEnabled(self) -> bool:
        """
        Get: HttpsGetEnabled(self: ServiceMetadataPublishingElement) -> bool
        Set: HttpsGetEnabled(self: ServiceMetadataPublishingElement) = value
        """
        ...

    @property
    def HttpsGetUrl(self) -> Uri:
        """
        Get: HttpsGetUrl(self: ServiceMetadataPublishingElement) -> Uri
        Set: HttpsGetUrl(self: ServiceMetadataPublishingElement) = value
        """
        ...

    @property
    def PolicyVersion(self): # -> PolicyVersion
        """
        Get: PolicyVersion(self: ServiceMetadataPublishingElement) -> PolicyVersion
        Set: PolicyVersion(self: ServiceMetadataPublishingElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: ServiceMetadataPublishingElement, from: ServiceModelExtensionElement) """
        ...


class ServiceModelConfigurationElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Add(self, element): # ->  # Not found arg types: {'element': 'ConfigurationElementType'}
        """ Add(self: ServiceModelConfigurationElementCollection[ConfigurationElementType], element: ConfigurationElementType) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ServiceModelConfigurationElementCollection[ConfigurationElementType]) """
        ...

    def ContainsKey(self, key:object) -> bool:
        """ ContainsKey(self: ServiceModelConfigurationElementCollection[ConfigurationElementType], key: object) -> bool """
        ...

    def IndexOf(self, element) -> int: # Not found arg types: {'element': 'ConfigurationElementType'}
        """ IndexOf(self: ServiceModelConfigurationElementCollection[ConfigurationElementType], element: ConfigurationElementType) -> int """
        ...

    def Remove(self, element): # ->  # Not found arg types: {'element': 'ConfigurationElementType'}
        """ Remove(self: ServiceModelConfigurationElementCollection[ConfigurationElementType], element: ConfigurationElementType) """
        ...

    def RemoveAt(self, *__args:object): # -> 
        """ RemoveAt(self: ServiceModelConfigurationElementCollection[ConfigurationElementType], key: object)RemoveAt(self: ServiceModelConfigurationElementCollection[ConfigurationElementType], index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        ...


class ServiceModelEnhancedConfigurationElementCollection(ServiceModelConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class ServiceModelExtensionCollectionElement(IConfigurationContextProviderInternal, ConfigurationElement, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[TServiceModelExtensionElement]'>, <type 'object'>
    """ no doc """
    def CanAdd(self, element) -> bool: # Not found arg types: {'element': 'TServiceModelExtensionElement'}
        """ CanAdd(self: ServiceModelExtensionCollectionElement[TServiceModelExtensionElement], element: TServiceModelExtensionElement) -> bool """
        ...

    def ContainsKey(self, *__args:Type) -> bool:
        """
        ContainsKey(self: ServiceModelExtensionCollectionElement[TServiceModelExtensionElement], elementType: Type) -> bool
        ContainsKey(self: ServiceModelExtensionCollectionElement[TServiceModelExtensionElement], elementName: str) -> bool
        """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ServiceModelExtensionCollectionElement[TServiceModelExtensionElement]) -> IEnumerator[TServiceModelExtensionElement] """
        ...

    def SetIsModified(self, *args): #cannot find CLR method
        """ SetIsModified(self: ServiceModelExtensionCollectionElement[TServiceModelExtensionElement]) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class ServiceModelSectionGroup(ConfigurationSectionGroup): # skipped bases: <type 'object'>
    """ ServiceModelSectionGroup() """
    @property
    def Behaviors(self) -> BehaviorsSection:
        """ Get: Behaviors(self: ServiceModelSectionGroup) -> BehaviorsSection """
        ...

    @property
    def Bindings(self) -> BindingsSection:
        """ Get: Bindings(self: ServiceModelSectionGroup) -> BindingsSection """
        ...

    @property
    def Client(self) -> ClientSection:
        """ Get: Client(self: ServiceModelSectionGroup) -> ClientSection """
        ...

    @property
    def ComContracts(self) -> ComContractsSection:
        """ Get: ComContracts(self: ServiceModelSectionGroup) -> ComContractsSection """
        ...

    @property
    def CommonBehaviors(self) -> CommonBehaviorsSection:
        """ Get: CommonBehaviors(self: ServiceModelSectionGroup) -> CommonBehaviorsSection """
        ...

    @property
    def Diagnostic(self) -> DiagnosticSection:
        """ Get: Diagnostic(self: ServiceModelSectionGroup) -> DiagnosticSection """
        ...

    @property
    def Extensions(self) -> ExtensionsSection:
        """ Get: Extensions(self: ServiceModelSectionGroup) -> ExtensionsSection """
        ...

    @property
    def ProtocolMapping(self) -> ProtocolMappingSection:
        """ Get: ProtocolMapping(self: ServiceModelSectionGroup) -> ProtocolMappingSection """
        ...

    @property
    def ServiceHostingEnvironment(self) -> ServiceHostingEnvironmentSection:
        """ Get: ServiceHostingEnvironment(self: ServiceModelSectionGroup) -> ServiceHostingEnvironmentSection """
        ...

    @property
    def Services(self): # -> ServicesSection
        """ Get: Services(self: ServiceModelSectionGroup) -> ServicesSection """
        ...

    @property
    def StandardEndpoints(self): # -> StandardEndpointsSection
        """ Get: StandardEndpoints(self: ServiceModelSectionGroup) -> StandardEndpointsSection """
        ...


    @staticmethod
    def GetSectionGroup(config:Configuration) -> ServiceModelSectionGroup:
        """ GetSectionGroup(config: Configuration) -> ServiceModelSectionGroup """
        ...


class ServicePrincipalNameElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ ServicePrincipalNameElement() """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: ServicePrincipalNameElement) -> str
        Set: Value(self: ServicePrincipalNameElement) = value
        """
        ...



class ServiceSecurityAuditElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ ServiceSecurityAuditElement() """
    @property
    def AuditLogLocation(self) -> AuditLogLocation:
        """
        Get: AuditLogLocation(self: ServiceSecurityAuditElement) -> AuditLogLocation
        Set: AuditLogLocation(self: ServiceSecurityAuditElement) = value
        """
        ...

    @property
    def MessageAuthenticationAuditLevel(self) -> AuditLevel:
        """
        Get: MessageAuthenticationAuditLevel(self: ServiceSecurityAuditElement) -> AuditLevel
        Set: MessageAuthenticationAuditLevel(self: ServiceSecurityAuditElement) = value
        """
        ...

    @property
    def ServiceAuthorizationAuditLevel(self) -> AuditLevel:
        """
        Get: ServiceAuthorizationAuditLevel(self: ServiceSecurityAuditElement) -> AuditLevel
        Set: ServiceAuthorizationAuditLevel(self: ServiceSecurityAuditElement) = value
        """
        ...

    @property
    def SuppressAuditFailure(self) -> bool:
        """
        Get: SuppressAuditFailure(self: ServiceSecurityAuditElement) -> bool
        Set: SuppressAuditFailure(self: ServiceSecurityAuditElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: ServiceSecurityAuditElement, from: ServiceModelExtensionElement) """
        ...


class ServicesSection(IConfigurationContextProviderInternal, ConfigurationSection): # skipped bases: <type 'object'>
    """ ServicesSection() """
    @property
    def Services(self) -> ServiceElementCollection:
        """ Get: Services(self: ServicesSection) -> ServiceElementCollection """
        ...



class ServiceThrottlingElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ ServiceThrottlingElement() """
    @property
    def MaxConcurrentCalls(self) -> int:
        """
        Get: MaxConcurrentCalls(self: ServiceThrottlingElement) -> int
        Set: MaxConcurrentCalls(self: ServiceThrottlingElement) = value
        """
        ...

    @property
    def MaxConcurrentInstances(self) -> int:
        """
        Get: MaxConcurrentInstances(self: ServiceThrottlingElement) -> int
        Set: MaxConcurrentInstances(self: ServiceThrottlingElement) = value
        """
        ...

    @property
    def MaxConcurrentSessions(self) -> int:
        """
        Get: MaxConcurrentSessions(self: ServiceThrottlingElement) -> int
        Set: MaxConcurrentSessions(self: ServiceThrottlingElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: ServiceThrottlingElement, from: ServiceModelExtensionElement) """
        ...


class ServiceTimeoutsElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ ServiceTimeoutsElement() """
    @property
    def TransactionTimeout(self) -> TimeSpan:
        """
        Get: TransactionTimeout(self: ServiceTimeoutsElement) -> TimeSpan
        Set: TransactionTimeout(self: ServiceTimeoutsElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: ServiceTimeoutsElement, from: ServiceModelExtensionElement) """
        ...


class SslStreamSecurityElement(BindingElementExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ SslStreamSecurityElement() """
    @property
    def RequireClientCertificate(self) -> bool:
        """
        Get: RequireClientCertificate(self: SslStreamSecurityElement) -> bool
        Set: RequireClientCertificate(self: SslStreamSecurityElement) = value
        """
        ...

    @property
    def SslProtocols(self) -> SslProtocols:
        """ Get: SslProtocols(self: SslStreamSecurityElement) -> SslProtocols """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: SslStreamSecurityElement, from: ServiceModelExtensionElement) """
        ...


class StandardBindingCollectionElement(BindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ StandardBindingCollectionElement[TStandardBinding, TBindingConfiguration]() """
    @property
    def Bindings(self): # -> StandardBindingElementCollection
        """ Get: Bindings(self: StandardBindingCollectionElement[TStandardBinding, TBindingConfiguration]) -> StandardBindingElementCollection[TBindingConfiguration] """
        ...



class StandardBindingElementCollection(ServiceModelEnhancedConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ StandardBindingElementCollection[TBindingConfiguration]() """
    pass

class StandardBindingReliableSessionElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ StandardBindingReliableSessionElement() """
    @property
    def InactivityTimeout(self) -> TimeSpan:
        """
        Get: InactivityTimeout(self: StandardBindingReliableSessionElement) -> TimeSpan
        Set: InactivityTimeout(self: StandardBindingReliableSessionElement) = value
        """
        ...

    @property
    def Ordered(self) -> bool:
        """
        Get: Ordered(self: StandardBindingReliableSessionElement) -> bool
        Set: Ordered(self: StandardBindingReliableSessionElement) = value
        """
        ...


    def ApplyConfiguration(self, reliableSession:ReliableSession): # -> 
        """ ApplyConfiguration(self: StandardBindingReliableSessionElement, reliableSession: ReliableSession) """
        ...

    def InitializeFrom(self, reliableSession:ReliableSession): # -> 
        """ InitializeFrom(self: StandardBindingReliableSessionElement, reliableSession: ReliableSession) """
        ...


class StandardBindingOptionalReliableSessionElement(StandardBindingReliableSessionElement): # skipped bases: <type 'object'>
    """ StandardBindingOptionalReliableSessionElement() """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: StandardBindingOptionalReliableSessionElement) -> bool
        Set: Enabled(self: StandardBindingOptionalReliableSessionElement) = value
        """
        ...



class StandardEndpointCollectionElement(EndpointCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ StandardEndpointCollectionElement[TStandardEndpoint, TEndpointConfiguration]() """
    @property
    def Endpoints(self): # -> StandardEndpointElementCollection
        """ Get: Endpoints(self: StandardEndpointCollectionElement[TStandardEndpoint, TEndpointConfiguration]) -> StandardEndpointElementCollection[TEndpointConfiguration] """
        ...



class StandardEndpointElementCollection(ServiceModelEnhancedConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ StandardEndpointElementCollection[TEndpointConfiguration]() """
    pass

class StandardEndpointsSection(IConfigurationContextProviderInternal, ConfigurationSection): # skipped bases: <type 'object'>
    """ StandardEndpointsSection() """
    @property
    def EndpointCollections(self) -> List:
        """ Get: EndpointCollections(self: StandardEndpointsSection) -> List[EndpointCollectionElement] """
        ...

    @property
    def MexEndpoint(self) -> ServiceMetadataEndpointCollectionElement:
        """ Get: MexEndpoint(self: StandardEndpointsSection) -> ServiceMetadataEndpointCollectionElement """
        ...


    @staticmethod
    def GetSection(config:Configuration) -> StandardEndpointsSection:
        """ GetSection(config: Configuration) -> StandardEndpointsSection """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class SynchronousReceiveElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ SynchronousReceiveElement() """
    pass

class TcpConnectionPoolSettingsElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ TcpConnectionPoolSettingsElement() """
    @property
    def GroupName(self) -> str:
        """
        Get: GroupName(self: TcpConnectionPoolSettingsElement) -> str
        Set: GroupName(self: TcpConnectionPoolSettingsElement) = value
        """
        ...

    @property
    def IdleTimeout(self) -> TimeSpan:
        """
        Get: IdleTimeout(self: TcpConnectionPoolSettingsElement) -> TimeSpan
        Set: IdleTimeout(self: TcpConnectionPoolSettingsElement) = value
        """
        ...

    @property
    def LeaseTimeout(self) -> TimeSpan:
        """
        Get: LeaseTimeout(self: TcpConnectionPoolSettingsElement) -> TimeSpan
        Set: LeaseTimeout(self: TcpConnectionPoolSettingsElement) = value
        """
        ...

    @property
    def MaxOutboundConnectionsPerEndpoint(self) -> int:
        """
        Get: MaxOutboundConnectionsPerEndpoint(self: TcpConnectionPoolSettingsElement) -> int
        Set: MaxOutboundConnectionsPerEndpoint(self: TcpConnectionPoolSettingsElement) = value
        """
        ...



class TcpTransportElement(ConnectionOrientedTransportElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ TcpTransportElement() """
    @property
    def BindingElementType(self) -> Type:
        """ Get: BindingElementType(self: TcpTransportElement) -> Type """
        ...

    @property
    def ConnectionPoolSettings(self) -> TcpConnectionPoolSettingsElement:
        """
        Get: ConnectionPoolSettings(self: TcpTransportElement) -> TcpConnectionPoolSettingsElement
        Set: ConnectionPoolSettings(self: TcpTransportElement) = value
        """
        ...

    @property
    def ExtendedProtectionPolicy(self) -> ExtendedProtectionPolicyElement:
        """ Get: ExtendedProtectionPolicy(self: TcpTransportElement) -> ExtendedProtectionPolicyElement """
        ...

    @property
    def ListenBacklog(self) -> int:
        """
        Get: ListenBacklog(self: TcpTransportElement) -> int
        Set: ListenBacklog(self: TcpTransportElement) = value
        """
        ...

    @property
    def PortSharingEnabled(self) -> bool:
        """
        Get: PortSharingEnabled(self: TcpTransportElement) -> bool
        Set: PortSharingEnabled(self: TcpTransportElement) = value
        """
        ...

    @property
    def TeredoEnabled(self) -> bool:
        """
        Get: TeredoEnabled(self: TcpTransportElement) -> bool
        Set: TeredoEnabled(self: TcpTransportElement) = value
        """
        ...



class TcpTransportSecurityElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ TcpTransportSecurityElement() """
    @property
    def ClientCredentialType(self) -> TcpClientCredentialType:
        """
        Get: ClientCredentialType(self: TcpTransportSecurityElement) -> TcpClientCredentialType
        Set: ClientCredentialType(self: TcpTransportSecurityElement) = value
        """
        ...

    @property
    def ExtendedProtectionPolicy(self) -> ExtendedProtectionPolicyElement:
        """ Get: ExtendedProtectionPolicy(self: TcpTransportSecurityElement) -> ExtendedProtectionPolicyElement """
        ...

    @property
    def ProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ProtectionLevel(self: TcpTransportSecurityElement) -> ProtectionLevel
        Set: ProtectionLevel(self: TcpTransportSecurityElement) = value
        """
        ...

    @property
    def SslProtocols(self) -> SslProtocols:
        """ Get: SslProtocols(self: TcpTransportSecurityElement) -> SslProtocols """
        ...



class TextMessageEncodingElement(BindingElementExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ TextMessageEncodingElement() """
    @property
    def MaxReadPoolSize(self) -> int:
        """
        Get: MaxReadPoolSize(self: TextMessageEncodingElement) -> int
        Set: MaxReadPoolSize(self: TextMessageEncodingElement) = value
        """
        ...

    @property
    def MaxWritePoolSize(self) -> int:
        """
        Get: MaxWritePoolSize(self: TextMessageEncodingElement) -> int
        Set: MaxWritePoolSize(self: TextMessageEncodingElement) = value
        """
        ...

    @property
    def MessageVersion(self): # -> MessageVersion
        """
        Get: MessageVersion(self: TextMessageEncodingElement) -> MessageVersion
        Set: MessageVersion(self: TextMessageEncodingElement) = value
        """
        ...

    @property
    def ReaderQuotas(self): # -> XmlDictionaryReaderQuotasElement
        """ Get: ReaderQuotas(self: TextMessageEncodingElement) -> XmlDictionaryReaderQuotasElement """
        ...

    @property
    def WriteEncoding(self) -> Encoding:
        """
        Get: WriteEncoding(self: TextMessageEncodingElement) -> Encoding
        Set: WriteEncoding(self: TextMessageEncodingElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: TextMessageEncodingElement, from: ServiceModelExtensionElement) """
        ...


class TransactedBatchingElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ TransactedBatchingElement() """
    @property
    def MaxBatchSize(self) -> int:
        """
        Get: MaxBatchSize(self: TransactedBatchingElement) -> int
        Set: MaxBatchSize(self: TransactedBatchingElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: TransactedBatchingElement, from: ServiceModelExtensionElement) """
        ...


class TransactionFlowElement(BindingElementExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ TransactionFlowElement() """
    @property
    def AllowWildcardAction(self) -> bool:
        """
        Get: AllowWildcardAction(self: TransactionFlowElement) -> bool
        Set: AllowWildcardAction(self: TransactionFlowElement) = value
        """
        ...

    @property
    def TransactionProtocol(self) -> TransactionProtocol:
        """
        Get: TransactionProtocol(self: TransactionFlowElement) -> TransactionProtocol
        Set: TransactionProtocol(self: TransactionFlowElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: TransactionFlowElement, from: ServiceModelExtensionElement) """
        ...


class TransportConfigurationTypeElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    TransportConfigurationTypeElement()
    TransportConfigurationTypeElement(name: str)
    TransportConfigurationTypeElement(name: str, transportConfigurationTypeName: str)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: TransportConfigurationTypeElement) -> str
        Set: Name(self: TransportConfigurationTypeElement) = value
        """
        ...

    @property
    def TransportConfigurationType(self) -> str:
        """
        Get: TransportConfigurationType(self: TransportConfigurationTypeElement) -> str
        Set: TransportConfigurationType(self: TransportConfigurationTypeElement) = value
        """
        ...


    def __new__(cls, name:str = ..., transportConfigurationTypeName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, transportConfigurationTypeName: str)
        """
        ...


class TransportConfigurationTypeElementCollection(ServiceModelConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ TransportConfigurationTypeElementCollection() """
    pass

class UdpBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ UdpBindingCollectionElement() """
    pass

class UdpBindingElement(StandardBindingElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    UdpBindingElement(name: str)
    UdpBindingElement()
    """
    @property
    def DuplicateMessageHistoryLength(self) -> int:
        """
        Get: DuplicateMessageHistoryLength(self: UdpBindingElement) -> int
        Set: DuplicateMessageHistoryLength(self: UdpBindingElement) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: UdpBindingElement) -> Int64
        Set: MaxBufferPoolSize(self: UdpBindingElement) = value
        """
        ...

    @property
    def MaxPendingMessagesTotalSize(self) -> Int64:
        """
        Get: MaxPendingMessagesTotalSize(self: UdpBindingElement) -> Int64
        Set: MaxPendingMessagesTotalSize(self: UdpBindingElement) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: UdpBindingElement) -> Int64
        Set: MaxReceivedMessageSize(self: UdpBindingElement) = value
        """
        ...

    @property
    def MaxRetransmitCount(self) -> int:
        """
        Get: MaxRetransmitCount(self: UdpBindingElement) -> int
        Set: MaxRetransmitCount(self: UdpBindingElement) = value
        """
        ...

    @property
    def MulticastInterfaceId(self) -> str:
        """
        Get: MulticastInterfaceId(self: UdpBindingElement) -> str
        Set: MulticastInterfaceId(self: UdpBindingElement) = value
        """
        ...

    @property
    def ReaderQuotas(self): # -> XmlDictionaryReaderQuotasElement
        """ Get: ReaderQuotas(self: UdpBindingElement) -> XmlDictionaryReaderQuotasElement """
        ...

    @property
    def TextEncoding(self) -> Encoding:
        """
        Get: TextEncoding(self: UdpBindingElement) -> Encoding
        Set: TextEncoding(self: UdpBindingElement) = value
        """
        ...

    @property
    def TimeToLive(self) -> int:
        """
        Get: TimeToLive(self: UdpBindingElement) -> int
        Set: TimeToLive(self: UdpBindingElement) = value
        """
        ...



class UdpRetransmissionSettingsElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ UdpRetransmissionSettingsElement() """
    @property
    def DelayLowerBound(self) -> TimeSpan:
        """
        Get: DelayLowerBound(self: UdpRetransmissionSettingsElement) -> TimeSpan
        Set: DelayLowerBound(self: UdpRetransmissionSettingsElement) = value
        """
        ...

    @property
    def DelayUpperBound(self) -> TimeSpan:
        """
        Get: DelayUpperBound(self: UdpRetransmissionSettingsElement) -> TimeSpan
        Set: DelayUpperBound(self: UdpRetransmissionSettingsElement) = value
        """
        ...

    @property
    def MaxDelayPerRetransmission(self) -> TimeSpan:
        """
        Get: MaxDelayPerRetransmission(self: UdpRetransmissionSettingsElement) -> TimeSpan
        Set: MaxDelayPerRetransmission(self: UdpRetransmissionSettingsElement) = value
        """
        ...

    @property
    def MaxMulticastRetransmitCount(self) -> int:
        """
        Get: MaxMulticastRetransmitCount(self: UdpRetransmissionSettingsElement) -> int
        Set: MaxMulticastRetransmitCount(self: UdpRetransmissionSettingsElement) = value
        """
        ...

    @property
    def MaxUnicastRetransmitCount(self) -> int:
        """
        Get: MaxUnicastRetransmitCount(self: UdpRetransmissionSettingsElement) -> int
        Set: MaxUnicastRetransmitCount(self: UdpRetransmissionSettingsElement) = value
        """
        ...



class UdpTransportElement(TransportElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ UdpTransportElement() """
    @property
    def BindingElementType(self) -> Type:
        """ Get: BindingElementType(self: UdpTransportElement) -> Type """
        ...

    @property
    def DuplicateMessageHistoryLength(self) -> int:
        """
        Get: DuplicateMessageHistoryLength(self: UdpTransportElement) -> int
        Set: DuplicateMessageHistoryLength(self: UdpTransportElement) = value
        """
        ...

    @property
    def MaxPendingMessagesTotalSize(self) -> Int64:
        """
        Get: MaxPendingMessagesTotalSize(self: UdpTransportElement) -> Int64
        Set: MaxPendingMessagesTotalSize(self: UdpTransportElement) = value
        """
        ...

    @property
    def MulticastInterfaceId(self) -> str:
        """
        Get: MulticastInterfaceId(self: UdpTransportElement) -> str
        Set: MulticastInterfaceId(self: UdpTransportElement) = value
        """
        ...

    @property
    def RetransmissionSettings(self) -> UdpRetransmissionSettingsElement:
        """
        Get: RetransmissionSettings(self: UdpTransportElement) -> UdpRetransmissionSettingsElement
        Set: RetransmissionSettings(self: UdpTransportElement) = value
        """
        ...

    @property
    def SocketReceiveBufferSize(self) -> int:
        """
        Get: SocketReceiveBufferSize(self: UdpTransportElement) -> int
        Set: SocketReceiveBufferSize(self: UdpTransportElement) = value
        """
        ...

    @property
    def TimeToLive(self) -> int:
        """
        Get: TimeToLive(self: UdpTransportElement) -> int
        Set: TimeToLive(self: UdpTransportElement) = value
        """
        ...



class UseManagedPresentationElement(BindingElementExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ UseManagedPresentationElement() """
    pass

class UseRequestHeadersForMetadataAddressElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ UseRequestHeadersForMetadataAddressElement() """
    @property
    def DefaultPorts(self) -> DefaultPortElementCollection:
        """ Get: DefaultPorts(self: UseRequestHeadersForMetadataAddressElement) -> DefaultPortElementCollection """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: UseRequestHeadersForMetadataAddressElement, from: ServiceModelExtensionElement) """
        ...


class UserNameServiceElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ UserNameServiceElement() """
    @property
    def CachedLogonTokenLifetime(self) -> TimeSpan:
        """
        Get: CachedLogonTokenLifetime(self: UserNameServiceElement) -> TimeSpan
        Set: CachedLogonTokenLifetime(self: UserNameServiceElement) = value
        """
        ...

    @property
    def CacheLogonTokens(self) -> bool:
        """
        Get: CacheLogonTokens(self: UserNameServiceElement) -> bool
        Set: CacheLogonTokens(self: UserNameServiceElement) = value
        """
        ...

    @property
    def CustomUserNamePasswordValidatorType(self) -> str:
        """
        Get: CustomUserNamePasswordValidatorType(self: UserNameServiceElement) -> str
        Set: CustomUserNamePasswordValidatorType(self: UserNameServiceElement) = value
        """
        ...

    @property
    def IncludeWindowsGroups(self) -> bool:
        """
        Get: IncludeWindowsGroups(self: UserNameServiceElement) -> bool
        Set: IncludeWindowsGroups(self: UserNameServiceElement) = value
        """
        ...

    @property
    def MaxCachedLogonTokens(self) -> int:
        """
        Get: MaxCachedLogonTokens(self: UserNameServiceElement) -> int
        Set: MaxCachedLogonTokens(self: UserNameServiceElement) = value
        """
        ...

    @property
    def MembershipProviderName(self) -> str:
        """
        Get: MembershipProviderName(self: UserNameServiceElement) -> str
        Set: MembershipProviderName(self: UserNameServiceElement) = value
        """
        ...

    @property
    def UserNamePasswordValidationMode(self) -> UserNamePasswordValidationMode:
        """
        Get: UserNamePasswordValidationMode(self: UserNameServiceElement) -> UserNamePasswordValidationMode
        Set: UserNamePasswordValidationMode(self: UserNameServiceElement) = value
        """
        ...


    def Copy(self, from_:UserNameServiceElement): # -> 
        """ Copy(self: UserNameServiceElement, from: UserNameServiceElement) """
        ...


class UserPrincipalNameElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ UserPrincipalNameElement() """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: UserPrincipalNameElement) -> str
        Set: Value(self: UserPrincipalNameElement) = value
        """
        ...



class WebHttpBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WebHttpBindingCollectionElement() """
    pass

class WebHttpBindingElement(StandardBindingElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    WebHttpBindingElement(name: str)
    WebHttpBindingElement()
    """
    @property
    def AllowCookies(self) -> bool:
        """
        Get: AllowCookies(self: WebHttpBindingElement) -> bool
        Set: AllowCookies(self: WebHttpBindingElement) = value
        """
        ...

    @property
    def BypassProxyOnLocal(self) -> bool:
        """
        Get: BypassProxyOnLocal(self: WebHttpBindingElement) -> bool
        Set: BypassProxyOnLocal(self: WebHttpBindingElement) = value
        """
        ...

    @property
    def ContentTypeMapper(self) -> str:
        """
        Get: ContentTypeMapper(self: WebHttpBindingElement) -> str
        Set: ContentTypeMapper(self: WebHttpBindingElement) = value
        """
        ...

    @property
    def CrossDomainScriptAccessEnabled(self) -> bool:
        """
        Get: CrossDomainScriptAccessEnabled(self: WebHttpBindingElement) -> bool
        Set: CrossDomainScriptAccessEnabled(self: WebHttpBindingElement) = value
        """
        ...

    @property
    def HostNameComparisonMode(self) -> HostNameComparisonMode:
        """
        Get: HostNameComparisonMode(self: WebHttpBindingElement) -> HostNameComparisonMode
        Set: HostNameComparisonMode(self: WebHttpBindingElement) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: WebHttpBindingElement) -> Int64
        Set: MaxBufferPoolSize(self: WebHttpBindingElement) = value
        """
        ...

    @property
    def MaxBufferSize(self) -> int:
        """
        Get: MaxBufferSize(self: WebHttpBindingElement) -> int
        Set: MaxBufferSize(self: WebHttpBindingElement) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: WebHttpBindingElement) -> Int64
        Set: MaxReceivedMessageSize(self: WebHttpBindingElement) = value
        """
        ...

    @property
    def ProxyAddress(self) -> Uri:
        """
        Get: ProxyAddress(self: WebHttpBindingElement) -> Uri
        Set: ProxyAddress(self: WebHttpBindingElement) = value
        """
        ...

    @property
    def ReaderQuotas(self): # -> XmlDictionaryReaderQuotasElement
        """ Get: ReaderQuotas(self: WebHttpBindingElement) -> XmlDictionaryReaderQuotasElement """
        ...

    @property
    def Security(self): # -> WebHttpSecurityElement
        """ Get: Security(self: WebHttpBindingElement) -> WebHttpSecurityElement """
        ...

    @property
    def TransferMode(self) -> TransferMode:
        """
        Get: TransferMode(self: WebHttpBindingElement) -> TransferMode
        Set: TransferMode(self: WebHttpBindingElement) = value
        """
        ...

    @property
    def UseDefaultWebProxy(self) -> bool:
        """
        Get: UseDefaultWebProxy(self: WebHttpBindingElement) -> bool
        Set: UseDefaultWebProxy(self: WebHttpBindingElement) = value
        """
        ...

    @property
    def WriteEncoding(self) -> Encoding:
        """
        Get: WriteEncoding(self: WebHttpBindingElement) -> Encoding
        Set: WriteEncoding(self: WebHttpBindingElement) = value
        """
        ...



class WebHttpElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WebHttpElement() """
    @property
    def AutomaticFormatSelectionEnabled(self) -> bool:
        """
        Get: AutomaticFormatSelectionEnabled(self: WebHttpElement) -> bool
        Set: AutomaticFormatSelectionEnabled(self: WebHttpElement) = value
        """
        ...

    @property
    def DefaultBodyStyle(self) -> WebMessageBodyStyle:
        """
        Get: DefaultBodyStyle(self: WebHttpElement) -> WebMessageBodyStyle
        Set: DefaultBodyStyle(self: WebHttpElement) = value
        """
        ...

    @property
    def DefaultOutgoingResponseFormat(self) -> WebMessageFormat:
        """
        Get: DefaultOutgoingResponseFormat(self: WebHttpElement) -> WebMessageFormat
        Set: DefaultOutgoingResponseFormat(self: WebHttpElement) = value
        """
        ...

    @property
    def FaultExceptionEnabled(self) -> bool:
        """
        Get: FaultExceptionEnabled(self: WebHttpElement) -> bool
        Set: FaultExceptionEnabled(self: WebHttpElement) = value
        """
        ...

    @property
    def HelpEnabled(self) -> bool:
        """
        Get: HelpEnabled(self: WebHttpElement) -> bool
        Set: HelpEnabled(self: WebHttpElement) = value
        """
        ...



class WebHttpEndpointCollectionElement(StandardEndpointCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WebHttpEndpointCollectionElement() """
    pass

class WebHttpEndpointElement(StandardEndpointElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WebHttpEndpointElement() """
    @property
    def AutomaticFormatSelectionEnabled(self) -> bool:
        """
        Get: AutomaticFormatSelectionEnabled(self: WebHttpEndpointElement) -> bool
        Set: AutomaticFormatSelectionEnabled(self: WebHttpEndpointElement) = value
        """
        ...

    @property
    def ContentTypeMapper(self) -> str:
        """
        Get: ContentTypeMapper(self: WebHttpEndpointElement) -> str
        Set: ContentTypeMapper(self: WebHttpEndpointElement) = value
        """
        ...

    @property
    def CrossDomainScriptAccessEnabled(self) -> bool:
        """
        Get: CrossDomainScriptAccessEnabled(self: WebHttpEndpointElement) -> bool
        Set: CrossDomainScriptAccessEnabled(self: WebHttpEndpointElement) = value
        """
        ...

    @property
    def DefaultOutgoingResponseFormat(self) -> WebMessageFormat:
        """
        Get: DefaultOutgoingResponseFormat(self: WebHttpEndpointElement) -> WebMessageFormat
        Set: DefaultOutgoingResponseFormat(self: WebHttpEndpointElement) = value
        """
        ...

    @property
    def FaultExceptionEnabled(self) -> bool:
        """
        Get: FaultExceptionEnabled(self: WebHttpEndpointElement) -> bool
        Set: FaultExceptionEnabled(self: WebHttpEndpointElement) = value
        """
        ...

    @property
    def HelpEnabled(self) -> bool:
        """
        Get: HelpEnabled(self: WebHttpEndpointElement) -> bool
        Set: HelpEnabled(self: WebHttpEndpointElement) = value
        """
        ...

    @property
    def HostNameComparisonMode(self) -> HostNameComparisonMode:
        """
        Get: HostNameComparisonMode(self: WebHttpEndpointElement) -> HostNameComparisonMode
        Set: HostNameComparisonMode(self: WebHttpEndpointElement) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: WebHttpEndpointElement) -> Int64
        Set: MaxBufferPoolSize(self: WebHttpEndpointElement) = value
        """
        ...

    @property
    def MaxBufferSize(self) -> int:
        """
        Get: MaxBufferSize(self: WebHttpEndpointElement) -> int
        Set: MaxBufferSize(self: WebHttpEndpointElement) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: WebHttpEndpointElement) -> Int64
        Set: MaxReceivedMessageSize(self: WebHttpEndpointElement) = value
        """
        ...

    @property
    def ReaderQuotas(self): # -> XmlDictionaryReaderQuotasElement
        """ Get: ReaderQuotas(self: WebHttpEndpointElement) -> XmlDictionaryReaderQuotasElement """
        ...

    @property
    def Security(self): # -> WebHttpSecurityElement
        """ Get: Security(self: WebHttpEndpointElement) -> WebHttpSecurityElement """
        ...

    @property
    def TransferMode(self) -> TransferMode:
        """
        Get: TransferMode(self: WebHttpEndpointElement) -> TransferMode
        Set: TransferMode(self: WebHttpEndpointElement) = value
        """
        ...

    @property
    def WriteEncoding(self) -> Encoding:
        """
        Get: WriteEncoding(self: WebHttpEndpointElement) -> Encoding
        Set: WriteEncoding(self: WebHttpEndpointElement) = value
        """
        ...



class WebHttpSecurityElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ WebHttpSecurityElement() """
    @property
    def Mode(self) -> WebHttpSecurityMode:
        """
        Get: Mode(self: WebHttpSecurityElement) -> WebHttpSecurityMode
        Set: Mode(self: WebHttpSecurityElement) = value
        """
        ...

    @property
    def Transport(self) -> HttpTransportSecurityElement:
        """ Get: Transport(self: WebHttpSecurityElement) -> HttpTransportSecurityElement """
        ...



class WebMessageEncodingElement(BindingElementExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WebMessageEncodingElement() """
    @property
    def MaxReadPoolSize(self) -> int:
        """
        Get: MaxReadPoolSize(self: WebMessageEncodingElement) -> int
        Set: MaxReadPoolSize(self: WebMessageEncodingElement) = value
        """
        ...

    @property
    def MaxWritePoolSize(self) -> int:
        """
        Get: MaxWritePoolSize(self: WebMessageEncodingElement) -> int
        Set: MaxWritePoolSize(self: WebMessageEncodingElement) = value
        """
        ...

    @property
    def ReaderQuotas(self): # -> XmlDictionaryReaderQuotasElement
        """ Get: ReaderQuotas(self: WebMessageEncodingElement) -> XmlDictionaryReaderQuotasElement """
        ...

    @property
    def WebContentTypeMapperType(self) -> str:
        """
        Get: WebContentTypeMapperType(self: WebMessageEncodingElement) -> str
        Set: WebContentTypeMapperType(self: WebMessageEncodingElement) = value
        """
        ...

    @property
    def WriteEncoding(self) -> Encoding:
        """
        Get: WriteEncoding(self: WebMessageEncodingElement) -> Encoding
        Set: WriteEncoding(self: WebMessageEncodingElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: WebMessageEncodingElement, from: ServiceModelExtensionElement) """
        ...


class WebScriptEnablingElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WebScriptEnablingElement() """
    pass

class WebScriptEndpointCollectionElement(StandardEndpointCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WebScriptEndpointCollectionElement() """
    pass

class WebScriptEndpointElement(StandardEndpointElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WebScriptEndpointElement() """
    @property
    def ContentTypeMapper(self) -> str:
        """
        Get: ContentTypeMapper(self: WebScriptEndpointElement) -> str
        Set: ContentTypeMapper(self: WebScriptEndpointElement) = value
        """
        ...

    @property
    def CrossDomainScriptAccessEnabled(self) -> bool:
        """
        Get: CrossDomainScriptAccessEnabled(self: WebScriptEndpointElement) -> bool
        Set: CrossDomainScriptAccessEnabled(self: WebScriptEndpointElement) = value
        """
        ...

    @property
    def HostNameComparisonMode(self) -> HostNameComparisonMode:
        """
        Get: HostNameComparisonMode(self: WebScriptEndpointElement) -> HostNameComparisonMode
        Set: HostNameComparisonMode(self: WebScriptEndpointElement) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: WebScriptEndpointElement) -> Int64
        Set: MaxBufferPoolSize(self: WebScriptEndpointElement) = value
        """
        ...

    @property
    def MaxBufferSize(self) -> int:
        """
        Get: MaxBufferSize(self: WebScriptEndpointElement) -> int
        Set: MaxBufferSize(self: WebScriptEndpointElement) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: WebScriptEndpointElement) -> Int64
        Set: MaxReceivedMessageSize(self: WebScriptEndpointElement) = value
        """
        ...

    @property
    def ReaderQuotas(self): # -> XmlDictionaryReaderQuotasElement
        """ Get: ReaderQuotas(self: WebScriptEndpointElement) -> XmlDictionaryReaderQuotasElement """
        ...

    @property
    def Security(self) -> WebHttpSecurityElement:
        """ Get: Security(self: WebScriptEndpointElement) -> WebHttpSecurityElement """
        ...

    @property
    def TransferMode(self) -> TransferMode:
        """
        Get: TransferMode(self: WebScriptEndpointElement) -> TransferMode
        Set: TransferMode(self: WebScriptEndpointElement) = value
        """
        ...

    @property
    def WriteEncoding(self) -> Encoding:
        """
        Get: WriteEncoding(self: WebScriptEndpointElement) -> Encoding
        Set: WriteEncoding(self: WebScriptEndpointElement) = value
        """
        ...



class WindowsClientElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ WindowsClientElement() """
    @property
    def AllowedImpersonationLevel(self) -> TokenImpersonationLevel:
        """
        Get: AllowedImpersonationLevel(self: WindowsClientElement) -> TokenImpersonationLevel
        Set: AllowedImpersonationLevel(self: WindowsClientElement) = value
        """
        ...

    @property
    def AllowNtlm(self) -> bool:
        """
        Get: AllowNtlm(self: WindowsClientElement) -> bool
        Set: AllowNtlm(self: WindowsClientElement) = value
        """
        ...


    def Copy(self, from_:WindowsClientElement): # -> 
        """ Copy(self: WindowsClientElement, from: WindowsClientElement) """
        ...


class WindowsServiceElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ WindowsServiceElement() """
    @property
    def AllowAnonymousLogons(self) -> bool:
        """
        Get: AllowAnonymousLogons(self: WindowsServiceElement) -> bool
        Set: AllowAnonymousLogons(self: WindowsServiceElement) = value
        """
        ...

    @property
    def IncludeWindowsGroups(self) -> bool:
        """
        Get: IncludeWindowsGroups(self: WindowsServiceElement) -> bool
        Set: IncludeWindowsGroups(self: WindowsServiceElement) = value
        """
        ...


    def Copy(self, from_:WindowsServiceElement): # -> 
        """ Copy(self: WindowsServiceElement, from: WindowsServiceElement) """
        ...


class WindowsStreamSecurityElement(BindingElementExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WindowsStreamSecurityElement() """
    @property
    def ProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ProtectionLevel(self: WindowsStreamSecurityElement) -> ProtectionLevel
        Set: ProtectionLevel(self: WindowsStreamSecurityElement) = value
        """
        ...


    def CopyFrom(self, from_:ServiceModelExtensionElement): # -> 
        """ CopyFrom(self: WindowsStreamSecurityElement, from: ServiceModelExtensionElement) """
        ...


class WorkflowRuntimeElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WorkflowRuntimeElement() """
    @property
    def CachedInstanceExpiration(self) -> TimeSpan:
        """
        Get: CachedInstanceExpiration(self: WorkflowRuntimeElement) -> TimeSpan
        Set: CachedInstanceExpiration(self: WorkflowRuntimeElement) = value
        """
        ...

    @property
    def CommonParameters(self) -> NameValueConfigurationCollection:
        """ Get: CommonParameters(self: WorkflowRuntimeElement) -> NameValueConfigurationCollection """
        ...

    @property
    def EnablePerformanceCounters(self) -> bool:
        """
        Get: EnablePerformanceCounters(self: WorkflowRuntimeElement) -> bool
        Set: EnablePerformanceCounters(self: WorkflowRuntimeElement) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: WorkflowRuntimeElement) -> str
        Set: Name(self: WorkflowRuntimeElement) = value
        """
        ...

    @property
    def Services(self) -> ExtendedWorkflowRuntimeServiceElementCollection:
        """ Get: Services(self: WorkflowRuntimeElement) -> ExtendedWorkflowRuntimeServiceElementCollection """
        ...

    @property
    def ValidateOnCreate(self) -> bool:
        """
        Get: ValidateOnCreate(self: WorkflowRuntimeElement) -> bool
        Set: ValidateOnCreate(self: WorkflowRuntimeElement) = value
        """
        ...



class WS2007FederationHttpBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WS2007FederationHttpBindingCollectionElement() """
    pass

class WSHttpBindingBaseElement(StandardBindingElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ no doc """
    @property
    def BypassProxyOnLocal(self) -> bool:
        """
        Get: BypassProxyOnLocal(self: WSHttpBindingBaseElement) -> bool
        Set: BypassProxyOnLocal(self: WSHttpBindingBaseElement) = value
        """
        ...

    @property
    def HostNameComparisonMode(self) -> HostNameComparisonMode:
        """
        Get: HostNameComparisonMode(self: WSHttpBindingBaseElement) -> HostNameComparisonMode
        Set: HostNameComparisonMode(self: WSHttpBindingBaseElement) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: WSHttpBindingBaseElement) -> Int64
        Set: MaxBufferPoolSize(self: WSHttpBindingBaseElement) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: WSHttpBindingBaseElement) -> Int64
        Set: MaxReceivedMessageSize(self: WSHttpBindingBaseElement) = value
        """
        ...

    @property
    def MessageEncoding(self) -> WSMessageEncoding:
        """
        Get: MessageEncoding(self: WSHttpBindingBaseElement) -> WSMessageEncoding
        Set: MessageEncoding(self: WSHttpBindingBaseElement) = value
        """
        ...

    @property
    def ProxyAddress(self) -> Uri:
        """
        Get: ProxyAddress(self: WSHttpBindingBaseElement) -> Uri
        Set: ProxyAddress(self: WSHttpBindingBaseElement) = value
        """
        ...

    @property
    def ReaderQuotas(self): # -> XmlDictionaryReaderQuotasElement
        """ Get: ReaderQuotas(self: WSHttpBindingBaseElement) -> XmlDictionaryReaderQuotasElement """
        ...

    @property
    def ReliableSession(self) -> StandardBindingOptionalReliableSessionElement:
        """ Get: ReliableSession(self: WSHttpBindingBaseElement) -> StandardBindingOptionalReliableSessionElement """
        ...

    @property
    def TextEncoding(self) -> Encoding:
        """
        Get: TextEncoding(self: WSHttpBindingBaseElement) -> Encoding
        Set: TextEncoding(self: WSHttpBindingBaseElement) = value
        """
        ...

    @property
    def TransactionFlow(self) -> bool:
        """
        Get: TransactionFlow(self: WSHttpBindingBaseElement) -> bool
        Set: TransactionFlow(self: WSHttpBindingBaseElement) = value
        """
        ...

    @property
    def UseDefaultWebProxy(self) -> bool:
        """
        Get: UseDefaultWebProxy(self: WSHttpBindingBaseElement) -> bool
        Set: UseDefaultWebProxy(self: WSHttpBindingBaseElement) = value
        """
        ...



class WSFederationHttpBindingElement(WSHttpBindingBaseElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    WSFederationHttpBindingElement(name: str)
    WSFederationHttpBindingElement()
    """
    @property
    def PrivacyNoticeAt(self) -> Uri:
        """
        Get: PrivacyNoticeAt(self: WSFederationHttpBindingElement) -> Uri
        Set: PrivacyNoticeAt(self: WSFederationHttpBindingElement) = value
        """
        ...

    @property
    def PrivacyNoticeVersion(self) -> int:
        """
        Get: PrivacyNoticeVersion(self: WSFederationHttpBindingElement) -> int
        Set: PrivacyNoticeVersion(self: WSFederationHttpBindingElement) = value
        """
        ...

    @property
    def Security(self): # -> WSFederationHttpSecurityElement
        """ Get: Security(self: WSFederationHttpBindingElement) -> WSFederationHttpSecurityElement """
        ...



class WS2007FederationHttpBindingElement(WSFederationHttpBindingElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    WS2007FederationHttpBindingElement(name: str)
    WS2007FederationHttpBindingElement()
    """
    pass

class WS2007HttpBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WS2007HttpBindingCollectionElement() """
    pass

class WSHttpBindingElement(WSHttpBindingBaseElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    WSHttpBindingElement(name: str)
    WSHttpBindingElement()
    """
    @property
    def AllowCookies(self) -> bool:
        """
        Get: AllowCookies(self: WSHttpBindingElement) -> bool
        Set: AllowCookies(self: WSHttpBindingElement) = value
        """
        ...

    @property
    def Security(self): # -> WSHttpSecurityElement
        """ Get: Security(self: WSHttpBindingElement) -> WSHttpSecurityElement """
        ...



class WS2007HttpBindingElement(WSHttpBindingElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    WS2007HttpBindingElement(name: str)
    WS2007HttpBindingElement()
    """
    pass

class WsdlImporterElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    WsdlImporterElement()
    WsdlImporterElement(type: str)
    WsdlImporterElement(type: Type)
    """
    @property
    def Type(self) -> str:
        """
        Get: Type(self: WsdlImporterElement) -> str
        Set: Type(self: WsdlImporterElement) = value
        """
        ...


    def __new__(cls, type:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: str)
        __new__(cls: type, type: Type)
        """
        ...


class WsdlImporterElementCollection(ServiceModelEnhancedConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ WsdlImporterElementCollection() """
    pass

class WSDualHttpBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WSDualHttpBindingCollectionElement() """
    pass

class WSDualHttpBindingElement(StandardBindingElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    WSDualHttpBindingElement(name: str)
    WSDualHttpBindingElement()
    """
    @property
    def BypassProxyOnLocal(self) -> bool:
        """
        Get: BypassProxyOnLocal(self: WSDualHttpBindingElement) -> bool
        Set: BypassProxyOnLocal(self: WSDualHttpBindingElement) = value
        """
        ...

    @property
    def ClientBaseAddress(self) -> Uri:
        """
        Get: ClientBaseAddress(self: WSDualHttpBindingElement) -> Uri
        Set: ClientBaseAddress(self: WSDualHttpBindingElement) = value
        """
        ...

    @property
    def HostNameComparisonMode(self) -> HostNameComparisonMode:
        """
        Get: HostNameComparisonMode(self: WSDualHttpBindingElement) -> HostNameComparisonMode
        Set: HostNameComparisonMode(self: WSDualHttpBindingElement) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: WSDualHttpBindingElement) -> Int64
        Set: MaxBufferPoolSize(self: WSDualHttpBindingElement) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: WSDualHttpBindingElement) -> Int64
        Set: MaxReceivedMessageSize(self: WSDualHttpBindingElement) = value
        """
        ...

    @property
    def MessageEncoding(self) -> WSMessageEncoding:
        """
        Get: MessageEncoding(self: WSDualHttpBindingElement) -> WSMessageEncoding
        Set: MessageEncoding(self: WSDualHttpBindingElement) = value
        """
        ...

    @property
    def ProxyAddress(self) -> Uri:
        """
        Get: ProxyAddress(self: WSDualHttpBindingElement) -> Uri
        Set: ProxyAddress(self: WSDualHttpBindingElement) = value
        """
        ...

    @property
    def ReaderQuotas(self): # -> XmlDictionaryReaderQuotasElement
        """ Get: ReaderQuotas(self: WSDualHttpBindingElement) -> XmlDictionaryReaderQuotasElement """
        ...

    @property
    def ReliableSession(self) -> StandardBindingReliableSessionElement:
        """ Get: ReliableSession(self: WSDualHttpBindingElement) -> StandardBindingReliableSessionElement """
        ...

    @property
    def Security(self): # -> WSDualHttpSecurityElement
        """ Get: Security(self: WSDualHttpBindingElement) -> WSDualHttpSecurityElement """
        ...

    @property
    def TextEncoding(self) -> Encoding:
        """
        Get: TextEncoding(self: WSDualHttpBindingElement) -> Encoding
        Set: TextEncoding(self: WSDualHttpBindingElement) = value
        """
        ...

    @property
    def TransactionFlow(self) -> bool:
        """
        Get: TransactionFlow(self: WSDualHttpBindingElement) -> bool
        Set: TransactionFlow(self: WSDualHttpBindingElement) = value
        """
        ...

    @property
    def UseDefaultWebProxy(self) -> bool:
        """
        Get: UseDefaultWebProxy(self: WSDualHttpBindingElement) -> bool
        Set: UseDefaultWebProxy(self: WSDualHttpBindingElement) = value
        """
        ...



class WSDualHttpSecurityElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ WSDualHttpSecurityElement() """
    @property
    def Message(self) -> MessageSecurityOverHttpElement:
        """ Get: Message(self: WSDualHttpSecurityElement) -> MessageSecurityOverHttpElement """
        ...

    @property
    def Mode(self) -> WSDualHttpSecurityMode:
        """
        Get: Mode(self: WSDualHttpSecurityElement) -> WSDualHttpSecurityMode
        Set: Mode(self: WSDualHttpSecurityElement) = value
        """
        ...



class WSFederationHttpBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WSFederationHttpBindingCollectionElement() """
    pass

class WSFederationHttpSecurityElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ WSFederationHttpSecurityElement() """
    @property
    def Message(self) -> FederatedMessageSecurityOverHttpElement:
        """ Get: Message(self: WSFederationHttpSecurityElement) -> FederatedMessageSecurityOverHttpElement """
        ...

    @property
    def Mode(self) -> WSFederationHttpSecurityMode:
        """
        Get: Mode(self: WSFederationHttpSecurityElement) -> WSFederationHttpSecurityMode
        Set: Mode(self: WSFederationHttpSecurityElement) = value
        """
        ...



class WSHttpBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WSHttpBindingCollectionElement() """
    pass

class WSHttpContextBindingCollectionElement(StandardBindingCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WSHttpContextBindingCollectionElement() """
    pass

class WSHttpContextBindingElement(WSHttpBindingElement): # skipped bases: <type 'IBindingConfigurationElement'>, <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """
    WSHttpContextBindingElement()
    WSHttpContextBindingElement(name: str)
    """
    @property
    def ClientCallbackAddress(self) -> Uri:
        """
        Get: ClientCallbackAddress(self: WSHttpContextBindingElement) -> Uri
        Set: ClientCallbackAddress(self: WSHttpContextBindingElement) = value
        """
        ...

    @property
    def ContextManagementEnabled(self) -> bool:
        """
        Get: ContextManagementEnabled(self: WSHttpContextBindingElement) -> bool
        Set: ContextManagementEnabled(self: WSHttpContextBindingElement) = value
        """
        ...

    @property
    def ContextProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ContextProtectionLevel(self: WSHttpContextBindingElement) -> ProtectionLevel
        Set: ContextProtectionLevel(self: WSHttpContextBindingElement) = value
        """
        ...



class WSHttpSecurityElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ WSHttpSecurityElement() """
    @property
    def Message(self) -> NonDualMessageSecurityOverHttpElement:
        """ Get: Message(self: WSHttpSecurityElement) -> NonDualMessageSecurityOverHttpElement """
        ...

    @property
    def Mode(self) -> SecurityMode:
        """
        Get: Mode(self: WSHttpSecurityElement) -> SecurityMode
        Set: Mode(self: WSHttpSecurityElement) = value
        """
        ...

    @property
    def Transport(self): # -> WSHttpTransportSecurityElement
        """ Get: Transport(self: WSHttpSecurityElement) -> WSHttpTransportSecurityElement """
        ...



class WSHttpTransportSecurityElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ WSHttpTransportSecurityElement() """
    @property
    def ClientCredentialType(self) -> HttpClientCredentialType:
        """
        Get: ClientCredentialType(self: WSHttpTransportSecurityElement) -> HttpClientCredentialType
        Set: ClientCredentialType(self: WSHttpTransportSecurityElement) = value
        """
        ...

    @property
    def ExtendedProtectionPolicy(self) -> ExtendedProtectionPolicyElement:
        """ Get: ExtendedProtectionPolicy(self: WSHttpTransportSecurityElement) -> ExtendedProtectionPolicyElement """
        ...

    @property
    def ProxyCredentialType(self) -> HttpProxyCredentialType:
        """
        Get: ProxyCredentialType(self: WSHttpTransportSecurityElement) -> HttpProxyCredentialType
        Set: ProxyCredentialType(self: WSHttpTransportSecurityElement) = value
        """
        ...

    @property
    def Realm(self) -> str:
        """
        Get: Realm(self: WSHttpTransportSecurityElement) -> str
        Set: Realm(self: WSHttpTransportSecurityElement) = value
        """
        ...



class X509CertificateTrustedIssuerElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ X509CertificateTrustedIssuerElement() """
    @property
    def FindValue(self) -> str:
        """
        Get: FindValue(self: X509CertificateTrustedIssuerElement) -> str
        Set: FindValue(self: X509CertificateTrustedIssuerElement) = value
        """
        ...

    @property
    def StoreLocation(self) -> StoreLocation:
        """
        Get: StoreLocation(self: X509CertificateTrustedIssuerElement) -> StoreLocation
        Set: StoreLocation(self: X509CertificateTrustedIssuerElement) = value
        """
        ...

    @property
    def StoreName(self) -> StoreName:
        """
        Get: StoreName(self: X509CertificateTrustedIssuerElement) -> StoreName
        Set: StoreName(self: X509CertificateTrustedIssuerElement) = value
        """
        ...

    @property
    def X509FindType(self) -> X509FindType:
        """
        Get: X509FindType(self: X509CertificateTrustedIssuerElement) -> X509FindType
        Set: X509FindType(self: X509CertificateTrustedIssuerElement) = value
        """
        ...


    def Copy(self, from_:X509CertificateTrustedIssuerElement): # -> 
        """ Copy(self: X509CertificateTrustedIssuerElement, from: X509CertificateTrustedIssuerElement) """
        ...


class X509CertificateTrustedIssuerElementCollection(ServiceModelConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ X509CertificateTrustedIssuerElementCollection() """
    pass

class X509ClientCertificateAuthenticationElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ X509ClientCertificateAuthenticationElement() """
    @property
    def CertificateValidationMode(self): # -> X509CertificateValidationMode
        """
        Get: CertificateValidationMode(self: X509ClientCertificateAuthenticationElement) -> X509CertificateValidationMode
        Set: CertificateValidationMode(self: X509ClientCertificateAuthenticationElement) = value
        """
        ...

    @property
    def CustomCertificateValidatorType(self) -> str:
        """
        Get: CustomCertificateValidatorType(self: X509ClientCertificateAuthenticationElement) -> str
        Set: CustomCertificateValidatorType(self: X509ClientCertificateAuthenticationElement) = value
        """
        ...

    @property
    def IncludeWindowsGroups(self) -> bool:
        """
        Get: IncludeWindowsGroups(self: X509ClientCertificateAuthenticationElement) -> bool
        Set: IncludeWindowsGroups(self: X509ClientCertificateAuthenticationElement) = value
        """
        ...

    @property
    def MapClientCertificateToWindowsAccount(self) -> bool:
        """
        Get: MapClientCertificateToWindowsAccount(self: X509ClientCertificateAuthenticationElement) -> bool
        Set: MapClientCertificateToWindowsAccount(self: X509ClientCertificateAuthenticationElement) = value
        """
        ...

    @property
    def RevocationMode(self) -> X509RevocationMode:
        """
        Get: RevocationMode(self: X509ClientCertificateAuthenticationElement) -> X509RevocationMode
        Set: RevocationMode(self: X509ClientCertificateAuthenticationElement) = value
        """
        ...

    @property
    def TrustedStoreLocation(self) -> StoreLocation:
        """
        Get: TrustedStoreLocation(self: X509ClientCertificateAuthenticationElement) -> StoreLocation
        Set: TrustedStoreLocation(self: X509ClientCertificateAuthenticationElement) = value
        """
        ...


    def Copy(self, from_:X509ClientCertificateAuthenticationElement): # -> 
        """ Copy(self: X509ClientCertificateAuthenticationElement, from: X509ClientCertificateAuthenticationElement) """
        ...


class X509ClientCertificateCredentialsElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ X509ClientCertificateCredentialsElement() """
    @property
    def FindValue(self) -> str:
        """
        Get: FindValue(self: X509ClientCertificateCredentialsElement) -> str
        Set: FindValue(self: X509ClientCertificateCredentialsElement) = value
        """
        ...

    @property
    def StoreLocation(self) -> StoreLocation:
        """
        Get: StoreLocation(self: X509ClientCertificateCredentialsElement) -> StoreLocation
        Set: StoreLocation(self: X509ClientCertificateCredentialsElement) = value
        """
        ...

    @property
    def StoreName(self) -> StoreName:
        """
        Get: StoreName(self: X509ClientCertificateCredentialsElement) -> StoreName
        Set: StoreName(self: X509ClientCertificateCredentialsElement) = value
        """
        ...

    @property
    def X509FindType(self) -> X509FindType:
        """
        Get: X509FindType(self: X509ClientCertificateCredentialsElement) -> X509FindType
        Set: X509FindType(self: X509ClientCertificateCredentialsElement) = value
        """
        ...


    def Copy(self, from_:X509ClientCertificateCredentialsElement): # -> 
        """ Copy(self: X509ClientCertificateCredentialsElement, from: X509ClientCertificateCredentialsElement) """
        ...


class X509DefaultServiceCertificateElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ X509DefaultServiceCertificateElement() """
    @property
    def FindValue(self) -> str:
        """
        Get: FindValue(self: X509DefaultServiceCertificateElement) -> str
        Set: FindValue(self: X509DefaultServiceCertificateElement) = value
        """
        ...

    @property
    def StoreLocation(self) -> StoreLocation:
        """
        Get: StoreLocation(self: X509DefaultServiceCertificateElement) -> StoreLocation
        Set: StoreLocation(self: X509DefaultServiceCertificateElement) = value
        """
        ...

    @property
    def StoreName(self) -> StoreName:
        """
        Get: StoreName(self: X509DefaultServiceCertificateElement) -> StoreName
        Set: StoreName(self: X509DefaultServiceCertificateElement) = value
        """
        ...

    @property
    def X509FindType(self) -> X509FindType:
        """
        Get: X509FindType(self: X509DefaultServiceCertificateElement) -> X509FindType
        Set: X509FindType(self: X509DefaultServiceCertificateElement) = value
        """
        ...


    def Copy(self, from_:X509DefaultServiceCertificateElement): # -> 
        """ Copy(self: X509DefaultServiceCertificateElement, from: X509DefaultServiceCertificateElement) """
        ...


class X509InitiatorCertificateClientElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ X509InitiatorCertificateClientElement() """
    @property
    def FindValue(self) -> str:
        """
        Get: FindValue(self: X509InitiatorCertificateClientElement) -> str
        Set: FindValue(self: X509InitiatorCertificateClientElement) = value
        """
        ...

    @property
    def StoreLocation(self) -> StoreLocation:
        """
        Get: StoreLocation(self: X509InitiatorCertificateClientElement) -> StoreLocation
        Set: StoreLocation(self: X509InitiatorCertificateClientElement) = value
        """
        ...

    @property
    def StoreName(self) -> StoreName:
        """
        Get: StoreName(self: X509InitiatorCertificateClientElement) -> StoreName
        Set: StoreName(self: X509InitiatorCertificateClientElement) = value
        """
        ...

    @property
    def X509FindType(self) -> X509FindType:
        """
        Get: X509FindType(self: X509InitiatorCertificateClientElement) -> X509FindType
        Set: X509FindType(self: X509InitiatorCertificateClientElement) = value
        """
        ...


    def Copy(self, from_:X509InitiatorCertificateClientElement): # -> 
        """ Copy(self: X509InitiatorCertificateClientElement, from: X509InitiatorCertificateClientElement) """
        ...


class X509InitiatorCertificateServiceElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ X509InitiatorCertificateServiceElement() """
    @property
    def Authentication(self) -> X509ClientCertificateAuthenticationElement:
        """ Get: Authentication(self: X509InitiatorCertificateServiceElement) -> X509ClientCertificateAuthenticationElement """
        ...

    @property
    def Certificate(self) -> X509ClientCertificateCredentialsElement:
        """ Get: Certificate(self: X509InitiatorCertificateServiceElement) -> X509ClientCertificateCredentialsElement """
        ...


    def Copy(self, from_:X509InitiatorCertificateServiceElement): # -> 
        """ Copy(self: X509InitiatorCertificateServiceElement, from: X509InitiatorCertificateServiceElement) """
        ...


class X509PeerCertificateAuthenticationElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ X509PeerCertificateAuthenticationElement() """
    @property
    def CertificateValidationMode(self): # -> X509CertificateValidationMode
        """
        Get: CertificateValidationMode(self: X509PeerCertificateAuthenticationElement) -> X509CertificateValidationMode
        Set: CertificateValidationMode(self: X509PeerCertificateAuthenticationElement) = value
        """
        ...

    @property
    def CustomCertificateValidatorType(self) -> str:
        """
        Get: CustomCertificateValidatorType(self: X509PeerCertificateAuthenticationElement) -> str
        Set: CustomCertificateValidatorType(self: X509PeerCertificateAuthenticationElement) = value
        """
        ...

    @property
    def RevocationMode(self) -> X509RevocationMode:
        """
        Get: RevocationMode(self: X509PeerCertificateAuthenticationElement) -> X509RevocationMode
        Set: RevocationMode(self: X509PeerCertificateAuthenticationElement) = value
        """
        ...

    @property
    def TrustedStoreLocation(self) -> StoreLocation:
        """
        Get: TrustedStoreLocation(self: X509PeerCertificateAuthenticationElement) -> StoreLocation
        Set: TrustedStoreLocation(self: X509PeerCertificateAuthenticationElement) = value
        """
        ...


    def Copy(self, from_:X509PeerCertificateAuthenticationElement): # -> 
        """ Copy(self: X509PeerCertificateAuthenticationElement, from: X509PeerCertificateAuthenticationElement) """
        ...


class X509PeerCertificateElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ X509PeerCertificateElement() """
    @property
    def FindValue(self) -> str:
        """
        Get: FindValue(self: X509PeerCertificateElement) -> str
        Set: FindValue(self: X509PeerCertificateElement) = value
        """
        ...

    @property
    def StoreLocation(self) -> StoreLocation:
        """
        Get: StoreLocation(self: X509PeerCertificateElement) -> StoreLocation
        Set: StoreLocation(self: X509PeerCertificateElement) = value
        """
        ...

    @property
    def StoreName(self) -> StoreName:
        """
        Get: StoreName(self: X509PeerCertificateElement) -> StoreName
        Set: StoreName(self: X509PeerCertificateElement) = value
        """
        ...

    @property
    def X509FindType(self) -> X509FindType:
        """
        Get: X509FindType(self: X509PeerCertificateElement) -> X509FindType
        Set: X509FindType(self: X509PeerCertificateElement) = value
        """
        ...


    def Copy(self, from_:X509PeerCertificateElement): # -> 
        """ Copy(self: X509PeerCertificateElement, from: X509PeerCertificateElement) """
        ...


class X509RecipientCertificateClientElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ X509RecipientCertificateClientElement() """
    @property
    def Authentication(self): # -> X509ServiceCertificateAuthenticationElement
        """ Get: Authentication(self: X509RecipientCertificateClientElement) -> X509ServiceCertificateAuthenticationElement """
        ...

    @property
    def DefaultCertificate(self) -> X509DefaultServiceCertificateElement:
        """ Get: DefaultCertificate(self: X509RecipientCertificateClientElement) -> X509DefaultServiceCertificateElement """
        ...

    @property
    def ScopedCertificates(self): # -> X509ScopedServiceCertificateElementCollection
        """ Get: ScopedCertificates(self: X509RecipientCertificateClientElement) -> X509ScopedServiceCertificateElementCollection """
        ...

    @property
    def SslCertificateAuthentication(self): # -> X509ServiceCertificateAuthenticationElement
        """ Get: SslCertificateAuthentication(self: X509RecipientCertificateClientElement) -> X509ServiceCertificateAuthenticationElement """
        ...


    def Copy(self, from_:X509RecipientCertificateClientElement): # -> 
        """ Copy(self: X509RecipientCertificateClientElement, from: X509RecipientCertificateClientElement) """
        ...


class X509RecipientCertificateServiceElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ X509RecipientCertificateServiceElement() """
    @property
    def FindValue(self) -> str:
        """
        Get: FindValue(self: X509RecipientCertificateServiceElement) -> str
        Set: FindValue(self: X509RecipientCertificateServiceElement) = value
        """
        ...

    @property
    def StoreLocation(self) -> StoreLocation:
        """
        Get: StoreLocation(self: X509RecipientCertificateServiceElement) -> StoreLocation
        Set: StoreLocation(self: X509RecipientCertificateServiceElement) = value
        """
        ...

    @property
    def StoreName(self) -> StoreName:
        """
        Get: StoreName(self: X509RecipientCertificateServiceElement) -> StoreName
        Set: StoreName(self: X509RecipientCertificateServiceElement) = value
        """
        ...

    @property
    def X509FindType(self) -> X509FindType:
        """
        Get: X509FindType(self: X509RecipientCertificateServiceElement) -> X509FindType
        Set: X509FindType(self: X509RecipientCertificateServiceElement) = value
        """
        ...


    def Copy(self, from_:X509RecipientCertificateServiceElement): # -> 
        """ Copy(self: X509RecipientCertificateServiceElement, from: X509RecipientCertificateServiceElement) """
        ...


class X509ScopedServiceCertificateElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ X509ScopedServiceCertificateElement() """
    @property
    def FindValue(self) -> str:
        """
        Get: FindValue(self: X509ScopedServiceCertificateElement) -> str
        Set: FindValue(self: X509ScopedServiceCertificateElement) = value
        """
        ...

    @property
    def StoreLocation(self) -> StoreLocation:
        """
        Get: StoreLocation(self: X509ScopedServiceCertificateElement) -> StoreLocation
        Set: StoreLocation(self: X509ScopedServiceCertificateElement) = value
        """
        ...

    @property
    def StoreName(self) -> StoreName:
        """
        Get: StoreName(self: X509ScopedServiceCertificateElement) -> StoreName
        Set: StoreName(self: X509ScopedServiceCertificateElement) = value
        """
        ...

    @property
    def TargetUri(self) -> Uri:
        """
        Get: TargetUri(self: X509ScopedServiceCertificateElement) -> Uri
        Set: TargetUri(self: X509ScopedServiceCertificateElement) = value
        """
        ...

    @property
    def X509FindType(self) -> X509FindType:
        """
        Get: X509FindType(self: X509ScopedServiceCertificateElement) -> X509FindType
        Set: X509FindType(self: X509ScopedServiceCertificateElement) = value
        """
        ...


    def Copy(self, from_:X509ScopedServiceCertificateElement): # -> 
        """ Copy(self: X509ScopedServiceCertificateElement, from: X509ScopedServiceCertificateElement) """
        ...


class X509ScopedServiceCertificateElementCollection(ServiceModelConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ X509ScopedServiceCertificateElementCollection() """
    pass

class X509ServiceCertificateAuthenticationElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ X509ServiceCertificateAuthenticationElement() """
    @property
    def CertificateValidationMode(self): # -> X509CertificateValidationMode
        """
        Get: CertificateValidationMode(self: X509ServiceCertificateAuthenticationElement) -> X509CertificateValidationMode
        Set: CertificateValidationMode(self: X509ServiceCertificateAuthenticationElement) = value
        """
        ...

    @property
    def CustomCertificateValidatorType(self) -> str:
        """
        Get: CustomCertificateValidatorType(self: X509ServiceCertificateAuthenticationElement) -> str
        Set: CustomCertificateValidatorType(self: X509ServiceCertificateAuthenticationElement) = value
        """
        ...

    @property
    def RevocationMode(self) -> X509RevocationMode:
        """
        Get: RevocationMode(self: X509ServiceCertificateAuthenticationElement) -> X509RevocationMode
        Set: RevocationMode(self: X509ServiceCertificateAuthenticationElement) = value
        """
        ...

    @property
    def TrustedStoreLocation(self) -> StoreLocation:
        """
        Get: TrustedStoreLocation(self: X509ServiceCertificateAuthenticationElement) -> StoreLocation
        Set: TrustedStoreLocation(self: X509ServiceCertificateAuthenticationElement) = value
        """
        ...


    def Copy(self, from_:X509ServiceCertificateAuthenticationElement): # -> 
        """ Copy(self: X509ServiceCertificateAuthenticationElement, from: X509ServiceCertificateAuthenticationElement) """
        ...


class XmlDictionaryReaderQuotasElement(ServiceModelConfigurationElement): # skipped bases: <type 'object'>
    """ XmlDictionaryReaderQuotasElement() """
    @property
    def MaxArrayLength(self) -> int:
        """
        Get: MaxArrayLength(self: XmlDictionaryReaderQuotasElement) -> int
        Set: MaxArrayLength(self: XmlDictionaryReaderQuotasElement) = value
        """
        ...

    @property
    def MaxBytesPerRead(self) -> int:
        """
        Get: MaxBytesPerRead(self: XmlDictionaryReaderQuotasElement) -> int
        Set: MaxBytesPerRead(self: XmlDictionaryReaderQuotasElement) = value
        """
        ...

    @property
    def MaxDepth(self) -> int:
        """
        Get: MaxDepth(self: XmlDictionaryReaderQuotasElement) -> int
        Set: MaxDepth(self: XmlDictionaryReaderQuotasElement) = value
        """
        ...

    @property
    def MaxNameTableCharCount(self) -> int:
        """
        Get: MaxNameTableCharCount(self: XmlDictionaryReaderQuotasElement) -> int
        Set: MaxNameTableCharCount(self: XmlDictionaryReaderQuotasElement) = value
        """
        ...

    @property
    def MaxStringContentLength(self) -> int:
        """
        Get: MaxStringContentLength(self: XmlDictionaryReaderQuotasElement) -> int
        Set: MaxStringContentLength(self: XmlDictionaryReaderQuotasElement) = value
        """
        ...



class XmlElementElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    XmlElementElement()
    XmlElementElement(element: XmlElement)
    """
    @property
    def XmlElement(self) -> XmlElement:
        """
        Get: XmlElement(self: XmlElementElement) -> XmlElement
        Set: XmlElement(self: XmlElementElement) = value
        """
        ...


    def Copy(self, source:XmlElementElement): # -> 
        """ Copy(self: XmlElementElement, source: XmlElementElement) """
        ...

    def __new__(cls, element:XmlElement = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, element: XmlElement)
        """
        ...


class XmlElementElementCollection(ServiceModelConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ XmlElementElementCollection() """
    pass

class XPathMessageFilterElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ XPathMessageFilterElement() """
    @property
    def Filter(self) -> XPathMessageFilter:
        """
        Get: Filter(self: XPathMessageFilterElement) -> XPathMessageFilter
        Set: Filter(self: XPathMessageFilterElement) = value
        """
        ...



class XPathMessageFilterElementCollection(ServiceModelConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ XPathMessageFilterElementCollection() """
    pass

class XPathMessageFilterElementComparer(IComparer): # skipped bases: <type 'object'>
    """ XPathMessageFilterElementComparer() """
    pass

