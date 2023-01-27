# encoding: utf-8
# module System.Windows.Forms.ComponentModel.Com2Interop calls itself Com2Interop
# from System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Win32 import RegistryKey

from System import Guid, IntPtr

"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class Com2Variant: # skipped bases: <type 'object'>, <type 'object'>
    """ Com2Variant() """
    pass

class ICom2PropertyPageDisplayService: # skipped bases: <type 'object'>
    """ no doc """
    def ShowPropertyPage(self, title:str, component:object, dispid:int, pageGuid:Guid, parentHandle:IntPtr): # -> 
        """ ShowPropertyPage(self: ICom2PropertyPageDisplayService, title: str, component: object, dispid: int, pageGuid: Guid, parentHandle: IntPtr) """
        ...


class IComPropertyBrowser: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def InPropertySet(self) -> bool:
        """ Get: InPropertySet(self: IComPropertyBrowser) -> bool """
        ...


    def DropDownDone(self): # -> 
        """ DropDownDone(self: IComPropertyBrowser) """
        ...

    def EnsurePendingChangesCommitted(self) -> bool:
        """ EnsurePendingChangesCommitted(self: IComPropertyBrowser) -> bool """
        ...

    def HandleF4(self): # -> 
        """ HandleF4(self: IComPropertyBrowser) """
        ...

    def LoadState(self, key:RegistryKey): # -> 
        """ LoadState(self: IComPropertyBrowser, key: RegistryKey) """
        ...

    def SaveState(self, key:RegistryKey): # -> 
        """ SaveState(self: IComPropertyBrowser, key: RegistryKey) """
        ...

    ComComponentNameChanged = ...


