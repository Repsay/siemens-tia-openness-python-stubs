# encoding: utf-8
# module Microsoft.SqlServer.Management.Smo.Broker calls itself Broker
# from Microsoft.SqlServer.Smo, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.ServiceBrokerEnum, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Common import (IAlterable, ICreatable, 
    IDropIfExists, IDroppable, IMarkForDrop)

from Microsoft.SqlServer.Management.Sdk.Sfc import (ISfcSupportsDesignMode, 
    ISfcValidate)

from Microsoft.SqlServer.Management.Smo import (ActivationExecutionContext, 
    Database, IExtendedProperties, IObjectPermission, IScriptable, 
    NamedSmoObject, ObjectEventSet, SchemaCollectionBase, 
    ScriptNameObjectBase, ScriptSchemaObjectBase, ServerEventHandler, 
    ServiceQueueEventSet, SimpleObjectCollectionBase, SmoObjectExtender, 
    SqlSmoObject)

from System import Array, Byte, DateTime, Enum, Int16, Int64, Version

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    MessageTypeValidation, field#)
"""

# no functions
# classes

class BrokerObjectBase(ScriptNameObjectBase, IScriptable): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: BrokerObjectBase) -> str
        Set: Name(self: BrokerObjectBase) = value
        """
        ...


    m_ExtendedProperties = ...
    singletonParent = ...


class BrokerPriority(IDroppable, IAlterable, ICreatable, IObjectPermission, BrokerObjectBase, IDropIfExists): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'IScriptable'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """
    BrokerPriority()
    BrokerPriority(serviceBroker: ServiceBroker, name: str)
    """
    @property
    def ContractName(self) -> str:
        """
        Get: ContractName(self: BrokerPriority) -> str
        Set: ContractName(self: BrokerPriority) = value
        """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: BrokerPriority) -> int """
        ...

    @property
    def LocalServiceName(self) -> str:
        """
        Get: LocalServiceName(self: BrokerPriority) -> str
        Set: LocalServiceName(self: BrokerPriority) = value
        """
        ...

    @property
    def Parent(self) -> ServiceBroker:
        """
        Get: Parent(self: BrokerPriority) -> ServiceBroker
        Set: Parent(self: BrokerPriority) = value
        """
        ...

    @property
    def PriorityLevel(self) -> Byte:
        """
        Get: PriorityLevel(self: BrokerPriority) -> Byte
        Set: PriorityLevel(self: BrokerPriority) = value
        """
        ...

    @property
    def RemoteServiceName(self) -> str:
        """
        Get: RemoteServiceName(self: BrokerPriority) -> str
        Set: RemoteServiceName(self: BrokerPriority) = value
        """
        ...


    def __new__(cls, serviceBroker:ServiceBroker = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, serviceBroker: ServiceBroker, name: str)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class BrokerPriorityCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> ServiceBroker:
        """ Get: Parent(self: BrokerPriorityCollection) -> ServiceBroker """
        ...


    def Add(self, brokerPriority:BrokerPriority): # -> 
        """ Add(self: BrokerPriorityCollection, brokerPriority: BrokerPriority) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: BrokerPriorityCollection, array: Array[BrokerPriority], index: int) """
        ...

    def ItemById(self, id:int) -> BrokerPriority:
        """ ItemById(self: BrokerPriorityCollection, id: int) -> BrokerPriority """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class BrokerPriorityExtender(SmoObjectExtender, ISfcValidate): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    BrokerPriorityExtender()
    BrokerPriorityExtender(brokerPriority: BrokerPriority)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: BrokerPriorityExtender) -> str
        Set: Name(self: BrokerPriorityExtender) = value
        """
        ...



class BrokerService(IDroppable, IAlterable, ICreatable, IObjectPermission, BrokerObjectBase, IDropIfExists, IExtendedProperties): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'IScriptable'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """
    BrokerService()
    BrokerService(serviceBroker: ServiceBroker, name: str)
    """
    @property
    def Events(self) -> BrokerServiceEvents:
        """ Get: Events(self: BrokerService) -> BrokerServiceEvents """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: BrokerService) -> int """
        ...

    @property
    def IsSystemObject(self) -> bool:
        """ Get: IsSystemObject(self: BrokerService) -> bool """
        ...

    @property
    def Owner(self) -> str:
        """
        Get: Owner(self: BrokerService) -> str
        Set: Owner(self: BrokerService) = value
        """
        ...

    @property
    def Parent(self) -> ServiceBroker:
        """
        Get: Parent(self: BrokerService) -> ServiceBroker
        Set: Parent(self: BrokerService) = value
        """
        ...

    @property
    def QueueName(self) -> str:
        """
        Get: QueueName(self: BrokerService) -> str
        Set: QueueName(self: BrokerService) = value
        """
        ...

    @property
    def QueueSchema(self) -> str:
        """
        Get: QueueSchema(self: BrokerService) -> str
        Set: QueueSchema(self: BrokerService) = value
        """
        ...

    @property
    def ServiceContractMappings(self) -> ServiceContractMappingCollection:
        """ Get: ServiceContractMappings(self: BrokerService) -> ServiceContractMappingCollection """
        ...


    def __new__(cls, serviceBroker:ServiceBroker = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, serviceBroker: ServiceBroker, name: str)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class BrokerServiceCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> ServiceBroker:
        """ Get: Parent(self: BrokerServiceCollection) -> ServiceBroker """
        ...


    def Add(self, brokerService:BrokerService): # -> 
        """ Add(self: BrokerServiceCollection, brokerService: BrokerService) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: BrokerServiceCollection, array: Array[BrokerService], index: int) """
        ...

    def ItemById(self, id:int) -> BrokerService:
        """ ItemById(self: BrokerServiceCollection, id: int) -> BrokerService """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class BrokerServiceEvents: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetEventSelection(self) -> ObjectEventSet:
        """ GetEventSelection(self: BrokerServiceEvents) -> ObjectEventSet """
        ...

    def StartEvents(self): # -> 
        """ StartEvents(self: BrokerServiceEvents) """
        ...

    def StopEvents(self): # -> 
        """ StopEvents(self: BrokerServiceEvents) """
        ...

    def SubscribeToEvents(self, events:ObjectEventSet, eventHandler:ServerEventHandler = ...): # -> 
        """ SubscribeToEvents(self: BrokerServiceEvents, events: ObjectEventSet)SubscribeToEvents(self: BrokerServiceEvents, events: ObjectEventSet, eventHandler: ServerEventHandler) """
        ...

    def UnsubscribeAllEvents(self): # -> 
        """ UnsubscribeAllEvents(self: BrokerServiceEvents) """
        ...

    def UnsubscribeFromEvents(self, events:ObjectEventSet): # -> 
        """ UnsubscribeFromEvents(self: BrokerServiceEvents, events: ObjectEventSet) """
        ...

    ServerEvent = ...


class BrokerServiceExtender(SmoObjectExtender, ISfcValidate): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    BrokerServiceExtender()
    BrokerServiceExtender(brokerService: BrokerService)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: BrokerServiceExtender) -> str
        Set: Name(self: BrokerServiceExtender) = value
        """
        ...

    @property
    def ServiceContractMappings(self) -> ServiceContractMappingCollection:
        """ Get: ServiceContractMappings(self: BrokerServiceExtender) -> ServiceContractMappingCollection """
        ...



class DialogEndPointState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DialogEndPointState, values: ClosedWait (9), ClosingWait (7), Disabled (6), ErrorWait (8), Open (1), OpenWait (2) """
    ClosedWait: DialogEndPointState = ...
    ClosingWait: DialogEndPointState = ...
    Disabled: DialogEndPointState = ...
    ErrorWait: DialogEndPointState = ...
    Open: DialogEndPointState = ...
    OpenWait: DialogEndPointState = ...
    value__ = ...


class DialogType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DialogType, values: MonologPublish (1), MonologReceive (2), Regular2Way (0) """
    MonologPublish: DialogType = ...
    MonologReceive: DialogType = ...
    Regular2Way: DialogType = ...
    value__ = ...


class MessageSource(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MessageSource, values: Initiator (0), InitiatorAndTarget (2), Target (1) """
    Initiator: MessageSource = ...
    InitiatorAndTarget: MessageSource = ...
    Target: MessageSource = ...
    value__ = ...


class MessageType(IDroppable, IAlterable, ICreatable, IObjectPermission, BrokerObjectBase, IDropIfExists, IExtendedProperties): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'IScriptable'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """
    MessageType()
    MessageType(serviceBroker: ServiceBroker, name: str)
    """
    @property
    def Events(self) -> MessageTypeEvents:
        """ Get: Events(self: MessageType) -> MessageTypeEvents """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: MessageType) -> int """
        ...

    @property
    def IsSystemObject(self) -> bool:
        """ Get: IsSystemObject(self: MessageType) -> bool """
        ...

    @property
    def MessageTypeValidation(self): # -> MessageTypeValidation
        """
        Get: MessageTypeValidation(self: MessageType) -> MessageTypeValidation
        Set: MessageTypeValidation(self: MessageType) = value
        """
        ...

    @property
    def Owner(self) -> str:
        """
        Get: Owner(self: MessageType) -> str
        Set: Owner(self: MessageType) = value
        """
        ...

    @property
    def Parent(self) -> ServiceBroker:
        """
        Get: Parent(self: MessageType) -> ServiceBroker
        Set: Parent(self: MessageType) = value
        """
        ...

    @property
    def ValidationXmlSchemaCollection(self) -> str:
        """
        Get: ValidationXmlSchemaCollection(self: MessageType) -> str
        Set: ValidationXmlSchemaCollection(self: MessageType) = value
        """
        ...

    @property
    def ValidationXmlSchemaCollectionSchema(self) -> str:
        """
        Get: ValidationXmlSchemaCollectionSchema(self: MessageType) -> str
        Set: ValidationXmlSchemaCollectionSchema(self: MessageType) = value
        """
        ...


    def __new__(cls, serviceBroker:ServiceBroker = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, serviceBroker: ServiceBroker, name: str)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class MessageTypeCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> ServiceBroker:
        """ Get: Parent(self: MessageTypeCollection) -> ServiceBroker """
        ...


    def Add(self, messageType:MessageType): # -> 
        """ Add(self: MessageTypeCollection, messageType: MessageType) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: MessageTypeCollection, array: Array[MessageType], index: int) """
        ...

    def ItemById(self, id:int) -> MessageType:
        """ ItemById(self: MessageTypeCollection, id: int) -> MessageType """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class MessageTypeEvents: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetEventSelection(self) -> ObjectEventSet:
        """ GetEventSelection(self: MessageTypeEvents) -> ObjectEventSet """
        ...

    def StartEvents(self): # -> 
        """ StartEvents(self: MessageTypeEvents) """
        ...

    def StopEvents(self): # -> 
        """ StopEvents(self: MessageTypeEvents) """
        ...

    def SubscribeToEvents(self, events:ObjectEventSet, eventHandler:ServerEventHandler = ...): # -> 
        """ SubscribeToEvents(self: MessageTypeEvents, events: ObjectEventSet)SubscribeToEvents(self: MessageTypeEvents, events: ObjectEventSet, eventHandler: ServerEventHandler) """
        ...

    def UnsubscribeAllEvents(self): # -> 
        """ UnsubscribeAllEvents(self: MessageTypeEvents) """
        ...

    def UnsubscribeFromEvents(self, events:ObjectEventSet): # -> 
        """ UnsubscribeFromEvents(self: MessageTypeEvents, events: ObjectEventSet) """
        ...

    ServerEvent = ...


class MessageTypeExtender(SmoObjectExtender, ISfcValidate): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    MessageTypeExtender()
    MessageTypeExtender(messageType: MessageType)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: MessageTypeExtender) -> str
        Set: Name(self: MessageTypeExtender) = value
        """
        ...



class MessageTypeMapping(ISfcSupportsDesignMode, IMarkForDrop, NamedSmoObject): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """
    MessageTypeMapping()
    MessageTypeMapping(serviceContract: ServiceContract, name: str)
    MessageTypeMapping(servicecontract: ServiceContract, messageName: str, messageSource: MessageSource)
    """
    @property
    def MessageSource(self) -> MessageSource:
        """
        Get: MessageSource(self: MessageTypeMapping) -> MessageSource
        Set: MessageSource(self: MessageTypeMapping) = value
        """
        ...

    @property
    def Parent(self) -> ServiceContract:
        """
        Get: Parent(self: MessageTypeMapping) -> ServiceContract
        Set: Parent(self: MessageTypeMapping) = value
        """
        ...


    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, serviceContract: ServiceContract, name: str)
        __new__(cls: type, servicecontract: ServiceContract, messageName: str, messageSource: MessageSource)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class MessageTypeMappingCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> ServiceContract:
        """ Get: Parent(self: MessageTypeMappingCollection) -> ServiceContract """
        ...


    def Add(self, messageTypeMapping:MessageTypeMapping): # -> 
        """ Add(self: MessageTypeMappingCollection, messageTypeMapping: MessageTypeMapping) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: MessageTypeMappingCollection, array: Array[MessageTypeMapping], index: int) """
        ...

    def Remove(self, *__args:str): # -> 
        """ Remove(self: MessageTypeMappingCollection, name: str)Remove(self: MessageTypeMappingCollection, messageTypeMapping: MessageTypeMapping) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class MessageTypeValidation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MessageTypeValidation, values: Empty (2), None (0), Xml (3), XmlSchemaCollection (1) """
    Empty: MessageTypeValidation = ...
    value__ = ...
    Xml: MessageTypeValidation = ...
    XmlSchemaCollection: MessageTypeValidation = ...


class RemoteServiceBinding(IDroppable, IAlterable, ICreatable, IObjectPermission, BrokerObjectBase, IDropIfExists, IExtendedProperties): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'IScriptable'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """
    RemoteServiceBinding()
    RemoteServiceBinding(serviceBroker: ServiceBroker, name: str)
    """
    @property
    def CertificateUser(self) -> str:
        """
        Get: CertificateUser(self: RemoteServiceBinding) -> str
        Set: CertificateUser(self: RemoteServiceBinding) = value
        """
        ...

    @property
    def Events(self) -> RemoteServiceBindingEvents:
        """ Get: Events(self: RemoteServiceBinding) -> RemoteServiceBindingEvents """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: RemoteServiceBinding) -> int """
        ...

    @property
    def IsAnonymous(self) -> bool:
        """
        Get: IsAnonymous(self: RemoteServiceBinding) -> bool
        Set: IsAnonymous(self: RemoteServiceBinding) = value
        """
        ...

    @property
    def Owner(self) -> str:
        """
        Get: Owner(self: RemoteServiceBinding) -> str
        Set: Owner(self: RemoteServiceBinding) = value
        """
        ...

    @property
    def Parent(self) -> ServiceBroker:
        """
        Get: Parent(self: RemoteServiceBinding) -> ServiceBroker
        Set: Parent(self: RemoteServiceBinding) = value
        """
        ...

    @property
    def RemoteService(self) -> str:
        """
        Get: RemoteService(self: RemoteServiceBinding) -> str
        Set: RemoteService(self: RemoteServiceBinding) = value
        """
        ...


    def __new__(cls, serviceBroker:ServiceBroker = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, serviceBroker: ServiceBroker, name: str)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class RemoteServiceBindingCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> ServiceBroker:
        """ Get: Parent(self: RemoteServiceBindingCollection) -> ServiceBroker """
        ...


    def Add(self, remoteServiceBinding:RemoteServiceBinding): # -> 
        """ Add(self: RemoteServiceBindingCollection, remoteServiceBinding: RemoteServiceBinding) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: RemoteServiceBindingCollection, array: Array[RemoteServiceBinding], index: int) """
        ...

    def ItemById(self, id:int) -> RemoteServiceBinding:
        """ ItemById(self: RemoteServiceBindingCollection, id: int) -> RemoteServiceBinding """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class RemoteServiceBindingEvents: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetEventSelection(self) -> ObjectEventSet:
        """ GetEventSelection(self: RemoteServiceBindingEvents) -> ObjectEventSet """
        ...

    def StartEvents(self): # -> 
        """ StartEvents(self: RemoteServiceBindingEvents) """
        ...

    def StopEvents(self): # -> 
        """ StopEvents(self: RemoteServiceBindingEvents) """
        ...

    def SubscribeToEvents(self, events:ObjectEventSet, eventHandler:ServerEventHandler = ...): # -> 
        """ SubscribeToEvents(self: RemoteServiceBindingEvents, events: ObjectEventSet)SubscribeToEvents(self: RemoteServiceBindingEvents, events: ObjectEventSet, eventHandler: ServerEventHandler) """
        ...

    def UnsubscribeAllEvents(self): # -> 
        """ UnsubscribeAllEvents(self: RemoteServiceBindingEvents) """
        ...

    def UnsubscribeFromEvents(self, events:ObjectEventSet): # -> 
        """ UnsubscribeFromEvents(self: RemoteServiceBindingEvents, events: ObjectEventSet) """
        ...

    ServerEvent = ...


class RemoteServiceBindingExtender(SmoObjectExtender, ISfcValidate): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    RemoteServiceBindingExtender()
    RemoteServiceBindingExtender(remoteServiceBinding: RemoteServiceBinding)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: RemoteServiceBindingExtender) -> str
        Set: Name(self: RemoteServiceBindingExtender) = value
        """
        ...



class ServiceBroker(SqlSmoObject): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """ no doc """
    @property
    def MessageTypes(self) -> MessageTypeCollection:
        """ Get: MessageTypes(self: ServiceBroker) -> MessageTypeCollection """
        ...

    @property
    def Parent(self) -> Database:
        """ Get: Parent(self: ServiceBroker) -> Database """
        ...

    @property
    def Priorities(self) -> BrokerPriorityCollection:
        """ Get: Priorities(self: ServiceBroker) -> BrokerPriorityCollection """
        ...

    @property
    def Queues(self) -> ServiceQueueCollection:
        """ Get: Queues(self: ServiceBroker) -> ServiceQueueCollection """
        ...

    @property
    def RemoteServiceBindings(self) -> RemoteServiceBindingCollection:
        """ Get: RemoteServiceBindings(self: ServiceBroker) -> RemoteServiceBindingCollection """
        ...

    @property
    def Routes(self) -> ServiceRouteCollection:
        """ Get: Routes(self: ServiceBroker) -> ServiceRouteCollection """
        ...

    @property
    def ServiceContracts(self) -> ServiceContractCollection:
        """ Get: ServiceContracts(self: ServiceBroker) -> ServiceContractCollection """
        ...

    @property
    def Services(self) -> BrokerServiceCollection:
        """ Get: Services(self: ServiceBroker) -> BrokerServiceCollection """
        ...


    m_ExtendedProperties = ...
    singletonParent = ...


class ServiceContract(IDroppable, IAlterable, ICreatable, IObjectPermission, BrokerObjectBase, IDropIfExists, IExtendedProperties): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'IScriptable'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """
    ServiceContract()
    ServiceContract(serviceBroker: ServiceBroker, name: str)
    """
    @property
    def Events(self) -> ServiceContractEvents:
        """ Get: Events(self: ServiceContract) -> ServiceContractEvents """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: ServiceContract) -> int """
        ...

    @property
    def IsSystemObject(self) -> bool:
        """ Get: IsSystemObject(self: ServiceContract) -> bool """
        ...

    @property
    def MessageTypeMappings(self) -> MessageTypeMappingCollection:
        """ Get: MessageTypeMappings(self: ServiceContract) -> MessageTypeMappingCollection """
        ...

    @property
    def Owner(self) -> str:
        """
        Get: Owner(self: ServiceContract) -> str
        Set: Owner(self: ServiceContract) = value
        """
        ...

    @property
    def Parent(self) -> ServiceBroker:
        """
        Get: Parent(self: ServiceContract) -> ServiceBroker
        Set: Parent(self: ServiceContract) = value
        """
        ...


    def __new__(cls, serviceBroker:ServiceBroker = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, serviceBroker: ServiceBroker, name: str)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class ServiceContractCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> ServiceBroker:
        """ Get: Parent(self: ServiceContractCollection) -> ServiceBroker """
        ...


    def Add(self, serviceContract:ServiceContract): # -> 
        """ Add(self: ServiceContractCollection, serviceContract: ServiceContract) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ServiceContractCollection, array: Array[ServiceContract], index: int) """
        ...

    def ItemById(self, id:int) -> ServiceContract:
        """ ItemById(self: ServiceContractCollection, id: int) -> ServiceContract """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class ServiceContractEvents: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetEventSelection(self) -> ObjectEventSet:
        """ GetEventSelection(self: ServiceContractEvents) -> ObjectEventSet """
        ...

    def StartEvents(self): # -> 
        """ StartEvents(self: ServiceContractEvents) """
        ...

    def StopEvents(self): # -> 
        """ StopEvents(self: ServiceContractEvents) """
        ...

    def SubscribeToEvents(self, events:ObjectEventSet, eventHandler:ServerEventHandler = ...): # -> 
        """ SubscribeToEvents(self: ServiceContractEvents, events: ObjectEventSet)SubscribeToEvents(self: ServiceContractEvents, events: ObjectEventSet, eventHandler: ServerEventHandler) """
        ...

    def UnsubscribeAllEvents(self): # -> 
        """ UnsubscribeAllEvents(self: ServiceContractEvents) """
        ...

    def UnsubscribeFromEvents(self, events:ObjectEventSet): # -> 
        """ UnsubscribeFromEvents(self: ServiceContractEvents, events: ObjectEventSet) """
        ...

    ServerEvent = ...


class ServiceContractExtender(SmoObjectExtender, ISfcValidate): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    ServiceContractExtender()
    ServiceContractExtender(serviceContract: ServiceContract)
    """
    @property
    def MessageTypeMappings(self) -> MessageTypeMappingCollection:
        """ Get: MessageTypeMappings(self: ServiceContractExtender) -> MessageTypeMappingCollection """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ServiceContractExtender) -> str
        Set: Name(self: ServiceContractExtender) = value
        """
        ...



class ServiceContractMapping(ISfcSupportsDesignMode, IMarkForDrop, NamedSmoObject): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """
    ServiceContractMapping()
    ServiceContractMapping(brokerService: BrokerService, name: str)
    """
    @property
    def Parent(self) -> BrokerService:
        """
        Get: Parent(self: ServiceContractMapping) -> BrokerService
        Set: Parent(self: ServiceContractMapping) = value
        """
        ...


    def __new__(cls, brokerService:BrokerService = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, brokerService: BrokerService, name: str)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class ServiceContractMappingCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> BrokerService:
        """ Get: Parent(self: ServiceContractMappingCollection) -> BrokerService """
        ...


    def Add(self, serviceContractMapping:ServiceContractMapping): # -> 
        """ Add(self: ServiceContractMappingCollection, serviceContractMapping: ServiceContractMapping) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ServiceContractMappingCollection, array: Array[ServiceContractMapping], index: int) """
        ...

    def Remove(self, *__args:str): # -> 
        """ Remove(self: ServiceContractMappingCollection, name: str)Remove(self: ServiceContractMappingCollection, serviceContractMapping: ServiceContractMapping) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class ServiceQueue(IDroppable, IAlterable, ICreatable, IScriptable, IObjectPermission, ISfcSupportsDesignMode, IDropIfExists, ScriptSchemaObjectBase, IExtendedProperties): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """
    ServiceQueue()
    ServiceQueue(serviceBroker: ServiceBroker, name: str)
    ServiceQueue(serviceBroker: ServiceBroker, name: str, schema: str)
    """
    @property
    def ActivationExecutionContext(self) -> ActivationExecutionContext:
        """
        Get: ActivationExecutionContext(self: ServiceQueue) -> ActivationExecutionContext
        Set: ActivationExecutionContext(self: ServiceQueue) = value
        """
        ...

    @property
    def CreateDate(self) -> DateTime:
        """ Get: CreateDate(self: ServiceQueue) -> DateTime """
        ...

    @property
    def DateLastModified(self) -> DateTime:
        """ Get: DateLastModified(self: ServiceQueue) -> DateTime """
        ...

    @property
    def Events(self) -> ServiceQueueEvents:
        """ Get: Events(self: ServiceQueue) -> ServiceQueueEvents """
        ...

    @property
    def ExecutionContextPrincipal(self) -> str:
        """
        Get: ExecutionContextPrincipal(self: ServiceQueue) -> str
        Set: ExecutionContextPrincipal(self: ServiceQueue) = value
        """
        ...

    @property
    def FileGroup(self) -> str:
        """
        Get: FileGroup(self: ServiceQueue) -> str
        Set: FileGroup(self: ServiceQueue) = value
        """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: ServiceQueue) -> int """
        ...

    @property
    def IsActivationEnabled(self) -> bool:
        """
        Get: IsActivationEnabled(self: ServiceQueue) -> bool
        Set: IsActivationEnabled(self: ServiceQueue) = value
        """
        ...

    @property
    def IsEnqueueEnabled(self) -> bool:
        """
        Get: IsEnqueueEnabled(self: ServiceQueue) -> bool
        Set: IsEnqueueEnabled(self: ServiceQueue) = value
        """
        ...

    @property
    def IsPoisonMessageHandlingEnabled(self) -> bool:
        """
        Get: IsPoisonMessageHandlingEnabled(self: ServiceQueue) -> bool
        Set: IsPoisonMessageHandlingEnabled(self: ServiceQueue) = value
        """
        ...

    @property
    def IsRetentionEnabled(self) -> bool:
        """
        Get: IsRetentionEnabled(self: ServiceQueue) -> bool
        Set: IsRetentionEnabled(self: ServiceQueue) = value
        """
        ...

    @property
    def IsSystemObject(self) -> bool:
        """ Get: IsSystemObject(self: ServiceQueue) -> bool """
        ...

    @property
    def MaxReaders(self) -> Int16:
        """
        Get: MaxReaders(self: ServiceQueue) -> Int16
        Set: MaxReaders(self: ServiceQueue) = value
        """
        ...

    @property
    def Parent(self) -> ServiceBroker:
        """
        Get: Parent(self: ServiceQueue) -> ServiceBroker
        Set: Parent(self: ServiceQueue) = value
        """
        ...

    @property
    def ProcedureDatabase(self) -> str:
        """
        Get: ProcedureDatabase(self: ServiceQueue) -> str
        Set: ProcedureDatabase(self: ServiceQueue) = value
        """
        ...

    @property
    def ProcedureName(self) -> str:
        """
        Get: ProcedureName(self: ServiceQueue) -> str
        Set: ProcedureName(self: ServiceQueue) = value
        """
        ...

    @property
    def ProcedureSchema(self) -> str:
        """
        Get: ProcedureSchema(self: ServiceQueue) -> str
        Set: ProcedureSchema(self: ServiceQueue) = value
        """
        ...

    @property
    def RowCount(self) -> Int64:
        """ Get: RowCount(self: ServiceQueue) -> Int64 """
        ...

    @property
    def RowCountAsDouble(self) -> float:
        """ Get: RowCountAsDouble(self: ServiceQueue) -> float """
        ...


    def MoveTo(self, fileGroup:str, maxDop:int = ...): # -> 
        """ MoveTo(self: ServiceQueue, fileGroup: str)MoveTo(self: ServiceQueue, fileGroup: str, maxDop: int) """
        ...

    def Rebuild(self, maxDop:int = ...): # -> 
        """ Rebuild(self: ServiceQueue)Rebuild(self: ServiceQueue, maxDop: int) """
        ...

    def Reorganize(self, lobCompaction:bool = ...): # -> 
        """ Reorganize(self: ServiceQueue)Reorganize(self: ServiceQueue, lobCompaction: bool) """
        ...

    def __new__(cls, serviceBroker:ServiceBroker = ..., name:str = ..., schema:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, serviceBroker: ServiceBroker, name: str)
        __new__(cls: type, serviceBroker: ServiceBroker, name: str, schema: str)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class ServiceQueueCollection(SchemaCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> ServiceBroker:
        """ Get: Parent(self: ServiceQueueCollection) -> ServiceBroker """
        ...


    def Add(self, serviceQueue:ServiceQueue): # -> 
        """ Add(self: ServiceQueueCollection, serviceQueue: ServiceQueue) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ServiceQueueCollection, array: Array[ServiceQueue], index: int) """
        ...

    def ItemById(self, id:int) -> ServiceQueue:
        """ ItemById(self: ServiceQueueCollection, id: int) -> ServiceQueue """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class ServiceQueueEvents: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetEventSelection(self) -> ServiceQueueEventSet:
        """ GetEventSelection(self: ServiceQueueEvents) -> ServiceQueueEventSet """
        ...

    def StartEvents(self): # -> 
        """ StartEvents(self: ServiceQueueEvents) """
        ...

    def StopEvents(self): # -> 
        """ StopEvents(self: ServiceQueueEvents) """
        ...

    def SubscribeToEvents(self, events:ServiceQueueEventSet, eventHandler:ServerEventHandler = ...): # -> 
        """ SubscribeToEvents(self: ServiceQueueEvents, events: ServiceQueueEventSet)SubscribeToEvents(self: ServiceQueueEvents, events: ServiceQueueEventSet, eventHandler: ServerEventHandler) """
        ...

    def UnsubscribeAllEvents(self): # -> 
        """ UnsubscribeAllEvents(self: ServiceQueueEvents) """
        ...

    def UnsubscribeFromEvents(self, events:ServiceQueueEventSet): # -> 
        """ UnsubscribeFromEvents(self: ServiceQueueEvents, events: ServiceQueueEventSet) """
        ...

    ServerEvent = ...


class ServiceQueueExtender(SmoObjectExtender, ISfcValidate): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    ServiceQueueExtender()
    ServiceQueueExtender(serviceQueue: ServiceQueue)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: ServiceQueueExtender) -> str
        Set: Name(self: ServiceQueueExtender) = value
        """
        ...

    @property
    def ServerVersion(self) -> Version:
        """ Get: ServerVersion(self: ServiceQueueExtender) -> Version """
        ...



class ServiceRoute(IDroppable, IAlterable, ICreatable, IObjectPermission, BrokerObjectBase, IDropIfExists, IExtendedProperties): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'IScriptable'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """
    ServiceRoute()
    ServiceRoute(serviceBroker: ServiceBroker, name: str)
    """
    @property
    def Address(self) -> str:
        """
        Get: Address(self: ServiceRoute) -> str
        Set: Address(self: ServiceRoute) = value
        """
        ...

    @property
    def BrokerInstance(self) -> str:
        """
        Get: BrokerInstance(self: ServiceRoute) -> str
        Set: BrokerInstance(self: ServiceRoute) = value
        """
        ...

    @property
    def Events(self) -> ServiceRouteEvents:
        """ Get: Events(self: ServiceRoute) -> ServiceRouteEvents """
        ...

    @property
    def ExpirationDate(self) -> DateTime:
        """
        Get: ExpirationDate(self: ServiceRoute) -> DateTime
        Set: ExpirationDate(self: ServiceRoute) = value
        """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: ServiceRoute) -> int """
        ...

    @property
    def MirrorAddress(self) -> str:
        """
        Get: MirrorAddress(self: ServiceRoute) -> str
        Set: MirrorAddress(self: ServiceRoute) = value
        """
        ...

    @property
    def Owner(self) -> str:
        """
        Get: Owner(self: ServiceRoute) -> str
        Set: Owner(self: ServiceRoute) = value
        """
        ...

    @property
    def Parent(self) -> ServiceBroker:
        """
        Get: Parent(self: ServiceRoute) -> ServiceBroker
        Set: Parent(self: ServiceRoute) = value
        """
        ...

    @property
    def RemoteService(self) -> str:
        """
        Get: RemoteService(self: ServiceRoute) -> str
        Set: RemoteService(self: ServiceRoute) = value
        """
        ...


    def __new__(cls, serviceBroker:ServiceBroker = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, serviceBroker: ServiceBroker, name: str)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class ServiceRouteCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> ServiceBroker:
        """ Get: Parent(self: ServiceRouteCollection) -> ServiceBroker """
        ...


    def Add(self, serviceRoute:ServiceRoute): # -> 
        """ Add(self: ServiceRouteCollection, serviceRoute: ServiceRoute) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ServiceRouteCollection, array: Array[ServiceRoute], index: int) """
        ...

    def ItemById(self, id:int) -> ServiceRoute:
        """ ItemById(self: ServiceRouteCollection, id: int) -> ServiceRoute """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class ServiceRouteEvents: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetEventSelection(self) -> ObjectEventSet:
        """ GetEventSelection(self: ServiceRouteEvents) -> ObjectEventSet """
        ...

    def StartEvents(self): # -> 
        """ StartEvents(self: ServiceRouteEvents) """
        ...

    def StopEvents(self): # -> 
        """ StopEvents(self: ServiceRouteEvents) """
        ...

    def SubscribeToEvents(self, events:ObjectEventSet, eventHandler:ServerEventHandler = ...): # -> 
        """ SubscribeToEvents(self: ServiceRouteEvents, events: ObjectEventSet)SubscribeToEvents(self: ServiceRouteEvents, events: ObjectEventSet, eventHandler: ServerEventHandler) """
        ...

    def UnsubscribeAllEvents(self): # -> 
        """ UnsubscribeAllEvents(self: ServiceRouteEvents) """
        ...

    def UnsubscribeFromEvents(self, events:ObjectEventSet): # -> 
        """ UnsubscribeFromEvents(self: ServiceRouteEvents, events: ObjectEventSet) """
        ...

    ServerEvent = ...


class ServiceRouteExtender(SmoObjectExtender, ISfcValidate): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    ServiceRouteExtender()
    ServiceRouteExtender(route: ServiceRoute)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: ServiceRouteExtender) -> str
        Set: Name(self: ServiceRouteExtender) = value
        """
        ...



