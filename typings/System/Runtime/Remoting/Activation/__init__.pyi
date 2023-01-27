# encoding: utf-8
# module System.Runtime.Remoting.Activation calls itself Activation
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, Type

from System.Collections import IList

from System.Runtime.Remoting.Contexts import ContextAttribute

from System.Runtime.Remoting.Messaging import (IMethodCallMessage, 
    IMethodReturnMessage)

"""The following names are not found in the module: field#
"""

# no functions
# classes

class ActivatorLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ActivatorLevel, values: AppDomain (12), Construction (4), Context (8), Machine (20), Process (16) """
    AppDomain: ActivatorLevel = ...
    Construction: ActivatorLevel = ...
    Context: ActivatorLevel = ...
    Machine: ActivatorLevel = ...
    Process: ActivatorLevel = ...
    value__ = ...


class IActivator: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Level(self) -> ActivatorLevel:
        """ Get: Level(self: IActivator) -> ActivatorLevel """
        ...

    @property
    def NextActivator(self) -> IActivator:
        """
        Get: NextActivator(self: IActivator) -> IActivator
        Set: NextActivator(self: IActivator) = value
        """
        ...


    def Activate(self, msg:IConstructionCallMessage) -> IConstructionReturnMessage:
        """ Activate(self: IActivator, msg: IConstructionCallMessage) -> IConstructionReturnMessage """
        ...


class IConstructionCallMessage(IMethodCallMessage): # skipped bases: <type 'IMethodMessage'>, <type 'IMessage'>, <type 'object'>
    """ no doc """
    @property
    def ActivationType(self) -> Type:
        """ Get: ActivationType(self: IConstructionCallMessage) -> Type """
        ...

    @property
    def ActivationTypeName(self) -> str:
        """ Get: ActivationTypeName(self: IConstructionCallMessage) -> str """
        ...

    @property
    def Activator(self) -> IActivator:
        """
        Get: Activator(self: IConstructionCallMessage) -> IActivator
        Set: Activator(self: IConstructionCallMessage) = value
        """
        ...

    @property
    def CallSiteActivationAttributes(self) -> Array:
        """ Get: CallSiteActivationAttributes(self: IConstructionCallMessage) -> Array[object] """
        ...

    @property
    def ContextProperties(self) -> IList:
        """ Get: ContextProperties(self: IConstructionCallMessage) -> IList """
        ...



class IConstructionReturnMessage(IMethodReturnMessage): # skipped bases: <type 'IMethodMessage'>, <type 'IMessage'>, <type 'object'>
    """ no doc """
    pass

class UrlAttribute(ContextAttribute): # skipped bases: <type '_Attribute'>, <type 'IContextProperty'>, <type 'IContextAttribute'>, <type 'object'>
    """ UrlAttribute(callsiteURL: str) """
    @property
    def UrlValue(self) -> str:
        """ Get: UrlValue(self: UrlAttribute) -> str """
        ...


    AttributeName = ...


