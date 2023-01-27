# encoding: utf-8
# module Microsoft.DataWarehouse.ComponentModel calls itself ComponentModel
# from Microsoft.DataWarehouse.Interfaces, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.ComponentModel import IComponent


# no functions
# classes

class IMaterializationService: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def MaterizalizationBlocked(self) -> bool:
        """ Get: MaterizalizationBlocked(self: IMaterializationService) -> bool """
        ...

    @property
    def SitingBlocked(self) -> bool:
        """ Get: SitingBlocked(self: IMaterializationService) -> bool """
        ...


    def BlockMaterialization(self) -> int:
        """ BlockMaterialization(self: IMaterializationService) -> int """
        ...

    def BlockSiting(self) -> int:
        """ BlockSiting(self: IMaterializationService) -> int """
        ...

    def ChangeMaterializedCaption(self, component:IComponent, componentName:str) -> bool:
        """ ChangeMaterializedCaption(self: IMaterializationService, component: IComponent, componentName: str) -> bool """
        ...

    def DematerializeComponent(self, component:IComponent, parent:object): # -> 
        """ DematerializeComponent(self: IMaterializationService, component: IComponent, parent: object) """
        ...

    def MaterializeComponent(self, component:IComponent, parent:object): # -> 
        """ MaterializeComponent(self: IMaterializationService, component: IComponent, parent: object) """
        ...

    def UnblockMaterialization(self) -> int:
        """ UnblockMaterialization(self: IMaterializationService) -> int """
        ...

    def UnblockSiting(self) -> int:
        """ UnblockSiting(self: IMaterializationService) -> int """
        ...

    def UpdateMaterialization(self, component:IComponent, updatePermanently:bool = ...): # -> 
        """ UpdateMaterialization(self: IMaterializationService, component: IComponent)UpdateMaterialization(self: IMaterializationService, component: IComponent, updatePermanently: bool) """
        ...


