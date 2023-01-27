# encoding: utf-8
# module System.Web.UI.Adapters calls itself Adapters
# from System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Collections import ICollection

from System.Collections.Specialized import (NameValueCollection, 
    StringCollection)

from System.Web.UI import HtmlTextWriter, PageStatePersister

from System.Windows.Forms import RadioButton


# no functions
# classes

class ControlAdapter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Browser(self):
        ...

    @property
    def Control(self):
        ...

    @property
    def Page(self):
        ...

    @property
    def PageAdapter(self):
        ...


    def BeginRender(self, *args): #cannot find CLR method
        """ BeginRender(self: ControlAdapter, writer: HtmlTextWriter) """
        ...

    def CreateChildControls(self, *args): #cannot find CLR method
        """ CreateChildControls(self: ControlAdapter) """
        ...

    def EndRender(self, *args): #cannot find CLR method
        """ EndRender(self: ControlAdapter, writer: HtmlTextWriter) """
        ...

    def LoadAdapterControlState(self, *args): #cannot find CLR method
        """ LoadAdapterControlState(self: ControlAdapter, state: object) """
        ...

    def LoadAdapterViewState(self, *args): #cannot find CLR method
        """ LoadAdapterViewState(self: ControlAdapter, state: object) """
        ...

    def OnInit(self, *args): #cannot find CLR method
        """ OnInit(self: ControlAdapter, e: EventArgs) """
        ...

    def OnLoad(self, *args): #cannot find CLR method
        """ OnLoad(self: ControlAdapter, e: EventArgs) """
        ...

    def OnPreRender(self, *args): #cannot find CLR method
        """ OnPreRender(self: ControlAdapter, e: EventArgs) """
        ...

    def OnUnload(self, *args): #cannot find CLR method
        """ OnUnload(self: ControlAdapter, e: EventArgs) """
        ...

    def Render(self, *args): #cannot find CLR method
        """ Render(self: ControlAdapter, writer: HtmlTextWriter) """
        ...

    def RenderChildren(self, *args): #cannot find CLR method
        """ RenderChildren(self: ControlAdapter, writer: HtmlTextWriter) """
        ...

    def SaveAdapterControlState(self, *args): #cannot find CLR method
        """ SaveAdapterControlState(self: ControlAdapter) -> object """
        ...

    def SaveAdapterViewState(self, *args): #cannot find CLR method
        """ SaveAdapterViewState(self: ControlAdapter) -> object """
        ...


class PageAdapter(ControlAdapter): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CacheVaryByHeaders(self) -> StringCollection:
        """ Get: CacheVaryByHeaders(self: PageAdapter) -> StringCollection """
        ...

    @property
    def CacheVaryByParams(self) -> StringCollection:
        """ Get: CacheVaryByParams(self: PageAdapter) -> StringCollection """
        ...

    @property
    def ClientState(self):
        ...


    def DeterminePostBackMode(self) -> NameValueCollection:
        """ DeterminePostBackMode(self: PageAdapter) -> NameValueCollection """
        ...

    def DeterminePostBackModeUnvalidated(self) -> NameValueCollection:
        """ DeterminePostBackModeUnvalidated(self: PageAdapter) -> NameValueCollection """
        ...

    def GetPostBackFormReference(self, *args): #cannot find CLR method
        """ GetPostBackFormReference(self: PageAdapter, formId: str) -> str """
        ...

    def GetRadioButtonsByGroup(self, groupName:str) -> ICollection:
        """ GetRadioButtonsByGroup(self: PageAdapter, groupName: str) -> ICollection """
        ...

    def GetStatePersister(self) -> PageStatePersister:
        """ GetStatePersister(self: PageAdapter) -> PageStatePersister """
        ...

    def RegisterRadioButton(self, radioButton:RadioButton): # -> 
        """ RegisterRadioButton(self: PageAdapter, radioButton: RadioButton) """
        ...

    def RenderBeginHyperlink(self, writer:HtmlTextWriter, targetUrl:str, encodeUrl:bool, softkeyLabel:str, accessKey:str = ...): # -> 
        """ RenderBeginHyperlink(self: PageAdapter, writer: HtmlTextWriter, targetUrl: str, encodeUrl: bool, softkeyLabel: str)RenderBeginHyperlink(self: PageAdapter, writer: HtmlTextWriter, targetUrl: str, encodeUrl: bool, softkeyLabel: str, accessKey: str) """
        ...

    def RenderEndHyperlink(self, writer:HtmlTextWriter): # -> 
        """ RenderEndHyperlink(self: PageAdapter, writer: HtmlTextWriter) """
        ...

    def RenderPostBackEvent(self, writer:HtmlTextWriter, target:str, argument:str, softkeyLabel:str, text:str, postUrl:str = ..., accessKey:str = ...): # -> 
        """ RenderPostBackEvent(self: PageAdapter, writer: HtmlTextWriter, target: str, argument: str, softkeyLabel: str, text: str)RenderPostBackEvent(self: PageAdapter, writer: HtmlTextWriter, target: str, argument: str, softkeyLabel: str, text: str, postUrl: str, accessKey: str) """
        ...

    def TransformText(self, text:str) -> str:
        """ TransformText(self: PageAdapter, text: str) -> str """
        ...


