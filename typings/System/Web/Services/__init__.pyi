# encoding: utf-8
# module System.Web.Services calls itself Services
# from System.Web.Services, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute, Enum

from System.ComponentModel import MarshalByValueComponent

from System.EnterpriseServices import TransactionOption

from System.Security.Principal import IPrincipal

from System.Web import HttpApplicationState, HttpContext, HttpServerUtility

from System.Web.Services.Protocols import SoapProtocolVersion

from System.Web.SessionState import HttpSessionState

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class WebMethodAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    WebMethodAttribute()
    WebMethodAttribute(enableSession: bool)
    WebMethodAttribute(enableSession: bool, transactionOption: TransactionOption)
    WebMethodAttribute(enableSession: bool, transactionOption: TransactionOption, cacheDuration: int)
    WebMethodAttribute(enableSession: bool, transactionOption: TransactionOption, cacheDuration: int, bufferResponse: bool)
    """
    @property
    def BufferResponse(self) -> bool:
        """
        Get: BufferResponse(self: WebMethodAttribute) -> bool
        Set: BufferResponse(self: WebMethodAttribute) = value
        """
        ...

    @property
    def CacheDuration(self) -> int:
        """
        Get: CacheDuration(self: WebMethodAttribute) -> int
        Set: CacheDuration(self: WebMethodAttribute) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: WebMethodAttribute) -> str
        Set: Description(self: WebMethodAttribute) = value
        """
        ...

    @property
    def EnableSession(self) -> bool:
        """
        Get: EnableSession(self: WebMethodAttribute) -> bool
        Set: EnableSession(self: WebMethodAttribute) = value
        """
        ...

    @property
    def MessageName(self) -> str:
        """
        Get: MessageName(self: WebMethodAttribute) -> str
        Set: MessageName(self: WebMethodAttribute) = value
        """
        ...

    @property
    def TransactionOption(self) -> TransactionOption:
        """
        Get: TransactionOption(self: WebMethodAttribute) -> TransactionOption
        Set: TransactionOption(self: WebMethodAttribute) = value
        """
        ...


    def __new__(cls, enableSession:bool = ..., transactionOption:TransactionOption = ..., cacheDuration:int = ..., bufferResponse:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, enableSession: bool)
        __new__(cls: type, enableSession: bool, transactionOption: TransactionOption)
        __new__(cls: type, enableSession: bool, transactionOption: TransactionOption, cacheDuration: int)
        __new__(cls: type, enableSession: bool, transactionOption: TransactionOption, cacheDuration: int, bufferResponse: bool)
        """
        ...


class WebService(MarshalByValueComponent): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IServiceProvider'>, <type 'object'>
    """ WebService() """
    @property
    def Application(self) -> HttpApplicationState:
        """ Get: Application(self: WebService) -> HttpApplicationState """
        ...

    @property
    def Context(self) -> HttpContext:
        """ Get: Context(self: WebService) -> HttpContext """
        ...

    @property
    def Server(self) -> HttpServerUtility:
        """ Get: Server(self: WebService) -> HttpServerUtility """
        ...

    @property
    def Session(self) -> HttpSessionState:
        """ Get: Session(self: WebService) -> HttpSessionState """
        ...

    @property
    def SoapVersion(self) -> SoapProtocolVersion:
        """ Get: SoapVersion(self: WebService) -> SoapProtocolVersion """
        ...

    @property
    def User(self) -> IPrincipal:
        """ Get: User(self: WebService) -> IPrincipal """
        ...



class WebServiceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ WebServiceAttribute() """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: WebServiceAttribute) -> str
        Set: Description(self: WebServiceAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: WebServiceAttribute) -> str
        Set: Name(self: WebServiceAttribute) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: WebServiceAttribute) -> str
        Set: Namespace(self: WebServiceAttribute) = value
        """
        ...


    DefaultNamespace: str = ...


class WebServiceBindingAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    WebServiceBindingAttribute()
    WebServiceBindingAttribute(name: str)
    WebServiceBindingAttribute(name: str, ns: str)
    WebServiceBindingAttribute(name: str, ns: str, location: str)
    """
    @property
    def ConformsTo(self) -> WsiProfiles:
        """
        Get: ConformsTo(self: WebServiceBindingAttribute) -> WsiProfiles
        Set: ConformsTo(self: WebServiceBindingAttribute) = value
        """
        ...

    @property
    def EmitConformanceClaims(self) -> bool:
        """
        Get: EmitConformanceClaims(self: WebServiceBindingAttribute) -> bool
        Set: EmitConformanceClaims(self: WebServiceBindingAttribute) = value
        """
        ...

    @property
    def Location(self) -> str:
        """
        Get: Location(self: WebServiceBindingAttribute) -> str
        Set: Location(self: WebServiceBindingAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: WebServiceBindingAttribute) -> str
        Set: Name(self: WebServiceBindingAttribute) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: WebServiceBindingAttribute) -> str
        Set: Namespace(self: WebServiceBindingAttribute) = value
        """
        ...


    def __new__(cls, name:str = ..., ns:str = ..., location:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, ns: str)
        __new__(cls: type, name: str, ns: str, location: str)
        """
        ...


class WsiProfiles(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) WsiProfiles, values: BasicProfile1_1 (1), None (0) """
    BasicProfile1_1: WsiProfiles = ...
    value__ = ...


# variables with complex values

