# encoding: utf-8
# module System.ServiceModel.Dispatcher calls itself Dispatcher
# from System.WorkflowServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.ServiceModel.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.ServiceModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Scripting.Interpreter import ExceptionHandler

from System import (Array, AsyncCallback, Guid, IAsyncResult, IDisposable, 
    Int64, MulticastDelegate, SystemException, TimeSpan, Type, Uri, 
    UriTemplate)

from System.Collections import (ICollection, IDictionary, IEnumerable, 
    IEnumerator, IList)

from System.Collections.Generic import (KeyValuePair, SynchronizedCollection, 
    SynchronizedKeyedCollection)

from System.Collections.ObjectModel import (Collection, KeyedCollection, 
    ReadOnlyCollection)

from System.Data import IsolationLevel

from System.Messaging import Message

from System.Reflection import MethodBase, MethodInfo

from System.ServiceModel import (AuditLevel, AuditLogLocation, 
    CommunicationException, ConcurrencyMode, EndpointAddress, IClientChannel, 
    IContextChannel, IDefaultCommunicationTimeouts, IDuplexContextChannel, 
    ImpersonationOption, InstanceContext, ServiceAuthenticationManager, 
    ServiceAuthorizationManager, ServiceHostBase)

from System.Threading import SynchronizationContext

from System.Web.Security import RoleProvider

from System.Xml import XmlNamespaceManager, XmlWriter

from System.Xml.Schema import XmlSchemaSet, XmlSchemaType

from System.Xml.Serialization import IXmlSerializable

from System.Xml.XPath import (XPathException, XPathNavigator, 
    XPathNodeIterator, XPathNodeType, XPathResultType)

from System.Xml.Xsl import XsltContext

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    ClientRuntime, CommunicationObject, DispatchRuntime, EndpointDispatcher, 
    IChannelListener, IClientMessageFormatter, IClientOperationSelector, 
    IDispatchMessageFormatter, IDispatchOperationSelector, 
    IInstanceContextProvider, IInstanceProvider, IOperationInvoker, 
    InstanceContextIdleCallback, MessageBuffer, MessageQueryCollection, 
    MessageVersion, PrincipalPermissionMode, ServiceThrottle, TFilterData, 
    TResult)
"""

# no functions
# classes

class MessageFilter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateFilterTable(self, *args): #cannot find CLR method
        """ CreateFilterTable[FilterData](self: MessageFilter) -> IMessageFilterTable[FilterData] """
        ...

    def Match(self, *__args) -> bool: # Not found arg types: {'*__args': 'MessageBuffer'}
        """
        Match(self: MessageFilter, buffer: MessageBuffer) -> bool
        Match(self: MessageFilter, message: Message) -> bool
        """
        ...


class ActionMessageFilter(MessageFilter): # skipped bases: <type 'object'>
    """ ActionMessageFilter(*actions: Array[str]) """
    @property
    def Actions(self) -> ReadOnlyCollection:
        """ Get: Actions(self: ActionMessageFilter) -> ReadOnlyCollection[str] """
        ...


    def __new__(cls, actions:Array) -> Self:
        """ __new__(cls: type, *actions: Array[str]) """
        ...


class ChannelDispatcherBase(CommunicationObject): # skipped bases: <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    @property
    def Host(self) -> ServiceHostBase:
        """ Get: Host(self: ChannelDispatcherBase) -> ServiceHostBase """
        ...

    @property
    def Listener(self): # -> IChannelListener
        """ Get: Listener(self: ChannelDispatcherBase) -> IChannelListener """
        ...


    def Attach(self, *args): #cannot find CLR method
        """ Attach(self: ChannelDispatcherBase, host: ServiceHostBase) """
        ...

    def CloseInput(self): # -> 
        """ CloseInput(self: ChannelDispatcherBase) """
        ...

    def Detach(self, *args): #cannot find CLR method
        """ Detach(self: ChannelDispatcherBase, host: ServiceHostBase) """
        ...


class ChannelDispatcher(ChannelDispatcherBase): # skipped bases: <type 'ICommunicationObject'>, <type 'object'>
    """
    ChannelDispatcher(listener: IChannelListener)
    ChannelDispatcher(listener: IChannelListener, bindingName: str)
    ChannelDispatcher(listener: IChannelListener, bindingName: str, timeouts: IDefaultCommunicationTimeouts)
    """
    @property
    def AsynchronousTransactedAcceptEnabled(self) -> bool:
        """
        Get: AsynchronousTransactedAcceptEnabled(self: ChannelDispatcher) -> bool
        Set: AsynchronousTransactedAcceptEnabled(self: ChannelDispatcher) = value
        """
        ...

    @property
    def BindingName(self) -> str:
        """ Get: BindingName(self: ChannelDispatcher) -> str """
        ...

    @property
    def ChannelInitializers(self) -> SynchronizedCollection:
        """ Get: ChannelInitializers(self: ChannelDispatcher) -> SynchronizedCollection[IChannelInitializer] """
        ...

    @property
    def Endpoints(self) -> SynchronizedCollection:
        """ Get: Endpoints(self: ChannelDispatcher) -> SynchronizedCollection[EndpointDispatcher] """
        ...

    @property
    def ErrorHandlers(self) -> Collection:
        """ Get: ErrorHandlers(self: ChannelDispatcher) -> Collection[IErrorHandler] """
        ...

    @property
    def IncludeExceptionDetailInFaults(self) -> bool:
        """
        Get: IncludeExceptionDetailInFaults(self: ChannelDispatcher) -> bool
        Set: IncludeExceptionDetailInFaults(self: ChannelDispatcher) = value
        """
        ...

    @property
    def IsTransactedAccept(self) -> bool:
        """ Get: IsTransactedAccept(self: ChannelDispatcher) -> bool """
        ...

    @property
    def IsTransactedReceive(self) -> bool:
        """
        Get: IsTransactedReceive(self: ChannelDispatcher) -> bool
        Set: IsTransactedReceive(self: ChannelDispatcher) = value
        """
        ...

    @property
    def ManualAddressing(self) -> bool:
        """
        Get: ManualAddressing(self: ChannelDispatcher) -> bool
        Set: ManualAddressing(self: ChannelDispatcher) = value
        """
        ...

    @property
    def MaxPendingReceives(self) -> int:
        """
        Get: MaxPendingReceives(self: ChannelDispatcher) -> int
        Set: MaxPendingReceives(self: ChannelDispatcher) = value
        """
        ...

    @property
    def MaxTransactedBatchSize(self) -> int:
        """
        Get: MaxTransactedBatchSize(self: ChannelDispatcher) -> int
        Set: MaxTransactedBatchSize(self: ChannelDispatcher) = value
        """
        ...

    @property
    def MessageVersion(self): # -> MessageVersion
        """
        Get: MessageVersion(self: ChannelDispatcher) -> MessageVersion
        Set: MessageVersion(self: ChannelDispatcher) = value
        """
        ...

    @property
    def ReceiveContextEnabled(self) -> bool:
        """
        Get: ReceiveContextEnabled(self: ChannelDispatcher) -> bool
        Set: ReceiveContextEnabled(self: ChannelDispatcher) = value
        """
        ...

    @property
    def ReceiveSynchronously(self) -> bool:
        """
        Get: ReceiveSynchronously(self: ChannelDispatcher) -> bool
        Set: ReceiveSynchronously(self: ChannelDispatcher) = value
        """
        ...

    @property
    def SendAsynchronously(self) -> bool:
        """
        Get: SendAsynchronously(self: ChannelDispatcher) -> bool
        Set: SendAsynchronously(self: ChannelDispatcher) = value
        """
        ...

    @property
    def ServiceThrottle(self): # -> ServiceThrottle
        """
        Get: ServiceThrottle(self: ChannelDispatcher) -> ServiceThrottle
        Set: ServiceThrottle(self: ChannelDispatcher) = value
        """
        ...

    @property
    def TransactionIsolationLevel(self) -> IsolationLevel:
        """
        Get: TransactionIsolationLevel(self: ChannelDispatcher) -> IsolationLevel
        Set: TransactionIsolationLevel(self: ChannelDispatcher) = value
        """
        ...

    @property
    def TransactionTimeout(self) -> TimeSpan:
        """
        Get: TransactionTimeout(self: ChannelDispatcher) -> TimeSpan
        Set: TransactionTimeout(self: ChannelDispatcher) = value
        """
        ...


    def __new__(cls, listener, bindingName:str = ..., timeouts:IDefaultCommunicationTimeouts = ...) -> Self: # Not found arg types: {'listener': 'IChannelListener'}
        """
        __new__(cls: type, listener: IChannelListener)
        __new__(cls: type, listener: IChannelListener, bindingName: str)
        __new__(cls: type, listener: IChannelListener, bindingName: str, timeouts: IDefaultCommunicationTimeouts)
        """
        ...


class ChannelDispatcherCollection(SynchronizedCollection): # skipped bases: <type 'IEnumerable[ChannelDispatcherBase]'>, <type 'IList[ChannelDispatcherBase]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[ChannelDispatcherBase]'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class ClientOperationCompatBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ParameterInspectors(self) -> IList:
        """ Get: ParameterInspectors(self: ClientOperationCompatBase) -> IList[IParameterInspector] """
        ...



class ClientOperation(ClientOperationCompatBase): # skipped bases: <type 'object'>
    """
    ClientOperation(parent: ClientRuntime, name: str, action: str)
    ClientOperation(parent: ClientRuntime, name: str, action: str, replyAction: str)
    """
    @property
    def Action(self) -> str:
        """ Get: Action(self: ClientOperation) -> str """
        ...

    @property
    def BeginMethod(self) -> MethodInfo:
        """
        Get: BeginMethod(self: ClientOperation) -> MethodInfo
        Set: BeginMethod(self: ClientOperation) = value
        """
        ...

    @property
    def ClientParameterInspectors(self) -> ICollection:
        """ Get: ClientParameterInspectors(self: ClientOperation) -> ICollection[IParameterInspector] """
        ...

    @property
    def DeserializeReply(self) -> bool:
        """
        Get: DeserializeReply(self: ClientOperation) -> bool
        Set: DeserializeReply(self: ClientOperation) = value
        """
        ...

    @property
    def EndMethod(self) -> MethodInfo:
        """
        Get: EndMethod(self: ClientOperation) -> MethodInfo
        Set: EndMethod(self: ClientOperation) = value
        """
        ...

    @property
    def FaultContractInfos(self) -> SynchronizedCollection:
        """ Get: FaultContractInfos(self: ClientOperation) -> SynchronizedCollection[FaultContractInfo] """
        ...

    @property
    def Formatter(self): # -> IClientMessageFormatter
        """
        Get: Formatter(self: ClientOperation) -> IClientMessageFormatter
        Set: Formatter(self: ClientOperation) = value
        """
        ...

    @property
    def IsInitiating(self) -> bool:
        """
        Get: IsInitiating(self: ClientOperation) -> bool
        Set: IsInitiating(self: ClientOperation) = value
        """
        ...

    @property
    def IsOneWay(self) -> bool:
        """
        Get: IsOneWay(self: ClientOperation) -> bool
        Set: IsOneWay(self: ClientOperation) = value
        """
        ...

    @property
    def IsTerminating(self) -> bool:
        """
        Get: IsTerminating(self: ClientOperation) -> bool
        Set: IsTerminating(self: ClientOperation) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ClientOperation) -> str """
        ...

    @property
    def Parent(self): # -> ClientRuntime
        """ Get: Parent(self: ClientOperation) -> ClientRuntime """
        ...

    @property
    def ReplyAction(self) -> str:
        """ Get: ReplyAction(self: ClientOperation) -> str """
        ...

    @property
    def SerializeRequest(self) -> bool:
        """
        Get: SerializeRequest(self: ClientOperation) -> bool
        Set: SerializeRequest(self: ClientOperation) = value
        """
        ...

    @property
    def SyncMethod(self) -> MethodInfo:
        """
        Get: SyncMethod(self: ClientOperation) -> MethodInfo
        Set: SyncMethod(self: ClientOperation) = value
        """
        ...

    @property
    def TaskMethod(self) -> MethodInfo:
        """
        Get: TaskMethod(self: ClientOperation) -> MethodInfo
        Set: TaskMethod(self: ClientOperation) = value
        """
        ...

    @property
    def TaskTResult(self) -> Type:
        """
        Get: TaskTResult(self: ClientOperation) -> Type
        Set: TaskTResult(self: ClientOperation) = value
        """
        ...


    def __new__(cls, parent, name:str, action:str, replyAction:str = ...) -> Self: # Not found arg types: {'parent': 'ClientRuntime'}
        """
        __new__(cls: type, parent: ClientRuntime, name: str, action: str)
        __new__(cls: type, parent: ClientRuntime, name: str, action: str, replyAction: str)
        """
        ...


class ClientRuntimeCompatBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def MessageInspectors(self) -> IList:
        """ Get: MessageInspectors(self: ClientRuntimeCompatBase) -> IList[IClientMessageInspector] """
        ...

    @property
    def Operations(self) -> KeyedCollection:
        """ Get: Operations(self: ClientRuntimeCompatBase) -> KeyedCollection[str, ClientOperation] """
        ...



class ClientRuntime(ClientRuntimeCompatBase): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CallbackClientType(self) -> Type:
        """
        Get: CallbackClientType(self: ClientRuntime) -> Type
        Set: CallbackClientType(self: ClientRuntime) = value
        """
        ...

    @property
    def CallbackDispatchRuntime(self): # -> DispatchRuntime
        """ Get: CallbackDispatchRuntime(self: ClientRuntime) -> DispatchRuntime """
        ...

    @property
    def ChannelInitializers(self) -> SynchronizedCollection:
        """ Get: ChannelInitializers(self: ClientRuntime) -> SynchronizedCollection[IChannelInitializer] """
        ...

    @property
    def ClientMessageInspectors(self) -> ICollection:
        """ Get: ClientMessageInspectors(self: ClientRuntime) -> ICollection[IClientMessageInspector] """
        ...

    @property
    def ClientOperations(self) -> ICollection:
        """ Get: ClientOperations(self: ClientRuntime) -> ICollection[ClientOperation] """
        ...

    @property
    def ContractClientType(self) -> Type:
        """
        Get: ContractClientType(self: ClientRuntime) -> Type
        Set: ContractClientType(self: ClientRuntime) = value
        """
        ...

    @property
    def ContractName(self) -> str:
        """ Get: ContractName(self: ClientRuntime) -> str """
        ...

    @property
    def ContractNamespace(self) -> str:
        """ Get: ContractNamespace(self: ClientRuntime) -> str """
        ...

    @property
    def InteractiveChannelInitializers(self) -> SynchronizedCollection:
        """ Get: InteractiveChannelInitializers(self: ClientRuntime) -> SynchronizedCollection[IInteractiveChannelInitializer] """
        ...

    @property
    def ManualAddressing(self) -> bool:
        """
        Get: ManualAddressing(self: ClientRuntime) -> bool
        Set: ManualAddressing(self: ClientRuntime) = value
        """
        ...

    @property
    def MaxFaultSize(self) -> int:
        """
        Get: MaxFaultSize(self: ClientRuntime) -> int
        Set: MaxFaultSize(self: ClientRuntime) = value
        """
        ...

    @property
    def MessageVersionNoneFaultsEnabled(self) -> bool:
        """
        Get: MessageVersionNoneFaultsEnabled(self: ClientRuntime) -> bool
        Set: MessageVersionNoneFaultsEnabled(self: ClientRuntime) = value
        """
        ...

    @property
    def OperationSelector(self): # -> IClientOperationSelector
        """
        Get: OperationSelector(self: ClientRuntime) -> IClientOperationSelector
        Set: OperationSelector(self: ClientRuntime) = value
        """
        ...

    @property
    def UnhandledClientOperation(self) -> ClientOperation:
        """ Get: UnhandledClientOperation(self: ClientRuntime) -> ClientOperation """
        ...

    @property
    def ValidateMustUnderstand(self) -> bool:
        """
        Get: ValidateMustUnderstand(self: ClientRuntime) -> bool
        Set: ValidateMustUnderstand(self: ClientRuntime) = value
        """
        ...

    @property
    def Via(self) -> Uri:
        """
        Get: Via(self: ClientRuntime) -> Uri
        Set: Via(self: ClientRuntime) = value
        """
        ...



class DispatchOperation: # skipped bases: <type 'object'>, <type 'object'>
    """
    DispatchOperation(parent: DispatchRuntime, name: str, action: str)
    DispatchOperation(parent: DispatchRuntime, name: str, action: str, replyAction: str)
    """
    @property
    def Action(self) -> str:
        """ Get: Action(self: DispatchOperation) -> str """
        ...

    @property
    def AutoDisposeParameters(self) -> bool:
        """
        Get: AutoDisposeParameters(self: DispatchOperation) -> bool
        Set: AutoDisposeParameters(self: DispatchOperation) = value
        """
        ...

    @property
    def CallContextInitializers(self) -> SynchronizedCollection:
        """ Get: CallContextInitializers(self: DispatchOperation) -> SynchronizedCollection[ICallContextInitializer] """
        ...

    @property
    def DeserializeRequest(self) -> bool:
        """
        Get: DeserializeRequest(self: DispatchOperation) -> bool
        Set: DeserializeRequest(self: DispatchOperation) = value
        """
        ...

    @property
    def FaultContractInfos(self) -> SynchronizedCollection:
        """ Get: FaultContractInfos(self: DispatchOperation) -> SynchronizedCollection[FaultContractInfo] """
        ...

    @property
    def Formatter(self): # -> IDispatchMessageFormatter
        """
        Get: Formatter(self: DispatchOperation) -> IDispatchMessageFormatter
        Set: Formatter(self: DispatchOperation) = value
        """
        ...

    @property
    def Impersonation(self) -> ImpersonationOption:
        """
        Get: Impersonation(self: DispatchOperation) -> ImpersonationOption
        Set: Impersonation(self: DispatchOperation) = value
        """
        ...

    @property
    def Invoker(self): # -> IOperationInvoker
        """
        Get: Invoker(self: DispatchOperation) -> IOperationInvoker
        Set: Invoker(self: DispatchOperation) = value
        """
        ...

    @property
    def IsInsideTransactedReceiveScope(self) -> bool:
        """
        Get: IsInsideTransactedReceiveScope(self: DispatchOperation) -> bool
        Set: IsInsideTransactedReceiveScope(self: DispatchOperation) = value
        """
        ...

    @property
    def IsOneWay(self) -> bool:
        """ Get: IsOneWay(self: DispatchOperation) -> bool """
        ...

    @property
    def IsTerminating(self) -> bool:
        """
        Get: IsTerminating(self: DispatchOperation) -> bool
        Set: IsTerminating(self: DispatchOperation) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DispatchOperation) -> str """
        ...

    @property
    def ParameterInspectors(self) -> SynchronizedCollection:
        """ Get: ParameterInspectors(self: DispatchOperation) -> SynchronizedCollection[IParameterInspector] """
        ...

    @property
    def Parent(self): # -> DispatchRuntime
        """ Get: Parent(self: DispatchOperation) -> DispatchRuntime """
        ...

    @property
    def ReleaseInstanceAfterCall(self) -> bool:
        """
        Get: ReleaseInstanceAfterCall(self: DispatchOperation) -> bool
        Set: ReleaseInstanceAfterCall(self: DispatchOperation) = value
        """
        ...

    @property
    def ReleaseInstanceBeforeCall(self) -> bool:
        """
        Get: ReleaseInstanceBeforeCall(self: DispatchOperation) -> bool
        Set: ReleaseInstanceBeforeCall(self: DispatchOperation) = value
        """
        ...

    @property
    def ReplyAction(self) -> str:
        """ Get: ReplyAction(self: DispatchOperation) -> str """
        ...

    @property
    def SerializeReply(self) -> bool:
        """
        Get: SerializeReply(self: DispatchOperation) -> bool
        Set: SerializeReply(self: DispatchOperation) = value
        """
        ...

    @property
    def TransactionAutoComplete(self) -> bool:
        """
        Get: TransactionAutoComplete(self: DispatchOperation) -> bool
        Set: TransactionAutoComplete(self: DispatchOperation) = value
        """
        ...

    @property
    def TransactionRequired(self) -> bool:
        """
        Get: TransactionRequired(self: DispatchOperation) -> bool
        Set: TransactionRequired(self: DispatchOperation) = value
        """
        ...



class DispatchRuntime: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AutomaticInputSessionShutdown(self) -> bool:
        """
        Get: AutomaticInputSessionShutdown(self: DispatchRuntime) -> bool
        Set: AutomaticInputSessionShutdown(self: DispatchRuntime) = value
        """
        ...

    @property
    def CallbackClientRuntime(self) -> ClientRuntime:
        """ Get: CallbackClientRuntime(self: DispatchRuntime) -> ClientRuntime """
        ...

    @property
    def ChannelDispatcher(self) -> ChannelDispatcher:
        """ Get: ChannelDispatcher(self: DispatchRuntime) -> ChannelDispatcher """
        ...

    @property
    def ConcurrencyMode(self) -> ConcurrencyMode:
        """
        Get: ConcurrencyMode(self: DispatchRuntime) -> ConcurrencyMode
        Set: ConcurrencyMode(self: DispatchRuntime) = value
        """
        ...

    @property
    def EndpointDispatcher(self): # -> EndpointDispatcher
        """ Get: EndpointDispatcher(self: DispatchRuntime) -> EndpointDispatcher """
        ...

    @property
    def EnsureOrderedDispatch(self) -> bool:
        """
        Get: EnsureOrderedDispatch(self: DispatchRuntime) -> bool
        Set: EnsureOrderedDispatch(self: DispatchRuntime) = value
        """
        ...

    @property
    def ExternalAuthorizationPolicies(self) -> ReadOnlyCollection:
        """
        Get: ExternalAuthorizationPolicies(self: DispatchRuntime) -> ReadOnlyCollection[IAuthorizationPolicy]
        Set: ExternalAuthorizationPolicies(self: DispatchRuntime) = value
        """
        ...

    @property
    def IgnoreTransactionMessageProperty(self) -> bool:
        """
        Get: IgnoreTransactionMessageProperty(self: DispatchRuntime) -> bool
        Set: IgnoreTransactionMessageProperty(self: DispatchRuntime) = value
        """
        ...

    @property
    def ImpersonateCallerForAllOperations(self) -> bool:
        """
        Get: ImpersonateCallerForAllOperations(self: DispatchRuntime) -> bool
        Set: ImpersonateCallerForAllOperations(self: DispatchRuntime) = value
        """
        ...

    @property
    def ImpersonateOnSerializingReply(self) -> bool:
        """
        Get: ImpersonateOnSerializingReply(self: DispatchRuntime) -> bool
        Set: ImpersonateOnSerializingReply(self: DispatchRuntime) = value
        """
        ...

    @property
    def InputSessionShutdownHandlers(self) -> SynchronizedCollection:
        """ Get: InputSessionShutdownHandlers(self: DispatchRuntime) -> SynchronizedCollection[IInputSessionShutdown] """
        ...

    @property
    def InstanceContextInitializers(self) -> SynchronizedCollection:
        """ Get: InstanceContextInitializers(self: DispatchRuntime) -> SynchronizedCollection[IInstanceContextInitializer] """
        ...

    @property
    def InstanceContextProvider(self): # -> IInstanceContextProvider
        """
        Get: InstanceContextProvider(self: DispatchRuntime) -> IInstanceContextProvider
        Set: InstanceContextProvider(self: DispatchRuntime) = value
        """
        ...

    @property
    def InstanceProvider(self): # -> IInstanceProvider
        """
        Get: InstanceProvider(self: DispatchRuntime) -> IInstanceProvider
        Set: InstanceProvider(self: DispatchRuntime) = value
        """
        ...

    @property
    def MessageAuthenticationAuditLevel(self) -> AuditLevel:
        """
        Get: MessageAuthenticationAuditLevel(self: DispatchRuntime) -> AuditLevel
        Set: MessageAuthenticationAuditLevel(self: DispatchRuntime) = value
        """
        ...

    @property
    def MessageInspectors(self) -> SynchronizedCollection:
        """ Get: MessageInspectors(self: DispatchRuntime) -> SynchronizedCollection[IDispatchMessageInspector] """
        ...

    @property
    def Operations(self) -> SynchronizedKeyedCollection:
        """ Get: Operations(self: DispatchRuntime) -> SynchronizedKeyedCollection[str, DispatchOperation] """
        ...

    @property
    def OperationSelector(self): # -> IDispatchOperationSelector
        """
        Get: OperationSelector(self: DispatchRuntime) -> IDispatchOperationSelector
        Set: OperationSelector(self: DispatchRuntime) = value
        """
        ...

    @property
    def PreserveMessage(self) -> bool:
        """
        Get: PreserveMessage(self: DispatchRuntime) -> bool
        Set: PreserveMessage(self: DispatchRuntime) = value
        """
        ...

    @property
    def PrincipalPermissionMode(self): # -> PrincipalPermissionMode
        """
        Get: PrincipalPermissionMode(self: DispatchRuntime) -> PrincipalPermissionMode
        Set: PrincipalPermissionMode(self: DispatchRuntime) = value
        """
        ...

    @property
    def ReleaseServiceInstanceOnTransactionComplete(self) -> bool:
        """
        Get: ReleaseServiceInstanceOnTransactionComplete(self: DispatchRuntime) -> bool
        Set: ReleaseServiceInstanceOnTransactionComplete(self: DispatchRuntime) = value
        """
        ...

    @property
    def RoleProvider(self) -> RoleProvider:
        """
        Get: RoleProvider(self: DispatchRuntime) -> RoleProvider
        Set: RoleProvider(self: DispatchRuntime) = value
        """
        ...

    @property
    def SecurityAuditLogLocation(self) -> AuditLogLocation:
        """
        Get: SecurityAuditLogLocation(self: DispatchRuntime) -> AuditLogLocation
        Set: SecurityAuditLogLocation(self: DispatchRuntime) = value
        """
        ...

    @property
    def ServiceAuthenticationManager(self) -> ServiceAuthenticationManager:
        """
        Get: ServiceAuthenticationManager(self: DispatchRuntime) -> ServiceAuthenticationManager
        Set: ServiceAuthenticationManager(self: DispatchRuntime) = value
        """
        ...

    @property
    def ServiceAuthorizationAuditLevel(self) -> AuditLevel:
        """
        Get: ServiceAuthorizationAuditLevel(self: DispatchRuntime) -> AuditLevel
        Set: ServiceAuthorizationAuditLevel(self: DispatchRuntime) = value
        """
        ...

    @property
    def ServiceAuthorizationManager(self) -> ServiceAuthorizationManager:
        """
        Get: ServiceAuthorizationManager(self: DispatchRuntime) -> ServiceAuthorizationManager
        Set: ServiceAuthorizationManager(self: DispatchRuntime) = value
        """
        ...

    @property
    def SingletonInstanceContext(self) -> InstanceContext:
        """
        Get: SingletonInstanceContext(self: DispatchRuntime) -> InstanceContext
        Set: SingletonInstanceContext(self: DispatchRuntime) = value
        """
        ...

    @property
    def SuppressAuditFailure(self) -> bool:
        """
        Get: SuppressAuditFailure(self: DispatchRuntime) -> bool
        Set: SuppressAuditFailure(self: DispatchRuntime) = value
        """
        ...

    @property
    def SynchronizationContext(self) -> SynchronizationContext:
        """
        Get: SynchronizationContext(self: DispatchRuntime) -> SynchronizationContext
        Set: SynchronizationContext(self: DispatchRuntime) = value
        """
        ...

    @property
    def TransactionAutoCompleteOnSessionClose(self) -> bool:
        """
        Get: TransactionAutoCompleteOnSessionClose(self: DispatchRuntime) -> bool
        Set: TransactionAutoCompleteOnSessionClose(self: DispatchRuntime) = value
        """
        ...

    @property
    def Type(self) -> Type:
        """
        Get: Type(self: DispatchRuntime) -> Type
        Set: Type(self: DispatchRuntime) = value
        """
        ...

    @property
    def UnhandledDispatchOperation(self) -> DispatchOperation:
        """
        Get: UnhandledDispatchOperation(self: DispatchRuntime) -> DispatchOperation
        Set: UnhandledDispatchOperation(self: DispatchRuntime) = value
        """
        ...

    @property
    def ValidateMustUnderstand(self) -> bool:
        """
        Get: ValidateMustUnderstand(self: DispatchRuntime) -> bool
        Set: ValidateMustUnderstand(self: DispatchRuntime) = value
        """
        ...



class DurableOperationContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId() -> Guid """
        ...


    @staticmethod
    def AbortInstance(): # -> 
        """ AbortInstance() """
        ...

    @staticmethod
    def CompleteInstance(): # -> 
        """ CompleteInstance() """
        ...

    __all__: list = ...


class EndpointAddressMessageFilter(MessageFilter): # skipped bases: <type 'object'>
    """
    EndpointAddressMessageFilter(address: EndpointAddress)
    EndpointAddressMessageFilter(address: EndpointAddress, includeHostNameInComparison: bool)
    """
    @property
    def Address(self) -> EndpointAddress:
        """ Get: Address(self: EndpointAddressMessageFilter) -> EndpointAddress """
        ...

    @property
    def IncludeHostNameInComparison(self) -> bool:
        """ Get: IncludeHostNameInComparison(self: EndpointAddressMessageFilter) -> bool """
        ...


    def __new__(cls, address:EndpointAddress, includeHostNameInComparison:bool = ...) -> Self:
        """
        __new__(cls: type, address: EndpointAddress)
        __new__(cls: type, address: EndpointAddress, includeHostNameInComparison: bool)
        """
        ...


class EndpointDispatcher: # skipped bases: <type 'object'>, <type 'object'>
    """
    EndpointDispatcher(address: EndpointAddress, contractName: str, contractNamespace: str)
    EndpointDispatcher(address: EndpointAddress, contractName: str, contractNamespace: str, isSystemEndpoint: bool)
    """
    @property
    def AddressFilter(self) -> MessageFilter:
        """
        Get: AddressFilter(self: EndpointDispatcher) -> MessageFilter
        Set: AddressFilter(self: EndpointDispatcher) = value
        """
        ...

    @property
    def ChannelDispatcher(self) -> ChannelDispatcher:
        """ Get: ChannelDispatcher(self: EndpointDispatcher) -> ChannelDispatcher """
        ...

    @property
    def ContractFilter(self) -> MessageFilter:
        """
        Get: ContractFilter(self: EndpointDispatcher) -> MessageFilter
        Set: ContractFilter(self: EndpointDispatcher) = value
        """
        ...

    @property
    def ContractName(self) -> str:
        """ Get: ContractName(self: EndpointDispatcher) -> str """
        ...

    @property
    def ContractNamespace(self) -> str:
        """ Get: ContractNamespace(self: EndpointDispatcher) -> str """
        ...

    @property
    def DispatchRuntime(self) -> DispatchRuntime:
        """ Get: DispatchRuntime(self: EndpointDispatcher) -> DispatchRuntime """
        ...

    @property
    def EndpointAddress(self) -> EndpointAddress:
        """ Get: EndpointAddress(self: EndpointDispatcher) -> EndpointAddress """
        ...

    @property
    def FilterPriority(self) -> int:
        """
        Get: FilterPriority(self: EndpointDispatcher) -> int
        Set: FilterPriority(self: EndpointDispatcher) = value
        """
        ...

    @property
    def IsSystemEndpoint(self) -> bool:
        """ Get: IsSystemEndpoint(self: EndpointDispatcher) -> bool """
        ...



class ExceptionHandler: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AlwaysHandle(self) -> ExceptionHandler:
        """ Get: AlwaysHandle() -> ExceptionHandler """
        ...

    @property
    def AsynchronousThreadExceptionHandler(self) -> ExceptionHandler:
        """
        Get: AsynchronousThreadExceptionHandler() -> ExceptionHandler
        Set: AsynchronousThreadExceptionHandler() = value
        """
        ...

    @property
    def TransportExceptionHandler(self) -> ExceptionHandler:
        """
        Get: TransportExceptionHandler() -> ExceptionHandler
        Set: TransportExceptionHandler() = value
        """
        ...


    def HandleException(self, exception:Exception) -> bool:
        """ HandleException(self: ExceptionHandler, exception: Exception) -> bool """
        ...



class FaultContractInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ FaultContractInfo(action: str, detail: Type) """
    @property
    def Action(self) -> str:
        """ Get: Action(self: FaultContractInfo) -> str """
        ...

    @property
    def Detail(self) -> Type:
        """ Get: Detail(self: FaultContractInfo) -> Type """
        ...



class InvalidBodyAccessException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    SerializeObjectState = ...


class FilterInvalidBodyAccessException(InvalidBodyAccessException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    FilterInvalidBodyAccessException()
    FilterInvalidBodyAccessException(message: str)
    FilterInvalidBodyAccessException(message: str, innerException: Exception)
    FilterInvalidBodyAccessException(message: str, filters: Collection[MessageFilter])
    FilterInvalidBodyAccessException(message: str, innerException: Exception, filters: Collection[MessageFilter])
    """
    @property
    def Filters(self) -> Collection:
        """ Get: Filters(self: FilterInvalidBodyAccessException) -> Collection[MessageFilter] """
        ...


    SerializeObjectState = ...


class ICallContextInitializer: # skipped bases: <type 'object'>
    """ no doc """
    def AfterInvoke(self, correlationState:object): # -> 
        """ AfterInvoke(self: ICallContextInitializer, correlationState: object) """
        ...

    def BeforeInvoke(self, instanceContext:InstanceContext, channel:IClientChannel, message:Message) -> object:
        """ BeforeInvoke(self: ICallContextInitializer, instanceContext: InstanceContext, channel: IClientChannel, message: Message) -> object """
        ...


class IChannelInitializer: # skipped bases: <type 'object'>
    """ no doc """
    def Initialize(self, channel:IClientChannel): # -> 
        """ Initialize(self: IChannelInitializer, channel: IClientChannel) """
        ...


class IClientMessageFormatter: # skipped bases: <type 'object'>
    """ no doc """
    def DeserializeReply(self, message:Message, parameters:Array) -> object:
        """ DeserializeReply(self: IClientMessageFormatter, message: Message, parameters: Array[object]) -> object """
        ...

    def SerializeRequest(self, messageVersion, parameters:Array) -> Message: # Not found arg types: {'messageVersion': 'MessageVersion'}
        """ SerializeRequest(self: IClientMessageFormatter, messageVersion: MessageVersion, parameters: Array[object]) -> Message """
        ...


class IClientMessageInspector: # skipped bases: <type 'object'>
    """ no doc """
    def AfterReceiveReply(self, reply:Message, correlationState:object) -> Message:
        """ AfterReceiveReply(self: IClientMessageInspector, reply: Message, correlationState: object) -> Message """
        ...

    def BeforeSendRequest(self, request:Message, channel:IClientChannel) -> Tuple_[object, Message]:
        """ BeforeSendRequest(self: IClientMessageInspector, request: Message, channel: IClientChannel) -> (object, Message) """
        ...


class IClientOperationSelector: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AreParametersRequiredForSelection(self) -> bool:
        """ Get: AreParametersRequiredForSelection(self: IClientOperationSelector) -> bool """
        ...


    def SelectOperation(self, method:MethodBase, parameters:Array) -> str:
        """ SelectOperation(self: IClientOperationSelector, method: MethodBase, parameters: Array[object]) -> str """
        ...


class IDispatchMessageFormatter: # skipped bases: <type 'object'>
    """ no doc """
    def DeserializeRequest(self, message:Message, parameters:Array): # -> 
        """ DeserializeRequest(self: IDispatchMessageFormatter, message: Message, parameters: Array[object]) """
        ...

    def SerializeReply(self, messageVersion, parameters:Array, result:object) -> Message: # Not found arg types: {'messageVersion': 'MessageVersion'}
        """ SerializeReply(self: IDispatchMessageFormatter, messageVersion: MessageVersion, parameters: Array[object], result: object) -> Message """
        ...


class IDispatchMessageInspector: # skipped bases: <type 'object'>
    """ no doc """
    def AfterReceiveRequest(self, request:Message, channel:IClientChannel, instanceContext:InstanceContext) -> Tuple_[object, Message]:
        """ AfterReceiveRequest(self: IDispatchMessageInspector, request: Message, channel: IClientChannel, instanceContext: InstanceContext) -> (object, Message) """
        ...

    def BeforeSendReply(self, reply:Message, correlationState:object) -> Message:
        """ BeforeSendReply(self: IDispatchMessageInspector, reply: Message, correlationState: object) -> Message """
        ...


class IDispatchOperationSelector: # skipped bases: <type 'object'>
    """ no doc """
    def SelectOperation(self, message:Message) -> Tuple_[str, Message]:
        """ SelectOperation(self: IDispatchOperationSelector, message: Message) -> (str, Message) """
        ...


class IErrorHandler: # skipped bases: <type 'object'>
    """ no doc """
    def HandleError(self, error:Exception) -> bool:
        """ HandleError(self: IErrorHandler, error: Exception) -> bool """
        ...

    def ProvideFault(self, error:Exception, version, fault:Message) -> Message: # Not found arg types: {'version': 'MessageVersion'}
        """ ProvideFault(self: IErrorHandler, error: Exception, version: MessageVersion, fault: Message) -> Message """
        ...


class IInputSessionShutdown: # skipped bases: <type 'object'>
    """ no doc """
    def ChannelFaulted(self, channel:IDuplexContextChannel): # -> 
        """ ChannelFaulted(self: IInputSessionShutdown, channel: IDuplexContextChannel) """
        ...

    def DoneReceiving(self, channel:IDuplexContextChannel): # -> 
        """ DoneReceiving(self: IInputSessionShutdown, channel: IDuplexContextChannel) """
        ...


class IInstanceContextInitializer: # skipped bases: <type 'object'>
    """ no doc """
    def Initialize(self, instanceContext:InstanceContext, message:Message): # -> 
        """ Initialize(self: IInstanceContextInitializer, instanceContext: InstanceContext, message: Message) """
        ...


class IInstanceContextProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetExistingInstanceContext(self, message:Message, channel:IContextChannel) -> InstanceContext:
        """ GetExistingInstanceContext(self: IInstanceContextProvider, message: Message, channel: IContextChannel) -> InstanceContext """
        ...

    def InitializeInstanceContext(self, instanceContext:InstanceContext, message:Message, channel:IContextChannel): # -> 
        """ InitializeInstanceContext(self: IInstanceContextProvider, instanceContext: InstanceContext, message: Message, channel: IContextChannel) """
        ...

    def IsIdle(self, instanceContext:InstanceContext) -> bool:
        """ IsIdle(self: IInstanceContextProvider, instanceContext: InstanceContext) -> bool """
        ...

    def NotifyIdle(self, callback, instanceContext:InstanceContext): # ->  # Not found arg types: {'callback': 'InstanceContextIdleCallback'}
        """ NotifyIdle(self: IInstanceContextProvider, callback: InstanceContextIdleCallback, instanceContext: InstanceContext) """
        ...


class IInstanceProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetInstance(self, instanceContext:InstanceContext, message:Message = ...) -> object:
        """
        GetInstance(self: IInstanceProvider, instanceContext: InstanceContext) -> object
        GetInstance(self: IInstanceProvider, instanceContext: InstanceContext, message: Message) -> object
        """
        ...

    def ReleaseInstance(self, instanceContext:InstanceContext, instance:object): # -> 
        """ ReleaseInstance(self: IInstanceProvider, instanceContext: InstanceContext, instance: object) """
        ...


class IInteractiveChannelInitializer: # skipped bases: <type 'object'>
    """ no doc """
    def BeginDisplayInitializationUI(self, channel:IClientChannel, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginDisplayInitializationUI(self: IInteractiveChannelInitializer, channel: IClientChannel, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndDisplayInitializationUI(self, result:IAsyncResult): # -> 
        """ EndDisplayInitializationUI(self: IInteractiveChannelInitializer, result: IAsyncResult) """
        ...


class IMessageFilterTable(IDictionary): # skipped bases: <type 'IEnumerable[KeyValuePair[MessageFilter, TFilterData]]'>, <type 'IEnumerable'>, <type 'ICollection[KeyValuePair[MessageFilter, TFilterData]]'>, <type 'object'>
    """ no doc """
    def GetMatchingFilter(self, *__args:Message) -> Tuple_[bool, MessageFilter]:
        """
        GetMatchingFilter(self: IMessageFilterTable[TFilterData], message: Message) -> (bool, MessageFilter)
        GetMatchingFilter(self: IMessageFilterTable[TFilterData], messageBuffer: MessageBuffer) -> (bool, MessageFilter)
        """
        ...

    def GetMatchingFilters(self, *__args) -> bool:
        """
        GetMatchingFilters(self: IMessageFilterTable[TFilterData], message: Message, results: ICollection[MessageFilter]) -> bool
        GetMatchingFilters(self: IMessageFilterTable[TFilterData], messageBuffer: MessageBuffer, results: ICollection[MessageFilter]) -> bool
        """
        ...

    def GetMatchingValue(self, *__args:Message): # -> Tuple_[bool, TFilterData]
        """
        GetMatchingValue(self: IMessageFilterTable[TFilterData], message: Message) -> (bool, TFilterData)
        GetMatchingValue(self: IMessageFilterTable[TFilterData], messageBuffer: MessageBuffer) -> (bool, TFilterData)
        """
        ...

    def GetMatchingValues(self, *__args) -> bool:
        """
        GetMatchingValues(self: IMessageFilterTable[TFilterData], message: Message, results: ICollection[TFilterData]) -> bool
        GetMatchingValues(self: IMessageFilterTable[TFilterData], messageBuffer: MessageBuffer, results: ICollection[TFilterData]) -> bool
        """
        ...


class InstanceContextIdleCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InstanceContextIdleCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, instanceContext:InstanceContext, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InstanceContextIdleCallback, instanceContext: InstanceContext, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InstanceContextIdleCallback, result: IAsyncResult) """
        ...

    def Invoke(self, instanceContext:InstanceContext): # -> 
        """ Invoke(self: InstanceContextIdleCallback, instanceContext: InstanceContext) """
        ...


class IOperationInvoker: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsSynchronous(self) -> bool:
        """ Get: IsSynchronous(self: IOperationInvoker) -> bool """
        ...


    def AllocateInputs(self) -> Array:
        """ AllocateInputs(self: IOperationInvoker) -> Array[object] """
        ...

    def Invoke(self, instance, inputs, outputs) -> Tuple_[object, Array]:
        """ Invoke(self: IOperationInvoker, instance: object, inputs: Array[object]) -> (object, Array[object]) """
        ...

    def InvokeBegin(self, instance:object, inputs:Array, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ InvokeBegin(self: IOperationInvoker, instance: object, inputs: Array[object], callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def InvokeEnd(self, instance, outputs, result) -> Tuple_[object, Array]:
        """ InvokeEnd(self: IOperationInvoker, instance: object, result: IAsyncResult) -> (object, Array[object]) """
        ...


class IParameterInspector: # skipped bases: <type 'object'>
    """ no doc """
    def AfterCall(self, operationName:str, outputs:Array, returnValue:object, correlationState:object): # -> 
        """ AfterCall(self: IParameterInspector, operationName: str, outputs: Array[object], returnValue: object, correlationState: object) """
        ...

    def BeforeCall(self, operationName:str, inputs:Array) -> object:
        """ BeforeCall(self: IParameterInspector, operationName: str, inputs: Array[object]) -> object """
        ...


class QueryStringConverter: # skipped bases: <type 'object'>, <type 'object'>
    """ QueryStringConverter() """
    def CanConvert(self, type:Type) -> bool:
        """ CanConvert(self: QueryStringConverter, type: Type) -> bool """
        ...

    def ConvertStringToValue(self, parameter:str, parameterType:Type) -> object:
        """ ConvertStringToValue(self: QueryStringConverter, parameter: str, parameterType: Type) -> object """
        ...

    def ConvertValueToString(self, parameter:object, parameterType:Type) -> str:
        """ ConvertValueToString(self: QueryStringConverter, parameter: object, parameterType: Type) -> str """
        ...


class JsonQueryStringConverter(QueryStringConverter): # skipped bases: <type 'object'>
    """ JsonQueryStringConverter() """
    pass

class MatchAllMessageFilter(MessageFilter): # skipped bases: <type 'object'>
    """ MatchAllMessageFilter() """
    pass

class MatchNoneMessageFilter(MessageFilter): # skipped bases: <type 'object'>
    """ MatchNoneMessageFilter() """
    pass

class MessageFilterException(CommunicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MessageFilterException()
    MessageFilterException(message: str)
    MessageFilterException(message: str, innerException: Exception)
    MessageFilterException(message: str, filters: Collection[MessageFilter])
    MessageFilterException(message: str, innerException: Exception, filters: Collection[MessageFilter])
    """
    @property
    def Filters(self) -> Collection:
        """ Get: Filters(self: MessageFilterException) -> Collection[MessageFilter] """
        ...


    SerializeObjectState = ...


class MessageFilterTable(IMessageFilterTable): # skipped bases: <type 'ICollection[KeyValuePair[MessageFilter, TFilterData]]'>, <type 'IEnumerable'>, <type 'IDictionary[MessageFilter, TFilterData]'>, <type 'IEnumerable[KeyValuePair[MessageFilter, TFilterData]]'>, <type 'object'>
    """
    MessageFilterTable[TFilterData]()
    MessageFilterTable[TFilterData](defaultPriority: int)
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: MessageFilterTable[TFilterData]) -> int """
        ...

    @property
    def DefaultPriority(self) -> int:
        """
        Get: DefaultPriority(self: MessageFilterTable[TFilterData]) -> int
        Set: DefaultPriority(self: MessageFilterTable[TFilterData]) = value
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: MessageFilterTable[TFilterData]) -> bool """
        ...

    @property
    def Keys(self) -> ICollection:
        """ Get: Keys(self: MessageFilterTable[TFilterData]) -> ICollection[MessageFilter] """
        ...

    @property
    def Values(self) -> ICollection:
        """ Get: Values(self: MessageFilterTable[TFilterData]) -> ICollection[TFilterData] """
        ...


    def Add(self, *__args:KeyValuePair): # -> 
        """ Add(self: MessageFilterTable[TFilterData], filter: MessageFilter, data: TFilterData)Add(self: MessageFilterTable[TFilterData], filter: MessageFilter, data: TFilterData, priority: int)Add(self: MessageFilterTable[TFilterData], item: KeyValuePair[MessageFilter, TFilterData]) """
        ...

    def Clear(self): # -> 
        """ Clear(self: MessageFilterTable[TFilterData]) """
        ...

    def Contains(self, item:KeyValuePair) -> bool:
        """ Contains(self: MessageFilterTable[TFilterData], item: KeyValuePair[MessageFilter, TFilterData]) -> bool """
        ...

    def ContainsKey(self, filter:MessageFilter) -> bool:
        """ ContainsKey(self: MessageFilterTable[TFilterData], filter: MessageFilter) -> bool """
        ...

    def CopyTo(self, array:Array, arrayIndex:int): # -> 
        """ CopyTo(self: MessageFilterTable[TFilterData], array: Array[KeyValuePair[MessageFilter, TFilterData]], arrayIndex: int) """
        ...

    def CreateFilterTable(self, *args): #cannot find CLR method
        """ CreateFilterTable(self: MessageFilterTable[TFilterData], filter: MessageFilter) -> IMessageFilterTable[TFilterData] """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: MessageFilterTable[TFilterData]) -> IEnumerator[KeyValuePair[MessageFilter, TFilterData]] """
        ...

    def GetPriority(self, filter:MessageFilter) -> int:
        """ GetPriority(self: MessageFilterTable[TFilterData], filter: MessageFilter) -> int """
        ...

    def Remove(self, *__args:MessageFilter) -> bool:
        """
        Remove(self: MessageFilterTable[TFilterData], filter: MessageFilter) -> bool
        Remove(self: MessageFilterTable[TFilterData], item: KeyValuePair[MessageFilter, TFilterData]) -> bool
        """
        ...

    def TryGetValue(self, filter, data): # -> Tuple_[bool, TFilterData]
        """ TryGetValue(self: MessageFilterTable[TFilterData], filter: MessageFilter) -> (bool, TFilterData) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class MessageQuery: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateMessageQueryCollection(self): # -> MessageQueryCollection
        """ CreateMessageQueryCollection(self: MessageQuery) -> MessageQueryCollection """
        ...

    def Evaluate(self, *__args:Message): # -> TResult
        """
        Evaluate[TResult](self: MessageQuery, message: Message) -> TResult
        Evaluate[TResult](self: MessageQuery, buffer: MessageBuffer) -> TResult
        """
        ...


class MessageQueryCollection(Collection): # skipped bases: <type 'IEnumerable[MessageQuery]'>, <type 'IReadOnlyList[MessageQuery]'>, <type 'IEnumerable'>, <type 'ICollection[MessageQuery]'>, <type 'IList'>, <type 'IList[MessageQuery]'>, <type 'IReadOnlyCollection[MessageQuery]'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Evaluate(self, *__args:Message) -> IEnumerable:
        """
        Evaluate[TResult](self: MessageQueryCollection, message: Message) -> IEnumerable[KeyValuePair[MessageQuery, TResult]]
        Evaluate[TResult](self: MessageQueryCollection, buffer: MessageBuffer) -> IEnumerable[KeyValuePair[MessageQuery, TResult]]
        """
        ...


class MessageQueryTable(IDictionary): # skipped bases: <type 'ICollection[KeyValuePair[MessageQuery, TItem]]'>, <type 'IEnumerable[KeyValuePair[MessageQuery, TItem]]'>, <type 'IEnumerable'>, <type 'object'>
    """ MessageQueryTable[TItem]() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: MessageQueryTable[TItem]) -> int """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: MessageQueryTable[TItem]) -> bool """
        ...


    def Clear(self): # -> 
        """ Clear(self: MessageQueryTable[TItem]) """
        ...

    def Contains(self, item:KeyValuePair) -> bool:
        """ Contains(self: MessageQueryTable[TItem], item: KeyValuePair[MessageQuery, TItem]) -> bool """
        ...

    def CopyTo(self, array:Array, arrayIndex:int): # -> 
        """ CopyTo(self: MessageQueryTable[TItem], array: Array[KeyValuePair[MessageQuery, TItem]], arrayIndex: int) """
        ...

    def Evaluate(self, *__args:Message) -> IEnumerable:
        """
        Evaluate[TResult](self: MessageQueryTable[TItem], message: Message) -> IEnumerable[KeyValuePair[MessageQuery, TResult]]
        Evaluate[TResult](self: MessageQueryTable[TItem], buffer: MessageBuffer) -> IEnumerable[KeyValuePair[MessageQuery, TResult]]
        """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: MessageQueryTable[TItem]) -> IEnumerator[KeyValuePair[MessageQuery, TItem]] """
        ...


class MultipleFilterMatchesException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MultipleFilterMatchesException()
    MultipleFilterMatchesException(message: str)
    MultipleFilterMatchesException(message: str, innerException: Exception)
    MultipleFilterMatchesException(message: str, filters: Collection[MessageFilter])
    MultipleFilterMatchesException(message: str, innerException: Exception, filters: Collection[MessageFilter])
    """
    @property
    def Filters(self) -> Collection:
        """ Get: Filters(self: MultipleFilterMatchesException) -> Collection[MessageFilter] """
        ...


    SerializeObjectState = ...


class NavigatorInvalidBodyAccessException(InvalidBodyAccessException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    NavigatorInvalidBodyAccessException()
    NavigatorInvalidBodyAccessException(message: str)
    NavigatorInvalidBodyAccessException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class PrefixEndpointAddressMessageFilter(MessageFilter): # skipped bases: <type 'object'>
    """
    PrefixEndpointAddressMessageFilter(address: EndpointAddress)
    PrefixEndpointAddressMessageFilter(address: EndpointAddress, includeHostNameInComparison: bool)
    """
    @property
    def Address(self) -> EndpointAddress:
        """ Get: Address(self: PrefixEndpointAddressMessageFilter) -> EndpointAddress """
        ...

    @property
    def IncludeHostNameInComparison(self) -> bool:
        """ Get: IncludeHostNameInComparison(self: PrefixEndpointAddressMessageFilter) -> bool """
        ...


    def __new__(cls, address:EndpointAddress, includeHostNameInComparison:bool = ...) -> Self:
        """
        __new__(cls: type, address: EndpointAddress)
        __new__(cls: type, address: EndpointAddress, includeHostNameInComparison: bool)
        """
        ...


class SeekableXPathNavigator(XPathNavigator): # skipped bases: <type 'IXPathNavigable'>, <type 'IXmlNamespaceResolver'>, <type 'ICloneable'>, <type 'object'>
    """ no doc """
    @property
    def CurrentPosition(self) -> Int64:
        """
        Get: CurrentPosition(self: SeekableXPathNavigator) -> Int64
        Set: CurrentPosition(self: SeekableXPathNavigator) = value
        """
        ...


    def GetLocalName(self, nodePosition:Int64) -> str:
        """ GetLocalName(self: SeekableXPathNavigator, nodePosition: Int64) -> str """
        ...

    def GetName(self, nodePosition:Int64) -> str:
        """ GetName(self: SeekableXPathNavigator, nodePosition: Int64) -> str """
        ...

    def GetNodeType(self, nodePosition:Int64) -> XPathNodeType:
        """ GetNodeType(self: SeekableXPathNavigator, nodePosition: Int64) -> XPathNodeType """
        ...

    def GetValue(self, nodePosition:Int64) -> str:
        """ GetValue(self: SeekableXPathNavigator, nodePosition: Int64) -> str """
        ...


class ServiceThrottle: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def MaxConcurrentCalls(self) -> int:
        """
        Get: MaxConcurrentCalls(self: ServiceThrottle) -> int
        Set: MaxConcurrentCalls(self: ServiceThrottle) = value
        """
        ...

    @property
    def MaxConcurrentInstances(self) -> int:
        """
        Get: MaxConcurrentInstances(self: ServiceThrottle) -> int
        Set: MaxConcurrentInstances(self: ServiceThrottle) = value
        """
        ...

    @property
    def MaxConcurrentSessions(self) -> int:
        """
        Get: MaxConcurrentSessions(self: ServiceThrottle) -> int
        Set: MaxConcurrentSessions(self: ServiceThrottle) = value
        """
        ...



class WebHttpDispatchOperationSelector(IDispatchOperationSelector): # skipped bases: <type 'object'>
    """ WebHttpDispatchOperationSelector(endpoint: ServiceEndpoint) """
    def GetUriTemplate(self, operationName:str) -> UriTemplate:
        """ GetUriTemplate(self: WebHttpDispatchOperationSelector, operationName: str) -> UriTemplate """
        ...

    HttpOperationNamePropertyName: str = ...
    HttpOperationSelectorUriMatchedPropertyName: str = ...


class XPathMessageContext(XsltContext): # skipped bases: <type 'IXmlNamespaceResolver'>, <type 'IEnumerable'>, <type 'object'>
    """
    XPathMessageContext()
    XPathMessageContext(table: NameTable)
    """
    pass

class XPathMessageFilter(IXmlSerializable, MessageFilter): # skipped bases: <type 'object'>
    """
    XPathMessageFilter()
    XPathMessageFilter(xpath: str)
    XPathMessageFilter(xpath: str, namespaces: XmlNamespaceManager)
    XPathMessageFilter(xpath: str, context: XsltContext)
    XPathMessageFilter(reader: XmlReader)
    XPathMessageFilter(reader: XmlReader, namespaces: XmlNamespaceManager)
    XPathMessageFilter(reader: XmlReader, context: XsltContext)
    """
    @property
    def Namespaces(self) -> XmlNamespaceManager:
        """ Get: Namespaces(self: XPathMessageFilter) -> XmlNamespaceManager """
        ...

    @property
    def NodeQuota(self) -> int:
        """
        Get: NodeQuota(self: XPathMessageFilter) -> int
        Set: NodeQuota(self: XPathMessageFilter) = value
        """
        ...

    @property
    def XPath(self) -> str:
        """ Get: XPath(self: XPathMessageFilter) -> str """
        ...


    def OnGetSchema(self, *args): #cannot find CLR method
        """ OnGetSchema(self: XPathMessageFilter) -> XmlSchema """
        ...

    def OnReadXml(self, *args): #cannot find CLR method
        """ OnReadXml(self: XPathMessageFilter, reader: XmlReader) """
        ...

    def OnWriteXml(self, *args): #cannot find CLR method
        """ OnWriteXml(self: XPathMessageFilter, writer: XmlWriter) """
        ...

    def ReadXPath(self, *args): #cannot find CLR method
        """ ReadXPath(self: XPathMessageFilter, reader: XmlReader, namespaces: XmlNamespaceManager) """
        ...

    @staticmethod
    def StaticGetSchema(schemas:XmlSchemaSet) -> XmlSchemaType:
        """ StaticGetSchema(schemas: XmlSchemaSet) -> XmlSchemaType """
        ...

    def TrimToSize(self): # -> 
        """ TrimToSize(self: XPathMessageFilter) """
        ...

    def WriteXPath(self, *args): #cannot find CLR method
        """ WriteXPath(self: XPathMessageFilter, writer: XmlWriter, resolver: IXmlNamespaceResolver) """
        ...

    def WriteXPathTo(self, writer:XmlWriter, prefix:str, localName:str, ns:str, writeNamespaces:bool): # -> 
        """ WriteXPathTo(self: XPathMessageFilter, writer: XmlWriter, prefix: str, localName: str, ns: str, writeNamespaces: bool) """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, xpath: str)
        __new__(cls: type, xpath: str, namespaces: XmlNamespaceManager)
        __new__(cls: type, xpath: str, context: XsltContext)
        __new__(cls: type, reader: XmlReader)
        __new__(cls: type, reader: XmlReader, namespaces: XmlNamespaceManager)
        __new__(cls: type, reader: XmlReader, context: XsltContext)
        """
        ...


class XPathMessageFilterTable(IMessageFilterTable): # skipped bases: <type 'IDictionary[MessageFilter, TFilterData]'>, <type 'ICollection[KeyValuePair[MessageFilter, TFilterData]]'>, <type 'IEnumerable'>, <type 'IEnumerable[KeyValuePair[MessageFilter, TFilterData]]'>, <type 'object'>
    """
    XPathMessageFilterTable[TFilterData]()
    XPathMessageFilterTable[TFilterData](capacity: int)
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: XPathMessageFilterTable[TFilterData]) -> int """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: XPathMessageFilterTable[TFilterData]) -> bool """
        ...

    @property
    def Keys(self) -> ICollection:
        """ Get: Keys(self: XPathMessageFilterTable[TFilterData]) -> ICollection[MessageFilter] """
        ...

    @property
    def NodeQuota(self) -> int:
        """
        Get: NodeQuota(self: XPathMessageFilterTable[TFilterData]) -> int
        Set: NodeQuota(self: XPathMessageFilterTable[TFilterData]) = value
        """
        ...

    @property
    def Values(self) -> ICollection:
        """ Get: Values(self: XPathMessageFilterTable[TFilterData]) -> ICollection[TFilterData] """
        ...


    def Add(self, *__args:KeyValuePair): # -> 
        """ Add(self: XPathMessageFilterTable[TFilterData], filter: MessageFilter, data: TFilterData)Add(self: XPathMessageFilterTable[TFilterData], item: KeyValuePair[MessageFilter, TFilterData])Add(self: XPathMessageFilterTable[TFilterData], filter: XPathMessageFilter, data: TFilterData) """
        ...

    def Clear(self): # -> 
        """ Clear(self: XPathMessageFilterTable[TFilterData]) """
        ...

    def Contains(self, item:KeyValuePair) -> bool:
        """ Contains(self: XPathMessageFilterTable[TFilterData], item: KeyValuePair[MessageFilter, TFilterData]) -> bool """
        ...

    def ContainsKey(self, filter:MessageFilter) -> bool:
        """ ContainsKey(self: XPathMessageFilterTable[TFilterData], filter: MessageFilter) -> bool """
        ...

    def CopyTo(self, array:Array, arrayIndex:int): # -> 
        """ CopyTo(self: XPathMessageFilterTable[TFilterData], array: Array[KeyValuePair[MessageFilter, TFilterData]], arrayIndex: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: XPathMessageFilterTable[TFilterData]) -> IEnumerator[KeyValuePair[MessageFilter, TFilterData]] """
        ...

    def Remove(self, *__args:MessageFilter) -> bool:
        """
        Remove(self: XPathMessageFilterTable[TFilterData], filter: MessageFilter) -> bool
        Remove(self: XPathMessageFilterTable[TFilterData], item: KeyValuePair[MessageFilter, TFilterData]) -> bool
        Remove(self: XPathMessageFilterTable[TFilterData], filter: XPathMessageFilter) -> bool
        """
        ...

    def TrimToSize(self): # -> 
        """ TrimToSize(self: XPathMessageFilterTable[TFilterData]) """
        ...

    def TryGetValue(self, filter, data): # -> Tuple_[bool, TFilterData]
        """ TryGetValue(self: XPathMessageFilterTable[TFilterData], filter: MessageFilter) -> (bool, TFilterData) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class XPathMessageQueryCollection(MessageQueryCollection): # skipped bases: <type 'IEnumerable[MessageQuery]'>, <type 'IReadOnlyList[MessageQuery]'>, <type 'IEnumerable'>, <type 'ICollection[MessageQuery]'>, <type 'IList'>, <type 'IList[MessageQuery]'>, <type 'IReadOnlyCollection[MessageQuery]'>, <type 'ICollection'>, <type 'object'>
    """ XPathMessageQueryCollection() """
    pass

class XPathNavigatorException(XPathException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XPathNavigatorException()
    XPathNavigatorException(message: str)
    XPathNavigatorException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class XPathResult(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ResultType(self) -> XPathResultType:
        """ Get: ResultType(self: XPathResult) -> XPathResultType """
        ...


    def GetResultAsBoolean(self) -> bool:
        """ GetResultAsBoolean(self: XPathResult) -> bool """
        ...

    def GetResultAsNodeset(self) -> XPathNodeIterator:
        """ GetResultAsNodeset(self: XPathResult) -> XPathNodeIterator """
        ...

    def GetResultAsNumber(self) -> float:
        """ GetResultAsNumber(self: XPathResult) -> float """
        ...

    def GetResultAsString(self) -> str:
        """ GetResultAsString(self: XPathResult) -> str """
        ...


