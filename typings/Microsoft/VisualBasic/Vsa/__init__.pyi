# encoding: utf-8
# module Microsoft.VisualBasic.Vsa calls itself Vsa
# from Microsoft.VisualBasic.Vsa, Version=8.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Vsa import (IVsaCodeItem, IVsaEngine, IVsaError, 
    IVsaGlobalItem, IVsaItem, IVsaItems, IVsaReferenceItem)

from System.Collections import IEnumerator

"""The following names are not found in the module: field#
"""

# no functions
# classes

class VsaItem(IVsaItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def _item(self) -> IVsaItem:
        """
        Get: _item(self: VsaItem) -> IVsaItem
        Set: _item(self: VsaItem) = value
        """
        ...



class VsaCodeItem(IVsaCodeItem, VsaItem): # skipped bases: <type 'IVsaItem'>, <type 'object'>
    """ no doc """
    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, item: IVsaCodeItem) """
        ...


class VsaCompilerError(IVsaError): # skipped bases: <type 'object'>
    """ no doc """
    pass

class VsaEngine(IVsaEngine): # skipped bases: <type 'object'>
    """ VsaEngine() """
    def CheckEngine(self, *args): #cannot find CLR method
        """ CheckEngine(self: VsaEngine) """
        ...

    def CreateEngine(self, *args): #cannot find CLR method
        """ CreateEngine(self: VsaEngine) """
        ...

    def Dispose(self, *args): #cannot find CLR method
        """ Dispose(self: VsaEngine, disposing: bool) """
        ...

    @staticmethod
    def GetExceptionToThrow(e:Exception) -> Exception:
        """ GetExceptionToThrow(e: Exception) -> Exception """
        ...

    m_Items = ...
    _baseEngine = ...
    _engineClosed = ...


class VsaGlobalItem(VsaItem, IVsaGlobalItem): # skipped bases: <type 'IVsaItem'>, <type 'object'>
    """ no doc """
    pass

class VsaItems(IVsaItems): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def AddCodeItemWrapper(self, *args): #cannot find CLR method
        """ AddCodeItemWrapper(self: VsaItems, item: IVsaItem) -> VsaItem """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: VsaItems) -> IEnumerator """
        ...

    def GetItemWrapper(self, *args): #cannot find CLR method
        """ GetItemWrapper(self: VsaItems, item: IVsaItem) -> IVsaItem """
        ...

    m_ItemCollection = ...


class VsaItemsEnumerator(IEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    pass

class VsaReferenceItem(IVsaReferenceItem, VsaItem): # skipped bases: <type 'IVsaItem'>, <type 'object'>
    """ no doc """
    pass

