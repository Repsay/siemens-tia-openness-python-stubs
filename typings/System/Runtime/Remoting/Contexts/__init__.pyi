# encoding: utf-8
# module System.Runtime.Remoting.Contexts calls itself Contexts
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Attribute, ContextBoundObject, 
    IAsyncResult, LocalDataStoreSlot, MarshalByRefObject, MulticastDelegate)

from System.Runtime.Remoting.Activation import (IConstructionCallMessage, 
    IConstructionReturnMessage)

from System.Runtime.Remoting.Messaging import IMessage, IMessageSink

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class Context: # skipped bases: <type 'object'>, <type 'object'>
    """ Context() """
    @property
    def ContextID(self) -> int:
        """ Get: ContextID(self: Context) -> int """
        ...

    @property
    def ContextProperties(self) -> Array:
        """ Get: ContextProperties(self: Context) -> Array[IContextProperty] """
        ...

    @property
    def DefaultContext(self) -> Context:
        """ Get: DefaultContext() -> Context """
        ...


    @staticmethod
    def AllocateDataSlot() -> LocalDataStoreSlot:
        """ AllocateDataSlot() -> LocalDataStoreSlot """
        ...

    @staticmethod
    def AllocateNamedDataSlot(name:str) -> LocalDataStoreSlot:
        """ AllocateNamedDataSlot(name: str) -> LocalDataStoreSlot """
        ...

    def DoCallBack(self, deleg:CrossContextDelegate): # -> 
        """ DoCallBack(self: Context, deleg: CrossContextDelegate) """
        ...

    @staticmethod
    def FreeNamedDataSlot(name:str): # -> 
        """ FreeNamedDataSlot(name: str) """
        ...

    def Freeze(self): # -> 
        """ Freeze(self: Context) """
        ...

    @staticmethod
    def GetData(slot:LocalDataStoreSlot) -> object:
        """ GetData(slot: LocalDataStoreSlot) -> object """
        ...

    @staticmethod
    def GetNamedDataSlot(name:str) -> LocalDataStoreSlot:
        """ GetNamedDataSlot(name: str) -> LocalDataStoreSlot """
        ...

    def GetProperty(self, name:str) -> IContextProperty:
        """ GetProperty(self: Context, name: str) -> IContextProperty """
        ...

    @staticmethod
    def RegisterDynamicProperty(prop:IDynamicProperty, obj:ContextBoundObject, ctx:Context) -> bool:
        """ RegisterDynamicProperty(prop: IDynamicProperty, obj: ContextBoundObject, ctx: Context) -> bool """
        ...

    @staticmethod
    def SetData(slot:LocalDataStoreSlot, data:object): # -> 
        """ SetData(slot: LocalDataStoreSlot, data: object) """
        ...

    def SetProperty(self, prop:IContextProperty): # -> 
        """ SetProperty(self: Context, prop: IContextProperty) """
        ...

    def ToString(self) -> str:
        """ ToString(self: Context) -> str """
        ...

    @staticmethod
    def UnregisterDynamicProperty(name:str, obj:ContextBoundObject, ctx:Context) -> bool:
        """ UnregisterDynamicProperty(name: str, obj: ContextBoundObject, ctx: Context) -> bool """
        ...



class IContextAttribute: # skipped bases: <type 'object'>
    """ no doc """
    def GetPropertiesForNewContext(self, msg:IConstructionCallMessage): # -> 
        """ GetPropertiesForNewContext(self: IContextAttribute, msg: IConstructionCallMessage) """
        ...

    def IsContextOK(self, ctx:Context, msg:IConstructionCallMessage) -> bool:
        """ IsContextOK(self: IContextAttribute, ctx: Context, msg: IConstructionCallMessage) -> bool """
        ...


class IContextProperty: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: IContextProperty) -> str """
        ...


    def Freeze(self, newContext:Context): # -> 
        """ Freeze(self: IContextProperty, newContext: Context) """
        ...

    def IsNewContextOK(self, newCtx:Context) -> bool:
        """ IsNewContextOK(self: IContextProperty, newCtx: Context) -> bool """
        ...


class ContextAttribute(IContextAttribute, IContextProperty, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ContextAttribute(name: str) """
    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...

    AttributeName = ...


class ContextProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: ContextProperty) -> str """
        ...

    @property
    def Property(self) -> object:
        """ Get: Property(self: ContextProperty) -> object """
        ...



class CrossContextDelegate(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CrossContextDelegate(object: object, method: IntPtr) """
    def BeginInvoke(self, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: CrossContextDelegate, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: CrossContextDelegate, result: IAsyncResult) """
        ...

    def Invoke(self): # -> 
        """ Invoke(self: CrossContextDelegate) """
        ...


class IContextPropertyActivator: # skipped bases: <type 'object'>
    """ no doc """
    def CollectFromClientContext(self, msg:IConstructionCallMessage): # -> 
        """ CollectFromClientContext(self: IContextPropertyActivator, msg: IConstructionCallMessage) """
        ...

    def CollectFromServerContext(self, msg:IConstructionReturnMessage): # -> 
        """ CollectFromServerContext(self: IContextPropertyActivator, msg: IConstructionReturnMessage) """
        ...

    def DeliverClientContextToServerContext(self, msg:IConstructionCallMessage) -> bool:
        """ DeliverClientContextToServerContext(self: IContextPropertyActivator, msg: IConstructionCallMessage) -> bool """
        ...

    def DeliverServerContextToClientContext(self, msg:IConstructionReturnMessage) -> bool:
        """ DeliverServerContextToClientContext(self: IContextPropertyActivator, msg: IConstructionReturnMessage) -> bool """
        ...

    def IsOKToActivate(self, msg:IConstructionCallMessage) -> bool:
        """ IsOKToActivate(self: IContextPropertyActivator, msg: IConstructionCallMessage) -> bool """
        ...


class IContributeClientContextSink: # skipped bases: <type 'object'>
    """ no doc """
    def GetClientContextSink(self, nextSink:IMessageSink) -> IMessageSink:
        """ GetClientContextSink(self: IContributeClientContextSink, nextSink: IMessageSink) -> IMessageSink """
        ...


class IContributeDynamicSink: # skipped bases: <type 'object'>
    """ no doc """
    def GetDynamicSink(self) -> IDynamicMessageSink:
        """ GetDynamicSink(self: IContributeDynamicSink) -> IDynamicMessageSink """
        ...


class IContributeEnvoySink: # skipped bases: <type 'object'>
    """ no doc """
    def GetEnvoySink(self, obj:MarshalByRefObject, nextSink:IMessageSink) -> IMessageSink:
        """ GetEnvoySink(self: IContributeEnvoySink, obj: MarshalByRefObject, nextSink: IMessageSink) -> IMessageSink """
        ...


class IContributeObjectSink: # skipped bases: <type 'object'>
    """ no doc """
    def GetObjectSink(self, obj:MarshalByRefObject, nextSink:IMessageSink) -> IMessageSink:
        """ GetObjectSink(self: IContributeObjectSink, obj: MarshalByRefObject, nextSink: IMessageSink) -> IMessageSink """
        ...


class IContributeServerContextSink: # skipped bases: <type 'object'>
    """ no doc """
    def GetServerContextSink(self, nextSink:IMessageSink) -> IMessageSink:
        """ GetServerContextSink(self: IContributeServerContextSink, nextSink: IMessageSink) -> IMessageSink """
        ...


class IDynamicMessageSink: # skipped bases: <type 'object'>
    """ no doc """
    def ProcessMessageFinish(self, replyMsg:IMessage, bCliSide:bool, bAsync:bool): # -> 
        """ ProcessMessageFinish(self: IDynamicMessageSink, replyMsg: IMessage, bCliSide: bool, bAsync: bool) """
        ...

    def ProcessMessageStart(self, reqMsg:IMessage, bCliSide:bool, bAsync:bool): # -> 
        """ ProcessMessageStart(self: IDynamicMessageSink, reqMsg: IMessage, bCliSide: bool, bAsync: bool) """
        ...


class IDynamicProperty: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: IDynamicProperty) -> str """
        ...



class SynchronizationAttribute(ContextAttribute, IContributeClientContextSink, IContributeServerContextSink): # skipped bases: <type '_Attribute'>, <type 'IContextProperty'>, <type 'IContextAttribute'>, <type 'object'>
    """
    SynchronizationAttribute()
    SynchronizationAttribute(reEntrant: bool)
    SynchronizationAttribute(flag: int)
    SynchronizationAttribute(flag: int, reEntrant: bool)
    """
    @property
    def IsReEntrant(self) -> bool:
        """ Get: IsReEntrant(self: SynchronizationAttribute) -> bool """
        ...

    @property
    def Locked(self) -> bool:
        """
        Get: Locked(self: SynchronizationAttribute) -> bool
        Set: Locked(self: SynchronizationAttribute) = value
        """
        ...


    AttributeName = ...
    NOT_SUPPORTED: int = ...
    REQUIRED: int = ...
    REQUIRES_NEW: int = ...
    SUPPORTED: int = ...


