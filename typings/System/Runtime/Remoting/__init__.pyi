# encoding: utf-8
# module System.Runtime.Remoting calls itself Remoting
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Runtime.Remoting, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, MarshalByRefObject, SystemException, Type

from System.Reflection import Assembly, MethodBase

from System.Runtime.Remoting.Messaging import (IMessageSink, 
    IMethodCallMessage, IMethodMessage, IMethodReturnMessage, MethodCall)

from System.Runtime.Remoting.Metadata import SoapAttribute

from System.Runtime.Remoting.Proxies import RealProxy

from System.Runtime.Serialization import (IObjectReference, ISerializable, 
    SerializationInfo, StreamingContext)

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class TypeEntry: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AssemblyName(self) -> str:
        """
        Get: AssemblyName(self: TypeEntry) -> str
        Set: AssemblyName(self: TypeEntry) = value
        """
        ...

    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: TypeEntry) -> str
        Set: TypeName(self: TypeEntry) = value
        """
        ...



class ActivatedClientTypeEntry(TypeEntry): # skipped bases: <type 'object'>
    """
    ActivatedClientTypeEntry(typeName: str, assemblyName: str, appUrl: str)
    ActivatedClientTypeEntry(type: Type, appUrl: str)
    """
    @property
    def ApplicationUrl(self) -> str:
        """ Get: ApplicationUrl(self: ActivatedClientTypeEntry) -> str """
        ...

    @property
    def ContextAttributes(self) -> Array:
        """
        Get: ContextAttributes(self: ActivatedClientTypeEntry) -> Array[IContextAttribute]
        Set: ContextAttributes(self: ActivatedClientTypeEntry) = value
        """
        ...

    @property
    def ObjectType(self) -> Type:
        """ Get: ObjectType(self: ActivatedClientTypeEntry) -> Type """
        ...


    def ToString(self) -> str:
        """ ToString(self: ActivatedClientTypeEntry) -> str """
        ...

    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, typeName: str, assemblyName: str, appUrl: str)
        __new__(cls: type, type: Type, appUrl: str)
        """
        ...


class ActivatedServiceTypeEntry(TypeEntry): # skipped bases: <type 'object'>
    """
    ActivatedServiceTypeEntry(typeName: str, assemblyName: str)
    ActivatedServiceTypeEntry(type: Type)
    """
    @property
    def ContextAttributes(self) -> Array:
        """
        Get: ContextAttributes(self: ActivatedServiceTypeEntry) -> Array[IContextAttribute]
        Set: ContextAttributes(self: ActivatedServiceTypeEntry) = value
        """
        ...

    @property
    def ObjectType(self) -> Type:
        """ Get: ObjectType(self: ActivatedServiceTypeEntry) -> Type """
        ...


    def ToString(self) -> str:
        """ ToString(self: ActivatedServiceTypeEntry) -> str """
        ...

    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type, typeName: str, assemblyName: str)
        __new__(cls: type, type: Type)
        """
        ...


class CustomErrorsModes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CustomErrorsModes, values: Off (1), On (0), RemoteOnly (2) """
    Off: CustomErrorsModes = ...
    On: CustomErrorsModes = ...
    RemoteOnly: CustomErrorsModes = ...
    value__ = ...


class IChannelInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ChannelData(self) -> Array:
        """
        Get: ChannelData(self: IChannelInfo) -> Array[object]
        Set: ChannelData(self: IChannelInfo) = value
        """
        ...



class IEnvoyInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def EnvoySinks(self) -> IMessageSink:
        """
        Get: EnvoySinks(self: IEnvoyInfo) -> IMessageSink
        Set: EnvoySinks(self: IEnvoyInfo) = value
        """
        ...



class InternalRemotingServices: # skipped bases: <type 'object'>, <type 'object'>
    """ InternalRemotingServices() """
    @staticmethod
    def DebugOutChnl(s:str): # -> 
        """ DebugOutChnl(s: str) """
        ...

    @staticmethod
    def GetCachedSoapAttribute(reflectionObject:object) -> SoapAttribute:
        """ GetCachedSoapAttribute(reflectionObject: object) -> SoapAttribute """
        ...

    @staticmethod
    def RemotingAssert(condition:bool, message:str): # -> 
        """ RemotingAssert(condition: bool, message: str) """
        ...

    @staticmethod
    def RemotingTrace(messages:Array): # -> 
        """ RemotingTrace(*messages: Array[object]) """
        ...

    @staticmethod
    def SetServerIdentity(m:MethodCall, srvID:object): # -> 
        """ SetServerIdentity(m: MethodCall, srvID: object) """
        ...


class IObjectHandle: # skipped bases: <type 'object'>
    """ no doc """
    def Unwrap(self) -> object:
        """ Unwrap(self: IObjectHandle) -> object """
        ...


class IRemotingTypeInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: IRemotingTypeInfo) -> str
        Set: TypeName(self: IRemotingTypeInfo) = value
        """
        ...


    def CanCastTo(self, fromType:Type, o:object) -> bool:
        """ CanCastTo(self: IRemotingTypeInfo, fromType: Type, o: object) -> bool """
        ...


class ObjectHandle(MarshalByRefObject, IObjectHandle): # skipped bases: <type 'object'>
    """ ObjectHandle(o: object) """
    def __new__(cls, o:object) -> Self:
        """ __new__(cls: type, o: object) """
        ...


class ObjRef(ISerializable, IObjectReference): # skipped bases: <type 'object'>
    """
    ObjRef(o: MarshalByRefObject, requestedType: Type)
    ObjRef()
    """
    @property
    def ChannelInfo(self) -> IChannelInfo:
        """
        Get: ChannelInfo(self: ObjRef) -> IChannelInfo
        Set: ChannelInfo(self: ObjRef) = value
        """
        ...

    @property
    def EnvoyInfo(self) -> IEnvoyInfo:
        """
        Get: EnvoyInfo(self: ObjRef) -> IEnvoyInfo
        Set: EnvoyInfo(self: ObjRef) = value
        """
        ...

    @property
    def TypeInfo(self) -> IRemotingTypeInfo:
        """
        Get: TypeInfo(self: ObjRef) -> IRemotingTypeInfo
        Set: TypeInfo(self: ObjRef) = value
        """
        ...

    @property
    def URI(self) -> str:
        """
        Get: URI(self: ObjRef) -> str
        Set: URI(self: ObjRef) = value
        """
        ...


    def IsFromThisAppDomain(self) -> bool:
        """ IsFromThisAppDomain(self: ObjRef) -> bool """
        ...

    def IsFromThisProcess(self) -> bool:
        """ IsFromThisProcess(self: ObjRef) -> bool """
        ...


class RemotingConfiguration: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ApplicationId(self) -> str:
        """ Get: ApplicationId() -> str """
        ...

    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName() -> str
        Set: ApplicationName() = value
        """
        ...

    @property
    def CustomErrorsMode(self) -> CustomErrorsModes:
        """
        Get: CustomErrorsMode() -> CustomErrorsModes
        Set: CustomErrorsMode() = value
        """
        ...

    @property
    def ProcessId(self) -> str:
        """ Get: ProcessId() -> str """
        ...


    @staticmethod
    def Configure(filename:str, ensureSecurity:bool = ...): # -> 
        """ Configure(filename: str)Configure(filename: str, ensureSecurity: bool) """
        ...

    @staticmethod
    def CustomErrorsEnabled(isLocalRequest:bool) -> bool:
        """ CustomErrorsEnabled(isLocalRequest: bool) -> bool """
        ...

    @staticmethod
    def GetRegisteredActivatedClientTypes() -> Array:
        """ GetRegisteredActivatedClientTypes() -> Array[ActivatedClientTypeEntry] """
        ...

    @staticmethod
    def GetRegisteredActivatedServiceTypes() -> Array:
        """ GetRegisteredActivatedServiceTypes() -> Array[ActivatedServiceTypeEntry] """
        ...

    @staticmethod
    def GetRegisteredWellKnownClientTypes() -> Array:
        """ GetRegisteredWellKnownClientTypes() -> Array[WellKnownClientTypeEntry] """
        ...

    @staticmethod
    def GetRegisteredWellKnownServiceTypes() -> Array:
        """ GetRegisteredWellKnownServiceTypes() -> Array[WellKnownServiceTypeEntry] """
        ...

    @staticmethod
    def IsActivationAllowed(svrType:Type) -> bool:
        """ IsActivationAllowed(svrType: Type) -> bool """
        ...

    @staticmethod
    def IsRemotelyActivatedClientType(*__args:Type) -> ActivatedClientTypeEntry:
        """
        IsRemotelyActivatedClientType(svrType: Type) -> ActivatedClientTypeEntry
        IsRemotelyActivatedClientType(typeName: str, assemblyName: str) -> ActivatedClientTypeEntry
        """
        ...

    @staticmethod
    def IsWellKnownClientType(*__args:Type) -> WellKnownClientTypeEntry:
        """
        IsWellKnownClientType(svrType: Type) -> WellKnownClientTypeEntry
        IsWellKnownClientType(typeName: str, assemblyName: str) -> WellKnownClientTypeEntry
        """
        ...

    @staticmethod
    def RegisterActivatedClientType(*__args:ActivatedClientTypeEntry): # -> 
        """ RegisterActivatedClientType(type: Type, appUrl: str)RegisterActivatedClientType(entry: ActivatedClientTypeEntry) """
        ...

    @staticmethod
    def RegisterActivatedServiceType(*__args:Type): # -> 
        """ RegisterActivatedServiceType(type: Type)RegisterActivatedServiceType(entry: ActivatedServiceTypeEntry) """
        ...

    @staticmethod
    def RegisterWellKnownClientType(*__args:WellKnownClientTypeEntry): # -> 
        """ RegisterWellKnownClientType(type: Type, objectUrl: str)RegisterWellKnownClientType(entry: WellKnownClientTypeEntry) """
        ...

    @staticmethod
    def RegisterWellKnownServiceType(*__args:WellKnownServiceTypeEntry): # -> 
        """ RegisterWellKnownServiceType(type: Type, objectUri: str, mode: WellKnownObjectMode)RegisterWellKnownServiceType(entry: WellKnownServiceTypeEntry) """
        ...

    __all__: list = ...


class RemotingException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RemotingException()
    RemotingException(message: str)
    RemotingException(message: str, InnerException: Exception)
    """
    SerializeObjectState = ...


class RemotingServices: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Connect(classToProxy:Type, url:str, data:object = ...) -> object:
        """
        Connect(classToProxy: Type, url: str) -> object
        Connect(classToProxy: Type, url: str, data: object) -> object
        """
        ...

    @staticmethod
    def Disconnect(obj:MarshalByRefObject) -> bool:
        """ Disconnect(obj: MarshalByRefObject) -> bool """
        ...

    @staticmethod
    def ExecuteMessage(target:MarshalByRefObject, reqMsg:IMethodCallMessage) -> IMethodReturnMessage:
        """ ExecuteMessage(target: MarshalByRefObject, reqMsg: IMethodCallMessage) -> IMethodReturnMessage """
        ...

    @staticmethod
    def GetEnvoyChainForProxy(obj:MarshalByRefObject) -> IMessageSink:
        """ GetEnvoyChainForProxy(obj: MarshalByRefObject) -> IMessageSink """
        ...

    @staticmethod
    def GetLifetimeService(obj:MarshalByRefObject) -> object:
        """ GetLifetimeService(obj: MarshalByRefObject) -> object """
        ...

    @staticmethod
    def GetMethodBaseFromMethodMessage(msg:IMethodMessage) -> MethodBase:
        """ GetMethodBaseFromMethodMessage(msg: IMethodMessage) -> MethodBase """
        ...

    @staticmethod
    def GetObjectData(obj:object, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(obj: object, info: SerializationInfo, context: StreamingContext) """
        ...

    @staticmethod
    def GetObjectUri(obj:MarshalByRefObject) -> str:
        """ GetObjectUri(obj: MarshalByRefObject) -> str """
        ...

    @staticmethod
    def GetObjRefForProxy(obj:MarshalByRefObject) -> ObjRef:
        """ GetObjRefForProxy(obj: MarshalByRefObject) -> ObjRef """
        ...

    @staticmethod
    def GetRealProxy(proxy:object) -> RealProxy:
        """ GetRealProxy(proxy: object) -> RealProxy """
        ...

    @staticmethod
    def GetServerTypeForUri(URI:str) -> Type:
        """ GetServerTypeForUri(URI: str) -> Type """
        ...

    @staticmethod
    def GetSessionIdForMethodMessage(msg:IMethodMessage) -> str:
        """ GetSessionIdForMethodMessage(msg: IMethodMessage) -> str """
        ...

    @staticmethod
    def IsMethodOverloaded(msg:IMethodMessage) -> bool:
        """ IsMethodOverloaded(msg: IMethodMessage) -> bool """
        ...

    @staticmethod
    def IsObjectOutOfAppDomain(tp:object) -> bool:
        """ IsObjectOutOfAppDomain(tp: object) -> bool """
        ...

    @staticmethod
    def IsObjectOutOfContext(tp:object) -> bool:
        """ IsObjectOutOfContext(tp: object) -> bool """
        ...

    @staticmethod
    def IsOneWay(method:MethodBase) -> bool:
        """ IsOneWay(method: MethodBase) -> bool """
        ...

    @staticmethod
    def IsTransparentProxy(proxy:object) -> bool:
        """ IsTransparentProxy(proxy: object) -> bool """
        ...

    @staticmethod
    def LogRemotingStage(stage:int): # -> 
        """ LogRemotingStage(stage: int) """
        ...

    @staticmethod
    def Marshal(Obj:MarshalByRefObject, *__args:str) -> ObjRef:
        """
        Marshal(Obj: MarshalByRefObject) -> ObjRef
        Marshal(Obj: MarshalByRefObject, URI: str) -> ObjRef
        Marshal(Obj: MarshalByRefObject, ObjURI: str, RequestedType: Type) -> ObjRef
        """
        ...

    @staticmethod
    def SetObjectUriForMarshal(obj:MarshalByRefObject, uri:str): # -> 
        """ SetObjectUriForMarshal(obj: MarshalByRefObject, uri: str) """
        ...

    @staticmethod
    def Unmarshal(objectRef:ObjRef, fRefine:bool = ...) -> object:
        """
        Unmarshal(objectRef: ObjRef) -> object
        Unmarshal(objectRef: ObjRef, fRefine: bool) -> object
        """
        ...

    __all__: list = ...


class RemotingTimeoutException(RemotingException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RemotingTimeoutException()
    RemotingTimeoutException(message: str)
    RemotingTimeoutException(message: str, InnerException: Exception)
    """
    SerializeObjectState = ...


class ServerException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ServerException()
    ServerException(message: str)
    ServerException(message: str, InnerException: Exception)
    """
    SerializeObjectState = ...


class SoapServices: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def XmlNsForClrType(self) -> str:
        """ Get: XmlNsForClrType() -> str """
        ...

    @property
    def XmlNsForClrTypeWithAssembly(self) -> str:
        """ Get: XmlNsForClrTypeWithAssembly() -> str """
        ...

    @property
    def XmlNsForClrTypeWithNs(self) -> str:
        """ Get: XmlNsForClrTypeWithNs() -> str """
        ...

    @property
    def XmlNsForClrTypeWithNsAndAssembly(self) -> str:
        """ Get: XmlNsForClrTypeWithNsAndAssembly() -> str """
        ...


    @staticmethod
    def CodeXmlNamespaceForClrTypeNamespace(typeNamespace:str, assemblyName:str) -> str:
        """ CodeXmlNamespaceForClrTypeNamespace(typeNamespace: str, assemblyName: str) -> str """
        ...

    @staticmethod
    def DecodeXmlNamespaceForClrTypeNamespace(inNamespace, typeNamespace, assemblyName) -> Tuple_[bool, str, str]:
        """ DecodeXmlNamespaceForClrTypeNamespace(inNamespace: str) -> (bool, str, str) """
        ...

    @staticmethod
    def GetInteropFieldTypeAndNameFromXmlAttribute(containingType, xmlAttribute, xmlNamespace, type, name) -> Tuple_[Type, str]:
        """ GetInteropFieldTypeAndNameFromXmlAttribute(containingType: Type, xmlAttribute: str, xmlNamespace: str) -> (Type, str) """
        ...

    @staticmethod
    def GetInteropFieldTypeAndNameFromXmlElement(containingType, xmlElement, xmlNamespace, type, name) -> Tuple_[Type, str]:
        """ GetInteropFieldTypeAndNameFromXmlElement(containingType: Type, xmlElement: str, xmlNamespace: str) -> (Type, str) """
        ...

    @staticmethod
    def GetInteropTypeFromXmlElement(xmlElement:str, xmlNamespace:str) -> Type:
        """ GetInteropTypeFromXmlElement(xmlElement: str, xmlNamespace: str) -> Type """
        ...

    @staticmethod
    def GetInteropTypeFromXmlType(xmlType:str, xmlTypeNamespace:str) -> Type:
        """ GetInteropTypeFromXmlType(xmlType: str, xmlTypeNamespace: str) -> Type """
        ...

    @staticmethod
    def GetSoapActionFromMethodBase(mb:MethodBase) -> str:
        """ GetSoapActionFromMethodBase(mb: MethodBase) -> str """
        ...

    @staticmethod
    def GetTypeAndMethodNameFromSoapAction(soapAction, typeName, methodName) -> Tuple_[bool, str, str]:
        """ GetTypeAndMethodNameFromSoapAction(soapAction: str) -> (bool, str, str) """
        ...

    @staticmethod
    def GetXmlElementForInteropType(type, xmlElement, xmlNamespace) -> Tuple_[bool, str, str]:
        """ GetXmlElementForInteropType(type: Type) -> (bool, str, str) """
        ...

    @staticmethod
    def GetXmlNamespaceForMethodCall(mb:MethodBase) -> str:
        """ GetXmlNamespaceForMethodCall(mb: MethodBase) -> str """
        ...

    @staticmethod
    def GetXmlNamespaceForMethodResponse(mb:MethodBase) -> str:
        """ GetXmlNamespaceForMethodResponse(mb: MethodBase) -> str """
        ...

    @staticmethod
    def GetXmlTypeForInteropType(type, xmlType, xmlTypeNamespace) -> Tuple_[bool, str, str]:
        """ GetXmlTypeForInteropType(type: Type) -> (bool, str, str) """
        ...

    @staticmethod
    def IsClrTypeNamespace(namespaceString:str) -> bool:
        """ IsClrTypeNamespace(namespaceString: str) -> bool """
        ...

    @staticmethod
    def IsSoapActionValidForMethodBase(soapAction:str, mb:MethodBase) -> bool:
        """ IsSoapActionValidForMethodBase(soapAction: str, mb: MethodBase) -> bool """
        ...

    @staticmethod
    def PreLoad(*__args:Assembly): # -> 
        """ PreLoad(assembly: Assembly)PreLoad(type: Type) """
        ...

    @staticmethod
    def RegisterInteropXmlElement(xmlElement:str, xmlNamespace:str, type:Type): # -> 
        """ RegisterInteropXmlElement(xmlElement: str, xmlNamespace: str, type: Type) """
        ...

    @staticmethod
    def RegisterInteropXmlType(xmlType:str, xmlTypeNamespace:str, type:Type): # -> 
        """ RegisterInteropXmlType(xmlType: str, xmlTypeNamespace: str, type: Type) """
        ...

    @staticmethod
    def RegisterSoapActionForMethodBase(mb:MethodBase, soapAction:str = ...): # -> 
        """ RegisterSoapActionForMethodBase(mb: MethodBase)RegisterSoapActionForMethodBase(mb: MethodBase, soapAction: str) """
        ...



class WellKnownClientTypeEntry(TypeEntry): # skipped bases: <type 'object'>
    """
    WellKnownClientTypeEntry(typeName: str, assemblyName: str, objectUrl: str)
    WellKnownClientTypeEntry(type: Type, objectUrl: str)
    """
    @property
    def ApplicationUrl(self) -> str:
        """
        Get: ApplicationUrl(self: WellKnownClientTypeEntry) -> str
        Set: ApplicationUrl(self: WellKnownClientTypeEntry) = value
        """
        ...

    @property
    def ObjectType(self) -> Type:
        """ Get: ObjectType(self: WellKnownClientTypeEntry) -> Type """
        ...

    @property
    def ObjectUrl(self) -> str:
        """ Get: ObjectUrl(self: WellKnownClientTypeEntry) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: WellKnownClientTypeEntry) -> str """
        ...

    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, typeName: str, assemblyName: str, objectUrl: str)
        __new__(cls: type, type: Type, objectUrl: str)
        """
        ...


class WellKnownObjectMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WellKnownObjectMode, values: SingleCall (2), Singleton (1) """
    SingleCall: WellKnownObjectMode = ...
    Singleton: WellKnownObjectMode = ...
    value__ = ...


class WellKnownServiceTypeEntry(TypeEntry): # skipped bases: <type 'object'>
    """
    WellKnownServiceTypeEntry(typeName: str, assemblyName: str, objectUri: str, mode: WellKnownObjectMode)
    WellKnownServiceTypeEntry(type: Type, objectUri: str, mode: WellKnownObjectMode)
    """
    @property
    def ContextAttributes(self) -> Array:
        """
        Get: ContextAttributes(self: WellKnownServiceTypeEntry) -> Array[IContextAttribute]
        Set: ContextAttributes(self: WellKnownServiceTypeEntry) = value
        """
        ...

    @property
    def Mode(self) -> WellKnownObjectMode:
        """ Get: Mode(self: WellKnownServiceTypeEntry) -> WellKnownObjectMode """
        ...

    @property
    def ObjectType(self) -> Type:
        """ Get: ObjectType(self: WellKnownServiceTypeEntry) -> Type """
        ...

    @property
    def ObjectUri(self) -> str:
        """ Get: ObjectUri(self: WellKnownServiceTypeEntry) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: WellKnownServiceTypeEntry) -> str """
        ...

    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, typeName: str, assemblyName: str, objectUri: str, mode: WellKnownObjectMode)
        __new__(cls: type, type: Type, objectUri: str, mode: WellKnownObjectMode)
        """
        ...


# variables with complex values

