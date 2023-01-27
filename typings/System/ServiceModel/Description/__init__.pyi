# encoding: utf-8
# module System.ServiceModel.Description calls itself Description
# from System.WorkflowServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.ServiceModel.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.ServiceModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.JScript import Binding

from System import (Array, AsyncCallback, Attribute, DateTimeOffset, Enum, 
    IAsyncResult, Int64, TimeSpan, Type, Uri)

from System.CodeDom import (CodeCompileUnit, CodeMemberMethod, 
    CodeTypeDeclaration, CodeTypeReference)

from System.Collections import ICollection, IDictionary, IEnumerable, IList

from System.Collections.Generic import Dictionary, KeyedByTypeCollection

from System.Collections.ObjectModel import (Collection, KeyedCollection, 
    ReadOnlyCollection)

from System.Configuration import Configuration

from System.IdentityModel.Configuration import IdentityConfiguration

from System.IdentityModel.Tokens import (
    SecurityTokenHandlerCollectionManager)

from System.Messaging import Message

from System.Net import AuthenticationSchemes, ICredentials

from System.Net.Security import ProtectionLevel

from System.Reflection import MemberInfo, MethodInfo

from System.ServiceModel import (AuditLevel, AuditLogLocation, 
    DataContractFormatAttribute, EndpointAddress, ExceptionDetail, 
    ExceptionMapper, HostNameComparisonMode, IExtension, 
    ServiceAuthenticationManager, ServiceAuthorizationManager, 
    ServiceHostBase, SessionMode, TransferMode, WebHttpSecurity, 
    XmlSerializerFormatAttribute)

from System.ServiceModel.Channels import WebContentTypeMapper

from System.ServiceModel.Configuration import ChannelEndpointElement

from System.ServiceModel.Dispatcher import (ClientOperation, ClientRuntime, 
    DispatchOperation, DispatchRuntime, EndpointDispatcher)

from System.ServiceModel.Persistence import PersistenceProviderFactory

from System.ServiceModel.Security import (HttpDigestClientCredential, 
    IssuedTokenClientCredential, IssuedTokenServiceCredential, PeerCredential, 
    SecureConversationServiceCredential, SecurityCredentialsManager, 
    UserNamePasswordClientCredential, UserNamePasswordServiceCredential, 
    WindowsClientCredential, WindowsServiceCredential, 
    X509CertificateInitiatorClientCredential, 
    X509CertificateInitiatorServiceCredential, 
    X509CertificateRecipientClientCredential, 
    X509CertificateRecipientServiceCredential)

from System.ServiceModel.Web import WebMessageBodyStyle, WebMessageFormat

from System.Text import Encoding

from System.Threading.Tasks import Task

from System.Web.Security import RoleProvider

from System.Web.Services.Description import (FaultBinding, MessageBinding, 
    Operation, OperationBinding, OperationFault, OperationMessage, Port, 
    PortType, ServiceDescription, ServiceDescriptionCollection)

from System.Workflow.Runtime import WorkflowRuntime

from System.Xml import (XmlDictionaryReaderQuotas, XmlElement, 
    XmlNamespaceManager, XmlQualifiedName, XmlReader, XmlWriter)

from System.Xml.Linq import XName

from System.Xml.Schema import XmlSchema, XmlSchemaSet

from System.Xml.Serialization import IXmlSerializable

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (AddressingVersion, 
    BindingElementCollection, BindingParameterCollection, 
    DataContractResolver, IContextSessionProvider, IDataContractSurrogate, 
    IWmiInstanceProvider, MessageDirection, 
    MessageHeaderDescriptionCollection, MessagePartDescription, 
    MessagePartDescriptionCollection, MessagePropertyDescriptionCollection, 
    MessageVersion, MetadataExchangeClientMode, MetadataExporter, 
    MetadataImporter, MetadataSet, OperationContractGenerationContext, 
    OperationDescription, OperationDescriptionCollection, 
    PolicyConversionContext, PolicyVersion, ProcessInformationModel, 
    ProcessThreadsModel, ServiceContractGenerationContext, 
    ServiceContractGenerator, ServiceEndpoint, ServiceEndpointCollection, 
    ServicePropertiesModel, WsdlContractConversionContext, 
    WsdlEndpointConversionContext, WsdlExporter, WsdlImporter, 
    XmlObjectSerializer, field#)
"""

# no functions
# classes

class IEndpointBehavior: # skipped bases: <type 'object'>
    """ no doc """
    def AddBindingParameters(self, endpoint, bindingParameters): # ->  # Not found arg types: {'bindingParameters': 'BindingParameterCollection', 'endpoint': 'ServiceEndpoint'}
        """ AddBindingParameters(self: IEndpointBehavior, endpoint: ServiceEndpoint, bindingParameters: BindingParameterCollection) """
        ...

    def ApplyClientBehavior(self, endpoint, clientRuntime:ClientRuntime): # ->  # Not found arg types: {'endpoint': 'ServiceEndpoint'}
        """ ApplyClientBehavior(self: IEndpointBehavior, endpoint: ServiceEndpoint, clientRuntime: ClientRuntime) """
        ...

    def ApplyDispatchBehavior(self, endpoint, endpointDispatcher:EndpointDispatcher): # ->  # Not found arg types: {'endpoint': 'ServiceEndpoint'}
        """ ApplyDispatchBehavior(self: IEndpointBehavior, endpoint: ServiceEndpoint, endpointDispatcher: EndpointDispatcher) """
        ...

    def Validate(self, endpoint): # ->  # Not found arg types: {'endpoint': 'ServiceEndpoint'}
        """ Validate(self: IEndpointBehavior, endpoint: ServiceEndpoint) """
        ...


class CallbackDebugBehavior(IEndpointBehavior): # skipped bases: <type 'object'>
    """ CallbackDebugBehavior(includeExceptionDetailInFaults: bool) """
    @property
    def IncludeExceptionDetailInFaults(self) -> bool:
        """
        Get: IncludeExceptionDetailInFaults(self: CallbackDebugBehavior) -> bool
        Set: IncludeExceptionDetailInFaults(self: CallbackDebugBehavior) = value
        """
        ...



class ClientCredentials(SecurityCredentialsManager, IEndpointBehavior): # skipped bases: <type 'object'>
    """ ClientCredentials() """
    @property
    def ClientCertificate(self) -> X509CertificateInitiatorClientCredential:
        """ Get: ClientCertificate(self: ClientCredentials) -> X509CertificateInitiatorClientCredential """
        ...

    @property
    def HttpDigest(self) -> HttpDigestClientCredential:
        """ Get: HttpDigest(self: ClientCredentials) -> HttpDigestClientCredential """
        ...

    @property
    def IssuedToken(self) -> IssuedTokenClientCredential:
        """ Get: IssuedToken(self: ClientCredentials) -> IssuedTokenClientCredential """
        ...

    @property
    def Peer(self) -> PeerCredential:
        """ Get: Peer(self: ClientCredentials) -> PeerCredential """
        ...

    @property
    def SecurityTokenHandlerCollectionManager(self) -> SecurityTokenHandlerCollectionManager:
        """
        Get: SecurityTokenHandlerCollectionManager(self: ClientCredentials) -> SecurityTokenHandlerCollectionManager
        Set: SecurityTokenHandlerCollectionManager(self: ClientCredentials) = value
        """
        ...

    @property
    def ServiceCertificate(self) -> X509CertificateRecipientClientCredential:
        """ Get: ServiceCertificate(self: ClientCredentials) -> X509CertificateRecipientClientCredential """
        ...

    @property
    def SupportInteractive(self) -> bool:
        """
        Get: SupportInteractive(self: ClientCredentials) -> bool
        Set: SupportInteractive(self: ClientCredentials) = value
        """
        ...

    @property
    def UseIdentityConfiguration(self) -> bool:
        """
        Get: UseIdentityConfiguration(self: ClientCredentials) -> bool
        Set: UseIdentityConfiguration(self: ClientCredentials) = value
        """
        ...

    @property
    def UserName(self) -> UserNamePasswordClientCredential:
        """ Get: UserName(self: ClientCredentials) -> UserNamePasswordClientCredential """
        ...

    @property
    def Windows(self) -> WindowsClientCredential:
        """ Get: Windows(self: ClientCredentials) -> WindowsClientCredential """
        ...


    def Clone(self) -> ClientCredentials:
        """ Clone(self: ClientCredentials) -> ClientCredentials """
        ...

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: ClientCredentials) -> ClientCredentials """
        ...

    def GetInfoCardSecurityToken(self, *args): #cannot find CLR method
        """ GetInfoCardSecurityToken(self: ClientCredentials, requiresInfoCard: bool, chain: Array[CardSpacePolicyElement], tokenSerializer: SecurityTokenSerializer) -> SecurityToken """
        ...

    def __new__(cls) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, other: ClientCredentials)
        """
        ...


class ClientViaBehavior(IEndpointBehavior): # skipped bases: <type 'object'>
    """ ClientViaBehavior(uri: Uri) """
    @property
    def Uri(self) -> Uri:
        """
        Get: Uri(self: ClientViaBehavior) -> Uri
        Set: Uri(self: ClientViaBehavior) = value
        """
        ...



class ContractDescription: # skipped bases: <type 'object'>, <type 'object'>
    """
    ContractDescription(name: str)
    ContractDescription(name: str, ns: str)
    """
    @property
    def Behaviors(self) -> KeyedByTypeCollection:
        """ Get: Behaviors(self: ContractDescription) -> KeyedByTypeCollection[IContractBehavior] """
        ...

    @property
    def CallbackContractType(self) -> Type:
        """
        Get: CallbackContractType(self: ContractDescription) -> Type
        Set: CallbackContractType(self: ContractDescription) = value
        """
        ...

    @property
    def ConfigurationName(self) -> str:
        """
        Get: ConfigurationName(self: ContractDescription) -> str
        Set: ConfigurationName(self: ContractDescription) = value
        """
        ...

    @property
    def ContractBehaviors(self) -> KeyedCollection:
        """ Get: ContractBehaviors(self: ContractDescription) -> KeyedCollection[Type, IContractBehavior] """
        ...

    @property
    def ContractType(self) -> Type:
        """
        Get: ContractType(self: ContractDescription) -> Type
        Set: ContractType(self: ContractDescription) = value
        """
        ...

    @property
    def HasProtectionLevel(self) -> bool:
        """ Get: HasProtectionLevel(self: ContractDescription) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ContractDescription) -> str
        Set: Name(self: ContractDescription) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: ContractDescription) -> str
        Set: Namespace(self: ContractDescription) = value
        """
        ...

    @property
    def Operations(self): # -> OperationDescriptionCollection
        """ Get: Operations(self: ContractDescription) -> OperationDescriptionCollection """
        ...

    @property
    def ProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ProtectionLevel(self: ContractDescription) -> ProtectionLevel
        Set: ProtectionLevel(self: ContractDescription) = value
        """
        ...

    @property
    def SessionMode(self) -> SessionMode:
        """
        Get: SessionMode(self: ContractDescription) -> SessionMode
        Set: SessionMode(self: ContractDescription) = value
        """
        ...


    @staticmethod
    def GetContract(contractType:Type, *__args:object) -> ContractDescription:
        """
        GetContract(contractType: Type) -> ContractDescription
        GetContract(contractType: Type, serviceImplementation: object) -> ContractDescription
        GetContract(contractType: Type, serviceType: Type) -> ContractDescription
        """
        ...

    def GetInheritedContracts(self) -> Collection:
        """ GetInheritedContracts(self: ContractDescription) -> Collection[ContractDescription] """
        ...

    def ShouldSerializeProtectionLevel(self) -> bool:
        """ ShouldSerializeProtectionLevel(self: ContractDescription) -> bool """
        ...


class IWsdlImportExtension: # skipped bases: <type 'object'>
    """ no doc """
    def BeforeImport(self, wsdlDocuments:ServiceDescriptionCollection, xmlSchemas:XmlSchemaSet, policy:ICollection): # -> 
        """ BeforeImport(self: IWsdlImportExtension, wsdlDocuments: ServiceDescriptionCollection, xmlSchemas: XmlSchemaSet, policy: ICollection[XmlElement]) """
        ...

    def ImportContract(self, importer, context): # ->  # Not found arg types: {'importer': 'WsdlImporter', 'context': 'WsdlContractConversionContext'}
        """ ImportContract(self: IWsdlImportExtension, importer: WsdlImporter, context: WsdlContractConversionContext) """
        ...

    def ImportEndpoint(self, importer, context): # ->  # Not found arg types: {'importer': 'WsdlImporter', 'context': 'WsdlEndpointConversionContext'}
        """ ImportEndpoint(self: IWsdlImportExtension, importer: WsdlImporter, context: WsdlEndpointConversionContext) """
        ...


class DataContractSerializerMessageContractImporter(IWsdlImportExtension): # skipped bases: <type 'object'>
    """ DataContractSerializerMessageContractImporter() """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: DataContractSerializerMessageContractImporter) -> bool
        Set: Enabled(self: DataContractSerializerMessageContractImporter) = value
        """
        ...



class IOperationBehavior: # skipped bases: <type 'object'>
    """ no doc """
    def AddBindingParameters(self, operationDescription, bindingParameters): # ->  # Not found arg types: {'bindingParameters': 'BindingParameterCollection', 'operationDescription': 'OperationDescription'}
        """ AddBindingParameters(self: IOperationBehavior, operationDescription: OperationDescription, bindingParameters: BindingParameterCollection) """
        ...

    def ApplyClientBehavior(self, operationDescription, clientOperation:ClientOperation): # ->  # Not found arg types: {'operationDescription': 'OperationDescription'}
        """ ApplyClientBehavior(self: IOperationBehavior, operationDescription: OperationDescription, clientOperation: ClientOperation) """
        ...

    def ApplyDispatchBehavior(self, operationDescription, dispatchOperation:DispatchOperation): # ->  # Not found arg types: {'operationDescription': 'OperationDescription'}
        """ ApplyDispatchBehavior(self: IOperationBehavior, operationDescription: OperationDescription, dispatchOperation: DispatchOperation) """
        ...

    def Validate(self, operationDescription): # ->  # Not found arg types: {'operationDescription': 'OperationDescription'}
        """ Validate(self: IOperationBehavior, operationDescription: OperationDescription) """
        ...


class IWsdlExportExtension: # skipped bases: <type 'object'>
    """ no doc """
    def ExportContract(self, exporter, context): # ->  # Not found arg types: {'exporter': 'WsdlExporter', 'context': 'WsdlContractConversionContext'}
        """ ExportContract(self: IWsdlExportExtension, exporter: WsdlExporter, context: WsdlContractConversionContext) """
        ...

    def ExportEndpoint(self, exporter, context): # ->  # Not found arg types: {'exporter': 'WsdlExporter', 'context': 'WsdlEndpointConversionContext'}
        """ ExportEndpoint(self: IWsdlExportExtension, exporter: WsdlExporter, context: WsdlEndpointConversionContext) """
        ...


class DataContractSerializerOperationBehavior(IOperationBehavior, IWsdlExportExtension): # skipped bases: <type 'object'>
    """
    DataContractSerializerOperationBehavior(operation: OperationDescription)
    DataContractSerializerOperationBehavior(operation: OperationDescription, dataContractFormatAttribute: DataContractFormatAttribute)
    """
    @property
    def DataContractFormatAttribute(self) -> DataContractFormatAttribute:
        """ Get: DataContractFormatAttribute(self: DataContractSerializerOperationBehavior) -> DataContractFormatAttribute """
        ...

    @property
    def DataContractResolver(self): # -> DataContractResolver
        """
        Get: DataContractResolver(self: DataContractSerializerOperationBehavior) -> DataContractResolver
        Set: DataContractResolver(self: DataContractSerializerOperationBehavior) = value
        """
        ...

    @property
    def DataContractSurrogate(self): # -> IDataContractSurrogate
        """
        Get: DataContractSurrogate(self: DataContractSerializerOperationBehavior) -> IDataContractSurrogate
        Set: DataContractSurrogate(self: DataContractSerializerOperationBehavior) = value
        """
        ...

    @property
    def IgnoreExtensionDataObject(self) -> bool:
        """
        Get: IgnoreExtensionDataObject(self: DataContractSerializerOperationBehavior) -> bool
        Set: IgnoreExtensionDataObject(self: DataContractSerializerOperationBehavior) = value
        """
        ...

    @property
    def MaxItemsInObjectGraph(self) -> int:
        """
        Get: MaxItemsInObjectGraph(self: DataContractSerializerOperationBehavior) -> int
        Set: MaxItemsInObjectGraph(self: DataContractSerializerOperationBehavior) = value
        """
        ...


    def CreateSerializer(self, type:Type, name:str, ns:str, knownTypes:IList): # -> XmlObjectSerializer
        """
        CreateSerializer(self: DataContractSerializerOperationBehavior, type: Type, name: str, ns: str, knownTypes: IList[Type]) -> XmlObjectSerializer
        CreateSerializer(self: DataContractSerializerOperationBehavior, type: Type, name: XmlDictionaryString, ns: XmlDictionaryString, knownTypes: IList[Type]) -> XmlObjectSerializer
        """
        ...


class DispatcherSynchronizationBehavior(IEndpointBehavior): # skipped bases: <type 'object'>
    """
    DispatcherSynchronizationBehavior()
    DispatcherSynchronizationBehavior(asynchronousSendEnabled: bool, maxPendingReceives: int)
    """
    @property
    def AsynchronousSendEnabled(self) -> bool:
        """
        Get: AsynchronousSendEnabled(self: DispatcherSynchronizationBehavior) -> bool
        Set: AsynchronousSendEnabled(self: DispatcherSynchronizationBehavior) = value
        """
        ...

    @property
    def MaxPendingReceives(self) -> int:
        """
        Get: MaxPendingReceives(self: DispatcherSynchronizationBehavior) -> int
        Set: MaxPendingReceives(self: DispatcherSynchronizationBehavior) = value
        """
        ...



class DurableOperationAttribute(Attribute, IWmiInstanceProvider, IOperationBehavior): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DurableOperationAttribute() """
    @property
    def CanCreateInstance(self) -> bool:
        """
        Get: CanCreateInstance(self: DurableOperationAttribute) -> bool
        Set: CanCreateInstance(self: DurableOperationAttribute) = value
        """
        ...

    @property
    def CompletesInstance(self) -> bool:
        """
        Get: CompletesInstance(self: DurableOperationAttribute) -> bool
        Set: CompletesInstance(self: DurableOperationAttribute) = value
        """
        ...



class IServiceBehavior: # skipped bases: <type 'object'>
    """ no doc """
    def AddBindingParameters(self, serviceDescription:ServiceDescription, serviceHostBase:ServiceHostBase, endpoints:Collection, bindingParameters): # ->  # Not found arg types: {'bindingParameters': 'BindingParameterCollection'}
        """ AddBindingParameters(self: IServiceBehavior, serviceDescription: ServiceDescription, serviceHostBase: ServiceHostBase, endpoints: Collection[ServiceEndpoint], bindingParameters: BindingParameterCollection) """
        ...

    def ApplyDispatchBehavior(self, serviceDescription:ServiceDescription, serviceHostBase:ServiceHostBase): # -> 
        """ ApplyDispatchBehavior(self: IServiceBehavior, serviceDescription: ServiceDescription, serviceHostBase: ServiceHostBase) """
        ...

    def Validate(self, serviceDescription:ServiceDescription, serviceHostBase:ServiceHostBase): # -> 
        """ Validate(self: IServiceBehavior, serviceDescription: ServiceDescription, serviceHostBase: ServiceHostBase) """
        ...


class DurableServiceAttribute(IContextSessionProvider, Attribute, IServiceBehavior, IWmiInstanceProvider): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DurableServiceAttribute() """
    @property
    def SaveStateInOperationTransaction(self) -> bool:
        """
        Get: SaveStateInOperationTransaction(self: DurableServiceAttribute) -> bool
        Set: SaveStateInOperationTransaction(self: DurableServiceAttribute) = value
        """
        ...

    @property
    def UnknownExceptionAction(self) -> UnknownExceptionAction:
        """
        Get: UnknownExceptionAction(self: DurableServiceAttribute) -> UnknownExceptionAction
        Set: UnknownExceptionAction(self: DurableServiceAttribute) = value
        """
        ...



class FaultDescription: # skipped bases: <type 'object'>, <type 'object'>
    """ FaultDescription(action: str) """
    @property
    def Action(self) -> str:
        """ Get: Action(self: FaultDescription) -> str """
        ...

    @property
    def DetailType(self) -> Type:
        """
        Get: DetailType(self: FaultDescription) -> Type
        Set: DetailType(self: FaultDescription) = value
        """
        ...

    @property
    def HasProtectionLevel(self) -> bool:
        """ Get: HasProtectionLevel(self: FaultDescription) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: FaultDescription) -> str
        Set: Name(self: FaultDescription) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: FaultDescription) -> str
        Set: Namespace(self: FaultDescription) = value
        """
        ...

    @property
    def ProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ProtectionLevel(self: FaultDescription) -> ProtectionLevel
        Set: ProtectionLevel(self: FaultDescription) = value
        """
        ...


    def ShouldSerializeProtectionLevel(self) -> bool:
        """ ShouldSerializeProtectionLevel(self: FaultDescription) -> bool """
        ...


class FaultDescriptionCollection(Collection): # skipped bases: <type 'IReadOnlyCollection[FaultDescription]'>, <type 'IList[FaultDescription]'>, <type 'IEnumerable'>, <type 'IEnumerable[FaultDescription]'>, <type 'IList'>, <type 'IReadOnlyList[FaultDescription]'>, <type 'ICollection[FaultDescription]'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Find(self, action:str) -> FaultDescription:
        """ Find(self: FaultDescriptionCollection, action: str) -> FaultDescription """
        ...

    def FindAll(self, action:str) -> Collection:
        """ FindAll(self: FaultDescriptionCollection, action: str) -> Collection[FaultDescription] """
        ...


class IContractBehavior: # skipped bases: <type 'object'>
    """ no doc """
    def AddBindingParameters(self, contractDescription:ContractDescription, endpoint, bindingParameters): # ->  # Not found arg types: {'bindingParameters': 'BindingParameterCollection', 'endpoint': 'ServiceEndpoint'}
        """ AddBindingParameters(self: IContractBehavior, contractDescription: ContractDescription, endpoint: ServiceEndpoint, bindingParameters: BindingParameterCollection) """
        ...

    def ApplyClientBehavior(self, contractDescription:ContractDescription, endpoint, clientRuntime:ClientRuntime): # ->  # Not found arg types: {'endpoint': 'ServiceEndpoint'}
        """ ApplyClientBehavior(self: IContractBehavior, contractDescription: ContractDescription, endpoint: ServiceEndpoint, clientRuntime: ClientRuntime) """
        ...

    def ApplyDispatchBehavior(self, contractDescription:ContractDescription, endpoint, dispatchRuntime:DispatchRuntime): # ->  # Not found arg types: {'endpoint': 'ServiceEndpoint'}
        """ ApplyDispatchBehavior(self: IContractBehavior, contractDescription: ContractDescription, endpoint: ServiceEndpoint, dispatchRuntime: DispatchRuntime) """
        ...

    def Validate(self, contractDescription:ContractDescription, endpoint): # ->  # Not found arg types: {'endpoint': 'ServiceEndpoint'}
        """ Validate(self: IContractBehavior, contractDescription: ContractDescription, endpoint: ServiceEndpoint) """
        ...


class IContractBehaviorAttribute: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def TargetContract(self) -> Type:
        """ Get: TargetContract(self: IContractBehaviorAttribute) -> Type """
        ...



class IMetadataExchange: # skipped bases: <type 'object'>
    """ no doc """
    def BeginGet(self, request:Message, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginGet(self: IMetadataExchange, request: Message, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndGet(self, result:IAsyncResult) -> Message:
        """ EndGet(self: IMetadataExchange, result: IAsyncResult) -> Message """
        ...

    def Get(self, request:Message) -> Message:
        """ Get(self: IMetadataExchange, request: Message) -> Message """
        ...


class IOperationContractGenerationExtension: # skipped bases: <type 'object'>
    """ no doc """
    def GenerateOperation(self, context): # ->  # Not found arg types: {'context': 'OperationContractGenerationContext'}
        """ GenerateOperation(self: IOperationContractGenerationExtension, context: OperationContractGenerationContext) """
        ...


class IPolicyExportExtension: # skipped bases: <type 'object'>
    """ no doc """
    def ExportPolicy(self, exporter, context): # ->  # Not found arg types: {'exporter': 'MetadataExporter', 'context': 'PolicyConversionContext'}
        """ ExportPolicy(self: IPolicyExportExtension, exporter: MetadataExporter, context: PolicyConversionContext) """
        ...


class IPolicyImportExtension: # skipped bases: <type 'object'>
    """ no doc """
    def ImportPolicy(self, importer, context): # ->  # Not found arg types: {'importer': 'MetadataImporter', 'context': 'PolicyConversionContext'}
        """ ImportPolicy(self: IPolicyImportExtension, importer: MetadataImporter, context: PolicyConversionContext) """
        ...


class IServiceContractGenerationExtension: # skipped bases: <type 'object'>
    """ no doc """
    def GenerateContract(self, context): # ->  # Not found arg types: {'context': 'ServiceContractGenerationContext'}
        """ GenerateContract(self: IServiceContractGenerationExtension, context: ServiceContractGenerationContext) """
        ...


class JsonFaultDetail: # skipped bases: <type 'object'>, <type 'object'>
    """ JsonFaultDetail() """
    @property
    def ExceptionDetail(self) -> ExceptionDetail:
        """
        Get: ExceptionDetail(self: JsonFaultDetail) -> ExceptionDetail
        Set: ExceptionDetail(self: JsonFaultDetail) = value
        """
        ...

    @property
    def ExceptionType(self) -> str:
        """
        Get: ExceptionType(self: JsonFaultDetail) -> str
        Set: ExceptionType(self: JsonFaultDetail) = value
        """
        ...

    @property
    def Message(self) -> str:
        """
        Get: Message(self: JsonFaultDetail) -> str
        Set: Message(self: JsonFaultDetail) = value
        """
        ...

    @property
    def StackTrace(self) -> str:
        """
        Get: StackTrace(self: JsonFaultDetail) -> str
        Set: StackTrace(self: JsonFaultDetail) = value
        """
        ...



class ListenUriMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ListenUriMode, values: Explicit (0), Unique (1) """
    Explicit: ListenUriMode = ...
    Unique: ListenUriMode = ...
    value__ = ...


class MessageBodyDescription: # skipped bases: <type 'object'>, <type 'object'>
    """ MessageBodyDescription() """
    @property
    def Parts(self): # -> MessagePartDescriptionCollection
        """ Get: Parts(self: MessageBodyDescription) -> MessagePartDescriptionCollection """
        ...

    @property
    def ReturnValue(self): # -> MessagePartDescription
        """
        Get: ReturnValue(self: MessageBodyDescription) -> MessagePartDescription
        Set: ReturnValue(self: MessageBodyDescription) = value
        """
        ...

    @property
    def WrapperName(self) -> str:
        """
        Get: WrapperName(self: MessageBodyDescription) -> str
        Set: WrapperName(self: MessageBodyDescription) = value
        """
        ...

    @property
    def WrapperNamespace(self) -> str:
        """
        Get: WrapperNamespace(self: MessageBodyDescription) -> str
        Set: WrapperNamespace(self: MessageBodyDescription) = value
        """
        ...



class MessageDescription: # skipped bases: <type 'object'>, <type 'object'>
    """ MessageDescription(action: str, direction: MessageDirection) """
    @property
    def Action(self) -> str:
        """ Get: Action(self: MessageDescription) -> str """
        ...

    @property
    def Body(self) -> MessageBodyDescription:
        """ Get: Body(self: MessageDescription) -> MessageBodyDescription """
        ...

    @property
    def Direction(self): # -> MessageDirection
        """ Get: Direction(self: MessageDescription) -> MessageDirection """
        ...

    @property
    def HasProtectionLevel(self) -> bool:
        """ Get: HasProtectionLevel(self: MessageDescription) -> bool """
        ...

    @property
    def Headers(self): # -> MessageHeaderDescriptionCollection
        """ Get: Headers(self: MessageDescription) -> MessageHeaderDescriptionCollection """
        ...

    @property
    def MessageType(self) -> Type:
        """
        Get: MessageType(self: MessageDescription) -> Type
        Set: MessageType(self: MessageDescription) = value
        """
        ...

    @property
    def Properties(self): # -> MessagePropertyDescriptionCollection
        """ Get: Properties(self: MessageDescription) -> MessagePropertyDescriptionCollection """
        ...

    @property
    def ProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ProtectionLevel(self: MessageDescription) -> ProtectionLevel
        Set: ProtectionLevel(self: MessageDescription) = value
        """
        ...


    def ShouldSerializeProtectionLevel(self) -> bool:
        """ ShouldSerializeProtectionLevel(self: MessageDescription) -> bool """
        ...


class MessageDescriptionCollection(Collection): # skipped bases: <type 'IReadOnlyList[MessageDescription]'>, <type 'ICollection[MessageDescription]'>, <type 'IReadOnlyCollection[MessageDescription]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IEnumerable[MessageDescription]'>, <type 'ICollection'>, <type 'IList[MessageDescription]'>, <type 'object'>
    """ no doc """
    def Find(self, action:str) -> MessageDescription:
        """ Find(self: MessageDescriptionCollection, action: str) -> MessageDescription """
        ...

    def FindAll(self, action:str) -> Collection:
        """ FindAll(self: MessageDescriptionCollection, action: str) -> Collection[MessageDescription] """
        ...


class MessageDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MessageDirection, values: Input (0), Output (1) """
    Input: MessageDirection = ...
    Output: MessageDirection = ...
    value__ = ...


class MessagePartDescription: # skipped bases: <type 'object'>, <type 'object'>
    """ MessagePartDescription(name: str, ns: str) """
    @property
    def HasProtectionLevel(self) -> bool:
        """ Get: HasProtectionLevel(self: MessagePartDescription) -> bool """
        ...

    @property
    def Index(self) -> int:
        """
        Get: Index(self: MessagePartDescription) -> int
        Set: Index(self: MessagePartDescription) = value
        """
        ...

    @property
    def MemberInfo(self) -> MemberInfo:
        """
        Get: MemberInfo(self: MessagePartDescription) -> MemberInfo
        Set: MemberInfo(self: MessagePartDescription) = value
        """
        ...

    @property
    def Multiple(self) -> bool:
        """
        Get: Multiple(self: MessagePartDescription) -> bool
        Set: Multiple(self: MessagePartDescription) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MessagePartDescription) -> str """
        ...

    @property
    def Namespace(self) -> str:
        """ Get: Namespace(self: MessagePartDescription) -> str """
        ...

    @property
    def ProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ProtectionLevel(self: MessagePartDescription) -> ProtectionLevel
        Set: ProtectionLevel(self: MessagePartDescription) = value
        """
        ...

    @property
    def Type(self) -> Type:
        """
        Get: Type(self: MessagePartDescription) -> Type
        Set: Type(self: MessagePartDescription) = value
        """
        ...



class MessageHeaderDescription(MessagePartDescription): # skipped bases: <type 'object'>
    """ MessageHeaderDescription(name: str, ns: str) """
    @property
    def Actor(self) -> str:
        """
        Get: Actor(self: MessageHeaderDescription) -> str
        Set: Actor(self: MessageHeaderDescription) = value
        """
        ...

    @property
    def MustUnderstand(self) -> bool:
        """
        Get: MustUnderstand(self: MessageHeaderDescription) -> bool
        Set: MustUnderstand(self: MessageHeaderDescription) = value
        """
        ...

    @property
    def Relay(self) -> bool:
        """
        Get: Relay(self: MessageHeaderDescription) -> bool
        Set: Relay(self: MessageHeaderDescription) = value
        """
        ...

    @property
    def TypedHeader(self) -> bool:
        """
        Get: TypedHeader(self: MessageHeaderDescription) -> bool
        Set: TypedHeader(self: MessageHeaderDescription) = value
        """
        ...



class MessageHeaderDescriptionCollection(KeyedCollection): # skipped bases: <type 'IList[MessageHeaderDescription]'>, <type 'IReadOnlyCollection[MessageHeaderDescription]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IEnumerable[MessageHeaderDescription]'>, <type 'IReadOnlyList[MessageHeaderDescription]'>, <type 'ICollection'>, <type 'ICollection[MessageHeaderDescription]'>, <type 'object'>
    """ no doc """
    pass

class MessagePartDescriptionCollection(KeyedCollection): # skipped bases: <type 'IReadOnlyList[MessagePartDescription]'>, <type 'IReadOnlyCollection[MessagePartDescription]'>, <type 'IEnumerable[MessagePartDescription]'>, <type 'ICollection[MessagePartDescription]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection'>, <type 'IList[MessagePartDescription]'>, <type 'object'>
    """ no doc """
    pass

class MessagePropertyDescription(MessagePartDescription): # skipped bases: <type 'object'>
    """ MessagePropertyDescription(name: str) """
    pass

class MessagePropertyDescriptionCollection(KeyedCollection): # skipped bases: <type 'IList'>, <type 'IReadOnlyCollection[MessagePropertyDescription]'>, <type 'IEnumerable[MessagePropertyDescription]'>, <type 'IList[MessagePropertyDescription]'>, <type 'IEnumerable'>, <type 'ICollection[MessagePropertyDescription]'>, <type 'ICollection'>, <type 'IReadOnlyList[MessagePropertyDescription]'>, <type 'object'>
    """ no doc """
    pass

class MetadataConversionError: # skipped bases: <type 'object'>, <type 'object'>
    """
    MetadataConversionError(message: str)
    MetadataConversionError(message: str, isWarning: bool)
    """
    @property
    def IsWarning(self) -> bool:
        """ Get: IsWarning(self: MetadataConversionError) -> bool """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: MetadataConversionError) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: MetadataConversionError, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: MetadataConversionError) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MetadataExchangeBindings: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateMexHttpBinding() -> Binding:
        """ CreateMexHttpBinding() -> Binding """
        ...

    @staticmethod
    def CreateMexHttpsBinding() -> Binding:
        """ CreateMexHttpsBinding() -> Binding """
        ...

    @staticmethod
    def CreateMexNamedPipeBinding() -> Binding:
        """ CreateMexNamedPipeBinding() -> Binding """
        ...

    @staticmethod
    def CreateMexTcpBinding() -> Binding:
        """ CreateMexTcpBinding() -> Binding """
        ...

    __all__: list = ...


class MetadataExchangeClient: # skipped bases: <type 'object'>, <type 'object'>
    """
    MetadataExchangeClient()
    MetadataExchangeClient(address: Uri, mode: MetadataExchangeClientMode)
    MetadataExchangeClient(address: EndpointAddress)
    MetadataExchangeClient(endpointConfigurationName: str)
    MetadataExchangeClient(mexBinding: Binding)
    """
    @property
    def HttpCredentials(self) -> ICredentials:
        """
        Get: HttpCredentials(self: MetadataExchangeClient) -> ICredentials
        Set: HttpCredentials(self: MetadataExchangeClient) = value
        """
        ...

    @property
    def MaximumResolvedReferences(self) -> int:
        """
        Get: MaximumResolvedReferences(self: MetadataExchangeClient) -> int
        Set: MaximumResolvedReferences(self: MetadataExchangeClient) = value
        """
        ...

    @property
    def OperationTimeout(self) -> TimeSpan:
        """
        Get: OperationTimeout(self: MetadataExchangeClient) -> TimeSpan
        Set: OperationTimeout(self: MetadataExchangeClient) = value
        """
        ...

    @property
    def ResolveMetadataReferences(self) -> bool:
        """
        Get: ResolveMetadataReferences(self: MetadataExchangeClient) -> bool
        Set: ResolveMetadataReferences(self: MetadataExchangeClient) = value
        """
        ...

    @property
    def SoapCredentials(self) -> ClientCredentials:
        """
        Get: SoapCredentials(self: MetadataExchangeClient) -> ClientCredentials
        Set: SoapCredentials(self: MetadataExchangeClient) = value
        """
        ...


    def BeginGetMetadata(self, *__args) -> IAsyncResult:
        """
        BeginGetMetadata(self: MetadataExchangeClient, callback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginGetMetadata(self: MetadataExchangeClient, address: Uri, mode: MetadataExchangeClientMode, callback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginGetMetadata(self: MetadataExchangeClient, address: EndpointAddress, callback: AsyncCallback, asyncState: object) -> IAsyncResult
        """
        ...

    def EndGetMetadata(self, result:IAsyncResult): # -> MetadataSet
        """ EndGetMetadata(self: MetadataExchangeClient, result: IAsyncResult) -> MetadataSet """
        ...

    def GetChannelFactory(self, *args): #cannot find CLR method
        """ GetChannelFactory(self: MetadataExchangeClient, metadataAddress: EndpointAddress, dialect: str, identifier: str) -> ChannelFactory[IMetadataExchange] """
        ...

    def GetMetadata(self, address:Uri = ..., *__args): # -> MetadataSet # Not found arg types: {'*__args': 'MetadataExchangeClientMode'}
        """
        GetMetadata(self: MetadataExchangeClient) -> MetadataSet
        GetMetadata(self: MetadataExchangeClient, address: Uri, mode: MetadataExchangeClientMode) -> MetadataSet
        GetMetadata(self: MetadataExchangeClient, address: EndpointAddress) -> MetadataSet
        GetMetadata(self: MetadataExchangeClient, address: EndpointAddress, via: Uri) -> MetadataSet
        """
        ...

    def GetMetadataAsync(self, address:Uri = ..., *__args) -> Task: # Not found arg types: {'*__args': 'MetadataExchangeClientMode'}
        """
        GetMetadataAsync(self: MetadataExchangeClient) -> Task[MetadataSet]
        GetMetadataAsync(self: MetadataExchangeClient, address: Uri, mode: MetadataExchangeClientMode) -> Task[MetadataSet]
        GetMetadataAsync(self: MetadataExchangeClient, address: EndpointAddress) -> Task[MetadataSet]
        GetMetadataAsync(self: MetadataExchangeClient, address: EndpointAddress, via: Uri) -> Task[MetadataSet]
        """
        ...

    def GetWebRequest(self, *args): #cannot find CLR method
        """ GetWebRequest(self: MetadataExchangeClient, location: Uri, dialect: str, identifier: str) -> HttpWebRequest """
        ...


class MetadataExchangeClientMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MetadataExchangeClientMode, values: HttpGet (1), MetadataExchange (0) """
    HttpGet: MetadataExchangeClientMode = ...
    MetadataExchange: MetadataExchangeClientMode = ...
    value__ = ...


class MetadataExporter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Errors(self) -> Collection:
        """ Get: Errors(self: MetadataExporter) -> Collection[MetadataConversionError] """
        ...

    @property
    def PolicyVersion(self): # -> PolicyVersion
        """
        Get: PolicyVersion(self: MetadataExporter) -> PolicyVersion
        Set: PolicyVersion(self: MetadataExporter) = value
        """
        ...

    @property
    def State(self) -> Dictionary:
        """ Get: State(self: MetadataExporter) -> Dictionary[object, object] """
        ...


    def ExportContract(self, contract:ContractDescription): # -> 
        """ ExportContract(self: MetadataExporter, contract: ContractDescription) """
        ...

    def ExportEndpoint(self, endpoint): # ->  # Not found arg types: {'endpoint': 'ServiceEndpoint'}
        """ ExportEndpoint(self: MetadataExporter, endpoint: ServiceEndpoint) """
        ...

    def ExportPolicy(self, *args): #cannot find CLR method
        """ ExportPolicy(self: MetadataExporter, endpoint: ServiceEndpoint) -> PolicyConversionContext """
        ...

    def GetGeneratedMetadata(self): # -> MetadataSet
        """ GetGeneratedMetadata(self: MetadataExporter) -> MetadataSet """
        ...


class MetadataImporter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Errors(self) -> Collection:
        """ Get: Errors(self: MetadataImporter) -> Collection[MetadataConversionError] """
        ...

    @property
    def KnownContracts(self) -> Dictionary:
        """ Get: KnownContracts(self: MetadataImporter) -> Dictionary[XmlQualifiedName, ContractDescription] """
        ...

    @property
    def PolicyImportExtensions(self) -> KeyedByTypeCollection:
        """ Get: PolicyImportExtensions(self: MetadataImporter) -> KeyedByTypeCollection[IPolicyImportExtension] """
        ...

    @property
    def State(self) -> Dictionary:
        """ Get: State(self: MetadataImporter) -> Dictionary[object, object] """
        ...


    def ImportAllContracts(self) -> Collection:
        """ ImportAllContracts(self: MetadataImporter) -> Collection[ContractDescription] """
        ...

    def ImportAllEndpoints(self): # -> ServiceEndpointCollection
        """ ImportAllEndpoints(self: MetadataImporter) -> ServiceEndpointCollection """
        ...


class MetadataImporterQuotas: # skipped bases: <type 'object'>, <type 'object'>
    """ MetadataImporterQuotas() """
    @property
    def Defaults(self) -> MetadataImporterQuotas:
        """ Get: Defaults() -> MetadataImporterQuotas """
        ...

    @property
    def Max(self) -> MetadataImporterQuotas:
        """ Get: Max() -> MetadataImporterQuotas """
        ...




class MetadataLocation: # skipped bases: <type 'object'>, <type 'object'>
    """
    MetadataLocation()
    MetadataLocation(location: str)
    """
    @property
    def Location(self) -> str:
        """
        Get: Location(self: MetadataLocation) -> str
        Set: Location(self: MetadataLocation) = value
        """
        ...



class MetadataReference(IXmlSerializable): # skipped bases: <type 'object'>
    """
    MetadataReference()
    MetadataReference(address: EndpointAddress, addressVersion: AddressingVersion)
    """
    @property
    def Address(self) -> EndpointAddress:
        """
        Get: Address(self: MetadataReference) -> EndpointAddress
        Set: Address(self: MetadataReference) = value
        """
        ...

    @property
    def AddressVersion(self): # -> AddressingVersion
        """
        Get: AddressVersion(self: MetadataReference) -> AddressingVersion
        Set: AddressVersion(self: MetadataReference) = value
        """
        ...



class MetadataResolver: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def BeginResolve(*__args) -> IAsyncResult:
        """
        BeginResolve(contracts: IEnumerable[ContractDescription], address: EndpointAddress, callback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginResolve(contracts: IEnumerable[ContractDescription], address: Uri, mode: MetadataExchangeClientMode, callback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginResolve(contract: Type, address: EndpointAddress, callback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginResolve(contracts: IEnumerable[ContractDescription], address: EndpointAddress, client: MetadataExchangeClient, callback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginResolve(contract: Type, address: Uri, mode: MetadataExchangeClientMode, callback: AsyncCallback, asyncState: object) -> IAsyncResult
        BeginResolve(contracts: IEnumerable[ContractDescription], address: Uri, mode: MetadataExchangeClientMode, client: MetadataExchangeClient, callback: AsyncCallback, asyncState: object) -> IAsyncResult
        """
        ...

    @staticmethod
    def EndResolve(result:IAsyncResult): # -> ServiceEndpointCollection
        """ EndResolve(result: IAsyncResult) -> ServiceEndpointCollection """
        ...

    @staticmethod
    def Resolve(*__args): # -> ServiceEndpointCollection
        """
        Resolve(contracts: IEnumerable[ContractDescription], address: EndpointAddress) -> ServiceEndpointCollection
        Resolve(contracts: IEnumerable[ContractDescription], address: Uri, mode: MetadataExchangeClientMode) -> ServiceEndpointCollection
        Resolve(contract: Type, address: EndpointAddress) -> ServiceEndpointCollection
        Resolve(contracts: IEnumerable[ContractDescription], address: EndpointAddress, client: MetadataExchangeClient) -> ServiceEndpointCollection
        Resolve(contract: Type, address: Uri, mode: MetadataExchangeClientMode) -> ServiceEndpointCollection
        Resolve(contracts: IEnumerable[ContractDescription], address: Uri, mode: MetadataExchangeClientMode, client: MetadataExchangeClient) -> ServiceEndpointCollection
        """
        ...

    __all__: list = ...


class MetadataSection: # skipped bases: <type 'object'>, <type 'object'>
    """
    MetadataSection()
    MetadataSection(dialect: str, identifier: str, metadata: object)
    """
    @property
    def Attributes(self) -> Collection:
        """ Get: Attributes(self: MetadataSection) -> Collection[XmlAttribute] """
        ...

    @property
    def Dialect(self) -> str:
        """
        Get: Dialect(self: MetadataSection) -> str
        Set: Dialect(self: MetadataSection) = value
        """
        ...

    @property
    def Identifier(self) -> str:
        """
        Get: Identifier(self: MetadataSection) -> str
        Set: Identifier(self: MetadataSection) = value
        """
        ...

    @property
    def Metadata(self) -> object:
        """
        Get: Metadata(self: MetadataSection) -> object
        Set: Metadata(self: MetadataSection) = value
        """
        ...

    @property
    def MetadataExchangeDialect(self) -> str:
        """ Get: MetadataExchangeDialect() -> str """
        ...

    @property
    def PolicyDialect(self) -> str:
        """ Get: PolicyDialect() -> str """
        ...

    @property
    def ServiceDescriptionDialect(self) -> str:
        """ Get: ServiceDescriptionDialect() -> str """
        ...

    @property
    def XmlSchemaDialect(self) -> str:
        """ Get: XmlSchemaDialect() -> str """
        ...


    @staticmethod
    def CreateFromPolicy(policy:XmlElement, identifier:str) -> MetadataSection:
        """ CreateFromPolicy(policy: XmlElement, identifier: str) -> MetadataSection """
        ...

    @staticmethod
    def CreateFromSchema(schema:XmlSchema) -> MetadataSection:
        """ CreateFromSchema(schema: XmlSchema) -> MetadataSection """
        ...

    @staticmethod
    def CreateFromServiceDescription(serviceDescription:ServiceDescription) -> MetadataSection:
        """ CreateFromServiceDescription(serviceDescription: ServiceDescription) -> MetadataSection """
        ...



class MetadataSet(IXmlSerializable): # skipped bases: <type 'object'>
    """
    MetadataSet()
    MetadataSet(sections: IEnumerable[MetadataSection])
    """
    @property
    def Attributes(self) -> Collection:
        """ Get: Attributes(self: MetadataSet) -> Collection[XmlAttribute] """
        ...

    @property
    def MetadataSections(self) -> Collection:
        """ Get: MetadataSections(self: MetadataSet) -> Collection[MetadataSection] """
        ...


    @staticmethod
    def ReadFrom(reader:XmlReader) -> MetadataSet:
        """ ReadFrom(reader: XmlReader) -> MetadataSet """
        ...

    def WriteTo(self, writer:XmlWriter): # -> 
        """ WriteTo(self: MetadataSet, writer: XmlWriter) """
        ...


class MustUnderstandBehavior(IEndpointBehavior): # skipped bases: <type 'object'>
    """ MustUnderstandBehavior(validate: bool) """
    @property
    def ValidateMustUnderstand(self) -> bool:
        """
        Get: ValidateMustUnderstand(self: MustUnderstandBehavior) -> bool
        Set: ValidateMustUnderstand(self: MustUnderstandBehavior) = value
        """
        ...



class OperationContractGenerationContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    OperationContractGenerationContext(serviceContractGenerator: ServiceContractGenerator, contract: ServiceContractGenerationContext, operation: OperationDescription, declaringType: CodeTypeDeclaration, syncMethod: CodeMemberMethod, beginMethod: CodeMemberMethod, endMethod: CodeMemberMethod, taskMethod: CodeMemberMethod)
    OperationContractGenerationContext(serviceContractGenerator: ServiceContractGenerator, contract: ServiceContractGenerationContext, operation: OperationDescription, declaringType: CodeTypeDeclaration, syncMethod: CodeMemberMethod, beginMethod: CodeMemberMethod, endMethod: CodeMemberMethod)
    OperationContractGenerationContext(serviceContractGenerator: ServiceContractGenerator, contract: ServiceContractGenerationContext, operation: OperationDescription, declaringType: CodeTypeDeclaration, syncMethod: CodeMemberMethod, taskMethod: CodeMemberMethod)
    OperationContractGenerationContext(serviceContractGenerator: ServiceContractGenerator, contract: ServiceContractGenerationContext, operation: OperationDescription, declaringType: CodeTypeDeclaration, method: CodeMemberMethod)
    """
    @property
    def BeginMethod(self) -> CodeMemberMethod:
        """ Get: BeginMethod(self: OperationContractGenerationContext) -> CodeMemberMethod """
        ...

    @property
    def Contract(self): # -> ServiceContractGenerationContext
        """ Get: Contract(self: OperationContractGenerationContext) -> ServiceContractGenerationContext """
        ...

    @property
    def DeclaringType(self) -> CodeTypeDeclaration:
        """ Get: DeclaringType(self: OperationContractGenerationContext) -> CodeTypeDeclaration """
        ...

    @property
    def EndMethod(self) -> CodeMemberMethod:
        """ Get: EndMethod(self: OperationContractGenerationContext) -> CodeMemberMethod """
        ...

    @property
    def IsAsync(self) -> bool:
        """ Get: IsAsync(self: OperationContractGenerationContext) -> bool """
        ...

    @property
    def IsTask(self) -> bool:
        """ Get: IsTask(self: OperationContractGenerationContext) -> bool """
        ...

    @property
    def Operation(self): # -> OperationDescription
        """ Get: Operation(self: OperationContractGenerationContext) -> OperationDescription """
        ...

    @property
    def ServiceContractGenerator(self): # -> ServiceContractGenerator
        """ Get: ServiceContractGenerator(self: OperationContractGenerationContext) -> ServiceContractGenerator """
        ...

    @property
    def SyncMethod(self) -> CodeMemberMethod:
        """ Get: SyncMethod(self: OperationContractGenerationContext) -> CodeMemberMethod """
        ...

    @property
    def TaskMethod(self) -> CodeMemberMethod:
        """ Get: TaskMethod(self: OperationContractGenerationContext) -> CodeMemberMethod """
        ...



class OperationDescription: # skipped bases: <type 'object'>, <type 'object'>
    """ OperationDescription(name: str, declaringContract: ContractDescription) """
    @property
    def BeginMethod(self) -> MethodInfo:
        """
        Get: BeginMethod(self: OperationDescription) -> MethodInfo
        Set: BeginMethod(self: OperationDescription) = value
        """
        ...

    @property
    def Behaviors(self) -> KeyedByTypeCollection:
        """ Get: Behaviors(self: OperationDescription) -> KeyedByTypeCollection[IOperationBehavior] """
        ...

    @property
    def DeclaringContract(self) -> ContractDescription:
        """
        Get: DeclaringContract(self: OperationDescription) -> ContractDescription
        Set: DeclaringContract(self: OperationDescription) = value
        """
        ...

    @property
    def EndMethod(self) -> MethodInfo:
        """
        Get: EndMethod(self: OperationDescription) -> MethodInfo
        Set: EndMethod(self: OperationDescription) = value
        """
        ...

    @property
    def Faults(self) -> FaultDescriptionCollection:
        """ Get: Faults(self: OperationDescription) -> FaultDescriptionCollection """
        ...

    @property
    def HasProtectionLevel(self) -> bool:
        """ Get: HasProtectionLevel(self: OperationDescription) -> bool """
        ...

    @property
    def IsInitiating(self) -> bool:
        """
        Get: IsInitiating(self: OperationDescription) -> bool
        Set: IsInitiating(self: OperationDescription) = value
        """
        ...

    @property
    def IsOneWay(self) -> bool:
        """ Get: IsOneWay(self: OperationDescription) -> bool """
        ...

    @property
    def IsTerminating(self) -> bool:
        """
        Get: IsTerminating(self: OperationDescription) -> bool
        Set: IsTerminating(self: OperationDescription) = value
        """
        ...

    @property
    def KnownTypes(self) -> Collection:
        """ Get: KnownTypes(self: OperationDescription) -> Collection[Type] """
        ...

    @property
    def Messages(self) -> MessageDescriptionCollection:
        """ Get: Messages(self: OperationDescription) -> MessageDescriptionCollection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: OperationDescription) -> str """
        ...

    @property
    def OperationBehaviors(self) -> KeyedCollection:
        """ Get: OperationBehaviors(self: OperationDescription) -> KeyedCollection[Type, IOperationBehavior] """
        ...

    @property
    def ProtectionLevel(self) -> ProtectionLevel:
        """
        Get: ProtectionLevel(self: OperationDescription) -> ProtectionLevel
        Set: ProtectionLevel(self: OperationDescription) = value
        """
        ...

    @property
    def SyncMethod(self) -> MethodInfo:
        """
        Get: SyncMethod(self: OperationDescription) -> MethodInfo
        Set: SyncMethod(self: OperationDescription) = value
        """
        ...

    @property
    def TaskMethod(self) -> MethodInfo:
        """
        Get: TaskMethod(self: OperationDescription) -> MethodInfo
        Set: TaskMethod(self: OperationDescription) = value
        """
        ...


    def ShouldSerializeProtectionLevel(self) -> bool:
        """ ShouldSerializeProtectionLevel(self: OperationDescription) -> bool """
        ...


class OperationDescriptionCollection(Collection): # skipped bases: <type 'IReadOnlyList[OperationDescription]'>, <type 'IReadOnlyCollection[OperationDescription]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IList[OperationDescription]'>, <type 'IEnumerable[OperationDescription]'>, <type 'ICollection[OperationDescription]'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Find(self, name:str) -> OperationDescription:
        """ Find(self: OperationDescriptionCollection, name: str) -> OperationDescription """
        ...

    def FindAll(self, name:str) -> Collection:
        """ FindAll(self: OperationDescriptionCollection, name: str) -> Collection[OperationDescription] """
        ...


class ParameterXPathQueryGenerator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateFromDataContractSerializer(serviceContractName, operationName, parameterName, isReply, type, pathToMember, namespaces) -> Tuple_[str, XmlNamespaceManager]:
        """ CreateFromDataContractSerializer(serviceContractName: XName, operationName: str, parameterName: str, isReply: bool, type: Type, pathToMember: Array[MemberInfo]) -> (str, XmlNamespaceManager) """
        ...

    __all__: list = ...


class PersistenceProviderBehavior(IServiceBehavior, IWmiInstanceProvider): # skipped bases: <type 'object'>
    """
    PersistenceProviderBehavior(providerFactory: PersistenceProviderFactory)
    PersistenceProviderBehavior(providerFactory: PersistenceProviderFactory, persistenceOperationTimeout: TimeSpan)
    """
    @property
    def PersistenceOperationTimeout(self) -> TimeSpan:
        """
        Get: PersistenceOperationTimeout(self: PersistenceProviderBehavior) -> TimeSpan
        Set: PersistenceOperationTimeout(self: PersistenceProviderBehavior) = value
        """
        ...

    @property
    def PersistenceProviderFactory(self) -> PersistenceProviderFactory:
        """
        Get: PersistenceProviderFactory(self: PersistenceProviderBehavior) -> PersistenceProviderFactory
        Set: PersistenceProviderFactory(self: PersistenceProviderBehavior) = value
        """
        ...



class PolicyAssertionCollection(Collection): # skipped bases: <type 'ICollection[XmlElement]'>, <type 'IReadOnlyCollection[XmlElement]'>, <type 'IList[XmlElement]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IReadOnlyList[XmlElement]'>, <type 'IEnumerable[XmlElement]'>, <type 'ICollection'>, <type 'object'>
    """
    PolicyAssertionCollection()
    PolicyAssertionCollection(elements: IEnumerable[XmlElement])
    """
    def Find(self, localName:str, namespaceUri:str) -> XmlElement:
        """ Find(self: PolicyAssertionCollection, localName: str, namespaceUri: str) -> XmlElement """
        ...

    def FindAll(self, localName:str, namespaceUri:str) -> Collection:
        """ FindAll(self: PolicyAssertionCollection, localName: str, namespaceUri: str) -> Collection[XmlElement] """
        ...

    def RemoveAll(self, localName:str, namespaceUri:str) -> Collection:
        """ RemoveAll(self: PolicyAssertionCollection, localName: str, namespaceUri: str) -> Collection[XmlElement] """
        ...


class PolicyConversionContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BindingElements(self): # -> BindingElementCollection
        """ Get: BindingElements(self: PolicyConversionContext) -> BindingElementCollection """
        ...

    @property
    def Contract(self) -> ContractDescription:
        """ Get: Contract(self: PolicyConversionContext) -> ContractDescription """
        ...


    def GetBindingAssertions(self) -> PolicyAssertionCollection:
        """ GetBindingAssertions(self: PolicyConversionContext) -> PolicyAssertionCollection """
        ...

    def GetFaultBindingAssertions(self, fault:FaultDescription) -> PolicyAssertionCollection:
        """ GetFaultBindingAssertions(self: PolicyConversionContext, fault: FaultDescription) -> PolicyAssertionCollection """
        ...

    def GetMessageBindingAssertions(self, message:MessageDescription) -> PolicyAssertionCollection:
        """ GetMessageBindingAssertions(self: PolicyConversionContext, message: MessageDescription) -> PolicyAssertionCollection """
        ...

    def GetOperationBindingAssertions(self, operation:OperationDescription) -> PolicyAssertionCollection:
        """ GetOperationBindingAssertions(self: PolicyConversionContext, operation: OperationDescription) -> PolicyAssertionCollection """
        ...


class PolicyVersion: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Default(self) -> PolicyVersion:
        """ Get: Default() -> PolicyVersion """
        ...

    @property
    def Namespace(self) -> str:
        """ Get: Namespace(self: PolicyVersion) -> str """
        ...

    @property
    def Policy12(self) -> PolicyVersion:
        """ Get: Policy12() -> PolicyVersion """
        ...

    @property
    def Policy15(self) -> PolicyVersion:
        """ Get: Policy15() -> PolicyVersion """
        ...


    def ToString(self) -> str:
        """ ToString(self: PolicyVersion) -> str """
        ...



class PrincipalPermissionMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PrincipalPermissionMode, values: Always (4), Custom (3), None (0), UseAspNetRoles (2), UseWindowsGroups (1) """
    Always: PrincipalPermissionMode = ...
    Custom: PrincipalPermissionMode = ...
    UseAspNetRoles: PrincipalPermissionMode = ...
    UseWindowsGroups: PrincipalPermissionMode = ...
    value__ = ...


class ServiceAuthenticationBehavior(IServiceBehavior): # skipped bases: <type 'object'>
    """ ServiceAuthenticationBehavior() """
    @property
    def AuthenticationSchemes(self) -> AuthenticationSchemes:
        """
        Get: AuthenticationSchemes(self: ServiceAuthenticationBehavior) -> AuthenticationSchemes
        Set: AuthenticationSchemes(self: ServiceAuthenticationBehavior) = value
        """
        ...

    @property
    def ServiceAuthenticationManager(self) -> ServiceAuthenticationManager:
        """
        Get: ServiceAuthenticationManager(self: ServiceAuthenticationBehavior) -> ServiceAuthenticationManager
        Set: ServiceAuthenticationManager(self: ServiceAuthenticationBehavior) = value
        """
        ...


    def ShouldSerializeAuthenticationSchemes(self) -> bool:
        """ ShouldSerializeAuthenticationSchemes(self: ServiceAuthenticationBehavior) -> bool """
        ...

    def ShouldSerializeServiceAuthenticationManager(self) -> bool:
        """ ShouldSerializeServiceAuthenticationManager(self: ServiceAuthenticationBehavior) -> bool """
        ...


class ServiceAuthorizationBehavior(IServiceBehavior): # skipped bases: <type 'object'>
    """ ServiceAuthorizationBehavior() """
    @property
    def ExternalAuthorizationPolicies(self) -> ReadOnlyCollection:
        """
        Get: ExternalAuthorizationPolicies(self: ServiceAuthorizationBehavior) -> ReadOnlyCollection[IAuthorizationPolicy]
        Set: ExternalAuthorizationPolicies(self: ServiceAuthorizationBehavior) = value
        """
        ...

    @property
    def ImpersonateCallerForAllOperations(self) -> bool:
        """
        Get: ImpersonateCallerForAllOperations(self: ServiceAuthorizationBehavior) -> bool
        Set: ImpersonateCallerForAllOperations(self: ServiceAuthorizationBehavior) = value
        """
        ...

    @property
    def ImpersonateOnSerializingReply(self) -> bool:
        """
        Get: ImpersonateOnSerializingReply(self: ServiceAuthorizationBehavior) -> bool
        Set: ImpersonateOnSerializingReply(self: ServiceAuthorizationBehavior) = value
        """
        ...

    @property
    def PrincipalPermissionMode(self) -> PrincipalPermissionMode:
        """
        Get: PrincipalPermissionMode(self: ServiceAuthorizationBehavior) -> PrincipalPermissionMode
        Set: PrincipalPermissionMode(self: ServiceAuthorizationBehavior) = value
        """
        ...

    @property
    def RoleProvider(self) -> RoleProvider:
        """
        Get: RoleProvider(self: ServiceAuthorizationBehavior) -> RoleProvider
        Set: RoleProvider(self: ServiceAuthorizationBehavior) = value
        """
        ...

    @property
    def ServiceAuthorizationManager(self) -> ServiceAuthorizationManager:
        """
        Get: ServiceAuthorizationManager(self: ServiceAuthorizationBehavior) -> ServiceAuthorizationManager
        Set: ServiceAuthorizationManager(self: ServiceAuthorizationBehavior) = value
        """
        ...


    def ShouldSerializeExternalAuthorizationPolicies(self) -> bool:
        """ ShouldSerializeExternalAuthorizationPolicies(self: ServiceAuthorizationBehavior) -> bool """
        ...

    def ShouldSerializeServiceAuthorizationManager(self) -> bool:
        """ ShouldSerializeServiceAuthorizationManager(self: ServiceAuthorizationBehavior) -> bool """
        ...


class ServiceContractGenerationContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    ServiceContractGenerationContext(serviceContractGenerator: ServiceContractGenerator, contract: ContractDescription, contractType: CodeTypeDeclaration)
    ServiceContractGenerationContext(serviceContractGenerator: ServiceContractGenerator, contract: ContractDescription, contractType: CodeTypeDeclaration, duplexCallbackType: CodeTypeDeclaration)
    """
    @property
    def Contract(self) -> ContractDescription:
        """ Get: Contract(self: ServiceContractGenerationContext) -> ContractDescription """
        ...

    @property
    def ContractType(self) -> CodeTypeDeclaration:
        """ Get: ContractType(self: ServiceContractGenerationContext) -> CodeTypeDeclaration """
        ...

    @property
    def DuplexCallbackType(self) -> CodeTypeDeclaration:
        """ Get: DuplexCallbackType(self: ServiceContractGenerationContext) -> CodeTypeDeclaration """
        ...

    @property
    def Operations(self) -> Collection:
        """ Get: Operations(self: ServiceContractGenerationContext) -> Collection[OperationContractGenerationContext] """
        ...

    @property
    def ServiceContractGenerator(self): # -> ServiceContractGenerator
        """ Get: ServiceContractGenerator(self: ServiceContractGenerationContext) -> ServiceContractGenerator """
        ...



class ServiceContractGenerationOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ServiceContractGenerationOptions, values: AsynchronousMethods (1), ChannelInterface (2), ClientClass (8), EventBasedAsynchronousMethods (32), InternalTypes (4), None (0), TaskBasedAsynchronousMethod (64), TypedMessages (16) """
    AsynchronousMethods: ServiceContractGenerationOptions = ...
    ChannelInterface: ServiceContractGenerationOptions = ...
    ClientClass: ServiceContractGenerationOptions = ...
    EventBasedAsynchronousMethods: ServiceContractGenerationOptions = ...
    InternalTypes: ServiceContractGenerationOptions = ...
    TaskBasedAsynchronousMethod: ServiceContractGenerationOptions = ...
    TypedMessages: ServiceContractGenerationOptions = ...
    value__ = ...


class ServiceContractGenerator: # skipped bases: <type 'object'>, <type 'object'>
    """
    ServiceContractGenerator()
    ServiceContractGenerator(targetConfig: Configuration)
    ServiceContractGenerator(targetCompileUnit: CodeCompileUnit)
    ServiceContractGenerator(targetCompileUnit: CodeCompileUnit, targetConfig: Configuration)
    """
    @property
    def Configuration(self) -> Configuration:
        """ Get: Configuration(self: ServiceContractGenerator) -> Configuration """
        ...

    @property
    def Errors(self) -> Collection:
        """ Get: Errors(self: ServiceContractGenerator) -> Collection[MetadataConversionError] """
        ...

    @property
    def NamespaceMappings(self) -> Dictionary:
        """ Get: NamespaceMappings(self: ServiceContractGenerator) -> Dictionary[str, str] """
        ...

    @property
    def Options(self) -> ServiceContractGenerationOptions:
        """
        Get: Options(self: ServiceContractGenerator) -> ServiceContractGenerationOptions
        Set: Options(self: ServiceContractGenerator) = value
        """
        ...

    @property
    def ReferencedTypes(self) -> Dictionary:
        """ Get: ReferencedTypes(self: ServiceContractGenerator) -> Dictionary[ContractDescription, Type] """
        ...

    @property
    def TargetCompileUnit(self) -> CodeCompileUnit:
        """ Get: TargetCompileUnit(self: ServiceContractGenerator) -> CodeCompileUnit """
        ...


    def GenerateBinding(self, binding, bindingSectionName, configurationName) -> Tuple_[str, str]:
        """ GenerateBinding(self: ServiceContractGenerator, binding: Binding) -> (str, str) """
        ...

    def GenerateServiceContractType(self, contractDescription:ContractDescription) -> CodeTypeReference:
        """ GenerateServiceContractType(self: ServiceContractGenerator, contractDescription: ContractDescription) -> CodeTypeReference """
        ...

    def GenerateServiceEndpoint(self, endpoint, channelElement) -> Tuple_[CodeTypeReference, ChannelEndpointElement]:
        """ GenerateServiceEndpoint(self: ServiceContractGenerator, endpoint: ServiceEndpoint) -> (CodeTypeReference, ChannelEndpointElement) """
        ...


class ServiceCredentials(SecurityCredentialsManager, IServiceBehavior): # skipped bases: <type 'object'>
    """ ServiceCredentials() """
    @property
    def ClientCertificate(self) -> X509CertificateInitiatorServiceCredential:
        """ Get: ClientCertificate(self: ServiceCredentials) -> X509CertificateInitiatorServiceCredential """
        ...

    @property
    def ExceptionMapper(self) -> ExceptionMapper:
        """
        Get: ExceptionMapper(self: ServiceCredentials) -> ExceptionMapper
        Set: ExceptionMapper(self: ServiceCredentials) = value
        """
        ...

    @property
    def IdentityConfiguration(self) -> IdentityConfiguration:
        """
        Get: IdentityConfiguration(self: ServiceCredentials) -> IdentityConfiguration
        Set: IdentityConfiguration(self: ServiceCredentials) = value
        """
        ...

    @property
    def IssuedTokenAuthentication(self) -> IssuedTokenServiceCredential:
        """ Get: IssuedTokenAuthentication(self: ServiceCredentials) -> IssuedTokenServiceCredential """
        ...

    @property
    def Peer(self) -> PeerCredential:
        """ Get: Peer(self: ServiceCredentials) -> PeerCredential """
        ...

    @property
    def SecureConversationAuthentication(self) -> SecureConversationServiceCredential:
        """ Get: SecureConversationAuthentication(self: ServiceCredentials) -> SecureConversationServiceCredential """
        ...

    @property
    def ServiceCertificate(self) -> X509CertificateRecipientServiceCredential:
        """ Get: ServiceCertificate(self: ServiceCredentials) -> X509CertificateRecipientServiceCredential """
        ...

    @property
    def UseIdentityConfiguration(self) -> bool:
        """
        Get: UseIdentityConfiguration(self: ServiceCredentials) -> bool
        Set: UseIdentityConfiguration(self: ServiceCredentials) = value
        """
        ...

    @property
    def UserNameAuthentication(self) -> UserNamePasswordServiceCredential:
        """ Get: UserNameAuthentication(self: ServiceCredentials) -> UserNamePasswordServiceCredential """
        ...

    @property
    def WindowsAuthentication(self) -> WindowsServiceCredential:
        """ Get: WindowsAuthentication(self: ServiceCredentials) -> WindowsServiceCredential """
        ...


    def Clone(self) -> ServiceCredentials:
        """ Clone(self: ServiceCredentials) -> ServiceCredentials """
        ...

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: ServiceCredentials) -> ServiceCredentials """
        ...

    def __new__(cls) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, other: ServiceCredentials)
        """
        ...


class ServiceDebugBehavior(IServiceBehavior): # skipped bases: <type 'object'>
    """ ServiceDebugBehavior() """
    @property
    def HttpHelpPageBinding(self) -> Binding:
        """
        Get: HttpHelpPageBinding(self: ServiceDebugBehavior) -> Binding
        Set: HttpHelpPageBinding(self: ServiceDebugBehavior) = value
        """
        ...

    @property
    def HttpHelpPageEnabled(self) -> bool:
        """
        Get: HttpHelpPageEnabled(self: ServiceDebugBehavior) -> bool
        Set: HttpHelpPageEnabled(self: ServiceDebugBehavior) = value
        """
        ...

    @property
    def HttpHelpPageUrl(self) -> Uri:
        """
        Get: HttpHelpPageUrl(self: ServiceDebugBehavior) -> Uri
        Set: HttpHelpPageUrl(self: ServiceDebugBehavior) = value
        """
        ...

    @property
    def HttpsHelpPageBinding(self) -> Binding:
        """
        Get: HttpsHelpPageBinding(self: ServiceDebugBehavior) -> Binding
        Set: HttpsHelpPageBinding(self: ServiceDebugBehavior) = value
        """
        ...

    @property
    def HttpsHelpPageEnabled(self) -> bool:
        """
        Get: HttpsHelpPageEnabled(self: ServiceDebugBehavior) -> bool
        Set: HttpsHelpPageEnabled(self: ServiceDebugBehavior) = value
        """
        ...

    @property
    def HttpsHelpPageUrl(self) -> Uri:
        """
        Get: HttpsHelpPageUrl(self: ServiceDebugBehavior) -> Uri
        Set: HttpsHelpPageUrl(self: ServiceDebugBehavior) = value
        """
        ...

    @property
    def IncludeExceptionDetailInFaults(self) -> bool:
        """
        Get: IncludeExceptionDetailInFaults(self: ServiceDebugBehavior) -> bool
        Set: IncludeExceptionDetailInFaults(self: ServiceDebugBehavior) = value
        """
        ...



class ServiceDescription: # skipped bases: <type 'object'>, <type 'object'>
    """
    ServiceDescription()
    ServiceDescription(endpoints: IEnumerable[ServiceEndpoint])
    """
    @property
    def Behaviors(self) -> KeyedByTypeCollection:
        """ Get: Behaviors(self: ServiceDescription) -> KeyedByTypeCollection[IServiceBehavior] """
        ...

    @property
    def ConfigurationName(self) -> str:
        """
        Get: ConfigurationName(self: ServiceDescription) -> str
        Set: ConfigurationName(self: ServiceDescription) = value
        """
        ...

    @property
    def Endpoints(self): # -> ServiceEndpointCollection
        """ Get: Endpoints(self: ServiceDescription) -> ServiceEndpointCollection """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ServiceDescription) -> str
        Set: Name(self: ServiceDescription) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: ServiceDescription) -> str
        Set: Namespace(self: ServiceDescription) = value
        """
        ...

    @property
    def ServiceType(self) -> Type:
        """
        Get: ServiceType(self: ServiceDescription) -> Type
        Set: ServiceType(self: ServiceDescription) = value
        """
        ...


    @staticmethod
    def GetService(*__args:object) -> ServiceDescription:
        """
        GetService(serviceImplementation: object) -> ServiceDescription
        GetService(serviceType: Type) -> ServiceDescription
        """
        ...


class ServiceEndpoint: # skipped bases: <type 'object'>, <type 'object'>
    """
    ServiceEndpoint(contract: ContractDescription)
    ServiceEndpoint(contract: ContractDescription, binding: Binding, address: EndpointAddress)
    """
    @property
    def Address(self) -> EndpointAddress:
        """
        Get: Address(self: ServiceEndpoint) -> EndpointAddress
        Set: Address(self: ServiceEndpoint) = value
        """
        ...

    @property
    def Behaviors(self) -> KeyedByTypeCollection:
        """ Get: Behaviors(self: ServiceEndpoint) -> KeyedByTypeCollection[IEndpointBehavior] """
        ...

    @property
    def Binding(self) -> Binding:
        """
        Get: Binding(self: ServiceEndpoint) -> Binding
        Set: Binding(self: ServiceEndpoint) = value
        """
        ...

    @property
    def Contract(self) -> ContractDescription:
        """
        Get: Contract(self: ServiceEndpoint) -> ContractDescription
        Set: Contract(self: ServiceEndpoint) = value
        """
        ...

    @property
    def EndpointBehaviors(self) -> KeyedCollection:
        """ Get: EndpointBehaviors(self: ServiceEndpoint) -> KeyedCollection[Type, IEndpointBehavior] """
        ...

    @property
    def IsSystemEndpoint(self) -> bool:
        """
        Get: IsSystemEndpoint(self: ServiceEndpoint) -> bool
        Set: IsSystemEndpoint(self: ServiceEndpoint) = value
        """
        ...

    @property
    def ListenUri(self) -> Uri:
        """
        Get: ListenUri(self: ServiceEndpoint) -> Uri
        Set: ListenUri(self: ServiceEndpoint) = value
        """
        ...

    @property
    def ListenUriMode(self) -> ListenUriMode:
        """
        Get: ListenUriMode(self: ServiceEndpoint) -> ListenUriMode
        Set: ListenUriMode(self: ServiceEndpoint) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ServiceEndpoint) -> str
        Set: Name(self: ServiceEndpoint) = value
        """
        ...



class ServiceEndpointCollection(Collection): # skipped bases: <type 'IReadOnlyCollection[ServiceEndpoint]'>, <type 'IReadOnlyList[ServiceEndpoint]'>, <type 'IEnumerable'>, <type 'IEnumerable[ServiceEndpoint]'>, <type 'IList'>, <type 'ICollection[ServiceEndpoint]'>, <type 'IList[ServiceEndpoint]'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Find(self, *__args:Type) -> ServiceEndpoint:
        """
        Find(self: ServiceEndpointCollection, contractType: Type) -> ServiceEndpoint
        Find(self: ServiceEndpointCollection, contractName: XmlQualifiedName) -> ServiceEndpoint
        Find(self: ServiceEndpointCollection, contractType: Type, bindingName: XmlQualifiedName) -> ServiceEndpoint
        Find(self: ServiceEndpointCollection, contractName: XmlQualifiedName, bindingName: XmlQualifiedName) -> ServiceEndpoint
        Find(self: ServiceEndpointCollection, address: Uri) -> ServiceEndpoint
        """
        ...

    def FindAll(self, *__args:Type) -> Collection:
        """
        FindAll(self: ServiceEndpointCollection, contractType: Type) -> Collection[ServiceEndpoint]
        FindAll(self: ServiceEndpointCollection, contractName: XmlQualifiedName) -> Collection[ServiceEndpoint]
        """
        ...


class ServiceHealthBehaviorBase(IServiceBehavior): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def HealthDetailsEnabled(self) -> bool:
        """
        Get: HealthDetailsEnabled(self: ServiceHealthBehaviorBase) -> bool
        Set: HealthDetailsEnabled(self: ServiceHealthBehaviorBase) = value
        """
        ...

    @property
    def HttpGetBinding(self) -> Binding:
        """
        Get: HttpGetBinding(self: ServiceHealthBehaviorBase) -> Binding
        Set: HttpGetBinding(self: ServiceHealthBehaviorBase) = value
        """
        ...

    @property
    def HttpGetEnabled(self) -> bool:
        """
        Get: HttpGetEnabled(self: ServiceHealthBehaviorBase) -> bool
        Set: HttpGetEnabled(self: ServiceHealthBehaviorBase) = value
        """
        ...

    @property
    def HttpGetUrl(self) -> Uri:
        """
        Get: HttpGetUrl(self: ServiceHealthBehaviorBase) -> Uri
        Set: HttpGetUrl(self: ServiceHealthBehaviorBase) = value
        """
        ...

    @property
    def HttpsGetBinding(self) -> Binding:
        """
        Get: HttpsGetBinding(self: ServiceHealthBehaviorBase) -> Binding
        Set: HttpsGetBinding(self: ServiceHealthBehaviorBase) = value
        """
        ...

    @property
    def HttpsGetEnabled(self) -> bool:
        """
        Get: HttpsGetEnabled(self: ServiceHealthBehaviorBase) -> bool
        Set: HttpsGetEnabled(self: ServiceHealthBehaviorBase) = value
        """
        ...

    @property
    def HttpsGetUrl(self) -> Uri:
        """
        Get: HttpsGetUrl(self: ServiceHealthBehaviorBase) -> Uri
        Set: HttpsGetUrl(self: ServiceHealthBehaviorBase) = value
        """
        ...

    @property
    def ServiceStartTime(self):
        ...


    def HandleHealthRequest(self, serviceHost, httpGetRequest, queries, replyMessage) -> Message:
        """ HandleHealthRequest(self: ServiceHealthBehaviorBase, serviceHost: ServiceHostBase, httpGetRequest: Message, queries: Array[str]) -> Message """
        ...


class ServiceHealthBehavior(ServiceHealthBehaviorBase): # skipped bases: <type 'IServiceBehavior'>, <type 'object'>
    """ ServiceHealthBehavior() """
    @property
    def HasXmlSupport(self):
        ...


    def AddHttpProperty(self, *args): #cannot find CLR method
        """ AddHttpProperty(message: Message, status: HttpStatusCode, isXml: bool) """
        ...

    def EnsureHttpStatusCode(self, *args): #cannot find CLR method
        """ EnsureHttpStatusCode(code: int) -> bool """
        ...

    def GetHttpResponseCode(self, *args): #cannot find CLR method
        """ GetHttpResponseCode(self: ServiceHealthBehavior, serviceHost: ServiceHostBase, queries: Array[str]) -> HttpStatusCode """
        ...

    def GetServiceHealthSections(self, *args): #cannot find CLR method
        """ GetServiceHealthSections(self: ServiceHealthBehavior, serviceHost: ServiceHostBase) -> ServiceHealthSectionCollection """
        ...

    def GetXmlDocument(self, *args): #cannot find CLR method
        """ GetXmlDocument(self: ServiceHealthBehavior, serviceHost: ServiceHostBase) -> XmlDocument """
        ...

    def TryParseBooleanQueryParameter(self, *args): #cannot find CLR method
        """ TryParseBooleanQueryParameter(parameterName: str, parameter: str, defaultValue: bool) -> (bool, bool) """
        ...

    def TryParseHttpStatusCodeQueryParameter(self, *args): #cannot find CLR method
        """ TryParseHttpStatusCodeQueryParameter(parameterName: str, parameter: str, defaultErrorCode: HttpStatusCode) -> (bool, HttpStatusCode) """
        ...


class ServiceHealthData: # skipped bases: <type 'object'>, <type 'object'>
    """ ServiceHealthData(key: str, values: Array[str]) """
    @property
    def Key(self) -> str:
        """
        Get: Key(self: ServiceHealthData) -> str
        Set: Key(self: ServiceHealthData) = value
        """
        ...

    @property
    def Values(self) -> Array:
        """
        Get: Values(self: ServiceHealthData) -> Array[str]
        Set: Values(self: ServiceHealthData) = value
        """
        ...



class ServiceHealthDataCollection(KeyedCollection): # skipped bases: <type 'IList[ServiceHealthData]'>, <type 'IReadOnlyCollection[ServiceHealthData]'>, <type 'IReadOnlyList[ServiceHealthData]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[ServiceHealthData]'>, <type 'IEnumerable[ServiceHealthData]'>, <type 'ICollection'>, <type 'object'>
    """ ServiceHealthDataCollection() """
    pass

class ServiceHealthModel: # skipped bases: <type 'object'>, <type 'object'>
    """
    ServiceHealthModel()
    ServiceHealthModel(serviceHost: ServiceHostBase)
    ServiceHealthModel(serviceHost: ServiceHostBase, serviceStartTime: DateTimeOffset)
    """
    @property
    def ChannelDispatchers(self) -> Array:
        """ Get: ChannelDispatchers(self: ServiceHealthModel) -> Array[ChannelDispatcherModel] """
        ...

    @property
    def Date(self) -> DateTimeOffset:
        """ Get: Date(self: ServiceHealthModel) -> DateTimeOffset """
        ...

    @property
    def ProcessInformation(self): # -> ProcessInformationModel
        """ Get: ProcessInformation(self: ServiceHealthModel) -> ProcessInformationModel """
        ...

    @property
    def ProcessThreads(self): # -> ProcessThreadsModel
        """ Get: ProcessThreads(self: ServiceHealthModel) -> ProcessThreadsModel """
        ...

    @property
    def ServiceEndpoints(self) -> Array:
        """ Get: ServiceEndpoints(self: ServiceHealthModel) -> Array[ServiceEndpointModel] """
        ...

    @property
    def ServiceProperties(self): # -> ServicePropertiesModel
        """ Get: ServiceProperties(self: ServiceHealthModel) -> ServicePropertiesModel """
        ...


    def ChannelDispatcherModel(self, *args): #cannot find CLR method
        """
        ChannelDispatcherModel()
        ChannelDispatcherModel(channelDispatcher: ChannelDispatcherBase)
        """
        ...

    def CommunicationTimeoutsModel(self, *args): #cannot find CLR method
        """
        CommunicationTimeoutsModel()
        CommunicationTimeoutsModel(timeouts: IDefaultCommunicationTimeouts)
        """
        ...

    def ProcessInformationModel(self, *args): #cannot find CLR method
        """
        ProcessInformationModel()
        ProcessInformationModel(serviceHost: ServiceHostBase)
        """
        ...

    def ProcessThreadsModel(self, *args): #cannot find CLR method
        """ ProcessThreadsModel() """
        ...

    def ServiceEndpointModel(self, *args): #cannot find CLR method
        """
        ServiceEndpointModel()
        ServiceEndpointModel(endpoint: ServiceEndpoint)
        """
        ...

    def ServicePropertiesModel(self, *args): #cannot find CLR method
        """
        ServicePropertiesModel()
        ServicePropertiesModel(serviceHost: ServiceHostBase)
        """
        ...

    def ServiceThrottleModel(self, *args): #cannot find CLR method
        """
        ServiceThrottleModel()
        ServiceThrottleModel(serviceThrottle: ServiceThrottle)
        """
        ...

    Namespace: str = ...


class ServiceHealthSection(Collection): # skipped bases: <type 'IEnumerable[ServiceHealthDataCollection]'>, <type 'IList[ServiceHealthDataCollection]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IReadOnlyList[ServiceHealthDataCollection]'>, <type 'IReadOnlyCollection[ServiceHealthDataCollection]'>, <type 'ICollection[ServiceHealthDataCollection]'>, <type 'ICollection'>, <type 'object'>
    """
    ServiceHealthSection()
    ServiceHealthSection(title: str)
    """
    @property
    def BackgroundColor(self) -> str:
        """
        Get: BackgroundColor(self: ServiceHealthSection) -> str
        Set: BackgroundColor(self: ServiceHealthSection) = value
        """
        ...

    @property
    def ForegroundColor(self) -> str:
        """
        Get: ForegroundColor(self: ServiceHealthSection) -> str
        Set: ForegroundColor(self: ServiceHealthSection) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: ServiceHealthSection) -> str
        Set: Title(self: ServiceHealthSection) = value
        """
        ...


    def CreateElementsCollection(self) -> ServiceHealthDataCollection:
        """ CreateElementsCollection(self: ServiceHealthSection) -> ServiceHealthDataCollection """
        ...


class ServiceHealthSectionCollection(Collection): # skipped bases: <type 'ICollection[ServiceHealthSection]'>, <type 'IList[ServiceHealthSection]'>, <type 'IEnumerable'>, <type 'IReadOnlyCollection[ServiceHealthSection]'>, <type 'IList'>, <type 'IReadOnlyList[ServiceHealthSection]'>, <type 'IEnumerable[ServiceHealthSection]'>, <type 'ICollection'>, <type 'object'>
    """ ServiceHealthSectionCollection() """
    def CreateSection(self, title:str, backgroundColor:str = ..., foregroundColor:str = ...) -> ServiceHealthSection:
        """
        CreateSection(self: ServiceHealthSectionCollection, title: str) -> ServiceHealthSection
        CreateSection(self: ServiceHealthSectionCollection, title: str, backgroundColor: str) -> ServiceHealthSection
        CreateSection(self: ServiceHealthSectionCollection, title: str, backgroundColor: str, foregroundColor: str) -> ServiceHealthSection
        """
        ...


class ServiceMetadataBehavior(IServiceBehavior): # skipped bases: <type 'object'>
    """ ServiceMetadataBehavior() """
    @property
    def ExternalMetadataLocation(self) -> Uri:
        """
        Get: ExternalMetadataLocation(self: ServiceMetadataBehavior) -> Uri
        Set: ExternalMetadataLocation(self: ServiceMetadataBehavior) = value
        """
        ...

    @property
    def HttpGetBinding(self) -> Binding:
        """
        Get: HttpGetBinding(self: ServiceMetadataBehavior) -> Binding
        Set: HttpGetBinding(self: ServiceMetadataBehavior) = value
        """
        ...

    @property
    def HttpGetEnabled(self) -> bool:
        """
        Get: HttpGetEnabled(self: ServiceMetadataBehavior) -> bool
        Set: HttpGetEnabled(self: ServiceMetadataBehavior) = value
        """
        ...

    @property
    def HttpGetUrl(self) -> Uri:
        """
        Get: HttpGetUrl(self: ServiceMetadataBehavior) -> Uri
        Set: HttpGetUrl(self: ServiceMetadataBehavior) = value
        """
        ...

    @property
    def HttpsGetBinding(self) -> Binding:
        """
        Get: HttpsGetBinding(self: ServiceMetadataBehavior) -> Binding
        Set: HttpsGetBinding(self: ServiceMetadataBehavior) = value
        """
        ...

    @property
    def HttpsGetEnabled(self) -> bool:
        """
        Get: HttpsGetEnabled(self: ServiceMetadataBehavior) -> bool
        Set: HttpsGetEnabled(self: ServiceMetadataBehavior) = value
        """
        ...

    @property
    def HttpsGetUrl(self) -> Uri:
        """
        Get: HttpsGetUrl(self: ServiceMetadataBehavior) -> Uri
        Set: HttpsGetUrl(self: ServiceMetadataBehavior) = value
        """
        ...

    @property
    def MetadataExporter(self) -> MetadataExporter:
        """
        Get: MetadataExporter(self: ServiceMetadataBehavior) -> MetadataExporter
        Set: MetadataExporter(self: ServiceMetadataBehavior) = value
        """
        ...


    MexContractName: str = ...


class ServiceMetadataContractBehavior(IContractBehavior): # skipped bases: <type 'object'>
    """
    ServiceMetadataContractBehavior()
    ServiceMetadataContractBehavior(metadataGenerationDisabled: bool)
    """
    @property
    def MetadataGenerationDisabled(self) -> bool:
        """
        Get: MetadataGenerationDisabled(self: ServiceMetadataContractBehavior) -> bool
        Set: MetadataGenerationDisabled(self: ServiceMetadataContractBehavior) = value
        """
        ...



class ServiceMetadataEndpoint(ServiceEndpoint): # skipped bases: <type 'object'>
    """
    ServiceMetadataEndpoint()
    ServiceMetadataEndpoint(address: EndpointAddress)
    ServiceMetadataEndpoint(binding: Binding, address: EndpointAddress)
    """
    pass

class ServiceMetadataExtension(IExtension): # skipped bases: <type 'object'>
    """ ServiceMetadataExtension() """
    @property
    def Metadata(self) -> MetadataSet:
        """ Get: Metadata(self: ServiceMetadataExtension) -> MetadataSet """
        ...

    @property
    def SingleWsdl(self) -> ServiceDescription:
        """ Get: SingleWsdl(self: ServiceMetadataExtension) -> ServiceDescription """
        ...



class ServiceSecurityAuditBehavior(IServiceBehavior): # skipped bases: <type 'object'>
    """ ServiceSecurityAuditBehavior() """
    @property
    def AuditLogLocation(self) -> AuditLogLocation:
        """
        Get: AuditLogLocation(self: ServiceSecurityAuditBehavior) -> AuditLogLocation
        Set: AuditLogLocation(self: ServiceSecurityAuditBehavior) = value
        """
        ...

    @property
    def MessageAuthenticationAuditLevel(self) -> AuditLevel:
        """
        Get: MessageAuthenticationAuditLevel(self: ServiceSecurityAuditBehavior) -> AuditLevel
        Set: MessageAuthenticationAuditLevel(self: ServiceSecurityAuditBehavior) = value
        """
        ...

    @property
    def ServiceAuthorizationAuditLevel(self) -> AuditLevel:
        """
        Get: ServiceAuthorizationAuditLevel(self: ServiceSecurityAuditBehavior) -> AuditLevel
        Set: ServiceAuthorizationAuditLevel(self: ServiceSecurityAuditBehavior) = value
        """
        ...

    @property
    def SuppressAuditFailure(self) -> bool:
        """
        Get: SuppressAuditFailure(self: ServiceSecurityAuditBehavior) -> bool
        Set: SuppressAuditFailure(self: ServiceSecurityAuditBehavior) = value
        """
        ...



class ServiceThrottlingBehavior(IServiceBehavior): # skipped bases: <type 'object'>
    """ ServiceThrottlingBehavior() """
    @property
    def MaxConcurrentCalls(self) -> int:
        """
        Get: MaxConcurrentCalls(self: ServiceThrottlingBehavior) -> int
        Set: MaxConcurrentCalls(self: ServiceThrottlingBehavior) = value
        """
        ...

    @property
    def MaxConcurrentInstances(self) -> int:
        """
        Get: MaxConcurrentInstances(self: ServiceThrottlingBehavior) -> int
        Set: MaxConcurrentInstances(self: ServiceThrottlingBehavior) = value
        """
        ...

    @property
    def MaxConcurrentSessions(self) -> int:
        """
        Get: MaxConcurrentSessions(self: ServiceThrottlingBehavior) -> int
        Set: MaxConcurrentSessions(self: ServiceThrottlingBehavior) = value
        """
        ...



class SynchronousReceiveBehavior(IEndpointBehavior): # skipped bases: <type 'object'>
    """ SynchronousReceiveBehavior() """
    pass

class TransactedBatchingBehavior(IEndpointBehavior): # skipped bases: <type 'object'>
    """ TransactedBatchingBehavior(maxBatchSize: int) """
    @property
    def MaxBatchSize(self) -> int:
        """
        Get: MaxBatchSize(self: TransactedBatchingBehavior) -> int
        Set: MaxBatchSize(self: TransactedBatchingBehavior) = value
        """
        ...



class TypedMessageConverter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Create(messageContract:Type, action:str, *__args:str) -> TypedMessageConverter:
        """
        Create(messageContract: Type, action: str) -> TypedMessageConverter
        Create(messageContract: Type, action: str, defaultNamespace: str) -> TypedMessageConverter
        Create(messageContract: Type, action: str, formatterAttribute: XmlSerializerFormatAttribute) -> TypedMessageConverter
        Create(messageContract: Type, action: str, formatterAttribute: DataContractFormatAttribute) -> TypedMessageConverter
        Create(messageContract: Type, action: str, defaultNamespace: str, formatterAttribute: XmlSerializerFormatAttribute) -> TypedMessageConverter
        Create(messageContract: Type, action: str, defaultNamespace: str, formatterAttribute: DataContractFormatAttribute) -> TypedMessageConverter
        """
        ...

    def FromMessage(self, message:Message) -> object:
        """ FromMessage(self: TypedMessageConverter, message: Message) -> object """
        ...

    def ToMessage(self, typedMessage:object, version = ...) -> Message: # Not found arg types: {'version': 'MessageVersion'}
        """
        ToMessage(self: TypedMessageConverter, typedMessage: object) -> Message
        ToMessage(self: TypedMessageConverter, typedMessage: object, version: MessageVersion) -> Message
        """
        ...


class UnknownExceptionAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UnknownExceptionAction, values: AbortInstance (1), TerminateInstance (0) """
    AbortInstance: UnknownExceptionAction = ...
    TerminateInstance: UnknownExceptionAction = ...
    value__ = ...


class UseRequestHeadersForMetadataAddressBehavior(IServiceBehavior): # skipped bases: <type 'object'>
    """ UseRequestHeadersForMetadataAddressBehavior() """
    @property
    def DefaultPortsByScheme(self) -> IDictionary:
        """ Get: DefaultPortsByScheme(self: UseRequestHeadersForMetadataAddressBehavior) -> IDictionary[str, int] """
        ...



class WebHttpBehavior(IWmiInstanceProvider, IEndpointBehavior): # skipped bases: <type 'object'>
    """ WebHttpBehavior() """
    @property
    def AutomaticFormatSelectionEnabled(self) -> bool:
        """
        Get: AutomaticFormatSelectionEnabled(self: WebHttpBehavior) -> bool
        Set: AutomaticFormatSelectionEnabled(self: WebHttpBehavior) = value
        """
        ...

    @property
    def DefaultBodyStyle(self) -> WebMessageBodyStyle:
        """
        Get: DefaultBodyStyle(self: WebHttpBehavior) -> WebMessageBodyStyle
        Set: DefaultBodyStyle(self: WebHttpBehavior) = value
        """
        ...

    @property
    def DefaultOutgoingRequestFormat(self) -> WebMessageFormat:
        """
        Get: DefaultOutgoingRequestFormat(self: WebHttpBehavior) -> WebMessageFormat
        Set: DefaultOutgoingRequestFormat(self: WebHttpBehavior) = value
        """
        ...

    @property
    def DefaultOutgoingResponseFormat(self) -> WebMessageFormat:
        """
        Get: DefaultOutgoingResponseFormat(self: WebHttpBehavior) -> WebMessageFormat
        Set: DefaultOutgoingResponseFormat(self: WebHttpBehavior) = value
        """
        ...

    @property
    def FaultExceptionEnabled(self) -> bool:
        """
        Get: FaultExceptionEnabled(self: WebHttpBehavior) -> bool
        Set: FaultExceptionEnabled(self: WebHttpBehavior) = value
        """
        ...

    @property
    def HelpEnabled(self) -> bool:
        """
        Get: HelpEnabled(self: WebHttpBehavior) -> bool
        Set: HelpEnabled(self: WebHttpBehavior) = value
        """
        ...

    @property
    def JavascriptCallbackParameterName(self):
        ...


    def AddClientErrorInspector(self, *args): #cannot find CLR method
        """ AddClientErrorInspector(self: WebHttpBehavior, endpoint: ServiceEndpoint, clientRuntime: ClientRuntime) """
        ...

    def AddServerErrorHandlers(self, *args): #cannot find CLR method
        """ AddServerErrorHandlers(self: WebHttpBehavior, endpoint: ServiceEndpoint, endpointDispatcher: EndpointDispatcher) """
        ...

    def GetOperationSelector(self, *args): #cannot find CLR method
        """ GetOperationSelector(self: WebHttpBehavior, endpoint: ServiceEndpoint) -> WebHttpDispatchOperationSelector """
        ...

    def GetQueryStringConverter(self, *args): #cannot find CLR method
        """ GetQueryStringConverter(self: WebHttpBehavior, operationDescription: OperationDescription) -> QueryStringConverter """
        ...

    def GetReplyClientFormatter(self, *args): #cannot find CLR method
        """ GetReplyClientFormatter(self: WebHttpBehavior, operationDescription: OperationDescription, endpoint: ServiceEndpoint) -> IClientMessageFormatter """
        ...

    def GetReplyDispatchFormatter(self, *args): #cannot find CLR method
        """ GetReplyDispatchFormatter(self: WebHttpBehavior, operationDescription: OperationDescription, endpoint: ServiceEndpoint) -> IDispatchMessageFormatter """
        ...

    def GetRequestClientFormatter(self, *args): #cannot find CLR method
        """ GetRequestClientFormatter(self: WebHttpBehavior, operationDescription: OperationDescription, endpoint: ServiceEndpoint) -> IClientMessageFormatter """
        ...

    def GetRequestDispatchFormatter(self, *args): #cannot find CLR method
        """ GetRequestDispatchFormatter(self: WebHttpBehavior, operationDescription: OperationDescription, endpoint: ServiceEndpoint) -> IDispatchMessageFormatter """
        ...

    def ValidateBinding(self, *args): #cannot find CLR method
        """ ValidateBinding(self: WebHttpBehavior, endpoint: ServiceEndpoint) """
        ...


class WebServiceEndpoint(ServiceEndpoint): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ContentTypeMapper(self) -> WebContentTypeMapper:
        """
        Get: ContentTypeMapper(self: WebServiceEndpoint) -> WebContentTypeMapper
        Set: ContentTypeMapper(self: WebServiceEndpoint) = value
        """
        ...

    @property
    def CrossDomainScriptAccessEnabled(self) -> bool:
        """
        Get: CrossDomainScriptAccessEnabled(self: WebServiceEndpoint) -> bool
        Set: CrossDomainScriptAccessEnabled(self: WebServiceEndpoint) = value
        """
        ...

    @property
    def HostNameComparisonMode(self) -> HostNameComparisonMode:
        """
        Get: HostNameComparisonMode(self: WebServiceEndpoint) -> HostNameComparisonMode
        Set: HostNameComparisonMode(self: WebServiceEndpoint) = value
        """
        ...

    @property
    def MaxBufferPoolSize(self) -> Int64:
        """
        Get: MaxBufferPoolSize(self: WebServiceEndpoint) -> Int64
        Set: MaxBufferPoolSize(self: WebServiceEndpoint) = value
        """
        ...

    @property
    def MaxBufferSize(self) -> int:
        """
        Get: MaxBufferSize(self: WebServiceEndpoint) -> int
        Set: MaxBufferSize(self: WebServiceEndpoint) = value
        """
        ...

    @property
    def MaxReceivedMessageSize(self) -> Int64:
        """
        Get: MaxReceivedMessageSize(self: WebServiceEndpoint) -> Int64
        Set: MaxReceivedMessageSize(self: WebServiceEndpoint) = value
        """
        ...

    @property
    def ReaderQuotas(self) -> XmlDictionaryReaderQuotas:
        """
        Get: ReaderQuotas(self: WebServiceEndpoint) -> XmlDictionaryReaderQuotas
        Set: ReaderQuotas(self: WebServiceEndpoint) = value
        """
        ...

    @property
    def Security(self) -> WebHttpSecurity:
        """ Get: Security(self: WebServiceEndpoint) -> WebHttpSecurity """
        ...

    @property
    def TransferMode(self) -> TransferMode:
        """
        Get: TransferMode(self: WebServiceEndpoint) -> TransferMode
        Set: TransferMode(self: WebServiceEndpoint) = value
        """
        ...

    @property
    def WebEndpointType(self):
        ...

    @property
    def WriteEncoding(self) -> Encoding:
        """
        Get: WriteEncoding(self: WebServiceEndpoint) -> Encoding
        Set: WriteEncoding(self: WebServiceEndpoint) = value
        """
        ...



class WebHttpEndpoint(WebServiceEndpoint): # skipped bases: <type 'object'>
    """
    WebHttpEndpoint(contract: ContractDescription)
    WebHttpEndpoint(contract: ContractDescription, address: EndpointAddress)
    """
    @property
    def AutomaticFormatSelectionEnabled(self) -> bool:
        """
        Get: AutomaticFormatSelectionEnabled(self: WebHttpEndpoint) -> bool
        Set: AutomaticFormatSelectionEnabled(self: WebHttpEndpoint) = value
        """
        ...

    @property
    def DefaultOutgoingResponseFormat(self) -> WebMessageFormat:
        """
        Get: DefaultOutgoingResponseFormat(self: WebHttpEndpoint) -> WebMessageFormat
        Set: DefaultOutgoingResponseFormat(self: WebHttpEndpoint) = value
        """
        ...

    @property
    def FaultExceptionEnabled(self) -> bool:
        """
        Get: FaultExceptionEnabled(self: WebHttpEndpoint) -> bool
        Set: FaultExceptionEnabled(self: WebHttpEndpoint) = value
        """
        ...

    @property
    def HelpEnabled(self) -> bool:
        """
        Get: HelpEnabled(self: WebHttpEndpoint) -> bool
        Set: HelpEnabled(self: WebHttpEndpoint) = value
        """
        ...


    def __new__(cls, contract:ContractDescription, address:EndpointAddress = ...) -> Self:
        """
        __new__(cls: type, contract: ContractDescription)
        __new__(cls: type, contract: ContractDescription, address: EndpointAddress)
        """
        ...


class WebScriptEnablingBehavior(WebHttpBehavior): # skipped bases: <type 'IEndpointBehavior'>, <type 'IWmiInstanceProvider'>, <type 'object'>
    """ WebScriptEnablingBehavior() """
    pass

class WebScriptEndpoint(WebServiceEndpoint): # skipped bases: <type 'object'>
    """
    WebScriptEndpoint(contract: ContractDescription)
    WebScriptEndpoint(contract: ContractDescription, address: EndpointAddress)
    """
    def __new__(cls, contract:ContractDescription, address:EndpointAddress = ...) -> Self:
        """
        __new__(cls: type, contract: ContractDescription)
        __new__(cls: type, contract: ContractDescription, address: EndpointAddress)
        """
        ...


class WorkflowRuntimeBehavior(IServiceBehavior, IWmiInstanceProvider): # skipped bases: <type 'object'>
    """ WorkflowRuntimeBehavior() """
    @property
    def CachedInstanceExpiration(self) -> TimeSpan:
        """
        Get: CachedInstanceExpiration(self: WorkflowRuntimeBehavior) -> TimeSpan
        Set: CachedInstanceExpiration(self: WorkflowRuntimeBehavior) = value
        """
        ...

    @property
    def WorkflowRuntime(self) -> WorkflowRuntime:
        """ Get: WorkflowRuntime(self: WorkflowRuntimeBehavior) -> WorkflowRuntime """
        ...



class WsdlContractConversionContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Contract(self) -> ContractDescription:
        """ Get: Contract(self: WsdlContractConversionContext) -> ContractDescription """
        ...

    @property
    def WsdlPortType(self) -> PortType:
        """ Get: WsdlPortType(self: WsdlContractConversionContext) -> PortType """
        ...


    def GetFaultDescription(self, operationFault:OperationFault) -> FaultDescription:
        """ GetFaultDescription(self: WsdlContractConversionContext, operationFault: OperationFault) -> FaultDescription """
        ...

    def GetMessageDescription(self, operationMessage:OperationMessage) -> MessageDescription:
        """ GetMessageDescription(self: WsdlContractConversionContext, operationMessage: OperationMessage) -> MessageDescription """
        ...

    def GetOperation(self, operation:OperationDescription) -> Operation:
        """ GetOperation(self: WsdlContractConversionContext, operation: OperationDescription) -> Operation """
        ...

    def GetOperationDescription(self, operation:Operation) -> OperationDescription:
        """ GetOperationDescription(self: WsdlContractConversionContext, operation: Operation) -> OperationDescription """
        ...

    def GetOperationFault(self, fault:FaultDescription) -> OperationFault:
        """ GetOperationFault(self: WsdlContractConversionContext, fault: FaultDescription) -> OperationFault """
        ...

    def GetOperationMessage(self, message:MessageDescription) -> OperationMessage:
        """ GetOperationMessage(self: WsdlContractConversionContext, message: MessageDescription) -> OperationMessage """
        ...


class WsdlEndpointConversionContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ContractConversionContext(self) -> WsdlContractConversionContext:
        """ Get: ContractConversionContext(self: WsdlEndpointConversionContext) -> WsdlContractConversionContext """
        ...

    @property
    def Endpoint(self) -> ServiceEndpoint:
        """ Get: Endpoint(self: WsdlEndpointConversionContext) -> ServiceEndpoint """
        ...

    @property
    def WsdlBinding(self) -> Binding:
        """ Get: WsdlBinding(self: WsdlEndpointConversionContext) -> Binding """
        ...

    @property
    def WsdlPort(self) -> Port:
        """ Get: WsdlPort(self: WsdlEndpointConversionContext) -> Port """
        ...


    def GetFaultBinding(self, fault:FaultDescription) -> FaultBinding:
        """ GetFaultBinding(self: WsdlEndpointConversionContext, fault: FaultDescription) -> FaultBinding """
        ...

    def GetFaultDescription(self, faultBinding:FaultBinding) -> FaultDescription:
        """ GetFaultDescription(self: WsdlEndpointConversionContext, faultBinding: FaultBinding) -> FaultDescription """
        ...

    def GetMessageBinding(self, message:MessageDescription) -> MessageBinding:
        """ GetMessageBinding(self: WsdlEndpointConversionContext, message: MessageDescription) -> MessageBinding """
        ...

    def GetMessageDescription(self, messageBinding:MessageBinding) -> MessageDescription:
        """ GetMessageDescription(self: WsdlEndpointConversionContext, messageBinding: MessageBinding) -> MessageDescription """
        ...

    def GetOperationBinding(self, operation:OperationDescription) -> OperationBinding:
        """ GetOperationBinding(self: WsdlEndpointConversionContext, operation: OperationDescription) -> OperationBinding """
        ...

    def GetOperationDescription(self, operationBinding:OperationBinding) -> OperationDescription:
        """ GetOperationDescription(self: WsdlEndpointConversionContext, operationBinding: OperationBinding) -> OperationDescription """
        ...


class WsdlExporter(MetadataExporter): # skipped bases: <type 'object'>
    """ WsdlExporter() """
    @property
    def GeneratedWsdlDocuments(self) -> ServiceDescriptionCollection:
        """ Get: GeneratedWsdlDocuments(self: WsdlExporter) -> ServiceDescriptionCollection """
        ...

    @property
    def GeneratedXmlSchemas(self) -> XmlSchemaSet:
        """ Get: GeneratedXmlSchemas(self: WsdlExporter) -> XmlSchemaSet """
        ...


    def ExportEndpoints(self, endpoints:IEnumerable, wsdlServiceQName:XmlQualifiedName): # -> 
        """ ExportEndpoints(self: WsdlExporter, endpoints: IEnumerable[ServiceEndpoint], wsdlServiceQName: XmlQualifiedName) """
        ...


class WsdlImporter(MetadataImporter): # skipped bases: <type 'object'>
    """
    WsdlImporter(metadata: MetadataSet)
    WsdlImporter(metadata: MetadataSet, policyImportExtensions: IEnumerable[IPolicyImportExtension], wsdlImportExtensions: IEnumerable[IWsdlImportExtension])
    WsdlImporter(metadata: MetadataSet, policyImportExtensions: IEnumerable[IPolicyImportExtension], wsdlImportExtensions: IEnumerable[IWsdlImportExtension], quotas: MetadataImporterQuotas)
    """
    @property
    def WsdlDocuments(self) -> ServiceDescriptionCollection:
        """ Get: WsdlDocuments(self: WsdlImporter) -> ServiceDescriptionCollection """
        ...

    @property
    def WsdlImportExtensions(self) -> KeyedByTypeCollection:
        """ Get: WsdlImportExtensions(self: WsdlImporter) -> KeyedByTypeCollection[IWsdlImportExtension] """
        ...

    @property
    def XmlSchemas(self) -> XmlSchemaSet:
        """ Get: XmlSchemas(self: WsdlImporter) -> XmlSchemaSet """
        ...


    def ImportAllBindings(self) -> Collection:
        """ ImportAllBindings(self: WsdlImporter) -> Collection[Binding] """
        ...

    def ImportBinding(self, wsdlBinding:Binding) -> Binding:
        """ ImportBinding(self: WsdlImporter, wsdlBinding: Binding) -> Binding """
        ...

    def ImportContract(self, wsdlPortType:PortType) -> ContractDescription:
        """ ImportContract(self: WsdlImporter, wsdlPortType: PortType) -> ContractDescription """
        ...

    def ImportEndpoint(self, wsdlPort:Port) -> ServiceEndpoint:
        """ ImportEndpoint(self: WsdlImporter, wsdlPort: Port) -> ServiceEndpoint """
        ...

    def ImportEndpoints(self, *__args:PortType) -> ServiceEndpointCollection:
        """
        ImportEndpoints(self: WsdlImporter, wsdlPortType: PortType) -> ServiceEndpointCollection
        ImportEndpoints(self: WsdlImporter, wsdlBinding: Binding) -> ServiceEndpointCollection
        ImportEndpoints(self: WsdlImporter, wsdlService: Service) -> ServiceEndpointCollection
        """
        ...

    def __new__(cls, metadata:MetadataSet, policyImportExtensions:IEnumerable = ..., wsdlImportExtensions:IEnumerable = ..., quotas:MetadataImporterQuotas = ...) -> Self:
        """
        __new__(cls: type, metadata: MetadataSet)
        __new__(cls: type, metadata: MetadataSet, policyImportExtensions: IEnumerable[IPolicyImportExtension], wsdlImportExtensions: IEnumerable[IWsdlImportExtension])
        __new__(cls: type, metadata: MetadataSet, policyImportExtensions: IEnumerable[IPolicyImportExtension], wsdlImportExtensions: IEnumerable[IWsdlImportExtension], quotas: MetadataImporterQuotas)
        """
        ...


class XmlSerializerMessageContractImporter(IWsdlImportExtension): # skipped bases: <type 'object'>
    """ XmlSerializerMessageContractImporter() """
    pass

class XmlSerializerOperationBehavior(IOperationBehavior, IWsdlExportExtension): # skipped bases: <type 'object'>
    """
    XmlSerializerOperationBehavior(operation: OperationDescription)
    XmlSerializerOperationBehavior(operation: OperationDescription, attribute: XmlSerializerFormatAttribute)
    """
    @property
    def XmlSerializerFormatAttribute(self) -> XmlSerializerFormatAttribute:
        """ Get: XmlSerializerFormatAttribute(self: XmlSerializerOperationBehavior) -> XmlSerializerFormatAttribute """
        ...


    def GetXmlMappings(self) -> Collection:
        """ GetXmlMappings(self: XmlSerializerOperationBehavior) -> Collection[XmlMapping] """
        ...


