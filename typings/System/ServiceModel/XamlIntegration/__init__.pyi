# encoding: utf-8
# module System.ServiceModel.XamlIntegration calls itself XamlIntegration
# from System.ServiceModel.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.ServiceModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Collections.Generic import Dictionary

from System.ComponentModel import TypeConverter

from System.Windows.Markup import MarkupExtension

from typing import Self

"""The following names are not found in the module: (SpnEndpointIdentity, 
    UpnEndpointIdentity, XPathMessageContext)
"""

# no functions
# classes

class EndpointIdentityConverter(TypeConverter): # skipped bases: <type 'object'>
    """ EndpointIdentityConverter() """
    pass

class ServiceXNameTypeConverter(TypeConverter): # skipped bases: <type 'object'>
    """ ServiceXNameTypeConverter() """
    pass

class SpnEndpointIdentityExtension(MarkupExtension): # skipped bases: <type 'object'>
    """
    SpnEndpointIdentityExtension()
    SpnEndpointIdentityExtension(identity: SpnEndpointIdentity)
    """
    @property
    def SpnName(self) -> str:
        """
        Get: SpnName(self: SpnEndpointIdentityExtension) -> str
        Set: SpnName(self: SpnEndpointIdentityExtension) = value
        """
        ...


    def __new__(cls, identity = ...) -> Self: # Not found arg types: {'identity': 'SpnEndpointIdentity'}
        """
        __new__(cls: type)
        __new__(cls: type, identity: SpnEndpointIdentity)
        """
        ...


class UpnEndpointIdentityExtension(MarkupExtension): # skipped bases: <type 'object'>
    """
    UpnEndpointIdentityExtension()
    UpnEndpointIdentityExtension(identity: UpnEndpointIdentity)
    """
    @property
    def UpnName(self) -> str:
        """
        Get: UpnName(self: UpnEndpointIdentityExtension) -> str
        Set: UpnName(self: UpnEndpointIdentityExtension) = value
        """
        ...


    def __new__(cls, identity = ...) -> Self: # Not found arg types: {'identity': 'UpnEndpointIdentity'}
        """
        __new__(cls: type)
        __new__(cls: type, identity: UpnEndpointIdentity)
        """
        ...


class XPathMessageContextMarkupExtension(MarkupExtension): # skipped bases: <type 'object'>
    """
    XPathMessageContextMarkupExtension()
    XPathMessageContextMarkupExtension(context: XPathMessageContext)
    """
    @property
    def Namespaces(self) -> Dictionary:
        """ Get: Namespaces(self: XPathMessageContextMarkupExtension) -> Dictionary[str, str] """
        ...


    def __new__(cls, context = ...) -> Self: # Not found arg types: {'context': 'XPathMessageContext'}
        """
        __new__(cls: type)
        __new__(cls: type, context: XPathMessageContext)
        """
        ...


class XPathMessageContextTypeConverter(TypeConverter): # skipped bases: <type 'object'>
    """ XPathMessageContextTypeConverter() """
    pass

