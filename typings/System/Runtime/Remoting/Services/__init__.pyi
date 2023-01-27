# encoding: utf-8
# module System.Runtime.Remoting.Services calls itself Services
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Runtime.Remoting, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, IntPtr, MarshalByRefObject

from System.ComponentModel import Component

from System.Runtime.Remoting import ObjRef

from System.Runtime.Remoting.Activation import (IConstructionCallMessage, 
    IConstructionReturnMessage)

from System.Runtime.Remoting.Proxies import RealProxy

from System.Security.Principal import IPrincipal

from System.Web import HttpApplicationState, HttpContext, HttpServerUtility

from System.Web.SessionState import HttpSessionState

"""The following names are not found in the module: field#
"""

# no functions
# classes

class EnterpriseServicesHelper: # skipped bases: <type 'object'>, <type 'object'>
    """ EnterpriseServicesHelper() """
    @staticmethod
    def CreateConstructionReturnMessage(ctorMsg:IConstructionCallMessage, retObj:MarshalByRefObject) -> IConstructionReturnMessage:
        """ CreateConstructionReturnMessage(ctorMsg: IConstructionCallMessage, retObj: MarshalByRefObject) -> IConstructionReturnMessage """
        ...

    @staticmethod
    def SwitchWrappers(oldcp:RealProxy, newcp:RealProxy): # -> 
        """ SwitchWrappers(oldcp: RealProxy, newcp: RealProxy) """
        ...

    @staticmethod
    def WrapIUnknownWithComObject(punk:IntPtr) -> object:
        """ WrapIUnknownWithComObject(punk: IntPtr) -> object """
        ...


class ITrackingHandler: # skipped bases: <type 'object'>
    """ no doc """
    def DisconnectedObject(self, obj:object): # -> 
        """ DisconnectedObject(self: ITrackingHandler, obj: object) """
        ...

    def MarshaledObject(self, obj:object, or_:ObjRef): # -> 
        """ MarshaledObject(self: ITrackingHandler, obj: object, or: ObjRef) """
        ...

    def UnmarshaledObject(self, obj:object, or_:ObjRef): # -> 
        """ UnmarshaledObject(self: ITrackingHandler, obj: object, or: ObjRef) """
        ...


class RemotingClientProxy(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    @property
    def AllowAutoRedirect(self) -> bool:
        """
        Get: AllowAutoRedirect(self: RemotingClientProxy) -> bool
        Set: AllowAutoRedirect(self: RemotingClientProxy) = value
        """
        ...

    @property
    def Cookies(self) -> object:
        """ Get: Cookies(self: RemotingClientProxy) -> object """
        ...

    @property
    def Domain(self) -> str:
        """
        Get: Domain(self: RemotingClientProxy) -> str
        Set: Domain(self: RemotingClientProxy) = value
        """
        ...

    @property
    def EnableCookies(self) -> bool:
        """
        Get: EnableCookies(self: RemotingClientProxy) -> bool
        Set: EnableCookies(self: RemotingClientProxy) = value
        """
        ...

    @property
    def Password(self) -> str:
        """
        Get: Password(self: RemotingClientProxy) -> str
        Set: Password(self: RemotingClientProxy) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: RemotingClientProxy) -> str
        Set: Path(self: RemotingClientProxy) = value
        """
        ...

    @property
    def PreAuthenticate(self) -> bool:
        """
        Get: PreAuthenticate(self: RemotingClientProxy) -> bool
        Set: PreAuthenticate(self: RemotingClientProxy) = value
        """
        ...

    @property
    def ProxyName(self) -> str:
        """
        Get: ProxyName(self: RemotingClientProxy) -> str
        Set: ProxyName(self: RemotingClientProxy) = value
        """
        ...

    @property
    def ProxyPort(self) -> int:
        """
        Get: ProxyPort(self: RemotingClientProxy) -> int
        Set: ProxyPort(self: RemotingClientProxy) = value
        """
        ...

    @property
    def Timeout(self) -> int:
        """
        Get: Timeout(self: RemotingClientProxy) -> int
        Set: Timeout(self: RemotingClientProxy) = value
        """
        ...

    @property
    def Url(self) -> str:
        """
        Get: Url(self: RemotingClientProxy) -> str
        Set: Url(self: RemotingClientProxy) = value
        """
        ...

    @property
    def UserAgent(self) -> str:
        """
        Get: UserAgent(self: RemotingClientProxy) -> str
        Set: UserAgent(self: RemotingClientProxy) = value
        """
        ...

    @property
    def Username(self) -> str:
        """
        Get: Username(self: RemotingClientProxy) -> str
        Set: Username(self: RemotingClientProxy) = value
        """
        ...


    def ConfigureProxy(self, *args): #cannot find CLR method
        """ ConfigureProxy(self: RemotingClientProxy, type: Type, url: str) """
        ...

    def ConnectProxy(self, *args): #cannot find CLR method
        """ ConnectProxy(self: RemotingClientProxy) """
        ...

    _tp = ...
    _type = ...
    _url = ...


class RemotingService(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ RemotingService() """
    @property
    def Application(self) -> HttpApplicationState:
        """ Get: Application(self: RemotingService) -> HttpApplicationState """
        ...

    @property
    def Context(self) -> HttpContext:
        """ Get: Context(self: RemotingService) -> HttpContext """
        ...

    @property
    def Server(self) -> HttpServerUtility:
        """ Get: Server(self: RemotingService) -> HttpServerUtility """
        ...

    @property
    def Session(self) -> HttpSessionState:
        """ Get: Session(self: RemotingService) -> HttpSessionState """
        ...

    @property
    def User(self) -> IPrincipal:
        """ Get: User(self: RemotingService) -> IPrincipal """
        ...



class TrackingServices: # skipped bases: <type 'object'>, <type 'object'>
    """ TrackingServices() """
    @property
    def RegisteredHandlers(self) -> Array:
        """ Get: RegisteredHandlers() -> Array[ITrackingHandler] """
        ...


    @staticmethod
    def RegisterTrackingHandler(handler:ITrackingHandler): # -> 
        """ RegisterTrackingHandler(handler: ITrackingHandler) """
        ...

    @staticmethod
    def UnregisterTrackingHandler(handler:ITrackingHandler): # -> 
        """ UnregisterTrackingHandler(handler: ITrackingHandler) """
        ...



