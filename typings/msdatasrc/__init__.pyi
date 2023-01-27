# encoding: utf-8
# module msdatasrc
# from MSDATASRC, Version=7.0.3300.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Guid

from typing import Tuple as Tuple_


# no functions
# classes

class DataSource: # skipped bases: <type 'object'>
    """ no doc """
    def addDataSourceListener(self, pDSL:DataSourceListener): # -> 
        """ addDataSourceListener(self: DataSource, pDSL: DataSourceListener) """
        ...

    def getDataMember(self, bstrDM:str, riid:Guid) -> Tuple_[object, Guid]:
        """ getDataMember(self: DataSource, bstrDM: str, riid: Guid) -> (object, Guid) """
        ...

    def getDataMemberCount(self) -> int:
        """ getDataMemberCount(self: DataSource) -> int """
        ...

    def getDataMemberName(self, lIndex:int) -> str:
        """ getDataMemberName(self: DataSource, lIndex: int) -> str """
        ...

    def removeDataSourceListener(self, pDSL:DataSourceListener): # -> 
        """ removeDataSourceListener(self: DataSource, pDSL: DataSourceListener) """
        ...


class DataSourceListener: # skipped bases: <type 'object'>
    """ no doc """
    def dataMemberAdded(self, bstrDM:str): # -> 
        """ dataMemberAdded(self: DataSourceListener, bstrDM: str) """
        ...

    def dataMemberChanged(self, bstrDM:str): # -> 
        """ dataMemberChanged(self: DataSourceListener, bstrDM: str) """
        ...

    def dataMemberRemoved(self, bstrDM:str): # -> 
        """ dataMemberRemoved(self: DataSourceListener, bstrDM: str) """
        ...


