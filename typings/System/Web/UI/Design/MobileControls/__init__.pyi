# encoding: utf-8
# module System.Web.UI.Design.MobileControls calls itself MobileControls
# from System.Web.Mobile, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Web.UI import Control


# no functions
# classes

class IMobileDesigner: # skipped bases: <type 'object'>
    """ no doc """
    def UpdateRendering(self): # -> 
        """ UpdateRendering(self: IMobileDesigner) """
        ...


class IMobileWebFormServices: # skipped bases: <type 'object'>
    """ no doc """
    def ClearUndoStack(self): # -> 
        """ ClearUndoStack(self: IMobileWebFormServices) """
        ...

    def GetCache(self, controlID:str, key:object) -> object:
        """ GetCache(self: IMobileWebFormServices, controlID: str, key: object) -> object """
        ...

    def RefreshPageView(self): # -> 
        """ RefreshPageView(self: IMobileWebFormServices) """
        ...

    def SetCache(self, controlID:str, key:object, value:object): # -> 
        """ SetCache(self: IMobileWebFormServices, controlID: str, key: object, value: object) """
        ...

    def UpdateRenderingRecursive(self, rootControl:Control): # -> 
        """ UpdateRenderingRecursive(self: IMobileWebFormServices, rootControl: Control) """
        ...


class MobileResource: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetString(name:str) -> str:
        """ GetString(name: str) -> str """
        ...


# variables with complex values

