# encoding: utf-8
# module System.Runtime.Remoting.Proxies calls itself Proxies
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.JScript import Context

from System import Attribute, Guid, IntPtr, MarshalByRefObject, Type

from System.Runtime.Remoting import ObjRef

from System.Runtime.Remoting.Activation import (IConstructionCallMessage, 
    IConstructionReturnMessage)

from System.Runtime.Remoting.Contexts import IContextAttribute

from System.Runtime.Remoting.Messaging import IMessage

from System.Runtime.Serialization import SerializationInfo, StreamingContext

from typing import Tuple as Tuple_


# no functions
# classes

class ProxyAttribute(IContextAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ProxyAttribute() """
    def CreateInstance(self, serverType:Type) -> MarshalByRefObject:
        """ CreateInstance(self: ProxyAttribute, serverType: Type) -> MarshalByRefObject """
        ...

    def CreateProxy(self, objRef:ObjRef, serverType:Type, serverObject:object, serverContext:Context) -> RealProxy:
        """ CreateProxy(self: ProxyAttribute, objRef: ObjRef, serverType: Type, serverObject: object, serverContext: Context) -> RealProxy """
        ...


class RealProxy: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def AttachServer(self, *args): #cannot find CLR method
        """ AttachServer(self: RealProxy, s: MarshalByRefObject) """
        ...

    def CreateObjRef(self, requestedType:Type) -> ObjRef:
        """ CreateObjRef(self: RealProxy, requestedType: Type) -> ObjRef """
        ...

    def DetachServer(self, *args): #cannot find CLR method
        """ DetachServer(self: RealProxy) -> MarshalByRefObject """
        ...

    def GetCOMIUnknown(self, fIsMarshalled:bool) -> IntPtr:
        """ GetCOMIUnknown(self: RealProxy, fIsMarshalled: bool) -> IntPtr """
        ...

    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: RealProxy, info: SerializationInfo, context: StreamingContext) """
        ...

    def GetProxiedType(self) -> Type:
        """ GetProxiedType(self: RealProxy) -> Type """
        ...

    @staticmethod
    def GetStubData(rp:RealProxy) -> object:
        """ GetStubData(rp: RealProxy) -> object """
        ...

    def GetTransparentProxy(self) -> object:
        """ GetTransparentProxy(self: RealProxy) -> object """
        ...

    def GetUnwrappedServer(self, *args): #cannot find CLR method
        """ GetUnwrappedServer(self: RealProxy) -> MarshalByRefObject """
        ...

    def InitializeServerObject(self, ctorMsg:IConstructionCallMessage) -> IConstructionReturnMessage:
        """ InitializeServerObject(self: RealProxy, ctorMsg: IConstructionCallMessage) -> IConstructionReturnMessage """
        ...

    def Invoke(self, msg:IMessage) -> IMessage:
        """ Invoke(self: RealProxy, msg: IMessage) -> IMessage """
        ...

    def SetCOMIUnknown(self, i:IntPtr): # -> 
        """ SetCOMIUnknown(self: RealProxy, i: IntPtr) """
        ...

    @staticmethod
    def SetStubData(rp:RealProxy, stubData:object): # -> 
        """ SetStubData(rp: RealProxy, stubData: object) """
        ...

    def SupportsInterface(self, iid:Guid) -> Tuple_[IntPtr, Guid]:
        """ SupportsInterface(self: RealProxy, iid: Guid) -> (IntPtr, Guid) """
        ...


