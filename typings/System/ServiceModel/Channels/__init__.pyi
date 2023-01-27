# encoding: utf-8
# module System.ServiceModel.Channels calls itself Channels
# from System.ServiceModel.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.ServiceModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.ServiceModel.Channels, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.JScript import Binding

from System import (Array, AsyncCallback, Enum, IAsyncResult, IDisposable, 
    IEquatable, Int64, Nullable, TimeSpan, Uri)

from System.CodeDom import CodeCompileUnit

from System.CodeDom.Compiler import CodeDomProvider

from System.Collections import ICollection, IDictionary, IEnumerable

from System.Collections.Generic import KeyedByTypeCollection

from System.Collections.ObjectModel import (Collection, ReadOnlyCollection, 
    ReadOnlyDictionary)

from System.IO import Stream

from System.Messaging import Message

from System.Net import (AuthenticationSchemes, CookieContainer, 
    HttpStatusCode, IPAddress, WebHeaderCollection)

from System.Net.Http import (HttpMessageHandler, HttpRequestMessage, 
    HttpResponseMessage)

from System.Net.Security import ProtectionLevel

from System.Net.WebSockets import (WebSocket, WebSocketCloseStatus, 
    WebSocketContext, WebSocketMessageType)

from System.Runtime.DurableInstancing import InstanceKey

from System.Runtime.Remoting.Channels import IChannel

from System.Runtime.Serialization import SerializationInfo, StreamingContext

from System.Security.Authentication import SslProtocols

from System.Security.Authentication.ExtendedProtection import (
    ExtendedProtectionPolicy)

from System.ServiceModel import (CommunicationException, DeadLetterQueue, 
    EndpointAddress, EndpointIdentity, EnvelopeVersion, FaultCode, 
    FaultReason, HostNameComparisonMode, ICommunicationObject, 
    IDefaultCommunicationTimeouts, MessageHeader, MessageSecurityVersion, 
    MsmqTransportSecurity, PeerResolver, PeerSecuritySettings, 
    QueueTransferProtocol, ReceiveErrorHandling, ReliableMessagingVersion, 
    TransactionProtocol, TransferMode)

from System.ServiceModel.Configuration import MsmqBindingElementBase

from System.ServiceModel.Description import (IPolicyExportExtension, 
    IPolicyImportExtension, IWsdlExportExtension, IWsdlImportExtension, 
    ListenUriMode)

from System.ServiceModel.PeerResolvers import PeerReferralPolicy

from System.ServiceModel.Security import (ChannelProtectionRequirements, 
    IdentityVerifier, MessageProtectionOrder, NonceCache, 
    SecurityAlgorithmSuite, SecurityKeyEntropyMode, SecurityMessageProperty)

from System.ServiceModel.Security.Tokens import (
    IssuedSecurityTokenParameters, SecurityTokenParameters, 
    SupportingTokenParameters)

from System.Text import Encoding

from System.Transactions import Transaction

from System.Web.Routing import RequestContext

from System.Web.Services.Description import WebReferenceOptions

from System.Xml import (UniqueId, XmlDictionaryReader, 
    XmlDictionaryReaderQuotas, XmlDictionaryString, XmlDictionaryWriter, 
    XmlElement, XmlWriter)

from System.Xml.Linq import XName, XNamespace

from System.Xml.XPath import IXPathNavigable

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (
    AsymmetricSecurityBindingElement, BindingContext, 
    BindingElementCollection, BindingParameterCollection, BoundEvent, 
    CompressionFormat, ContextExchangeMechanism, CustomBinding, Func, 
    IChannelFactory, IChannelListener, IContextSessionProvider, 
    IMergeEnabledMessageProperty, IMessageProperty, ISessionChannel, 
    ITransportPolicyImport, IWmiInstanceProvider, LocalClientSecuritySettings, 
    LocalServiceSecuritySettings, MessageBuffer, MessageEncoderFactory, 
    MessageFault, MessageHeaders, MessageProperties, MessageState, 
    MessageVersion, ReceiveContextState, RedirectionScope, RedirectionType, 
    SecurityHeaderLayout, StreamUpgradeProvider, 
    SymmetricSecurityBindingElement, T, TransportSecurityBindingElement, 
    UnderstoodHeaders, WebSocketTransportSettings, WebSocketTransportUsage, 
    XmlObjectSerializer, field#)
"""

# no functions
# classes

class AddressHeader: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: AddressHeader) -> str """
        ...

    @property
    def Namespace(self) -> str:
        """ Get: Namespace(self: AddressHeader) -> str """
        ...


    @staticmethod
    def CreateAddressHeader(*__args:object) -> AddressHeader:
        """
        CreateAddressHeader(value: object) -> AddressHeader
        CreateAddressHeader(value: object, serializer: XmlObjectSerializer) -> AddressHeader
        CreateAddressHeader(name: str, ns: str, value: object) -> AddressHeader
        CreateAddressHeader(name: str, ns: str, value: object, serializer: XmlObjectSerializer) -> AddressHeader
        """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: AddressHeader, obj: object) -> bool """
        ...

    def GetAddressHeaderReader(self) -> XmlDictionaryReader:
        """ GetAddressHeaderReader(self: AddressHeader) -> XmlDictionaryReader """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: AddressHeader) -> int """
        ...

    def GetValue(self, serializer = ...): # -> T # Not found arg types: {'serializer': 'XmlObjectSerializer'}
        """
        GetValue[T](self: AddressHeader) -> T
        GetValue[T](self: AddressHeader, serializer: XmlObjectSerializer) -> T
        """
        ...

    def OnWriteAddressHeaderContents(self, *args): #cannot find CLR method
        """ OnWriteAddressHeaderContents(self: AddressHeader, writer: XmlDictionaryWriter) """
        ...

    def OnWriteStartAddressHeader(self, *args): #cannot find CLR method
        """ OnWriteStartAddressHeader(self: AddressHeader, writer: XmlDictionaryWriter) """
        ...

    def ToMessageHeader(self) -> MessageHeader:
        """ ToMessageHeader(self: AddressHeader) -> MessageHeader """
        ...

    def WriteAddressHeader(self, writer:XmlWriter): # -> 
        """ WriteAddressHeader(self: AddressHeader, writer: XmlWriter)WriteAddressHeader(self: AddressHeader, writer: XmlDictionaryWriter) """
        ...

    def WriteAddressHeaderContents(self, writer:XmlDictionaryWriter): # -> 
        """ WriteAddressHeaderContents(self: AddressHeader, writer: XmlDictionaryWriter) """
        ...

    def WriteStartAddressHeader(self, writer:XmlDictionaryWriter): # -> 
        """ WriteStartAddressHeader(self: AddressHeader, writer: XmlDictionaryWriter) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class AddressHeaderCollection(ReadOnlyCollection): # skipped bases: <type 'IReadOnlyCollection[AddressHeader]'>, <type 'ICollection[AddressHeader]'>, <type 'IEnumerable'>, <type 'IEnumerable[AddressHeader]'>, <type 'IList'>, <type 'IReadOnlyList[AddressHeader]'>, <type 'IList[AddressHeader]'>, <type 'ICollection'>, <type 'object'>
    """
    AddressHeaderCollection()
    AddressHeaderCollection(addressHeaders: IEnumerable[AddressHeader])
    """
    def AddHeadersTo(self, message:Message): # -> 
        """ AddHeadersTo(self: AddressHeaderCollection, message: Message) """
        ...

    def FindAll(self, name:str, ns:str) -> Array:
        """ FindAll(self: AddressHeaderCollection, name: str, ns: str) -> Array[AddressHeader] """
        ...

    def FindHeader(self, name:str, ns:str) -> AddressHeader:
        """ FindHeader(self: AddressHeaderCollection, name: str, ns: str) -> AddressHeader """
        ...


class AddressingVersion: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def WSAddressing10(self) -> AddressingVersion:
        """ Get: WSAddressing10() -> AddressingVersion """
        ...

    @property
    def WSAddressingAugust2004(self) -> AddressingVersion:
        """ Get: WSAddressingAugust2004() -> AddressingVersion """
        ...


    def ToString(self) -> str:
        """ ToString(self: AddressingVersion) -> str """
        ...



class ApplicationContainerSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def PackageFullName(self) -> str:
        """
        Get: PackageFullName(self: ApplicationContainerSettings) -> str
        Set: PackageFullName(self: ApplicationContainerSettings) = value
        """
        ...

    @property
    def SessionId(self) -> int:
        """
        Get: SessionId(self: ApplicationContainerSettings) -> int
        Set: SessionId(self: ApplicationContainerSettings) = value
        """
        ...


    CurrentSession: int = ...
    ServiceSession: int = ...


class BindingElement: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def BuildChannelFactory(self, context): # -> IChannelFactory # Not found arg types: {'context': 'BindingContext'}
        """ BuildChannelFactory[TChannel](self: BindingElement, context: BindingContext) -> IChannelFactory[TChannel] """
        ...

    def BuildChannelListener(self, context): # -> IChannelListener # Not found arg types: {'context': 'BindingContext'}
        """ BuildChannelListener[TChannel](self: BindingElement, context: BindingContext) -> IChannelListener[TChannel] """
        ...

    def CanBuildChannelFactory(self, context) -> bool: # Not found arg types: {'context': 'BindingContext'}
        """ CanBuildChannelFactory[TChannel](self: BindingElement, context: BindingContext) -> bool """
        ...

    def CanBuildChannelListener(self, context) -> bool: # Not found arg types: {'context': 'BindingContext'}
        """ CanBuildChannelListener[TChannel](self: BindingElement, context: BindingContext) -> bool """
        ...

    def Clone(self) -> BindingElement:
        """ Clone(self: BindingElement) -> BindingElement """
        ...

    def GetProperty(self, context): # -> T # Not found arg types: {'context': 'BindingContext'}
        """ GetProperty[T](self: BindingElement, context: BindingContext) -> T """
        ...


class SecurityBindingElement(BindingElement): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AllowInsecureTransport(self) -> bool:
        """
        Get: AllowInsecureTransport(self: SecurityBindingElement) -> bool
        Set: AllowInsecureTransport(self: SecurityBindingElement) = value
        """
        ...

    @property
    def DefaultAlgorithmSuite(self) -> SecurityAlgorithmSuite:
        """
        Get: DefaultAlgorithmSuite(self: SecurityBindingElement) -> SecurityAlgorithmSuite
        Set: DefaultAlgorithmSuite(self: SecurityBindingElement) = value
        """
        ...

    @property
    def EnableUnsecuredResponse(self) -> bool:
        """
        Get: EnableUnsecuredResponse(self: SecurityBindingElement) -> bool
        Set: EnableUnsecuredResponse(self: SecurityBindingElement) = value
        """
        ...

    @property
    def EndpointSupportingTokenParameters(self) -> SupportingTokenParameters:
        """ Get: EndpointSupportingTokenParameters(self: SecurityBindingElement) -> SupportingTokenParameters """
        ...

    @property
    def IncludeTimestamp(self) -> bool:
        """
        Get: IncludeTimestamp(self: SecurityBindingElement) -> bool
        Set: IncludeTimestamp(self: SecurityBindingElement) = value
        """
        ...

    @property
    def KeyEntropyMode(self) -> SecurityKeyEntropyMode:
        """
        Get: KeyEntropyMode(self: SecurityBindingElement) -> SecurityKeyEntropyMode
        Set: KeyEntropyMode(self: SecurityBindingElement) = value
        """
        ...

    @property
    def LocalClientSettings(self): # -> LocalClientSecuritySettings
        """ Get: LocalClientSettings(self: SecurityBindingElement) -> LocalClientSecuritySettings """
        ...

    @property
    def LocalServiceSettings(self): # -> LocalServiceSecuritySettings
        """ Get: LocalServiceSettings(self: SecurityBindingElement) -> LocalServiceSecuritySettings """
        ...

    @property
    def MessageSecurityVersion(self) -> MessageSecurityVersion:
        """
        Get: MessageSecurityVersion(self: SecurityBindingElement) -> MessageSecurityVersion
        Set: MessageSecurityVersion(self: SecurityBindingElement) = value
        """
        ...

    @property
    def OperationSupportingTokenParameters(self) -> IDictionary:
        """ Get: OperationSupportingTokenParameters(self: SecurityBindingElement) -> IDictionary[str, SupportingTokenParameters] """
        ...

    @property
    def OptionalEndpointSupportingTokenParameters(self) -> SupportingTokenParameters:
        """ Get: OptionalEndpointSupportingTokenParameters(self: SecurityBindingElement) -> SupportingTokenParameters """
        ...

    @property
    def OptionalOperationSupportingTokenParameters(self) -> IDictionary:
        """ Get: OptionalOperationSupportingTokenParameters(self: SecurityBindingElement) -> IDictionary[str, SupportingTokenParameters] """
        ...

    @property
    def ProtectTokens(self) -> bool:
        """
        Get: ProtectTokens(self: SecurityBindingElement) -> bool
        Set: ProtectTokens(self: SecurityBindingElement) = value
        """
        ...

    @property
    def SecurityHeaderLayout(self): # -> SecurityHeaderLayout
        """
        Get: SecurityHeaderLayout(self: SecurityBindingElement) -> SecurityHeaderLayout
        Set: SecurityHeaderLayout(self: SecurityBindingElement) = value
        """
        ...


    def BuildChannelFactoryCore(self, *args): #cannot find CLR method
        """ BuildChannelFactoryCore[TChannel](self: SecurityBindingElement, context: BindingContext) -> IChannelFactory[TChannel] """
        ...

    def BuildChannelListenerCore(self, *args): #cannot find CLR method
        """ BuildChannelListenerCore[TChannel](self: SecurityBindingElement, context: BindingContext) -> IChannelListener[TChannel] """
        ...

    @staticmethod
    def CreateAnonymousForCertificateBindingElement(): # -> SymmetricSecurityBindingElement
        """ CreateAnonymousForCertificateBindingElement() -> SymmetricSecurityBindingElement """
        ...

    @staticmethod
    def CreateCertificateOverTransportBindingElement(version=None): # -> TransportSecurityBindingElement
        """
        CreateCertificateOverTransportBindingElement() -> TransportSecurityBindingElement
        CreateCertificateOverTransportBindingElement(version: MessageSecurityVersion) -> TransportSecurityBindingElement
        """
        ...

    @staticmethod
    def CreateCertificateSignatureBindingElement(): # -> AsymmetricSecurityBindingElement
        """ CreateCertificateSignatureBindingElement() -> AsymmetricSecurityBindingElement """
        ...

    @staticmethod
    def CreateIssuedTokenBindingElement(issuedTokenParameters:IssuedSecurityTokenParameters): # -> SymmetricSecurityBindingElement
        """ CreateIssuedTokenBindingElement(issuedTokenParameters: IssuedSecurityTokenParameters) -> SymmetricSecurityBindingElement """
        ...

    @staticmethod
    def CreateIssuedTokenForCertificateBindingElement(issuedTokenParameters:IssuedSecurityTokenParameters): # -> SymmetricSecurityBindingElement
        """ CreateIssuedTokenForCertificateBindingElement(issuedTokenParameters: IssuedSecurityTokenParameters) -> SymmetricSecurityBindingElement """
        ...

    @staticmethod
    def CreateIssuedTokenForSslBindingElement(issuedTokenParameters:IssuedSecurityTokenParameters, requireCancellation:bool = ...): # -> SymmetricSecurityBindingElement
        """
        CreateIssuedTokenForSslBindingElement(issuedTokenParameters: IssuedSecurityTokenParameters) -> SymmetricSecurityBindingElement
        CreateIssuedTokenForSslBindingElement(issuedTokenParameters: IssuedSecurityTokenParameters, requireCancellation: bool) -> SymmetricSecurityBindingElement
        """
        ...

    @staticmethod
    def CreateIssuedTokenOverTransportBindingElement(issuedTokenParameters:IssuedSecurityTokenParameters): # -> TransportSecurityBindingElement
        """ CreateIssuedTokenOverTransportBindingElement(issuedTokenParameters: IssuedSecurityTokenParameters) -> TransportSecurityBindingElement """
        ...

    @staticmethod
    def CreateKerberosBindingElement(): # -> SymmetricSecurityBindingElement
        """ CreateKerberosBindingElement() -> SymmetricSecurityBindingElement """
        ...

    @staticmethod
    def CreateKerberosOverTransportBindingElement(): # -> TransportSecurityBindingElement
        """ CreateKerberosOverTransportBindingElement() -> TransportSecurityBindingElement """
        ...

    @staticmethod
    def CreateMutualCertificateBindingElement(version:MessageSecurityVersion = ..., allowSerializedSigningTokenOnReply:bool = ...) -> SecurityBindingElement:
        """
        CreateMutualCertificateBindingElement() -> SecurityBindingElement
        CreateMutualCertificateBindingElement(version: MessageSecurityVersion) -> SecurityBindingElement
        CreateMutualCertificateBindingElement(version: MessageSecurityVersion, allowSerializedSigningTokenOnReply: bool) -> SecurityBindingElement
        """
        ...

    @staticmethod
    def CreateMutualCertificateDuplexBindingElement(version=None): # -> AsymmetricSecurityBindingElement
        """
        CreateMutualCertificateDuplexBindingElement() -> AsymmetricSecurityBindingElement
        CreateMutualCertificateDuplexBindingElement(version: MessageSecurityVersion) -> AsymmetricSecurityBindingElement
        """
        ...

    @staticmethod
    def CreateSecureConversationBindingElement(bootstrapSecurity:SecurityBindingElement, requireCancellation:bool = ..., bootstrapProtectionRequirements:ChannelProtectionRequirements = ...) -> SecurityBindingElement:
        """
        CreateSecureConversationBindingElement(bootstrapSecurity: SecurityBindingElement) -> SecurityBindingElement
        CreateSecureConversationBindingElement(bootstrapSecurity: SecurityBindingElement, requireCancellation: bool) -> SecurityBindingElement
        CreateSecureConversationBindingElement(bootstrapSecurity: SecurityBindingElement, requireCancellation: bool, bootstrapProtectionRequirements: ChannelProtectionRequirements) -> SecurityBindingElement
        """
        ...

    @staticmethod
    def CreateSslNegotiationBindingElement(requireClientCertificate:bool, requireCancellation:bool = ...): # -> SymmetricSecurityBindingElement
        """
        CreateSslNegotiationBindingElement(requireClientCertificate: bool) -> SymmetricSecurityBindingElement
        CreateSslNegotiationBindingElement(requireClientCertificate: bool, requireCancellation: bool) -> SymmetricSecurityBindingElement
        """
        ...

    @staticmethod
    def CreateSspiNegotiationBindingElement(requireCancellation=None): # -> SymmetricSecurityBindingElement
        """
        CreateSspiNegotiationBindingElement() -> SymmetricSecurityBindingElement
        CreateSspiNegotiationBindingElement(requireCancellation: bool) -> SymmetricSecurityBindingElement
        """
        ...

    @staticmethod
    def CreateSspiNegotiationOverTransportBindingElement(requireCancellation=None): # -> TransportSecurityBindingElement
        """
        CreateSspiNegotiationOverTransportBindingElement() -> TransportSecurityBindingElement
        CreateSspiNegotiationOverTransportBindingElement(requireCancellation: bool) -> TransportSecurityBindingElement
        """
        ...

    @staticmethod
    def CreateUserNameForCertificateBindingElement(): # -> SymmetricSecurityBindingElement
        """ CreateUserNameForCertificateBindingElement() -> SymmetricSecurityBindingElement """
        ...

    @staticmethod
    def CreateUserNameForSslBindingElement(requireCancellation=None): # -> SymmetricSecurityBindingElement
        """
        CreateUserNameForSslBindingElement() -> SymmetricSecurityBindingElement
        CreateUserNameForSslBindingElement(requireCancellation: bool) -> SymmetricSecurityBindingElement
        """
        ...

    @staticmethod
    def CreateUserNameOverTransportBindingElement(): # -> TransportSecurityBindingElement
        """ CreateUserNameOverTransportBindingElement() -> TransportSecurityBindingElement """
        ...

    def SetIssuerBindingContextIfRequired(self, *args): #cannot find CLR method
        """ SetIssuerBindingContextIfRequired(parameters: SecurityTokenParameters, issuerBindingContext: BindingContext) """
        ...

    def SetKeyDerivation(self, requireDerivedKeys:bool): # -> 
        """ SetKeyDerivation(self: SecurityBindingElement, requireDerivedKeys: bool) """
        ...

    def ToString(self) -> str:
        """ ToString(self: SecurityBindingElement) -> str """
        ...


class AsymmetricSecurityBindingElement(SecurityBindingElement, IPolicyExportExtension): # skipped bases: <type 'object'>
    """
    AsymmetricSecurityBindingElement()
    AsymmetricSecurityBindingElement(recipientTokenParameters: SecurityTokenParameters)
    AsymmetricSecurityBindingElement(recipientTokenParameters: SecurityTokenParameters, initiatorTokenParameters: SecurityTokenParameters)
    """
    @property
    def AllowSerializedSigningTokenOnReply(self) -> bool:
        """
        Get: AllowSerializedSigningTokenOnReply(self: AsymmetricSecurityBindingElement) -> bool
        Set: AllowSerializedSigningTokenOnReply(self: AsymmetricSecurityBindingElement) = value
        """
        ...

    @property
    def InitiatorTokenParameters(self) -> SecurityTokenParameters:
        """
        Get: InitiatorTokenParameters(self: AsymmetricSecurityBindingElement) -> SecurityTokenParameters
        Set: InitiatorTokenParameters(self: AsymmetricSecurityBindingElement) = value
        """
        ...

    @property
    def MessageProtectionOrder(self) -> MessageProtectionOrder:
        """
        Get: MessageProtectionOrder(self: AsymmetricSecurityBindingElement) -> MessageProtectionOrder
        Set: MessageProtectionOrder(self: AsymmetricSecurityBindingElement) = value
        """
        ...

    @property
    def RecipientTokenParameters(self) -> SecurityTokenParameters:
        """
        Get: RecipientTokenParameters(self: AsymmetricSecurityBindingElement) -> SecurityTokenParameters
        Set: RecipientTokenParameters(self: AsymmetricSecurityBindingElement) = value
        """
        ...

    @property
    def RequireSignatureConfirmation(self) -> bool:
        """
        Get: RequireSignatureConfirmation(self: AsymmetricSecurityBindingElement) -> bool
        Set: RequireSignatureConfirmation(self: AsymmetricSecurityBindingElement) = value
        """
        ...


    def Clone(self) -> BindingElement:
        """ Clone(self: AsymmetricSecurityBindingElement) -> BindingElement """
        ...

    def __new__(cls, recipientTokenParameters:SecurityTokenParameters = ..., initiatorTokenParameters:SecurityTokenParameters = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, recipientTokenParameters: SecurityTokenParameters)
        __new__(cls: type, recipientTokenParameters: SecurityTokenParameters, initiatorTokenParameters: SecurityTokenParameters)
        """
        ...


class MessageEncodingBindingElement(BindingElement): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def MessageVersion(self): # -> MessageVersion
        """
        Get: MessageVersion(self: MessageEncodingBindingElement) -> MessageVersion
        Set: MessageVersion(self: MessageEncodingBindingElement) = value
        """
        ...


    def CreateMessageEncoderFactory(self): # -> MessageEncoderFactory
        """ CreateMessageEncoderFactory(self: MessageEncodingBindingElement) -> MessageEncoderFactory """
        ...


class BinaryMessageEncodingBindingElement(IPolicyExportExtension, MessageEncodingBindingElement, IWsdlExportExtension): # skipped bases: <type 'object'>
    """ BinaryMessageEncodingBindingElement() """
    @property
    def CompressionFormat(self): # -> CompressionFormat
        """
        Get: CompressionFormat(self: BinaryMessageEncodingBindingElement) -> CompressionFormat
        Set: CompressionFormat(self: BinaryMessageEncodingBindingElement) = value
        """
        ...

    @property
    def MaxReadPoolSize(self) -> int:
        """
        Get: MaxReadPoolSize(self: BinaryMessageEncodingBindingElement) -> int
        Set: MaxReadPoolSize(self: BinaryMessageEncodingBindingElement) = value
        """
        ...

    @property
    def MaxSessionSize(self) -> int:
        """
        Get: MaxSessionSize(self: BinaryMessageEncodingBindingElement) -> int
        Set: MaxSessionSize(self: BinaryMessageEncodingBindingElement) = value
        """
        ...

    @property
    def MaxWritePoolSize(self) -> int:
        """
        Get: MaxWritePoolSize(self: BinaryMessageEncodingBindingElement) -> int
        Set: MaxWritePoolSize(self: BinaryMessageEncodingBindingElement) = value
        """
        ...

    @property
    def ReaderQuotas(self) -> XmlDictionaryReaderQuotas:
        """
        Get: ReaderQuotas(self: BinaryMessageEncodingBindingElement) -> XmlDictionaryReaderQuotas
        Set: ReaderQuotas(self: BinaryMessageEncodingBindingElement) = value
        """
        ...


    def BuildChannelFactory(self, context): # -> IChannelFactory # Not found arg types: {'context': 'BindingContext'}
        """ BuildChannelFactory[TChannel](self: BinaryMessageEncodingBindingElement, context: BindingContext) -> IChannelFactory[TChannel] """
        ...

    def BuildChannelListener(self, context): # -> IChannelListener # Not found arg types: {'context': 'BindingContext'}
        """ BuildChannelListener[TChannel](self: BinaryMessageEncodingBindingElement, context: BindingContext) -> IChannelListener[TChannel] """
        ...

    def CanBuildChannelListener(self, context) -> bool: # Not found arg types: {'context': 'BindingContext'}
        """ CanBuildChannelListener[TChannel](self: BinaryMessageEncodingBindingElement, context: BindingContext) -> bool """
        ...

    def Clone(self) -> BindingElement:
        """ Clone(self: BinaryMessageEncodingBindingElement) -> BindingElement """
        ...

    def ShouldSerializeMessageVersion(self) -> bool:
        """ ShouldSerializeMessageVersion(self: BinaryMessageEncodingBindingElement) -> bool """
        ...

    def ShouldSerializeReaderQuotas(self) -> bool:
        """ ShouldSerializeReaderQuotas(self: BinaryMessageEncodingBindingElement) -> bool """
        ...


class Binding(IDefaultCommunicationTimeouts): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def MessageVersion(self): # -> MessageVersion
        """ Get: MessageVersion(self: Binding) -> MessageVersion """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Binding) -> str
        Set: Name(self: Binding) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: Binding) -> str
        Set: Namespace(self: Binding) = value
        """
        ...

    @property
    def Scheme(self) -> str:
        """ Get: Scheme(self: Binding) -> str """
        ...


    def BuildChannelFactory(self, parameters:Array): # -> IChannelFactory
        """
        BuildChannelFactory[TChannel](self: Binding, *parameters: Array[object]) -> IChannelFactory[TChannel]
        BuildChannelFactory[TChannel](self: Binding, parameters: BindingParameterCollection) -> IChannelFactory[TChannel]
        """
        ...

    def BuildChannelListener(self, *__args:Array): # -> IChannelListener
        """
        BuildChannelListener[TChannel](self: Binding, *parameters: Array[object]) -> IChannelListener[TChannel]
        BuildChannelListener[TChannel](self: Binding, listenUriBaseAddress: Uri, *parameters: Array[object]) -> IChannelListener[TChannel]
        BuildChannelListener[TChannel](self: Binding, listenUriBaseAddress: Uri, listenUriRelativeAddress: str, *parameters: Array[object]) -> IChannelListener[TChannel]
        BuildChannelListener[TChannel](self: Binding, listenUriBaseAddress: Uri, listenUriRelativeAddress: str, listenUriMode: ListenUriMode, *parameters: Array[object]) -> IChannelListener[TChannel]
        BuildChannelListener[TChannel](self: Binding, parameters: BindingParameterCollection) -> IChannelListener[TChannel]
        BuildChannelListener[TChannel](self: Binding, listenUriBaseAddress: Uri, parameters: BindingParameterCollection) -> IChannelListener[TChannel]
        BuildChannelListener[TChannel](self: Binding, listenUriBaseAddress: Uri, listenUriRelativeAddress: str, parameters: BindingParameterCollection) -> IChannelListener[TChannel]
        BuildChannelListener[TChannel](self: Binding, listenUriBaseAddress: Uri, listenUriRelativeAddress: str, listenUriMode: ListenUriMode, parameters: BindingParameterCollection) -> IChannelListener[TChannel]
        """
        ...

    def CanBuildChannelFactory(self, parameters:Array) -> bool:
        """
        CanBuildChannelFactory[TChannel](self: Binding, *parameters: Array[object]) -> bool
        CanBuildChannelFactory[TChannel](self: Binding, parameters: BindingParameterCollection) -> bool
        """
        ...

    def CanBuildChannelListener(self, parameters:Array) -> bool:
        """
        CanBuildChannelListener[TChannel](self: Binding, *parameters: Array[object]) -> bool
        CanBuildChannelListener[TChannel](self: Binding, parameters: BindingParameterCollection) -> bool
        """
        ...

    def CreateBindingElements(self): # -> BindingElementCollection
        """ CreateBindingElements(self: Binding) -> BindingElementCollection """
        ...

    def GetProperty(self, parameters): # -> T # Not found arg types: {'parameters': 'BindingParameterCollection'}
        """ GetProperty[T](self: Binding, parameters: BindingParameterCollection) -> T """
        ...

    def ShouldSerializeName(self) -> bool:
        """ ShouldSerializeName(self: Binding) -> bool """
        ...

    def ShouldSerializeNamespace(self) -> bool:
        """ ShouldSerializeNamespace(self: Binding) -> bool """
        ...


class BindingContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    BindingContext(binding: CustomBinding, parameters: BindingParameterCollection)
    BindingContext(binding: CustomBinding, parameters: BindingParameterCollection, listenUriBaseAddress: Uri, listenUriRelativeAddress: str, listenUriMode: ListenUriMode)
    """
    @property
    def Binding(self): # -> CustomBinding
        """ Get: Binding(self: BindingContext) -> CustomBinding """
        ...

    @property
    def BindingParameters(self): # -> BindingParameterCollection
        """ Get: BindingParameters(self: BindingContext) -> BindingParameterCollection """
        ...

    @property
    def ListenUriBaseAddress(self) -> Uri:
        """
        Get: ListenUriBaseAddress(self: BindingContext) -> Uri
        Set: ListenUriBaseAddress(self: BindingContext) = value
        """
        ...

    @property
    def ListenUriMode(self) -> ListenUriMode:
        """
        Get: ListenUriMode(self: BindingContext) -> ListenUriMode
        Set: ListenUriMode(self: BindingContext) = value
        """
        ...

    @property
    def ListenUriRelativeAddress(self) -> str:
        """
        Get: ListenUriRelativeAddress(self: BindingContext) -> str
        Set: ListenUriRelativeAddress(self: BindingContext) = value
        """
        ...

    @property
    def RemainingBindingElements(self): # -> BindingElementCollection
        """ Get: RemainingBindingElements(self: BindingContext) -> BindingElementCollection """
        ...


    def BuildInnerChannelFactory(self): # -> IChannelFactory
        """ BuildInnerChannelFactory[TChannel](self: BindingContext) -> IChannelFactory[TChannel] """
        ...

    def BuildInnerChannelListener(self): # -> IChannelListener
        """ BuildInnerChannelListener[TChannel](self: BindingContext) -> IChannelListener[TChannel] """
        ...

    def CanBuildInnerChannelFactory(self) -> bool:
        """ CanBuildInnerChannelFactory[TChannel](self: BindingContext) -> bool """
        ...

    def CanBuildInnerChannelListener(self) -> bool:
        """ CanBuildInnerChannelListener[TChannel](self: BindingContext) -> bool """
        ...

    def Clone(self) -> BindingContext:
        """ Clone(self: BindingContext) -> BindingContext """
        ...

    def GetInnerProperty(self): # -> T
        """ GetInnerProperty[T](self: BindingContext) -> T """
        ...


class BindingElementCollection(Collection): # skipped bases: <type 'ICollection[BindingElement]'>, <type 'IEnumerable'>, <type 'IList[BindingElement]'>, <type 'IList'>, <type 'IReadOnlyList[BindingElement]'>, <type 'IReadOnlyCollection[BindingElement]'>, <type 'ICollection'>, <type 'IEnumerable[BindingElement]'>, <type 'object'>
    """
    BindingElementCollection()
    BindingElementCollection(elements: IEnumerable[BindingElement])
    BindingElementCollection(elements: Array[BindingElement])
    """
    def AddRange(self, elements:Array): # -> 
        """ AddRange(self: BindingElementCollection, *elements: Array[BindingElement]) """
        ...

    def Clone(self) -> BindingElementCollection:
        """ Clone(self: BindingElementCollection) -> BindingElementCollection """
        ...

    def Find(self): # -> T
        """ Find[T](self: BindingElementCollection) -> T """
        ...

    def FindAll(self) -> Collection:
        """ FindAll[T](self: BindingElementCollection) -> Collection[T] """
        ...

    def RemoveAll(self) -> Collection:
        """ RemoveAll[T](self: BindingElementCollection) -> Collection[T] """
        ...


class BindingParameterCollection(KeyedByTypeCollection): # skipped bases: <type 'IReadOnlyCollection[object]'>, <type 'IReadOnlyList[object]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IList[object]'>, <type 'IEnumerable[object]'>, <type 'ICollection'>, <type 'ICollection[object]'>, <type 'object'>
    """ BindingParameterCollection() """
    pass

class BodyWriter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsBuffered(self) -> bool:
        """ Get: IsBuffered(self: BodyWriter) -> bool """
        ...


    def BeginWriteBodyContents(self, writer:XmlDictionaryWriter, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginWriteBodyContents(self: BodyWriter, writer: XmlDictionaryWriter, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def CreateBufferedCopy(self, maxBufferSize:int) -> BodyWriter:
        """ CreateBufferedCopy(self: BodyWriter, maxBufferSize: int) -> BodyWriter """
        ...

    def EndWriteBodyContents(self, result:IAsyncResult): # -> 
        """ EndWriteBodyContents(self: BodyWriter, result: IAsyncResult) """
        ...

    def OnBeginWriteBodyContents(self, *args): #cannot find CLR method
        """ OnBeginWriteBodyContents(self: BodyWriter, writer: XmlDictionaryWriter, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def OnCreateBufferedCopy(self, *args): #cannot find CLR method
        """ OnCreateBufferedCopy(self: BodyWriter, maxBufferSize: int) -> BodyWriter """
        ...

    def OnEndWriteBodyContents(self, *args): #cannot find CLR method
        """ OnEndWriteBodyContents(self: BodyWriter, result: IAsyncResult) """
        ...

    def OnWriteBodyContents(self, *args): #cannot find CLR method
        """ OnWriteBodyContents(self: BodyWriter, writer: XmlDictionaryWriter) """
        ...

    def WriteBodyContents(self, writer:XmlDictionaryWriter): # -> 
        """ WriteBodyContents(self: BodyWriter, writer: XmlDictionaryWriter) """
        ...


class BufferManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Clear(self): # -> 
        """ Clear(self: BufferManager) """
        ...

    @staticmethod
    def CreateBufferManager(maxBufferPoolSize:Int64, maxBufferSize:int) -> BufferManager:
        """ CreateBufferManager(maxBufferPoolSize: Int64, maxBufferSize: int) -> BufferManager """
        ...

    def ReturnBuffer(self, buffer:Array): # -> 
        """ ReturnBuffer(self: BufferManager, buffer: Array[Byte]) """
        ...

    def TakeBuffer(self, bufferSize:int) -> Array:
        """ TakeBuffer(self: BufferManager, bufferSize: int) -> Array[Byte] """
        ...


class ByteStreamMessage: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateMessage(*__args:Stream) -> Message:
        """
        CreateMessage(stream: Stream) -> Message
        CreateMessage(buffer: ArraySegment[Byte]) -> Message
        CreateMessage(buffer: ArraySegment[Byte], bufferManager: BufferManager) -> Message
        """
        ...

    __all__: list = ...


class ByteStreamMessageEncodingBindingElement(MessageEncodingBindingElement): # skipped bases: <type 'object'>
    """
    ByteStreamMessageEncodingBindingElement()
    ByteStreamMessageEncodingBindingElement(quota: XmlDictionaryReaderQuotas)
    """
    @property
    def ReaderQuotas(self) -> XmlDictionaryReaderQuotas:
        """
        Get: ReaderQuotas(self: ByteStreamMessageEncodingBindingElement) -> XmlDictionaryReaderQuotas
        Set: ReaderQuotas(self: ByteStreamMessageEncodingBindingElement) = value
        """
        ...


    def BuildChannelFactory(self, context:BindingContext): # -> IChannelFactory
        """ BuildChannelFactory[TChannel](self: ByteStreamMessageEncodingBindingElement, context: BindingContext) -> IChannelFactory[TChannel] """
        ...

    def BuildChannelListener(self, context:BindingContext): # -> IChannelListener
        """ BuildChannelListener[TChannel](self: ByteStreamMessageEncodingBindingElement, context: BindingContext) -> IChannelListener[TChannel] """
        ...

    def CanBuildChannelFactory(self, context:BindingContext) -> bool:
        """ CanBuildChannelFactory[TChannel](self: ByteStreamMessageEncodingBindingElement, context: BindingContext) -> bool """
        ...

    def CanBuildChannelListener(self, context:BindingContext) -> bool:
        """ CanBuildChannelListener[TChannel](self: ByteStreamMessageEncodingBindingElement, context: BindingContext) -> bool """
        ...

    def Clone(self) -> BindingElement:
        """ Clone(self: ByteStreamMessageEncodingBindingElement) -> BindingElement """
        ...

    def ShouldSerializeMessageVersion(self) -> bool:
        """ ShouldSerializeMessageVersion(self: ByteStreamMessageEncodingBindingElement) -> bool """
        ...

    def ShouldSerializeReaderQuotas(self) -> bool:
        """ ShouldSerializeReaderQuotas(self: ByteStreamMessageEncodingBindingElement) -> bool """
        ...


class CallbackContextMessageProperty(IMessageProperty): # skipped bases: <type 'object'>
    """
    CallbackContextMessageProperty(context: IDictionary[str, str])
    CallbackContextMessageProperty(listenAddress: str, context: IDictionary[str, str])
    CallbackContextMessageProperty(listenAddress: Uri, context: IDictionary[str, str])
    CallbackContextMessageProperty(listenAddress: EndpointAddress, context: IDictionary[str, str])
    CallbackContextMessageProperty(callbackAddress: EndpointAddress)
    """
    @property
    def CallbackAddress(self) -> EndpointAddress:
        """ Get: CallbackAddress(self: CallbackContextMessageProperty) -> EndpointAddress """
        ...

    @property
    def Context(self) -> IDictionary:
        """ Get: Context(self: CallbackContextMessageProperty) -> IDictionary[str, str] """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name() -> str """
        ...


    def AddOrReplaceInMessage(self, message:Message): # -> 
        """ AddOrReplaceInMessage(self: CallbackContextMessageProperty, message: Message) """
        ...

    def AddOrReplaceInMessageProperties(self, properties): # ->  # Not found arg types: {'properties': 'MessageProperties'}
        """ AddOrReplaceInMessageProperties(self: CallbackContextMessageProperty, properties: MessageProperties) """
        ...

    def CreateCallbackAddress(self, listenAddress:Uri) -> EndpointAddress:
        """ CreateCallbackAddress(self: CallbackContextMessageProperty, listenAddress: Uri) -> EndpointAddress """
        ...

    def GetListenAddressAndContext(self, listenAddress, context) -> Tuple_[EndpointAddress, IDictionary]:
        """ GetListenAddressAndContext(self: CallbackContextMessageProperty) -> (EndpointAddress, IDictionary[str, str]) """
        ...

    @staticmethod
    def TryGet(*__args:Message) -> Tuple_[bool, CallbackContextMessageProperty]:
        """
        TryGet(message: Message) -> (bool, CallbackContextMessageProperty)
        TryGet(properties: MessageProperties) -> (bool, CallbackContextMessageProperty)
        """
        ...



class CommunicationObject(ICommunicationObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DefaultCloseTimeout(self):
        ...

    @property
    def DefaultOpenTimeout(self):
        ...

    @property
    def IsDisposed(self):
        ...

    @property
    def ThisLock(self):
        ...


    def Fault(self, *args): #cannot find CLR method
        """ Fault(self: CommunicationObject) """
        ...

    def GetCommunicationObjectType(self, *args): #cannot find CLR method
        """ GetCommunicationObjectType(self: CommunicationObject) -> Type """
        ...

    def OnAbort(self, *args): #cannot find CLR method
        """ OnAbort(self: CommunicationObject) """
        ...

    def OnBeginClose(self, *args): #cannot find CLR method
        """ OnBeginClose(self: CommunicationObject, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def OnBeginOpen(self, *args): #cannot find CLR method
        """ OnBeginOpen(self: CommunicationObject, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def OnClose(self, *args): #cannot find CLR method
        """ OnClose(self: CommunicationObject, timeout: TimeSpan) """
        ...

    def OnClosed(self, *args): #cannot find CLR method
        """ OnClosed(self: CommunicationObject) """
        ...

    def OnClosing(self, *args): #cannot find CLR method
        """ OnClosing(self: CommunicationObject) """
        ...

    def OnEndClose(self, *args): #cannot find CLR method
        """ OnEndClose(self: CommunicationObject, result: IAsyncResult) """
        ...

    def OnEndOpen(self, *args): #cannot find CLR method
        """ OnEndOpen(self: CommunicationObject, result: IAsyncResult) """
        ...

    def OnFaulted(self, *args): #cannot find CLR method
        """ OnFaulted(self: CommunicationObject) """
        ...

    def OnOpen(self, *args): #cannot find CLR method
        """ OnOpen(self: CommunicationObject, timeout: TimeSpan) """
        ...

    def OnOpened(self, *args): #cannot find CLR method
        """ OnOpened(self: CommunicationObject) """
        ...

    def OnOpening(self, *args): #cannot find CLR method
        """ OnOpening(self: CommunicationObject) """
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

    Closed = ...
    Closing = ...
    Faulted = ...
    Opened = ...
    Opening = ...


class IChannel(ICommunicationObject): # skipped bases: <type 'object'>
    """ no doc """
    def GetProperty(self): # -> T
        """ GetProperty[T](self: IChannel) -> T """
        ...


class ChannelBase(IChannel, IDefaultCommunicationTimeouts, CommunicationObject): # skipped bases: <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    @property
    def DefaultReceiveTimeout(self):
        ...

    @property
    def DefaultSendTimeout(self):
        ...

    @property
    def Manager(self):
        ...



class ChannelFactoryBase: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DefaultCloseTimeout(self):
        ...

    @property
    def DefaultOpenTimeout(self):
        ...

    @property
    def DefaultReceiveTimeout(self):
        ...

    @property
    def DefaultSendTimeout(self):
        ...

    @property
    def IsDisposed(self):
        ...

    @property
    def ThisLock(self):
        ...


    def Fault(self, *args): #cannot find CLR method
        """ Fault(self: CommunicationObject) """
        ...

    def GetCommunicationObjectType(self, *args): #cannot find CLR method
        """ GetCommunicationObjectType(self: CommunicationObject) -> Type """
        ...

    def GetProperty(self): # -> T
        """ GetProperty[T](self: ChannelFactoryBase) -> T """
        ...

    def OnAbort(self, *args): #cannot find CLR method
        """ OnAbort(self: ChannelFactoryBase) """
        ...

    def OnBeginClose(self, *args): #cannot find CLR method
        """ OnBeginClose(self: ChannelFactoryBase, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def OnBeginOpen(self, *args): #cannot find CLR method
        """ OnBeginOpen(self: CommunicationObject, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def OnClose(self, *args): #cannot find CLR method
        """ OnClose(self: ChannelFactoryBase, timeout: TimeSpan) """
        ...

    def OnClosed(self, *args): #cannot find CLR method
        """ OnClosed(self: CommunicationObject) """
        ...

    def OnClosing(self, *args): #cannot find CLR method
        """ OnClosing(self: CommunicationObject) """
        ...

    def OnEndClose(self, *args): #cannot find CLR method
        """ OnEndClose(self: ChannelFactoryBase, result: IAsyncResult) """
        ...

    def OnEndOpen(self, *args): #cannot find CLR method
        """ OnEndOpen(self: CommunicationObject, result: IAsyncResult) """
        ...

    def OnFaulted(self, *args): #cannot find CLR method
        """ OnFaulted(self: CommunicationObject) """
        ...

    def OnOpen(self, *args): #cannot find CLR method
        """ OnOpen(self: CommunicationObject, timeout: TimeSpan) """
        ...

    def OnOpened(self, *args): #cannot find CLR method
        """ OnOpened(self: CommunicationObject) """
        ...

    def OnOpening(self, *args): #cannot find CLR method
        """ OnOpening(self: CommunicationObject) """
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

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, timeouts: IDefaultCommunicationTimeouts)
        """
        ...


class ChannelListenerBase: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DefaultCloseTimeout(self):
        ...

    @property
    def DefaultOpenTimeout(self):
        ...

    @property
    def DefaultReceiveTimeout(self):
        ...

    @property
    def DefaultSendTimeout(self):
        ...

    @property
    def IsDisposed(self):
        ...

    @property
    def ThisLock(self):
        ...

    @property
    def Uri(self) -> Uri:
        """ Get: Uri(self: ChannelListenerBase) -> Uri """
        ...


    def BeginWaitForChannel(self, timeout:TimeSpan, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginWaitForChannel(self: ChannelListenerBase, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndWaitForChannel(self, result:IAsyncResult) -> bool:
        """ EndWaitForChannel(self: ChannelListenerBase, result: IAsyncResult) -> bool """
        ...

    def Fault(self, *args): #cannot find CLR method
        """ Fault(self: CommunicationObject) """
        ...

    def GetCommunicationObjectType(self, *args): #cannot find CLR method
        """ GetCommunicationObjectType(self: CommunicationObject) -> Type """
        ...

    def GetProperty(self): # -> T
        """ GetProperty[T](self: ChannelListenerBase) -> T """
        ...

    def OnAbort(self, *args): #cannot find CLR method
        """ OnAbort(self: CommunicationObject) """
        ...

    def OnBeginClose(self, *args): #cannot find CLR method
        """ OnBeginClose(self: CommunicationObject, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def OnBeginOpen(self, *args): #cannot find CLR method
        """ OnBeginOpen(self: CommunicationObject, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def OnBeginWaitForChannel(self, *args): #cannot find CLR method
        """ OnBeginWaitForChannel(self: ChannelListenerBase, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def OnClose(self, *args): #cannot find CLR method
        """ OnClose(self: CommunicationObject, timeout: TimeSpan) """
        ...

    def OnClosed(self, *args): #cannot find CLR method
        """ OnClosed(self: CommunicationObject) """
        ...

    def OnClosing(self, *args): #cannot find CLR method
        """ OnClosing(self: CommunicationObject) """
        ...

    def OnEndClose(self, *args): #cannot find CLR method
        """ OnEndClose(self: CommunicationObject, result: IAsyncResult) """
        ...

    def OnEndOpen(self, *args): #cannot find CLR method
        """ OnEndOpen(self: CommunicationObject, result: IAsyncResult) """
        ...

    def OnEndWaitForChannel(self, *args): #cannot find CLR method
        """ OnEndWaitForChannel(self: ChannelListenerBase, result: IAsyncResult) -> bool """
        ...

    def OnFaulted(self, *args): #cannot find CLR method
        """ OnFaulted(self: CommunicationObject) """
        ...

    def OnOpen(self, *args): #cannot find CLR method
        """ OnOpen(self: CommunicationObject, timeout: TimeSpan) """
        ...

    def OnOpened(self, *args): #cannot find CLR method
        """ OnOpened(self: CommunicationObject) """
        ...

    def OnOpening(self, *args): #cannot find CLR method
        """ OnOpening(self: CommunicationObject) """
        ...

    def OnWaitForChannel(self, *args): #cannot find CLR method
        """ OnWaitForChannel(self: ChannelListenerBase, timeout: TimeSpan) -> bool """
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

    def WaitForChannel(self, timeout:TimeSpan) -> bool:
        """ WaitForChannel(self: ChannelListenerBase, timeout: TimeSpan) -> bool """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, timeouts: IDefaultCommunicationTimeouts)
        """
        ...


class ChannelManagerBase(IDefaultCommunicationTimeouts, CommunicationObject): # skipped bases: <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    @property
    def DefaultReceiveTimeout(self):
        ...

    @property
    def DefaultSendTimeout(self):
        ...



class ChannelParameterCollection(Collection): # skipped bases: <type 'ICollection'>, <type 'IReadOnlyList[object]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IList[object]'>, <type 'IEnumerable[object]'>, <type 'IReadOnlyCollection[object]'>, <type 'ICollection[object]'>, <type 'object'>
    """
    ChannelParameterCollection()
    ChannelParameterCollection(channel: IChannel)
    """
    @property
    def Channel(self):
        ...


    def PropagateChannelParameters(self, innerChannel:IChannel): # -> 
        """ PropagateChannelParameters(self: ChannelParameterCollection, innerChannel: IChannel) """
        ...


class ChannelPoolSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ ChannelPoolSettings() """
    @property
    def IdleTimeout(self) -> TimeSpan:
        """
        Get: IdleTimeout(self: ChannelPoolSettings) -> TimeSpan
        Set: IdleTimeout(self: ChannelPoolSettings) = value
        """
        ...

    @property
    def LeaseTimeout(self) -> TimeSpan:
        """
        Get: LeaseTimeout(self: ChannelPoolSettings) -> TimeSpan
        Set: LeaseTimeout(self: ChannelPoolSettings) = value
        """
        ...

    @property
    def MaxOutboundChannelsPerEndpoint(self) -> int:
        """
        Get: MaxOutboundChannelsPerEndpoint(self: ChannelPoolSettings) -> int
        Set: MaxOutboundChannelsPerEndpoint(self: ChannelPoolSettings) = value
        """
        ...



class ClientWebSocketFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def WebSocketVersion(self) -> str:
        """ Get: WebSocketVersion(self: ClientWebSocketFactory) -> str """
        ...


    def CreateWebSocket(self, connection:Stream, settings) -> WebSocket: # Not found arg types: {'settings': 'WebSocketTransportSettings'}
        """ CreateWebSocket(self: ClientWebSocketFactory, connection: Stream, settings: WebSocketTransportSettings) -> WebSocket """
        ...


class CompositeDuplexBindingElement(IPolicyExportExtension, BindingElement): # skipped bases: <type 'object'>
    """ CompositeDuplexBindingElement() """
    @property
    def ClientBaseAddress(self) -> Uri:
        """
        Get: ClientBaseAddress(self: CompositeDuplexBindingElement) -> Uri
        Set: ClientBaseAddress(self: CompositeDuplexBindingElement) = value
        """
        ...



class CompositeDuplexBindingElementImporter(IPolicyImportExtension): # skipped bases: <type 'object'>
    """ CompositeDuplexBindingElementImporter() """
    pass

class CompressionFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CompressionFormat, values: Deflate (2), GZip (1), None (0) """
    Deflate: CompressionFormat = ...
    GZip: CompressionFormat = ...
    value__ = ...


class TransportBindingElement(BindingElement): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ManualAddressing(self) -> bool:
        """
        Get: ManualAddressing(self: TransportBindingElement) -> bool
        Set: ManualAddressing(self: TransportBindingElement) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: TransportBindingElement) -> Int64
        Set: MaxBufferPoolSize(self: TransportBindingElement) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: TransportBindingElement) -> Int64
        Set: MaxReceivedMessageSize(self: TransportBindingElement) = value
        """
        ...

    @property
    def Scheme(self) -> str:
        """ Get: Scheme(self: TransportBindingElement) -> str """
        ...



class ConnectionOrientedTransportBindingElement(TransportBindingElement, IPolicyExportExtension, ITransportPolicyImport, IWsdlExportExtension): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ChannelInitializationTimeout(self) -> TimeSpan:
        """
        Get: ChannelInitializationTimeout(self: ConnectionOrientedTransportBindingElement) -> TimeSpan
        Set: ChannelInitializationTimeout(self: ConnectionOrientedTransportBindingElement) = value
        """
        ...

    @property
    def ConnectionBufferSize(self) -> int:
        """
        Get: ConnectionBufferSize(self: ConnectionOrientedTransportBindingElement) -> int
        Set: ConnectionBufferSize(self: ConnectionOrientedTransportBindingElement) = value
        """
        ...

    @property
    def HostNameComparisonMode(self) -> HostNameComparisonMode:
        """
        Get: HostNameComparisonMode(self: ConnectionOrientedTransportBindingElement) -> HostNameComparisonMode
        Set: HostNameComparisonMode(self: ConnectionOrientedTransportBindingElement) = value
        """
        ...

    @property
    def MaxBufferSize(self) -> int:
        """
        Get: MaxBufferSize(self: ConnectionOrientedTransportBindingElement) -> int
        Set: MaxBufferSize(self: ConnectionOrientedTransportBindingElement) = value
        """
        ...

    @property
    def MaxOutputDelay(self) -> TimeSpan:
        """
        Get: MaxOutputDelay(self: ConnectionOrientedTransportBindingElement) -> TimeSpan
        Set: MaxOutputDelay(self: ConnectionOrientedTransportBindingElement) = value
        """
        ...

    @property
    def MaxPendingAccepts(self) -> int:
        """
        Get: MaxPendingAccepts(self: ConnectionOrientedTransportBindingElement) -> int
        Set: MaxPendingAccepts(self: ConnectionOrientedTransportBindingElement) = value
        """
        ...

    @property
    def MaxPendingConnections(self) -> int:
        """
        Get: MaxPendingConnections(self: ConnectionOrientedTransportBindingElement) -> int
        Set: MaxPendingConnections(self: ConnectionOrientedTransportBindingElement) = value
        """
        ...

    @property
    def TransferMode(self) -> TransferMode:
        """
        Get: TransferMode(self: ConnectionOrientedTransportBindingElement) -> TransferMode
        Set: TransferMode(self: ConnectionOrientedTransportBindingElement) = value
        """
        ...


    def CanBuildChannelFactory(self, context:BindingContext) -> bool:
        """ CanBuildChannelFactory[TChannel](self: ConnectionOrientedTransportBindingElement, context: BindingContext) -> bool """
        ...

    def CanBuildChannelListener(self, context:BindingContext) -> bool:
        """ CanBuildChannelListener[TChannel](self: ConnectionOrientedTransportBindingElement, context: BindingContext) -> bool """
        ...

    def ShouldSerializeMaxPendingAccepts(self) -> bool:
        """ ShouldSerializeMaxPendingAccepts(self: ConnectionOrientedTransportBindingElement) -> bool """
        ...

    def ShouldSerializeMaxPendingConnections(self) -> bool:
        """ ShouldSerializeMaxPendingConnections(self: ConnectionOrientedTransportBindingElement) -> bool """
        ...


class IContextBindingElement: # skipped bases: <type 'object'>
    """ no doc """
    pass

class ContextBindingElement(IContextSessionProvider, IPolicyExportExtension, BindingElement, IWmiInstanceProvider, IContextBindingElement): # skipped bases: <type 'object'>
    """
    ContextBindingElement()
    ContextBindingElement(protectionLevel: ProtectionLevel)
    ContextBindingElement(protectionLevel: ProtectionLevel, contextExchangeMechanism: ContextExchangeMechanism)
    ContextBindingElement(protectionLevel: ProtectionLevel, contextExchangeMechanism: ContextExchangeMechanism, clientCallbackAddress: Uri)
    ContextBindingElement(protectionLevel: ProtectionLevel, contextExchangeMechanism: ContextExchangeMechanism, clientCallbackAddress: Uri, contextManagementEnabled: bool)
    """
    @property
    def ClientCallbackAddress(self) -> Uri:
        """
        Get: ClientCallbackAddress(self: ContextBindingElement) -> Uri
        Set: ClientCallbackAddress(self: ContextBindingElement) = value
        """
        ...

    @property
    def ContextExchangeMechanism(self): # -> ContextExchangeMechanism
        """
        Get: ContextExchangeMechanism(self: ContextBindingElement) -> ContextExchangeMechanism
        Set: ContextExchangeMechanism(self: ContextBindingElement) = value
        """
        ...

    @property
    def ContextManagementEnabled(self) -> bool:
        """
        Get: ContextManagementEnabled(self: ContextBindingElement) -> bool
        Set: ContextManagementEnabled(self: ContextBindingElement) = value
        """
        ...

    @property
    def ProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ProtectionLevel(self: ContextBindingElement) -> ProtectionLevel
        Set: ProtectionLevel(self: ContextBindingElement) = value
        """
        ...



class ContextBindingElementImporter(IPolicyImportExtension, IWsdlImportExtension): # skipped bases: <type 'object'>
    """ ContextBindingElementImporter() """
    pass

class ContextExchangeMechanism(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ContextExchangeMechanism, values: ContextSoapHeader (0), HttpCookie (1) """
    ContextSoapHeader: ContextExchangeMechanism = ...
    HttpCookie: ContextExchangeMechanism = ...
    value__ = ...


class ContextMessageProperty(IMessageProperty): # skipped bases: <type 'object'>
    """
    ContextMessageProperty()
    ContextMessageProperty(context: IDictionary[str, str])
    """
    @property
    def Context(self) -> IDictionary:
        """ Get: Context(self: ContextMessageProperty) -> IDictionary[str, str] """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name() -> str """
        ...


    def AddOrReplaceInMessage(self, message:Message): # -> 
        """ AddOrReplaceInMessage(self: ContextMessageProperty, message: Message) """
        ...

    def AddOrReplaceInMessageProperties(self, properties): # ->  # Not found arg types: {'properties': 'MessageProperties'}
        """ AddOrReplaceInMessageProperties(self: ContextMessageProperty, properties: MessageProperties) """
        ...

    @staticmethod
    def TryCreateFromHttpCookieHeader(httpCookieHeader, context) -> Tuple_[bool, ContextMessageProperty]:
        """ TryCreateFromHttpCookieHeader(httpCookieHeader: str) -> (bool, ContextMessageProperty) """
        ...

    @staticmethod
    def TryGet(*__args:Message) -> Tuple_[bool, ContextMessageProperty]:
        """
        TryGet(message: Message) -> (bool, ContextMessageProperty)
        TryGet(properties: MessageProperties) -> (bool, ContextMessageProperty)
        """
        ...



class CorrelationCallbackMessageProperty(IMessageProperty): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsFullyDefined(self) -> bool:
        """ Get: IsFullyDefined(self: CorrelationCallbackMessageProperty) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name() -> str """
        ...

    @property
    def NeededData(self) -> IEnumerable:
        """ Get: NeededData(self: CorrelationCallbackMessageProperty) -> IEnumerable[str] """
        ...


    def AddData(self, name:str, value): # ->  # Not found arg types: {'value': 'Func'}
        """ AddData(self: CorrelationCallbackMessageProperty, name: str, value: Func[str]) """
        ...

    def BeginFinalizeCorrelation(self, message:Message, timeout:TimeSpan, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginFinalizeCorrelation(self: CorrelationCallbackMessageProperty, message: Message, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndFinalizeCorrelation(self, result:IAsyncResult) -> Message:
        """ EndFinalizeCorrelation(self: CorrelationCallbackMessageProperty, result: IAsyncResult) -> Message """
        ...

    def FinalizeCorrelation(self, message:Message, timeout:TimeSpan) -> Message:
        """ FinalizeCorrelation(self: CorrelationCallbackMessageProperty, message: Message, timeout: TimeSpan) -> Message """
        ...

    def OnBeginFinalizeCorrelation(self, *args): #cannot find CLR method
        """ OnBeginFinalizeCorrelation(self: CorrelationCallbackMessageProperty, message: Message, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def OnEndFinalizeCorrelation(self, *args): #cannot find CLR method
        """ OnEndFinalizeCorrelation(self: CorrelationCallbackMessageProperty, result: IAsyncResult) -> Message """
        ...

    def OnFinalizeCorrelation(self, *args): #cannot find CLR method
        """ OnFinalizeCorrelation(self: CorrelationCallbackMessageProperty, message: Message, timeout: TimeSpan) -> Message """
        ...

    @staticmethod
    def TryGet(*__args:Message) -> Tuple_[bool, CorrelationCallbackMessageProperty]:
        """
        TryGet(message: Message) -> (bool, CorrelationCallbackMessageProperty)
        TryGet(properties: MessageProperties) -> (bool, CorrelationCallbackMessageProperty)
        """
        ...



class CorrelationDataDescription: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsDefault(self) -> bool:
        """ Get: IsDefault(self: CorrelationDataDescription) -> bool """
        ...

    @property
    def IsOptional(self) -> bool:
        """ Get: IsOptional(self: CorrelationDataDescription) -> bool """
        ...

    @property
    def KnownBeforeSend(self) -> bool:
        """ Get: KnownBeforeSend(self: CorrelationDataDescription) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: CorrelationDataDescription) -> str """
        ...

    @property
    def ReceiveValue(self) -> bool:
        """ Get: ReceiveValue(self: CorrelationDataDescription) -> bool """
        ...

    @property
    def SendValue(self) -> bool:
        """ Get: SendValue(self: CorrelationDataDescription) -> bool """
        ...



class CorrelationDataMessageProperty(IMessageProperty): # skipped bases: <type 'object'>
    """ CorrelationDataMessageProperty() """
    @property
    def Name(self) -> str:
        """ Get: Name() -> str """
        ...


    def Add(self, name:str, dataProvider): # ->  # Not found arg types: {'dataProvider': 'Func'}
        """ Add(self: CorrelationDataMessageProperty, name: str, dataProvider: Func[str]) """
        ...

    @staticmethod
    def AddData(message:Message, name:str, dataProvider): # ->  # Not found arg types: {'dataProvider': 'Func'}
        """ AddData(message: Message, name: str, dataProvider: Func[str]) """
        ...

    def Remove(self, name:str) -> bool:
        """ Remove(self: CorrelationDataMessageProperty, name: str) -> bool """
        ...

    @staticmethod
    def TryGet(*__args:Message) -> Tuple_[bool, CorrelationDataMessageProperty]:
        """
        TryGet(message: Message) -> (bool, CorrelationDataMessageProperty)
        TryGet(properties: MessageProperties) -> (bool, CorrelationDataMessageProperty)
        """
        ...

    def TryGetValue(self, name, value) -> Tuple_[bool, str]:
        """ TryGetValue(self: CorrelationDataMessageProperty, name: str) -> (bool, str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...



class CorrelationKey(InstanceKey): # skipped bases: <type 'object'>
    """ CorrelationKey(keyData: IDictionary[str, str], scopeName: XName, provider: XNamespace) """
    @property
    def KeyData(self) -> IDictionary:
        """ Get: KeyData(self: CorrelationKey) -> IDictionary[str, str] """
        ...

    @property
    def KeyString(self) -> str:
        """ Get: KeyString(self: CorrelationKey) -> str """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: CorrelationKey) -> str
        Set: Name(self: CorrelationKey) = value
        """
        ...

    @property
    def Provider(self) -> XNamespace:
        """ Get: Provider(self: CorrelationKey) -> XNamespace """
        ...

    @property
    def ScopeName(self) -> XName:
        """ Get: ScopeName(self: CorrelationKey) -> XName """
        ...



class CorrelationMessageProperty: # skipped bases: <type 'object'>, <type 'object'>
    """
    CorrelationMessageProperty(correlationKey: InstanceKey, additionalKeys: IEnumerable[InstanceKey])
    CorrelationMessageProperty(correlationKey: InstanceKey, additionalKeys: IEnumerable[InstanceKey], transientCorrelations: IEnumerable[InstanceKey])
    """
    @property
    def AdditionalKeys(self) -> ReadOnlyCollection:
        """ Get: AdditionalKeys(self: CorrelationMessageProperty) -> ReadOnlyCollection[InstanceKey] """
        ...

    @property
    def CorrelationKey(self) -> InstanceKey:
        """ Get: CorrelationKey(self: CorrelationMessageProperty) -> InstanceKey """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name() -> str """
        ...

    @property
    def TransientCorrelations(self) -> ReadOnlyCollection:
        """ Get: TransientCorrelations(self: CorrelationMessageProperty) -> ReadOnlyCollection[InstanceKey] """
        ...


    @staticmethod
    def TryGet(*__args:Message) -> Tuple_[bool, CorrelationMessageProperty]:
        """
        TryGet(message: Message) -> (bool, CorrelationMessageProperty)
        TryGet(properties: MessageProperties) -> (bool, CorrelationMessageProperty)
        """
        ...



class CustomBinding(Binding): # skipped bases: <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    CustomBinding()
    CustomBinding(configurationName: str)
    CustomBinding(*bindingElementsInTopDownChannelStackOrder: Array[BindingElement])
    CustomBinding(name: str, ns: str, *bindingElementsInTopDownChannelStackOrder: Array[BindingElement])
    CustomBinding(bindingElementsInTopDownChannelStackOrder: IEnumerable[BindingElement])
    CustomBinding(binding: Binding)
    """
    @property
    def Elements(self) -> BindingElementCollection:
        """ Get: Elements(self: CustomBinding) -> BindingElementCollection """
        ...



class DeliveryFailure(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DeliveryFailure, values: AccessDenied (32772), BadDestinationQueue (32768), BadEncryption (32775), BadSignature (32774), CouldNotEncrypt (32776), HopCountExceeded (32773), NotTransactionalMessage (32778), NotTransactionalQueue (32777), Purged (32769), QueueDeleted (49152), QueueExceedMaximumSize (32771), QueuePurged (49153), ReachQueueTimeout (32770), ReceiveTimeout (49154), Unknown (0) """
    AccessDenied: DeliveryFailure = ...
    BadDestinationQueue: DeliveryFailure = ...
    BadEncryption: DeliveryFailure = ...
    BadSignature: DeliveryFailure = ...
    CouldNotEncrypt: DeliveryFailure = ...
    HopCountExceeded: DeliveryFailure = ...
    NotTransactionalMessage: DeliveryFailure = ...
    NotTransactionalQueue: DeliveryFailure = ...
    Purged: DeliveryFailure = ...
    QueueDeleted: DeliveryFailure = ...
    QueueExceedMaximumSize: DeliveryFailure = ...
    QueuePurged: DeliveryFailure = ...
    ReachQueueTimeout: DeliveryFailure = ...
    ReceiveTimeout: DeliveryFailure = ...
    Unknown: DeliveryFailure = ...
    value__ = ...


class DeliveryStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DeliveryStatus, values: InDoubt (0), NotDelivered (1) """
    InDoubt: DeliveryStatus = ...
    NotDelivered: DeliveryStatus = ...
    value__ = ...


class FaultConverter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetDefaultFaultConverter(version) -> FaultConverter: # Not found arg types: {'version': 'MessageVersion'}
        """ GetDefaultFaultConverter(version: MessageVersion) -> FaultConverter """
        ...

    def OnTryCreateException(self, *args): #cannot find CLR method
        """ OnTryCreateException(self: FaultConverter, message: Message, fault: MessageFault) -> (bool, Exception) """
        ...

    def OnTryCreateFaultMessage(self, *args): #cannot find CLR method
        """ OnTryCreateFaultMessage(self: FaultConverter, exception: Exception) -> (bool, Message) """
        ...

    def TryCreateException(self, message, fault, exception) -> Tuple_[bool, Exception]:
        """ TryCreateException(self: FaultConverter, message: Message, fault: MessageFault) -> (bool, Exception) """
        ...

    def TryCreateFaultMessage(self, exception, message) -> Tuple_[bool, Message]:
        """ TryCreateFaultMessage(self: FaultConverter, exception: Exception) -> (bool, Message) """
        ...


class HttpCookieContainerBindingElement(BindingElement): # skipped bases: <type 'object'>
    """ HttpCookieContainerBindingElement() """
    pass

class HttpMessageHandlerFactory: # skipped bases: <type 'object'>, <type 'object'>
    """
    HttpMessageHandlerFactory(*handlers: Array[Type])
    HttpMessageHandlerFactory(handlers: Func[IEnumerable[DelegatingHandler]])
    """
    def Create(self, innerChannel:HttpMessageHandler) -> HttpMessageHandler:
        """ Create(self: HttpMessageHandlerFactory, innerChannel: HttpMessageHandler) -> HttpMessageHandler """
        ...

    def OnCreate(self, *args): #cannot find CLR method
        """ OnCreate(self: HttpMessageHandlerFactory, innerChannel: HttpMessageHandler) -> HttpMessageHandler """
        ...


class HttpMessageSettings(IEquatable): # skipped bases: <type 'object'>
    """ HttpMessageSettings() """
    @property
    def HttpMessagesSupported(self) -> bool:
        """
        Get: HttpMessagesSupported(self: HttpMessageSettings) -> bool
        Set: HttpMessagesSupported(self: HttpMessageSettings) = value
        """
        ...



class HttpRequestMessageExtensionMethods: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ToMessage(httpRequestMessage:HttpRequestMessage) -> Message:
        """ ToMessage(httpRequestMessage: HttpRequestMessage) -> Message """
        ...

    __all__: list = ...


class IMessageProperty: # skipped bases: <type 'object'>
    """ no doc """
    def CreateCopy(self) -> IMessageProperty:
        """ CreateCopy(self: IMessageProperty) -> IMessageProperty """
        ...


class HttpRequestMessageProperty(IMessageProperty, IMergeEnabledMessageProperty): # skipped bases: <type 'object'>
    """ HttpRequestMessageProperty() """
    @property
    def Headers(self) -> WebHeaderCollection:
        """ Get: Headers(self: HttpRequestMessageProperty) -> WebHeaderCollection """
        ...

    @property
    def Method(self) -> str:
        """
        Get: Method(self: HttpRequestMessageProperty) -> str
        Set: Method(self: HttpRequestMessageProperty) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name() -> str """
        ...

    @property
    def QueryString(self) -> str:
        """
        Get: QueryString(self: HttpRequestMessageProperty) -> str
        Set: QueryString(self: HttpRequestMessageProperty) = value
        """
        ...

    @property
    def SuppressEntityBody(self) -> bool:
        """
        Get: SuppressEntityBody(self: HttpRequestMessageProperty) -> bool
        Set: SuppressEntityBody(self: HttpRequestMessageProperty) = value
        """
        ...




class HttpResponseMessageExtensionMethods: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ToMessage(httpResponseMessage:HttpResponseMessage) -> Message:
        """ ToMessage(httpResponseMessage: HttpResponseMessage) -> Message """
        ...

    __all__: list = ...


class HttpResponseMessageProperty(IMessageProperty, IMergeEnabledMessageProperty): # skipped bases: <type 'object'>
    """ HttpResponseMessageProperty() """
    @property
    def Headers(self) -> WebHeaderCollection:
        """ Get: Headers(self: HttpResponseMessageProperty) -> WebHeaderCollection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name() -> str """
        ...

    @property
    def StatusCode(self) -> HttpStatusCode:
        """
        Get: StatusCode(self: HttpResponseMessageProperty) -> HttpStatusCode
        Set: StatusCode(self: HttpResponseMessageProperty) = value
        """
        ...

    @property
    def StatusDescription(self) -> str:
        """
        Get: StatusDescription(self: HttpResponseMessageProperty) -> str
        Set: StatusDescription(self: HttpResponseMessageProperty) = value
        """
        ...

    @property
    def SuppressEntityBody(self) -> bool:
        """
        Get: SuppressEntityBody(self: HttpResponseMessageProperty) -> bool
        Set: SuppressEntityBody(self: HttpResponseMessageProperty) = value
        """
        ...

    @property
    def SuppressPreamble(self) -> bool:
        """
        Get: SuppressPreamble(self: HttpResponseMessageProperty) -> bool
        Set: SuppressPreamble(self: HttpResponseMessageProperty) = value
        """
        ...




class HttpTransportBindingElement(TransportBindingElement, IPolicyExportExtension, ITransportPolicyImport, IWsdlExportExtension): # skipped bases: <type 'object'>
    """ HttpTransportBindingElement() """
    @property
    def AllowCookies(self) -> bool:
        """
        Get: AllowCookies(self: HttpTransportBindingElement) -> bool
        Set: AllowCookies(self: HttpTransportBindingElement) = value
        """
        ...

    @property
    def AuthenticationScheme(self) -> AuthenticationSchemes:
        """
        Get: AuthenticationScheme(self: HttpTransportBindingElement) -> AuthenticationSchemes
        Set: AuthenticationScheme(self: HttpTransportBindingElement) = value
        """
        ...

    @property
    def BypassProxyOnLocal(self) -> bool:
        """
        Get: BypassProxyOnLocal(self: HttpTransportBindingElement) -> bool
        Set: BypassProxyOnLocal(self: HttpTransportBindingElement) = value
        """
        ...

    @property
    def DecompressionEnabled(self) -> bool:
        """
        Get: DecompressionEnabled(self: HttpTransportBindingElement) -> bool
        Set: DecompressionEnabled(self: HttpTransportBindingElement) = value
        """
        ...

    @property
    def ExtendedProtectionPolicy(self) -> ExtendedProtectionPolicy:
        """
        Get: ExtendedProtectionPolicy(self: HttpTransportBindingElement) -> ExtendedProtectionPolicy
        Set: ExtendedProtectionPolicy(self: HttpTransportBindingElement) = value
        """
        ...

    @property
    def HostNameComparisonMode(self) -> HostNameComparisonMode:
        """
        Get: HostNameComparisonMode(self: HttpTransportBindingElement) -> HostNameComparisonMode
        Set: HostNameComparisonMode(self: HttpTransportBindingElement) = value
        """
        ...

    @property
    def KeepAliveEnabled(self) -> bool:
        """
        Get: KeepAliveEnabled(self: HttpTransportBindingElement) -> bool
        Set: KeepAliveEnabled(self: HttpTransportBindingElement) = value
        """
        ...

    @property
    def MaxBufferSize(self) -> int:
        """
        Get: MaxBufferSize(self: HttpTransportBindingElement) -> int
        Set: MaxBufferSize(self: HttpTransportBindingElement) = value
        """
        ...

    @property
    def MaxPendingAccepts(self) -> int:
        """
        Get: MaxPendingAccepts(self: HttpTransportBindingElement) -> int
        Set: MaxPendingAccepts(self: HttpTransportBindingElement) = value
        """
        ...

    @property
    def MessageHandlerFactory(self) -> HttpMessageHandlerFactory:
        """
        Get: MessageHandlerFactory(self: HttpTransportBindingElement) -> HttpMessageHandlerFactory
        Set: MessageHandlerFactory(self: HttpTransportBindingElement) = value
        """
        ...

    @property
    def ProxyAddress(self) -> Uri:
        """
        Get: ProxyAddress(self: HttpTransportBindingElement) -> Uri
        Set: ProxyAddress(self: HttpTransportBindingElement) = value
        """
        ...

    @property
    def ProxyAuthenticationScheme(self) -> AuthenticationSchemes:
        """
        Get: ProxyAuthenticationScheme(self: HttpTransportBindingElement) -> AuthenticationSchemes
        Set: ProxyAuthenticationScheme(self: HttpTransportBindingElement) = value
        """
        ...

    @property
    def Realm(self) -> str:
        """
        Get: Realm(self: HttpTransportBindingElement) -> str
        Set: Realm(self: HttpTransportBindingElement) = value
        """
        ...

    @property
    def RequestInitializationTimeout(self) -> TimeSpan:
        """
        Get: RequestInitializationTimeout(self: HttpTransportBindingElement) -> TimeSpan
        Set: RequestInitializationTimeout(self: HttpTransportBindingElement) = value
        """
        ...

    @property
    def TransferMode(self) -> TransferMode:
        """
        Get: TransferMode(self: HttpTransportBindingElement) -> TransferMode
        Set: TransferMode(self: HttpTransportBindingElement) = value
        """
        ...

    @property
    def UnsafeConnectionNtlmAuthentication(self) -> bool:
        """
        Get: UnsafeConnectionNtlmAuthentication(self: HttpTransportBindingElement) -> bool
        Set: UnsafeConnectionNtlmAuthentication(self: HttpTransportBindingElement) = value
        """
        ...

    @property
    def UseDefaultWebProxy(self) -> bool:
        """
        Get: UseDefaultWebProxy(self: HttpTransportBindingElement) -> bool
        Set: UseDefaultWebProxy(self: HttpTransportBindingElement) = value
        """
        ...

    @property
    def WebSocketSettings(self): # -> WebSocketTransportSettings
        """
        Get: WebSocketSettings(self: HttpTransportBindingElement) -> WebSocketTransportSettings
        Set: WebSocketSettings(self: HttpTransportBindingElement) = value
        """
        ...


    def BuildChannelFactory(self, context:BindingContext): # -> IChannelFactory
        """ BuildChannelFactory[TChannel](self: HttpTransportBindingElement, context: BindingContext) -> IChannelFactory[TChannel] """
        ...

    def BuildChannelListener(self, context:BindingContext): # -> IChannelListener
        """ BuildChannelListener[TChannel](self: HttpTransportBindingElement, context: BindingContext) -> IChannelListener[TChannel] """
        ...

    def CanBuildChannelFactory(self, context:BindingContext) -> bool:
        """ CanBuildChannelFactory[TChannel](self: HttpTransportBindingElement, context: BindingContext) -> bool """
        ...

    def CanBuildChannelListener(self, context:BindingContext) -> bool:
        """ CanBuildChannelListener[TChannel](self: HttpTransportBindingElement, context: BindingContext) -> bool """
        ...

    def Clone(self) -> BindingElement:
        """ Clone(self: HttpTransportBindingElement) -> BindingElement """
        ...

    def ShouldSerializeExtendedProtectionPolicy(self) -> bool:
        """ ShouldSerializeExtendedProtectionPolicy(self: HttpTransportBindingElement) -> bool """
        ...

    def ShouldSerializeMessageHandlerFactory(self) -> bool:
        """ ShouldSerializeMessageHandlerFactory(self: HttpTransportBindingElement) -> bool """
        ...

    def ShouldSerializeWebSocketSettings(self) -> bool:
        """ ShouldSerializeWebSocketSettings(self: HttpTransportBindingElement) -> bool """
        ...

    def UpdateAuthenticationSchemes(self, *args): #cannot find CLR method
        """ UpdateAuthenticationSchemes(self: HttpTransportBindingElement, context: BindingContext) """
        ...


class ITransportTokenAssertionProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetTransportTokenAssertion(self) -> XmlElement:
        """ GetTransportTokenAssertion(self: ITransportTokenAssertionProvider) -> XmlElement """
        ...


class HttpsTransportBindingElement(HttpTransportBindingElement, ITransportTokenAssertionProvider): # skipped bases: <type 'IPolicyExportExtension'>, <type 'ITransportPolicyImport'>, <type 'IWsdlExportExtension'>, <type 'object'>
    """ HttpsTransportBindingElement() """
    @property
    def RequireClientCertificate(self) -> bool:
        """
        Get: RequireClientCertificate(self: HttpsTransportBindingElement) -> bool
        Set: RequireClientCertificate(self: HttpsTransportBindingElement) = value
        """
        ...



class IAnonymousUriPrefixMatcher: # skipped bases: <type 'object'>
    """ no doc """
    def Register(self, anonymousUriPrefix:Uri): # -> 
        """ Register(self: IAnonymousUriPrefixMatcher, anonymousUriPrefix: Uri) """
        ...


class IBindingDeliveryCapabilities: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AssuresOrderedDelivery(self) -> bool:
        """ Get: AssuresOrderedDelivery(self: IBindingDeliveryCapabilities) -> bool """
        ...

    @property
    def QueuedDelivery(self) -> bool:
        """ Get: QueuedDelivery(self: IBindingDeliveryCapabilities) -> bool """
        ...



class IBindingMulticastCapabilities: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsMulticast(self) -> bool:
        """ Get: IsMulticast(self: IBindingMulticastCapabilities) -> bool """
        ...



class IBindingRuntimePreferences: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ReceiveSynchronously(self) -> bool:
        """ Get: ReceiveSynchronously(self: IBindingRuntimePreferences) -> bool """
        ...



class IChannelFactory: # skipped bases: <type 'object'>
    """ no doc """
    def GetProperty(self): # -> T
        """ GetProperty[T](self: IChannelFactory) -> T """
        ...


class IChannelListener: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Uri(self) -> Uri:
        """ Get: Uri(self: IChannelListener) -> Uri """
        ...


    def BeginWaitForChannel(self, timeout:TimeSpan, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginWaitForChannel(self: IChannelListener, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndWaitForChannel(self, result:IAsyncResult) -> bool:
        """ EndWaitForChannel(self: IChannelListener, result: IAsyncResult) -> bool """
        ...

    def GetProperty(self): # -> T
        """ GetProperty[T](self: IChannelListener) -> T """
        ...

    def WaitForChannel(self, timeout:TimeSpan) -> bool:
        """ WaitForChannel(self: IChannelListener, timeout: TimeSpan) -> bool """
        ...


class IContextManager: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: IContextManager) -> bool
        Set: Enabled(self: IContextManager) = value
        """
        ...


    def GetContext(self) -> IDictionary:
        """ GetContext(self: IContextManager) -> IDictionary[str, str] """
        ...

    def SetContext(self, context:IDictionary): # -> 
        """ SetContext(self: IContextManager, context: IDictionary[str, str]) """
        ...


class ICorrelationDataSource: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataSources(self) -> ICollection:
        """ Get: DataSources(self: ICorrelationDataSource) -> ICollection[CorrelationDataDescription] """
        ...



class IInputChannel(IChannel): # skipped bases: <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    @property
    def LocalAddress(self) -> EndpointAddress:
        """ Get: LocalAddress(self: IInputChannel) -> EndpointAddress """
        ...


    def BeginReceive(self, *__args) -> IAsyncResult:
        """
        BeginReceive(self: IInputChannel, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginReceive(self: IInputChannel, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginTryReceive(self, timeout:TimeSpan, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTryReceive(self: IInputChannel, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginWaitForMessage(self, timeout:TimeSpan, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginWaitForMessage(self: IInputChannel, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndReceive(self, result:IAsyncResult) -> Message:
        """ EndReceive(self: IInputChannel, result: IAsyncResult) -> Message """
        ...

    def EndTryReceive(self, result, message) -> Tuple_[bool, Message]:
        """ EndTryReceive(self: IInputChannel, result: IAsyncResult) -> (bool, Message) """
        ...

    def EndWaitForMessage(self, result:IAsyncResult) -> bool:
        """ EndWaitForMessage(self: IInputChannel, result: IAsyncResult) -> bool """
        ...

    def Receive(self, timeout:TimeSpan = ...) -> Message:
        """
        Receive(self: IInputChannel) -> Message
        Receive(self: IInputChannel, timeout: TimeSpan) -> Message
        """
        ...

    def TryReceive(self, timeout, message) -> Tuple_[bool, Message]:
        """ TryReceive(self: IInputChannel, timeout: TimeSpan) -> (bool, Message) """
        ...

    def WaitForMessage(self, timeout:TimeSpan) -> bool:
        """ WaitForMessage(self: IInputChannel, timeout: TimeSpan) -> bool """
        ...


class IOutputChannel(IChannel): # skipped bases: <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    @property
    def RemoteAddress(self) -> EndpointAddress:
        """ Get: RemoteAddress(self: IOutputChannel) -> EndpointAddress """
        ...

    @property
    def Via(self) -> Uri:
        """ Get: Via(self: IOutputChannel) -> Uri """
        ...


    def BeginSend(self, message, *__args) -> IAsyncResult:
        """
        BeginSend(self: IOutputChannel, message: Message, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginSend(self: IOutputChannel, message: Message, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def EndSend(self, result:IAsyncResult): # -> 
        """ EndSend(self: IOutputChannel, result: IAsyncResult) """
        ...

    def Send(self, message:Message, timeout:TimeSpan = ...): # -> 
        """ Send(self: IOutputChannel, message: Message)Send(self: IOutputChannel, message: Message, timeout: TimeSpan) """
        ...


class IDuplexChannel(IOutputChannel, IInputChannel): # skipped bases: <type 'IChannel'>, <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    pass

class ISession: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Id(self) -> str:
        """ Get: Id(self: ISession) -> str """
        ...



class IInputSession(ISession): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IOutputSession(ISession): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDuplexSession(IOutputSession, IInputSession): # skipped bases: <type 'ISession'>, <type 'object'>
    """ no doc """
    def BeginCloseOutputSession(self, *__args) -> IAsyncResult:
        """
        BeginCloseOutputSession(self: IDuplexSession, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginCloseOutputSession(self: IDuplexSession, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def CloseOutputSession(self, timeout:TimeSpan = ...): # -> 
        """ CloseOutputSession(self: IDuplexSession)CloseOutputSession(self: IDuplexSession, timeout: TimeSpan) """
        ...

    def EndCloseOutputSession(self, result:IAsyncResult): # -> 
        """ EndCloseOutputSession(self: IDuplexSession, result: IAsyncResult) """
        ...


class IDuplexSessionChannel(IDuplexChannel, ISessionChannel): # skipped bases: <type 'IOutputChannel'>, <type 'IChannel'>, <type 'ICommunicationObject'>, <type 'IInputChannel'>, <type 'object'>
    """ no doc """
    pass

class IHttpCookieContainerManager: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CookieContainer(self) -> CookieContainer:
        """
        Get: CookieContainer(self: IHttpCookieContainerManager) -> CookieContainer
        Set: CookieContainer(self: IHttpCookieContainerManager) = value
        """
        ...



class IInputSessionChannel(ISessionChannel, IInputChannel): # skipped bases: <type 'IChannel'>, <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    pass

class InvalidChannelBindingException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidChannelBindingException()
    InvalidChannelBindingException(message: str)
    InvalidChannelBindingException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class IOutputSessionChannel(ISessionChannel, IOutputChannel): # skipped bases: <type 'IChannel'>, <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    pass

class IReceiveContextSettings: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: IReceiveContextSettings) -> bool
        Set: Enabled(self: IReceiveContextSettings) = value
        """
        ...

    @property
    def ValidityDuration(self) -> TimeSpan:
        """ Get: ValidityDuration(self: IReceiveContextSettings) -> TimeSpan """
        ...



class IReplyChannel(IChannel): # skipped bases: <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    @property
    def LocalAddress(self) -> EndpointAddress:
        """ Get: LocalAddress(self: IReplyChannel) -> EndpointAddress """
        ...


    def BeginReceiveRequest(self, *__args) -> IAsyncResult:
        """
        BeginReceiveRequest(self: IReplyChannel, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginReceiveRequest(self: IReplyChannel, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginTryReceiveRequest(self, timeout:TimeSpan, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTryReceiveRequest(self: IReplyChannel, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginWaitForRequest(self, timeout:TimeSpan, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginWaitForRequest(self: IReplyChannel, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndReceiveRequest(self, result:IAsyncResult) -> RequestContext:
        """ EndReceiveRequest(self: IReplyChannel, result: IAsyncResult) -> RequestContext """
        ...

    def EndTryReceiveRequest(self, result, context) -> Tuple_[bool, RequestContext]:
        """ EndTryReceiveRequest(self: IReplyChannel, result: IAsyncResult) -> (bool, RequestContext) """
        ...

    def EndWaitForRequest(self, result:IAsyncResult) -> bool:
        """ EndWaitForRequest(self: IReplyChannel, result: IAsyncResult) -> bool """
        ...

    def ReceiveRequest(self, timeout:TimeSpan = ...) -> RequestContext:
        """
        ReceiveRequest(self: IReplyChannel) -> RequestContext
        ReceiveRequest(self: IReplyChannel, timeout: TimeSpan) -> RequestContext
        """
        ...

    def TryReceiveRequest(self, timeout, context) -> Tuple_[bool, RequestContext]:
        """ TryReceiveRequest(self: IReplyChannel, timeout: TimeSpan) -> (bool, RequestContext) """
        ...

    def WaitForRequest(self, timeout:TimeSpan) -> bool:
        """ WaitForRequest(self: IReplyChannel, timeout: TimeSpan) -> bool """
        ...


class IReplySessionChannel(ISessionChannel, IReplyChannel): # skipped bases: <type 'IChannel'>, <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    pass

class IRequestChannel(IChannel): # skipped bases: <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    @property
    def RemoteAddress(self) -> EndpointAddress:
        """ Get: RemoteAddress(self: IRequestChannel) -> EndpointAddress """
        ...

    @property
    def Via(self) -> Uri:
        """ Get: Via(self: IRequestChannel) -> Uri """
        ...


    def BeginRequest(self, message, *__args) -> IAsyncResult:
        """
        BeginRequest(self: IRequestChannel, message: Message, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginRequest(self: IRequestChannel, message: Message, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def EndRequest(self, result:IAsyncResult) -> Message:
        """ EndRequest(self: IRequestChannel, result: IAsyncResult) -> Message """
        ...

    def Request(self, message:Message, timeout:TimeSpan = ...) -> Message:
        """
        Request(self: IRequestChannel, message: Message) -> Message
        Request(self: IRequestChannel, message: Message, timeout: TimeSpan) -> Message
        """
        ...


class IRequestSessionChannel(ISessionChannel, IRequestChannel): # skipped bases: <type 'IChannel'>, <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    pass

class ISecurityCapabilities: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SupportedRequestProtectionLevel(self) -> ProtectionLevel:
        """ Get: SupportedRequestProtectionLevel(self: ISecurityCapabilities) -> ProtectionLevel """
        ...

    @property
    def SupportedResponseProtectionLevel(self) -> ProtectionLevel:
        """ Get: SupportedResponseProtectionLevel(self: ISecurityCapabilities) -> ProtectionLevel """
        ...

    @property
    def SupportsClientAuthentication(self) -> bool:
        """ Get: SupportsClientAuthentication(self: ISecurityCapabilities) -> bool """
        ...

    @property
    def SupportsClientWindowsIdentity(self) -> bool:
        """ Get: SupportsClientWindowsIdentity(self: ISecurityCapabilities) -> bool """
        ...

    @property
    def SupportsServerAuthentication(self) -> bool:
        """ Get: SupportsServerAuthentication(self: ISecurityCapabilities) -> bool """
        ...



class ISessionChannel: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Session(self):
        ...



class ITransactedBindingElement: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def TransactedReceiveEnabled(self) -> bool:
        """ Get: TransactedReceiveEnabled(self: ITransactedBindingElement) -> bool """
        ...



class IWebSocketCloseDetails: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def InputCloseStatus(self) -> Nullable:
        """ Get: InputCloseStatus(self: IWebSocketCloseDetails) -> Nullable[WebSocketCloseStatus] """
        ...

    @property
    def InputCloseStatusDescription(self) -> str:
        """ Get: InputCloseStatusDescription(self: IWebSocketCloseDetails) -> str """
        ...


    def SetOutputCloseStatus(self, closeStatus:WebSocketCloseStatus, closeStatusDescription:str): # -> 
        """ SetOutputCloseStatus(self: IWebSocketCloseDetails, closeStatus: WebSocketCloseStatus, closeStatusDescription: str) """
        ...


class JavascriptCallbackResponseMessageProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ JavascriptCallbackResponseMessageProperty() """
    @property
    def CallbackFunctionName(self) -> str:
        """
        Get: CallbackFunctionName(self: JavascriptCallbackResponseMessageProperty) -> str
        Set: CallbackFunctionName(self: JavascriptCallbackResponseMessageProperty) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name() -> str """
        ...

    @property
    def StatusCode(self) -> Nullable:
        """
        Get: StatusCode(self: JavascriptCallbackResponseMessageProperty) -> Nullable[HttpStatusCode]
        Set: StatusCode(self: JavascriptCallbackResponseMessageProperty) = value
        """
        ...




class LocalClientSecuritySettings: # skipped bases: <type 'object'>, <type 'object'>
    """ LocalClientSecuritySettings() """
    @property
    def CacheCookies(self) -> bool:
        """
        Get: CacheCookies(self: LocalClientSecuritySettings) -> bool
        Set: CacheCookies(self: LocalClientSecuritySettings) = value
        """
        ...

    @property
    def CookieRenewalThresholdPercentage(self) -> int:
        """
        Get: CookieRenewalThresholdPercentage(self: LocalClientSecuritySettings) -> int
        Set: CookieRenewalThresholdPercentage(self: LocalClientSecuritySettings) = value
        """
        ...

    @property
    def DetectReplays(self) -> bool:
        """
        Get: DetectReplays(self: LocalClientSecuritySettings) -> bool
        Set: DetectReplays(self: LocalClientSecuritySettings) = value
        """
        ...

    @property
    def IdentityVerifier(self) -> IdentityVerifier:
        """
        Get: IdentityVerifier(self: LocalClientSecuritySettings) -> IdentityVerifier
        Set: IdentityVerifier(self: LocalClientSecuritySettings) = value
        """
        ...

    @property
    def MaxClockSkew(self) -> TimeSpan:
        """
        Get: MaxClockSkew(self: LocalClientSecuritySettings) -> TimeSpan
        Set: MaxClockSkew(self: LocalClientSecuritySettings) = value
        """
        ...

    @property
    def MaxCookieCachingTime(self) -> TimeSpan:
        """
        Get: MaxCookieCachingTime(self: LocalClientSecuritySettings) -> TimeSpan
        Set: MaxCookieCachingTime(self: LocalClientSecuritySettings) = value
        """
        ...

    @property
    def NonceCache(self) -> NonceCache:
        """
        Get: NonceCache(self: LocalClientSecuritySettings) -> NonceCache
        Set: NonceCache(self: LocalClientSecuritySettings) = value
        """
        ...

    @property
    def ReconnectTransportOnFailure(self) -> bool:
        """
        Get: ReconnectTransportOnFailure(self: LocalClientSecuritySettings) -> bool
        Set: ReconnectTransportOnFailure(self: LocalClientSecuritySettings) = value
        """
        ...

    @property
    def ReplayCacheSize(self) -> int:
        """
        Get: ReplayCacheSize(self: LocalClientSecuritySettings) -> int
        Set: ReplayCacheSize(self: LocalClientSecuritySettings) = value
        """
        ...

    @property
    def ReplayWindow(self) -> TimeSpan:
        """
        Get: ReplayWindow(self: LocalClientSecuritySettings) -> TimeSpan
        Set: ReplayWindow(self: LocalClientSecuritySettings) = value
        """
        ...

    @property
    def SessionKeyRenewalInterval(self) -> TimeSpan:
        """
        Get: SessionKeyRenewalInterval(self: LocalClientSecuritySettings) -> TimeSpan
        Set: SessionKeyRenewalInterval(self: LocalClientSecuritySettings) = value
        """
        ...

    @property
    def SessionKeyRolloverInterval(self) -> TimeSpan:
        """
        Get: SessionKeyRolloverInterval(self: LocalClientSecuritySettings) -> TimeSpan
        Set: SessionKeyRolloverInterval(self: LocalClientSecuritySettings) = value
        """
        ...

    @property
    def TimestampValidityDuration(self) -> TimeSpan:
        """
        Get: TimestampValidityDuration(self: LocalClientSecuritySettings) -> TimeSpan
        Set: TimestampValidityDuration(self: LocalClientSecuritySettings) = value
        """
        ...


    def Clone(self) -> LocalClientSecuritySettings:
        """ Clone(self: LocalClientSecuritySettings) -> LocalClientSecuritySettings """
        ...


class LocalServiceSecuritySettings: # skipped bases: <type 'object'>, <type 'object'>
    """ LocalServiceSecuritySettings() """
    @property
    def DetectReplays(self) -> bool:
        """
        Get: DetectReplays(self: LocalServiceSecuritySettings) -> bool
        Set: DetectReplays(self: LocalServiceSecuritySettings) = value
        """
        ...

    @property
    def InactivityTimeout(self) -> TimeSpan:
        """
        Get: InactivityTimeout(self: LocalServiceSecuritySettings) -> TimeSpan
        Set: InactivityTimeout(self: LocalServiceSecuritySettings) = value
        """
        ...

    @property
    def IssuedCookieLifetime(self) -> TimeSpan:
        """
        Get: IssuedCookieLifetime(self: LocalServiceSecuritySettings) -> TimeSpan
        Set: IssuedCookieLifetime(self: LocalServiceSecuritySettings) = value
        """
        ...

    @property
    def MaxCachedCookies(self) -> int:
        """
        Get: MaxCachedCookies(self: LocalServiceSecuritySettings) -> int
        Set: MaxCachedCookies(self: LocalServiceSecuritySettings) = value
        """
        ...

    @property
    def MaxClockSkew(self) -> TimeSpan:
        """
        Get: MaxClockSkew(self: LocalServiceSecuritySettings) -> TimeSpan
        Set: MaxClockSkew(self: LocalServiceSecuritySettings) = value
        """
        ...

    @property
    def MaxPendingSessions(self) -> int:
        """
        Get: MaxPendingSessions(self: LocalServiceSecuritySettings) -> int
        Set: MaxPendingSessions(self: LocalServiceSecuritySettings) = value
        """
        ...

    @property
    def MaxStatefulNegotiations(self) -> int:
        """
        Get: MaxStatefulNegotiations(self: LocalServiceSecuritySettings) -> int
        Set: MaxStatefulNegotiations(self: LocalServiceSecuritySettings) = value
        """
        ...

    @property
    def NegotiationTimeout(self) -> TimeSpan:
        """
        Get: NegotiationTimeout(self: LocalServiceSecuritySettings) -> TimeSpan
        Set: NegotiationTimeout(self: LocalServiceSecuritySettings) = value
        """
        ...

    @property
    def NonceCache(self) -> NonceCache:
        """
        Get: NonceCache(self: LocalServiceSecuritySettings) -> NonceCache
        Set: NonceCache(self: LocalServiceSecuritySettings) = value
        """
        ...

    @property
    def ReconnectTransportOnFailure(self) -> bool:
        """
        Get: ReconnectTransportOnFailure(self: LocalServiceSecuritySettings) -> bool
        Set: ReconnectTransportOnFailure(self: LocalServiceSecuritySettings) = value
        """
        ...

    @property
    def ReplayCacheSize(self) -> int:
        """
        Get: ReplayCacheSize(self: LocalServiceSecuritySettings) -> int
        Set: ReplayCacheSize(self: LocalServiceSecuritySettings) = value
        """
        ...

    @property
    def ReplayWindow(self) -> TimeSpan:
        """
        Get: ReplayWindow(self: LocalServiceSecuritySettings) -> TimeSpan
        Set: ReplayWindow(self: LocalServiceSecuritySettings) = value
        """
        ...

    @property
    def SessionKeyRenewalInterval(self) -> TimeSpan:
        """
        Get: SessionKeyRenewalInterval(self: LocalServiceSecuritySettings) -> TimeSpan
        Set: SessionKeyRenewalInterval(self: LocalServiceSecuritySettings) = value
        """
        ...

    @property
    def SessionKeyRolloverInterval(self) -> TimeSpan:
        """
        Get: SessionKeyRolloverInterval(self: LocalServiceSecuritySettings) -> TimeSpan
        Set: SessionKeyRolloverInterval(self: LocalServiceSecuritySettings) = value
        """
        ...

    @property
    def TimestampValidityDuration(self) -> TimeSpan:
        """
        Get: TimestampValidityDuration(self: LocalServiceSecuritySettings) -> TimeSpan
        Set: TimestampValidityDuration(self: LocalServiceSecuritySettings) = value
        """
        ...


    def Clone(self) -> LocalServiceSecuritySettings:
        """ Clone(self: LocalServiceSecuritySettings) -> LocalServiceSecuritySettings """
        ...


class Message(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Headers(self): # -> MessageHeaders
        """ Get: Headers(self: Message) -> MessageHeaders """
        ...

    @property
    def IsDisposed(self):
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: Message) -> bool """
        ...

    @property
    def IsFault(self) -> bool:
        """ Get: IsFault(self: Message) -> bool """
        ...

    @property
    def Properties(self): # -> MessageProperties
        """ Get: Properties(self: Message) -> MessageProperties """
        ...

    @property
    def State(self): # -> MessageState
        """ Get: State(self: Message) -> MessageState """
        ...

    @property
    def Version(self): # -> MessageVersion
        """ Get: Version(self: Message) -> MessageVersion """
        ...


    def BeginWriteBodyContents(self, writer:XmlDictionaryWriter, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginWriteBodyContents(self: Message, writer: XmlDictionaryWriter, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginWriteMessage(self, writer:XmlDictionaryWriter, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginWriteMessage(self: Message, writer: XmlDictionaryWriter, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def Close(self): # -> 
        """ Close(self: Message) """
        ...

    def CreateBufferedCopy(self, maxBufferSize:int): # -> MessageBuffer
        """ CreateBufferedCopy(self: Message, maxBufferSize: int) -> MessageBuffer """
        ...

    @staticmethod
    def CreateMessage(*__args) -> Message:
        """
        CreateMessage(version: MessageVersion, action: str, body: object) -> Message
        CreateMessage(version: MessageVersion, action: str, body: object, serializer: XmlObjectSerializer) -> Message
        CreateMessage(version: MessageVersion, action: str, body: XmlReader) -> Message
        CreateMessage(version: MessageVersion, action: str, body: XmlDictionaryReader) -> Message
        CreateMessage(version: MessageVersion, action: str, body: BodyWriter) -> Message
        CreateMessage(version: MessageVersion, action: str) -> Message
        CreateMessage(envelopeReader: XmlReader, maxSizeOfHeaders: int, version: MessageVersion) -> Message
        CreateMessage(envelopeReader: XmlDictionaryReader, maxSizeOfHeaders: int, version: MessageVersion) -> Message
        CreateMessage(version: MessageVersion, faultCode: FaultCode, reason: str, action: str) -> Message
        CreateMessage(version: MessageVersion, faultCode: FaultCode, reason: str, detail: object, action: str) -> Message
        CreateMessage(version: MessageVersion, fault: MessageFault, action: str) -> Message
        """
        ...

    def EndWriteBodyContents(self, result:IAsyncResult): # -> 
        """ EndWriteBodyContents(self: Message, result: IAsyncResult) """
        ...

    def EndWriteMessage(self, result:IAsyncResult): # -> 
        """ EndWriteMessage(self: Message, result: IAsyncResult) """
        ...

    def GetBody(self, serializer = ...): # -> T # Not found arg types: {'serializer': 'XmlObjectSerializer'}
        """
        GetBody[T](self: Message) -> T
        GetBody[T](self: Message, serializer: XmlObjectSerializer) -> T
        """
        ...

    def GetBodyAttribute(self, localName:str, ns:str) -> str:
        """ GetBodyAttribute(self: Message, localName: str, ns: str) -> str """
        ...

    def GetReaderAtBodyContents(self) -> XmlDictionaryReader:
        """ GetReaderAtBodyContents(self: Message) -> XmlDictionaryReader """
        ...

    def OnBeginWriteBodyContents(self, *args): #cannot find CLR method
        """ OnBeginWriteBodyContents(self: Message, writer: XmlDictionaryWriter, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def OnBeginWriteMessage(self, *args): #cannot find CLR method
        """ OnBeginWriteMessage(self: Message, writer: XmlDictionaryWriter, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def OnBodyToString(self, *args): #cannot find CLR method
        """ OnBodyToString(self: Message, writer: XmlDictionaryWriter) """
        ...

    def OnClose(self, *args): #cannot find CLR method
        """ OnClose(self: Message) """
        ...

    def OnCreateBufferedCopy(self, *args): #cannot find CLR method
        """ OnCreateBufferedCopy(self: Message, maxBufferSize: int) -> MessageBuffer """
        ...

    def OnEndWriteBodyContents(self, *args): #cannot find CLR method
        """ OnEndWriteBodyContents(self: Message, result: IAsyncResult) """
        ...

    def OnEndWriteMessage(self, *args): #cannot find CLR method
        """ OnEndWriteMessage(self: Message, result: IAsyncResult) """
        ...

    def OnGetBody(self, *args): #cannot find CLR method
        """ OnGetBody[T](self: Message, reader: XmlDictionaryReader) -> T """
        ...

    def OnGetBodyAttribute(self, *args): #cannot find CLR method
        """ OnGetBodyAttribute(self: Message, localName: str, ns: str) -> str """
        ...

    def OnGetReaderAtBodyContents(self, *args): #cannot find CLR method
        """ OnGetReaderAtBodyContents(self: Message) -> XmlDictionaryReader """
        ...

    def OnWriteBodyContents(self, *args): #cannot find CLR method
        """ OnWriteBodyContents(self: Message, writer: XmlDictionaryWriter) """
        ...

    def OnWriteMessage(self, *args): #cannot find CLR method
        """ OnWriteMessage(self: Message, writer: XmlDictionaryWriter) """
        ...

    def OnWriteStartBody(self, *args): #cannot find CLR method
        """ OnWriteStartBody(self: Message, writer: XmlDictionaryWriter) """
        ...

    def OnWriteStartEnvelope(self, *args): #cannot find CLR method
        """ OnWriteStartEnvelope(self: Message, writer: XmlDictionaryWriter) """
        ...

    def OnWriteStartHeaders(self, *args): #cannot find CLR method
        """ OnWriteStartHeaders(self: Message, writer: XmlDictionaryWriter) """
        ...

    def ToString(self) -> str:
        """ ToString(self: Message) -> str """
        ...

    def WriteBody(self, writer:XmlWriter): # -> 
        """ WriteBody(self: Message, writer: XmlWriter)WriteBody(self: Message, writer: XmlDictionaryWriter) """
        ...

    def WriteBodyContents(self, writer:XmlDictionaryWriter): # -> 
        """ WriteBodyContents(self: Message, writer: XmlDictionaryWriter) """
        ...

    def WriteMessage(self, writer:XmlDictionaryWriter): # -> 
        """ WriteMessage(self: Message, writer: XmlDictionaryWriter)WriteMessage(self: Message, writer: XmlWriter) """
        ...

    def WriteStartBody(self, writer:XmlDictionaryWriter): # -> 
        """ WriteStartBody(self: Message, writer: XmlDictionaryWriter)WriteStartBody(self: Message, writer: XmlWriter) """
        ...

    def WriteStartEnvelope(self, writer:XmlDictionaryWriter): # -> 
        """ WriteStartEnvelope(self: Message, writer: XmlDictionaryWriter) """
        ...


class MessageBuffer(IDisposable, IXPathNavigable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BufferSize(self) -> int:
        """ Get: BufferSize(self: MessageBuffer) -> int """
        ...

    @property
    def MessageContentType(self) -> str:
        """ Get: MessageContentType(self: MessageBuffer) -> str """
        ...


    def Close(self): # -> 
        """ Close(self: MessageBuffer) """
        ...

    def CreateMessage(self) -> Message:
        """ CreateMessage(self: MessageBuffer) -> Message """
        ...

    def WriteMessage(self, stream:Stream): # -> 
        """ WriteMessage(self: MessageBuffer, stream: Stream) """
        ...


class MessageEncoder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ContentType(self) -> str:
        """ Get: ContentType(self: MessageEncoder) -> str """
        ...

    @property
    def MediaType(self) -> str:
        """ Get: MediaType(self: MessageEncoder) -> str """
        ...

    @property
    def MessageVersion(self): # -> MessageVersion
        """ Get: MessageVersion(self: MessageEncoder) -> MessageVersion """
        ...


    def BeginWriteMessage(self, message:Message, stream:Stream, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginWriteMessage(self: MessageEncoder, message: Message, stream: Stream, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndWriteMessage(self, result:IAsyncResult): # -> 
        """ EndWriteMessage(self: MessageEncoder, result: IAsyncResult) """
        ...

    def GetProperty(self): # -> T
        """ GetProperty[T](self: MessageEncoder) -> T """
        ...

    def IsContentTypeSupported(self, contentType:str) -> bool:
        """ IsContentTypeSupported(self: MessageEncoder, contentType: str) -> bool """
        ...

    def ReadMessage(self, *__args) -> Message:
        """
        ReadMessage(self: MessageEncoder, stream: Stream, maxSizeOfHeaders: int) -> Message
        ReadMessage(self: MessageEncoder, stream: Stream, maxSizeOfHeaders: int, contentType: str) -> Message
        ReadMessage(self: MessageEncoder, buffer: ArraySegment[Byte], bufferManager: BufferManager) -> Message
        ReadMessage(self: MessageEncoder, buffer: ArraySegment[Byte], bufferManager: BufferManager, contentType: str) -> Message
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: MessageEncoder) -> str """
        ...

    def WriteMessage(self, message:Message, *__args:Stream): # -> 
        """
        WriteMessage(self: MessageEncoder, message: Message, stream: Stream)WriteMessage(self: MessageEncoder, message: Message, maxMessageSize: int, bufferManager: BufferManager) -> ArraySegment[Byte]
        WriteMessage(self: MessageEncoder, message: Message, maxMessageSize: int, bufferManager: BufferManager, messageOffset: int) -> ArraySegment[Byte]
        """
        ...


class MessageEncoderFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Encoder(self) -> MessageEncoder:
        """ Get: Encoder(self: MessageEncoderFactory) -> MessageEncoder """
        ...

    @property
    def MessageVersion(self): # -> MessageVersion
        """ Get: MessageVersion(self: MessageEncoderFactory) -> MessageVersion """
        ...


    def CreateSessionEncoder(self) -> MessageEncoder:
        """ CreateSessionEncoder(self: MessageEncoderFactory) -> MessageEncoder """
        ...


class MessageEncodingBindingElementImporter(IPolicyImportExtension, IWsdlImportExtension): # skipped bases: <type 'object'>
    """ MessageEncodingBindingElementImporter() """
    pass

class MessageExtensionMethods: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ToHttpRequestMessage(message:Message) -> HttpRequestMessage:
        """ ToHttpRequestMessage(message: Message) -> HttpRequestMessage """
        ...

    @staticmethod
    def ToHttpResponseMessage(message:Message) -> HttpResponseMessage:
        """ ToHttpResponseMessage(message: Message) -> HttpResponseMessage """
        ...

    __all__: list = ...


class MessageFault: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Actor(self) -> str:
        """ Get: Actor(self: MessageFault) -> str """
        ...

    @property
    def Code(self) -> FaultCode:
        """ Get: Code(self: MessageFault) -> FaultCode """
        ...

    @property
    def HasDetail(self) -> bool:
        """ Get: HasDetail(self: MessageFault) -> bool """
        ...

    @property
    def IsMustUnderstandFault(self) -> bool:
        """ Get: IsMustUnderstandFault(self: MessageFault) -> bool """
        ...

    @property
    def Node(self) -> str:
        """ Get: Node(self: MessageFault) -> str """
        ...

    @property
    def Reason(self) -> FaultReason:
        """ Get: Reason(self: MessageFault) -> FaultReason """
        ...


    @staticmethod
    def CreateFault(*__args) -> MessageFault:
        """
        CreateFault(code: FaultCode, reason: str) -> MessageFault
        CreateFault(code: FaultCode, reason: FaultReason) -> MessageFault
        CreateFault(code: FaultCode, reason: FaultReason, detail: object, serializer: XmlObjectSerializer) -> MessageFault
        CreateFault(code: FaultCode, reason: FaultReason, detail: object) -> MessageFault
        CreateFault(code: FaultCode, reason: FaultReason, detail: object, serializer: XmlObjectSerializer, actor: str) -> MessageFault
        CreateFault(code: FaultCode, reason: FaultReason, detail: object, serializer: XmlObjectSerializer, actor: str, node: str) -> MessageFault
        CreateFault(message: Message, maxBufferSize: int) -> MessageFault
        """
        ...

    def GetDetail(self, serializer = ...): # -> T # Not found arg types: {'serializer': 'XmlObjectSerializer'}
        """
        GetDetail[T](self: MessageFault) -> T
        GetDetail[T](self: MessageFault, serializer: XmlObjectSerializer) -> T
        """
        ...

    def GetReaderAtDetailContents(self) -> XmlDictionaryReader:
        """ GetReaderAtDetailContents(self: MessageFault) -> XmlDictionaryReader """
        ...

    def OnGetReaderAtDetailContents(self, *args): #cannot find CLR method
        """ OnGetReaderAtDetailContents(self: MessageFault) -> XmlDictionaryReader """
        ...

    def OnWriteDetail(self, *args): #cannot find CLR method
        """ OnWriteDetail(self: MessageFault, writer: XmlDictionaryWriter, version: EnvelopeVersion) """
        ...

    def OnWriteDetailContents(self, *args): #cannot find CLR method
        """ OnWriteDetailContents(self: MessageFault, writer: XmlDictionaryWriter) """
        ...

    def OnWriteStartDetail(self, *args): #cannot find CLR method
        """ OnWriteStartDetail(self: MessageFault, writer: XmlDictionaryWriter, version: EnvelopeVersion) """
        ...

    @staticmethod
    def WasHeaderNotUnderstood(headers, name:str, ns:str) -> bool: # Not found arg types: {'headers': 'MessageHeaders'}
        """ WasHeaderNotUnderstood(headers: MessageHeaders, name: str, ns: str) -> bool """
        ...

    def WriteTo(self, writer:XmlWriter, version:EnvelopeVersion): # -> 
        """ WriteTo(self: MessageFault, writer: XmlWriter, version: EnvelopeVersion)WriteTo(self: MessageFault, writer: XmlDictionaryWriter, version: EnvelopeVersion) """
        ...


class MessageHeaderInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Actor(self) -> str:
        """ Get: Actor(self: MessageHeaderInfo) -> str """
        ...

    @property
    def IsReferenceParameter(self) -> bool:
        """ Get: IsReferenceParameter(self: MessageHeaderInfo) -> bool """
        ...

    @property
    def MustUnderstand(self) -> bool:
        """ Get: MustUnderstand(self: MessageHeaderInfo) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MessageHeaderInfo) -> str """
        ...

    @property
    def Namespace(self) -> str:
        """ Get: Namespace(self: MessageHeaderInfo) -> str """
        ...

    @property
    def Relay(self) -> bool:
        """ Get: Relay(self: MessageHeaderInfo) -> bool """
        ...



class MessageHeader(MessageHeaderInfo): # skipped bases: <type 'object'>
    """ no doc """
    @staticmethod
    def CreateHeader(name:str, ns:str, value:object, *__args:bool) -> MessageHeader:
        """
        CreateHeader(name: str, ns: str, value: object) -> MessageHeader
        CreateHeader(name: str, ns: str, value: object, mustUnderstand: bool) -> MessageHeader
        CreateHeader(name: str, ns: str, value: object, mustUnderstand: bool, actor: str) -> MessageHeader
        CreateHeader(name: str, ns: str, value: object, mustUnderstand: bool, actor: str, relay: bool) -> MessageHeader
        CreateHeader(name: str, ns: str, value: object, serializer: XmlObjectSerializer) -> MessageHeader
        CreateHeader(name: str, ns: str, value: object, serializer: XmlObjectSerializer, mustUnderstand: bool) -> MessageHeader
        CreateHeader(name: str, ns: str, value: object, serializer: XmlObjectSerializer, mustUnderstand: bool, actor: str) -> MessageHeader
        CreateHeader(name: str, ns: str, value: object, serializer: XmlObjectSerializer, mustUnderstand: bool, actor: str, relay: bool) -> MessageHeader
        """
        ...

    def IsMessageVersionSupported(self, messageVersion) -> bool: # Not found arg types: {'messageVersion': 'MessageVersion'}
        """ IsMessageVersionSupported(self: MessageHeader, messageVersion: MessageVersion) -> bool """
        ...

    def OnWriteHeaderContents(self, *args): #cannot find CLR method
        """ OnWriteHeaderContents(self: MessageHeader, writer: XmlDictionaryWriter, messageVersion: MessageVersion) """
        ...

    def OnWriteStartHeader(self, *args): #cannot find CLR method
        """ OnWriteStartHeader(self: MessageHeader, writer: XmlDictionaryWriter, messageVersion: MessageVersion) """
        ...

    def ToString(self) -> str:
        """ ToString(self: MessageHeader) -> str """
        ...

    def WriteHeader(self, writer:XmlWriter, messageVersion): # ->  # Not found arg types: {'messageVersion': 'MessageVersion'}
        """ WriteHeader(self: MessageHeader, writer: XmlWriter, messageVersion: MessageVersion)WriteHeader(self: MessageHeader, writer: XmlDictionaryWriter, messageVersion: MessageVersion) """
        ...

    def WriteHeaderAttributes(self, *args): #cannot find CLR method
        """ WriteHeaderAttributes(self: MessageHeader, writer: XmlDictionaryWriter, messageVersion: MessageVersion) """
        ...

    def WriteHeaderContents(self, writer:XmlDictionaryWriter, messageVersion): # ->  # Not found arg types: {'messageVersion': 'MessageVersion'}
        """ WriteHeaderContents(self: MessageHeader, writer: XmlDictionaryWriter, messageVersion: MessageVersion) """
        ...

    def WriteStartHeader(self, writer:XmlDictionaryWriter, messageVersion): # ->  # Not found arg types: {'messageVersion': 'MessageVersion'}
        """ WriteStartHeader(self: MessageHeader, writer: XmlDictionaryWriter, messageVersion: MessageVersion) """
        ...


class MessageHeaders(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """
    MessageHeaders(version: MessageVersion, initialSize: int)
    MessageHeaders(version: MessageVersion)
    MessageHeaders(collection: MessageHeaders)
    """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: MessageHeaders) -> str
        Set: Action(self: MessageHeaders) = value
        """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: MessageHeaders) -> int """
        ...

    @property
    def FaultTo(self) -> EndpointAddress:
        """
        Get: FaultTo(self: MessageHeaders) -> EndpointAddress
        Set: FaultTo(self: MessageHeaders) = value
        """
        ...

    @property
    def From(self) -> EndpointAddress:
        """
        Get: From(self: MessageHeaders) -> EndpointAddress
        Set: From(self: MessageHeaders) = value
        """
        ...

    @property
    def MessageId(self) -> UniqueId:
        """
        Get: MessageId(self: MessageHeaders) -> UniqueId
        Set: MessageId(self: MessageHeaders) = value
        """
        ...

    @property
    def MessageVersion(self): # -> MessageVersion
        """ Get: MessageVersion(self: MessageHeaders) -> MessageVersion """
        ...

    @property
    def RelatesTo(self) -> UniqueId:
        """
        Get: RelatesTo(self: MessageHeaders) -> UniqueId
        Set: RelatesTo(self: MessageHeaders) = value
        """
        ...

    @property
    def ReplyTo(self) -> EndpointAddress:
        """
        Get: ReplyTo(self: MessageHeaders) -> EndpointAddress
        Set: ReplyTo(self: MessageHeaders) = value
        """
        ...

    @property
    def To(self) -> Uri:
        """
        Get: To(self: MessageHeaders) -> Uri
        Set: To(self: MessageHeaders) = value
        """
        ...

    @property
    def UnderstoodHeaders(self): # -> UnderstoodHeaders
        """ Get: UnderstoodHeaders(self: MessageHeaders) -> UnderstoodHeaders """
        ...


    def Add(self, header:MessageHeader): # -> 
        """ Add(self: MessageHeaders, header: MessageHeader) """
        ...

    def Clear(self): # -> 
        """ Clear(self: MessageHeaders) """
        ...

    def CopyHeaderFrom(self, *__args): # -> 
        """ CopyHeaderFrom(self: MessageHeaders, message: Message, headerIndex: int)CopyHeaderFrom(self: MessageHeaders, collection: MessageHeaders, headerIndex: int) """
        ...

    def CopyHeadersFrom(self, *__args:Message): # -> 
        """ CopyHeadersFrom(self: MessageHeaders, message: Message)CopyHeadersFrom(self: MessageHeaders, collection: MessageHeaders) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: MessageHeaders, array: Array[MessageHeaderInfo], index: int) """
        ...

    def FindHeader(self, name:str, ns:str, actors:Array = ...) -> int:
        """
        FindHeader(self: MessageHeaders, name: str, ns: str) -> int
        FindHeader(self: MessageHeaders, name: str, ns: str, *actors: Array[str]) -> int
        """
        ...

    def GetHeader(self, *__args:int): # -> T
        """
        GetHeader[T](self: MessageHeaders, name: str, ns: str) -> T
        GetHeader[T](self: MessageHeaders, name: str, ns: str, *actors: Array[str]) -> T
        GetHeader[T](self: MessageHeaders, name: str, ns: str, serializer: XmlObjectSerializer) -> T
        GetHeader[T](self: MessageHeaders, index: int) -> T
        GetHeader[T](self: MessageHeaders, index: int, serializer: XmlObjectSerializer) -> T
        """
        ...

    def GetReaderAtHeader(self, headerIndex:int) -> XmlDictionaryReader:
        """ GetReaderAtHeader(self: MessageHeaders, headerIndex: int) -> XmlDictionaryReader """
        ...

    def HaveMandatoryHeadersBeenUnderstood(self, actors:Array = ...) -> bool:
        """
        HaveMandatoryHeadersBeenUnderstood(self: MessageHeaders) -> bool
        HaveMandatoryHeadersBeenUnderstood(self: MessageHeaders, *actors: Array[str]) -> bool
        """
        ...

    def Insert(self, headerIndex:int, header:MessageHeader): # -> 
        """ Insert(self: MessageHeaders, headerIndex: int, header: MessageHeader) """
        ...

    def RemoveAll(self, name:str, ns:str): # -> 
        """ RemoveAll(self: MessageHeaders, name: str, ns: str) """
        ...

    def RemoveAt(self, headerIndex:int): # -> 
        """ RemoveAt(self: MessageHeaders, headerIndex: int) """
        ...

    def SetAction(self, action:XmlDictionaryString): # -> 
        """ SetAction(self: MessageHeaders, action: XmlDictionaryString) """
        ...

    def WriteHeader(self, headerIndex:int, writer:XmlWriter): # -> 
        """ WriteHeader(self: MessageHeaders, headerIndex: int, writer: XmlWriter)WriteHeader(self: MessageHeaders, headerIndex: int, writer: XmlDictionaryWriter) """
        ...

    def WriteHeaderContents(self, headerIndex:int, writer:XmlDictionaryWriter): # -> 
        """ WriteHeaderContents(self: MessageHeaders, headerIndex: int, writer: XmlDictionaryWriter)WriteHeaderContents(self: MessageHeaders, headerIndex: int, writer: XmlWriter) """
        ...

    def WriteStartHeader(self, headerIndex:int, writer:XmlDictionaryWriter): # -> 
        """ WriteStartHeader(self: MessageHeaders, headerIndex: int, writer: XmlDictionaryWriter)WriteStartHeader(self: MessageHeaders, headerIndex: int, writer: XmlWriter) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MessageHeaderInfo](enumerable: IEnumerable[MessageHeaderInfo], value: MessageHeaderInfo) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class MessageProperties(IDictionary, IDisposable): # skipped bases: <type 'IEnumerable[KeyValuePair[str, object]]'>, <type 'ICollection[KeyValuePair[str, object]]'>, <type 'IEnumerable'>, <type 'object'>
    """
    MessageProperties()
    MessageProperties(properties: MessageProperties)
    """
    @property
    def AllowOutputBatching(self) -> bool:
        """
        Get: AllowOutputBatching(self: MessageProperties) -> bool
        Set: AllowOutputBatching(self: MessageProperties) = value
        """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: MessageProperties) -> int """
        ...

    @property
    def Encoder(self) -> MessageEncoder:
        """
        Get: Encoder(self: MessageProperties) -> MessageEncoder
        Set: Encoder(self: MessageProperties) = value
        """
        ...

    @property
    def IsFixedSize(self) -> bool:
        """ Get: IsFixedSize(self: MessageProperties) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: MessageProperties) -> bool """
        ...

    @property
    def Security(self) -> SecurityMessageProperty:
        """
        Get: Security(self: MessageProperties) -> SecurityMessageProperty
        Set: Security(self: MessageProperties) = value
        """
        ...

    @property
    def Via(self) -> Uri:
        """
        Get: Via(self: MessageProperties) -> Uri
        Set: Via(self: MessageProperties) = value
        """
        ...


    def Clear(self): # -> 
        """ Clear(self: MessageProperties) """
        ...

    def CopyProperties(self, properties:MessageProperties): # -> 
        """ CopyProperties(self: MessageProperties, properties: MessageProperties) """
        ...


class MessageState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MessageState, values: Closed (4), Copied (3), Created (0), Read (1), Written (2) """
    Closed: MessageState = ...
    Copied: MessageState = ...
    Created: MessageState = ...
    Read: MessageState = ...
    value__ = ...
    Written: MessageState = ...


class MessageVersion: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Addressing(self) -> AddressingVersion:
        """ Get: Addressing(self: MessageVersion) -> AddressingVersion """
        ...

    @property
    def Default(self) -> MessageVersion:
        """ Get: Default() -> MessageVersion """
        ...

    @property
    def Envelope(self) -> EnvelopeVersion:
        """ Get: Envelope(self: MessageVersion) -> EnvelopeVersion """
        ...

    @property
    def Soap11(self) -> MessageVersion:
        """ Get: Soap11() -> MessageVersion """
        ...

    @property
    def Soap11WSAddressing10(self) -> MessageVersion:
        """ Get: Soap11WSAddressing10() -> MessageVersion """
        ...

    @property
    def Soap11WSAddressingAugust2004(self) -> MessageVersion:
        """ Get: Soap11WSAddressingAugust2004() -> MessageVersion """
        ...

    @property
    def Soap12(self) -> MessageVersion:
        """ Get: Soap12() -> MessageVersion """
        ...

    @property
    def Soap12WSAddressing10(self) -> MessageVersion:
        """ Get: Soap12WSAddressing10() -> MessageVersion """
        ...

    @property
    def Soap12WSAddressingAugust2004(self) -> MessageVersion:
        """ Get: Soap12WSAddressingAugust2004() -> MessageVersion """
        ...


    @staticmethod
    def CreateVersion(envelopeVersion:EnvelopeVersion, addressingVersion:AddressingVersion = ...) -> MessageVersion:
        """
        CreateVersion(envelopeVersion: EnvelopeVersion, addressingVersion: AddressingVersion) -> MessageVersion
        CreateVersion(envelopeVersion: EnvelopeVersion) -> MessageVersion
        """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: MessageVersion, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: MessageVersion) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: MessageVersion) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class MsmqBindingElementBase(TransportBindingElement, IPolicyExportExtension, ITransactedBindingElement, ITransportPolicyImport, IWsdlExportExtension): # skipped bases: <type 'object'>
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
    def MaxRetryCycles(self) -> int:
        """
        Get: MaxRetryCycles(self: MsmqBindingElementBase) -> int
        Set: MaxRetryCycles(self: MsmqBindingElementBase) = value
        """
        ...

    @property
    def MsmqTransportSecurity(self) -> MsmqTransportSecurity:
        """ Get: MsmqTransportSecurity(self: MsmqBindingElementBase) -> MsmqTransportSecurity """
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



class MsmqMessageProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AbortCount(self) -> int:
        """ Get: AbortCount(self: MsmqMessageProperty) -> int """
        ...

    @property
    def DeliveryFailure(self) -> Nullable:
        """ Get: DeliveryFailure(self: MsmqMessageProperty) -> Nullable[DeliveryFailure] """
        ...

    @property
    def DeliveryStatus(self) -> Nullable:
        """ Get: DeliveryStatus(self: MsmqMessageProperty) -> Nullable[DeliveryStatus] """
        ...

    @property
    def MoveCount(self) -> int:
        """ Get: MoveCount(self: MsmqMessageProperty) -> int """
        ...


    @staticmethod
    def Get(message:Message) -> MsmqMessageProperty:
        """ Get(message: Message) -> MsmqMessageProperty """
        ...

    Name: str = ...


class MsmqTransportBindingElement(MsmqBindingElementBase): # skipped bases: <type 'IPolicyExportExtension'>, <type 'ITransactedBindingElement'>, <type 'ITransportPolicyImport'>, <type 'IWsdlExportExtension'>, <type 'object'>
    """ MsmqTransportBindingElement() """
    @property
    def MaxPoolSize(self) -> int:
        """
        Get: MaxPoolSize(self: MsmqTransportBindingElement) -> int
        Set: MaxPoolSize(self: MsmqTransportBindingElement) = value
        """
        ...

    @property
    def QueueTransferProtocol(self) -> QueueTransferProtocol:
        """
        Get: QueueTransferProtocol(self: MsmqTransportBindingElement) -> QueueTransferProtocol
        Set: QueueTransferProtocol(self: MsmqTransportBindingElement) = value
        """
        ...

    @property
    def Scheme(self) -> str:
        """ Get: Scheme(self: MsmqTransportBindingElement) -> str """
        ...

    @property
    def UseActiveDirectory(self) -> bool:
        """
        Get: UseActiveDirectory(self: MsmqTransportBindingElement) -> bool
        Set: UseActiveDirectory(self: MsmqTransportBindingElement) = value
        """
        ...


    def BuildChannelFactory(self, context:BindingContext) -> IChannelFactory:
        """ BuildChannelFactory[TChannel](self: MsmqTransportBindingElement, context: BindingContext) -> IChannelFactory[TChannel] """
        ...

    def BuildChannelListener(self, context:BindingContext) -> IChannelListener:
        """ BuildChannelListener[TChannel](self: MsmqTransportBindingElement, context: BindingContext) -> IChannelListener[TChannel] """
        ...

    def CanBuildChannelFactory(self, context:BindingContext) -> bool:
        """ CanBuildChannelFactory[TChannel](self: MsmqTransportBindingElement, context: BindingContext) -> bool """
        ...

    def CanBuildChannelListener(self, context:BindingContext) -> bool:
        """ CanBuildChannelListener[TChannel](self: MsmqTransportBindingElement, context: BindingContext) -> bool """
        ...

    def Clone(self) -> BindingElement:
        """ Clone(self: MsmqTransportBindingElement) -> BindingElement """
        ...


class MtomMessageEncodingBindingElement(IPolicyExportExtension, MessageEncodingBindingElement, IWsdlExportExtension): # skipped bases: <type 'object'>
    """
    MtomMessageEncodingBindingElement()
    MtomMessageEncodingBindingElement(messageVersion: MessageVersion, writeEncoding: Encoding)
    """
    @property
    def MaxBufferSize(self) -> int:
        """
        Get: MaxBufferSize(self: MtomMessageEncodingBindingElement) -> int
        Set: MaxBufferSize(self: MtomMessageEncodingBindingElement) = value
        """
        ...

    @property
    def MaxReadPoolSize(self) -> int:
        """
        Get: MaxReadPoolSize(self: MtomMessageEncodingBindingElement) -> int
        Set: MaxReadPoolSize(self: MtomMessageEncodingBindingElement) = value
        """
        ...

    @property
    def MaxWritePoolSize(self) -> int:
        """
        Get: MaxWritePoolSize(self: MtomMessageEncodingBindingElement) -> int
        Set: MaxWritePoolSize(self: MtomMessageEncodingBindingElement) = value
        """
        ...

    @property
    def ReaderQuotas(self) -> XmlDictionaryReaderQuotas:
        """ Get: ReaderQuotas(self: MtomMessageEncodingBindingElement) -> XmlDictionaryReaderQuotas """
        ...

    @property
    def WriteEncoding(self) -> Encoding:
        """
        Get: WriteEncoding(self: MtomMessageEncodingBindingElement) -> Encoding
        Set: WriteEncoding(self: MtomMessageEncodingBindingElement) = value
        """
        ...


    def BuildChannelFactory(self, context:BindingContext) -> IChannelFactory:
        """ BuildChannelFactory[TChannel](self: MtomMessageEncodingBindingElement, context: BindingContext) -> IChannelFactory[TChannel] """
        ...

    def BuildChannelListener(self, context:BindingContext) -> IChannelListener:
        """ BuildChannelListener[TChannel](self: MtomMessageEncodingBindingElement, context: BindingContext) -> IChannelListener[TChannel] """
        ...

    def CanBuildChannelFactory(self, context:BindingContext) -> bool:
        """ CanBuildChannelFactory[TChannel](self: MtomMessageEncodingBindingElement, context: BindingContext) -> bool """
        ...

    def CanBuildChannelListener(self, context:BindingContext) -> bool:
        """ CanBuildChannelListener[TChannel](self: MtomMessageEncodingBindingElement, context: BindingContext) -> bool """
        ...

    def Clone(self) -> BindingElement:
        """ Clone(self: MtomMessageEncodingBindingElement) -> BindingElement """
        ...

    def ShouldSerializeMessageVersion(self) -> bool:
        """ ShouldSerializeMessageVersion(self: MtomMessageEncodingBindingElement) -> bool """
        ...

    def ShouldSerializeReaderQuotas(self) -> bool:
        """ ShouldSerializeReaderQuotas(self: MtomMessageEncodingBindingElement) -> bool """
        ...

    def ShouldSerializeWriteEncoding(self) -> bool:
        """ ShouldSerializeWriteEncoding(self: MtomMessageEncodingBindingElement) -> bool """
        ...


class NamedPipeConnectionPoolSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def GroupName(self) -> str:
        """
        Get: GroupName(self: NamedPipeConnectionPoolSettings) -> str
        Set: GroupName(self: NamedPipeConnectionPoolSettings) = value
        """
        ...

    @property
    def IdleTimeout(self) -> TimeSpan:
        """
        Get: IdleTimeout(self: NamedPipeConnectionPoolSettings) -> TimeSpan
        Set: IdleTimeout(self: NamedPipeConnectionPoolSettings) = value
        """
        ...

    @property
    def MaxOutboundConnectionsPerEndpoint(self) -> int:
        """
        Get: MaxOutboundConnectionsPerEndpoint(self: NamedPipeConnectionPoolSettings) -> int
        Set: MaxOutboundConnectionsPerEndpoint(self: NamedPipeConnectionPoolSettings) = value
        """
        ...



class NamedPipeSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ApplicationContainerSettings(self) -> ApplicationContainerSettings:
        """ Get: ApplicationContainerSettings(self: NamedPipeSettings) -> ApplicationContainerSettings """
        ...



class NamedPipeTransportBindingElement(ConnectionOrientedTransportBindingElement): # skipped bases: <type 'IPolicyExportExtension'>, <type 'ITransportPolicyImport'>, <type 'IWsdlExportExtension'>, <type 'object'>
    """ NamedPipeTransportBindingElement() """
    @property
    def AllowedSecurityIdentifiers(self) -> Collection:
        """ Get: AllowedSecurityIdentifiers(self: NamedPipeTransportBindingElement) -> Collection[SecurityIdentifier] """
        ...

    @property
    def ConnectionPoolSettings(self) -> NamedPipeConnectionPoolSettings:
        """ Get: ConnectionPoolSettings(self: NamedPipeTransportBindingElement) -> NamedPipeConnectionPoolSettings """
        ...

    @property
    def PipeSettings(self) -> NamedPipeSettings:
        """ Get: PipeSettings(self: NamedPipeTransportBindingElement) -> NamedPipeSettings """
        ...

    @property
    def Scheme(self) -> str:
        """ Get: Scheme(self: NamedPipeTransportBindingElement) -> str """
        ...


    def BuildChannelFactory(self, context:BindingContext) -> IChannelFactory:
        """ BuildChannelFactory[TChannel](self: NamedPipeTransportBindingElement, context: BindingContext) -> IChannelFactory[TChannel] """
        ...

    def BuildChannelListener(self, context:BindingContext) -> IChannelListener:
        """ BuildChannelListener[TChannel](self: NamedPipeTransportBindingElement, context: BindingContext) -> IChannelListener[TChannel] """
        ...

    def Clone(self) -> BindingElement:
        """ Clone(self: NamedPipeTransportBindingElement) -> BindingElement """
        ...

    def __new__(cls) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, elementToBeCloned: NamedPipeTransportBindingElement)
        """
        ...


class NetworkInterfaceMessageProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ NetworkInterfaceMessageProperty(interfaceIndex: int) """
    @property
    def InterfaceIndex(self) -> int:
        """ Get: InterfaceIndex(self: NetworkInterfaceMessageProperty) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name() -> str """
        ...


    def AddTo(self, *__args:Message): # -> 
        """ AddTo(self: NetworkInterfaceMessageProperty, message: Message)AddTo(self: NetworkInterfaceMessageProperty, properties: MessageProperties) """
        ...

    @staticmethod
    def TryGet(*__args:Message) -> Tuple_[bool, NetworkInterfaceMessageProperty]:
        """
        TryGet(message: Message) -> (bool, NetworkInterfaceMessageProperty)
        TryGet(properties: MessageProperties) -> (bool, NetworkInterfaceMessageProperty)
        """
        ...



class OneWayBindingElement(IPolicyExportExtension, BindingElement): # skipped bases: <type 'object'>
    """ OneWayBindingElement() """
    @property
    def ChannelPoolSettings(self) -> ChannelPoolSettings:
        """
        Get: ChannelPoolSettings(self: OneWayBindingElement) -> ChannelPoolSettings
        Set: ChannelPoolSettings(self: OneWayBindingElement) = value
        """
        ...

    @property
    def MaxAcceptedChannels(self) -> int:
        """
        Get: MaxAcceptedChannels(self: OneWayBindingElement) -> int
        Set: MaxAcceptedChannels(self: OneWayBindingElement) = value
        """
        ...

    @property
    def PacketRoutable(self) -> bool:
        """
        Get: PacketRoutable(self: OneWayBindingElement) -> bool
        Set: PacketRoutable(self: OneWayBindingElement) = value
        """
        ...


    def ShouldSerializeChannelPoolSettings(self) -> bool:
        """ ShouldSerializeChannelPoolSettings(self: OneWayBindingElement) -> bool """
        ...


class OneWayBindingElementImporter(IPolicyImportExtension): # skipped bases: <type 'object'>
    """ OneWayBindingElementImporter() """
    pass

class PeerResolverBindingElement(BindingElement): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ReferralPolicy(self) -> PeerReferralPolicy:
        """
        Get: ReferralPolicy(self: PeerResolverBindingElement) -> PeerReferralPolicy
        Set: ReferralPolicy(self: PeerResolverBindingElement) = value
        """
        ...


    def CreatePeerResolver(self) -> PeerResolver:
        """ CreatePeerResolver(self: PeerResolverBindingElement) -> PeerResolver """
        ...


class PeerCustomResolverBindingElement(PeerResolverBindingElement): # skipped bases: <type 'object'>
    """
    PeerCustomResolverBindingElement()
    PeerCustomResolverBindingElement(other: PeerCustomResolverBindingElement)
    PeerCustomResolverBindingElement(settings: PeerCustomResolverSettings)
    PeerCustomResolverBindingElement(context: BindingContext, settings: PeerCustomResolverSettings)
    """
    @property
    def Address(self) -> EndpointAddress:
        """
        Get: Address(self: PeerCustomResolverBindingElement) -> EndpointAddress
        Set: Address(self: PeerCustomResolverBindingElement) = value
        """
        ...

    @property
    def Binding(self) -> Binding:
        """
        Get: Binding(self: PeerCustomResolverBindingElement) -> Binding
        Set: Binding(self: PeerCustomResolverBindingElement) = value
        """
        ...


    def BuildChannelFactory(self, context:BindingContext) -> IChannelFactory:
        """ BuildChannelFactory[TChannel](self: PeerCustomResolverBindingElement, context: BindingContext) -> IChannelFactory[TChannel] """
        ...

    def BuildChannelListener(self, context:BindingContext) -> IChannelListener:
        """ BuildChannelListener[TChannel](self: PeerCustomResolverBindingElement, context: BindingContext) -> IChannelListener[TChannel] """
        ...

    def CanBuildChannelFactory(self, context:BindingContext) -> bool:
        """ CanBuildChannelFactory[TChannel](self: PeerCustomResolverBindingElement, context: BindingContext) -> bool """
        ...

    def CanBuildChannelListener(self, context:BindingContext) -> bool:
        """ CanBuildChannelListener[TChannel](self: PeerCustomResolverBindingElement, context: BindingContext) -> bool """
        ...

    def Clone(self) -> BindingElement:
        """ Clone(self: PeerCustomResolverBindingElement) -> BindingElement """
        ...

    def GetProperty(self, context:BindingContext): # -> T
        """ GetProperty[T](self: PeerCustomResolverBindingElement, context: BindingContext) -> T """
        ...


class PeerTransportBindingElement(TransportBindingElement, IPolicyExportExtension, ITransportPolicyImport, IWsdlExportExtension): # skipped bases: <type 'object'>
    """ PeerTransportBindingElement() """
    @property
    def ListenIPAddress(self) -> IPAddress:
        """
        Get: ListenIPAddress(self: PeerTransportBindingElement) -> IPAddress
        Set: ListenIPAddress(self: PeerTransportBindingElement) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: PeerTransportBindingElement) -> int
        Set: Port(self: PeerTransportBindingElement) = value
        """
        ...

    @property
    def Security(self) -> PeerSecuritySettings:
        """ Get: Security(self: PeerTransportBindingElement) -> PeerSecuritySettings """
        ...


    def BuildChannelFactory(self, context:BindingContext) -> IChannelFactory:
        """ BuildChannelFactory[TChannel](self: PeerTransportBindingElement, context: BindingContext) -> IChannelFactory[TChannel] """
        ...

    def BuildChannelListener(self, context:BindingContext) -> IChannelListener:
        """ BuildChannelListener[TChannel](self: PeerTransportBindingElement, context: BindingContext) -> IChannelListener[TChannel] """
        ...

    def CanBuildChannelFactory(self, context:BindingContext) -> bool:
        """ CanBuildChannelFactory[TChannel](self: PeerTransportBindingElement, context: BindingContext) -> bool """
        ...

    def CanBuildChannelListener(self, context:BindingContext) -> bool:
        """ CanBuildChannelListener[TChannel](self: PeerTransportBindingElement, context: BindingContext) -> bool """
        ...

    def Clone(self) -> BindingElement:
        """ Clone(self: PeerTransportBindingElement) -> BindingElement """
        ...


class PnrpPeerResolverBindingElement(PeerResolverBindingElement): # skipped bases: <type 'object'>
    """
    PnrpPeerResolverBindingElement()
    PnrpPeerResolverBindingElement(referralPolicy: PeerReferralPolicy)
    """
    def BuildChannelFactory(self, context:BindingContext) -> IChannelFactory:
        """ BuildChannelFactory[TChannel](self: PnrpPeerResolverBindingElement, context: BindingContext) -> IChannelFactory[TChannel] """
        ...

    def BuildChannelListener(self, context:BindingContext) -> IChannelListener:
        """ BuildChannelListener[TChannel](self: PnrpPeerResolverBindingElement, context: BindingContext) -> IChannelListener[TChannel] """
        ...

    def CanBuildChannelFactory(self, context:BindingContext) -> bool:
        """ CanBuildChannelFactory[TChannel](self: PnrpPeerResolverBindingElement, context: BindingContext) -> bool """
        ...

    def CanBuildChannelListener(self, context:BindingContext) -> bool:
        """ CanBuildChannelListener[TChannel](self: PnrpPeerResolverBindingElement, context: BindingContext) -> bool """
        ...

    def Clone(self) -> BindingElement:
        """ Clone(self: PnrpPeerResolverBindingElement) -> BindingElement """
        ...

    def GetProperty(self, context:BindingContext): # -> T
        """ GetProperty[T](self: PnrpPeerResolverBindingElement, context: BindingContext) -> T """
        ...


class PrivacyNoticeBindingElement(IPolicyExportExtension, BindingElement): # skipped bases: <type 'object'>
    """
    PrivacyNoticeBindingElement()
    PrivacyNoticeBindingElement(elementToBeCloned: PrivacyNoticeBindingElement)
    """
    @property
    def Url(self) -> Uri:
        """
        Get: Url(self: PrivacyNoticeBindingElement) -> Uri
        Set: Url(self: PrivacyNoticeBindingElement) = value
        """
        ...

    @property
    def Version(self) -> int:
        """
        Get: Version(self: PrivacyNoticeBindingElement) -> int
        Set: Version(self: PrivacyNoticeBindingElement) = value
        """
        ...



class PrivacyNoticeBindingElementImporter(IPolicyImportExtension): # skipped bases: <type 'object'>
    """ PrivacyNoticeBindingElementImporter() """
    pass

class ReceiveContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def State(self): # -> ReceiveContextState
        """ Get: State(self: ReceiveContext) -> ReceiveContextState """
        ...

    @property
    def ThisLock(self):
        ...


    def Abandon(self, *__args:TimeSpan): # -> 
        """ Abandon(self: ReceiveContext, timeout: TimeSpan)Abandon(self: ReceiveContext, exception: Exception, timeout: TimeSpan) """
        ...

    def BeginAbandon(self, *__args) -> IAsyncResult:
        """
        BeginAbandon(self: ReceiveContext, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginAbandon(self: ReceiveContext, exception: Exception, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginComplete(self, timeout:TimeSpan, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginComplete(self: ReceiveContext, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def Complete(self, timeout:TimeSpan): # -> 
        """ Complete(self: ReceiveContext, timeout: TimeSpan) """
        ...

    def EndAbandon(self, result:IAsyncResult): # -> 
        """ EndAbandon(self: ReceiveContext, result: IAsyncResult) """
        ...

    def EndComplete(self, result:IAsyncResult): # -> 
        """ EndComplete(self: ReceiveContext, result: IAsyncResult) """
        ...

    def Fault(self, *args): #cannot find CLR method
        """ Fault(self: ReceiveContext) """
        ...

    def OnAbandon(self, *args): #cannot find CLR method
        """ OnAbandon(self: ReceiveContext, exception: Exception, timeout: TimeSpan)OnAbandon(self: ReceiveContext, timeout: TimeSpan) """
        ...

    def OnBeginAbandon(self, *args): #cannot find CLR method
        """
        OnBeginAbandon(self: ReceiveContext, exception: Exception, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        OnBeginAbandon(self: ReceiveContext, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def OnBeginComplete(self, *args): #cannot find CLR method
        """ OnBeginComplete(self: ReceiveContext, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def OnComplete(self, *args): #cannot find CLR method
        """ OnComplete(self: ReceiveContext, timeout: TimeSpan) """
        ...

    def OnEndAbandon(self, *args): #cannot find CLR method
        """ OnEndAbandon(self: ReceiveContext, result: IAsyncResult) """
        ...

    def OnEndComplete(self, *args): #cannot find CLR method
        """ OnEndComplete(self: ReceiveContext, result: IAsyncResult) """
        ...

    def OnFaulted(self, *args): #cannot find CLR method
        """ OnFaulted(self: ReceiveContext) """
        ...

    @staticmethod
    def TryGet(*__args:Message) -> Tuple_[bool, ReceiveContext]:
        """
        TryGet(message: Message) -> (bool, ReceiveContext)
        TryGet(properties: MessageProperties) -> (bool, ReceiveContext)
        """
        ...

    Faulted = ...
    Name: str = ...


class ReceiveContextState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ReceiveContextState, values: Abandoned (4), Abandoning (3), Completed (2), Completing (1), Faulted (5), Received (0) """
    Abandoned: ReceiveContextState = ...
    Abandoning: ReceiveContextState = ...
    Completed: ReceiveContextState = ...
    Completing: ReceiveContextState = ...
    Faulted: ReceiveContextState = ...
    Received: ReceiveContextState = ...
    value__ = ...


class RedirectionDuration: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Namespace(self) -> str:
        """ Get: Namespace(self: RedirectionDuration) -> str """
        ...

    @property
    def Permanent(self) -> RedirectionDuration:
        """ Get: Permanent() -> RedirectionDuration """
        ...

    @property
    def Temporary(self) -> RedirectionDuration:
        """ Get: Temporary() -> RedirectionDuration """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: RedirectionDuration) -> str """
        ...


    @staticmethod
    def Create(duration:str, ns:str) -> RedirectionDuration:
        """ Create(duration: str, ns: str) -> RedirectionDuration """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: RedirectionDuration, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: RedirectionDuration) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: RedirectionDuration) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class RedirectionException(CommunicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RedirectionException(type: RedirectionType, duration: RedirectionDuration, scope: RedirectionScope, *locations: Array[RedirectionLocation])
    RedirectionException(type: RedirectionType, duration: RedirectionDuration, scope: RedirectionScope, innerException: Exception, *locations: Array[RedirectionLocation])
    RedirectionException(message: str, type: RedirectionType, duration: RedirectionDuration, scope: RedirectionScope, *locations: Array[RedirectionLocation])
    RedirectionException(message: str, type: RedirectionType, duration: RedirectionDuration, scope: RedirectionScope, innerException: Exception, *locations: Array[RedirectionLocation])
    """
    @property
    def Duration(self) -> RedirectionDuration:
        """ Get: Duration(self: RedirectionException) -> RedirectionDuration """
        ...

    @property
    def Locations(self) -> IEnumerable:
        """ Get: Locations(self: RedirectionException) -> IEnumerable[RedirectionLocation] """
        ...

    @property
    def Scope(self): # -> RedirectionScope
        """ Get: Scope(self: RedirectionException) -> RedirectionScope """
        ...

    @property
    def Type(self): # -> RedirectionType
        """ Get: Type(self: RedirectionException) -> RedirectionType """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: RedirectionException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class RedirectionLocation: # skipped bases: <type 'object'>, <type 'object'>
    """ RedirectionLocation(address: Uri) """
    @property
    def Address(self) -> Uri:
        """ Get: Address(self: RedirectionLocation) -> Uri """
        ...



class RedirectionScope: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Endpoint(self) -> RedirectionScope:
        """ Get: Endpoint() -> RedirectionScope """
        ...

    @property
    def Message(self) -> RedirectionScope:
        """ Get: Message() -> RedirectionScope """
        ...

    @property
    def Namespace(self) -> str:
        """ Get: Namespace(self: RedirectionScope) -> str """
        ...

    @property
    def Session(self) -> RedirectionScope:
        """ Get: Session() -> RedirectionScope """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: RedirectionScope) -> str """
        ...


    @staticmethod
    def Create(scope:str, ns:str) -> RedirectionScope:
        """ Create(scope: str, ns: str) -> RedirectionScope """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: RedirectionScope, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: RedirectionScope) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: RedirectionScope) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class RedirectionType: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Cache(self) -> RedirectionType:
        """ Get: Cache() -> RedirectionType """
        ...

    @property
    def Namespace(self) -> str:
        """ Get: Namespace(self: RedirectionType) -> str """
        ...

    @property
    def Resource(self) -> RedirectionType:
        """ Get: Resource() -> RedirectionType """
        ...

    @property
    def UseIntermediary(self) -> RedirectionType:
        """ Get: UseIntermediary() -> RedirectionType """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: RedirectionType) -> str """
        ...


    @staticmethod
    def Create(type:str, ns:str) -> RedirectionType:
        """ Create(type: str, ns: str) -> RedirectionType """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: RedirectionType, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: RedirectionType) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: RedirectionType) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class ReliableSessionBindingElement(IPolicyExportExtension, BindingElement): # skipped bases: <type 'object'>
    """
    ReliableSessionBindingElement()
    ReliableSessionBindingElement(ordered: bool)
    """
    @property
    def AcknowledgementInterval(self) -> TimeSpan:
        """
        Get: AcknowledgementInterval(self: ReliableSessionBindingElement) -> TimeSpan
        Set: AcknowledgementInterval(self: ReliableSessionBindingElement) = value
        """
        ...

    @property
    def FlowControlEnabled(self) -> bool:
        """
        Get: FlowControlEnabled(self: ReliableSessionBindingElement) -> bool
        Set: FlowControlEnabled(self: ReliableSessionBindingElement) = value
        """
        ...

    @property
    def InactivityTimeout(self) -> TimeSpan:
        """
        Get: InactivityTimeout(self: ReliableSessionBindingElement) -> TimeSpan
        Set: InactivityTimeout(self: ReliableSessionBindingElement) = value
        """
        ...

    @property
    def MaxPendingChannels(self) -> int:
        """
        Get: MaxPendingChannels(self: ReliableSessionBindingElement) -> int
        Set: MaxPendingChannels(self: ReliableSessionBindingElement) = value
        """
        ...

    @property
    def MaxRetryCount(self) -> int:
        """
        Get: MaxRetryCount(self: ReliableSessionBindingElement) -> int
        Set: MaxRetryCount(self: ReliableSessionBindingElement) = value
        """
        ...

    @property
    def MaxTransferWindowSize(self) -> int:
        """
        Get: MaxTransferWindowSize(self: ReliableSessionBindingElement) -> int
        Set: MaxTransferWindowSize(self: ReliableSessionBindingElement) = value
        """
        ...

    @property
    def Ordered(self) -> bool:
        """
        Get: Ordered(self: ReliableSessionBindingElement) -> bool
        Set: Ordered(self: ReliableSessionBindingElement) = value
        """
        ...

    @property
    def ReliableMessagingVersion(self) -> ReliableMessagingVersion:
        """
        Get: ReliableMessagingVersion(self: ReliableSessionBindingElement) -> ReliableMessagingVersion
        Set: ReliableMessagingVersion(self: ReliableSessionBindingElement) = value
        """
        ...



class ReliableSessionBindingElementImporter(IPolicyImportExtension): # skipped bases: <type 'object'>
    """ ReliableSessionBindingElementImporter() """
    pass

class RemoteEndpointMessageProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ RemoteEndpointMessageProperty(address: str, port: int) """
    @property
    def Address(self) -> str:
        """ Get: Address(self: RemoteEndpointMessageProperty) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name() -> str """
        ...

    @property
    def Port(self) -> int:
        """ Get: Port(self: RemoteEndpointMessageProperty) -> int """
        ...




class RequestContext(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RequestMessage(self) -> Message:
        """ Get: RequestMessage(self: RequestContext) -> Message """
        ...


    def Abort(self): # -> 
        """ Abort(self: RequestContext) """
        ...

    def BeginReply(self, message, *__args) -> IAsyncResult:
        """
        BeginReply(self: RequestContext, message: Message, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginReply(self: RequestContext, message: Message, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def Close(self, timeout:TimeSpan = ...): # -> 
        """ Close(self: RequestContext)Close(self: RequestContext, timeout: TimeSpan) """
        ...

    def EndReply(self, result:IAsyncResult): # -> 
        """ EndReply(self: RequestContext, result: IAsyncResult) """
        ...

    def Reply(self, message:Message, timeout:TimeSpan = ...): # -> 
        """ Reply(self: RequestContext, message: Message)Reply(self: RequestContext, message: Message, timeout: TimeSpan) """
        ...


class RetryException(CommunicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RetryException()
    RetryException(message: str)
    RetryException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SecurityBindingElementImporter(IPolicyImportExtension): # skipped bases: <type 'object'>
    """ SecurityBindingElementImporter() """
    @property
    def MaxPolicyRedirections(self) -> int:
        """ Get: MaxPolicyRedirections(self: SecurityBindingElementImporter) -> int """
        ...



class SecurityHeaderLayout(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SecurityHeaderLayout, values: Lax (1), LaxTimestampFirst (2), LaxTimestampLast (3), Strict (0) """
    Lax: SecurityHeaderLayout = ...
    LaxTimestampFirst: SecurityHeaderLayout = ...
    LaxTimestampLast: SecurityHeaderLayout = ...
    Strict: SecurityHeaderLayout = ...
    value__ = ...


class SessionOpenNotification: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsEnabled(self) -> bool:
        """ Get: IsEnabled(self: SessionOpenNotification) -> bool """
        ...


    def UpdateMessageProperties(self, inboundMessageProperties:MessageProperties): # -> 
        """ UpdateMessageProperties(self: SessionOpenNotification, inboundMessageProperties: MessageProperties) """
        ...


class StreamUpgradeBindingElement(BindingElement): # skipped bases: <type 'object'>
    """ no doc """
    def BuildClientStreamUpgradeProvider(self, context:BindingContext): # -> StreamUpgradeProvider
        """ BuildClientStreamUpgradeProvider(self: StreamUpgradeBindingElement, context: BindingContext) -> StreamUpgradeProvider """
        ...

    def BuildServerStreamUpgradeProvider(self, context:BindingContext): # -> StreamUpgradeProvider
        """ BuildServerStreamUpgradeProvider(self: StreamUpgradeBindingElement, context: BindingContext) -> StreamUpgradeProvider """
        ...


class SslStreamSecurityBindingElement(ITransportTokenAssertionProvider, IPolicyExportExtension, StreamUpgradeBindingElement): # skipped bases: <type 'object'>
    """ SslStreamSecurityBindingElement() """
    @property
    def IdentityVerifier(self) -> IdentityVerifier:
        """
        Get: IdentityVerifier(self: SslStreamSecurityBindingElement) -> IdentityVerifier
        Set: IdentityVerifier(self: SslStreamSecurityBindingElement) = value
        """
        ...

    @property
    def RequireClientCertificate(self) -> bool:
        """
        Get: RequireClientCertificate(self: SslStreamSecurityBindingElement) -> bool
        Set: RequireClientCertificate(self: SslStreamSecurityBindingElement) = value
        """
        ...

    @property
    def SslProtocols(self) -> SslProtocols:
        """
        Get: SslProtocols(self: SslStreamSecurityBindingElement) -> SslProtocols
        Set: SslProtocols(self: SslStreamSecurityBindingElement) = value
        """
        ...


    def BuildChannelFactory(self, context:BindingContext) -> IChannelFactory:
        """ BuildChannelFactory[TChannel](self: SslStreamSecurityBindingElement, context: BindingContext) -> IChannelFactory[TChannel] """
        ...

    def BuildChannelListener(self, context:BindingContext) -> IChannelListener:
        """ BuildChannelListener[TChannel](self: SslStreamSecurityBindingElement, context: BindingContext) -> IChannelListener[TChannel] """
        ...

    def CanBuildChannelFactory(self, context:BindingContext) -> bool:
        """ CanBuildChannelFactory[TChannel](self: SslStreamSecurityBindingElement, context: BindingContext) -> bool """
        ...

    def CanBuildChannelListener(self, context:BindingContext) -> bool:
        """ CanBuildChannelListener[TChannel](self: SslStreamSecurityBindingElement, context: BindingContext) -> bool """
        ...

    def Clone(self) -> BindingElement:
        """ Clone(self: SslStreamSecurityBindingElement) -> BindingElement """
        ...

    def GetProperty(self, context:BindingContext): # -> T
        """ GetProperty[T](self: SslStreamSecurityBindingElement, context: BindingContext) -> T """
        ...

    def ShouldSerializeIdentityVerifier(self) -> bool:
        """ ShouldSerializeIdentityVerifier(self: SslStreamSecurityBindingElement) -> bool """
        ...


class StandardBindingImporter(IWsdlImportExtension): # skipped bases: <type 'object'>
    """ StandardBindingImporter() """
    pass

class StreamBodyWriter(BodyWriter): # skipped bases: <type 'object'>
    """ no doc """
    pass

class StreamUpgradeAcceptor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def AcceptUpgrade(self, stream:Stream) -> Stream:
        """ AcceptUpgrade(self: StreamUpgradeAcceptor, stream: Stream) -> Stream """
        ...

    def BeginAcceptUpgrade(self, stream:Stream, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginAcceptUpgrade(self: StreamUpgradeAcceptor, stream: Stream, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def CanUpgrade(self, contentType:str) -> bool:
        """ CanUpgrade(self: StreamUpgradeAcceptor, contentType: str) -> bool """
        ...

    def EndAcceptUpgrade(self, result:IAsyncResult) -> Stream:
        """ EndAcceptUpgrade(self: StreamUpgradeAcceptor, result: IAsyncResult) -> Stream """
        ...


class StreamSecurityUpgradeAcceptor(StreamUpgradeAcceptor): # skipped bases: <type 'object'>
    """ no doc """
    def GetRemoteSecurity(self) -> SecurityMessageProperty:
        """ GetRemoteSecurity(self: StreamSecurityUpgradeAcceptor) -> SecurityMessageProperty """
        ...


class StreamUpgradeInitiator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def BeginInitiateUpgrade(self, stream:Stream, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginInitiateUpgrade(self: StreamUpgradeInitiator, stream: Stream, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndInitiateUpgrade(self, result:IAsyncResult) -> Stream:
        """ EndInitiateUpgrade(self: StreamUpgradeInitiator, result: IAsyncResult) -> Stream """
        ...

    def GetNextUpgrade(self) -> str:
        """ GetNextUpgrade(self: StreamUpgradeInitiator) -> str """
        ...

    def InitiateUpgrade(self, stream:Stream) -> Stream:
        """ InitiateUpgrade(self: StreamUpgradeInitiator, stream: Stream) -> Stream """
        ...


class StreamSecurityUpgradeInitiator(StreamUpgradeInitiator): # skipped bases: <type 'object'>
    """ no doc """
    def GetRemoteSecurity(self) -> SecurityMessageProperty:
        """ GetRemoteSecurity(self: StreamSecurityUpgradeInitiator) -> SecurityMessageProperty """
        ...


class StreamUpgradeProvider(CommunicationObject): # skipped bases: <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    def CreateUpgradeAcceptor(self) -> StreamUpgradeAcceptor:
        """ CreateUpgradeAcceptor(self: StreamUpgradeProvider) -> StreamUpgradeAcceptor """
        ...

    def CreateUpgradeInitiator(self, remoteAddress:EndpointAddress, via:Uri) -> StreamUpgradeInitiator:
        """ CreateUpgradeInitiator(self: StreamUpgradeProvider, remoteAddress: EndpointAddress, via: Uri) -> StreamUpgradeInitiator """
        ...

    def GetProperty(self): # -> T
        """ GetProperty[T](self: StreamUpgradeProvider) -> T """
        ...


class StreamSecurityUpgradeProvider(StreamUpgradeProvider): # skipped bases: <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    @property
    def Identity(self) -> EndpointIdentity:
        """ Get: Identity(self: StreamSecurityUpgradeProvider) -> EndpointIdentity """
        ...



class SupportedAddressingMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SupportedAddressingMode, values: Anonymous (0), Mixed (2), NonAnonymous (1) """
    Anonymous: SupportedAddressingMode = ...
    Mixed: SupportedAddressingMode = ...
    NonAnonymous: SupportedAddressingMode = ...
    value__ = ...


class SymmetricSecurityBindingElement(SecurityBindingElement, IPolicyExportExtension): # skipped bases: <type 'object'>
    """
    SymmetricSecurityBindingElement()
    SymmetricSecurityBindingElement(protectionTokenParameters: SecurityTokenParameters)
    """
    @property
    def MessageProtectionOrder(self) -> MessageProtectionOrder:
        """
        Get: MessageProtectionOrder(self: SymmetricSecurityBindingElement) -> MessageProtectionOrder
        Set: MessageProtectionOrder(self: SymmetricSecurityBindingElement) = value
        """
        ...

    @property
    def ProtectionTokenParameters(self) -> SecurityTokenParameters:
        """
        Get: ProtectionTokenParameters(self: SymmetricSecurityBindingElement) -> SecurityTokenParameters
        Set: ProtectionTokenParameters(self: SymmetricSecurityBindingElement) = value
        """
        ...

    @property
    def RequireSignatureConfirmation(self) -> bool:
        """
        Get: RequireSignatureConfirmation(self: SymmetricSecurityBindingElement) -> bool
        Set: RequireSignatureConfirmation(self: SymmetricSecurityBindingElement) = value
        """
        ...


    def Clone(self) -> BindingElement:
        """ Clone(self: SymmetricSecurityBindingElement) -> BindingElement """
        ...

    def __new__(cls, protectionTokenParameters:SecurityTokenParameters = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, protectionTokenParameters: SecurityTokenParameters)
        """
        ...


class TcpConnectionPoolSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def GroupName(self) -> str:
        """
        Get: GroupName(self: TcpConnectionPoolSettings) -> str
        Set: GroupName(self: TcpConnectionPoolSettings) = value
        """
        ...

    @property
    def IdleTimeout(self) -> TimeSpan:
        """
        Get: IdleTimeout(self: TcpConnectionPoolSettings) -> TimeSpan
        Set: IdleTimeout(self: TcpConnectionPoolSettings) = value
        """
        ...

    @property
    def LeaseTimeout(self) -> TimeSpan:
        """
        Get: LeaseTimeout(self: TcpConnectionPoolSettings) -> TimeSpan
        Set: LeaseTimeout(self: TcpConnectionPoolSettings) = value
        """
        ...

    @property
    def MaxOutboundConnectionsPerEndpoint(self) -> int:
        """
        Get: MaxOutboundConnectionsPerEndpoint(self: TcpConnectionPoolSettings) -> int
        Set: MaxOutboundConnectionsPerEndpoint(self: TcpConnectionPoolSettings) = value
        """
        ...



class TcpTransportBindingElement(ConnectionOrientedTransportBindingElement): # skipped bases: <type 'IPolicyExportExtension'>, <type 'ITransportPolicyImport'>, <type 'IWsdlExportExtension'>, <type 'object'>
    """ TcpTransportBindingElement() """
    @property
    def ConnectionPoolSettings(self) -> TcpConnectionPoolSettings:
        """ Get: ConnectionPoolSettings(self: TcpTransportBindingElement) -> TcpConnectionPoolSettings """
        ...

    @property
    def ExtendedProtectionPolicy(self) -> ExtendedProtectionPolicy:
        """
        Get: ExtendedProtectionPolicy(self: TcpTransportBindingElement) -> ExtendedProtectionPolicy
        Set: ExtendedProtectionPolicy(self: TcpTransportBindingElement) = value
        """
        ...

    @property
    def ListenBacklog(self) -> int:
        """
        Get: ListenBacklog(self: TcpTransportBindingElement) -> int
        Set: ListenBacklog(self: TcpTransportBindingElement) = value
        """
        ...

    @property
    def PortSharingEnabled(self) -> bool:
        """
        Get: PortSharingEnabled(self: TcpTransportBindingElement) -> bool
        Set: PortSharingEnabled(self: TcpTransportBindingElement) = value
        """
        ...

    @property
    def Scheme(self) -> str:
        """ Get: Scheme(self: TcpTransportBindingElement) -> str """
        ...

    @property
    def TeredoEnabled(self) -> bool:
        """
        Get: TeredoEnabled(self: TcpTransportBindingElement) -> bool
        Set: TeredoEnabled(self: TcpTransportBindingElement) = value
        """
        ...


    def BuildChannelFactory(self, context:BindingContext) -> IChannelFactory:
        """ BuildChannelFactory[TChannel](self: TcpTransportBindingElement, context: BindingContext) -> IChannelFactory[TChannel] """
        ...

    def BuildChannelListener(self, context:BindingContext) -> IChannelListener:
        """ BuildChannelListener[TChannel](self: TcpTransportBindingElement, context: BindingContext) -> IChannelListener[TChannel] """
        ...

    def Clone(self) -> BindingElement:
        """ Clone(self: TcpTransportBindingElement) -> BindingElement """
        ...

    def ShouldSerializeExtendedProtectionPolicy(self) -> bool:
        """ ShouldSerializeExtendedProtectionPolicy(self: TcpTransportBindingElement) -> bool """
        ...

    def ShouldSerializeListenBacklog(self) -> bool:
        """ ShouldSerializeListenBacklog(self: TcpTransportBindingElement) -> bool """
        ...

    def __new__(cls) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, elementToBeCloned: TcpTransportBindingElement)
        """
        ...


class TextMessageEncodingBindingElement(IPolicyExportExtension, MessageEncodingBindingElement, IWsdlExportExtension): # skipped bases: <type 'object'>
    """
    TextMessageEncodingBindingElement()
    TextMessageEncodingBindingElement(messageVersion: MessageVersion, writeEncoding: Encoding)
    """
    @property
    def MaxReadPoolSize(self) -> int:
        """
        Get: MaxReadPoolSize(self: TextMessageEncodingBindingElement) -> int
        Set: MaxReadPoolSize(self: TextMessageEncodingBindingElement) = value
        """
        ...

    @property
    def MaxWritePoolSize(self) -> int:
        """
        Get: MaxWritePoolSize(self: TextMessageEncodingBindingElement) -> int
        Set: MaxWritePoolSize(self: TextMessageEncodingBindingElement) = value
        """
        ...

    @property
    def ReaderQuotas(self) -> XmlDictionaryReaderQuotas:
        """
        Get: ReaderQuotas(self: TextMessageEncodingBindingElement) -> XmlDictionaryReaderQuotas
        Set: ReaderQuotas(self: TextMessageEncodingBindingElement) = value
        """
        ...

    @property
    def WriteEncoding(self) -> Encoding:
        """
        Get: WriteEncoding(self: TextMessageEncodingBindingElement) -> Encoding
        Set: WriteEncoding(self: TextMessageEncodingBindingElement) = value
        """
        ...


    def BuildChannelFactory(self, context:BindingContext) -> IChannelFactory:
        """ BuildChannelFactory[TChannel](self: TextMessageEncodingBindingElement, context: BindingContext) -> IChannelFactory[TChannel] """
        ...

    def BuildChannelListener(self, context:BindingContext) -> IChannelListener:
        """ BuildChannelListener[TChannel](self: TextMessageEncodingBindingElement, context: BindingContext) -> IChannelListener[TChannel] """
        ...

    def CanBuildChannelListener(self, context:BindingContext) -> bool:
        """ CanBuildChannelListener[TChannel](self: TextMessageEncodingBindingElement, context: BindingContext) -> bool """
        ...

    def Clone(self) -> BindingElement:
        """ Clone(self: TextMessageEncodingBindingElement) -> BindingElement """
        ...

    def ShouldSerializeReaderQuotas(self) -> bool:
        """ ShouldSerializeReaderQuotas(self: TextMessageEncodingBindingElement) -> bool """
        ...

    def ShouldSerializeWriteEncoding(self) -> bool:
        """ ShouldSerializeWriteEncoding(self: TextMessageEncodingBindingElement) -> bool """
        ...


class TransactionFlowBindingElement(IPolicyExportExtension, BindingElement): # skipped bases: <type 'object'>
    """
    TransactionFlowBindingElement()
    TransactionFlowBindingElement(transactionProtocol: TransactionProtocol)
    """
    @property
    def AllowWildcardAction(self) -> bool:
        """
        Get: AllowWildcardAction(self: TransactionFlowBindingElement) -> bool
        Set: AllowWildcardAction(self: TransactionFlowBindingElement) = value
        """
        ...

    @property
    def TransactionProtocol(self) -> TransactionProtocol:
        """
        Get: TransactionProtocol(self: TransactionFlowBindingElement) -> TransactionProtocol
        Set: TransactionProtocol(self: TransactionFlowBindingElement) = value
        """
        ...


    def ShouldSerializeTransactionProtocol(self) -> bool:
        """ ShouldSerializeTransactionProtocol(self: TransactionFlowBindingElement) -> bool """
        ...


class TransactionFlowBindingElementImporter(IPolicyImportExtension): # skipped bases: <type 'object'>
    """ TransactionFlowBindingElementImporter() """
    pass

class TransactionMessageProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Transaction(self) -> Transaction:
        """ Get: Transaction(self: TransactionMessageProperty) -> Transaction """
        ...


    @staticmethod
    def Set(transaction:Transaction, message:Message): # -> 
        """ Set(transaction: Transaction, message: Message) """
        ...


class TransferSession(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TransferSession, values: None (0), Ordered (1), Unordered (2) """
    Ordered: TransferSession = ...
    Unordered: TransferSession = ...
    value__ = ...


class TransportBindingElementImporter(IPolicyImportExtension, IWsdlImportExtension): # skipped bases: <type 'object'>
    """ TransportBindingElementImporter() """
    pass

class TransportSecurityBindingElement(SecurityBindingElement, IPolicyExportExtension): # skipped bases: <type 'object'>
    """ TransportSecurityBindingElement() """
    def Clone(self) -> BindingElement:
        """ Clone(self: TransportSecurityBindingElement) -> BindingElement """
        ...


class UdpRetransmissionSettings: # skipped bases: <type 'object'>, <type 'object'>
    """
    UdpRetransmissionSettings()
    UdpRetransmissionSettings(maxUnicastRetransmitCount: int, maxMulticastRetransmitCount: int)
    UdpRetransmissionSettings(maxUnicastRetransmitCount: int, maxMulticastRetransmitCount: int, delayLowerBound: TimeSpan, delayUpperBound: TimeSpan, maxDelayPerRetransmission: TimeSpan)
    """
    @property
    def DelayLowerBound(self) -> TimeSpan:
        """
        Get: DelayLowerBound(self: UdpRetransmissionSettings) -> TimeSpan
        Set: DelayLowerBound(self: UdpRetransmissionSettings) = value
        """
        ...

    @property
    def DelayUpperBound(self) -> TimeSpan:
        """
        Get: DelayUpperBound(self: UdpRetransmissionSettings) -> TimeSpan
        Set: DelayUpperBound(self: UdpRetransmissionSettings) = value
        """
        ...

    @property
    def MaxDelayPerRetransmission(self) -> TimeSpan:
        """
        Get: MaxDelayPerRetransmission(self: UdpRetransmissionSettings) -> TimeSpan
        Set: MaxDelayPerRetransmission(self: UdpRetransmissionSettings) = value
        """
        ...

    @property
    def MaxMulticastRetransmitCount(self) -> int:
        """
        Get: MaxMulticastRetransmitCount(self: UdpRetransmissionSettings) -> int
        Set: MaxMulticastRetransmitCount(self: UdpRetransmissionSettings) = value
        """
        ...

    @property
    def MaxUnicastRetransmitCount(self) -> int:
        """
        Get: MaxUnicastRetransmitCount(self: UdpRetransmissionSettings) -> int
        Set: MaxUnicastRetransmitCount(self: UdpRetransmissionSettings) = value
        """
        ...


    def ShouldSerializeDelayLowerBound(self) -> bool:
        """ ShouldSerializeDelayLowerBound(self: UdpRetransmissionSettings) -> bool """
        ...

    def ShouldSerializeDelayUpperBound(self) -> bool:
        """ ShouldSerializeDelayUpperBound(self: UdpRetransmissionSettings) -> bool """
        ...

    def ShouldSerializeMaxDelayPerRetransmission(self) -> bool:
        """ ShouldSerializeMaxDelayPerRetransmission(self: UdpRetransmissionSettings) -> bool """
        ...


class UdpTransportBindingElement(TransportBindingElement, IPolicyExportExtension, ITransportPolicyImport, IWsdlExportExtension): # skipped bases: <type 'object'>
    """ UdpTransportBindingElement() """
    @property
    def DuplicateMessageHistoryLength(self) -> int:
        """
        Get: DuplicateMessageHistoryLength(self: UdpTransportBindingElement) -> int
        Set: DuplicateMessageHistoryLength(self: UdpTransportBindingElement) = value
        """
        ...

    @property
    def MaxPendingMessagesTotalSize(self) -> Int64:
        """
        Get: MaxPendingMessagesTotalSize(self: UdpTransportBindingElement) -> Int64
        Set: MaxPendingMessagesTotalSize(self: UdpTransportBindingElement) = value
        """
        ...

    @property
    def MulticastInterfaceId(self) -> str:
        """
        Get: MulticastInterfaceId(self: UdpTransportBindingElement) -> str
        Set: MulticastInterfaceId(self: UdpTransportBindingElement) = value
        """
        ...

    @property
    def RetransmissionSettings(self) -> UdpRetransmissionSettings:
        """
        Get: RetransmissionSettings(self: UdpTransportBindingElement) -> UdpRetransmissionSettings
        Set: RetransmissionSettings(self: UdpTransportBindingElement) = value
        """
        ...

    @property
    def SocketReceiveBufferSize(self) -> int:
        """
        Get: SocketReceiveBufferSize(self: UdpTransportBindingElement) -> int
        Set: SocketReceiveBufferSize(self: UdpTransportBindingElement) = value
        """
        ...

    @property
    def TimeToLive(self) -> int:
        """
        Get: TimeToLive(self: UdpTransportBindingElement) -> int
        Set: TimeToLive(self: UdpTransportBindingElement) = value
        """
        ...


    def BuildChannelFactory(self, context:BindingContext) -> IChannelFactory:
        """ BuildChannelFactory[TChannel](self: UdpTransportBindingElement, context: BindingContext) -> IChannelFactory[TChannel] """
        ...

    def BuildChannelListener(self, context:BindingContext) -> IChannelListener:
        """ BuildChannelListener[TChannel](self: UdpTransportBindingElement, context: BindingContext) -> IChannelListener[TChannel] """
        ...

    def CanBuildChannelFactory(self, context:BindingContext) -> bool:
        """ CanBuildChannelFactory[TChannel](self: UdpTransportBindingElement, context: BindingContext) -> bool """
        ...

    def CanBuildChannelListener(self, context:BindingContext) -> bool:
        """ CanBuildChannelListener[TChannel](self: UdpTransportBindingElement, context: BindingContext) -> bool """
        ...

    def Clone(self) -> BindingElement:
        """ Clone(self: UdpTransportBindingElement) -> BindingElement """
        ...

    def ShouldSerializeRetransmissionSettings(self) -> bool:
        """ ShouldSerializeRetransmissionSettings(self: UdpTransportBindingElement) -> bool """
        ...


class UdpTransportImporter(IPolicyImportExtension, IWsdlImportExtension): # skipped bases: <type 'object'>
    """ UdpTransportImporter() """
    pass

class UnderstoodHeaders(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Add(self, headerInfo:MessageHeaderInfo): # -> 
        """ Add(self: UnderstoodHeaders, headerInfo: MessageHeaderInfo) """
        ...

    def Contains(self, headerInfo:MessageHeaderInfo) -> bool:
        """ Contains(self: UnderstoodHeaders, headerInfo: MessageHeaderInfo) -> bool """
        ...

    def Remove(self, headerInfo:MessageHeaderInfo): # -> 
        """ Remove(self: UnderstoodHeaders, headerInfo: MessageHeaderInfo) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MessageHeaderInfo](enumerable: IEnumerable[MessageHeaderInfo], value: MessageHeaderInfo) -> bool """
        ...


class UseManagedPresentationBindingElement(IPolicyExportExtension, BindingElement): # skipped bases: <type 'object'>
    """ UseManagedPresentationBindingElement() """
    pass

class UseManagedPresentationBindingElementImporter(IPolicyImportExtension): # skipped bases: <type 'object'>
    """ UseManagedPresentationBindingElementImporter() """
    pass

class WebBodyFormatMessageProperty(IMessageProperty): # skipped bases: <type 'object'>
    """ WebBodyFormatMessageProperty(format: WebContentFormat) """
    @property
    def Format(self) -> WebContentFormat:
        """ Get: Format(self: WebBodyFormatMessageProperty) -> WebContentFormat """
        ...


    def ToString(self) -> str:
        """ ToString(self: WebBodyFormatMessageProperty) -> str """
        ...

    Name: str = ...


class WebContentFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WebContentFormat, values: Default (0), Json (2), Raw (3), Xml (1) """
    Default: WebContentFormat = ...
    Json: WebContentFormat = ...
    Raw: WebContentFormat = ...
    value__ = ...
    Xml: WebContentFormat = ...


class WebContentTypeMapper: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetMessageFormatForContentType(self, contentType:str) -> WebContentFormat:
        """ GetMessageFormatForContentType(self: WebContentTypeMapper, contentType: str) -> WebContentFormat """
        ...


class WebMessageEncodingBindingElement(IWmiInstanceProvider, MessageEncodingBindingElement, IWsdlExportExtension): # skipped bases: <type 'object'>
    """
    WebMessageEncodingBindingElement()
    WebMessageEncodingBindingElement(writeEncoding: Encoding)
    """
    @property
    def ContentTypeMapper(self) -> WebContentTypeMapper:
        """
        Get: ContentTypeMapper(self: WebMessageEncodingBindingElement) -> WebContentTypeMapper
        Set: ContentTypeMapper(self: WebMessageEncodingBindingElement) = value
        """
        ...

    @property
    def CrossDomainScriptAccessEnabled(self) -> bool:
        """
        Get: CrossDomainScriptAccessEnabled(self: WebMessageEncodingBindingElement) -> bool
        Set: CrossDomainScriptAccessEnabled(self: WebMessageEncodingBindingElement) = value
        """
        ...

    @property
    def MaxReadPoolSize(self) -> int:
        """
        Get: MaxReadPoolSize(self: WebMessageEncodingBindingElement) -> int
        Set: MaxReadPoolSize(self: WebMessageEncodingBindingElement) = value
        """
        ...

    @property
    def MaxWritePoolSize(self) -> int:
        """
        Get: MaxWritePoolSize(self: WebMessageEncodingBindingElement) -> int
        Set: MaxWritePoolSize(self: WebMessageEncodingBindingElement) = value
        """
        ...

    @property
    def ReaderQuotas(self) -> XmlDictionaryReaderQuotas:
        """ Get: ReaderQuotas(self: WebMessageEncodingBindingElement) -> XmlDictionaryReaderQuotas """
        ...

    @property
    def WriteEncoding(self) -> Encoding:
        """
        Get: WriteEncoding(self: WebMessageEncodingBindingElement) -> Encoding
        Set: WriteEncoding(self: WebMessageEncodingBindingElement) = value
        """
        ...


    def BuildChannelFactory(self, context:BindingContext) -> IChannelFactory:
        """ BuildChannelFactory[TChannel](self: WebMessageEncodingBindingElement, context: BindingContext) -> IChannelFactory[TChannel] """
        ...

    def BuildChannelListener(self, context:BindingContext) -> IChannelListener:
        """ BuildChannelListener[TChannel](self: WebMessageEncodingBindingElement, context: BindingContext) -> IChannelListener[TChannel] """
        ...

    def CanBuildChannelListener(self, context:BindingContext) -> bool:
        """ CanBuildChannelListener[TChannel](self: WebMessageEncodingBindingElement, context: BindingContext) -> bool """
        ...

    def Clone(self) -> BindingElement:
        """ Clone(self: WebMessageEncodingBindingElement) -> BindingElement """
        ...


class WebSocketMessageProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ WebSocketMessageProperty() """
    @property
    def MessageType(self) -> WebSocketMessageType:
        """
        Get: MessageType(self: WebSocketMessageProperty) -> WebSocketMessageType
        Set: MessageType(self: WebSocketMessageProperty) = value
        """
        ...

    @property
    def OpeningHandshakeProperties(self) -> ReadOnlyDictionary:
        """ Get: OpeningHandshakeProperties(self: WebSocketMessageProperty) -> ReadOnlyDictionary[str, object] """
        ...

    @property
    def SubProtocol(self) -> str:
        """ Get: SubProtocol(self: WebSocketMessageProperty) -> str """
        ...

    @property
    def WebSocketContext(self) -> WebSocketContext:
        """ Get: WebSocketContext(self: WebSocketMessageProperty) -> WebSocketContext """
        ...


    Name: str = ...


class WebSocketTransportSettings(IEquatable): # skipped bases: <type 'object'>
    """ WebSocketTransportSettings() """
    @property
    def CreateNotificationOnConnection(self) -> bool:
        """
        Get: CreateNotificationOnConnection(self: WebSocketTransportSettings) -> bool
        Set: CreateNotificationOnConnection(self: WebSocketTransportSettings) = value
        """
        ...

    @property
    def DisablePayloadMasking(self) -> bool:
        """
        Get: DisablePayloadMasking(self: WebSocketTransportSettings) -> bool
        Set: DisablePayloadMasking(self: WebSocketTransportSettings) = value
        """
        ...

    @property
    def KeepAliveInterval(self) -> TimeSpan:
        """
        Get: KeepAliveInterval(self: WebSocketTransportSettings) -> TimeSpan
        Set: KeepAliveInterval(self: WebSocketTransportSettings) = value
        """
        ...

    @property
    def MaxPendingConnections(self) -> int:
        """
        Get: MaxPendingConnections(self: WebSocketTransportSettings) -> int
        Set: MaxPendingConnections(self: WebSocketTransportSettings) = value
        """
        ...

    @property
    def SubProtocol(self) -> str:
        """
        Get: SubProtocol(self: WebSocketTransportSettings) -> str
        Set: SubProtocol(self: WebSocketTransportSettings) = value
        """
        ...

    @property
    def TransportUsage(self): # -> WebSocketTransportUsage
        """
        Get: TransportUsage(self: WebSocketTransportSettings) -> WebSocketTransportUsage
        Set: TransportUsage(self: WebSocketTransportSettings) = value
        """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: WebSocketTransportSettings) -> int """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    BinaryEncoderTransferModeHeader: str = ...
    BinaryMessageReceivedAction: str = ...
    ConnectionOpenedAction: str = ...
    SoapContentTypeHeader: str = ...
    TextMessageReceivedAction: str = ...


class WebSocketTransportUsage(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WebSocketTransportUsage, values: Always (1), Never (2), WhenDuplex (0) """
    Always: WebSocketTransportUsage = ...
    Never: WebSocketTransportUsage = ...
    value__ = ...
    WhenDuplex: WebSocketTransportUsage = ...


class WindowsStreamSecurityBindingElement(ITransportTokenAssertionProvider, IPolicyExportExtension, StreamUpgradeBindingElement): # skipped bases: <type 'object'>
    """ WindowsStreamSecurityBindingElement() """
    @property
    def ProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ProtectionLevel(self: WindowsStreamSecurityBindingElement) -> ProtectionLevel
        Set: ProtectionLevel(self: WindowsStreamSecurityBindingElement) = value
        """
        ...


    def BuildChannelFactory(self, context:BindingContext) -> IChannelFactory:
        """ BuildChannelFactory[TChannel](self: WindowsStreamSecurityBindingElement, context: BindingContext) -> IChannelFactory[TChannel] """
        ...

    def BuildChannelListener(self, context:BindingContext) -> IChannelListener:
        """ BuildChannelListener[TChannel](self: WindowsStreamSecurityBindingElement, context: BindingContext) -> IChannelListener[TChannel] """
        ...

    def CanBuildChannelFactory(self, context:BindingContext) -> bool:
        """ CanBuildChannelFactory[TChannel](self: WindowsStreamSecurityBindingElement, context: BindingContext) -> bool """
        ...

    def CanBuildChannelListener(self, context:BindingContext) -> bool:
        """ CanBuildChannelListener[TChannel](self: WindowsStreamSecurityBindingElement, context: BindingContext) -> bool """
        ...

    def Clone(self) -> BindingElement:
        """ Clone(self: WindowsStreamSecurityBindingElement) -> BindingElement """
        ...

    def GetProperty(self, context:BindingContext): # -> T
        """ GetProperty[T](self: WindowsStreamSecurityBindingElement, context: BindingContext) -> T """
        ...


class WrappedOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ WrappedOptions() """
    @property
    def WrappedFlag(self) -> bool:
        """
        Get: WrappedFlag(self: WrappedOptions) -> bool
        Set: WrappedFlag(self: WrappedOptions) = value
        """
        ...



class XmlSerializerImportOptions: # skipped bases: <type 'object'>, <type 'object'>
    """
    XmlSerializerImportOptions()
    XmlSerializerImportOptions(codeCompileUnit: CodeCompileUnit)
    """
    @property
    def ClrNamespace(self) -> str:
        """
        Get: ClrNamespace(self: XmlSerializerImportOptions) -> str
        Set: ClrNamespace(self: XmlSerializerImportOptions) = value
        """
        ...

    @property
    def CodeCompileUnit(self) -> CodeCompileUnit:
        """ Get: CodeCompileUnit(self: XmlSerializerImportOptions) -> CodeCompileUnit """
        ...

    @property
    def CodeProvider(self) -> CodeDomProvider:
        """
        Get: CodeProvider(self: XmlSerializerImportOptions) -> CodeDomProvider
        Set: CodeProvider(self: XmlSerializerImportOptions) = value
        """
        ...

    @property
    def WebReferenceOptions(self) -> WebReferenceOptions:
        """
        Get: WebReferenceOptions(self: XmlSerializerImportOptions) -> WebReferenceOptions
        Set: WebReferenceOptions(self: XmlSerializerImportOptions) = value
        """
        ...



