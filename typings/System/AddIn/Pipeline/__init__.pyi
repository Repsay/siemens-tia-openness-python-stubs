# encoding: utf-8
# module System.AddIn.Pipeline calls itself Pipeline
# from System.Windows.Presentation, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.AddIn.Contract, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.AddIn, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (AppDomain, Array, Attribute, Converter, IDisposable, 
    MarshalByRefObject)

from System.AddIn.Contract import (IContract, IListContract, 
    INativeHandleContract)

from System.AddIn.Hosting import PipelineStoreLocation

from System.Collections import IList

from System.Runtime.Remoting.Lifetime import ISponsor

from typing import Self

"""The following names are not found in the module: (ContractHandle, 
    FrameworkElement, TView)
"""

# no functions
# classes

class AddInAdapterAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AddInAdapterAttribute() """
    pass

class AddInBaseAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AddInBaseAttribute() """
    @property
    def ActivatableAs(self) -> Array:
        """
        Get: ActivatableAs(self: AddInBaseAttribute) -> Array[Type]
        Set: ActivatableAs(self: AddInBaseAttribute) = value
        """
        ...



class AddInContractAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AddInContractAttribute() """
    pass

class CollectionAdapters: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ToIList(collection:IListContract, contractViewAdapter:Converter = ..., viewContractAdapter:Converter = ...) -> IList:
        """
        ToIList[(TContract, TView)](collection: IListContract[TContract], contractViewAdapter: Converter[TContract, TView], viewContractAdapter: Converter[TView, TContract]) -> IList[TView]
        ToIList[T](collection: IListContract[T]) -> IList[T]
        """
        ...

    @staticmethod
    def ToIListContract(collection:IList, viewContractAdapter:Converter = ..., contractViewAdapter:Converter = ...) -> IListContract:
        """
        ToIListContract[(TView, TContract)](collection: IList[TView], viewContractAdapter: Converter[TView, TContract], contractViewAdapter: Converter[TContract, TView]) -> IListContract[TContract]
        ToIListContract[T](collection: IList[T]) -> IListContract[T]
        """
        ...

    __all__: list = ...


class ContractAdapter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ContractToViewAdapter(contract, *__args:PipelineStoreLocation): # -> TView # Not found arg types: {'contract': 'ContractHandle'}
        """
        ContractToViewAdapter[TView](contract: ContractHandle, location: PipelineStoreLocation) -> TView
        ContractToViewAdapter[TView](contract: ContractHandle, pipelineRoot: str) -> TView
        """
        ...

    @staticmethod
    def ViewToContractAdapter(view:object): # -> ContractHandle
        """ ViewToContractAdapter(view: object) -> ContractHandle """
        ...

    __all__: list = ...


class ContractBase(MarshalByRefObject, ISponsor, IContract): # skipped bases: <type 'object'>
    """ ContractBase() """
    def OnFinalRevoke(self, *args): #cannot find CLR method
        """ OnFinalRevoke(self: ContractBase) """
        ...


class ContractHandle(IDisposable): # skipped bases: <type 'object'>
    """ ContractHandle(contract: IContract) """
    @property
    def Contract(self) -> IContract:
        """ Get: Contract(self: ContractHandle) -> IContract """
        ...


    @staticmethod
    def AppDomainOwner(domain:AppDomain) -> IContract:
        """ AppDomainOwner(domain: AppDomain) -> IContract """
        ...

    @staticmethod
    def ContractOwnsAppDomain(contract:IContract, domain:AppDomain) -> bool:
        """ ContractOwnsAppDomain(contract: IContract, domain: AppDomain) -> bool """
        ...


class FrameworkElementAdapters: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ContractToViewAdapter(nativeHandleContract:INativeHandleContract): # -> FrameworkElement
        """ ContractToViewAdapter(nativeHandleContract: INativeHandleContract) -> FrameworkElement """
        ...

    @staticmethod
    def ViewToContractAdapter(root) -> INativeHandleContract: # Not found arg types: {'root': 'FrameworkElement'}
        """ ViewToContractAdapter(root: FrameworkElement) -> INativeHandleContract """
        ...

    __all__: list = ...


class HostAdapterAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ HostAdapterAttribute() """
    pass

class QualificationDataAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ QualificationDataAttribute(name: str, value: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: QualificationDataAttribute) -> str """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: QualificationDataAttribute) -> str """
        ...


    def __new__(cls, name:str, value:str) -> Self:
        """ __new__(cls: type, name: str, value: str) """
        ...


