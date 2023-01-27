# encoding: utf-8
# module System.Xaml.Hosting.Configuration calls itself Configuration
# from System.Xaml.Hosting, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Configuration import (ConfigurationElement, 
    ConfigurationElementCollection, ConfigurationSection, 
    ConfigurationSectionGroup)

from typing import Self


# no functions
# classes

class HandlerElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    HandlerElement()
    HandlerElement(xamlType: str, handlerType: str)
    """
    @property
    def HttpHandlerType(self) -> str:
        """
        Get: HttpHandlerType(self: HandlerElement) -> str
        Set: HttpHandlerType(self: HandlerElement) = value
        """
        ...

    @property
    def XamlRootElementType(self) -> str:
        """
        Get: XamlRootElementType(self: HandlerElement) -> str
        Set: XamlRootElementType(self: HandlerElement) = value
        """
        ...


    def __new__(cls, xamlType:str = ..., handlerType:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, xamlType: str, handlerType: str)
        """
        ...


class HandlerElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ HandlerElementCollection() """
    def Add(self, handlerElement:HandlerElement): # -> 
        """ Add(self: HandlerElementCollection, handlerElement: HandlerElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: HandlerElementCollection) """
        ...

    def Remove(self, *__args:HandlerElement): # -> 
        """ Remove(self: HandlerElementCollection, handlerElement: HandlerElement)Remove(self: HandlerElementCollection, xamlRootElementType: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: HandlerElementCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class XamlHostingSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ XamlHostingSection() """
    @property
    def Handlers(self) -> HandlerElementCollection:
        """ Get: Handlers(self: XamlHostingSection) -> HandlerElementCollection """
        ...



class XamlHostingSectionGroup(ConfigurationSectionGroup): # skipped bases: <type 'object'>
    """ XamlHostingSectionGroup() """
    @property
    def XamlHostingSection(self) -> XamlHostingSection:
        """ Get: XamlHostingSection(self: XamlHostingSectionGroup) -> XamlHostingSection """
        ...



