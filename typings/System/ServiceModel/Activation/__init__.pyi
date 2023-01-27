# encoding: utf-8
# module System.ServiceModel.Activation calls itself Activation
# from System.WorkflowServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.ServiceModel.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.ServiceModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Attribute, Enum

from System.ServiceModel import IExtension, ServiceHostBase

"""The following names are not found in the module: (
    AspNetCompatibilityRequirementsMode, IServiceBehavior, ServiceHostFactory, 
    field#)
"""

# no functions
# classes

class AspNetCompatibilityRequirementsAttribute(Attribute, IServiceBehavior): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AspNetCompatibilityRequirementsAttribute() """
    @property
    def RequirementsMode(self): # -> AspNetCompatibilityRequirementsMode
        """
        Get: RequirementsMode(self: AspNetCompatibilityRequirementsAttribute) -> AspNetCompatibilityRequirementsMode
        Set: RequirementsMode(self: AspNetCompatibilityRequirementsAttribute) = value
        """
        ...



class AspNetCompatibilityRequirementsMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AspNetCompatibilityRequirementsMode, values: Allowed (1), NotAllowed (0), Required (2) """
    Allowed: AspNetCompatibilityRequirementsMode = ...
    NotAllowed: AspNetCompatibilityRequirementsMode = ...
    Required: AspNetCompatibilityRequirementsMode = ...
    value__ = ...


class ServiceHostFactoryBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateServiceHost(self, constructorString:str, baseAddresses:Array) -> ServiceHostBase:
        """ CreateServiceHost(self: ServiceHostFactoryBase, constructorString: str, baseAddresses: Array[Uri]) -> ServiceHostBase """
        ...


class VirtualPathExtension(IExtension): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ApplicationVirtualPath(self) -> str:
        """ Get: ApplicationVirtualPath(self: VirtualPathExtension) -> str """
        ...

    @property
    def SiteName(self) -> str:
        """ Get: SiteName(self: VirtualPathExtension) -> str """
        ...

    @property
    def VirtualPath(self) -> str:
        """ Get: VirtualPath(self: VirtualPathExtension) -> str """
        ...



class WebScriptServiceHostFactory(ServiceHostFactory): # skipped bases: <type 'object'>
    """ WebScriptServiceHostFactory() """
    pass

class WebServiceHostFactory(ServiceHostFactory): # skipped bases: <type 'object'>
    """ WebServiceHostFactory() """
    pass

class WorkflowServiceHostFactory(ServiceHostFactoryBase): # skipped bases: <type 'object'>
    """ WorkflowServiceHostFactory() """
    pass

# variables with complex values

