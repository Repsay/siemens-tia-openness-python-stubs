# encoding: utf-8
# module Microsoft.DataWarehouse.Serialization calls itself Serialization
# from Microsoft.DataWarehouse.Interfaces, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Type


# no functions
# classes

class IDeserializationStartCallback: # skipped bases: <type 'object'>
    """ no doc """
    def OnDeserializationBegin(self, sender:object): # -> 
        """ OnDeserializationBegin(self: IDeserializationStartCallback, sender: object) """
        ...


class IObjectOnDemandLoader: # skipped bases: <type 'object'>
    """ no doc """
    def LoadObjectOnDemand(self, loadableObject:object, context:object) -> bool:
        """ LoadObjectOnDemand(self: IObjectOnDemandLoader, loadableObject: object, context: object) -> bool """
        ...


class IExtensibleOnDemandObjectLoader(IObjectOnDemandLoader): # skipped bases: <type 'object'>
    """ no doc """
    def AddExtender(self, type:Type, extender:IOnDemandLoaderExtender): # -> 
        """ AddExtender(self: IExtensibleOnDemandObjectLoader, type: Type, extender: IOnDemandLoaderExtender) """
        ...

    def RemoveExtender(self, type:Type, extender:IOnDemandLoaderExtender): # -> 
        """ RemoveExtender(self: IExtensibleOnDemandObjectLoader, type: Type, extender: IOnDemandLoaderExtender) """
        ...


class IOnDemandLoaderExtender: # skipped bases: <type 'object'>
    """ no doc """
    def CanLoadOnDemand(self, loadableObject:object, context:object) -> bool:
        """ CanLoadOnDemand(self: IOnDemandLoaderExtender, loadableObject: object, context: object) -> bool """
        ...

    def LoadOnDemand(self, loadableObject:object, context:object) -> bool:
        """ LoadOnDemand(self: IOnDemandLoaderExtender, loadableObject: object, context: object) -> bool """
        ...


class ISerializationStartCallback: # skipped bases: <type 'object'>
    """ no doc """
    def OnSerializationBegin(self, sender:object): # -> 
        """ OnSerializationBegin(self: ISerializationStartCallback, sender: object) """
        ...


