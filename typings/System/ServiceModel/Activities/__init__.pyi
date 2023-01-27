# encoding: utf-8
# module System.ServiceModel.Activities calls itself Activities
# from System.ServiceModel.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.WorkflowServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Enum, Guid, IAsyncResult, 
    IDisposable, Nullable, TimeSpan, Type, Uri)

from System.Activities import (Bookmark, ExecutionProperties, Handle, 
    InArgument, NativeActivity, OutArgument, WorkflowIdentity)

from System.Activities.Debugger import IDebuggableWorkflowTree

from System.Activities.Hosting import WorkflowInstanceExtensionManager

from System.Activities.Validation import (ValidationResults, 
    ValidationSettings)

from System.Collections import ICollection, IDictionary, IEnumerable

from System.Collections.ObjectModel import Collection

from System.EnterpriseServices import Activity

from System.Messaging import Message

from System.Runtime.DurableInstancing import InstanceKey, InstanceStore

from System.Security.Principal import TokenImpersonationLevel

from System.ServiceModel import (ClientBase, Endpoint, MessageQuerySet, 
    OperationContext, ServiceHostBase)

from System.Xml.Linq import XName

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, ICancelable, 
    IDurableInstancingOptions, OperationDescription, ServiceEndpoint, field#)
"""

# no functions
# classes

class CorrelationInitializer: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CorrelationHandle(self) -> InArgument:
        """
        Get: CorrelationHandle(self: CorrelationInitializer) -> InArgument[CorrelationHandle]
        Set: CorrelationHandle(self: CorrelationInitializer) = value
        """
        ...



class CallbackCorrelationInitializer(CorrelationInitializer): # skipped bases: <type 'object'>
    """ CallbackCorrelationInitializer() """
    pass

class ChannelCacheSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ ChannelCacheSettings() """
    @property
    def IdleTimeout(self) -> TimeSpan:
        """
        Get: IdleTimeout(self: ChannelCacheSettings) -> TimeSpan
        Set: IdleTimeout(self: ChannelCacheSettings) = value
        """
        ...

    @property
    def LeaseTimeout(self) -> TimeSpan:
        """
        Get: LeaseTimeout(self: ChannelCacheSettings) -> TimeSpan
        Set: LeaseTimeout(self: ChannelCacheSettings) = value
        """
        ...

    @property
    def MaxItemsInCache(self) -> int:
        """
        Get: MaxItemsInCache(self: ChannelCacheSettings) -> int
        Set: MaxItemsInCache(self: ChannelCacheSettings) = value
        """
        ...



class ContextCorrelationInitializer(CorrelationInitializer): # skipped bases: <type 'object'>
    """ ContextCorrelationInitializer() """
    pass

class CorrelationHandle(Handle): # skipped bases: <type 'object'>
    """ CorrelationHandle() """
    pass

class CorrelationScope(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ CorrelationScope() """
    @property
    def Body(self) -> Activity:
        """
        Get: Body(self: CorrelationScope) -> Activity
        Set: Body(self: CorrelationScope) = value
        """
        ...

    @property
    def CorrelatesWith(self) -> InArgument:
        """
        Get: CorrelatesWith(self: CorrelationScope) -> InArgument[CorrelationHandle]
        Set: CorrelatesWith(self: CorrelationScope) = value
        """
        ...


    def ShouldSerializeCorrelatesWith(self) -> bool:
        """ ShouldSerializeCorrelatesWith(self: CorrelationScope) -> bool """
        ...


class DurableInstancingOptions(IDurableInstancingOptions): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def InstanceStore(self) -> InstanceStore:
        """
        Get: InstanceStore(self: DurableInstancingOptions) -> InstanceStore
        Set: InstanceStore(self: DurableInstancingOptions) = value
        """
        ...


    def AddInitialInstanceValues(self, writeOnlyValues:IDictionary): # -> 
        """ AddInitialInstanceValues(self: DurableInstancingOptions, writeOnlyValues: IDictionary[XName, object]) """
        ...

    def AddInstanceOwnerValues(self, readWriteValues:IDictionary, writeOnlyValues:IDictionary): # -> 
        """ AddInstanceOwnerValues(self: DurableInstancingOptions, readWriteValues: IDictionary[XName, object], writeOnlyValues: IDictionary[XName, object]) """
        ...


class HostSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ HostSettings() """
    @property
    def IncludeExceptionDetailInFaults(self) -> bool:
        """
        Get: IncludeExceptionDetailInFaults(self: HostSettings) -> bool
        Set: IncludeExceptionDetailInFaults(self: HostSettings) = value
        """
        ...

    @property
    def ScopeName(self) -> XName:
        """
        Get: ScopeName(self: HostSettings) -> XName
        Set: ScopeName(self: HostSettings) = value
        """
        ...

    @property
    def UseNoPersistHandle(self) -> bool:
        """
        Get: UseNoPersistHandle(self: HostSettings) -> bool
        Set: UseNoPersistHandle(self: HostSettings) = value
        """
        ...



class InitializeCorrelation(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ InitializeCorrelation() """
    @property
    def Correlation(self) -> InArgument:
        """
        Get: Correlation(self: InitializeCorrelation) -> InArgument[CorrelationHandle]
        Set: Correlation(self: InitializeCorrelation) = value
        """
        ...

    @property
    def CorrelationData(self) -> IDictionary:
        """ Get: CorrelationData(self: InitializeCorrelation) -> IDictionary[str, InArgument[str]] """
        ...



class IReceiveMessageCallback: # skipped bases: <type 'object'>
    """ no doc """
    def OnReceiveMessage(self, operationContext:OperationContext, activityExecutionProperties:ExecutionProperties): # -> 
        """ OnReceiveMessage(self: IReceiveMessageCallback, operationContext: OperationContext, activityExecutionProperties: ExecutionProperties) """
        ...


class ISendMessageCallback: # skipped bases: <type 'object'>
    """ no doc """
    def OnSendMessage(self, operationContext:OperationContext): # -> 
        """ OnSendMessage(self: ISendMessageCallback, operationContext: OperationContext) """
        ...


class IWorkflowInstanceManagement: # skipped bases: <type 'object'>
    """ no doc """
    def Abandon(self, instanceId:Guid, reason:str): # -> 
        """ Abandon(self: IWorkflowInstanceManagement, instanceId: Guid, reason: str) """
        ...

    def BeginAbandon(self, instanceId:Guid, reason:str, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginAbandon(self: IWorkflowInstanceManagement, instanceId: Guid, reason: str, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginCancel(self, instanceId:Guid, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginCancel(self: IWorkflowInstanceManagement, instanceId: Guid, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginRun(self, instanceId:Guid, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginRun(self: IWorkflowInstanceManagement, instanceId: Guid, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginSuspend(self, instanceId:Guid, reason:str, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginSuspend(self: IWorkflowInstanceManagement, instanceId: Guid, reason: str, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTerminate(self, instanceId:Guid, reason:str, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTerminate(self: IWorkflowInstanceManagement, instanceId: Guid, reason: str, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTransactedCancel(self, instanceId:Guid, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTransactedCancel(self: IWorkflowInstanceManagement, instanceId: Guid, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTransactedRun(self, instanceId:Guid, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTransactedRun(self: IWorkflowInstanceManagement, instanceId: Guid, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTransactedSuspend(self, instanceId:Guid, reason:str, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTransactedSuspend(self: IWorkflowInstanceManagement, instanceId: Guid, reason: str, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTransactedTerminate(self, instanceId:Guid, reason:str, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTransactedTerminate(self: IWorkflowInstanceManagement, instanceId: Guid, reason: str, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTransactedUnsuspend(self, instanceId:Guid, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTransactedUnsuspend(self: IWorkflowInstanceManagement, instanceId: Guid, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginUnsuspend(self, instanceId:Guid, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginUnsuspend(self: IWorkflowInstanceManagement, instanceId: Guid, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def Cancel(self, instanceId:Guid): # -> 
        """ Cancel(self: IWorkflowInstanceManagement, instanceId: Guid) """
        ...

    def EndAbandon(self, result:IAsyncResult): # -> 
        """ EndAbandon(self: IWorkflowInstanceManagement, result: IAsyncResult) """
        ...

    def EndCancel(self, result:IAsyncResult): # -> 
        """ EndCancel(self: IWorkflowInstanceManagement, result: IAsyncResult) """
        ...

    def EndRun(self, result:IAsyncResult): # -> 
        """ EndRun(self: IWorkflowInstanceManagement, result: IAsyncResult) """
        ...

    def EndSuspend(self, result:IAsyncResult): # -> 
        """ EndSuspend(self: IWorkflowInstanceManagement, result: IAsyncResult) """
        ...

    def EndTerminate(self, result:IAsyncResult): # -> 
        """ EndTerminate(self: IWorkflowInstanceManagement, result: IAsyncResult) """
        ...

    def EndTransactedCancel(self, result:IAsyncResult): # -> 
        """ EndTransactedCancel(self: IWorkflowInstanceManagement, result: IAsyncResult) """
        ...

    def EndTransactedRun(self, result:IAsyncResult): # -> 
        """ EndTransactedRun(self: IWorkflowInstanceManagement, result: IAsyncResult) """
        ...

    def EndTransactedSuspend(self, result:IAsyncResult): # -> 
        """ EndTransactedSuspend(self: IWorkflowInstanceManagement, result: IAsyncResult) """
        ...

    def EndTransactedTerminate(self, result:IAsyncResult): # -> 
        """ EndTransactedTerminate(self: IWorkflowInstanceManagement, result: IAsyncResult) """
        ...

    def EndTransactedUnsuspend(self, result:IAsyncResult): # -> 
        """ EndTransactedUnsuspend(self: IWorkflowInstanceManagement, result: IAsyncResult) """
        ...

    def EndUnsuspend(self, result:IAsyncResult): # -> 
        """ EndUnsuspend(self: IWorkflowInstanceManagement, result: IAsyncResult) """
        ...

    def Run(self, instanceId:Guid): # -> 
        """ Run(self: IWorkflowInstanceManagement, instanceId: Guid) """
        ...

    def Suspend(self, instanceId:Guid, reason:str): # -> 
        """ Suspend(self: IWorkflowInstanceManagement, instanceId: Guid, reason: str) """
        ...

    def Terminate(self, instanceId:Guid, reason:str): # -> 
        """ Terminate(self: IWorkflowInstanceManagement, instanceId: Guid, reason: str) """
        ...

    def TransactedCancel(self, instanceId:Guid): # -> 
        """ TransactedCancel(self: IWorkflowInstanceManagement, instanceId: Guid) """
        ...

    def TransactedRun(self, instanceId:Guid): # -> 
        """ TransactedRun(self: IWorkflowInstanceManagement, instanceId: Guid) """
        ...

    def TransactedSuspend(self, instanceId:Guid, reason:str): # -> 
        """ TransactedSuspend(self: IWorkflowInstanceManagement, instanceId: Guid, reason: str) """
        ...

    def TransactedTerminate(self, instanceId:Guid, reason:str): # -> 
        """ TransactedTerminate(self: IWorkflowInstanceManagement, instanceId: Guid, reason: str) """
        ...

    def TransactedUnsuspend(self, instanceId:Guid): # -> 
        """ TransactedUnsuspend(self: IWorkflowInstanceManagement, instanceId: Guid) """
        ...

    def Unsuspend(self, instanceId:Guid): # -> 
        """ Unsuspend(self: IWorkflowInstanceManagement, instanceId: Guid) """
        ...


class IWorkflowUpdateableInstanceManagement(IWorkflowInstanceManagement): # skipped bases: <type 'object'>
    """ no doc """
    def BeginTransactedUpdate(self, instanceId:Guid, updatedDefinitionIdentity:WorkflowIdentity, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginTransactedUpdate(self: IWorkflowUpdateableInstanceManagement, instanceId: Guid, updatedDefinitionIdentity: WorkflowIdentity, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginUpdate(self, instanceId:Guid, updatedDefinitionIdentity:WorkflowIdentity, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginUpdate(self: IWorkflowUpdateableInstanceManagement, instanceId: Guid, updatedDefinitionIdentity: WorkflowIdentity, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndTransactedUpdate(self, result:IAsyncResult): # -> 
        """ EndTransactedUpdate(self: IWorkflowUpdateableInstanceManagement, result: IAsyncResult) """
        ...

    def EndUpdate(self, result:IAsyncResult): # -> 
        """ EndUpdate(self: IWorkflowUpdateableInstanceManagement, result: IAsyncResult) """
        ...

    def TransactedUpdate(self, instanceId:Guid, updatedDefinitionIdentity:WorkflowIdentity): # -> 
        """ TransactedUpdate(self: IWorkflowUpdateableInstanceManagement, instanceId: Guid, updatedDefinitionIdentity: WorkflowIdentity) """
        ...

    def Update(self, instanceId:Guid, updatedDefinitionIdentity:WorkflowIdentity): # -> 
        """ Update(self: IWorkflowUpdateableInstanceManagement, instanceId: Guid, updatedDefinitionIdentity: WorkflowIdentity) """
        ...


class MessageContext: # skipped bases: <type 'object'>, <type 'object'>
    """ MessageContext() """
    @property
    def EndToEndTracingId(self) -> Guid:
        """
        Get: EndToEndTracingId(self: MessageContext) -> Guid
        Set: EndToEndTracingId(self: MessageContext) = value
        """
        ...

    @property
    def Message(self) -> Message:
        """
        Get: Message(self: MessageContext) -> Message
        Set: Message(self: MessageContext) = value
        """
        ...



class QueryCorrelationInitializer(CorrelationInitializer): # skipped bases: <type 'object'>
    """ QueryCorrelationInitializer() """
    @property
    def MessageQuerySet(self) -> MessageQuerySet:
        """
        Get: MessageQuerySet(self: QueryCorrelationInitializer) -> MessageQuerySet
        Set: MessageQuerySet(self: QueryCorrelationInitializer) = value
        """
        ...



class Receive(Activity): # skipped bases: <type 'object'>
    """ Receive() """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: Receive) -> str
        Set: Action(self: Receive) = value
        """
        ...

    @property
    def CanCreateInstance(self) -> bool:
        """
        Get: CanCreateInstance(self: Receive) -> bool
        Set: CanCreateInstance(self: Receive) = value
        """
        ...

    @property
    def Content(self) -> ReceiveContent:
        """
        Get: Content(self: Receive) -> ReceiveContent
        Set: Content(self: Receive) = value
        """
        ...

    @property
    def CorrelatesOn(self) -> MessageQuerySet:
        """
        Get: CorrelatesOn(self: Receive) -> MessageQuerySet
        Set: CorrelatesOn(self: Receive) = value
        """
        ...

    @property
    def CorrelatesWith(self) -> InArgument:
        """
        Get: CorrelatesWith(self: Receive) -> InArgument[CorrelationHandle]
        Set: CorrelatesWith(self: Receive) = value
        """
        ...

    @property
    def CorrelationInitializers(self) -> Collection:
        """ Get: CorrelationInitializers(self: Receive) -> Collection[CorrelationInitializer] """
        ...

    @property
    def KnownTypes(self) -> Collection:
        """ Get: KnownTypes(self: Receive) -> Collection[Type] """
        ...

    @property
    def OperationName(self) -> str:
        """
        Get: OperationName(self: Receive) -> str
        Set: OperationName(self: Receive) = value
        """
        ...

    @property
    def ProtectionLevel(self) -> Nullable:
        """
        Get: ProtectionLevel(self: Receive) -> Nullable[ProtectionLevel]
        Set: ProtectionLevel(self: Receive) = value
        """
        ...

    @property
    def SerializerOption(self) -> SerializerOption:
        """
        Get: SerializerOption(self: Receive) -> SerializerOption
        Set: SerializerOption(self: Receive) = value
        """
        ...

    @property
    def ServiceContractName(self) -> XName:
        """
        Get: ServiceContractName(self: Receive) -> XName
        Set: ServiceContractName(self: Receive) = value
        """
        ...


    @staticmethod
    def FromOperationDescription(operation) -> Receive: # Not found arg types: {'operation': 'OperationDescription'}
        """ FromOperationDescription(operation: OperationDescription) -> Receive """
        ...

    def ShouldSerializeCorrelatesOn(self) -> bool:
        """ ShouldSerializeCorrelatesOn(self: Receive) -> bool """
        ...


class ReceiveContent: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Create(*__args:OutArgument) -> ReceiveMessageContent:
        """
        Create(message: OutArgument) -> ReceiveMessageContent
        Create(message: OutArgument, declaredMessageType: Type) -> ReceiveMessageContent
        Create(parameters: IDictionary[str, OutArgument]) -> ReceiveParametersContent
        """
        ...


class ReceiveMessageContent(ReceiveContent): # skipped bases: <type 'object'>
    """
    ReceiveMessageContent()
    ReceiveMessageContent(message: OutArgument)
    ReceiveMessageContent(message: OutArgument, declaredMessageType: Type)
    """
    @property
    def DeclaredMessageType(self) -> Type:
        """
        Get: DeclaredMessageType(self: ReceiveMessageContent) -> Type
        Set: DeclaredMessageType(self: ReceiveMessageContent) = value
        """
        ...

    @property
    def Message(self) -> OutArgument:
        """
        Get: Message(self: ReceiveMessageContent) -> OutArgument
        Set: Message(self: ReceiveMessageContent) = value
        """
        ...


    def ShouldSerializeDeclaredMessageType(self) -> bool:
        """ ShouldSerializeDeclaredMessageType(self: ReceiveMessageContent) -> bool """
        ...

    def __new__(cls, message:OutArgument = ..., declaredMessageType:Type = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, message: OutArgument)
        __new__(cls: type, message: OutArgument, declaredMessageType: Type)
        """
        ...


class ReceiveParametersContent(ReceiveContent): # skipped bases: <type 'object'>
    """
    ReceiveParametersContent()
    ReceiveParametersContent(parameters: IDictionary[str, OutArgument])
    """
    @property
    def Parameters(self) -> IDictionary:
        """ Get: Parameters(self: ReceiveParametersContent) -> IDictionary[str, OutArgument] """
        ...


    def __new__(cls, parameters:IDictionary = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parameters: IDictionary[str, OutArgument])
        """
        ...


class ReceiveReply(Activity): # skipped bases: <type 'object'>
    """ ReceiveReply() """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: ReceiveReply) -> str
        Set: Action(self: ReceiveReply) = value
        """
        ...

    @property
    def Content(self) -> ReceiveContent:
        """
        Get: Content(self: ReceiveReply) -> ReceiveContent
        Set: Content(self: ReceiveReply) = value
        """
        ...

    @property
    def CorrelationInitializers(self) -> Collection:
        """ Get: CorrelationInitializers(self: ReceiveReply) -> Collection[CorrelationInitializer] """
        ...

    @property
    def Request(self) -> Send:
        """
        Get: Request(self: ReceiveReply) -> Send
        Set: Request(self: ReceiveReply) = value
        """
        ...



class ReceiveSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ ReceiveSettings() """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: ReceiveSettings) -> str
        Set: Action(self: ReceiveSettings) = value
        """
        ...

    @property
    def CanCreateInstance(self) -> bool:
        """
        Get: CanCreateInstance(self: ReceiveSettings) -> bool
        Set: CanCreateInstance(self: ReceiveSettings) = value
        """
        ...

    @property
    def OwnerDisplayName(self) -> str:
        """
        Get: OwnerDisplayName(self: ReceiveSettings) -> str
        Set: OwnerDisplayName(self: ReceiveSettings) = value
        """
        ...



class RequestReplyCorrelationInitializer(CorrelationInitializer): # skipped bases: <type 'object'>
    """ RequestReplyCorrelationInitializer() """
    pass

class Send(Activity): # skipped bases: <type 'object'>
    """ Send() """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: Send) -> str
        Set: Action(self: Send) = value
        """
        ...

    @property
    def Content(self) -> SendContent:
        """
        Get: Content(self: Send) -> SendContent
        Set: Content(self: Send) = value
        """
        ...

    @property
    def CorrelatesWith(self) -> InArgument:
        """
        Get: CorrelatesWith(self: Send) -> InArgument[CorrelationHandle]
        Set: CorrelatesWith(self: Send) = value
        """
        ...

    @property
    def CorrelationInitializers(self) -> Collection:
        """ Get: CorrelationInitializers(self: Send) -> Collection[CorrelationInitializer] """
        ...

    @property
    def Endpoint(self) -> Endpoint:
        """
        Get: Endpoint(self: Send) -> Endpoint
        Set: Endpoint(self: Send) = value
        """
        ...

    @property
    def EndpointAddress(self) -> InArgument:
        """
        Get: EndpointAddress(self: Send) -> InArgument[Uri]
        Set: EndpointAddress(self: Send) = value
        """
        ...

    @property
    def EndpointConfigurationName(self) -> str:
        """
        Get: EndpointConfigurationName(self: Send) -> str
        Set: EndpointConfigurationName(self: Send) = value
        """
        ...

    @property
    def KnownTypes(self) -> Collection:
        """ Get: KnownTypes(self: Send) -> Collection[Type] """
        ...

    @property
    def OperationName(self) -> str:
        """
        Get: OperationName(self: Send) -> str
        Set: OperationName(self: Send) = value
        """
        ...

    @property
    def ProtectionLevel(self) -> Nullable:
        """
        Get: ProtectionLevel(self: Send) -> Nullable[ProtectionLevel]
        Set: ProtectionLevel(self: Send) = value
        """
        ...

    @property
    def SerializerOption(self) -> SerializerOption:
        """
        Get: SerializerOption(self: Send) -> SerializerOption
        Set: SerializerOption(self: Send) = value
        """
        ...

    @property
    def ServiceContractName(self) -> XName:
        """
        Get: ServiceContractName(self: Send) -> XName
        Set: ServiceContractName(self: Send) = value
        """
        ...

    @property
    def TokenImpersonationLevel(self) -> TokenImpersonationLevel:
        """
        Get: TokenImpersonationLevel(self: Send) -> TokenImpersonationLevel
        Set: TokenImpersonationLevel(self: Send) = value
        """
        ...



class SendContent: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Create(*__args:InArgument) -> SendMessageContent:
        """
        Create(message: InArgument) -> SendMessageContent
        Create(message: InArgument, declaredMessageType: Type) -> SendMessageContent
        Create(parameters: IDictionary[str, InArgument]) -> SendParametersContent
        """
        ...


class SendMessageChannelCache(IDisposable, ICancelable): # skipped bases: <type 'object'>
    """
    SendMessageChannelCache()
    SendMessageChannelCache(factorySettings: ChannelCacheSettings, channelSettings: ChannelCacheSettings)
    SendMessageChannelCache(factorySettings: ChannelCacheSettings, channelSettings: ChannelCacheSettings, allowUnsafeCaching: bool)
    """
    @property
    def AllowUnsafeCaching(self) -> bool:
        """
        Get: AllowUnsafeCaching(self: SendMessageChannelCache) -> bool
        Set: AllowUnsafeCaching(self: SendMessageChannelCache) = value
        """
        ...

    @property
    def ChannelSettings(self) -> ChannelCacheSettings:
        """
        Get: ChannelSettings(self: SendMessageChannelCache) -> ChannelCacheSettings
        Set: ChannelSettings(self: SendMessageChannelCache) = value
        """
        ...

    @property
    def FactorySettings(self) -> ChannelCacheSettings:
        """
        Get: FactorySettings(self: SendMessageChannelCache) -> ChannelCacheSettings
        Set: FactorySettings(self: SendMessageChannelCache) = value
        """
        ...



class SendMessageContent(SendContent): # skipped bases: <type 'object'>
    """
    SendMessageContent()
    SendMessageContent(message: InArgument)
    SendMessageContent(message: InArgument, declaredMessageType: Type)
    """
    @property
    def DeclaredMessageType(self) -> Type:
        """
        Get: DeclaredMessageType(self: SendMessageContent) -> Type
        Set: DeclaredMessageType(self: SendMessageContent) = value
        """
        ...

    @property
    def Message(self) -> InArgument:
        """
        Get: Message(self: SendMessageContent) -> InArgument
        Set: Message(self: SendMessageContent) = value
        """
        ...


    def ShouldSerializeDeclaredMessageType(self) -> bool:
        """ ShouldSerializeDeclaredMessageType(self: SendMessageContent) -> bool """
        ...

    def __new__(cls, message:InArgument = ..., declaredMessageType:Type = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, message: InArgument)
        __new__(cls: type, message: InArgument, declaredMessageType: Type)
        """
        ...


class SendParametersContent(SendContent): # skipped bases: <type 'object'>
    """
    SendParametersContent()
    SendParametersContent(parameters: IDictionary[str, InArgument])
    """
    @property
    def Parameters(self) -> IDictionary:
        """ Get: Parameters(self: SendParametersContent) -> IDictionary[str, InArgument] """
        ...


    def __new__(cls, parameters:IDictionary = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parameters: IDictionary[str, InArgument])
        """
        ...


class SendReceiveExtension: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def HostSettings(self) -> HostSettings:
        """ Get: HostSettings(self: SendReceiveExtension) -> HostSettings """
        ...


    def Cancel(self, bookmark:Bookmark): # -> 
        """ Cancel(self: SendReceiveExtension, bookmark: Bookmark) """
        ...

    def OnRegisterReceive(self, *args): #cannot find CLR method
        """ OnRegisterReceive(self: SendReceiveExtension, settings: ReceiveSettings, correlatesWith: InstanceKey, receiveBookmark: Bookmark) """
        ...

    def OnUninitializeCorrelation(self, correlationKey:InstanceKey): # -> 
        """ OnUninitializeCorrelation(self: SendReceiveExtension, correlationKey: InstanceKey) """
        ...

    def RegisterReceive(self, settings:ReceiveSettings, correlatesWith:InstanceKey, receiveBookmark:Bookmark): # -> 
        """ RegisterReceive(self: SendReceiveExtension, settings: ReceiveSettings, correlatesWith: InstanceKey, receiveBookmark: Bookmark) """
        ...

    def Send(self, message:MessageContext, settings:SendSettings, correlatesWith:InstanceKey, sendCompleteBookmark:Bookmark): # -> 
        """ Send(self: SendReceiveExtension, message: MessageContext, settings: SendSettings, correlatesWith: InstanceKey, sendCompleteBookmark: Bookmark) """
        ...


class SendReply(Activity): # skipped bases: <type 'object'>
    """ SendReply() """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: SendReply) -> str
        Set: Action(self: SendReply) = value
        """
        ...

    @property
    def Content(self) -> SendContent:
        """
        Get: Content(self: SendReply) -> SendContent
        Set: Content(self: SendReply) = value
        """
        ...

    @property
    def CorrelationInitializers(self) -> Collection:
        """ Get: CorrelationInitializers(self: SendReply) -> Collection[CorrelationInitializer] """
        ...

    @property
    def PersistBeforeSend(self) -> bool:
        """
        Get: PersistBeforeSend(self: SendReply) -> bool
        Set: PersistBeforeSend(self: SendReply) = value
        """
        ...

    @property
    def Request(self) -> Receive:
        """
        Get: Request(self: SendReply) -> Receive
        Set: Request(self: SendReply) = value
        """
        ...


    @staticmethod
    def FromOperationDescription(operation, faultReplies) -> Tuple_[SendReply, IEnumerable]:
        """ FromOperationDescription(operation: OperationDescription) -> (SendReply, IEnumerable[SendReply]) """
        ...


class SendSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ SendSettings() """
    @property
    def Endpoint(self) -> Endpoint:
        """
        Get: Endpoint(self: SendSettings) -> Endpoint
        Set: Endpoint(self: SendSettings) = value
        """
        ...

    @property
    def EndpointAddress(self) -> Uri:
        """
        Get: EndpointAddress(self: SendSettings) -> Uri
        Set: EndpointAddress(self: SendSettings) = value
        """
        ...

    @property
    def EndpointConfigurationName(self) -> str:
        """
        Get: EndpointConfigurationName(self: SendSettings) -> str
        Set: EndpointConfigurationName(self: SendSettings) = value
        """
        ...

    @property
    def IsOneWay(self) -> bool:
        """
        Get: IsOneWay(self: SendSettings) -> bool
        Set: IsOneWay(self: SendSettings) = value
        """
        ...

    @property
    def OwnerDisplayName(self) -> str:
        """
        Get: OwnerDisplayName(self: SendSettings) -> str
        Set: OwnerDisplayName(self: SendSettings) = value
        """
        ...

    @property
    def ProtectionLevel(self) -> Nullable:
        """
        Get: ProtectionLevel(self: SendSettings) -> Nullable[ProtectionLevel]
        Set: ProtectionLevel(self: SendSettings) = value
        """
        ...

    @property
    def RequirePersistBeforeSend(self) -> bool:
        """
        Get: RequirePersistBeforeSend(self: SendSettings) -> bool
        Set: RequirePersistBeforeSend(self: SendSettings) = value
        """
        ...

    @property
    def TokenImpersonationLevel(self) -> TokenImpersonationLevel:
        """
        Get: TokenImpersonationLevel(self: SendSettings) -> TokenImpersonationLevel
        Set: TokenImpersonationLevel(self: SendSettings) = value
        """
        ...



class SerializerOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SerializerOption, values: DataContractSerializer (0), XmlSerializer (1) """
    DataContractSerializer: SerializerOption = ...
    value__ = ...
    XmlSerializer: SerializerOption = ...


class TransactedReceiveScope(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ TransactedReceiveScope() """
    @property
    def Body(self) -> Activity:
        """
        Get: Body(self: TransactedReceiveScope) -> Activity
        Set: Body(self: TransactedReceiveScope) = value
        """
        ...

    @property
    def Request(self) -> Receive:
        """
        Get: Request(self: TransactedReceiveScope) -> Receive
        Set: Request(self: TransactedReceiveScope) = value
        """
        ...

    @property
    def Variables(self) -> Collection:
        """ Get: Variables(self: TransactedReceiveScope) -> Collection[Variable] """
        ...



class WorkflowControlClient(ClientBase): # skipped bases: <type 'IDisposable'>, <type 'ICommunicationObject'>, <type 'object'>
    """
    WorkflowControlClient()
    WorkflowControlClient(endpointConfigurationName: str)
    WorkflowControlClient(endpointConfigurationName: str, remoteAddress: EndpointAddress)
    WorkflowControlClient(endpointConfigurationName: str, remoteAddress: str)
    WorkflowControlClient(binding: Binding, remoteAddress: EndpointAddress)
    WorkflowControlClient(workflowEndpoint: WorkflowControlEndpoint)
    """
    def Abandon(self, instanceId:Guid, reason:str = ...): # -> 
        """ Abandon(self: WorkflowControlClient, instanceId: Guid)Abandon(self: WorkflowControlClient, instanceId: Guid, reason: str) """
        ...

    def AbandonAsync(self, instanceId:Guid, *__args:object): # -> 
        """ AbandonAsync(self: WorkflowControlClient, instanceId: Guid)AbandonAsync(self: WorkflowControlClient, instanceId: Guid, userState: object)AbandonAsync(self: WorkflowControlClient, instanceId: Guid, reason: str)AbandonAsync(self: WorkflowControlClient, instanceId: Guid, reason: str, userState: object) """
        ...

    def BeginAbandon(self, instanceId, *__args) -> IAsyncResult:
        """
        BeginAbandon(self: WorkflowControlClient, instanceId: Guid, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginAbandon(self: WorkflowControlClient, instanceId: Guid, reason: str, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginCancel(self, instanceId:Guid, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginCancel(self: WorkflowControlClient, instanceId: Guid, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginRun(self, instanceId:Guid, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginRun(self: WorkflowControlClient, instanceId: Guid, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginSuspend(self, instanceId, *__args) -> IAsyncResult:
        """
        BeginSuspend(self: WorkflowControlClient, instanceId: Guid, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginSuspend(self: WorkflowControlClient, instanceId: Guid, reason: str, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginTerminate(self, instanceId, *__args) -> IAsyncResult:
        """
        BeginTerminate(self: WorkflowControlClient, instanceId: Guid, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginTerminate(self: WorkflowControlClient, instanceId: Guid, reason: str, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginUnsuspend(self, instanceId:Guid, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginUnsuspend(self: WorkflowControlClient, instanceId: Guid, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def Cancel(self, instanceId:Guid): # -> 
        """ Cancel(self: WorkflowControlClient, instanceId: Guid) """
        ...

    def CancelAsync(self, instanceId:Guid, userState:object = ...): # -> 
        """ CancelAsync(self: WorkflowControlClient, instanceId: Guid)CancelAsync(self: WorkflowControlClient, instanceId: Guid, userState: object) """
        ...

    def EndAbandon(self, result:IAsyncResult): # -> 
        """ EndAbandon(self: WorkflowControlClient, result: IAsyncResult) """
        ...

    def EndCancel(self, result:IAsyncResult): # -> 
        """ EndCancel(self: WorkflowControlClient, result: IAsyncResult) """
        ...

    def EndRun(self, result:IAsyncResult): # -> 
        """ EndRun(self: WorkflowControlClient, result: IAsyncResult) """
        ...

    def EndSuspend(self, result:IAsyncResult): # -> 
        """ EndSuspend(self: WorkflowControlClient, result: IAsyncResult) """
        ...

    def EndTerminate(self, result:IAsyncResult): # -> 
        """ EndTerminate(self: WorkflowControlClient, result: IAsyncResult) """
        ...

    def EndUnsuspend(self, result:IAsyncResult): # -> 
        """ EndUnsuspend(self: WorkflowControlClient, result: IAsyncResult) """
        ...

    def Run(self, instanceId:Guid): # -> 
        """ Run(self: WorkflowControlClient, instanceId: Guid) """
        ...

    def RunAsync(self, instanceId:Guid, userState:object = ...): # -> 
        """ RunAsync(self: WorkflowControlClient, instanceId: Guid)RunAsync(self: WorkflowControlClient, instanceId: Guid, userState: object) """
        ...

    def Suspend(self, instanceId:Guid, reason:str = ...): # -> 
        """ Suspend(self: WorkflowControlClient, instanceId: Guid)Suspend(self: WorkflowControlClient, instanceId: Guid, reason: str) """
        ...

    def SuspendAsync(self, instanceId:Guid, *__args:str): # -> 
        """ SuspendAsync(self: WorkflowControlClient, instanceId: Guid)SuspendAsync(self: WorkflowControlClient, instanceId: Guid, reason: str)SuspendAsync(self: WorkflowControlClient, instanceId: Guid, userState: object)SuspendAsync(self: WorkflowControlClient, instanceId: Guid, reason: str, userState: object) """
        ...

    def Terminate(self, instanceId:Guid, reason:str = ...): # -> 
        """ Terminate(self: WorkflowControlClient, instanceId: Guid)Terminate(self: WorkflowControlClient, instanceId: Guid, reason: str) """
        ...

    def TerminateAsync(self, instanceId:Guid, *__args:str): # -> 
        """ TerminateAsync(self: WorkflowControlClient, instanceId: Guid)TerminateAsync(self: WorkflowControlClient, instanceId: Guid, reason: str)TerminateAsync(self: WorkflowControlClient, instanceId: Guid, userState: object)TerminateAsync(self: WorkflowControlClient, instanceId: Guid, reason: str, userState: object) """
        ...

    def Unsuspend(self, instanceId:Guid): # -> 
        """ Unsuspend(self: WorkflowControlClient, instanceId: Guid) """
        ...

    def UnsuspendAsync(self, instanceId:Guid, userState:object = ...): # -> 
        """ UnsuspendAsync(self: WorkflowControlClient, instanceId: Guid)UnsuspendAsync(self: WorkflowControlClient, instanceId: Guid, userState: object) """
        ...

    AbandonCompleted = ...
    CancelCompleted = ...
    RunCompleted = ...
    SuspendCompleted = ...
    TerminateCompleted = ...
    UnsuspendCompleted = ...


class WorkflowControlEndpoint(ServiceEndpoint): # skipped bases: <type 'object'>
    """
    WorkflowControlEndpoint()
    WorkflowControlEndpoint(binding: Binding, address: EndpointAddress)
    """
    pass

class WorkflowCreationContext: # skipped bases: <type 'object'>, <type 'object'>
    """ WorkflowCreationContext() """
    @property
    def CreateOnly(self) -> bool:
        """
        Get: CreateOnly(self: WorkflowCreationContext) -> bool
        Set: CreateOnly(self: WorkflowCreationContext) = value
        """
        ...

    @property
    def IsCompletionTransactionRequired(self) -> bool:
        """
        Get: IsCompletionTransactionRequired(self: WorkflowCreationContext) -> bool
        Set: IsCompletionTransactionRequired(self: WorkflowCreationContext) = value
        """
        ...

    @property
    def WorkflowArguments(self) -> IDictionary:
        """ Get: WorkflowArguments(self: WorkflowCreationContext) -> IDictionary[str, object] """
        ...


    def OnAbort(self, *args): #cannot find CLR method
        """ OnAbort(self: WorkflowCreationContext) """
        ...

    def OnBeginWorkflowCompleted(self, *args): #cannot find CLR method
        """ OnBeginWorkflowCompleted(self: WorkflowCreationContext, completionState: ActivityInstanceState, workflowOutputs: IDictionary[str, object], terminationException: Exception, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def OnEndWorkflowCompleted(self, *args): #cannot find CLR method
        """ OnEndWorkflowCompleted(self: WorkflowCreationContext, result: IAsyncResult) """
        ...


class WorkflowHostingEndpoint(ServiceEndpoint): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CorrelationQueries(self) -> Collection:
        """ Get: CorrelationQueries(self: WorkflowHostingEndpoint) -> Collection[CorrelationQuery] """
        ...


    def OnGetCreationContext(self, *args): #cannot find CLR method
        """ OnGetCreationContext(self: WorkflowHostingEndpoint, inputs: Array[object], operationContext: OperationContext, instanceId: Guid, responseContext: WorkflowHostingResponseContext) -> WorkflowCreationContext """
        ...

    def OnGetInstanceId(self, *args): #cannot find CLR method
        """ OnGetInstanceId(self: WorkflowHostingEndpoint, inputs: Array[object], operationContext: OperationContext) -> Guid """
        ...

    def OnResolveBookmark(self, *args): #cannot find CLR method
        """ OnResolveBookmark(self: WorkflowHostingEndpoint, inputs: Array[object], operationContext: OperationContext, responseContext: WorkflowHostingResponseContext) -> (Bookmark, object) """
        ...


class WorkflowHostingResponseContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def SendResponse(self, returnValue:object, outputs:Array): # -> 
        """ SendResponse(self: WorkflowHostingResponseContext, returnValue: object, outputs: Array[object]) """
        ...


class WorkflowService(IDebuggableWorkflowTree): # skipped bases: <type 'object'>
    """ WorkflowService() """
    @property
    def AllowBufferedReceive(self) -> bool:
        """
        Get: AllowBufferedReceive(self: WorkflowService) -> bool
        Set: AllowBufferedReceive(self: WorkflowService) = value
        """
        ...

    @property
    def Body(self) -> Activity:
        """
        Get: Body(self: WorkflowService) -> Activity
        Set: Body(self: WorkflowService) = value
        """
        ...

    @property
    def ConfigurationName(self) -> str:
        """
        Get: ConfigurationName(self: WorkflowService) -> str
        Set: ConfigurationName(self: WorkflowService) = value
        """
        ...

    @property
    def DefinitionIdentity(self) -> WorkflowIdentity:
        """
        Get: DefinitionIdentity(self: WorkflowService) -> WorkflowIdentity
        Set: DefinitionIdentity(self: WorkflowService) = value
        """
        ...

    @property
    def Endpoints(self) -> Collection:
        """ Get: Endpoints(self: WorkflowService) -> Collection[Endpoint] """
        ...

    @property
    def ImplementedContracts(self) -> Collection:
        """ Get: ImplementedContracts(self: WorkflowService) -> Collection[Type] """
        ...

    @property
    def Name(self) -> XName:
        """
        Get: Name(self: WorkflowService) -> XName
        Set: Name(self: WorkflowService) = value
        """
        ...

    @property
    def UpdateMaps(self) -> IDictionary:
        """ Get: UpdateMaps(self: WorkflowService) -> IDictionary[WorkflowIdentity, DynamicUpdateMap] """
        ...


    def GetContractDescriptions(self) -> IDictionary:
        """ GetContractDescriptions(self: WorkflowService) -> IDictionary[XName, ContractDescription] """
        ...

    def Validate(self, settings:ValidationSettings) -> ValidationResults:
        """ Validate(self: WorkflowService, settings: ValidationSettings) -> ValidationResults """
        ...


class WorkflowServiceHost(ServiceHostBase): # skipped bases: <type 'IDisposable'>, <type 'ICommunicationObject'>, <type 'IExtensibleObject[ServiceHostBase]'>, <type 'object'>
    """
    WorkflowServiceHost(serviceImplementation: object, *baseAddresses: Array[Uri])
    WorkflowServiceHost(activity: Activity, *baseAddresses: Array[Uri])
    WorkflowServiceHost(serviceDefinition: WorkflowService, *baseAddresses: Array[Uri])
    """
    @property
    def Activity(self) -> Activity:
        """ Get: Activity(self: WorkflowServiceHost) -> Activity """
        ...

    @property
    def DurableInstancingOptions(self) -> DurableInstancingOptions:
        """ Get: DurableInstancingOptions(self: WorkflowServiceHost) -> DurableInstancingOptions """
        ...

    @property
    def SupportedVersions(self) -> ICollection:
        """ Get: SupportedVersions(self: WorkflowServiceHost) -> ICollection[WorkflowService] """
        ...

    @property
    def WorkflowExtensions(self) -> WorkflowInstanceExtensionManager:
        """ Get: WorkflowExtensions(self: WorkflowServiceHost) -> WorkflowInstanceExtensionManager """
        ...


    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, serviceImplementation: object, *baseAddresses: Array[Uri])
        __new__(cls: type, activity: Activity, *baseAddresses: Array[Uri])
        __new__(cls: type, serviceDefinition: WorkflowService, *baseAddresses: Array[Uri])
        __new__(cls: type)
        """
        ...


class WorkflowUpdateableControlClient(ClientBase): # skipped bases: <type 'IDisposable'>, <type 'ICommunicationObject'>, <type 'object'>
    """
    WorkflowUpdateableControlClient()
    WorkflowUpdateableControlClient(endpointConfigurationName: str)
    WorkflowUpdateableControlClient(endpointConfigurationName: str, remoteAddress: EndpointAddress)
    WorkflowUpdateableControlClient(endpointConfigurationName: str, remoteAddress: str)
    WorkflowUpdateableControlClient(binding: Binding, remoteAddress: EndpointAddress)
    WorkflowUpdateableControlClient(workflowEndpoint: WorkflowControlEndpoint)
    """
    def Abandon(self, instanceId:Guid, reason:str = ...): # -> 
        """ Abandon(self: WorkflowUpdateableControlClient, instanceId: Guid)Abandon(self: WorkflowUpdateableControlClient, instanceId: Guid, reason: str) """
        ...

    def AbandonAsync(self, instanceId:Guid, *__args:object): # -> 
        """ AbandonAsync(self: WorkflowUpdateableControlClient, instanceId: Guid)AbandonAsync(self: WorkflowUpdateableControlClient, instanceId: Guid, userState: object)AbandonAsync(self: WorkflowUpdateableControlClient, instanceId: Guid, reason: str)AbandonAsync(self: WorkflowUpdateableControlClient, instanceId: Guid, reason: str, userState: object) """
        ...

    def BeginAbandon(self, instanceId, *__args) -> IAsyncResult:
        """
        BeginAbandon(self: WorkflowUpdateableControlClient, instanceId: Guid, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginAbandon(self: WorkflowUpdateableControlClient, instanceId: Guid, reason: str, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginCancel(self, instanceId:Guid, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginCancel(self: WorkflowUpdateableControlClient, instanceId: Guid, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginRun(self, instanceId:Guid, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginRun(self: WorkflowUpdateableControlClient, instanceId: Guid, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginSuspend(self, instanceId, *__args) -> IAsyncResult:
        """
        BeginSuspend(self: WorkflowUpdateableControlClient, instanceId: Guid, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginSuspend(self: WorkflowUpdateableControlClient, instanceId: Guid, reason: str, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginTerminate(self, instanceId, *__args) -> IAsyncResult:
        """
        BeginTerminate(self: WorkflowUpdateableControlClient, instanceId: Guid, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginTerminate(self: WorkflowUpdateableControlClient, instanceId: Guid, reason: str, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginUnsuspend(self, instanceId:Guid, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginUnsuspend(self: WorkflowUpdateableControlClient, instanceId: Guid, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginUpdate(self, instanceId:Guid, updatedDefinitionIdentity:WorkflowIdentity, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginUpdate(self: WorkflowUpdateableControlClient, instanceId: Guid, updatedDefinitionIdentity: WorkflowIdentity, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def Cancel(self, instanceId:Guid): # -> 
        """ Cancel(self: WorkflowUpdateableControlClient, instanceId: Guid) """
        ...

    def CancelAsync(self, instanceId:Guid, userState:object = ...): # -> 
        """ CancelAsync(self: WorkflowUpdateableControlClient, instanceId: Guid)CancelAsync(self: WorkflowUpdateableControlClient, instanceId: Guid, userState: object) """
        ...

    def EndAbandon(self, result:IAsyncResult): # -> 
        """ EndAbandon(self: WorkflowUpdateableControlClient, result: IAsyncResult) """
        ...

    def EndCancel(self, result:IAsyncResult): # -> 
        """ EndCancel(self: WorkflowUpdateableControlClient, result: IAsyncResult) """
        ...

    def EndRun(self, result:IAsyncResult): # -> 
        """ EndRun(self: WorkflowUpdateableControlClient, result: IAsyncResult) """
        ...

    def EndSuspend(self, result:IAsyncResult): # -> 
        """ EndSuspend(self: WorkflowUpdateableControlClient, result: IAsyncResult) """
        ...

    def EndTerminate(self, result:IAsyncResult): # -> 
        """ EndTerminate(self: WorkflowUpdateableControlClient, result: IAsyncResult) """
        ...

    def EndUnsuspend(self, result:IAsyncResult): # -> 
        """ EndUnsuspend(self: WorkflowUpdateableControlClient, result: IAsyncResult) """
        ...

    def EndUpdate(self, result:IAsyncResult): # -> 
        """ EndUpdate(self: WorkflowUpdateableControlClient, result: IAsyncResult) """
        ...

    def Run(self, instanceId:Guid): # -> 
        """ Run(self: WorkflowUpdateableControlClient, instanceId: Guid) """
        ...

    def RunAsync(self, instanceId:Guid, userState:object = ...): # -> 
        """ RunAsync(self: WorkflowUpdateableControlClient, instanceId: Guid)RunAsync(self: WorkflowUpdateableControlClient, instanceId: Guid, userState: object) """
        ...

    def Suspend(self, instanceId:Guid, reason:str = ...): # -> 
        """ Suspend(self: WorkflowUpdateableControlClient, instanceId: Guid)Suspend(self: WorkflowUpdateableControlClient, instanceId: Guid, reason: str) """
        ...

    def SuspendAsync(self, instanceId:Guid, *__args:str): # -> 
        """ SuspendAsync(self: WorkflowUpdateableControlClient, instanceId: Guid)SuspendAsync(self: WorkflowUpdateableControlClient, instanceId: Guid, reason: str)SuspendAsync(self: WorkflowUpdateableControlClient, instanceId: Guid, userState: object)SuspendAsync(self: WorkflowUpdateableControlClient, instanceId: Guid, reason: str, userState: object) """
        ...

    def Terminate(self, instanceId:Guid, reason:str = ...): # -> 
        """ Terminate(self: WorkflowUpdateableControlClient, instanceId: Guid)Terminate(self: WorkflowUpdateableControlClient, instanceId: Guid, reason: str) """
        ...

    def TerminateAsync(self, instanceId:Guid, *__args:str): # -> 
        """ TerminateAsync(self: WorkflowUpdateableControlClient, instanceId: Guid)TerminateAsync(self: WorkflowUpdateableControlClient, instanceId: Guid, reason: str)TerminateAsync(self: WorkflowUpdateableControlClient, instanceId: Guid, userState: object)TerminateAsync(self: WorkflowUpdateableControlClient, instanceId: Guid, reason: str, userState: object) """
        ...

    def Unsuspend(self, instanceId:Guid): # -> 
        """ Unsuspend(self: WorkflowUpdateableControlClient, instanceId: Guid) """
        ...

    def UnsuspendAsync(self, instanceId:Guid, userState:object = ...): # -> 
        """ UnsuspendAsync(self: WorkflowUpdateableControlClient, instanceId: Guid)UnsuspendAsync(self: WorkflowUpdateableControlClient, instanceId: Guid, userState: object) """
        ...

    def Update(self, instanceId:Guid, updatedDefinitionIdentity:WorkflowIdentity): # -> 
        """ Update(self: WorkflowUpdateableControlClient, instanceId: Guid, updatedDefinitionIdentity: WorkflowIdentity) """
        ...

    def UpdateAsync(self, instanceId:Guid, updatedDefinitionIdentity:WorkflowIdentity, userState:object = ...): # -> 
        """ UpdateAsync(self: WorkflowUpdateableControlClient, instanceId: Guid, updatedDefinitionIdentity: WorkflowIdentity)UpdateAsync(self: WorkflowUpdateableControlClient, instanceId: Guid, updatedDefinitionIdentity: WorkflowIdentity, userState: object) """
        ...

    AbandonCompleted = ...
    CancelCompleted = ...
    RunCompleted = ...
    SuspendCompleted = ...
    TerminateCompleted = ...
    UnsuspendCompleted = ...
    UpdateCompleted = ...


# variables with complex values

