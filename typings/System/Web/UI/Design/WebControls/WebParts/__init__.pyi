# encoding: utf-8
# module System.Web.UI.Design.WebControls.WebParts calls itself WebParts
# from System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.ComponentModel.Design import DesignerActionListCollection

from System.Web.UI.Design import (DesignerAutoFormatCollection, 
    DesignerRegionCollection, EditableDesignerRegion, TemplateGroupCollection)

from System.Web.UI.Design.WebControls import CompositeControlDesigner

from System.Windows.Forms.Design import ControlDesigner


# no functions
# classes

class PartDesigner(CompositeControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ no doc """
    pass

class CatalogPartDesigner(PartDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ CatalogPartDesigner() """
    def GetDesignTimeHtml(self, regions=None) -> str:
        """ GetDesignTimeHtml(self: CatalogPartDesigner) -> str """
        ...


class WebZoneDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ no doc """
    pass

class ToolZoneDesigner(WebZoneDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ ToolZoneDesigner() """
    @property
    def ActionLists(self) -> DesignerActionListCollection:
        """ Get: ActionLists(self: ToolZoneDesigner) -> DesignerActionListCollection """
        ...

    @property
    def ViewInBrowseMode(self):
        ...



class CatalogZoneDesigner(ToolZoneDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ CatalogZoneDesigner() """
    @property
    def AutoFormats(self) -> DesignerAutoFormatCollection:
        """ Get: AutoFormats(self: CatalogZoneDesigner) -> DesignerAutoFormatCollection """
        ...

    @property
    def TemplateGroups(self) -> TemplateGroupCollection:
        """ Get: TemplateGroups(self: CatalogZoneDesigner) -> TemplateGroupCollection """
        ...


    def GetDesignTimeHtml(self, regions:DesignerRegionCollection = ...) -> str:
        """
        GetDesignTimeHtml(self: CatalogZoneDesigner) -> str
        GetDesignTimeHtml(self: CatalogZoneDesigner, regions: DesignerRegionCollection) -> str
        """
        ...

    def GetEditableDesignerRegionContent(self, region:EditableDesignerRegion) -> str:
        """ GetEditableDesignerRegionContent(self: CatalogZoneDesigner, region: EditableDesignerRegion) -> str """
        ...

    def SetEditableDesignerRegionContent(self, region:EditableDesignerRegion, content:str): # -> 
        """ SetEditableDesignerRegionContent(self: CatalogZoneDesigner, region: EditableDesignerRegion, content: str) """
        ...


class ConnectionsZoneDesigner(ToolZoneDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ ConnectionsZoneDesigner() """
    @property
    def AutoFormats(self) -> DesignerAutoFormatCollection:
        """ Get: AutoFormats(self: ConnectionsZoneDesigner) -> DesignerAutoFormatCollection """
        ...


    def GetDesignTimeHtml(self, regions=None) -> str:
        """ GetDesignTimeHtml(self: ConnectionsZoneDesigner) -> str """
        ...


class DeclarativeCatalogPartDesigner(CatalogPartDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ DeclarativeCatalogPartDesigner() """
    @property
    def TemplateGroups(self) -> TemplateGroupCollection:
        """ Get: TemplateGroups(self: DeclarativeCatalogPartDesigner) -> TemplateGroupCollection """
        ...



class EditorPartDesigner(PartDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ EditorPartDesigner() """
    def GetDesignTimeHtml(self, regions=None) -> str:
        """ GetDesignTimeHtml(self: EditorPartDesigner) -> str """
        ...


class EditorZoneDesigner(ToolZoneDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ EditorZoneDesigner() """
    @property
    def AutoFormats(self) -> DesignerAutoFormatCollection:
        """ Get: AutoFormats(self: EditorZoneDesigner) -> DesignerAutoFormatCollection """
        ...

    @property
    def TemplateGroups(self) -> TemplateGroupCollection:
        """ Get: TemplateGroups(self: EditorZoneDesigner) -> TemplateGroupCollection """
        ...


    def GetDesignTimeHtml(self, regions:DesignerRegionCollection = ...) -> str:
        """
        GetDesignTimeHtml(self: EditorZoneDesigner) -> str
        GetDesignTimeHtml(self: EditorZoneDesigner, regions: DesignerRegionCollection) -> str
        """
        ...

    def GetEditableDesignerRegionContent(self, region:EditableDesignerRegion) -> str:
        """ GetEditableDesignerRegionContent(self: EditorZoneDesigner, region: EditableDesignerRegion) -> str """
        ...

    def SetEditableDesignerRegionContent(self, region:EditableDesignerRegion, content:str): # -> 
        """ SetEditableDesignerRegionContent(self: EditorZoneDesigner, region: EditableDesignerRegion, content: str) """
        ...


class PageCatalogPartDesigner(CatalogPartDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ PageCatalogPartDesigner() """
    pass

class ProxyWebPartManagerDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ ProxyWebPartManagerDesigner() """
    pass

class WebPartDesigner(PartDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ WebPartDesigner() """
    pass

class WebPartManagerDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ WebPartManagerDesigner() """
    pass

class WebPartZoneBaseDesigner(WebZoneDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ WebPartZoneBaseDesigner() """
    pass

class WebPartZoneDesigner(WebPartZoneBaseDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ WebPartZoneDesigner() """
    @property
    def AutoFormats(self) -> DesignerAutoFormatCollection:
        """ Get: AutoFormats(self: WebPartZoneDesigner) -> DesignerAutoFormatCollection """
        ...

    @property
    def TemplateGroups(self) -> TemplateGroupCollection:
        """ Get: TemplateGroups(self: WebPartZoneDesigner) -> TemplateGroupCollection """
        ...


    def GetDesignTimeHtml(self, regions:DesignerRegionCollection = ...) -> str:
        """
        GetDesignTimeHtml(self: WebPartZoneDesigner) -> str
        GetDesignTimeHtml(self: WebPartZoneDesigner, regions: DesignerRegionCollection) -> str
        """
        ...

    def GetEditableDesignerRegionContent(self, region:EditableDesignerRegion) -> str:
        """ GetEditableDesignerRegionContent(self: WebPartZoneDesigner, region: EditableDesignerRegion) -> str """
        ...

    def SetEditableDesignerRegionContent(self, region:EditableDesignerRegion, content:str): # -> 
        """ SetEditableDesignerRegionContent(self: WebPartZoneDesigner, region: EditableDesignerRegion, content: str) """
        ...


