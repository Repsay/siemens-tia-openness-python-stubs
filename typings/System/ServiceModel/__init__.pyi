# encoding: utf-8
# module System.ServiceModel calls itself ServiceModel
# from System.ServiceModel.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.WorkflowServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.ServiceModel.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.ServiceModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.ServiceModel.Channels, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, Microsoft.Transactions.Bridge, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.IdentityModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.JScript import Binding

from Microsoft.SqlServer.Management.Smo import AuditLevel

from System import (Array, AsyncCallback, Attribute, Enum, EventArgs, 
    IAsyncResult, IDisposable, Int64, SystemException, TimeSpan, Type, Uri)

from System.Collections import ICollection

from System.Collections.Generic import (Dictionary, SynchronizedCollection, 
    SynchronizedKeyedCollection, SynchronizedReadOnlyCollection)

from System.Collections.ObjectModel import Collection, ReadOnlyCollection

from System.Configuration import Configuration

from System.Data import IsolationLevel

from System.Data.Metadata.Edm import ConcurrencyMode

from System.Globalization import CultureInfo

from System.IdentityModel.Claims import Claim

from System.IdentityModel.Configuration import IdentityConfiguration

from System.IdentityModel.Policy import AuthorizationContext

from System.IdentityModel.Selectors import (SecurityTokenManager, 
    SecurityTokenVersion)

from System.IdentityModel.Tokens import SecurityKeyType

from System.Messaging import Message

from System.Net import IPAddress

from System.Net.Security import ProtectionLevel

from System.Runtime.InteropServices import ExternalException

from System.Runtime.Remoting.Channels import IChannel

from System.Runtime.Serialization import SerializationInfo, StreamingContext

from System.Security.Authentication import SslProtocols

from System.Security.Authentication.ExtendedProtection import (
    ExtendedProtectionPolicy)

from System.Security.Claims import ClaimsPrincipal

from System.Security.Cryptography.X509Certificates import (X509Certificate2, 
    X509Certificate2Collection)

from System.Security.Principal import IIdentity, WindowsIdentity

from System.ServiceModel.Channels import WebContentTypeMapper

from System.ServiceModel.PeerResolvers import (PeerReferralPolicy, 
    PeerResolverSettings)

from System.ServiceModel.Security import (BasicSecurityProfileVersion, 
    SecureConversationVersion, SecurityAlgorithmSuite, SecurityPolicyVersion, 
    SecurityVersion, TrustVersion)

from System.Text import Encoding

from System.Threading import SynchronizationContext

from System.Web.Routing import RequestContext

from System.Web.Services.Description import ServiceDescription

from System.Windows.Markup import MarkupExtension

from System.Xml import (XmlDictionaryReader, XmlDictionaryReaderQuotas, 
    XmlDictionaryString, XmlDictionaryWriter, XmlNamespaceManager, XmlWriter)

from System.Xml.Linq import XName

from System.Xml.Serialization import IXmlSerializable

from System.Xml.Xsl import XsltContext

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (AddressHeaderCollection, 
    AddressingVersion, BasicHttpSecurity, BasicHttpSecurityMode, 
    BasicHttpsSecurity, BasicHttpsSecurityMode, BindingElementCollection, 
    BindingParameterCollection, BoundEvent, ChannelDispatcherCollection, 
    ClientCredentials, CommunicationObject, E, EndpointAddress, 
    EndpointDispatcher, EnvelopeVersion, FaultException, FaultReason, 
    FaultReasonText, HostNameComparisonMode, HttpTransportSecurity, 
    IBindingRuntimePreferences, IChannelFactory, IClientChannel, 
    ICommunicationObject, IContractBehavior, IContractBehaviorAttribute, 
    IDuplexContextChannel, IEndpointBehavior, IExtensibleObject, 
    IExtensionCollection, IInputSession, IOperationBehavior, IOutputSession, 
    IServiceBehavior, InstanceContext, MessageFault, MessageFilter, 
    MessageHeaders, MessageProperties, MessageQuery, MessageQueryTable, 
    MessageVersion, NetHttpMessageEncoding, NetMsmqSecurity, 
    NetMsmqSecurityMode, NetNamedPipeSecurity, NetNamedPipeSecurityMode, 
    NetTcpSecurity, OperationFormatStyle, OptionalReliableSession, 
    PeerSecuritySettings, PeerTransportSecuritySettings, 
    QueueTransferProtocol, QueuedDeliveryRequirementsMode, 
    ReceiveErrorHandling, ReleaseInstanceMode, SecurityMode, 
    ServiceAuthenticationBehavior, ServiceAuthorizationBehavior, 
    ServiceCredentials, ServiceEndpoint, ServiceHostBase, 
    ServiceSecurityContext, SessionMode, T, TcpTransportSecurity, 
    TransactionFlowOption, TransactionProtocol, TransferMode, 
    WSDualHttpSecurity, WSDualHttpSecurityMode, WSFederationHttpSecurity, 
    WSFederationHttpSecurityMode, WSHttpSecurity, WSMessageEncoding, 
    WebHttpSecurity, WebHttpSecurityMode, WebSocketTransportSettings, field#)
"""

# no functions
# classes

class CommunicationException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CommunicationException()
    CommunicationException(message: str)
    CommunicationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ActionNotSupportedException(CommunicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ActionNotSupportedException()
    ActionNotSupportedException(message: str)
    ActionNotSupportedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class AddressAccessDeniedException(CommunicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    AddressAccessDeniedException()
    AddressAccessDeniedException(message: str)
    AddressAccessDeniedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class AddressAlreadyInUseException(CommunicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    AddressAlreadyInUseException()
    AddressAlreadyInUseException(message: str)
    AddressAlreadyInUseException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class AddressFilterMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AddressFilterMode, values: Any (2), Exact (0), Prefix (1) """
    Any: AddressFilterMode = ...
    Exact: AddressFilterMode = ...
    Prefix: AddressFilterMode = ...
    value__ = ...


class AuditLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AuditLevel, values: Failure (2), None (0), Success (1), SuccessOrFailure (3) """
    Failure: AuditLevel = ...
    Success: AuditLevel = ...
    SuccessOrFailure: AuditLevel = ...
    value__ = ...


class AuditLogLocation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AuditLogLocation, values: Application (1), Default (0), Security (2) """
    Application: AuditLogLocation = ...
    Default: AuditLogLocation = ...
    Security: AuditLogLocation = ...
    value__ = ...


class IDefaultCommunicationTimeouts: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CloseTimeout(self) -> TimeSpan:
        """ Get: CloseTimeout(self: IDefaultCommunicationTimeouts) -> TimeSpan """
        ...

    @property
    def OpenTimeout(self) -> TimeSpan:
        """ Get: OpenTimeout(self: IDefaultCommunicationTimeouts) -> TimeSpan """
        ...

    @property
    def ReceiveTimeout(self) -> TimeSpan:
        """ Get: ReceiveTimeout(self: IDefaultCommunicationTimeouts) -> TimeSpan """
        ...

    @property
    def SendTimeout(self) -> TimeSpan:
        """ Get: SendTimeout(self: IDefaultCommunicationTimeouts) -> TimeSpan """
        ...



class HttpBindingBase(IBindingRuntimePreferences, Binding): # skipped bases: <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """ no doc """
    @property
    def AllowCookies(self) -> bool:
        """
        Get: AllowCookies(self: HttpBindingBase) -> bool
        Set: AllowCookies(self: HttpBindingBase) = value
        """
        ...

    @property
    def BypassProxyOnLocal(self) -> bool:
        """
        Get: BypassProxyOnLocal(self: HttpBindingBase) -> bool
        Set: BypassProxyOnLocal(self: HttpBindingBase) = value
        """
        ...

    @property
    def EnvelopeVersion(self): # -> EnvelopeVersion
        """ Get: EnvelopeVersion(self: HttpBindingBase) -> EnvelopeVersion """
        ...

    @property
    def HostNameComparisonMode(self): # -> HostNameComparisonMode
        """
        Get: HostNameComparisonMode(self: HttpBindingBase) -> HostNameComparisonMode
        Set: HostNameComparisonMode(self: HttpBindingBase) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: HttpBindingBase) -> Int64
        Set: MaxBufferPoolSize(self: HttpBindingBase) = value
        """
        ...

    @property
    def MaxBufferSize(self) -> int:
        """
        Get: MaxBufferSize(self: HttpBindingBase) -> int
        Set: MaxBufferSize(self: HttpBindingBase) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: HttpBindingBase) -> Int64
        Set: MaxReceivedMessageSize(self: HttpBindingBase) = value
        """
        ...

    @property
    def ProxyAddress(self) -> Uri:
        """
        Get: ProxyAddress(self: HttpBindingBase) -> Uri
        Set: ProxyAddress(self: HttpBindingBase) = value
        """
        ...

    @property
    def ReaderQuotas(self) -> XmlDictionaryReaderQuotas:
        """
        Get: ReaderQuotas(self: HttpBindingBase) -> XmlDictionaryReaderQuotas
        Set: ReaderQuotas(self: HttpBindingBase) = value
        """
        ...

    @property
    def TextEncoding(self) -> Encoding:
        """
        Get: TextEncoding(self: HttpBindingBase) -> Encoding
        Set: TextEncoding(self: HttpBindingBase) = value
        """
        ...

    @property
    def TransferMode(self): # -> TransferMode
        """
        Get: TransferMode(self: HttpBindingBase) -> TransferMode
        Set: TransferMode(self: HttpBindingBase) = value
        """
        ...

    @property
    def UseDefaultWebProxy(self) -> bool:
        """
        Get: UseDefaultWebProxy(self: HttpBindingBase) -> bool
        Set: UseDefaultWebProxy(self: HttpBindingBase) = value
        """
        ...


    def ShouldSerializeReaderQuotas(self) -> bool:
        """ ShouldSerializeReaderQuotas(self: HttpBindingBase) -> bool """
        ...

    def ShouldSerializeTextEncoding(self) -> bool:
        """ ShouldSerializeTextEncoding(self: HttpBindingBase) -> bool """
        ...


class BasicHttpBinding(HttpBindingBase): # skipped bases: <type 'IBindingRuntimePreferences'>, <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    BasicHttpBinding()
    BasicHttpBinding(configurationName: str)
    BasicHttpBinding(securityMode: BasicHttpSecurityMode)
    """
    @property
    def EnableHttpCookieContainer(self) -> bool:
        """
        Get: EnableHttpCookieContainer(self: BasicHttpBinding) -> bool
        Set: EnableHttpCookieContainer(self: BasicHttpBinding) = value
        """
        ...

    @property
    def MessageEncoding(self): # -> WSMessageEncoding
        """
        Get: MessageEncoding(self: BasicHttpBinding) -> WSMessageEncoding
        Set: MessageEncoding(self: BasicHttpBinding) = value
        """
        ...

    @property
    def Security(self): # -> BasicHttpSecurity
        """
        Get: Security(self: BasicHttpBinding) -> BasicHttpSecurity
        Set: Security(self: BasicHttpBinding) = value
        """
        ...


    def BuildChannelFactory(self, parameters): # -> IChannelFactory # Not found arg types: {'parameters': 'BindingParameterCollection'}
        """ BuildChannelFactory[TChannel](self: BasicHttpBinding, parameters: BindingParameterCollection) -> IChannelFactory[TChannel] """
        ...

    def CreateBindingElements(self): # -> BindingElementCollection
        """ CreateBindingElements(self: BasicHttpBinding) -> BindingElementCollection """
        ...

    def ShouldSerializeEnableHttpCookieContainer(self) -> bool:
        """ ShouldSerializeEnableHttpCookieContainer(self: BasicHttpBinding) -> bool """
        ...

    def ShouldSerializeSecurity(self) -> bool:
        """ ShouldSerializeSecurity(self: BasicHttpBinding) -> bool """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, configurationName: str)
        __new__(cls: type, securityMode: BasicHttpSecurityMode)
        """
        ...


class BasicHttpContextBinding(BasicHttpBinding): # skipped bases: <type 'IBindingRuntimePreferences'>, <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    BasicHttpContextBinding()
    BasicHttpContextBinding(securityMode: BasicHttpSecurityMode)
    BasicHttpContextBinding(configName: str)
    """
    @property
    def ContextManagementEnabled(self) -> bool:
        """
        Get: ContextManagementEnabled(self: BasicHttpContextBinding) -> bool
        Set: ContextManagementEnabled(self: BasicHttpContextBinding) = value
        """
        ...



class BasicHttpMessageCredentialType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BasicHttpMessageCredentialType, values: Certificate (1), UserName (0) """
    Certificate: BasicHttpMessageCredentialType = ...
    UserName: BasicHttpMessageCredentialType = ...
    value__ = ...


class BasicHttpMessageSecurity: # skipped bases: <type 'object'>, <type 'object'>
    """ BasicHttpMessageSecurity() """
    @property
    def AlgorithmSuite(self) -> SecurityAlgorithmSuite:
        """
        Get: AlgorithmSuite(self: BasicHttpMessageSecurity) -> SecurityAlgorithmSuite
        Set: AlgorithmSuite(self: BasicHttpMessageSecurity) = value
        """
        ...

    @property
    def ClientCredentialType(self) -> BasicHttpMessageCredentialType:
        """
        Get: ClientCredentialType(self: BasicHttpMessageSecurity) -> BasicHttpMessageCredentialType
        Set: ClientCredentialType(self: BasicHttpMessageSecurity) = value
        """
        ...


    def ShouldSerializeAlgorithmSuite(self) -> bool:
        """ ShouldSerializeAlgorithmSuite(self: BasicHttpMessageSecurity) -> bool """
        ...

    def ShouldSerializeClientCredentialType(self) -> bool:
        """ ShouldSerializeClientCredentialType(self: BasicHttpMessageSecurity) -> bool """
        ...


class BasicHttpsBinding(HttpBindingBase): # skipped bases: <type 'IBindingRuntimePreferences'>, <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    BasicHttpsBinding()
    BasicHttpsBinding(configurationName: str)
    BasicHttpsBinding(securityMode: BasicHttpsSecurityMode)
    """
    @property
    def MessageEncoding(self): # -> WSMessageEncoding
        """
        Get: MessageEncoding(self: BasicHttpsBinding) -> WSMessageEncoding
        Set: MessageEncoding(self: BasicHttpsBinding) = value
        """
        ...

    @property
    def Security(self): # -> BasicHttpsSecurity
        """
        Get: Security(self: BasicHttpsBinding) -> BasicHttpsSecurity
        Set: Security(self: BasicHttpsBinding) = value
        """
        ...


    def BuildChannelFactory(self, parameters): # -> IChannelFactory # Not found arg types: {'parameters': 'BindingParameterCollection'}
        """ BuildChannelFactory[TChannel](self: BasicHttpsBinding, parameters: BindingParameterCollection) -> IChannelFactory[TChannel] """
        ...

    def CreateBindingElements(self): # -> BindingElementCollection
        """ CreateBindingElements(self: BasicHttpsBinding) -> BindingElementCollection """
        ...

    def ShouldSerializeSecurity(self) -> bool:
        """ ShouldSerializeSecurity(self: BasicHttpsBinding) -> bool """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, configurationName: str)
        __new__(cls: type, securityMode: BasicHttpsSecurityMode)
        """
        ...


class BasicHttpSecurity: # skipped bases: <type 'object'>, <type 'object'>
    """ BasicHttpSecurity() """
    @property
    def Message(self) -> BasicHttpMessageSecurity:
        """
        Get: Message(self: BasicHttpSecurity) -> BasicHttpMessageSecurity
        Set: Message(self: BasicHttpSecurity) = value
        """
        ...

    @property
    def Mode(self): # -> BasicHttpSecurityMode
        """
        Get: Mode(self: BasicHttpSecurity) -> BasicHttpSecurityMode
        Set: Mode(self: BasicHttpSecurity) = value
        """
        ...

    @property
    def Transport(self): # -> HttpTransportSecurity
        """
        Get: Transport(self: BasicHttpSecurity) -> HttpTransportSecurity
        Set: Transport(self: BasicHttpSecurity) = value
        """
        ...


    def ShouldSerializeMessage(self) -> bool:
        """ ShouldSerializeMessage(self: BasicHttpSecurity) -> bool """
        ...

    def ShouldSerializeTransport(self) -> bool:
        """ ShouldSerializeTransport(self: BasicHttpSecurity) -> bool """
        ...


class BasicHttpSecurityMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BasicHttpSecurityMode, values: Message (2), None (0), Transport (1), TransportCredentialOnly (4), TransportWithMessageCredential (3) """
    Message: BasicHttpSecurityMode = ...
    Transport: BasicHttpSecurityMode = ...
    TransportCredentialOnly: BasicHttpSecurityMode = ...
    TransportWithMessageCredential: BasicHttpSecurityMode = ...
    value__ = ...


class BasicHttpsSecurity: # skipped bases: <type 'object'>, <type 'object'>
    """ BasicHttpsSecurity() """
    @property
    def Message(self) -> BasicHttpMessageSecurity:
        """
        Get: Message(self: BasicHttpsSecurity) -> BasicHttpMessageSecurity
        Set: Message(self: BasicHttpsSecurity) = value
        """
        ...

    @property
    def Mode(self): # -> BasicHttpsSecurityMode
        """
        Get: Mode(self: BasicHttpsSecurity) -> BasicHttpsSecurityMode
        Set: Mode(self: BasicHttpsSecurity) = value
        """
        ...

    @property
    def Transport(self): # -> HttpTransportSecurity
        """
        Get: Transport(self: BasicHttpsSecurity) -> HttpTransportSecurity
        Set: Transport(self: BasicHttpsSecurity) = value
        """
        ...


    def ShouldSerializeMessage(self) -> bool:
        """ ShouldSerializeMessage(self: BasicHttpsSecurity) -> bool """
        ...

    def ShouldSerializeTransport(self) -> bool:
        """ ShouldSerializeTransport(self: BasicHttpsSecurity) -> bool """
        ...


class BasicHttpsSecurityMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BasicHttpsSecurityMode, values: Transport (0), TransportWithMessageCredential (1) """
    Transport: BasicHttpsSecurityMode = ...
    TransportWithMessageCredential: BasicHttpsSecurityMode = ...
    value__ = ...


class CacheSetting(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CacheSetting, values: AlwaysOff (2), AlwaysOn (1), Default (0) """
    AlwaysOff: CacheSetting = ...
    AlwaysOn: CacheSetting = ...
    Default: CacheSetting = ...
    value__ = ...


class CallbackBehaviorAttribute(Attribute, IEndpointBehavior): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CallbackBehaviorAttribute() """
    @property
    def AutomaticSessionShutdown(self) -> bool:
        """
        Get: AutomaticSessionShutdown(self: CallbackBehaviorAttribute) -> bool
        Set: AutomaticSessionShutdown(self: CallbackBehaviorAttribute) = value
        """
        ...

    @property
    def ConcurrencyMode(self) -> ConcurrencyMode:
        """
        Get: ConcurrencyMode(self: CallbackBehaviorAttribute) -> ConcurrencyMode
        Set: ConcurrencyMode(self: CallbackBehaviorAttribute) = value
        """
        ...

    @property
    def IgnoreExtensionDataObject(self) -> bool:
        """
        Get: IgnoreExtensionDataObject(self: CallbackBehaviorAttribute) -> bool
        Set: IgnoreExtensionDataObject(self: CallbackBehaviorAttribute) = value
        """
        ...

    @property
    def IncludeExceptionDetailInFaults(self) -> bool:
        """
        Get: IncludeExceptionDetailInFaults(self: CallbackBehaviorAttribute) -> bool
        Set: IncludeExceptionDetailInFaults(self: CallbackBehaviorAttribute) = value
        """
        ...

    @property
    def MaxItemsInObjectGraph(self) -> int:
        """
        Get: MaxItemsInObjectGraph(self: CallbackBehaviorAttribute) -> int
        Set: MaxItemsInObjectGraph(self: CallbackBehaviorAttribute) = value
        """
        ...

    @property
    def TransactionIsolationLevel(self) -> IsolationLevel:
        """
        Get: TransactionIsolationLevel(self: CallbackBehaviorAttribute) -> IsolationLevel
        Set: TransactionIsolationLevel(self: CallbackBehaviorAttribute) = value
        """
        ...

    @property
    def TransactionTimeout(self) -> str:
        """
        Get: TransactionTimeout(self: CallbackBehaviorAttribute) -> str
        Set: TransactionTimeout(self: CallbackBehaviorAttribute) = value
        """
        ...

    @property
    def UseSynchronizationContext(self) -> bool:
        """
        Get: UseSynchronizationContext(self: CallbackBehaviorAttribute) -> bool
        Set: UseSynchronizationContext(self: CallbackBehaviorAttribute) = value
        """
        ...

    @property
    def ValidateMustUnderstand(self) -> bool:
        """
        Get: ValidateMustUnderstand(self: CallbackBehaviorAttribute) -> bool
        Set: ValidateMustUnderstand(self: CallbackBehaviorAttribute) = value
        """
        ...



class ChannelFactory: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Credentials(self): # -> ClientCredentials
        """ Get: Credentials(self: ChannelFactory) -> ClientCredentials """
        ...

    @property
    def DefaultCloseTimeout(self):
        ...

    @property
    def DefaultOpenTimeout(self):
        ...

    @property
    def Endpoint(self): # -> ServiceEndpoint
        """ Get: Endpoint(self: ChannelFactory) -> ServiceEndpoint """
        ...

    @property
    def IsDisposed(self):
        ...

    @property
    def ThisLock(self):
        ...


    def ApplyConfiguration(self, *args): #cannot find CLR method
        """ ApplyConfiguration(self: ChannelFactory, configurationName: str) """
        ...

    def CreateDescription(self, *args): #cannot find CLR method
        """ CreateDescription(self: ChannelFactory) -> ServiceEndpoint """
        ...

    def CreateFactory(self, *args): #cannot find CLR method
        """ CreateFactory(self: ChannelFactory) -> IChannelFactory """
        ...

    def EnsureOpened(self, *args): #cannot find CLR method
        """ EnsureOpened(self: ChannelFactory) """
        ...

    def Fault(self, *args): #cannot find CLR method
        """ Fault(self: CommunicationObject) """
        ...

    def GetCommunicationObjectType(self, *args): #cannot find CLR method
        """ GetCommunicationObjectType(self: CommunicationObject) -> Type """
        ...

    def GetProperty(self): # -> T
        """ GetProperty[T](self: ChannelFactory) -> T """
        ...

    def InitializeEndpoint(self, *args): #cannot find CLR method
        """ InitializeEndpoint(self: ChannelFactory, binding: Binding, address: EndpointAddress)InitializeEndpoint(self: ChannelFactory, endpoint: ServiceEndpoint)InitializeEndpoint(self: ChannelFactory, configurationName: str, address: EndpointAddress) """
        ...

    def OnAbort(self, *args): #cannot find CLR method
        """ OnAbort(self: ChannelFactory) """
        ...

    def OnBeginClose(self, *args): #cannot find CLR method
        """ OnBeginClose(self: ChannelFactory, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def OnBeginOpen(self, *args): #cannot find CLR method
        """ OnBeginOpen(self: ChannelFactory, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def OnClose(self, *args): #cannot find CLR method
        """ OnClose(self: ChannelFactory, timeout: TimeSpan) """
        ...

    def OnClosed(self, *args): #cannot find CLR method
        """ OnClosed(self: CommunicationObject) """
        ...

    def OnClosing(self, *args): #cannot find CLR method
        """ OnClosing(self: CommunicationObject) """
        ...

    def OnEndClose(self, *args): #cannot find CLR method
        """ OnEndClose(self: ChannelFactory, result: IAsyncResult) """
        ...

    def OnEndOpen(self, *args): #cannot find CLR method
        """ OnEndOpen(self: ChannelFactory, result: IAsyncResult) """
        ...

    def OnFaulted(self, *args): #cannot find CLR method
        """ OnFaulted(self: CommunicationObject) """
        ...

    def OnOpen(self, *args): #cannot find CLR method
        """ OnOpen(self: ChannelFactory, timeout: TimeSpan) """
        ...

    def OnOpened(self, *args): #cannot find CLR method
        """ OnOpened(self: ChannelFactory) """
        ...

    def OnOpening(self, *args): #cannot find CLR method
        """ OnOpening(self: ChannelFactory) """
        ...

    def ThrowIfDisposed(self, *args): #cannot find CLR method
        """ ThrowIfDisposed(self: CommunicationObject) """
        ...

    def ThrowIfDisposedOrImmutable(self, *args): #cannot find CLR method
        """ ThrowIfDisposedOrImmutable(self: CommunicationObject) """
        ...

    def ThrowIfDisposedOrNotOpen(self, *args): #cannot find CLR method
        """ ThrowIfDisposedOrNotOpen(self: CommunicationObject) """
        ...

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        ...

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        ...


class ChannelTerminatedException(CommunicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ChannelTerminatedException()
    ChannelTerminatedException(message: str)
    ChannelTerminatedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ClientBase(ICommunicationObject, IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CacheSetting(self) -> CacheSetting:
        """
        Get: CacheSetting() -> CacheSetting
        Set: CacheSetting() = value
        """
        ...

    @property
    def Channel(self):
        ...

    @property
    def ChannelFactory(self) -> ChannelFactory:
        """ Get: ChannelFactory(self: ClientBase[TChannel]) -> ChannelFactory[TChannel] """
        ...

    @property
    def ClientCredentials(self): # -> ClientCredentials
        """ Get: ClientCredentials(self: ClientBase[TChannel]) -> ClientCredentials """
        ...

    @property
    def Endpoint(self): # -> ServiceEndpoint
        """ Get: Endpoint(self: ClientBase[TChannel]) -> ServiceEndpoint """
        ...

    @property
    def InnerChannel(self): # -> IClientChannel
        """ Get: InnerChannel(self: ClientBase[TChannel]) -> IClientChannel """
        ...


    def BeginOperationDelegate(self, *args): #cannot find CLR method
        """ BeginOperationDelegate(object: object, method: IntPtr) """
        ...

    def ChannelBase`1(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def CreateChannel(self, *args): #cannot find CLR method
        """ CreateChannel(self: ClientBase[TChannel]) -> TChannel """
        ...

    def DisplayInitializationUI(self): # -> 
        """ DisplayInitializationUI(self: ClientBase[TChannel]) """
        ...

    def EndOperationDelegate(self, *args): #cannot find CLR method
        """ EndOperationDelegate(object: object, method: IntPtr) """
        ...

    def GetDefaultValueForInitialization(self, *args): #cannot find CLR method
        """ GetDefaultValueForInitialization[T](self: ClientBase[TChannel]) -> T """
        ...

    def InvokeAsync(self, *args): #cannot find CLR method
        """ InvokeAsync(self: ClientBase[TChannel], beginOperationDelegate: BeginOperationDelegate, inValues: Array[object], endOperationDelegate: EndOperationDelegate, operationCompletedCallback: SendOrPostCallback, userState: object) """
        ...

    def InvokeAsyncCompletedEventArgs(self, *args): #cannot find CLR method
        """ no doc """
        ...



class ClientCredentialsSecurityTokenManager(SecurityTokenManager): # skipped bases: <type 'object'>
    """ ClientCredentialsSecurityTokenManager(clientCredentials: ClientCredentials) """
    @property
    def ClientCredentials(self): # -> ClientCredentials
        """ Get: ClientCredentials(self: ClientCredentialsSecurityTokenManager) -> ClientCredentials """
        ...


    def IsIssuedSecurityTokenRequirement(self, *args): #cannot find CLR method
        """ IsIssuedSecurityTokenRequirement(self: ClientCredentialsSecurityTokenManager, requirement: SecurityTokenRequirement) -> bool """
        ...

    def __new__(cls, clientCredentials) -> Self: # Not found arg types: {'clientCredentials': 'ClientCredentials'}
        """ __new__(cls: type, clientCredentials: ClientCredentials) """
        ...


class CommunicationObjectAbortedException(CommunicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CommunicationObjectAbortedException()
    CommunicationObjectAbortedException(message: str)
    CommunicationObjectAbortedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class CommunicationObjectFaultedException(CommunicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CommunicationObjectFaultedException()
    CommunicationObjectFaultedException(message: str)
    CommunicationObjectFaultedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class CommunicationState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CommunicationState, values: Closed (4), Closing (3), Created (0), Faulted (5), Opened (2), Opening (1) """
    Closed: CommunicationState = ...
    Closing: CommunicationState = ...
    Created: CommunicationState = ...
    Faulted: CommunicationState = ...
    Opened: CommunicationState = ...
    Opening: CommunicationState = ...
    value__ = ...


class ConcurrencyMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConcurrencyMode, values: Multiple (2), Reentrant (1), Single (0) """
    Multiple: ConcurrencyMode = ...
    Reentrant: ConcurrencyMode = ...
    Single: ConcurrencyMode = ...
    value__ = ...


class CorrelationActionMessageFilter(MessageFilter): # skipped bases: <type 'object'>
    """ CorrelationActionMessageFilter() """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: CorrelationActionMessageFilter) -> str
        Set: Action(self: CorrelationActionMessageFilter) = value
        """
        ...


    def Equals(self, other:object) -> bool:
        """ Equals(self: CorrelationActionMessageFilter, other: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CorrelationActionMessageFilter) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: CorrelationActionMessageFilter) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CorrelationQuery: # skipped bases: <type 'object'>, <type 'object'>
    """ CorrelationQuery() """
    @property
    def Select(self) -> MessageQuerySet:
        """
        Get: Select(self: CorrelationQuery) -> MessageQuerySet
        Set: Select(self: CorrelationQuery) = value
        """
        ...

    @property
    def SelectAdditional(self) -> Collection:
        """ Get: SelectAdditional(self: CorrelationQuery) -> Collection[MessageQuerySet] """
        ...

    @property
    def Where(self): # -> MessageFilter
        """
        Get: Where(self: CorrelationQuery) -> MessageFilter
        Set: Where(self: CorrelationQuery) = value
        """
        ...


    def Equals(self, other:object) -> bool:
        """ Equals(self: CorrelationQuery, other: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CorrelationQuery) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DataContractFormatAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DataContractFormatAttribute() """
    @property
    def Style(self): # -> OperationFormatStyle
        """
        Get: Style(self: DataContractFormatAttribute) -> OperationFormatStyle
        Set: Style(self: DataContractFormatAttribute) = value
        """
        ...



class DeadLetterQueue(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DeadLetterQueue, values: Custom (2), None (0), System (1) """
    Custom: DeadLetterQueue = ...
    System: DeadLetterQueue = ...
    value__ = ...


class DeliveryRequirementsAttribute(Attribute, IContractBehaviorAttribute, IContractBehavior): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DeliveryRequirementsAttribute() """
    @property
    def QueuedDeliveryRequirements(self): # -> QueuedDeliveryRequirementsMode
        """
        Get: QueuedDeliveryRequirements(self: DeliveryRequirementsAttribute) -> QueuedDeliveryRequirementsMode
        Set: QueuedDeliveryRequirements(self: DeliveryRequirementsAttribute) = value
        """
        ...

    @property
    def RequireOrderedDelivery(self) -> bool:
        """
        Get: RequireOrderedDelivery(self: DeliveryRequirementsAttribute) -> bool
        Set: RequireOrderedDelivery(self: DeliveryRequirementsAttribute) = value
        """
        ...



class EndpointIdentity: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IdentityClaim(self) -> Claim:
        """ Get: IdentityClaim(self: EndpointIdentity) -> Claim """
        ...


    @staticmethod
    def CreateDnsIdentity(dnsName:str) -> EndpointIdentity:
        """ CreateDnsIdentity(dnsName: str) -> EndpointIdentity """
        ...

    @staticmethod
    def CreateIdentity(identity:Claim) -> EndpointIdentity:
        """ CreateIdentity(identity: Claim) -> EndpointIdentity """
        ...

    @staticmethod
    def CreateRsaIdentity(*__args:str) -> EndpointIdentity:
        """
        CreateRsaIdentity(publicKey: str) -> EndpointIdentity
        CreateRsaIdentity(certificate: X509Certificate2) -> EndpointIdentity
        """
        ...

    @staticmethod
    def CreateSpnIdentity(spnName:str) -> EndpointIdentity:
        """ CreateSpnIdentity(spnName: str) -> EndpointIdentity """
        ...

    @staticmethod
    def CreateUpnIdentity(upnName:str) -> EndpointIdentity:
        """ CreateUpnIdentity(upnName: str) -> EndpointIdentity """
        ...

    @staticmethod
    def CreateX509CertificateIdentity(*__args:X509Certificate2) -> EndpointIdentity:
        """
        CreateX509CertificateIdentity(certificate: X509Certificate2) -> EndpointIdentity
        CreateX509CertificateIdentity(primaryCertificate: X509Certificate2, supportingCertificates: X509Certificate2Collection) -> EndpointIdentity
        """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: EndpointIdentity, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: EndpointIdentity) -> int """
        ...

    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: EndpointIdentity, identityClaim: Claim)Initialize(self: EndpointIdentity, identityClaim: Claim, claimComparer: IEqualityComparer[Claim]) """
        ...

    def ToString(self) -> str:
        """ ToString(self: EndpointIdentity) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DnsEndpointIdentity(EndpointIdentity): # skipped bases: <type 'object'>
    """
    DnsEndpointIdentity(dnsName: str)
    DnsEndpointIdentity(identity: Claim)
    """
    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, dnsName: str)
        __new__(cls: type, identity: Claim)
        """
        ...


class ICommunicationObject: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def State(self) -> CommunicationState:
        """ Get: State(self: ICommunicationObject) -> CommunicationState """
        ...


    def Abort(self): # -> 
        """ Abort(self: ICommunicationObject) """
        ...

    def BeginClose(self, *__args) -> IAsyncResult:
        """
        BeginClose(self: ICommunicationObject, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginClose(self: ICommunicationObject, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginOpen(self, *__args) -> IAsyncResult:
        """
        BeginOpen(self: ICommunicationObject, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginOpen(self: ICommunicationObject, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def Close(self, timeout:TimeSpan = ...): # -> 
        """ Close(self: ICommunicationObject)Close(self: ICommunicationObject, timeout: TimeSpan) """
        ...

    def EndClose(self, result:IAsyncResult): # -> 
        """ EndClose(self: ICommunicationObject, result: IAsyncResult) """
        ...

    def EndOpen(self, result:IAsyncResult): # -> 
        """ EndOpen(self: ICommunicationObject, result: IAsyncResult) """
        ...

    def Open(self, timeout:TimeSpan = ...): # -> 
        """ Open(self: ICommunicationObject)Open(self: ICommunicationObject, timeout: TimeSpan) """
        ...

    Closed = ...
    Closing = ...
    Faulted = ...
    Opened = ...
    Opening = ...


class DuplexChannelFactory(ChannelFactory): # skipped bases: <type 'IDisposable'>, <type 'IChannelFactory'>, <type 'ICommunicationObject'>, <type 'IChannelFactory[TChannel]'>, <type 'object'>
    """
    DuplexChannelFactory[TChannel](callbackInstanceType: Type)
    DuplexChannelFactory[TChannel](callbackInstanceType: Type, binding: Binding, remoteAddress: str)
    DuplexChannelFactory[TChannel](callbackInstanceType: Type, binding: Binding, remoteAddress: EndpointAddress)
    DuplexChannelFactory[TChannel](callbackInstanceType: Type, binding: Binding)
    DuplexChannelFactory[TChannel](callbackInstanceType: Type, endpointConfigurationName: str, remoteAddress: EndpointAddress)
    DuplexChannelFactory[TChannel](callbackInstanceType: Type, endpointConfigurationName: str)
    DuplexChannelFactory[TChannel](callbackInstanceType: Type, endpoint: ServiceEndpoint)
    DuplexChannelFactory[TChannel](callbackInstance: InstanceContext)
    DuplexChannelFactory[TChannel](callbackInstance: InstanceContext, binding: Binding, remoteAddress: str)
    DuplexChannelFactory[TChannel](callbackInstance: InstanceContext, binding: Binding, remoteAddress: EndpointAddress)
    DuplexChannelFactory[TChannel](callbackInstance: InstanceContext, binding: Binding)
    DuplexChannelFactory[TChannel](callbackInstance: InstanceContext, endpointConfigurationName: str, remoteAddress: EndpointAddress)
    DuplexChannelFactory[TChannel](callbackInstance: InstanceContext, endpointConfigurationName: str)
    DuplexChannelFactory[TChannel](callbackInstance: InstanceContext, endpoint: ServiceEndpoint)
    DuplexChannelFactory[TChannel](callbackObject: object)
    DuplexChannelFactory[TChannel](callbackObject: object, endpointConfigurationName: str)
    DuplexChannelFactory[TChannel](callbackObject: object, endpointConfigurationName: str, remoteAddress: EndpointAddress)
    DuplexChannelFactory[TChannel](callbackObject: object, binding: Binding)
    DuplexChannelFactory[TChannel](callbackObject: object, binding: Binding, remoteAddress: str)
    DuplexChannelFactory[TChannel](callbackObject: object, binding: Binding, remoteAddress: EndpointAddress)
    DuplexChannelFactory[TChannel](callbackObject: object, endpoint: ServiceEndpoint)
    """
    pass

class DuplexClientBase(ClientBase): # skipped bases: <type 'IDisposable'>, <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    @property
    def InnerDuplexChannel(self): # -> IDuplexContextChannel
        """ Get: InnerDuplexChannel(self: DuplexClientBase[TChannel]) -> IDuplexContextChannel """
        ...



class Endpoint: # skipped bases: <type 'object'>, <type 'object'>
    """ Endpoint() """
    @property
    def AddressUri(self) -> Uri:
        """
        Get: AddressUri(self: Endpoint) -> Uri
        Set: AddressUri(self: Endpoint) = value
        """
        ...

    @property
    def BehaviorConfigurationName(self) -> str:
        """
        Get: BehaviorConfigurationName(self: Endpoint) -> str
        Set: BehaviorConfigurationName(self: Endpoint) = value
        """
        ...

    @property
    def Binding(self) -> Binding:
        """
        Get: Binding(self: Endpoint) -> Binding
        Set: Binding(self: Endpoint) = value
        """
        ...

    @property
    def Headers(self) -> Collection:
        """ Get: Headers(self: Endpoint) -> Collection[AddressHeader] """
        ...

    @property
    def Identity(self) -> EndpointIdentity:
        """
        Get: Identity(self: Endpoint) -> EndpointIdentity
        Set: Identity(self: Endpoint) = value
        """
        ...

    @property
    def ListenUri(self) -> Uri:
        """
        Get: ListenUri(self: Endpoint) -> Uri
        Set: ListenUri(self: Endpoint) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Endpoint) -> str
        Set: Name(self: Endpoint) = value
        """
        ...

    @property
    def ServiceContractName(self) -> XName:
        """
        Get: ServiceContractName(self: Endpoint) -> XName
        Set: ServiceContractName(self: Endpoint) = value
        """
        ...


    def GetAddress(self, host = ...): # -> EndpointAddress # Not found arg types: {'host': 'ServiceHostBase'}
        """
        GetAddress(self: Endpoint) -> EndpointAddress
        GetAddress(self: Endpoint, host: ServiceHostBase) -> EndpointAddress
        """
        ...


class EndpointAddress: # skipped bases: <type 'object'>, <type 'object'>
    """
    EndpointAddress(uri: str)
    EndpointAddress(uri: Uri, *addressHeaders: Array[AddressHeader])
    EndpointAddress(uri: Uri, identity: EndpointIdentity, *addressHeaders: Array[AddressHeader])
    EndpointAddress(uri: Uri, identity: EndpointIdentity, headers: AddressHeaderCollection)
    EndpointAddress(uri: Uri, identity: EndpointIdentity, headers: AddressHeaderCollection, metadataReader: XmlDictionaryReader, extensionReader: XmlDictionaryReader)
    """
    @property
    def AnonymousUri(self) -> Uri:
        """ Get: AnonymousUri() -> Uri """
        ...

    @property
    def Headers(self): # -> AddressHeaderCollection
        """ Get: Headers(self: EndpointAddress) -> AddressHeaderCollection """
        ...

    @property
    def Identity(self) -> EndpointIdentity:
        """ Get: Identity(self: EndpointAddress) -> EndpointIdentity """
        ...

    @property
    def IsAnonymous(self) -> bool:
        """ Get: IsAnonymous(self: EndpointAddress) -> bool """
        ...

    @property
    def IsNone(self) -> bool:
        """ Get: IsNone(self: EndpointAddress) -> bool """
        ...

    @property
    def NoneUri(self) -> Uri:
        """ Get: NoneUri() -> Uri """
        ...

    @property
    def Uri(self) -> Uri:
        """ Get: Uri(self: EndpointAddress) -> Uri """
        ...


    def ApplyTo(self, message:Message): # -> 
        """ ApplyTo(self: EndpointAddress, message: Message) """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: EndpointAddress, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: EndpointAddress) -> int """
        ...

    def GetReaderAtExtensions(self) -> XmlDictionaryReader:
        """ GetReaderAtExtensions(self: EndpointAddress) -> XmlDictionaryReader """
        ...

    def GetReaderAtMetadata(self) -> XmlDictionaryReader:
        """ GetReaderAtMetadata(self: EndpointAddress) -> XmlDictionaryReader """
        ...

    @staticmethod
    def ReadFrom(*__args:XmlDictionaryReader) -> EndpointAddress:
        """
        ReadFrom(reader: XmlDictionaryReader) -> EndpointAddress
        ReadFrom(reader: XmlDictionaryReader, localName: XmlDictionaryString, ns: XmlDictionaryString) -> EndpointAddress
        ReadFrom(addressingVersion: AddressingVersion, reader: XmlReader) -> EndpointAddress
        ReadFrom(addressingVersion: AddressingVersion, reader: XmlReader, localName: str, ns: str) -> EndpointAddress
        ReadFrom(addressingVersion: AddressingVersion, reader: XmlDictionaryReader, localName: XmlDictionaryString, ns: XmlDictionaryString) -> EndpointAddress
        ReadFrom(addressingVersion: AddressingVersion, reader: XmlDictionaryReader) -> EndpointAddress
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: EndpointAddress) -> str """
        ...

    def WriteContentsTo(self, addressingVersion, writer:XmlWriter): # ->  # Not found arg types: {'addressingVersion': 'AddressingVersion'}
        """ WriteContentsTo(self: EndpointAddress, addressingVersion: AddressingVersion, writer: XmlWriter)WriteContentsTo(self: EndpointAddress, addressingVersion: AddressingVersion, writer: XmlDictionaryWriter) """
        ...

    def WriteTo(self, addressingVersion, writer:XmlDictionaryWriter, localName:XmlDictionaryString = ..., ns:XmlDictionaryString = ...): # ->  # Not found arg types: {'addressingVersion': 'AddressingVersion'}
        """ WriteTo(self: EndpointAddress, addressingVersion: AddressingVersion, writer: XmlDictionaryWriter)WriteTo(self: EndpointAddress, addressingVersion: AddressingVersion, writer: XmlDictionaryWriter, localName: XmlDictionaryString, ns: XmlDictionaryString)WriteTo(self: EndpointAddress, addressingVersion: AddressingVersion, writer: XmlWriter)WriteTo(self: EndpointAddress, addressingVersion: AddressingVersion, writer: XmlWriter, localName: str, ns: str) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class EndpointAddress10(IXmlSerializable): # skipped bases: <type 'object'>
    """ no doc """
    @staticmethod
    def FromEndpointAddress(address:EndpointAddress) -> EndpointAddress10:
        """ FromEndpointAddress(address: EndpointAddress) -> EndpointAddress10 """
        ...

    def ToEndpointAddress(self) -> EndpointAddress:
        """ ToEndpointAddress(self: EndpointAddress10) -> EndpointAddress """
        ...


class EndpointAddressAugust2004(IXmlSerializable): # skipped bases: <type 'object'>
    """ no doc """
    @staticmethod
    def FromEndpointAddress(address:EndpointAddress) -> EndpointAddressAugust2004:
        """ FromEndpointAddress(address: EndpointAddress) -> EndpointAddressAugust2004 """
        ...

    def ToEndpointAddress(self) -> EndpointAddress:
        """ ToEndpointAddress(self: EndpointAddressAugust2004) -> EndpointAddress """
        ...


class EndpointAddressBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """
    EndpointAddressBuilder()
    EndpointAddressBuilder(address: EndpointAddress)
    """
    @property
    def Headers(self) -> Collection:
        """ Get: Headers(self: EndpointAddressBuilder) -> Collection[AddressHeader] """
        ...

    @property
    def Identity(self) -> EndpointIdentity:
        """
        Get: Identity(self: EndpointAddressBuilder) -> EndpointIdentity
        Set: Identity(self: EndpointAddressBuilder) = value
        """
        ...

    @property
    def Uri(self) -> Uri:
        """
        Get: Uri(self: EndpointAddressBuilder) -> Uri
        Set: Uri(self: EndpointAddressBuilder) = value
        """
        ...


    def GetReaderAtExtensions(self) -> XmlDictionaryReader:
        """ GetReaderAtExtensions(self: EndpointAddressBuilder) -> XmlDictionaryReader """
        ...

    def GetReaderAtMetadata(self) -> XmlDictionaryReader:
        """ GetReaderAtMetadata(self: EndpointAddressBuilder) -> XmlDictionaryReader """
        ...

    def SetExtensionReader(self, reader:XmlDictionaryReader): # -> 
        """ SetExtensionReader(self: EndpointAddressBuilder, reader: XmlDictionaryReader) """
        ...

    def SetMetadataReader(self, reader:XmlDictionaryReader): # -> 
        """ SetMetadataReader(self: EndpointAddressBuilder, reader: XmlDictionaryReader) """
        ...

    def ToEndpointAddress(self) -> EndpointAddress:
        """ ToEndpointAddress(self: EndpointAddressBuilder) -> EndpointAddress """
        ...


class EndpointIdentityExtension(MarkupExtension): # skipped bases: <type 'object'>
    """
    EndpointIdentityExtension()
    EndpointIdentityExtension(identity: EndpointIdentity)
    """
    @property
    def ClaimResource(self) -> object:
        """
        Get: ClaimResource(self: EndpointIdentityExtension) -> object
        Set: ClaimResource(self: EndpointIdentityExtension) = value
        """
        ...

    @property
    def ClaimRight(self) -> str:
        """
        Get: ClaimRight(self: EndpointIdentityExtension) -> str
        Set: ClaimRight(self: EndpointIdentityExtension) = value
        """
        ...

    @property
    def ClaimType(self) -> str:
        """
        Get: ClaimType(self: EndpointIdentityExtension) -> str
        Set: ClaimType(self: EndpointIdentityExtension) = value
        """
        ...


    def __new__(cls, identity:EndpointIdentity = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, identity: EndpointIdentity)
        """
        ...


class EndpointNotFoundException(CommunicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    EndpointNotFoundException()
    EndpointNotFoundException(message: str)
    EndpointNotFoundException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class EnvelopeVersion: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def NextDestinationActorValue(self) -> str:
        """ Get: NextDestinationActorValue(self: EnvelopeVersion) -> str """
        ...

    @property
    def Soap11(self) -> EnvelopeVersion:
        """ Get: Soap11() -> EnvelopeVersion """
        ...

    @property
    def Soap12(self) -> EnvelopeVersion:
        """ Get: Soap12() -> EnvelopeVersion """
        ...


    def GetUltimateDestinationActorValues(self) -> Array:
        """ GetUltimateDestinationActorValues(self: EnvelopeVersion) -> Array[str] """
        ...

    def ToString(self) -> str:
        """ ToString(self: EnvelopeVersion) -> str """
        ...



class ExceptionDetail: # skipped bases: <type 'object'>, <type 'object'>
    """ ExceptionDetail(exception: Exception) """
    @property
    def HelpLink(self) -> str:
        """
        Get: HelpLink(self: ExceptionDetail) -> str
        Set: HelpLink(self: ExceptionDetail) = value
        """
        ...

    @property
    def InnerException(self) -> ExceptionDetail:
        """
        Get: InnerException(self: ExceptionDetail) -> ExceptionDetail
        Set: InnerException(self: ExceptionDetail) = value
        """
        ...

    @property
    def Message(self) -> str:
        """
        Get: Message(self: ExceptionDetail) -> str
        Set: Message(self: ExceptionDetail) = value
        """
        ...

    @property
    def StackTrace(self) -> str:
        """
        Get: StackTrace(self: ExceptionDetail) -> str
        Set: StackTrace(self: ExceptionDetail) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: ExceptionDetail) -> str
        Set: Type(self: ExceptionDetail) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: ExceptionDetail) -> str """
        ...


class ExceptionMapper: # skipped bases: <type 'object'>, <type 'object'>
    """ ExceptionMapper() """
    def FromException(self, ex:Exception, soapNamespace:str = ..., trustNamespace:str = ...): # -> FaultException
        """
        FromException(self: ExceptionMapper, ex: Exception) -> FaultException
        FromException(self: ExceptionMapper, ex: Exception, soapNamespace: str, trustNamespace: str) -> FaultException
        """
        ...

    def HandleSecurityTokenProcessingException(self, ex:Exception) -> bool:
        """ HandleSecurityTokenProcessingException(self: ExceptionMapper, ex: Exception) -> bool """
        ...


class ExtensionCollection(SynchronizedCollection, IExtensionCollection): # skipped bases: <type 'IEnumerable[IExtension[T]]'>, <type 'ICollection[IExtension[T]]'>, <type 'IList'>, <type 'IEnumerable'>, <type 'IList[IExtension[T]]'>, <type 'ICollection'>, <type 'object'>
    """
    ExtensionCollection[T](owner: T)
    ExtensionCollection[T](owner: T, syncRoot: object)
    """
    pass

class FaultCode: # skipped bases: <type 'object'>, <type 'object'>
    """
    FaultCode(name: str)
    FaultCode(name: str, subCode: FaultCode)
    FaultCode(name: str, ns: str)
    FaultCode(name: str, ns: str, subCode: FaultCode)
    """
    @property
    def IsPredefinedFault(self) -> bool:
        """ Get: IsPredefinedFault(self: FaultCode) -> bool """
        ...

    @property
    def IsReceiverFault(self) -> bool:
        """ Get: IsReceiverFault(self: FaultCode) -> bool """
        ...

    @property
    def IsSenderFault(self) -> bool:
        """ Get: IsSenderFault(self: FaultCode) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: FaultCode) -> str """
        ...

    @property
    def Namespace(self) -> str:
        """ Get: Namespace(self: FaultCode) -> str """
        ...

    @property
    def SubCode(self) -> FaultCode:
        """ Get: SubCode(self: FaultCode) -> FaultCode """
        ...


    @staticmethod
    def CreateReceiverFaultCode(*__args:FaultCode) -> FaultCode:
        """
        CreateReceiverFaultCode(name: str, ns: str) -> FaultCode
        CreateReceiverFaultCode(subCode: FaultCode) -> FaultCode
        """
        ...

    @staticmethod
    def CreateSenderFaultCode(*__args:FaultCode) -> FaultCode:
        """
        CreateSenderFaultCode(subCode: FaultCode) -> FaultCode
        CreateSenderFaultCode(name: str, ns: str) -> FaultCode
        """
        ...


class FaultContractAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ FaultContractAttribute(detailType: Type) """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: FaultContractAttribute) -> str
        Set: Action(self: FaultContractAttribute) = value
        """
        ...

    @property
    def DetailType(self) -> Type:
        """ Get: DetailType(self: FaultContractAttribute) -> Type """
        ...

    @property
    def HasProtectionLevel(self) -> bool:
        """ Get: HasProtectionLevel(self: FaultContractAttribute) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: FaultContractAttribute) -> str
        Set: Name(self: FaultContractAttribute) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: FaultContractAttribute) -> str
        Set: Namespace(self: FaultContractAttribute) = value
        """
        ...

    @property
    def ProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ProtectionLevel(self: FaultContractAttribute) -> ProtectionLevel
        Set: ProtectionLevel(self: FaultContractAttribute) = value
        """
        ...


    def __new__(cls, detailType:Type) -> Self:
        """ __new__(cls: type, detailType: Type) """
        ...


class FaultException: # skipped bases: <type 'object'>
    """
    FaultException()
    FaultException(reason: str)
    FaultException(reason: FaultReason)
    FaultException(reason: str, code: FaultCode)
    FaultException(reason: FaultReason, code: FaultCode)
    FaultException(reason: str, code: FaultCode, action: str)
    FaultException(reason: FaultReason, code: FaultCode, action: str)
    FaultException(fault: MessageFault)
    FaultException(fault: MessageFault, action: str)
    """
    @property
    def Action(self) -> str:
        """ Get: Action(self: FaultException) -> str """
        ...

    @property
    def Code(self) -> FaultCode:
        """ Get: Code(self: FaultException) -> FaultCode """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: FaultException) -> str """
        ...

    @property
    def Reason(self): # -> FaultReason
        """ Get: Reason(self: FaultException) -> FaultReason """
        ...


    @staticmethod
    def CreateFault(messageFault, *__args:Array) -> FaultException: # Not found arg types: {'messageFault': 'MessageFault'}
        """
        CreateFault(messageFault: MessageFault, *faultDetailTypes: Array[Type]) -> FaultException
        CreateFault(messageFault: MessageFault, action: str, *faultDetailTypes: Array[Type]) -> FaultException
        """
        ...

    def CreateMessageFault(self): # -> MessageFault
        """ CreateMessageFault(self: FaultException) -> MessageFault """
        ...

    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: FaultException, info: SerializationInfo, context: StreamingContext) """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, reason: str)
        __new__(cls: type, reason: FaultReason)
        __new__(cls: type, reason: str, code: FaultCode)
        __new__(cls: type, reason: FaultReason, code: FaultCode)
        __new__(cls: type, reason: str, code: FaultCode, action: str)
        __new__(cls: type, reason: FaultReason, code: FaultCode, action: str)
        __new__(cls: type, fault: MessageFault)
        __new__(cls: type, fault: MessageFault, action: str)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        ...

    def __reduce_ex__(self, *args): #cannot find CLR method
        ...

    def __str__(self, *args): #cannot find CLR method
        ...

    SerializeObjectState = ...


class FaultImportOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ FaultImportOptions() """
    @property
    def UseMessageFormat(self) -> bool:
        """
        Get: UseMessageFormat(self: FaultImportOptions) -> bool
        Set: UseMessageFormat(self: FaultImportOptions) = value
        """
        ...



class FaultReason: # skipped bases: <type 'object'>, <type 'object'>
    """
    FaultReason(translation: FaultReasonText)
    FaultReason(text: str)
    FaultReason(translations: IEnumerable[FaultReasonText])
    """
    @property
    def Translations(self) -> SynchronizedReadOnlyCollection:
        """ Get: Translations(self: FaultReason) -> SynchronizedReadOnlyCollection[FaultReasonText] """
        ...


    def GetMatchingTranslation(self, cultureInfo:CultureInfo = ...): # -> FaultReasonText
        """
        GetMatchingTranslation(self: FaultReason) -> FaultReasonText
        GetMatchingTranslation(self: FaultReason, cultureInfo: CultureInfo) -> FaultReasonText
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: FaultReason) -> str """
        ...


class FaultReasonText: # skipped bases: <type 'object'>, <type 'object'>
    """
    FaultReasonText(text: str)
    FaultReasonText(text: str, xmlLang: str)
    FaultReasonText(text: str, cultureInfo: CultureInfo)
    """
    @property
    def Text(self) -> str:
        """ Get: Text(self: FaultReasonText) -> str """
        ...

    @property
    def XmlLang(self) -> str:
        """ Get: XmlLang(self: FaultReasonText) -> str """
        ...


    def Matches(self, cultureInfo:CultureInfo) -> bool:
        """ Matches(self: FaultReasonText, cultureInfo: CultureInfo) -> bool """
        ...


class FederatedMessageSecurityOverHttp: # skipped bases: <type 'object'>, <type 'object'>
    """ FederatedMessageSecurityOverHttp() """
    @property
    def AlgorithmSuite(self) -> SecurityAlgorithmSuite:
        """
        Get: AlgorithmSuite(self: FederatedMessageSecurityOverHttp) -> SecurityAlgorithmSuite
        Set: AlgorithmSuite(self: FederatedMessageSecurityOverHttp) = value
        """
        ...

    @property
    def ClaimTypeRequirements(self) -> Collection:
        """ Get: ClaimTypeRequirements(self: FederatedMessageSecurityOverHttp) -> Collection[ClaimTypeRequirement] """
        ...

    @property
    def EstablishSecurityContext(self) -> bool:
        """
        Get: EstablishSecurityContext(self: FederatedMessageSecurityOverHttp) -> bool
        Set: EstablishSecurityContext(self: FederatedMessageSecurityOverHttp) = value
        """
        ...

    @property
    def IssuedKeyType(self) -> SecurityKeyType:
        """
        Get: IssuedKeyType(self: FederatedMessageSecurityOverHttp) -> SecurityKeyType
        Set: IssuedKeyType(self: FederatedMessageSecurityOverHttp) = value
        """
        ...

    @property
    def IssuedTokenType(self) -> str:
        """
        Get: IssuedTokenType(self: FederatedMessageSecurityOverHttp) -> str
        Set: IssuedTokenType(self: FederatedMessageSecurityOverHttp) = value
        """
        ...

    @property
    def IssuerAddress(self) -> EndpointAddress:
        """
        Get: IssuerAddress(self: FederatedMessageSecurityOverHttp) -> EndpointAddress
        Set: IssuerAddress(self: FederatedMessageSecurityOverHttp) = value
        """
        ...

    @property
    def IssuerBinding(self) -> Binding:
        """
        Get: IssuerBinding(self: FederatedMessageSecurityOverHttp) -> Binding
        Set: IssuerBinding(self: FederatedMessageSecurityOverHttp) = value
        """
        ...

    @property
    def IssuerMetadataAddress(self) -> EndpointAddress:
        """
        Get: IssuerMetadataAddress(self: FederatedMessageSecurityOverHttp) -> EndpointAddress
        Set: IssuerMetadataAddress(self: FederatedMessageSecurityOverHttp) = value
        """
        ...

    @property
    def NegotiateServiceCredential(self) -> bool:
        """
        Get: NegotiateServiceCredential(self: FederatedMessageSecurityOverHttp) -> bool
        Set: NegotiateServiceCredential(self: FederatedMessageSecurityOverHttp) = value
        """
        ...

    @property
    def TokenRequestParameters(self) -> Collection:
        """ Get: TokenRequestParameters(self: FederatedMessageSecurityOverHttp) -> Collection[XmlElement] """
        ...


    def ShouldSerializeAlgorithmSuite(self) -> bool:
        """ ShouldSerializeAlgorithmSuite(self: FederatedMessageSecurityOverHttp) -> bool """
        ...

    def ShouldSerializeClaimTypeRequirements(self) -> bool:
        """ ShouldSerializeClaimTypeRequirements(self: FederatedMessageSecurityOverHttp) -> bool """
        ...

    def ShouldSerializeEstablishSecurityContext(self) -> bool:
        """ ShouldSerializeEstablishSecurityContext(self: FederatedMessageSecurityOverHttp) -> bool """
        ...

    def ShouldSerializeIssuedKeyType(self) -> bool:
        """ ShouldSerializeIssuedKeyType(self: FederatedMessageSecurityOverHttp) -> bool """
        ...

    def ShouldSerializeNegotiateServiceCredential(self) -> bool:
        """ ShouldSerializeNegotiateServiceCredential(self: FederatedMessageSecurityOverHttp) -> bool """
        ...

    def ShouldSerializeTokenRequestParameters(self) -> bool:
        """ ShouldSerializeTokenRequestParameters(self: FederatedMessageSecurityOverHttp) -> bool """
        ...


class HostNameComparisonMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HostNameComparisonMode, values: Exact (1), StrongWildcard (0), WeakWildcard (2) """
    Exact: HostNameComparisonMode = ...
    StrongWildcard: HostNameComparisonMode = ...
    value__ = ...
    WeakWildcard: HostNameComparisonMode = ...


class HttpClientCredentialType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HttpClientCredentialType, values: Basic (1), Certificate (5), Digest (2), InheritedFromHost (6), None (0), Ntlm (3), Windows (4) """
    Basic: HttpClientCredentialType = ...
    Certificate: HttpClientCredentialType = ...
    Digest: HttpClientCredentialType = ...
    InheritedFromHost: HttpClientCredentialType = ...
    Ntlm: HttpClientCredentialType = ...
    value__ = ...
    Windows: HttpClientCredentialType = ...


class HttpProxyCredentialType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HttpProxyCredentialType, values: Basic (1), Digest (2), None (0), Ntlm (3), Windows (4) """
    Basic: HttpProxyCredentialType = ...
    Digest: HttpProxyCredentialType = ...
    Ntlm: HttpProxyCredentialType = ...
    value__ = ...
    Windows: HttpProxyCredentialType = ...


class HttpTransportSecurity: # skipped bases: <type 'object'>, <type 'object'>
    """ HttpTransportSecurity() """
    @property
    def ClientCredentialType(self) -> HttpClientCredentialType:
        """
        Get: ClientCredentialType(self: HttpTransportSecurity) -> HttpClientCredentialType
        Set: ClientCredentialType(self: HttpTransportSecurity) = value
        """
        ...

    @property
    def ExtendedProtectionPolicy(self) -> ExtendedProtectionPolicy:
        """
        Get: ExtendedProtectionPolicy(self: HttpTransportSecurity) -> ExtendedProtectionPolicy
        Set: ExtendedProtectionPolicy(self: HttpTransportSecurity) = value
        """
        ...

    @property
    def ProxyCredentialType(self) -> HttpProxyCredentialType:
        """
        Get: ProxyCredentialType(self: HttpTransportSecurity) -> HttpProxyCredentialType
        Set: ProxyCredentialType(self: HttpTransportSecurity) = value
        """
        ...

    @property
    def Realm(self) -> str:
        """
        Get: Realm(self: HttpTransportSecurity) -> str
        Set: Realm(self: HttpTransportSecurity) = value
        """
        ...


    def ShouldSerializeClientCredentialType(self) -> bool:
        """ ShouldSerializeClientCredentialType(self: HttpTransportSecurity) -> bool """
        ...

    def ShouldSerializeExtendedProtectionPolicy(self) -> bool:
        """ ShouldSerializeExtendedProtectionPolicy(self: HttpTransportSecurity) -> bool """
        ...

    def ShouldSerializeProxyCredentialType(self) -> bool:
        """ ShouldSerializeProxyCredentialType(self: HttpTransportSecurity) -> bool """
        ...

    def ShouldSerializeRealm(self) -> bool:
        """ ShouldSerializeRealm(self: HttpTransportSecurity) -> bool """
        ...


class IContextChannel(IChannel, IExtensibleObject): # skipped bases: <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    @property
    def AllowOutputBatching(self) -> bool:
        """
        Get: AllowOutputBatching(self: IContextChannel) -> bool
        Set: AllowOutputBatching(self: IContextChannel) = value
        """
        ...

    @property
    def InputSession(self): # -> IInputSession
        """ Get: InputSession(self: IContextChannel) -> IInputSession """
        ...

    @property
    def LocalAddress(self) -> EndpointAddress:
        """ Get: LocalAddress(self: IContextChannel) -> EndpointAddress """
        ...

    @property
    def OperationTimeout(self) -> TimeSpan:
        """
        Get: OperationTimeout(self: IContextChannel) -> TimeSpan
        Set: OperationTimeout(self: IContextChannel) = value
        """
        ...

    @property
    def OutputSession(self): # -> IOutputSession
        """ Get: OutputSession(self: IContextChannel) -> IOutputSession """
        ...

    @property
    def RemoteAddress(self) -> EndpointAddress:
        """ Get: RemoteAddress(self: IContextChannel) -> EndpointAddress """
        ...

    @property
    def SessionId(self) -> str:
        """ Get: SessionId(self: IContextChannel) -> str """
        ...



class IClientChannel(IContextChannel, IDisposable): # skipped bases: <type 'IChannel'>, <type 'ICommunicationObject'>, <type 'IExtensibleObject[IContextChannel]'>, <type 'object'>
    """ no doc """
    @property
    def AllowInitializationUI(self) -> bool:
        """
        Get: AllowInitializationUI(self: IClientChannel) -> bool
        Set: AllowInitializationUI(self: IClientChannel) = value
        """
        ...

    @property
    def DidInteractiveInitialization(self) -> bool:
        """ Get: DidInteractiveInitialization(self: IClientChannel) -> bool """
        ...

    @property
    def Via(self) -> Uri:
        """ Get: Via(self: IClientChannel) -> Uri """
        ...


    def BeginDisplayInitializationUI(self, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginDisplayInitializationUI(self: IClientChannel, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def DisplayInitializationUI(self): # -> 
        """ DisplayInitializationUI(self: IClientChannel) """
        ...

    def EndDisplayInitializationUI(self, result:IAsyncResult): # -> 
        """ EndDisplayInitializationUI(self: IClientChannel, result: IAsyncResult) """
        ...

    UnknownMessageReceived = ...


class IDuplexContextChannel(IContextChannel): # skipped bases: <type 'IChannel'>, <type 'ICommunicationObject'>, <type 'IExtensibleObject[IContextChannel]'>, <type 'object'>
    """ no doc """
    @property
    def AutomaticInputSessionShutdown(self) -> bool:
        """
        Get: AutomaticInputSessionShutdown(self: IDuplexContextChannel) -> bool
        Set: AutomaticInputSessionShutdown(self: IDuplexContextChannel) = value
        """
        ...

    @property
    def CallbackInstance(self): # -> InstanceContext
        """
        Get: CallbackInstance(self: IDuplexContextChannel) -> InstanceContext
        Set: CallbackInstance(self: IDuplexContextChannel) = value
        """
        ...


    def BeginCloseOutputSession(self, timeout:TimeSpan, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginCloseOutputSession(self: IDuplexContextChannel, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def CloseOutputSession(self, timeout:TimeSpan): # -> 
        """ CloseOutputSession(self: IDuplexContextChannel, timeout: TimeSpan) """
        ...

    def EndCloseOutputSession(self, result:IAsyncResult): # -> 
        """ EndCloseOutputSession(self: IDuplexContextChannel, result: IAsyncResult) """
        ...


class IExtensibleObject: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Extensions(self): # -> IExtensionCollection
        """ Get: Extensions(self: IExtensibleObject[T]) -> IExtensionCollection[T] """
        ...



class IExtension: # skipped bases: <type 'object'>
    """ no doc """
    def Attach(self, owner): # ->  # Not found arg types: {'owner': 'T'}
        """ Attach(self: IExtension[T], owner: T) """
        ...

    def Detach(self, owner): # ->  # Not found arg types: {'owner': 'T'}
        """ Detach(self: IExtension[T], owner: T) """
        ...


class IExtensionCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[IExtension[T]]'>, <type 'object'>
    """ no doc """
    def Find(self): # -> E
        """ Find[E](self: IExtensionCollection[T]) -> E """
        ...

    def FindAll(self) -> Collection:
        """ FindAll[E](self: IExtensionCollection[T]) -> Collection[E] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class ImpersonationOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ImpersonationOption, values: Allowed (1), NotAllowed (0), Required (2) """
    Allowed: ImpersonationOption = ...
    NotAllowed: ImpersonationOption = ...
    Required: ImpersonationOption = ...
    value__ = ...


class InstanceContext(IExtensibleObject, CommunicationObject): # skipped bases: <type 'ICommunicationObject'>, <type 'object'>
    """
    InstanceContext(implementation: object)
    InstanceContext(host: ServiceHostBase, implementation: object)
    InstanceContext(host: ServiceHostBase)
    """
    @property
    def Host(self): # -> ServiceHostBase
        """ Get: Host(self: InstanceContext) -> ServiceHostBase """
        ...

    @property
    def IncomingChannels(self) -> ICollection:
        """ Get: IncomingChannels(self: InstanceContext) -> ICollection[IChannel] """
        ...

    @property
    def ManualFlowControlLimit(self) -> int:
        """
        Get: ManualFlowControlLimit(self: InstanceContext) -> int
        Set: ManualFlowControlLimit(self: InstanceContext) = value
        """
        ...

    @property
    def OutgoingChannels(self) -> ICollection:
        """ Get: OutgoingChannels(self: InstanceContext) -> ICollection[IChannel] """
        ...

    @property
    def SynchronizationContext(self) -> SynchronizationContext:
        """
        Get: SynchronizationContext(self: InstanceContext) -> SynchronizationContext
        Set: SynchronizationContext(self: InstanceContext) = value
        """
        ...


    def GetServiceInstance(self, message:Message = ...) -> object:
        """
        GetServiceInstance(self: InstanceContext, message: Message) -> object
        GetServiceInstance(self: InstanceContext) -> object
        """
        ...

    def IncrementManualFlowControlLimit(self, incrementBy:int) -> int:
        """ IncrementManualFlowControlLimit(self: InstanceContext, incrementBy: int) -> int """
        ...

    def ReleaseServiceInstance(self): # -> 
        """ ReleaseServiceInstance(self: InstanceContext) """
        ...


class InstanceContextMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InstanceContextMode, values: PerCall (1), PerSession (0), Single (2) """
    PerCall: InstanceContextMode = ...
    PerSession: InstanceContextMode = ...
    Single: InstanceContextMode = ...
    value__ = ...


class InvalidMessageContractException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidMessageContractException()
    InvalidMessageContractException(message: str)
    InvalidMessageContractException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class IOnlineStatus: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsOnline(self) -> bool:
        """ Get: IsOnline(self: IOnlineStatus) -> bool """
        ...


    Offline = ...
    Online = ...


class IServiceChannel(IContextChannel): # skipped bases: <type 'IChannel'>, <type 'ICommunicationObject'>, <type 'IExtensibleObject[IContextChannel]'>, <type 'object'>
    """ no doc """
    @property
    def ListenUri(self) -> Uri:
        """ Get: ListenUri(self: IServiceChannel) -> Uri """
        ...



class MessageContractMemberAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    @property
    def HasProtectionLevel(self) -> bool:
        """ Get: HasProtectionLevel(self: MessageContractMemberAttribute) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: MessageContractMemberAttribute) -> str
        Set: Name(self: MessageContractMemberAttribute) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: MessageContractMemberAttribute) -> str
        Set: Namespace(self: MessageContractMemberAttribute) = value
        """
        ...

    @property
    def ProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ProtectionLevel(self: MessageContractMemberAttribute) -> ProtectionLevel
        Set: ProtectionLevel(self: MessageContractMemberAttribute) = value
        """
        ...



class MessageBodyMemberAttribute(MessageContractMemberAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MessageBodyMemberAttribute() """
    @property
    def Order(self) -> int:
        """
        Get: Order(self: MessageBodyMemberAttribute) -> int
        Set: Order(self: MessageBodyMemberAttribute) = value
        """
        ...



class MessageContractAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MessageContractAttribute() """
    @property
    def HasProtectionLevel(self) -> bool:
        """ Get: HasProtectionLevel(self: MessageContractAttribute) -> bool """
        ...

    @property
    def IsWrapped(self) -> bool:
        """
        Get: IsWrapped(self: MessageContractAttribute) -> bool
        Set: IsWrapped(self: MessageContractAttribute) = value
        """
        ...

    @property
    def ProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ProtectionLevel(self: MessageContractAttribute) -> ProtectionLevel
        Set: ProtectionLevel(self: MessageContractAttribute) = value
        """
        ...

    @property
    def WrapperName(self) -> str:
        """
        Get: WrapperName(self: MessageContractAttribute) -> str
        Set: WrapperName(self: MessageContractAttribute) = value
        """
        ...

    @property
    def WrapperNamespace(self) -> str:
        """
        Get: WrapperNamespace(self: MessageContractAttribute) -> str
        Set: WrapperNamespace(self: MessageContractAttribute) = value
        """
        ...



class MessageCredentialType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MessageCredentialType, values: Certificate (3), IssuedToken (4), None (0), UserName (2), Windows (1) """
    Certificate: MessageCredentialType = ...
    IssuedToken: MessageCredentialType = ...
    UserName: MessageCredentialType = ...
    value__ = ...
    Windows: MessageCredentialType = ...


class MessageHeader: # skipped bases: <type 'object'>, <type 'object'>
    """
    MessageHeader[T]()
    MessageHeader[T](content: T)
    MessageHeader[T](content: T, mustUnderstand: bool, actor: str, relay: bool)
    """
    @property
    def Actor(self) -> str:
        """
        Get: Actor(self: MessageHeader[T]) -> str
        Set: Actor(self: MessageHeader[T]) = value
        """
        ...

    @property
    def Content(self): # -> T
        """
        Get: Content(self: MessageHeader[T]) -> T
        Set: Content(self: MessageHeader[T]) = value
        """
        ...

    @property
    def MustUnderstand(self) -> bool:
        """
        Get: MustUnderstand(self: MessageHeader[T]) -> bool
        Set: MustUnderstand(self: MessageHeader[T]) = value
        """
        ...

    @property
    def Relay(self) -> bool:
        """
        Get: Relay(self: MessageHeader[T]) -> bool
        Set: Relay(self: MessageHeader[T]) = value
        """
        ...


    def GetUntypedHeader(self, name:str, ns:str) -> MessageHeader:
        """ GetUntypedHeader(self: MessageHeader[T], name: str, ns: str) -> MessageHeader """
        ...


class MessageHeaderAttribute(MessageContractMemberAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MessageHeaderAttribute() """
    @property
    def Actor(self) -> str:
        """
        Get: Actor(self: MessageHeaderAttribute) -> str
        Set: Actor(self: MessageHeaderAttribute) = value
        """
        ...

    @property
    def MustUnderstand(self) -> bool:
        """
        Get: MustUnderstand(self: MessageHeaderAttribute) -> bool
        Set: MustUnderstand(self: MessageHeaderAttribute) = value
        """
        ...

    @property
    def Relay(self) -> bool:
        """
        Get: Relay(self: MessageHeaderAttribute) -> bool
        Set: Relay(self: MessageHeaderAttribute) = value
        """
        ...



class MessageHeaderArrayAttribute(MessageHeaderAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MessageHeaderArrayAttribute() """
    pass

class ProtocolException(CommunicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ProtocolException()
    ProtocolException(message: str)
    ProtocolException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class MessageHeaderException(ProtocolException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MessageHeaderException(message: str)
    MessageHeaderException(message: str, isDuplicate: bool)
    MessageHeaderException(message: str, innerException: Exception)
    MessageHeaderException(message: str, headerName: str, ns: str)
    MessageHeaderException(message: str, headerName: str, ns: str, isDuplicate: bool)
    MessageHeaderException(message: str, headerName: str, ns: str, innerException: Exception)
    MessageHeaderException(message: str, headerName: str, ns: str, isDuplicate: bool, innerException: Exception)
    MessageHeaderException()
    """
    @property
    def HeaderName(self) -> str:
        """ Get: HeaderName(self: MessageHeaderException) -> str """
        ...

    @property
    def HeaderNamespace(self) -> str:
        """ Get: HeaderNamespace(self: MessageHeaderException) -> str """
        ...

    @property
    def IsDuplicate(self) -> bool:
        """ Get: IsDuplicate(self: MessageHeaderException) -> bool """
        ...


    SerializeObjectState = ...


class MessageParameterAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MessageParameterAttribute() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: MessageParameterAttribute) -> str
        Set: Name(self: MessageParameterAttribute) = value
        """
        ...



class MessagePropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MessagePropertyAttribute() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: MessagePropertyAttribute) -> str
        Set: Name(self: MessagePropertyAttribute) = value
        """
        ...



class MessageQuerySet(Dictionary): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable[KeyValuePair[str, MessageQuery]]'>, <type 'IReadOnlyCollection[KeyValuePair[str, MessageQuery]]'>, <type 'IEnumerable'>, <type 'IReadOnlyDictionary[str, MessageQuery]'>, <type 'IDictionary[str, MessageQuery]'>, <type 'IDeserializationCallback'>, <type 'ISerializable'>, <type 'ICollection[KeyValuePair[str, MessageQuery]]'>, <type 'ICollection'>, <type 'object'>
    """
    MessageQuerySet()
    MessageQuerySet(queryTable: MessageQueryTable[str])
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: MessageQuerySet) -> str
        Set: Name(self: MessageQuerySet) = value
        """
        ...


    def GetMessageQueryTable(self): # -> MessageQueryTable
        """ GetMessageQueryTable(self: MessageQuerySet) -> MessageQueryTable[str] """
        ...


class MessageSecurityOverHttp: # skipped bases: <type 'object'>, <type 'object'>
    """ MessageSecurityOverHttp() """
    @property
    def AlgorithmSuite(self) -> SecurityAlgorithmSuite:
        """
        Get: AlgorithmSuite(self: MessageSecurityOverHttp) -> SecurityAlgorithmSuite
        Set: AlgorithmSuite(self: MessageSecurityOverHttp) = value
        """
        ...

    @property
    def ClientCredentialType(self) -> MessageCredentialType:
        """
        Get: ClientCredentialType(self: MessageSecurityOverHttp) -> MessageCredentialType
        Set: ClientCredentialType(self: MessageSecurityOverHttp) = value
        """
        ...

    @property
    def NegotiateServiceCredential(self) -> bool:
        """
        Get: NegotiateServiceCredential(self: MessageSecurityOverHttp) -> bool
        Set: NegotiateServiceCredential(self: MessageSecurityOverHttp) = value
        """
        ...


    def IsSecureConversationEnabled(self, *args): #cannot find CLR method
        """ IsSecureConversationEnabled(self: MessageSecurityOverHttp) -> bool """
        ...

    def ShouldSerializeAlgorithmSuite(self) -> bool:
        """ ShouldSerializeAlgorithmSuite(self: MessageSecurityOverHttp) -> bool """
        ...

    def ShouldSerializeClientCredentialType(self) -> bool:
        """ ShouldSerializeClientCredentialType(self: MessageSecurityOverHttp) -> bool """
        ...

    def ShouldSerializeNegotiateServiceCredential(self) -> bool:
        """ ShouldSerializeNegotiateServiceCredential(self: MessageSecurityOverHttp) -> bool """
        ...


class MessageSecurityOverMsmq: # skipped bases: <type 'object'>, <type 'object'>
    """ MessageSecurityOverMsmq() """
    @property
    def AlgorithmSuite(self) -> SecurityAlgorithmSuite:
        """
        Get: AlgorithmSuite(self: MessageSecurityOverMsmq) -> SecurityAlgorithmSuite
        Set: AlgorithmSuite(self: MessageSecurityOverMsmq) = value
        """
        ...

    @property
    def ClientCredentialType(self) -> MessageCredentialType:
        """
        Get: ClientCredentialType(self: MessageSecurityOverMsmq) -> MessageCredentialType
        Set: ClientCredentialType(self: MessageSecurityOverMsmq) = value
        """
        ...



class MessageSecurityOverTcp: # skipped bases: <type 'object'>, <type 'object'>
    """ MessageSecurityOverTcp() """
    @property
    def AlgorithmSuite(self) -> SecurityAlgorithmSuite:
        """
        Get: AlgorithmSuite(self: MessageSecurityOverTcp) -> SecurityAlgorithmSuite
        Set: AlgorithmSuite(self: MessageSecurityOverTcp) = value
        """
        ...

    @property
    def ClientCredentialType(self) -> MessageCredentialType:
        """
        Get: ClientCredentialType(self: MessageSecurityOverTcp) -> MessageCredentialType
        Set: ClientCredentialType(self: MessageSecurityOverTcp) = value
        """
        ...



class MessageSecurityVersion: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BasicSecurityProfileVersion(self) -> BasicSecurityProfileVersion:
        """ Get: BasicSecurityProfileVersion(self: MessageSecurityVersion) -> BasicSecurityProfileVersion """
        ...

    @property
    def Default(self) -> MessageSecurityVersion:
        """ Get: Default() -> MessageSecurityVersion """
        ...

    @property
    def SecureConversationVersion(self) -> SecureConversationVersion:
        """ Get: SecureConversationVersion(self: MessageSecurityVersion) -> SecureConversationVersion """
        ...

    @property
    def SecurityPolicyVersion(self) -> SecurityPolicyVersion:
        """ Get: SecurityPolicyVersion(self: MessageSecurityVersion) -> SecurityPolicyVersion """
        ...

    @property
    def SecurityTokenVersion(self) -> SecurityTokenVersion:
        """ Get: SecurityTokenVersion(self: MessageSecurityVersion) -> SecurityTokenVersion """
        ...

    @property
    def SecurityVersion(self) -> SecurityVersion:
        """ Get: SecurityVersion(self: MessageSecurityVersion) -> SecurityVersion """
        ...

    @property
    def TrustVersion(self) -> TrustVersion:
        """ Get: TrustVersion(self: MessageSecurityVersion) -> TrustVersion """
        ...

    @property
    def WSSecurity10WSTrust13WSSecureConversation13WSSecurityPolicy12BasicSecurityProfile10(self) -> MessageSecurityVersion:
        """ Get: WSSecurity10WSTrust13WSSecureConversation13WSSecurityPolicy12BasicSecurityProfile10() -> MessageSecurityVersion """
        ...

    @property
    def WSSecurity10WSTrustFebruary2005WSSecureConversationFebruary2005WSSecurityPolicy11BasicSecurityProfile10(self) -> MessageSecurityVersion:
        """ Get: WSSecurity10WSTrustFebruary2005WSSecureConversationFebruary2005WSSecurityPolicy11BasicSecurityProfile10() -> MessageSecurityVersion """
        ...

    @property
    def WSSecurity11WSTrust13WSSecureConversation13WSSecurityPolicy12(self) -> MessageSecurityVersion:
        """ Get: WSSecurity11WSTrust13WSSecureConversation13WSSecurityPolicy12() -> MessageSecurityVersion """
        ...

    @property
    def WSSecurity11WSTrust13WSSecureConversation13WSSecurityPolicy12BasicSecurityProfile10(self) -> MessageSecurityVersion:
        """ Get: WSSecurity11WSTrust13WSSecureConversation13WSSecurityPolicy12BasicSecurityProfile10() -> MessageSecurityVersion """
        ...

    @property
    def WSSecurity11WSTrustFebruary2005WSSecureConversationFebruary2005WSSecurityPolicy11(self) -> MessageSecurityVersion:
        """ Get: WSSecurity11WSTrustFebruary2005WSSecureConversationFebruary2005WSSecurityPolicy11() -> MessageSecurityVersion """
        ...

    @property
    def WSSecurity11WSTrustFebruary2005WSSecureConversationFebruary2005WSSecurityPolicy11BasicSecurityProfile10(self) -> MessageSecurityVersion:
        """ Get: WSSecurity11WSTrustFebruary2005WSSecureConversationFebruary2005WSSecurityPolicy11BasicSecurityProfile10() -> MessageSecurityVersion """
        ...




class MsmqAuthenticationMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsmqAuthenticationMode, values: Certificate (2), None (0), WindowsDomain (1) """
    Certificate: MsmqAuthenticationMode = ...
    value__ = ...
    WindowsDomain: MsmqAuthenticationMode = ...


class MsmqBindingBase(IBindingRuntimePreferences, Binding): # skipped bases: <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """ no doc """
    @property
    def CustomDeadLetterQueue(self) -> Uri:
        """
        Get: CustomDeadLetterQueue(self: MsmqBindingBase) -> Uri
        Set: CustomDeadLetterQueue(self: MsmqBindingBase) = value
        """
        ...

    @property
    def DeadLetterQueue(self) -> DeadLetterQueue:
        """
        Get: DeadLetterQueue(self: MsmqBindingBase) -> DeadLetterQueue
        Set: DeadLetterQueue(self: MsmqBindingBase) = value
        """
        ...

    @property
    def Durable(self) -> bool:
        """
        Get: Durable(self: MsmqBindingBase) -> bool
        Set: Durable(self: MsmqBindingBase) = value
        """
        ...

    @property
    def ExactlyOnce(self) -> bool:
        """
        Get: ExactlyOnce(self: MsmqBindingBase) -> bool
        Set: ExactlyOnce(self: MsmqBindingBase) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: MsmqBindingBase) -> Int64
        Set: MaxReceivedMessageSize(self: MsmqBindingBase) = value
        """
        ...

    @property
    def MaxRetryCycles(self) -> int:
        """
        Get: MaxRetryCycles(self: MsmqBindingBase) -> int
        Set: MaxRetryCycles(self: MsmqBindingBase) = value
        """
        ...

    @property
    def ReceiveContextEnabled(self) -> bool:
        """
        Get: ReceiveContextEnabled(self: MsmqBindingBase) -> bool
        Set: ReceiveContextEnabled(self: MsmqBindingBase) = value
        """
        ...

    @property
    def ReceiveErrorHandling(self): # -> ReceiveErrorHandling
        """
        Get: ReceiveErrorHandling(self: MsmqBindingBase) -> ReceiveErrorHandling
        Set: ReceiveErrorHandling(self: MsmqBindingBase) = value
        """
        ...

    @property
    def ReceiveRetryCount(self) -> int:
        """
        Get: ReceiveRetryCount(self: MsmqBindingBase) -> int
        Set: ReceiveRetryCount(self: MsmqBindingBase) = value
        """
        ...

    @property
    def RetryCycleDelay(self) -> TimeSpan:
        """
        Get: RetryCycleDelay(self: MsmqBindingBase) -> TimeSpan
        Set: RetryCycleDelay(self: MsmqBindingBase) = value
        """
        ...

    @property
    def TimeToLive(self) -> TimeSpan:
        """
        Get: TimeToLive(self: MsmqBindingBase) -> TimeSpan
        Set: TimeToLive(self: MsmqBindingBase) = value
        """
        ...

    @property
    def UseMsmqTracing(self) -> bool:
        """
        Get: UseMsmqTracing(self: MsmqBindingBase) -> bool
        Set: UseMsmqTracing(self: MsmqBindingBase) = value
        """
        ...

    @property
    def UseSourceJournal(self) -> bool:
        """
        Get: UseSourceJournal(self: MsmqBindingBase) -> bool
        Set: UseSourceJournal(self: MsmqBindingBase) = value
        """
        ...

    @property
    def ValidityDuration(self) -> TimeSpan:
        """
        Get: ValidityDuration(self: MsmqBindingBase) -> TimeSpan
        Set: ValidityDuration(self: MsmqBindingBase) = value
        """
        ...



class MsmqEncryptionAlgorithm(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsmqEncryptionAlgorithm, values: Aes (1), RC4Stream (0) """
    Aes: MsmqEncryptionAlgorithm = ...
    RC4Stream: MsmqEncryptionAlgorithm = ...
    value__ = ...


class MsmqException(ExternalException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MsmqException()
    MsmqException(message: str)
    MsmqException(message: str, error: int)
    MsmqException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class PoisonMessageException(CommunicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PoisonMessageException()
    PoisonMessageException(message: str)
    PoisonMessageException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class MsmqPoisonMessageException(PoisonMessageException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MsmqPoisonMessageException()
    MsmqPoisonMessageException(message: str)
    MsmqPoisonMessageException(message: str, innerException: Exception)
    MsmqPoisonMessageException(messageLookupId: Int64)
    MsmqPoisonMessageException(messageLookupId: Int64, innerException: Exception)
    """
    @property
    def MessageLookupId(self) -> Int64:
        """ Get: MessageLookupId(self: MsmqPoisonMessageException) -> Int64 """
        ...


    SerializeObjectState = ...


class MsmqSecureHashAlgorithm(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsmqSecureHashAlgorithm, values: MD5 (0), Sha1 (1), Sha256 (2), Sha512 (3) """
    MD5: MsmqSecureHashAlgorithm = ...
    Sha1: MsmqSecureHashAlgorithm = ...
    Sha256: MsmqSecureHashAlgorithm = ...
    Sha512: MsmqSecureHashAlgorithm = ...
    value__ = ...


class MsmqTransportSecurity: # skipped bases: <type 'object'>, <type 'object'>
    """
    MsmqTransportSecurity()
    MsmqTransportSecurity(other: MsmqTransportSecurity)
    """
    @property
    def MsmqAuthenticationMode(self) -> MsmqAuthenticationMode:
        """
        Get: MsmqAuthenticationMode(self: MsmqTransportSecurity) -> MsmqAuthenticationMode
        Set: MsmqAuthenticationMode(self: MsmqTransportSecurity) = value
        """
        ...

    @property
    def MsmqEncryptionAlgorithm(self) -> MsmqEncryptionAlgorithm:
        """
        Get: MsmqEncryptionAlgorithm(self: MsmqTransportSecurity) -> MsmqEncryptionAlgorithm
        Set: MsmqEncryptionAlgorithm(self: MsmqTransportSecurity) = value
        """
        ...

    @property
    def MsmqProtectionLevel(self) -> ProtectionLevel:
        """
        Get: MsmqProtectionLevel(self: MsmqTransportSecurity) -> ProtectionLevel
        Set: MsmqProtectionLevel(self: MsmqTransportSecurity) = value
        """
        ...

    @property
    def MsmqSecureHashAlgorithm(self) -> MsmqSecureHashAlgorithm:
        """
        Get: MsmqSecureHashAlgorithm(self: MsmqTransportSecurity) -> MsmqSecureHashAlgorithm
        Set: MsmqSecureHashAlgorithm(self: MsmqTransportSecurity) = value
        """
        ...



class NamedPipeTransportSecurity: # skipped bases: <type 'object'>, <type 'object'>
    """ NamedPipeTransportSecurity() """
    @property
    def ProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ProtectionLevel(self: NamedPipeTransportSecurity) -> ProtectionLevel
        Set: ProtectionLevel(self: NamedPipeTransportSecurity) = value
        """
        ...



class NetHttpBinding(HttpBindingBase): # skipped bases: <type 'IBindingRuntimePreferences'>, <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    NetHttpBinding()
    NetHttpBinding(securityMode: BasicHttpSecurityMode)
    NetHttpBinding(securityMode: BasicHttpSecurityMode, reliableSessionEnabled: bool)
    NetHttpBinding(configurationName: str)
    """
    @property
    def MessageEncoding(self): # -> NetHttpMessageEncoding
        """
        Get: MessageEncoding(self: NetHttpBinding) -> NetHttpMessageEncoding
        Set: MessageEncoding(self: NetHttpBinding) = value
        """
        ...

    @property
    def ReliableSession(self): # -> OptionalReliableSession
        """
        Get: ReliableSession(self: NetHttpBinding) -> OptionalReliableSession
        Set: ReliableSession(self: NetHttpBinding) = value
        """
        ...

    @property
    def Security(self) -> BasicHttpSecurity:
        """
        Get: Security(self: NetHttpBinding) -> BasicHttpSecurity
        Set: Security(self: NetHttpBinding) = value
        """
        ...

    @property
    def WebSocketSettings(self): # -> WebSocketTransportSettings
        """ Get: WebSocketSettings(self: NetHttpBinding) -> WebSocketTransportSettings """
        ...


    def BuildChannelFactory(self, parameters): # -> IChannelFactory # Not found arg types: {'parameters': 'BindingParameterCollection'}
        """ BuildChannelFactory[TChannel](self: NetHttpBinding, parameters: BindingParameterCollection) -> IChannelFactory[TChannel] """
        ...

    def CreateBindingElements(self): # -> BindingElementCollection
        """ CreateBindingElements(self: NetHttpBinding) -> BindingElementCollection """
        ...

    def ShouldSerializeReliableSession(self) -> bool:
        """ ShouldSerializeReliableSession(self: NetHttpBinding) -> bool """
        ...

    def ShouldSerializeSecurity(self) -> bool:
        """ ShouldSerializeSecurity(self: NetHttpBinding) -> bool """
        ...

    def __new__(cls, *__args:BasicHttpSecurityMode) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, securityMode: BasicHttpSecurityMode)
        __new__(cls: type, securityMode: BasicHttpSecurityMode, reliableSessionEnabled: bool)
        __new__(cls: type, configurationName: str)
        """
        ...


class NetHttpMessageEncoding(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NetHttpMessageEncoding, values: Binary (0), Mtom (2), Text (1) """
    Binary: NetHttpMessageEncoding = ...
    Mtom: NetHttpMessageEncoding = ...
    Text: NetHttpMessageEncoding = ...
    value__ = ...


class NetHttpsBinding(HttpBindingBase): # skipped bases: <type 'IBindingRuntimePreferences'>, <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    NetHttpsBinding()
    NetHttpsBinding(securityMode: BasicHttpsSecurityMode)
    NetHttpsBinding(securityMode: BasicHttpsSecurityMode, reliableSessionEnabled: bool)
    NetHttpsBinding(configurationName: str)
    """
    @property
    def MessageEncoding(self) -> NetHttpMessageEncoding:
        """
        Get: MessageEncoding(self: NetHttpsBinding) -> NetHttpMessageEncoding
        Set: MessageEncoding(self: NetHttpsBinding) = value
        """
        ...

    @property
    def ReliableSession(self): # -> OptionalReliableSession
        """
        Get: ReliableSession(self: NetHttpsBinding) -> OptionalReliableSession
        Set: ReliableSession(self: NetHttpsBinding) = value
        """
        ...

    @property
    def Security(self) -> BasicHttpsSecurity:
        """
        Get: Security(self: NetHttpsBinding) -> BasicHttpsSecurity
        Set: Security(self: NetHttpsBinding) = value
        """
        ...

    @property
    def WebSocketSettings(self): # -> WebSocketTransportSettings
        """ Get: WebSocketSettings(self: NetHttpsBinding) -> WebSocketTransportSettings """
        ...


    def BuildChannelFactory(self, parameters): # -> IChannelFactory # Not found arg types: {'parameters': 'BindingParameterCollection'}
        """ BuildChannelFactory[TChannel](self: NetHttpsBinding, parameters: BindingParameterCollection) -> IChannelFactory[TChannel] """
        ...

    def CreateBindingElements(self): # -> BindingElementCollection
        """ CreateBindingElements(self: NetHttpsBinding) -> BindingElementCollection """
        ...

    def ShouldSerializeReliableSession(self) -> bool:
        """ ShouldSerializeReliableSession(self: NetHttpsBinding) -> bool """
        ...

    def ShouldSerializeSecurity(self) -> bool:
        """ ShouldSerializeSecurity(self: NetHttpsBinding) -> bool """
        ...

    def __new__(cls, *__args:BasicHttpsSecurityMode) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, securityMode: BasicHttpsSecurityMode)
        __new__(cls: type, securityMode: BasicHttpsSecurityMode, reliableSessionEnabled: bool)
        __new__(cls: type, configurationName: str)
        """
        ...


class NetMsmqBinding(MsmqBindingBase): # skipped bases: <type 'IBindingRuntimePreferences'>, <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    NetMsmqBinding()
    NetMsmqBinding(configurationName: str)
    NetMsmqBinding(securityMode: NetMsmqSecurityMode)
    """
    @property
    def EnvelopeVersion(self) -> EnvelopeVersion:
        """ Get: EnvelopeVersion(self: NetMsmqBinding) -> EnvelopeVersion """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: NetMsmqBinding) -> Int64
        Set: MaxBufferPoolSize(self: NetMsmqBinding) = value
        """
        ...

    @property
    def QueueTransferProtocol(self): # -> QueueTransferProtocol
        """
        Get: QueueTransferProtocol(self: NetMsmqBinding) -> QueueTransferProtocol
        Set: QueueTransferProtocol(self: NetMsmqBinding) = value
        """
        ...

    @property
    def ReaderQuotas(self) -> XmlDictionaryReaderQuotas:
        """
        Get: ReaderQuotas(self: NetMsmqBinding) -> XmlDictionaryReaderQuotas
        Set: ReaderQuotas(self: NetMsmqBinding) = value
        """
        ...

    @property
    def Security(self): # -> NetMsmqSecurity
        """
        Get: Security(self: NetMsmqBinding) -> NetMsmqSecurity
        Set: Security(self: NetMsmqBinding) = value
        """
        ...

    @property
    def UseActiveDirectory(self) -> bool:
        """
        Get: UseActiveDirectory(self: NetMsmqBinding) -> bool
        Set: UseActiveDirectory(self: NetMsmqBinding) = value
        """
        ...


    def CreateBindingElements(self): # -> BindingElementCollection
        """ CreateBindingElements(self: NetMsmqBinding) -> BindingElementCollection """
        ...

    def ShouldSerializeReaderQuotas(self) -> bool:
        """ ShouldSerializeReaderQuotas(self: NetMsmqBinding) -> bool """
        ...

    def ShouldSerializeSecurity(self) -> bool:
        """ ShouldSerializeSecurity(self: NetMsmqBinding) -> bool """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, configurationName: str)
        __new__(cls: type, securityMode: NetMsmqSecurityMode)
        """
        ...


class NetMsmqSecurity: # skipped bases: <type 'object'>, <type 'object'>
    """ NetMsmqSecurity() """
    @property
    def Message(self) -> MessageSecurityOverMsmq:
        """
        Get: Message(self: NetMsmqSecurity) -> MessageSecurityOverMsmq
        Set: Message(self: NetMsmqSecurity) = value
        """
        ...

    @property
    def Mode(self): # -> NetMsmqSecurityMode
        """
        Get: Mode(self: NetMsmqSecurity) -> NetMsmqSecurityMode
        Set: Mode(self: NetMsmqSecurity) = value
        """
        ...

    @property
    def Transport(self) -> MsmqTransportSecurity:
        """
        Get: Transport(self: NetMsmqSecurity) -> MsmqTransportSecurity
        Set: Transport(self: NetMsmqSecurity) = value
        """
        ...



class NetMsmqSecurityMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NetMsmqSecurityMode, values: Both (3), Message (2), None (0), Transport (1) """
    Both: NetMsmqSecurityMode = ...
    Message: NetMsmqSecurityMode = ...
    Transport: NetMsmqSecurityMode = ...
    value__ = ...


class NetNamedPipeBinding(IBindingRuntimePreferences, Binding): # skipped bases: <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    NetNamedPipeBinding()
    NetNamedPipeBinding(securityMode: NetNamedPipeSecurityMode)
    NetNamedPipeBinding(configurationName: str)
    """
    @property
    def EnvelopeVersion(self) -> EnvelopeVersion:
        """ Get: EnvelopeVersion(self: NetNamedPipeBinding) -> EnvelopeVersion """
        ...

    @property
    def HostNameComparisonMode(self) -> HostNameComparisonMode:
        """
        Get: HostNameComparisonMode(self: NetNamedPipeBinding) -> HostNameComparisonMode
        Set: HostNameComparisonMode(self: NetNamedPipeBinding) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: NetNamedPipeBinding) -> Int64
        Set: MaxBufferPoolSize(self: NetNamedPipeBinding) = value
        """
        ...

    @property
    def MaxBufferSize(self) -> int:
        """
        Get: MaxBufferSize(self: NetNamedPipeBinding) -> int
        Set: MaxBufferSize(self: NetNamedPipeBinding) = value
        """
        ...

    @property
    def MaxConnections(self) -> int:
        """
        Get: MaxConnections(self: NetNamedPipeBinding) -> int
        Set: MaxConnections(self: NetNamedPipeBinding) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: NetNamedPipeBinding) -> Int64
        Set: MaxReceivedMessageSize(self: NetNamedPipeBinding) = value
        """
        ...

    @property
    def ReaderQuotas(self) -> XmlDictionaryReaderQuotas:
        """
        Get: ReaderQuotas(self: NetNamedPipeBinding) -> XmlDictionaryReaderQuotas
        Set: ReaderQuotas(self: NetNamedPipeBinding) = value
        """
        ...

    @property
    def Security(self): # -> NetNamedPipeSecurity
        """
        Get: Security(self: NetNamedPipeBinding) -> NetNamedPipeSecurity
        Set: Security(self: NetNamedPipeBinding) = value
        """
        ...

    @property
    def TransactionFlow(self) -> bool:
        """
        Get: TransactionFlow(self: NetNamedPipeBinding) -> bool
        Set: TransactionFlow(self: NetNamedPipeBinding) = value
        """
        ...

    @property
    def TransactionProtocol(self): # -> TransactionProtocol
        """
        Get: TransactionProtocol(self: NetNamedPipeBinding) -> TransactionProtocol
        Set: TransactionProtocol(self: NetNamedPipeBinding) = value
        """
        ...

    @property
    def TransferMode(self): # -> TransferMode
        """
        Get: TransferMode(self: NetNamedPipeBinding) -> TransferMode
        Set: TransferMode(self: NetNamedPipeBinding) = value
        """
        ...


    def ShouldSerializeMaxConnections(self) -> bool:
        """ ShouldSerializeMaxConnections(self: NetNamedPipeBinding) -> bool """
        ...

    def ShouldSerializeReaderQuotas(self) -> bool:
        """ ShouldSerializeReaderQuotas(self: NetNamedPipeBinding) -> bool """
        ...

    def ShouldSerializeSecurity(self) -> bool:
        """ ShouldSerializeSecurity(self: NetNamedPipeBinding) -> bool """
        ...

    def ShouldSerializeTransactionProtocol(self) -> bool:
        """ ShouldSerializeTransactionProtocol(self: NetNamedPipeBinding) -> bool """
        ...


class NetNamedPipeSecurity: # skipped bases: <type 'object'>, <type 'object'>
    """ NetNamedPipeSecurity() """
    @property
    def Mode(self): # -> NetNamedPipeSecurityMode
        """
        Get: Mode(self: NetNamedPipeSecurity) -> NetNamedPipeSecurityMode
        Set: Mode(self: NetNamedPipeSecurity) = value
        """
        ...

    @property
    def Transport(self) -> NamedPipeTransportSecurity:
        """
        Get: Transport(self: NetNamedPipeSecurity) -> NamedPipeTransportSecurity
        Set: Transport(self: NetNamedPipeSecurity) = value
        """
        ...


    def ShouldSerializeTransport(self) -> bool:
        """ ShouldSerializeTransport(self: NetNamedPipeSecurity) -> bool """
        ...


class NetNamedPipeSecurityMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NetNamedPipeSecurityMode, values: None (0), Transport (1) """
    Transport: NetNamedPipeSecurityMode = ...
    value__ = ...


class NetPeerTcpBinding(IBindingRuntimePreferences, Binding): # skipped bases: <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    NetPeerTcpBinding()
    NetPeerTcpBinding(configurationName: str)
    """
    @property
    def EnvelopeVersion(self) -> EnvelopeVersion:
        """ Get: EnvelopeVersion(self: NetPeerTcpBinding) -> EnvelopeVersion """
        ...

    @property
    def IsPnrpAvailable(self) -> bool:
        """ Get: IsPnrpAvailable() -> bool """
        ...

    @property
    def ListenIPAddress(self) -> IPAddress:
        """
        Get: ListenIPAddress(self: NetPeerTcpBinding) -> IPAddress
        Set: ListenIPAddress(self: NetPeerTcpBinding) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: NetPeerTcpBinding) -> Int64
        Set: MaxBufferPoolSize(self: NetPeerTcpBinding) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: NetPeerTcpBinding) -> Int64
        Set: MaxReceivedMessageSize(self: NetPeerTcpBinding) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: NetPeerTcpBinding) -> int
        Set: Port(self: NetPeerTcpBinding) = value
        """
        ...

    @property
    def ReaderQuotas(self) -> XmlDictionaryReaderQuotas:
        """
        Get: ReaderQuotas(self: NetPeerTcpBinding) -> XmlDictionaryReaderQuotas
        Set: ReaderQuotas(self: NetPeerTcpBinding) = value
        """
        ...

    @property
    def Resolver(self) -> PeerResolverSettings:
        """ Get: Resolver(self: NetPeerTcpBinding) -> PeerResolverSettings """
        ...

    @property
    def Security(self): # -> PeerSecuritySettings
        """
        Get: Security(self: NetPeerTcpBinding) -> PeerSecuritySettings
        Set: Security(self: NetPeerTcpBinding) = value
        """
        ...


    def ShouldSerializeReaderQuotas(self) -> bool:
        """ ShouldSerializeReaderQuotas(self: NetPeerTcpBinding) -> bool """
        ...

    def ShouldSerializeSecurity(self) -> bool:
        """ ShouldSerializeSecurity(self: NetPeerTcpBinding) -> bool """
        ...



class NetTcpBinding(IBindingRuntimePreferences, Binding): # skipped bases: <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    NetTcpBinding()
    NetTcpBinding(securityMode: SecurityMode)
    NetTcpBinding(securityMode: SecurityMode, reliableSessionEnabled: bool)
    NetTcpBinding(configurationName: str)
    """
    @property
    def EnvelopeVersion(self) -> EnvelopeVersion:
        """ Get: EnvelopeVersion(self: NetTcpBinding) -> EnvelopeVersion """
        ...

    @property
    def HostNameComparisonMode(self) -> HostNameComparisonMode:
        """
        Get: HostNameComparisonMode(self: NetTcpBinding) -> HostNameComparisonMode
        Set: HostNameComparisonMode(self: NetTcpBinding) = value
        """
        ...

    @property
    def ListenBacklog(self) -> int:
        """
        Get: ListenBacklog(self: NetTcpBinding) -> int
        Set: ListenBacklog(self: NetTcpBinding) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: NetTcpBinding) -> Int64
        Set: MaxBufferPoolSize(self: NetTcpBinding) = value
        """
        ...

    @property
    def MaxBufferSize(self) -> int:
        """
        Get: MaxBufferSize(self: NetTcpBinding) -> int
        Set: MaxBufferSize(self: NetTcpBinding) = value
        """
        ...

    @property
    def MaxConnections(self) -> int:
        """
        Get: MaxConnections(self: NetTcpBinding) -> int
        Set: MaxConnections(self: NetTcpBinding) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: NetTcpBinding) -> Int64
        Set: MaxReceivedMessageSize(self: NetTcpBinding) = value
        """
        ...

    @property
    def PortSharingEnabled(self) -> bool:
        """
        Get: PortSharingEnabled(self: NetTcpBinding) -> bool
        Set: PortSharingEnabled(self: NetTcpBinding) = value
        """
        ...

    @property
    def ReaderQuotas(self) -> XmlDictionaryReaderQuotas:
        """
        Get: ReaderQuotas(self: NetTcpBinding) -> XmlDictionaryReaderQuotas
        Set: ReaderQuotas(self: NetTcpBinding) = value
        """
        ...

    @property
    def ReliableSession(self): # -> OptionalReliableSession
        """
        Get: ReliableSession(self: NetTcpBinding) -> OptionalReliableSession
        Set: ReliableSession(self: NetTcpBinding) = value
        """
        ...

    @property
    def Security(self): # -> NetTcpSecurity
        """
        Get: Security(self: NetTcpBinding) -> NetTcpSecurity
        Set: Security(self: NetTcpBinding) = value
        """
        ...

    @property
    def TransactionFlow(self) -> bool:
        """
        Get: TransactionFlow(self: NetTcpBinding) -> bool
        Set: TransactionFlow(self: NetTcpBinding) = value
        """
        ...

    @property
    def TransactionProtocol(self): # -> TransactionProtocol
        """
        Get: TransactionProtocol(self: NetTcpBinding) -> TransactionProtocol
        Set: TransactionProtocol(self: NetTcpBinding) = value
        """
        ...

    @property
    def TransferMode(self): # -> TransferMode
        """
        Get: TransferMode(self: NetTcpBinding) -> TransferMode
        Set: TransferMode(self: NetTcpBinding) = value
        """
        ...


    def ShouldSerializeListenBacklog(self) -> bool:
        """ ShouldSerializeListenBacklog(self: NetTcpBinding) -> bool """
        ...

    def ShouldSerializeMaxConnections(self) -> bool:
        """ ShouldSerializeMaxConnections(self: NetTcpBinding) -> bool """
        ...

    def ShouldSerializeReaderQuotas(self) -> bool:
        """ ShouldSerializeReaderQuotas(self: NetTcpBinding) -> bool """
        ...

    def ShouldSerializeReliableSession(self) -> bool:
        """ ShouldSerializeReliableSession(self: NetTcpBinding) -> bool """
        ...

    def ShouldSerializeSecurity(self) -> bool:
        """ ShouldSerializeSecurity(self: NetTcpBinding) -> bool """
        ...

    def ShouldSerializeTransactionProtocol(self) -> bool:
        """ ShouldSerializeTransactionProtocol(self: NetTcpBinding) -> bool """
        ...


class NetTcpContextBinding(NetTcpBinding): # skipped bases: <type 'IBindingRuntimePreferences'>, <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    NetTcpContextBinding()
    NetTcpContextBinding(securityMode: SecurityMode)
    NetTcpContextBinding(configName: str)
    NetTcpContextBinding(securityMode: SecurityMode, reliableSessionEnabled: bool)
    """
    @property
    def ClientCallbackAddress(self) -> Uri:
        """
        Get: ClientCallbackAddress(self: NetTcpContextBinding) -> Uri
        Set: ClientCallbackAddress(self: NetTcpContextBinding) = value
        """
        ...

    @property
    def ContextManagementEnabled(self) -> bool:
        """
        Get: ContextManagementEnabled(self: NetTcpContextBinding) -> bool
        Set: ContextManagementEnabled(self: NetTcpContextBinding) = value
        """
        ...

    @property
    def ContextProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ContextProtectionLevel(self: NetTcpContextBinding) -> ProtectionLevel
        Set: ContextProtectionLevel(self: NetTcpContextBinding) = value
        """
        ...



class NetTcpSecurity: # skipped bases: <type 'object'>, <type 'object'>
    """ NetTcpSecurity() """
    @property
    def Message(self) -> MessageSecurityOverTcp:
        """
        Get: Message(self: NetTcpSecurity) -> MessageSecurityOverTcp
        Set: Message(self: NetTcpSecurity) = value
        """
        ...

    @property
    def Mode(self): # -> SecurityMode
        """
        Get: Mode(self: NetTcpSecurity) -> SecurityMode
        Set: Mode(self: NetTcpSecurity) = value
        """
        ...

    @property
    def Transport(self): # -> TcpTransportSecurity
        """
        Get: Transport(self: NetTcpSecurity) -> TcpTransportSecurity
        Set: Transport(self: NetTcpSecurity) = value
        """
        ...



class NonDualMessageSecurityOverHttp(MessageSecurityOverHttp): # skipped bases: <type 'object'>
    """ NonDualMessageSecurityOverHttp() """
    @property
    def EstablishSecurityContext(self) -> bool:
        """
        Get: EstablishSecurityContext(self: NonDualMessageSecurityOverHttp) -> bool
        Set: EstablishSecurityContext(self: NonDualMessageSecurityOverHttp) = value
        """
        ...



class OperationBehaviorAttribute(Attribute, IOperationBehavior): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ OperationBehaviorAttribute() """
    @property
    def AutoDisposeParameters(self) -> bool:
        """
        Get: AutoDisposeParameters(self: OperationBehaviorAttribute) -> bool
        Set: AutoDisposeParameters(self: OperationBehaviorAttribute) = value
        """
        ...

    @property
    def Impersonation(self) -> ImpersonationOption:
        """
        Get: Impersonation(self: OperationBehaviorAttribute) -> ImpersonationOption
        Set: Impersonation(self: OperationBehaviorAttribute) = value
        """
        ...

    @property
    def ReleaseInstanceMode(self): # -> ReleaseInstanceMode
        """
        Get: ReleaseInstanceMode(self: OperationBehaviorAttribute) -> ReleaseInstanceMode
        Set: ReleaseInstanceMode(self: OperationBehaviorAttribute) = value
        """
        ...

    @property
    def TransactionAutoComplete(self) -> bool:
        """
        Get: TransactionAutoComplete(self: OperationBehaviorAttribute) -> bool
        Set: TransactionAutoComplete(self: OperationBehaviorAttribute) = value
        """
        ...

    @property
    def TransactionScopeRequired(self) -> bool:
        """
        Get: TransactionScopeRequired(self: OperationBehaviorAttribute) -> bool
        Set: TransactionScopeRequired(self: OperationBehaviorAttribute) = value
        """
        ...



class OperationContext(IExtensibleObject): # skipped bases: <type 'object'>
    """ OperationContext(channel: IContextChannel) """
    @property
    def Channel(self) -> IContextChannel:
        """ Get: Channel(self: OperationContext) -> IContextChannel """
        ...

    @property
    def ClaimsPrincipal(self) -> ClaimsPrincipal:
        """ Get: ClaimsPrincipal(self: OperationContext) -> ClaimsPrincipal """
        ...

    @property
    def Current(self) -> OperationContext:
        """
        Get: Current() -> OperationContext
        Set: Current() = value
        """
        ...

    @property
    def EndpointDispatcher(self): # -> EndpointDispatcher
        """
        Get: EndpointDispatcher(self: OperationContext) -> EndpointDispatcher
        Set: EndpointDispatcher(self: OperationContext) = value
        """
        ...

    @property
    def HasSupportingTokens(self) -> bool:
        """ Get: HasSupportingTokens(self: OperationContext) -> bool """
        ...

    @property
    def Host(self): # -> ServiceHostBase
        """ Get: Host(self: OperationContext) -> ServiceHostBase """
        ...

    @property
    def IncomingMessageHeaders(self): # -> MessageHeaders
        """ Get: IncomingMessageHeaders(self: OperationContext) -> MessageHeaders """
        ...

    @property
    def IncomingMessageProperties(self): # -> MessageProperties
        """ Get: IncomingMessageProperties(self: OperationContext) -> MessageProperties """
        ...

    @property
    def IncomingMessageVersion(self): # -> MessageVersion
        """ Get: IncomingMessageVersion(self: OperationContext) -> MessageVersion """
        ...

    @property
    def InstanceContext(self) -> InstanceContext:
        """ Get: InstanceContext(self: OperationContext) -> InstanceContext """
        ...

    @property
    def IsUserContext(self) -> bool:
        """ Get: IsUserContext(self: OperationContext) -> bool """
        ...

    @property
    def OutgoingMessageHeaders(self): # -> MessageHeaders
        """ Get: OutgoingMessageHeaders(self: OperationContext) -> MessageHeaders """
        ...

    @property
    def OutgoingMessageProperties(self): # -> MessageProperties
        """ Get: OutgoingMessageProperties(self: OperationContext) -> MessageProperties """
        ...

    @property
    def RequestContext(self) -> RequestContext:
        """
        Get: RequestContext(self: OperationContext) -> RequestContext
        Set: RequestContext(self: OperationContext) = value
        """
        ...

    @property
    def ServiceSecurityContext(self): # -> ServiceSecurityContext
        """ Get: ServiceSecurityContext(self: OperationContext) -> ServiceSecurityContext """
        ...

    @property
    def SessionId(self) -> str:
        """ Get: SessionId(self: OperationContext) -> str """
        ...

    @property
    def SupportingTokens(self) -> ICollection:
        """ Get: SupportingTokens(self: OperationContext) -> ICollection[SupportingTokenSpecification] """
        ...


    def GetCallbackChannel(self): # -> T
        """ GetCallbackChannel[T](self: OperationContext) -> T """
        ...

    def SetTransactionComplete(self): # -> 
        """ SetTransactionComplete(self: OperationContext) """
        ...

    OperationCompleted = ...


class OperationContextScope(IDisposable): # skipped bases: <type 'object'>
    """
    OperationContextScope(channel: IContextChannel)
    OperationContextScope(context: OperationContext)
    """
    pass

class OperationContractAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ OperationContractAttribute() """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: OperationContractAttribute) -> str
        Set: Action(self: OperationContractAttribute) = value
        """
        ...

    @property
    def AsyncPattern(self) -> bool:
        """
        Get: AsyncPattern(self: OperationContractAttribute) -> bool
        Set: AsyncPattern(self: OperationContractAttribute) = value
        """
        ...

    @property
    def HasProtectionLevel(self) -> bool:
        """ Get: HasProtectionLevel(self: OperationContractAttribute) -> bool """
        ...

    @property
    def IsInitiating(self) -> bool:
        """
        Get: IsInitiating(self: OperationContractAttribute) -> bool
        Set: IsInitiating(self: OperationContractAttribute) = value
        """
        ...

    @property
    def IsOneWay(self) -> bool:
        """
        Get: IsOneWay(self: OperationContractAttribute) -> bool
        Set: IsOneWay(self: OperationContractAttribute) = value
        """
        ...

    @property
    def IsTerminating(self) -> bool:
        """
        Get: IsTerminating(self: OperationContractAttribute) -> bool
        Set: IsTerminating(self: OperationContractAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: OperationContractAttribute) -> str
        Set: Name(self: OperationContractAttribute) = value
        """
        ...

    @property
    def ProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ProtectionLevel(self: OperationContractAttribute) -> ProtectionLevel
        Set: ProtectionLevel(self: OperationContractAttribute) = value
        """
        ...

    @property
    def ReplyAction(self) -> str:
        """
        Get: ReplyAction(self: OperationContractAttribute) -> str
        Set: ReplyAction(self: OperationContractAttribute) = value
        """
        ...



class OperationFormatStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OperationFormatStyle, values: Document (0), Rpc (1) """
    Document: OperationFormatStyle = ...
    Rpc: OperationFormatStyle = ...
    value__ = ...


class OperationFormatUse(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OperationFormatUse, values: Encoded (1), Literal (0) """
    Encoded: OperationFormatUse = ...
    Literal: OperationFormatUse = ...
    value__ = ...


class ReliableSession: # skipped bases: <type 'object'>, <type 'object'>
    """
    ReliableSession()
    ReliableSession(reliableSessionBindingElement: ReliableSessionBindingElement)
    """
    @property
    def InactivityTimeout(self) -> TimeSpan:
        """
        Get: InactivityTimeout(self: ReliableSession) -> TimeSpan
        Set: InactivityTimeout(self: ReliableSession) = value
        """
        ...

    @property
    def Ordered(self) -> bool:
        """
        Get: Ordered(self: ReliableSession) -> bool
        Set: Ordered(self: ReliableSession) = value
        """
        ...



class OptionalReliableSession(ReliableSession): # skipped bases: <type 'object'>
    """
    OptionalReliableSession()
    OptionalReliableSession(reliableSessionBindingElement: ReliableSessionBindingElement)
    """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: OptionalReliableSession) -> bool
        Set: Enabled(self: OptionalReliableSession) = value
        """
        ...



class PeerHopCountAttribute(MessageHeaderAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PeerHopCountAttribute() """
    @property
    def Name(self) -> str:
        """ Get: Name(self: PeerHopCountAttribute) -> str """
        ...

    @property
    def Namespace(self) -> str:
        """ Get: Namespace(self: PeerHopCountAttribute) -> str """
        ...

    @property
    def ProtectionLevel(self) -> ProtectionLevel:
        """ Get: ProtectionLevel(self: PeerHopCountAttribute) -> ProtectionLevel """
        ...



class PeerMessageOrigination(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PeerMessageOrigination, values: Local (0), Remote (1) """
    Local: PeerMessageOrigination = ...
    Remote: PeerMessageOrigination = ...
    value__ = ...


class PeerMessagePropagation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PeerMessagePropagation, values: Local (1), LocalAndRemote (3), None (0), Remote (2) """
    Local: PeerMessagePropagation = ...
    LocalAndRemote: PeerMessagePropagation = ...
    Remote: PeerMessagePropagation = ...
    value__ = ...


class PeerMessagePropagationFilter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def ShouldMessagePropagate(self, message:Message, origination:PeerMessageOrigination) -> PeerMessagePropagation:
        """ ShouldMessagePropagate(self: PeerMessagePropagationFilter, message: Message, origination: PeerMessageOrigination) -> PeerMessagePropagation """
        ...


class PeerNode(IOnlineStatus): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def MessagePropagationFilter(self) -> PeerMessagePropagationFilter:
        """
        Get: MessagePropagationFilter(self: PeerNode) -> PeerMessagePropagationFilter
        Set: MessagePropagationFilter(self: PeerNode) = value
        """
        ...

    @property
    def Port(self) -> int:
        """ Get: Port(self: PeerNode) -> int """
        ...


    def RefreshConnection(self): # -> 
        """ RefreshConnection(self: PeerNode) """
        ...

    def ToString(self) -> str:
        """ ToString(self: PeerNode) -> str """
        ...

    Offline = ...
    Online = ...


class PeerNodeAddress: # skipped bases: <type 'object'>, <type 'object'>
    """ PeerNodeAddress(endpointAddress: EndpointAddress, ipAddresses: ReadOnlyCollection[IPAddress]) """
    @property
    def EndpointAddress(self) -> EndpointAddress:
        """ Get: EndpointAddress(self: PeerNodeAddress) -> EndpointAddress """
        ...

    @property
    def IPAddresses(self) -> ReadOnlyCollection:
        """ Get: IPAddresses(self: PeerNodeAddress) -> ReadOnlyCollection[IPAddress] """
        ...



class PeerResolver: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CanShareReferrals(self) -> bool:
        """ Get: CanShareReferrals(self: PeerResolver) -> bool """
        ...


    def Initialize(self, address:EndpointAddress, binding:Binding, credentials, referralPolicy:PeerReferralPolicy): # ->  # Not found arg types: {'credentials': 'ClientCredentials'}
        """ Initialize(self: PeerResolver, address: EndpointAddress, binding: Binding, credentials: ClientCredentials, referralPolicy: PeerReferralPolicy) """
        ...

    def Register(self, meshId:str, nodeAddress:PeerNodeAddress, timeout:TimeSpan) -> object:
        """ Register(self: PeerResolver, meshId: str, nodeAddress: PeerNodeAddress, timeout: TimeSpan) -> object """
        ...

    def Resolve(self, meshId:str, maxAddresses:int, timeout:TimeSpan) -> ReadOnlyCollection:
        """ Resolve(self: PeerResolver, meshId: str, maxAddresses: int, timeout: TimeSpan) -> ReadOnlyCollection[PeerNodeAddress] """
        ...

    def Unregister(self, registrationId:object, timeout:TimeSpan): # -> 
        """ Unregister(self: PeerResolver, registrationId: object, timeout: TimeSpan) """
        ...

    def Update(self, registrationId:object, updatedNodeAddress:PeerNodeAddress, timeout:TimeSpan): # -> 
        """ Update(self: PeerResolver, registrationId: object, updatedNodeAddress: PeerNodeAddress, timeout: TimeSpan) """
        ...


class PeerSecuritySettings: # skipped bases: <type 'object'>, <type 'object'>
    """ PeerSecuritySettings() """
    @property
    def Mode(self): # -> SecurityMode
        """
        Get: Mode(self: PeerSecuritySettings) -> SecurityMode
        Set: Mode(self: PeerSecuritySettings) = value
        """
        ...

    @property
    def Transport(self): # -> PeerTransportSecuritySettings
        """
        Get: Transport(self: PeerSecuritySettings) -> PeerTransportSecuritySettings
        Set: Transport(self: PeerSecuritySettings) = value
        """
        ...


    def ShouldSerializeMode(self) -> bool:
        """ ShouldSerializeMode(self: PeerSecuritySettings) -> bool """
        ...

    def ShouldSerializeTransport(self) -> bool:
        """ ShouldSerializeTransport(self: PeerSecuritySettings) -> bool """
        ...


class PeerTransportCredentialType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PeerTransportCredentialType, values: Certificate (1), Password (0) """
    Certificate: PeerTransportCredentialType = ...
    Password: PeerTransportCredentialType = ...
    value__ = ...


class PeerTransportSecuritySettings: # skipped bases: <type 'object'>, <type 'object'>
    """ PeerTransportSecuritySettings() """
    @property
    def CredentialType(self) -> PeerTransportCredentialType:
        """
        Get: CredentialType(self: PeerTransportSecuritySettings) -> PeerTransportCredentialType
        Set: CredentialType(self: PeerTransportSecuritySettings) = value
        """
        ...



class QueuedDeliveryRequirementsMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum QueuedDeliveryRequirementsMode, values: Allowed (0), NotAllowed (2), Required (1) """
    Allowed: QueuedDeliveryRequirementsMode = ...
    NotAllowed: QueuedDeliveryRequirementsMode = ...
    Required: QueuedDeliveryRequirementsMode = ...
    value__ = ...


class QueueTransferProtocol(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum QueueTransferProtocol, values: Native (0), Srmp (1), SrmpSecure (2) """
    Native: QueueTransferProtocol = ...
    Srmp: QueueTransferProtocol = ...
    SrmpSecure: QueueTransferProtocol = ...
    value__ = ...


class QuotaExceededException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    QuotaExceededException()
    QuotaExceededException(message: str)
    QuotaExceededException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ReceiveContextEnabledAttribute(Attribute, IOperationBehavior): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ReceiveContextEnabledAttribute() """
    @property
    def ManualControl(self) -> bool:
        """
        Get: ManualControl(self: ReceiveContextEnabledAttribute) -> bool
        Set: ManualControl(self: ReceiveContextEnabledAttribute) = value
        """
        ...



class ReceiveErrorHandling(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ReceiveErrorHandling, values: Drop (1), Fault (0), Move (3), Reject (2) """
    Drop: ReceiveErrorHandling = ...
    Fault: ReceiveErrorHandling = ...
    Move: ReceiveErrorHandling = ...
    Reject: ReceiveErrorHandling = ...
    value__ = ...


class ReleaseInstanceMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ReleaseInstanceMode, values: AfterCall (2), BeforeAndAfterCall (3), BeforeCall (1), None (0) """
    AfterCall: ReleaseInstanceMode = ...
    BeforeAndAfterCall: ReleaseInstanceMode = ...
    BeforeCall: ReleaseInstanceMode = ...
    value__ = ...


class ReliableMessagingVersion: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Default(self) -> ReliableMessagingVersion:
        """ Get: Default() -> ReliableMessagingVersion """
        ...

    @property
    def WSReliableMessaging11(self) -> ReliableMessagingVersion:
        """ Get: WSReliableMessaging11() -> ReliableMessagingVersion """
        ...

    @property
    def WSReliableMessagingFebruary2005(self) -> ReliableMessagingVersion:
        """ Get: WSReliableMessagingFebruary2005() -> ReliableMessagingVersion """
        ...




class RsaEndpointIdentity(EndpointIdentity): # skipped bases: <type 'object'>
    """
    RsaEndpointIdentity(publicKey: str)
    RsaEndpointIdentity(certificate: X509Certificate2)
    RsaEndpointIdentity(identity: Claim)
    """
    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, publicKey: str)
        __new__(cls: type, certificate: X509Certificate2)
        __new__(cls: type, identity: Claim)
        """
        ...


class SecurityMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SecurityMode, values: Message (2), None (0), Transport (1), TransportWithMessageCredential (3) """
    Message: SecurityMode = ...
    Transport: SecurityMode = ...
    TransportWithMessageCredential: SecurityMode = ...
    value__ = ...


class ServerTooBusyException(CommunicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ServerTooBusyException()
    ServerTooBusyException(message: str)
    ServerTooBusyException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ServiceActivationException(CommunicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ServiceActivationException()
    ServiceActivationException(message: str)
    ServiceActivationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ServiceAuthenticationManager: # skipped bases: <type 'object'>, <type 'object'>
    """ ServiceAuthenticationManager() """
    def Authenticate(self, authPolicy:ReadOnlyCollection, listenUri:Uri, message:Message) -> Tuple_[ReadOnlyCollection, Message]:
        """ Authenticate(self: ServiceAuthenticationManager, authPolicy: ReadOnlyCollection[IAuthorizationPolicy], listenUri: Uri, message: Message) -> (ReadOnlyCollection[IAuthorizationPolicy], Message) """
        ...


class ServiceAuthorizationManager: # skipped bases: <type 'object'>, <type 'object'>
    """ ServiceAuthorizationManager() """
    def CheckAccess(self, operationContext:OperationContext, message:Message = ...) -> Tuple_[bool, Message]:
        """
        CheckAccess(self: ServiceAuthorizationManager, operationContext: OperationContext, message: Message) -> (bool, Message)
        CheckAccess(self: ServiceAuthorizationManager, operationContext: OperationContext) -> bool
        """
        ...

    def CheckAccessCore(self, *args): #cannot find CLR method
        """ CheckAccessCore(self: ServiceAuthorizationManager, operationContext: OperationContext) -> bool """
        ...

    def GetAuthorizationPolicies(self, *args): #cannot find CLR method
        """ GetAuthorizationPolicies(self: ServiceAuthorizationManager, operationContext: OperationContext) -> ReadOnlyCollection[IAuthorizationPolicy] """
        ...


class ServiceBehaviorAttribute(Attribute, IServiceBehavior): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ServiceBehaviorAttribute() """
    @property
    def AddressFilterMode(self) -> AddressFilterMode:
        """
        Get: AddressFilterMode(self: ServiceBehaviorAttribute) -> AddressFilterMode
        Set: AddressFilterMode(self: ServiceBehaviorAttribute) = value
        """
        ...

    @property
    def AutomaticSessionShutdown(self) -> bool:
        """
        Get: AutomaticSessionShutdown(self: ServiceBehaviorAttribute) -> bool
        Set: AutomaticSessionShutdown(self: ServiceBehaviorAttribute) = value
        """
        ...

    @property
    def ConcurrencyMode(self) -> ConcurrencyMode:
        """
        Get: ConcurrencyMode(self: ServiceBehaviorAttribute) -> ConcurrencyMode
        Set: ConcurrencyMode(self: ServiceBehaviorAttribute) = value
        """
        ...

    @property
    def ConfigurationName(self) -> str:
        """
        Get: ConfigurationName(self: ServiceBehaviorAttribute) -> str
        Set: ConfigurationName(self: ServiceBehaviorAttribute) = value
        """
        ...

    @property
    def EnsureOrderedDispatch(self) -> bool:
        """
        Get: EnsureOrderedDispatch(self: ServiceBehaviorAttribute) -> bool
        Set: EnsureOrderedDispatch(self: ServiceBehaviorAttribute) = value
        """
        ...

    @property
    def IgnoreExtensionDataObject(self) -> bool:
        """
        Get: IgnoreExtensionDataObject(self: ServiceBehaviorAttribute) -> bool
        Set: IgnoreExtensionDataObject(self: ServiceBehaviorAttribute) = value
        """
        ...

    @property
    def IncludeExceptionDetailInFaults(self) -> bool:
        """
        Get: IncludeExceptionDetailInFaults(self: ServiceBehaviorAttribute) -> bool
        Set: IncludeExceptionDetailInFaults(self: ServiceBehaviorAttribute) = value
        """
        ...

    @property
    def InstanceContextMode(self) -> InstanceContextMode:
        """
        Get: InstanceContextMode(self: ServiceBehaviorAttribute) -> InstanceContextMode
        Set: InstanceContextMode(self: ServiceBehaviorAttribute) = value
        """
        ...

    @property
    def MaxItemsInObjectGraph(self) -> int:
        """
        Get: MaxItemsInObjectGraph(self: ServiceBehaviorAttribute) -> int
        Set: MaxItemsInObjectGraph(self: ServiceBehaviorAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ServiceBehaviorAttribute) -> str
        Set: Name(self: ServiceBehaviorAttribute) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: ServiceBehaviorAttribute) -> str
        Set: Namespace(self: ServiceBehaviorAttribute) = value
        """
        ...

    @property
    def ReleaseServiceInstanceOnTransactionComplete(self) -> bool:
        """
        Get: ReleaseServiceInstanceOnTransactionComplete(self: ServiceBehaviorAttribute) -> bool
        Set: ReleaseServiceInstanceOnTransactionComplete(self: ServiceBehaviorAttribute) = value
        """
        ...

    @property
    def TransactionAutoCompleteOnSessionClose(self) -> bool:
        """
        Get: TransactionAutoCompleteOnSessionClose(self: ServiceBehaviorAttribute) -> bool
        Set: TransactionAutoCompleteOnSessionClose(self: ServiceBehaviorAttribute) = value
        """
        ...

    @property
    def TransactionIsolationLevel(self) -> IsolationLevel:
        """
        Get: TransactionIsolationLevel(self: ServiceBehaviorAttribute) -> IsolationLevel
        Set: TransactionIsolationLevel(self: ServiceBehaviorAttribute) = value
        """
        ...

    @property
    def TransactionTimeout(self) -> str:
        """
        Get: TransactionTimeout(self: ServiceBehaviorAttribute) -> str
        Set: TransactionTimeout(self: ServiceBehaviorAttribute) = value
        """
        ...

    @property
    def UseSynchronizationContext(self) -> bool:
        """
        Get: UseSynchronizationContext(self: ServiceBehaviorAttribute) -> bool
        Set: UseSynchronizationContext(self: ServiceBehaviorAttribute) = value
        """
        ...

    @property
    def ValidateMustUnderstand(self) -> bool:
        """
        Get: ValidateMustUnderstand(self: ServiceBehaviorAttribute) -> bool
        Set: ValidateMustUnderstand(self: ServiceBehaviorAttribute) = value
        """
        ...


    def GetWellKnownSingleton(self) -> object:
        """ GetWellKnownSingleton(self: ServiceBehaviorAttribute) -> object """
        ...

    def SetWellKnownSingleton(self, value:object): # -> 
        """ SetWellKnownSingleton(self: ServiceBehaviorAttribute, value: object) """
        ...

    def ShouldSerializeConfigurationName(self) -> bool:
        """ ShouldSerializeConfigurationName(self: ServiceBehaviorAttribute) -> bool """
        ...

    def ShouldSerializeReleaseServiceInstanceOnTransactionComplete(self) -> bool:
        """ ShouldSerializeReleaseServiceInstanceOnTransactionComplete(self: ServiceBehaviorAttribute) -> bool """
        ...

    def ShouldSerializeTransactionAutoCompleteOnSessionClose(self) -> bool:
        """ ShouldSerializeTransactionAutoCompleteOnSessionClose(self: ServiceBehaviorAttribute) -> bool """
        ...

    def ShouldSerializeTransactionIsolationLevel(self) -> bool:
        """ ShouldSerializeTransactionIsolationLevel(self: ServiceBehaviorAttribute) -> bool """
        ...

    def ShouldSerializeTransactionTimeout(self) -> bool:
        """ ShouldSerializeTransactionTimeout(self: ServiceBehaviorAttribute) -> bool """
        ...


class ServiceConfiguration: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Authentication(self): # -> ServiceAuthenticationBehavior
        """ Get: Authentication(self: ServiceConfiguration) -> ServiceAuthenticationBehavior """
        ...

    @property
    def Authorization(self): # -> ServiceAuthorizationBehavior
        """ Get: Authorization(self: ServiceConfiguration) -> ServiceAuthorizationBehavior """
        ...

    @property
    def BaseAddresses(self) -> ReadOnlyCollection:
        """ Get: BaseAddresses(self: ServiceConfiguration) -> ReadOnlyCollection[Uri] """
        ...

    @property
    def CloseTimeout(self) -> TimeSpan:
        """
        Get: CloseTimeout(self: ServiceConfiguration) -> TimeSpan
        Set: CloseTimeout(self: ServiceConfiguration) = value
        """
        ...

    @property
    def Credentials(self): # -> ServiceCredentials
        """ Get: Credentials(self: ServiceConfiguration) -> ServiceCredentials """
        ...

    @property
    def Description(self) -> ServiceDescription:
        """ Get: Description(self: ServiceConfiguration) -> ServiceDescription """
        ...

    @property
    def IdentityConfiguration(self) -> IdentityConfiguration:
        """
        Get: IdentityConfiguration(self: ServiceConfiguration) -> IdentityConfiguration
        Set: IdentityConfiguration(self: ServiceConfiguration) = value
        """
        ...

    @property
    def OpenTimeout(self) -> TimeSpan:
        """
        Get: OpenTimeout(self: ServiceConfiguration) -> TimeSpan
        Set: OpenTimeout(self: ServiceConfiguration) = value
        """
        ...

    @property
    def UseIdentityConfiguration(self) -> bool:
        """
        Get: UseIdentityConfiguration(self: ServiceConfiguration) -> bool
        Set: UseIdentityConfiguration(self: ServiceConfiguration) = value
        """
        ...


    def AddServiceEndpoint(self, *__args): # ->  # Not found arg types: {'*__args': 'ServiceEndpoint'}
        """
        AddServiceEndpoint(self: ServiceConfiguration, endpoint: ServiceEndpoint)AddServiceEndpoint(self: ServiceConfiguration, contractType: Type, binding: Binding, address: str) -> ServiceEndpoint
        AddServiceEndpoint(self: ServiceConfiguration, contractType: Type, binding: Binding, address: Uri) -> ServiceEndpoint
        AddServiceEndpoint(self: ServiceConfiguration, contractType: Type, binding: Binding, address: str, listenUri: Uri) -> ServiceEndpoint
        AddServiceEndpoint(self: ServiceConfiguration, contractType: Type, binding: Binding, address: Uri, listenUri: Uri) -> ServiceEndpoint
        """
        ...

    def EnableProtocol(self, protocol:Binding) -> Collection:
        """ EnableProtocol(self: ServiceConfiguration, protocol: Binding) -> Collection[ServiceEndpoint] """
        ...

    def LoadFromConfiguration(self, configuration:Configuration = ...): # -> 
        """ LoadFromConfiguration(self: ServiceConfiguration)LoadFromConfiguration(self: ServiceConfiguration, configuration: Configuration) """
        ...

    def SetEndpointAddress(self, endpoint, relativeAddress:str): # ->  # Not found arg types: {'endpoint': 'ServiceEndpoint'}
        """ SetEndpointAddress(self: ServiceConfiguration, endpoint: ServiceEndpoint, relativeAddress: str) """
        ...


class ServiceContractAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ServiceContractAttribute() """
    @property
    def CallbackContract(self) -> Type:
        """
        Get: CallbackContract(self: ServiceContractAttribute) -> Type
        Set: CallbackContract(self: ServiceContractAttribute) = value
        """
        ...

    @property
    def ConfigurationName(self) -> str:
        """
        Get: ConfigurationName(self: ServiceContractAttribute) -> str
        Set: ConfigurationName(self: ServiceContractAttribute) = value
        """
        ...

    @property
    def HasProtectionLevel(self) -> bool:
        """ Get: HasProtectionLevel(self: ServiceContractAttribute) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ServiceContractAttribute) -> str
        Set: Name(self: ServiceContractAttribute) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: ServiceContractAttribute) -> str
        Set: Namespace(self: ServiceContractAttribute) = value
        """
        ...

    @property
    def ProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ProtectionLevel(self: ServiceContractAttribute) -> ProtectionLevel
        Set: ProtectionLevel(self: ServiceContractAttribute) = value
        """
        ...

    @property
    def SessionMode(self): # -> SessionMode
        """
        Get: SessionMode(self: ServiceContractAttribute) -> SessionMode
        Set: SessionMode(self: ServiceContractAttribute) = value
        """
        ...



class ServiceHostBase(IDisposable, IExtensibleObject, CommunicationObject): # skipped bases: <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    @property
    def Authentication(self): # -> ServiceAuthenticationBehavior
        """ Get: Authentication(self: ServiceHostBase) -> ServiceAuthenticationBehavior """
        ...

    @property
    def Authorization(self): # -> ServiceAuthorizationBehavior
        """ Get: Authorization(self: ServiceHostBase) -> ServiceAuthorizationBehavior """
        ...

    @property
    def BaseAddresses(self) -> ReadOnlyCollection:
        """ Get: BaseAddresses(self: ServiceHostBase) -> ReadOnlyCollection[Uri] """
        ...

    @property
    def ChannelDispatchers(self): # -> ChannelDispatcherCollection
        """ Get: ChannelDispatchers(self: ServiceHostBase) -> ChannelDispatcherCollection """
        ...

    @property
    def CloseTimeout(self) -> TimeSpan:
        """
        Get: CloseTimeout(self: ServiceHostBase) -> TimeSpan
        Set: CloseTimeout(self: ServiceHostBase) = value
        """
        ...

    @property
    def Credentials(self): # -> ServiceCredentials
        """ Get: Credentials(self: ServiceHostBase) -> ServiceCredentials """
        ...

    @property
    def Description(self) -> ServiceDescription:
        """ Get: Description(self: ServiceHostBase) -> ServiceDescription """
        ...

    @property
    def ImplementedContracts(self):
        ...

    @property
    def ManualFlowControlLimit(self) -> int:
        """
        Get: ManualFlowControlLimit(self: ServiceHostBase) -> int
        Set: ManualFlowControlLimit(self: ServiceHostBase) = value
        """
        ...

    @property
    def OpenTimeout(self) -> TimeSpan:
        """
        Get: OpenTimeout(self: ServiceHostBase) -> TimeSpan
        Set: OpenTimeout(self: ServiceHostBase) = value
        """
        ...


    def AddBaseAddress(self, *args): #cannot find CLR method
        """ AddBaseAddress(self: ServiceHostBase, baseAddress: Uri) """
        ...

    def AddDefaultEndpoints(self) -> ReadOnlyCollection:
        """ AddDefaultEndpoints(self: ServiceHostBase) -> ReadOnlyCollection[ServiceEndpoint] """
        ...

    def AddServiceEndpoint(self, *__args): # ->  # Not found arg types: {'*__args': 'ServiceEndpoint'}
        """
        AddServiceEndpoint(self: ServiceHostBase, implementedContract: str, binding: Binding, address: str) -> ServiceEndpoint
        AddServiceEndpoint(self: ServiceHostBase, implementedContract: str, binding: Binding, address: Uri) -> ServiceEndpoint
        AddServiceEndpoint(self: ServiceHostBase, implementedContract: str, binding: Binding, address: str, listenUri: Uri) -> ServiceEndpoint
        AddServiceEndpoint(self: ServiceHostBase, endpoint: ServiceEndpoint)AddServiceEndpoint(self: ServiceHostBase, implementedContract: str, binding: Binding, address: Uri, listenUri: Uri) -> ServiceEndpoint
        """
        ...

    def ApplyConfiguration(self, *args): #cannot find CLR method
        """ ApplyConfiguration(self: ServiceHostBase) """
        ...

    def CreateDescription(self, *args): #cannot find CLR method
        """ CreateDescription(self: ServiceHostBase) -> (ServiceDescription, IDictionary[str, ContractDescription]) """
        ...

    def IncrementManualFlowControlLimit(self, incrementBy:int) -> int:
        """ IncrementManualFlowControlLimit(self: ServiceHostBase, incrementBy: int) -> int """
        ...

    def InitializeDescription(self, *args): #cannot find CLR method
        """ InitializeDescription(self: ServiceHostBase, baseAddresses: UriSchemeKeyedCollection) """
        ...

    def InitializeRuntime(self, *args): #cannot find CLR method
        """ InitializeRuntime(self: ServiceHostBase) """
        ...

    def LoadConfigurationSection(self, *args): #cannot find CLR method
        """ LoadConfigurationSection(self: ServiceHostBase, serviceSection: ServiceElement) """
        ...

    def ReleasePerformanceCounters(self, *args): #cannot find CLR method
        """ ReleasePerformanceCounters(self: ServiceHostBase) """
        ...

    def SetEndpointAddress(self, endpoint, relativeAddress:str): # ->  # Not found arg types: {'endpoint': 'ServiceEndpoint'}
        """ SetEndpointAddress(self: ServiceHostBase, endpoint: ServiceEndpoint, relativeAddress: str) """
        ...

    UnknownMessageReceived = ...


class ServiceHost(ServiceHostBase): # skipped bases: <type 'IDisposable'>, <type 'ICommunicationObject'>, <type 'IExtensibleObject[ServiceHostBase]'>, <type 'object'>
    """
    ServiceHost(serviceType: Type, *baseAddresses: Array[Uri])
    ServiceHost(singletonInstance: object, *baseAddresses: Array[Uri])
    """
    @property
    def SingletonInstance(self) -> object:
        """ Get: SingletonInstance(self: ServiceHost) -> object """
        ...


    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, serviceType: Type, *baseAddresses: Array[Uri])
        __new__(cls: type, singletonInstance: object, *baseAddresses: Array[Uri])
        """
        ...


class ServiceKnownTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ServiceKnownTypeAttribute(type: Type)
    ServiceKnownTypeAttribute(methodName: str)
    ServiceKnownTypeAttribute(methodName: str, declaringType: Type)
    """
    @property
    def DeclaringType(self) -> Type:
        """ Get: DeclaringType(self: ServiceKnownTypeAttribute) -> Type """
        ...

    @property
    def MethodName(self) -> str:
        """ Get: MethodName(self: ServiceKnownTypeAttribute) -> str """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: ServiceKnownTypeAttribute) -> Type """
        ...


    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type, type: Type)
        __new__(cls: type, methodName: str)
        __new__(cls: type, methodName: str, declaringType: Type)
        """
        ...


class ServiceSecurityContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    ServiceSecurityContext(authorizationPolicies: ReadOnlyCollection[IAuthorizationPolicy])
    ServiceSecurityContext(authorizationContext: AuthorizationContext)
    ServiceSecurityContext(authorizationContext: AuthorizationContext, authorizationPolicies: ReadOnlyCollection[IAuthorizationPolicy])
    """
    @property
    def Anonymous(self) -> ServiceSecurityContext:
        """ Get: Anonymous() -> ServiceSecurityContext """
        ...

    @property
    def AuthorizationContext(self) -> AuthorizationContext:
        """ Get: AuthorizationContext(self: ServiceSecurityContext) -> AuthorizationContext """
        ...

    @property
    def AuthorizationPolicies(self) -> ReadOnlyCollection:
        """
        Get: AuthorizationPolicies(self: ServiceSecurityContext) -> ReadOnlyCollection[IAuthorizationPolicy]
        Set: AuthorizationPolicies(self: ServiceSecurityContext) = value
        """
        ...

    @property
    def Current(self) -> ServiceSecurityContext:
        """ Get: Current() -> ServiceSecurityContext """
        ...

    @property
    def IsAnonymous(self) -> bool:
        """ Get: IsAnonymous(self: ServiceSecurityContext) -> bool """
        ...

    @property
    def PrimaryIdentity(self) -> IIdentity:
        """ Get: PrimaryIdentity(self: ServiceSecurityContext) -> IIdentity """
        ...

    @property
    def WindowsIdentity(self) -> WindowsIdentity:
        """ Get: WindowsIdentity(self: ServiceSecurityContext) -> WindowsIdentity """
        ...




class SessionMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SessionMode, values: Allowed (0), NotAllowed (2), Required (1) """
    Allowed: SessionMode = ...
    NotAllowed: SessionMode = ...
    Required: SessionMode = ...
    value__ = ...


class SpnEndpointIdentity(EndpointIdentity): # skipped bases: <type 'object'>
    """
    SpnEndpointIdentity(spnName: str)
    SpnEndpointIdentity(identity: Claim)
    """
    @property
    def SpnLookupTime(self) -> TimeSpan:
        """
        Get: SpnLookupTime() -> TimeSpan
        Set: SpnLookupTime() = value
        """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, spnName: str)
        __new__(cls: type, identity: Claim)
        """
        ...



class TcpClientCredentialType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TcpClientCredentialType, values: Certificate (2), None (0), Windows (1) """
    Certificate: TcpClientCredentialType = ...
    value__ = ...
    Windows: TcpClientCredentialType = ...


class TcpTransportSecurity: # skipped bases: <type 'object'>, <type 'object'>
    """ TcpTransportSecurity() """
    @property
    def ClientCredentialType(self) -> TcpClientCredentialType:
        """
        Get: ClientCredentialType(self: TcpTransportSecurity) -> TcpClientCredentialType
        Set: ClientCredentialType(self: TcpTransportSecurity) = value
        """
        ...

    @property
    def ExtendedProtectionPolicy(self) -> ExtendedProtectionPolicy:
        """
        Get: ExtendedProtectionPolicy(self: TcpTransportSecurity) -> ExtendedProtectionPolicy
        Set: ExtendedProtectionPolicy(self: TcpTransportSecurity) = value
        """
        ...

    @property
    def ProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ProtectionLevel(self: TcpTransportSecurity) -> ProtectionLevel
        Set: ProtectionLevel(self: TcpTransportSecurity) = value
        """
        ...

    @property
    def SslProtocols(self) -> SslProtocols:
        """
        Get: SslProtocols(self: TcpTransportSecurity) -> SslProtocols
        Set: SslProtocols(self: TcpTransportSecurity) = value
        """
        ...


    def ShouldSerializeExtendedProtectionPolicy(self) -> bool:
        """ ShouldSerializeExtendedProtectionPolicy(self: TcpTransportSecurity) -> bool """
        ...


class TransactionFlowAttribute(Attribute, IOperationBehavior): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ TransactionFlowAttribute(transactions: TransactionFlowOption) """
    @property
    def Transactions(self): # -> TransactionFlowOption
        """ Get: Transactions(self: TransactionFlowAttribute) -> TransactionFlowOption """
        ...


    def __new__(cls, transactions) -> Self: # Not found arg types: {'transactions': 'TransactionFlowOption'}
        """ __new__(cls: type, transactions: TransactionFlowOption) """
        ...


class TransactionFlowOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TransactionFlowOption, values: Allowed (1), Mandatory (2), NotAllowed (0) """
    Allowed: TransactionFlowOption = ...
    Mandatory: TransactionFlowOption = ...
    NotAllowed: TransactionFlowOption = ...
    value__ = ...


class TransactionProtocol: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Default(self) -> TransactionProtocol:
        """ Get: Default() -> TransactionProtocol """
        ...

    @property
    def OleTransactions(self) -> TransactionProtocol:
        """ Get: OleTransactions() -> TransactionProtocol """
        ...

    @property
    def WSAtomicTransaction11(self) -> TransactionProtocol:
        """ Get: WSAtomicTransaction11() -> TransactionProtocol """
        ...

    @property
    def WSAtomicTransactionOctober2004(self) -> TransactionProtocol:
        """ Get: WSAtomicTransactionOctober2004() -> TransactionProtocol """
        ...




class TransferMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TransferMode, values: Buffered (0), Streamed (1), StreamedRequest (2), StreamedResponse (3) """
    Buffered: TransferMode = ...
    Streamed: TransferMode = ...
    StreamedRequest: TransferMode = ...
    StreamedResponse: TransferMode = ...
    value__ = ...


class UdpBinding(IBindingRuntimePreferences, Binding): # skipped bases: <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    UdpBinding()
    UdpBinding(configurationName: str)
    """
    @property
    def DuplicateMessageHistoryLength(self) -> int:
        """
        Get: DuplicateMessageHistoryLength(self: UdpBinding) -> int
        Set: DuplicateMessageHistoryLength(self: UdpBinding) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: UdpBinding) -> Int64
        Set: MaxBufferPoolSize(self: UdpBinding) = value
        """
        ...

    @property
    def MaxPendingMessagesTotalSize(self) -> Int64:
        """
        Get: MaxPendingMessagesTotalSize(self: UdpBinding) -> Int64
        Set: MaxPendingMessagesTotalSize(self: UdpBinding) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: UdpBinding) -> Int64
        Set: MaxReceivedMessageSize(self: UdpBinding) = value
        """
        ...

    @property
    def MaxRetransmitCount(self) -> int:
        """
        Get: MaxRetransmitCount(self: UdpBinding) -> int
        Set: MaxRetransmitCount(self: UdpBinding) = value
        """
        ...

    @property
    def MulticastInterfaceId(self) -> str:
        """
        Get: MulticastInterfaceId(self: UdpBinding) -> str
        Set: MulticastInterfaceId(self: UdpBinding) = value
        """
        ...

    @property
    def ReaderQuotas(self) -> XmlDictionaryReaderQuotas:
        """
        Get: ReaderQuotas(self: UdpBinding) -> XmlDictionaryReaderQuotas
        Set: ReaderQuotas(self: UdpBinding) = value
        """
        ...

    @property
    def TextEncoding(self) -> Encoding:
        """
        Get: TextEncoding(self: UdpBinding) -> Encoding
        Set: TextEncoding(self: UdpBinding) = value
        """
        ...

    @property
    def TimeToLive(self) -> int:
        """
        Get: TimeToLive(self: UdpBinding) -> int
        Set: TimeToLive(self: UdpBinding) = value
        """
        ...


    def ShouldSerializeReaderQuotas(self) -> bool:
        """ ShouldSerializeReaderQuotas(self: UdpBinding) -> bool """
        ...

    def ShouldSerializeTextEncoding(self) -> bool:
        """ ShouldSerializeTextEncoding(self: UdpBinding) -> bool """
        ...


class UnknownMessageReceivedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Message(self) -> Message:
        """ Get: Message(self: UnknownMessageReceivedEventArgs) -> Message """
        ...



class UpnEndpointIdentity(EndpointIdentity): # skipped bases: <type 'object'>
    """
    UpnEndpointIdentity(upnName: str)
    UpnEndpointIdentity(identity: Claim)
    """
    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, upnName: str)
        __new__(cls: type, identity: Claim)
        """
        ...


class UriSchemeKeyedCollection(SynchronizedKeyedCollection): # skipped bases: <type 'ICollection'>, <type 'IList'>, <type 'IEnumerable'>, <type 'IEnumerable[Uri]'>, <type 'ICollection[Uri]'>, <type 'IList[Uri]'>, <type 'object'>
    """ UriSchemeKeyedCollection(*addresses: Array[Uri]) """
    pass

class WebHttpBinding(IBindingRuntimePreferences, Binding): # skipped bases: <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    WebHttpBinding()
    WebHttpBinding(configurationName: str)
    WebHttpBinding(securityMode: WebHttpSecurityMode)
    """
    @property
    def AllowCookies(self) -> bool:
        """
        Get: AllowCookies(self: WebHttpBinding) -> bool
        Set: AllowCookies(self: WebHttpBinding) = value
        """
        ...

    @property
    def BypassProxyOnLocal(self) -> bool:
        """
        Get: BypassProxyOnLocal(self: WebHttpBinding) -> bool
        Set: BypassProxyOnLocal(self: WebHttpBinding) = value
        """
        ...

    @property
    def ContentTypeMapper(self) -> WebContentTypeMapper:
        """
        Get: ContentTypeMapper(self: WebHttpBinding) -> WebContentTypeMapper
        Set: ContentTypeMapper(self: WebHttpBinding) = value
        """
        ...

    @property
    def CrossDomainScriptAccessEnabled(self) -> bool:
        """
        Get: CrossDomainScriptAccessEnabled(self: WebHttpBinding) -> bool
        Set: CrossDomainScriptAccessEnabled(self: WebHttpBinding) = value
        """
        ...

    @property
    def EnvelopeVersion(self) -> EnvelopeVersion:
        """ Get: EnvelopeVersion(self: WebHttpBinding) -> EnvelopeVersion """
        ...

    @property
    def HostNameComparisonMode(self) -> HostNameComparisonMode:
        """
        Get: HostNameComparisonMode(self: WebHttpBinding) -> HostNameComparisonMode
        Set: HostNameComparisonMode(self: WebHttpBinding) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: WebHttpBinding) -> Int64
        Set: MaxBufferPoolSize(self: WebHttpBinding) = value
        """
        ...

    @property
    def MaxBufferSize(self) -> int:
        """
        Get: MaxBufferSize(self: WebHttpBinding) -> int
        Set: MaxBufferSize(self: WebHttpBinding) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: WebHttpBinding) -> Int64
        Set: MaxReceivedMessageSize(self: WebHttpBinding) = value
        """
        ...

    @property
    def ProxyAddress(self) -> Uri:
        """
        Get: ProxyAddress(self: WebHttpBinding) -> Uri
        Set: ProxyAddress(self: WebHttpBinding) = value
        """
        ...

    @property
    def ReaderQuotas(self) -> XmlDictionaryReaderQuotas:
        """
        Get: ReaderQuotas(self: WebHttpBinding) -> XmlDictionaryReaderQuotas
        Set: ReaderQuotas(self: WebHttpBinding) = value
        """
        ...

    @property
    def Security(self): # -> WebHttpSecurity
        """
        Get: Security(self: WebHttpBinding) -> WebHttpSecurity
        Set: Security(self: WebHttpBinding) = value
        """
        ...

    @property
    def TransferMode(self) -> TransferMode:
        """
        Get: TransferMode(self: WebHttpBinding) -> TransferMode
        Set: TransferMode(self: WebHttpBinding) = value
        """
        ...

    @property
    def UseDefaultWebProxy(self) -> bool:
        """
        Get: UseDefaultWebProxy(self: WebHttpBinding) -> bool
        Set: UseDefaultWebProxy(self: WebHttpBinding) = value
        """
        ...

    @property
    def WriteEncoding(self) -> Encoding:
        """
        Get: WriteEncoding(self: WebHttpBinding) -> Encoding
        Set: WriteEncoding(self: WebHttpBinding) = value
        """
        ...


    def ShouldSerializeReaderQuotas(self) -> bool:
        """ ShouldSerializeReaderQuotas(self: WebHttpBinding) -> bool """
        ...

    def ShouldSerializeSecurity(self) -> bool:
        """ ShouldSerializeSecurity(self: WebHttpBinding) -> bool """
        ...

    def ShouldSerializeWriteEncoding(self) -> bool:
        """ ShouldSerializeWriteEncoding(self: WebHttpBinding) -> bool """
        ...


class WebHttpSecurity: # skipped bases: <type 'object'>, <type 'object'>
    """ WebHttpSecurity() """
    @property
    def Mode(self): # -> WebHttpSecurityMode
        """
        Get: Mode(self: WebHttpSecurity) -> WebHttpSecurityMode
        Set: Mode(self: WebHttpSecurity) = value
        """
        ...

    @property
    def Transport(self) -> HttpTransportSecurity:
        """
        Get: Transport(self: WebHttpSecurity) -> HttpTransportSecurity
        Set: Transport(self: WebHttpSecurity) = value
        """
        ...


    def ShouldSerializeMode(self) -> bool:
        """ ShouldSerializeMode(self: WebHttpSecurity) -> bool """
        ...

    def ShouldSerializeTransport(self) -> bool:
        """ ShouldSerializeTransport(self: WebHttpSecurity) -> bool """
        ...


class WebHttpSecurityMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WebHttpSecurityMode, values: None (0), Transport (1), TransportCredentialOnly (2) """
    Transport: WebHttpSecurityMode = ...
    TransportCredentialOnly: WebHttpSecurityMode = ...
    value__ = ...


class WorkflowServiceHost(ServiceHostBase): # skipped bases: <type 'IDisposable'>, <type 'ICommunicationObject'>, <type 'IExtensibleObject[ServiceHostBase]'>, <type 'object'>
    """
    WorkflowServiceHost(workflowType: Type, *baseAddress: Array[Uri])
    WorkflowServiceHost(workflowDefinitionPath: str, *baseAddress: Array[Uri])
    WorkflowServiceHost(workflowDefinitionPath: str, ruleDefinitionPath: str, *baseAddress: Array[Uri])
    WorkflowServiceHost(workflowDefinitionPath: str, ruleDefinitionPath: str, typeProvider: ITypeProvider, *baseAddress: Array[Uri])
    WorkflowServiceHost(workflowDefinition: Stream, *baseAddress: Array[Uri])
    WorkflowServiceHost(workflowDefinition: Stream, ruleDefinition: Stream, *baseAddress: Array[Uri])
    WorkflowServiceHost(workflowDefinition: Stream, ruleDefinition: Stream, typeProvider: ITypeProvider, *baseAddress: Array[Uri])
    """
    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, workflowType: Type, *baseAddress: Array[Uri])
        __new__(cls: type, workflowDefinitionPath: str, *baseAddress: Array[Uri])
        __new__(cls: type, workflowDefinitionPath: str, ruleDefinitionPath: str, *baseAddress: Array[Uri])
        __new__(cls: type, workflowDefinitionPath: str, ruleDefinitionPath: str, typeProvider: ITypeProvider, *baseAddress: Array[Uri])
        __new__(cls: type, workflowDefinition: Stream, *baseAddress: Array[Uri])
        __new__(cls: type, workflowDefinition: Stream, ruleDefinition: Stream, *baseAddress: Array[Uri])
        __new__(cls: type, workflowDefinition: Stream, ruleDefinition: Stream, typeProvider: ITypeProvider, *baseAddress: Array[Uri])
        __new__(cls: type)
        """
        ...


class WSHttpBindingBase(IBindingRuntimePreferences, Binding): # skipped bases: <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """ no doc """
    @property
    def BypassProxyOnLocal(self) -> bool:
        """
        Get: BypassProxyOnLocal(self: WSHttpBindingBase) -> bool
        Set: BypassProxyOnLocal(self: WSHttpBindingBase) = value
        """
        ...

    @property
    def EnvelopeVersion(self) -> EnvelopeVersion:
        """ Get: EnvelopeVersion(self: WSHttpBindingBase) -> EnvelopeVersion """
        ...

    @property
    def HostNameComparisonMode(self) -> HostNameComparisonMode:
        """
        Get: HostNameComparisonMode(self: WSHttpBindingBase) -> HostNameComparisonMode
        Set: HostNameComparisonMode(self: WSHttpBindingBase) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: WSHttpBindingBase) -> Int64
        Set: MaxBufferPoolSize(self: WSHttpBindingBase) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: WSHttpBindingBase) -> Int64
        Set: MaxReceivedMessageSize(self: WSHttpBindingBase) = value
        """
        ...

    @property
    def MessageEncoding(self): # -> WSMessageEncoding
        """
        Get: MessageEncoding(self: WSHttpBindingBase) -> WSMessageEncoding
        Set: MessageEncoding(self: WSHttpBindingBase) = value
        """
        ...

    @property
    def ProxyAddress(self) -> Uri:
        """
        Get: ProxyAddress(self: WSHttpBindingBase) -> Uri
        Set: ProxyAddress(self: WSHttpBindingBase) = value
        """
        ...

    @property
    def ReaderQuotas(self) -> XmlDictionaryReaderQuotas:
        """
        Get: ReaderQuotas(self: WSHttpBindingBase) -> XmlDictionaryReaderQuotas
        Set: ReaderQuotas(self: WSHttpBindingBase) = value
        """
        ...

    @property
    def ReliableSession(self) -> OptionalReliableSession:
        """
        Get: ReliableSession(self: WSHttpBindingBase) -> OptionalReliableSession
        Set: ReliableSession(self: WSHttpBindingBase) = value
        """
        ...

    @property
    def TextEncoding(self) -> Encoding:
        """
        Get: TextEncoding(self: WSHttpBindingBase) -> Encoding
        Set: TextEncoding(self: WSHttpBindingBase) = value
        """
        ...

    @property
    def TransactionFlow(self) -> bool:
        """
        Get: TransactionFlow(self: WSHttpBindingBase) -> bool
        Set: TransactionFlow(self: WSHttpBindingBase) = value
        """
        ...

    @property
    def UseDefaultWebProxy(self) -> bool:
        """
        Get: UseDefaultWebProxy(self: WSHttpBindingBase) -> bool
        Set: UseDefaultWebProxy(self: WSHttpBindingBase) = value
        """
        ...


    def CreateMessageSecurity(self, *args): #cannot find CLR method
        """ CreateMessageSecurity(self: WSHttpBindingBase) -> SecurityBindingElement """
        ...

    def GetTransport(self, *args): #cannot find CLR method
        """ GetTransport(self: WSHttpBindingBase) -> TransportBindingElement """
        ...

    def ShouldSerializeReaderQuotas(self) -> bool:
        """ ShouldSerializeReaderQuotas(self: WSHttpBindingBase) -> bool """
        ...

    def ShouldSerializeReliableSession(self) -> bool:
        """ ShouldSerializeReliableSession(self: WSHttpBindingBase) -> bool """
        ...

    def ShouldSerializeTextEncoding(self) -> bool:
        """ ShouldSerializeTextEncoding(self: WSHttpBindingBase) -> bool """
        ...


class WSFederationHttpBinding(WSHttpBindingBase): # skipped bases: <type 'IBindingRuntimePreferences'>, <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    WSFederationHttpBinding(configName: str)
    WSFederationHttpBinding()
    WSFederationHttpBinding(securityMode: WSFederationHttpSecurityMode)
    WSFederationHttpBinding(securityMode: WSFederationHttpSecurityMode, reliableSessionEnabled: bool)
    """
    @property
    def PrivacyNoticeAt(self) -> Uri:
        """
        Get: PrivacyNoticeAt(self: WSFederationHttpBinding) -> Uri
        Set: PrivacyNoticeAt(self: WSFederationHttpBinding) = value
        """
        ...

    @property
    def PrivacyNoticeVersion(self) -> int:
        """
        Get: PrivacyNoticeVersion(self: WSFederationHttpBinding) -> int
        Set: PrivacyNoticeVersion(self: WSFederationHttpBinding) = value
        """
        ...

    @property
    def Security(self): # -> WSFederationHttpSecurity
        """
        Get: Security(self: WSFederationHttpBinding) -> WSFederationHttpSecurity
        Set: Security(self: WSFederationHttpBinding) = value
        """
        ...


    def ShouldSerializeSecurity(self) -> bool:
        """ ShouldSerializeSecurity(self: WSFederationHttpBinding) -> bool """
        ...


class WS2007FederationHttpBinding(WSFederationHttpBinding): # skipped bases: <type 'IBindingRuntimePreferences'>, <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    WS2007FederationHttpBinding(configName: str)
    WS2007FederationHttpBinding()
    WS2007FederationHttpBinding(securityMode: WSFederationHttpSecurityMode)
    WS2007FederationHttpBinding(securityMode: WSFederationHttpSecurityMode, reliableSessionEnabled: bool)
    """
    pass

class WSHttpBinding(WSHttpBindingBase): # skipped bases: <type 'IBindingRuntimePreferences'>, <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    WSHttpBinding(configName: str)
    WSHttpBinding()
    WSHttpBinding(securityMode: SecurityMode)
    WSHttpBinding(securityMode: SecurityMode, reliableSessionEnabled: bool)
    """
    @property
    def AllowCookies(self) -> bool:
        """
        Get: AllowCookies(self: WSHttpBinding) -> bool
        Set: AllowCookies(self: WSHttpBinding) = value
        """
        ...

    @property
    def Security(self): # -> WSHttpSecurity
        """
        Get: Security(self: WSHttpBinding) -> WSHttpSecurity
        Set: Security(self: WSHttpBinding) = value
        """
        ...


    def BuildChannelFactory(self, parameters): # -> IChannelFactory # Not found arg types: {'parameters': 'BindingParameterCollection'}
        """ BuildChannelFactory[TChannel](self: WSHttpBinding, parameters: BindingParameterCollection) -> IChannelFactory[TChannel] """
        ...

    def ShouldSerializeSecurity(self) -> bool:
        """ ShouldSerializeSecurity(self: WSHttpBinding) -> bool """
        ...


class WS2007HttpBinding(WSHttpBinding): # skipped bases: <type 'IBindingRuntimePreferences'>, <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    WS2007HttpBinding(configName: str)
    WS2007HttpBinding()
    WS2007HttpBinding(securityMode: SecurityMode)
    WS2007HttpBinding(securityMode: SecurityMode, reliableSessionEnabled: bool)
    """
    pass

class WSDualHttpBinding(IBindingRuntimePreferences, Binding): # skipped bases: <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    WSDualHttpBinding(configName: str)
    WSDualHttpBinding(securityMode: WSDualHttpSecurityMode)
    WSDualHttpBinding()
    """
    @property
    def BypassProxyOnLocal(self) -> bool:
        """
        Get: BypassProxyOnLocal(self: WSDualHttpBinding) -> bool
        Set: BypassProxyOnLocal(self: WSDualHttpBinding) = value
        """
        ...

    @property
    def ClientBaseAddress(self) -> Uri:
        """
        Get: ClientBaseAddress(self: WSDualHttpBinding) -> Uri
        Set: ClientBaseAddress(self: WSDualHttpBinding) = value
        """
        ...

    @property
    def EnvelopeVersion(self) -> EnvelopeVersion:
        """ Get: EnvelopeVersion(self: WSDualHttpBinding) -> EnvelopeVersion """
        ...

    @property
    def HostNameComparisonMode(self) -> HostNameComparisonMode:
        """
        Get: HostNameComparisonMode(self: WSDualHttpBinding) -> HostNameComparisonMode
        Set: HostNameComparisonMode(self: WSDualHttpBinding) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: WSDualHttpBinding) -> Int64
        Set: MaxBufferPoolSize(self: WSDualHttpBinding) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: WSDualHttpBinding) -> Int64
        Set: MaxReceivedMessageSize(self: WSDualHttpBinding) = value
        """
        ...

    @property
    def MessageEncoding(self): # -> WSMessageEncoding
        """
        Get: MessageEncoding(self: WSDualHttpBinding) -> WSMessageEncoding
        Set: MessageEncoding(self: WSDualHttpBinding) = value
        """
        ...

    @property
    def ProxyAddress(self) -> Uri:
        """
        Get: ProxyAddress(self: WSDualHttpBinding) -> Uri
        Set: ProxyAddress(self: WSDualHttpBinding) = value
        """
        ...

    @property
    def ReaderQuotas(self) -> XmlDictionaryReaderQuotas:
        """
        Get: ReaderQuotas(self: WSDualHttpBinding) -> XmlDictionaryReaderQuotas
        Set: ReaderQuotas(self: WSDualHttpBinding) = value
        """
        ...

    @property
    def ReliableSession(self) -> ReliableSession:
        """
        Get: ReliableSession(self: WSDualHttpBinding) -> ReliableSession
        Set: ReliableSession(self: WSDualHttpBinding) = value
        """
        ...

    @property
    def Security(self): # -> WSDualHttpSecurity
        """
        Get: Security(self: WSDualHttpBinding) -> WSDualHttpSecurity
        Set: Security(self: WSDualHttpBinding) = value
        """
        ...

    @property
    def TextEncoding(self) -> Encoding:
        """
        Get: TextEncoding(self: WSDualHttpBinding) -> Encoding
        Set: TextEncoding(self: WSDualHttpBinding) = value
        """
        ...

    @property
    def TransactionFlow(self) -> bool:
        """
        Get: TransactionFlow(self: WSDualHttpBinding) -> bool
        Set: TransactionFlow(self: WSDualHttpBinding) = value
        """
        ...

    @property
    def UseDefaultWebProxy(self) -> bool:
        """
        Get: UseDefaultWebProxy(self: WSDualHttpBinding) -> bool
        Set: UseDefaultWebProxy(self: WSDualHttpBinding) = value
        """
        ...


    def ShouldSerializeReaderQuotas(self) -> bool:
        """ ShouldSerializeReaderQuotas(self: WSDualHttpBinding) -> bool """
        ...

    def ShouldSerializeReliableSession(self) -> bool:
        """ ShouldSerializeReliableSession(self: WSDualHttpBinding) -> bool """
        ...

    def ShouldSerializeSecurity(self) -> bool:
        """ ShouldSerializeSecurity(self: WSDualHttpBinding) -> bool """
        ...

    def ShouldSerializeTextEncoding(self) -> bool:
        """ ShouldSerializeTextEncoding(self: WSDualHttpBinding) -> bool """
        ...


class WSDualHttpSecurity: # skipped bases: <type 'object'>, <type 'object'>
    """ WSDualHttpSecurity() """
    @property
    def Message(self) -> MessageSecurityOverHttp:
        """
        Get: Message(self: WSDualHttpSecurity) -> MessageSecurityOverHttp
        Set: Message(self: WSDualHttpSecurity) = value
        """
        ...

    @property
    def Mode(self): # -> WSDualHttpSecurityMode
        """
        Get: Mode(self: WSDualHttpSecurity) -> WSDualHttpSecurityMode
        Set: Mode(self: WSDualHttpSecurity) = value
        """
        ...


    def ShouldSerializeMessage(self) -> bool:
        """ ShouldSerializeMessage(self: WSDualHttpSecurity) -> bool """
        ...

    def ShouldSerializeMode(self) -> bool:
        """ ShouldSerializeMode(self: WSDualHttpSecurity) -> bool """
        ...


class WSDualHttpSecurityMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WSDualHttpSecurityMode, values: Message (1), None (0) """
    Message: WSDualHttpSecurityMode = ...
    value__ = ...


class WSFederationHttpSecurity: # skipped bases: <type 'object'>, <type 'object'>
    """ WSFederationHttpSecurity() """
    @property
    def Message(self) -> FederatedMessageSecurityOverHttp:
        """
        Get: Message(self: WSFederationHttpSecurity) -> FederatedMessageSecurityOverHttp
        Set: Message(self: WSFederationHttpSecurity) = value
        """
        ...

    @property
    def Mode(self): # -> WSFederationHttpSecurityMode
        """
        Get: Mode(self: WSFederationHttpSecurity) -> WSFederationHttpSecurityMode
        Set: Mode(self: WSFederationHttpSecurity) = value
        """
        ...


    def ShouldSerializeMessage(self) -> bool:
        """ ShouldSerializeMessage(self: WSFederationHttpSecurity) -> bool """
        ...

    def ShouldSerializeMode(self) -> bool:
        """ ShouldSerializeMode(self: WSFederationHttpSecurity) -> bool """
        ...


class WSFederationHttpSecurityMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WSFederationHttpSecurityMode, values: Message (1), None (0), TransportWithMessageCredential (2) """
    Message: WSFederationHttpSecurityMode = ...
    TransportWithMessageCredential: WSFederationHttpSecurityMode = ...
    value__ = ...


class WSHttpContextBinding(WSHttpBinding): # skipped bases: <type 'IBindingRuntimePreferences'>, <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    WSHttpContextBinding()
    WSHttpContextBinding(securityMode: SecurityMode)
    WSHttpContextBinding(configName: str)
    WSHttpContextBinding(securityMode: SecurityMode, reliableSessionEnabled: bool)
    """
    @property
    def ClientCallbackAddress(self) -> Uri:
        """
        Get: ClientCallbackAddress(self: WSHttpContextBinding) -> Uri
        Set: ClientCallbackAddress(self: WSHttpContextBinding) = value
        """
        ...

    @property
    def ContextManagementEnabled(self) -> bool:
        """
        Get: ContextManagementEnabled(self: WSHttpContextBinding) -> bool
        Set: ContextManagementEnabled(self: WSHttpContextBinding) = value
        """
        ...

    @property
    def ContextProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ContextProtectionLevel(self: WSHttpContextBinding) -> ProtectionLevel
        Set: ContextProtectionLevel(self: WSHttpContextBinding) = value
        """
        ...



class WSHttpSecurity: # skipped bases: <type 'object'>, <type 'object'>
    """ WSHttpSecurity() """
    @property
    def Message(self) -> NonDualMessageSecurityOverHttp:
        """
        Get: Message(self: WSHttpSecurity) -> NonDualMessageSecurityOverHttp
        Set: Message(self: WSHttpSecurity) = value
        """
        ...

    @property
    def Mode(self) -> SecurityMode:
        """
        Get: Mode(self: WSHttpSecurity) -> SecurityMode
        Set: Mode(self: WSHttpSecurity) = value
        """
        ...

    @property
    def Transport(self) -> HttpTransportSecurity:
        """
        Get: Transport(self: WSHttpSecurity) -> HttpTransportSecurity
        Set: Transport(self: WSHttpSecurity) = value
        """
        ...


    def ShouldSerializeMessage(self) -> bool:
        """ ShouldSerializeMessage(self: WSHttpSecurity) -> bool """
        ...

    def ShouldSerializeMode(self) -> bool:
        """ ShouldSerializeMode(self: WSHttpSecurity) -> bool """
        ...

    def ShouldSerializeTransport(self) -> bool:
        """ ShouldSerializeTransport(self: WSHttpSecurity) -> bool """
        ...


class WSMessageEncoding(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WSMessageEncoding, values: Mtom (1), Text (0) """
    Mtom: WSMessageEncoding = ...
    Text: WSMessageEncoding = ...
    value__ = ...


class X509CertificateEndpointIdentity(EndpointIdentity): # skipped bases: <type 'object'>
    """
    X509CertificateEndpointIdentity(certificate: X509Certificate2)
    X509CertificateEndpointIdentity(primaryCertificate: X509Certificate2, supportingCertificates: X509Certificate2Collection)
    """
    @property
    def Certificates(self) -> X509Certificate2Collection:
        """ Get: Certificates(self: X509CertificateEndpointIdentity) -> X509Certificate2Collection """
        ...


    def __new__(cls, *__args:X509Certificate2) -> Self:
        """
        __new__(cls: type, certificate: X509Certificate2)
        __new__(cls: type, primaryCertificate: X509Certificate2, supportingCertificates: X509Certificate2Collection)
        """
        ...


class XmlSerializerFormatAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ XmlSerializerFormatAttribute() """
    @property
    def Style(self) -> OperationFormatStyle:
        """
        Get: Style(self: XmlSerializerFormatAttribute) -> OperationFormatStyle
        Set: Style(self: XmlSerializerFormatAttribute) = value
        """
        ...

    @property
    def SupportFaults(self) -> bool:
        """
        Get: SupportFaults(self: XmlSerializerFormatAttribute) -> bool
        Set: SupportFaults(self: XmlSerializerFormatAttribute) = value
        """
        ...

    @property
    def Use(self) -> OperationFormatUse:
        """
        Get: Use(self: XmlSerializerFormatAttribute) -> OperationFormatUse
        Set: Use(self: XmlSerializerFormatAttribute) = value
        """
        ...



class XPathMessageQuery(MessageQuery): # skipped bases: <type 'object'>
    """
    XPathMessageQuery()
    XPathMessageQuery(expression: str)
    XPathMessageQuery(expression: str, context: XsltContext)
    XPathMessageQuery(expression: str, namespaces: XmlNamespaceManager)
    """
    @property
    def Expression(self) -> str:
        """
        Get: Expression(self: XPathMessageQuery) -> str
        Set: Expression(self: XPathMessageQuery) = value
        """
        ...

    @property
    def Namespaces(self) -> XmlNamespaceManager:
        """
        Get: Namespaces(self: XPathMessageQuery) -> XmlNamespaceManager
        Set: Namespaces(self: XPathMessageQuery) = value
        """
        ...


    def __new__(cls, expression:str = ..., *__args:XsltContext) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, expression: str)
        __new__(cls: type, expression: str, context: XsltContext)
        __new__(cls: type, expression: str, namespaces: XmlNamespaceManager)
        """
        ...


# variables with complex values

