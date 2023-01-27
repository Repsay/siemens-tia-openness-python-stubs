# encoding: utf-8
# module System.ServiceModel.MsmqIntegration calls itself MsmqIntegration
# from System.ServiceModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, Nullable, Uri

from System.Messaging import Message

from System.ServiceModel import MsmqBindingBase, MsmqTransportSecurity

from System.ServiceModel.Channels import (BindingContext, BindingElement, 
    BindingElementCollection, IChannelFactory, IChannelListener, 
    MsmqBindingElementBase)

from typing import Self

"""The following names are not found in the module: T, field#
"""

# no functions
# classes

class MsmqIntegrationBinding(MsmqBindingBase): # skipped bases: <type 'IBindingRuntimePreferences'>, <type 'IDefaultCommunicationTimeouts'>, <type 'object'>
    """
    MsmqIntegrationBinding()
    MsmqIntegrationBinding(configurationName: str)
    MsmqIntegrationBinding(securityMode: MsmqIntegrationSecurityMode)
    """
    @property
    def Security(self) -> MsmqIntegrationSecurity:
        """
        Get: Security(self: MsmqIntegrationBinding) -> MsmqIntegrationSecurity
        Set: Security(self: MsmqIntegrationBinding) = value
        """
        ...

    @property
    def SerializationFormat(self) -> MsmqMessageSerializationFormat:
        """
        Get: SerializationFormat(self: MsmqIntegrationBinding) -> MsmqMessageSerializationFormat
        Set: SerializationFormat(self: MsmqIntegrationBinding) = value
        """
        ...


    def CreateBindingElements(self) -> BindingElementCollection:
        """ CreateBindingElements(self: MsmqIntegrationBinding) -> BindingElementCollection """
        ...

    def ShouldSerializeSecurity(self) -> bool:
        """ ShouldSerializeSecurity(self: MsmqIntegrationBinding) -> bool """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, configurationName: str)
        __new__(cls: type, securityMode: MsmqIntegrationSecurityMode)
        """
        ...


class MsmqIntegrationBindingElement(MsmqBindingElementBase): # skipped bases: <type 'IPolicyExportExtension'>, <type 'ITransactedBindingElement'>, <type 'ITransportPolicyImport'>, <type 'IWsdlExportExtension'>, <type 'object'>
    """ MsmqIntegrationBindingElement() """
    @property
    def Scheme(self) -> str:
        """ Get: Scheme(self: MsmqIntegrationBindingElement) -> str """
        ...

    @property
    def SerializationFormat(self) -> MsmqMessageSerializationFormat:
        """
        Get: SerializationFormat(self: MsmqIntegrationBindingElement) -> MsmqMessageSerializationFormat
        Set: SerializationFormat(self: MsmqIntegrationBindingElement) = value
        """
        ...

    @property
    def TargetSerializationTypes(self) -> Array:
        """
        Get: TargetSerializationTypes(self: MsmqIntegrationBindingElement) -> Array[Type]
        Set: TargetSerializationTypes(self: MsmqIntegrationBindingElement) = value
        """
        ...


    def BuildChannelFactory(self, context:BindingContext) -> IChannelFactory:
        """ BuildChannelFactory[TChannel](self: MsmqIntegrationBindingElement, context: BindingContext) -> IChannelFactory[TChannel] """
        ...

    def BuildChannelListener(self, context:BindingContext) -> IChannelListener:
        """ BuildChannelListener[TChannel](self: MsmqIntegrationBindingElement, context: BindingContext) -> IChannelListener[TChannel] """
        ...

    def CanBuildChannelFactory(self, context:BindingContext) -> bool:
        """ CanBuildChannelFactory[TChannel](self: MsmqIntegrationBindingElement, context: BindingContext) -> bool """
        ...

    def CanBuildChannelListener(self, context:BindingContext) -> bool:
        """ CanBuildChannelListener[TChannel](self: MsmqIntegrationBindingElement, context: BindingContext) -> bool """
        ...

    def Clone(self) -> BindingElement:
        """ Clone(self: MsmqIntegrationBindingElement) -> BindingElement """
        ...


class MsmqIntegrationMessageProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ MsmqIntegrationMessageProperty() """
    @property
    def AcknowledgeType(self) -> Nullable:
        """
        Get: AcknowledgeType(self: MsmqIntegrationMessageProperty) -> Nullable[AcknowledgeTypes]
        Set: AcknowledgeType(self: MsmqIntegrationMessageProperty) = value
        """
        ...

    @property
    def Acknowledgment(self) -> Nullable:
        """ Get: Acknowledgment(self: MsmqIntegrationMessageProperty) -> Nullable[Acknowledgment] """
        ...

    @property
    def AdministrationQueue(self) -> Uri:
        """
        Get: AdministrationQueue(self: MsmqIntegrationMessageProperty) -> Uri
        Set: AdministrationQueue(self: MsmqIntegrationMessageProperty) = value
        """
        ...

    @property
    def AppSpecific(self) -> Nullable:
        """
        Get: AppSpecific(self: MsmqIntegrationMessageProperty) -> Nullable[int]
        Set: AppSpecific(self: MsmqIntegrationMessageProperty) = value
        """
        ...

    @property
    def ArrivedTime(self) -> Nullable:
        """ Get: ArrivedTime(self: MsmqIntegrationMessageProperty) -> Nullable[DateTime] """
        ...

    @property
    def Authenticated(self) -> Nullable:
        """ Get: Authenticated(self: MsmqIntegrationMessageProperty) -> Nullable[bool] """
        ...

    @property
    def Body(self) -> object:
        """
        Get: Body(self: MsmqIntegrationMessageProperty) -> object
        Set: Body(self: MsmqIntegrationMessageProperty) = value
        """
        ...

    @property
    def BodyType(self) -> Nullable:
        """
        Get: BodyType(self: MsmqIntegrationMessageProperty) -> Nullable[int]
        Set: BodyType(self: MsmqIntegrationMessageProperty) = value
        """
        ...

    @property
    def CorrelationId(self) -> str:
        """
        Get: CorrelationId(self: MsmqIntegrationMessageProperty) -> str
        Set: CorrelationId(self: MsmqIntegrationMessageProperty) = value
        """
        ...

    @property
    def DestinationQueue(self) -> Uri:
        """ Get: DestinationQueue(self: MsmqIntegrationMessageProperty) -> Uri """
        ...

    @property
    def Extension(self) -> Array:
        """
        Get: Extension(self: MsmqIntegrationMessageProperty) -> Array[Byte]
        Set: Extension(self: MsmqIntegrationMessageProperty) = value
        """
        ...

    @property
    def Id(self) -> str:
        """ Get: Id(self: MsmqIntegrationMessageProperty) -> str """
        ...

    @property
    def Label(self) -> str:
        """
        Get: Label(self: MsmqIntegrationMessageProperty) -> str
        Set: Label(self: MsmqIntegrationMessageProperty) = value
        """
        ...

    @property
    def MessageType(self) -> Nullable:
        """ Get: MessageType(self: MsmqIntegrationMessageProperty) -> Nullable[MessageType] """
        ...

    @property
    def Priority(self) -> Nullable:
        """
        Get: Priority(self: MsmqIntegrationMessageProperty) -> Nullable[MessagePriority]
        Set: Priority(self: MsmqIntegrationMessageProperty) = value
        """
        ...

    @property
    def ResponseQueue(self) -> Uri:
        """
        Get: ResponseQueue(self: MsmqIntegrationMessageProperty) -> Uri
        Set: ResponseQueue(self: MsmqIntegrationMessageProperty) = value
        """
        ...

    @property
    def SenderId(self) -> Array:
        """ Get: SenderId(self: MsmqIntegrationMessageProperty) -> Array[Byte] """
        ...

    @property
    def SentTime(self) -> Nullable:
        """ Get: SentTime(self: MsmqIntegrationMessageProperty) -> Nullable[DateTime] """
        ...

    @property
    def TimeToReachQueue(self) -> Nullable:
        """
        Get: TimeToReachQueue(self: MsmqIntegrationMessageProperty) -> Nullable[TimeSpan]
        Set: TimeToReachQueue(self: MsmqIntegrationMessageProperty) = value
        """
        ...


    @staticmethod
    def Get(message:Message) -> MsmqIntegrationMessageProperty:
        """ Get(message: Message) -> MsmqIntegrationMessageProperty """
        ...

    Name: str = ...


class MsmqIntegrationSecurity: # skipped bases: <type 'object'>, <type 'object'>
    """ MsmqIntegrationSecurity() """
    @property
    def Mode(self) -> MsmqIntegrationSecurityMode:
        """
        Get: Mode(self: MsmqIntegrationSecurity) -> MsmqIntegrationSecurityMode
        Set: Mode(self: MsmqIntegrationSecurity) = value
        """
        ...

    @property
    def Transport(self) -> MsmqTransportSecurity:
        """
        Get: Transport(self: MsmqIntegrationSecurity) -> MsmqTransportSecurity
        Set: Transport(self: MsmqIntegrationSecurity) = value
        """
        ...



class MsmqIntegrationSecurityMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsmqIntegrationSecurityMode, values: None (0), Transport (1) """
    Transport: MsmqIntegrationSecurityMode = ...
    value__ = ...


class MsmqMessage: # skipped bases: <type 'object'>, <type 'object'>
    """ MsmqMessage[T](body: T) """
    @property
    def AcknowledgeType(self) -> Nullable:
        """
        Get: AcknowledgeType(self: MsmqMessage[T]) -> Nullable[AcknowledgeTypes]
        Set: AcknowledgeType(self: MsmqMessage[T]) = value
        """
        ...

    @property
    def Acknowledgment(self) -> Nullable:
        """ Get: Acknowledgment(self: MsmqMessage[T]) -> Nullable[Acknowledgment] """
        ...

    @property
    def AdministrationQueue(self) -> Uri:
        """
        Get: AdministrationQueue(self: MsmqMessage[T]) -> Uri
        Set: AdministrationQueue(self: MsmqMessage[T]) = value
        """
        ...

    @property
    def AppSpecific(self) -> Nullable:
        """
        Get: AppSpecific(self: MsmqMessage[T]) -> Nullable[int]
        Set: AppSpecific(self: MsmqMessage[T]) = value
        """
        ...

    @property
    def ArrivedTime(self) -> Nullable:
        """ Get: ArrivedTime(self: MsmqMessage[T]) -> Nullable[DateTime] """
        ...

    @property
    def Authenticated(self) -> Nullable:
        """ Get: Authenticated(self: MsmqMessage[T]) -> Nullable[bool] """
        ...

    @property
    def Body(self): # -> T
        """
        Get: Body(self: MsmqMessage[T]) -> T
        Set: Body(self: MsmqMessage[T]) = value
        """
        ...

    @property
    def BodyType(self) -> Nullable:
        """
        Get: BodyType(self: MsmqMessage[T]) -> Nullable[int]
        Set: BodyType(self: MsmqMessage[T]) = value
        """
        ...

    @property
    def CorrelationId(self) -> str:
        """
        Get: CorrelationId(self: MsmqMessage[T]) -> str
        Set: CorrelationId(self: MsmqMessage[T]) = value
        """
        ...

    @property
    def DestinationQueue(self) -> Uri:
        """ Get: DestinationQueue(self: MsmqMessage[T]) -> Uri """
        ...

    @property
    def Extension(self) -> Array:
        """
        Get: Extension(self: MsmqMessage[T]) -> Array[Byte]
        Set: Extension(self: MsmqMessage[T]) = value
        """
        ...

    @property
    def Id(self) -> str:
        """ Get: Id(self: MsmqMessage[T]) -> str """
        ...

    @property
    def Label(self) -> str:
        """
        Get: Label(self: MsmqMessage[T]) -> str
        Set: Label(self: MsmqMessage[T]) = value
        """
        ...

    @property
    def MessageType(self) -> Nullable:
        """ Get: MessageType(self: MsmqMessage[T]) -> Nullable[MessageType] """
        ...

    @property
    def Priority(self) -> Nullable:
        """
        Get: Priority(self: MsmqMessage[T]) -> Nullable[MessagePriority]
        Set: Priority(self: MsmqMessage[T]) = value
        """
        ...

    @property
    def ResponseQueue(self) -> Uri:
        """
        Get: ResponseQueue(self: MsmqMessage[T]) -> Uri
        Set: ResponseQueue(self: MsmqMessage[T]) = value
        """
        ...

    @property
    def SenderId(self) -> Array:
        """ Get: SenderId(self: MsmqMessage[T]) -> Array[Byte] """
        ...

    @property
    def SentTime(self) -> Nullable:
        """ Get: SentTime(self: MsmqMessage[T]) -> Nullable[DateTime] """
        ...

    @property
    def TimeToReachQueue(self) -> Nullable:
        """
        Get: TimeToReachQueue(self: MsmqMessage[T]) -> Nullable[TimeSpan]
        Set: TimeToReachQueue(self: MsmqMessage[T]) = value
        """
        ...



class MsmqMessageSerializationFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsmqMessageSerializationFormat, values: ActiveX (2), Binary (1), ByteArray (3), Stream (4), Xml (0) """
    ActiveX: MsmqMessageSerializationFormat = ...
    Binary: MsmqMessageSerializationFormat = ...
    ByteArray: MsmqMessageSerializationFormat = ...
    Stream: MsmqMessageSerializationFormat = ...
    value__ = ...
    Xml: MsmqMessageSerializationFormat = ...


