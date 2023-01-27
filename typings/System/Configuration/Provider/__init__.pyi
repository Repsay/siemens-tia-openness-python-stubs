# encoding: utf-8
# module System.Configuration.Provider calls itself Provider
# from System.Configuration, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Collections import ICollection, IEnumerator

from System.Collections.Specialized import NameValueCollection

"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class ProviderBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Description(self) -> str:
        """ Get: Description(self: ProviderBase) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ProviderBase) -> str """
        ...


    def Initialize(self, name:str, config:NameValueCollection): # -> 
        """ Initialize(self: ProviderBase, name: str, config: NameValueCollection) """
        ...


class ProviderCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ ProviderCollection() """
    def Add(self, provider:ProviderBase): # -> 
        """ Add(self: ProviderCollection, provider: ProviderBase) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ProviderCollection) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ProviderCollection) -> IEnumerator """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: ProviderCollection, name: str) """
        ...

    def SetReadOnly(self): # -> 
        """ SetReadOnly(self: ProviderCollection) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class ProviderException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ProviderException()
    ProviderException(message: str)
    ProviderException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


