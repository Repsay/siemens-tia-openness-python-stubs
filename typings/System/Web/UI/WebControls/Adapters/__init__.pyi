# encoding: utf-8
# module System.Web.UI.WebControls.Adapters calls itself Adapters
# from System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Web.UI import IPostBackEventHandler

from System.Web.UI.Adapters import ControlAdapter


# no functions
# classes

class WebControlAdapter(ControlAdapter): # skipped bases: <type 'object'>
    """ WebControlAdapter() """
    @property
    def IsEnabled(self):
        ...


    def RenderBeginTag(self, *args): #cannot find CLR method
        """ RenderBeginTag(self: WebControlAdapter, writer: HtmlTextWriter) """
        ...

    def RenderContents(self, *args): #cannot find CLR method
        """ RenderContents(self: WebControlAdapter, writer: HtmlTextWriter) """
        ...

    def RenderEndTag(self, *args): #cannot find CLR method
        """ RenderEndTag(self: WebControlAdapter, writer: HtmlTextWriter) """
        ...


class DataBoundControlAdapter(WebControlAdapter): # skipped bases: <type 'object'>
    """ DataBoundControlAdapter() """
    def PerformDataBinding(self, *args): #cannot find CLR method
        """ PerformDataBinding(self: DataBoundControlAdapter, data: IEnumerable) """
        ...


class HideDisabledControlAdapter(WebControlAdapter): # skipped bases: <type 'object'>
    """ HideDisabledControlAdapter() """
    pass

class HierarchicalDataBoundControlAdapter(WebControlAdapter): # skipped bases: <type 'object'>
    """ HierarchicalDataBoundControlAdapter() """
    def PerformDataBinding(self, *args): #cannot find CLR method
        """ PerformDataBinding(self: HierarchicalDataBoundControlAdapter) """
        ...


class MenuAdapter(WebControlAdapter, IPostBackEventHandler): # skipped bases: <type 'object'>
    """ MenuAdapter() """
    def RenderItem(self, *args): #cannot find CLR method
        """ RenderItem(self: MenuAdapter, writer: HtmlTextWriter, item: MenuItem, position: int) """
        ...


